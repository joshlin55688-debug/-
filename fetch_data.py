import yfinance as yf
import json
import os

# 1. 這裡填入你想要追蹤的股票清單
# 美股直接輸入代號，台股上市請加 .TW，上櫃請加 .TWO
symbols = ["AAPL", "TSLA", "NVDA", "2330.TW", "0050.TW"]

# 建立一個 data 資料夾來放生成的 json 檔
os.makedirs("data", exist_ok=True)

for symbol in symbols:
    print(f"正在抓取 {symbol} 的資料...")
    try:
        # 抓取過去一年的歷史資料
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="1y")
        
        data_list = []
        for index, row in df.iterrows():
            # 將時間格式化為 Lightweight Charts 支援的 YYYY-MM-DD
            date_str = index.strftime('%Y-%m-%d')
            data_list.append({
                "time": date_str,
                "open": round(row["Open"], 2),
                "high": round(row["High"], 2),
                "low": round(row["Low"], 2),
                "close": round(row["Close"], 2)
            })
            
        # 存成 JSON 檔案 (例如 data/AAPL.json)
        with open(f"data/{symbol}.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f)
            
    except Exception as e:
        print(f"抓取 {symbol} 失敗: {e}")

print("所有資料更新完畢！")
