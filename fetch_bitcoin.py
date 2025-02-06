import requests
from datetime import datetime

# API URL
API_URL = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"

# API에서 데이터 가져오기
def fetch_btc_price():
    response = requests.get(API_URL)
    data = response.json()

    # 필요한 정보 추출
    price = data["quotes"]["USD"]["price"]
    change_1h = data["quotes"]["USD"]["percent_change_1h"]
    change_24h = data["quotes"]["USD"]["percent_change_24h"]
    ath_price = data["quotes"]["USD"]["ath_price"]
    percent_from_ath = data["quotes"]["USD"]["percent_from_price_ath"]

    return {
        "price": price,
        "change_1h": change_1h,
        "change_24h": change_24h,
        "ath_price": ath_price,
        "percent_from_ath": percent_from_ath,
    }

# Markdown 업데이트
def update_markdown(btc_data):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    markdown_content = f"""# 🪙 비트코인 가격 업데이트 ({now})

| 항목                | 값 |
|--------------------|----------------|
| 💰 현재 가격 (USD) | ${btc_data["price"]:.2f} |
| ⏳ 1시간 변동률    | {btc_data["change_1h"]:.2f}% |
| 📆 24시간 변동률   | {btc_data["change_24h"]:.2f}% |
| 🔝 역대 최고가 (ATH) | ${btc_data["ath_price"]:.2f} |
| 📉 ATH 대비 하락률 | {btc_data["percent_from_ath"]:.2f}% |

🔄 **이 파일은 GitHub Actions에 의해 자동으로 업데이트됩니다.**
"""

    with open("bitcoin_prices.md", "w") as f:
        f.write(markdown_content)

# 실행
if __name__ == "__main__":
    btc_data = fetch_btc_price()
    update_markdown(btc_data)
