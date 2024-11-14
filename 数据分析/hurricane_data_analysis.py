

import pandas as pd

# 使用绝对路径读取文件
data = pd.read_csv('/Users/kyleqi/数据分析/orders_export_1.csv')
'''
print(data.head())
print(data.info())
print(data.describe())
'''

hurricane_data = data[
    data['Lineitem name'].str.contains('hurricane', case=False, na=False)
    ]
title_counts = hurricane_data.groupby('Lineitem name').size()

# 仅对筛选后的 hurricane_data 进行拆分
hurricane_data[['Model', 'Power', 'Type', 'Bundle']] = hurricane_data['Lineitem name'].str.split(' / ', expand=True)

# 打印拆分后的 hurricane_data
print(hurricane_data[['Model', 'Power', 'Type', 'Bundle']].head())


'''
hurricane_data_eu = data[
    data['Lineitem name'].str.contains('hurricane', case=False, na=False) & 
    data['Lineitem name'].str.contains('eu', case=False, na=False) &
    ~data['Lineitem name'].str.contains('Final payment', case=False, na=False)
    ]
title_counts_eu = hurricane_data_eu.groupby('Lineitem name').size()

hurricane_data_us = data[
    data['Lineitem name'].str.contains('hurricane', case=False, na=False) & 
    data['Lineitem name'].str.contains('us', case=False, na=False) &
    ~data['Lineitem name'].str.contains('Final payment', case=False, na=False)
    ]
title_counts_us = hurricane_data_eu.groupby('Lineitem name').size()

hurricane_data_ = data[
    data['Lineitem name'].str.contains('hurricane', case=False, na=False) & 
    data['Lineitem name'].str.contains('eu', case=False, na=False) &
    ~data['Lineitem name'].str.contains('Final payment', case=False, na=False)
    ]
title_counts_eu = hurricane_data_eu.groupby('Lineitem name').size()

print(title_counts_eu)

# sales_by_province = hurricane_data.groupby('shipping province name').size()

'''
'''
import matplotlib.pyplot as plt
sales_by_province.plot(kind='bar')
plt.xlabel('Province')
plt.ylabel('Sales Count')
plt.title('Sales by Province')
plt.show()
'''