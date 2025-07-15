import time
import psutil
import requests

# 检查QQ是否正在运行
def is_qq_running():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"{proc}")
        if 'qq' in proc.info['name'].lower():
            return True
        else:
            return False    

# 发送企业微信消息
def send_wechat_message(webhook_url, message):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message,
            "mentioned_list": ["@all"]  # 可选：指定@的成员
        }
    }
    response = requests.post(webhook_url, headers=headers, json=data)
    print("done")
    return response.status_code

# 主循环
def monitor_qq(webhook_url, check_interval=1):
    while True:
        if not is_qq_running():
            send_wechat_message(webhook_url, "QQ进程已停止，请检查！")
        time.sleep(check_interval)  # 每隔一段时间检查一次

# 配置企业微信机器人的Webhook地址
webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=67e62638-af00-4879-a146-b468fd718a30"

# 开始监控
monitor_qq(webhook_url)

