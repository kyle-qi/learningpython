import yfinance as yf
import matplotlib.pyplot as plt

# 下载特斯拉的实时数据，包括盘前数据
ticker = yf.Ticker("TSLA")
data = ticker.history(period="1d", interval="1m", prepost=True)

# 获取总股本信息（注意：总股本可能是动态的，建议定期查询）
shares_outstanding = ticker.info['sharesOutstanding']

# 计算总市值
data['Market Cap'] = data['Close'] * shares_outstanding

# 绘制价格和总市值随时间变化的折线图
plt.figure(figsize=(10, 6))

# 绘制收盘价格
plt.plot(data.index, data['Close'], label='Close Price', color='blue')

# 绘制总市值
plt.plot(data.index, data['Market Cap'], label='Market Cap', color='green')

# 添加图表标题和标签
plt.title('Tesla Price and Market Cap Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD) / Market Cap (USD)')
plt.xticks(rotation=45)  # 旋转x轴标签，使时间标签更容易阅读

# 添加图例
plt.legend()

# 显示图表
plt.tight_layout()  # 自动调整布局以防止标签重叠
plt.show()

print(data)