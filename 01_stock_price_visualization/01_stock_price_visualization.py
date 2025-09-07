import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

days = 20
tickers = {
    "apple": "AAPL",
    "facebook": "FB",
    "google": "GOOGL",
    "microsoft": "MSFT",
    "netflix": "NFLX",
    "amazon": "AMZN"
}

# 株価取得関数
def get_data(days, tickers):
    
    # 空のデータフレームを用意
    df = pd.DataFrame()

    for company in tickers.keys():

        # 指定日数分の株価取得
        tkr = tickers[company]
        stock_price = yf.Ticker(tkr)
        hist = stock_price.history(period=f'{days}d')

        # 日付フォーマット修正
        hist.index = hist.index.strftime('%d %B %Y')

        # データを終値のみとする
        hist = hist[['Close']]

        # カラム名変更
        hist.columns = [company]

        # 行列変換
        hist = hist.T

        # インデックスのカラム名を変更
        hist.index.name = 'Company'

        # データフレームに追加
        df = pd.concat([df, hist])

    return df

df = get_data(days, tickers)
df
