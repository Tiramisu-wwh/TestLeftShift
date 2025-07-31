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

# 检查环境变量是否设置
if not secret or not webhook:
    raise ValueError("DING_SECRET 和 DING_WEBHOOK 环境变量必须设置")

timestamp = str(round(time.time() * 1000))
string_to_sign = '{}\n{}'.format(timestamp, secret)
hmac_code = hmac.new(secret.encode('utf-8'), string_to_sign.encode('utf-8'), digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

send_url = f"{webhook}&timestamp={timestamp}&sign={sign}"

headers = {
    "Content-Type": "application/json"
}

# 读取报告内容
try:
    with open("report.md", "r", encoding="utf-8") as f:
        report_content = f.read()
        # 截断过长的报告内容，钉钉消息有长度限制
        if len(report_content) > 2000:
            report_content = report_content[:2000] + "\n... 报告内容过长，已截断 ..."
except FileNotFoundError:
    report_content = "❌ 测试报告文件未找到"
except Exception as e:
    report_content = f"❌ 读取报告失败: {str(e)}"

data = {
    "msgtype": "text",
    "text": {
        "content": f"📊 接口自动化测试报告\n{report_content}"
    }
}

response = requests.post(send_url, headers=headers, json=data)
print(response.status_code)
print(response.text)
