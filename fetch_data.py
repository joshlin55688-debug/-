import yfinance as yf
import pandas as pd
import os
import json

# 1. 設定你想要追蹤的股票代號 (你可以隨時在這裡新增)
symbols = ['AAPL', 'TSLA', '2330.TW', '0050.TW']

# 2. 確保 data 資料夾存在，如果沒有就自動建立
os.makedirs('data', exist_ok=True)

for symbol in symbols:
    print(f"正在抓取 {symbol} ...")
    try:
        # 抓取過去 1 年的歷史資料
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="1y")

        if df.empty:
            print(f"警告: {symbol} 沒有抓到資料，可能代號錯誤或無交易。")
            continue

        # 3. 整理資料格式，符合前端圖表的需求 (time, open, high, low, close)
        data_list = []
        for index, row in df.iterrows():
            data_list.append({
                "time": index.strftime('%Y-%m-%d'),
                "open": round(row['Open'], 2),
                "high": round(row['High'], 2),
                "low": round(row['Low'], 2),
                "close": round(row['Close'], 2)
            })

        # 4. 存成 JSON 檔案放入 data 資料夾
        file_path = f"data/{symbol}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        
        print(f"成功儲存 -> {file_path}")

    except Exception as e:
        print(f"抓取 {symbol} 時發生錯誤: {e}")

print("✅ 所有資料抓取完畢！")
