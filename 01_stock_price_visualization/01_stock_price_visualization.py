import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# 取得日数
days = 20

# ティッカーシンボル指定で株価を取得する
aapl = yf.Ticker('AAPL')

# 指定日数分のデータ取得
hist_aapl = aapl.history(period=f'{days}d')

# 行列数を確認
# hist_aapl.shape
# 列定義を確認
# hist_aapl.columns
# 日付がindexになっているため、リセットしてみる
# r_hist = hist_aapl.reset_index()
# r_hist

# 日付フォーマット修正
hist_aapl.index = hist_aapl.index.strftime('%d %B %Y')

# データを終値のみとする
hist_aapl = hist_aapl[['Close']]

# カラム名変更
hist_aapl.columns = ['apple']

# 行列変換
hist_aapl = hist_aapl.T

# インデックスのカラム名を変更
hist_aapl.index.name = 'Company'

# データ表示
hist_aapl
