import pandas as pd
from datetime import datetime, timedelta

# 读取CSV文件
df = pd.read_csv("10yuan_data.csv")

# 创建一个起始时间
start_time = datetime(2022, 1, 1, 0, 0)

# 定义时间增量为30分钟
time_increment = timedelta(minutes=30)

# 将第一列编号转换为时间戳数据
df['Time'] = [(start_time + i * time_increment).strftime('%Y-%m-%d %H:%M') for i in range(len(df))]

print(df)
# 保存修改后的数据到新的CSV文件
df.to_csv("10yuan_data.csv", index=False)
