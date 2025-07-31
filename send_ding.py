import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import os

# 替换为你的钉钉 webhook 和加签密钥
secret = os.environ.get('DING_SECRET')
webhook = os.environ.get('DING_WEBHOOK')

timestamp = str(round(time.time() * 1000))
string_to_sign = '{}\n{}'.format(timestamp, secret)
hmac_code = hmac.new(secret.encode('utf-8'), string_to_sign.encode('utf-8'), digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

send_url = f"{webhook}&timestamp={timestamp}&sign={sign}"

headers = {
    "Content-Type": "application/json"
}
data = {
    "msgtype": "text",
    "text": {
        "content": "✅ Python 本地钉钉签名测试发送成功！"
    }
}

response = requests.post(send_url, headers=headers, json=data)
print(response.status_code)
print(response.text)
