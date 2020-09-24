#!/usr/bin/python
# coding=UTF-8

import requests
import json

def text_msg(msg):
    res = {
        "msg_type": "text", 
        "content": {"text": msg}
    }
    return json.dumps(res)

def post_msg(txt, tip, url):
    res = {
            "msg_type": "post", 
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "打包成功", 
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": txt
                                }, {
                                    "tag": "a",
                                    "text": tip,
                                    "href": url
                                }
                            ]
                        ]
                    }
                }
            }
        }
    return json.dumps(res)

def request(data):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/b7a09d17-512d-426d-8d4d-233cf0931bca"
    r = requests.post(url, data = data)
    print r.status_code
    print r.content

data = post_msg("注意: ", "最新打包地址", "http://www.baidu.com")
request(data)