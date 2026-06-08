import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

try:
    data = requests.get(url, timeout=20).json()

    score = int(data["fear_and_greed"]["score"])

    if score <= 100:
        message = (
            f"🚨 Fear & Greed Alert\n\n"
            f"현재 지수: {score}\n"
            f"공포 구간 진입"
        )

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=20
        )

except Exception as e:
    print(e)
