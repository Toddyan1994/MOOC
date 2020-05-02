# WeekNamePrintV1.py
week_str = "星期一星期二星期三星期四星期五星期六星期日"
week_id = int(input("请输入星期数字(1-7):"))
pos = (week_id - 1) * 3
print(week_str[pos:pos + 3])
