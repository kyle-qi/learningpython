import yfinance as yf

# 获取上证指数的 Ticker 对象
shanghai_index = yf.Ticker("000001.SS")

# 获取最近20个交易日的历史数据
# period='1mo' 表示最近一个月的数据，可以根据实际需要调整为更长的时间窗口
data = shanghai_index.history(period="3mo")

# 获取最近20个交易日的日内最高点数据
# 如果时间跨度超过20天，确保只获取20个交易日的数据
recent_highs = data['High'].tail(20)

# 输出最近20个交易日的日内最高点
print(recent_highs)