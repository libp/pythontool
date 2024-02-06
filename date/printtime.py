import datetime

current_time = datetime.datetime.now()
timestamp = current_time.timestamp()
print("当前时间（秒数）：", int(timestamp))
milliseconds = int(timestamp * 1000)
print("当前时间（毫秒数）：", milliseconds)

milliseconds = 1698648360000
timestamp = milliseconds / 1000
datetime_obj = datetime.datetime.fromtimestamp(timestamp)
formatted_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("转换后的时间：", formatted_time)
