# DayDayUpQ4.py
def day_up(df):
    day_up_base = 1
    down_factor = 0.01
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up_base *= (1 - down_factor)  # weekends
        else:
            day_up_base *= (1 + df)  # weekdays
    return day_up_base


day_factor = 0.01
while day_up(day_factor) < 37.78:
    day_factor += 0.001
print(f"work_day_up_factor is:{day_factor:.3f}")
# GRIT: perseverance and passion for long term goals
"这个字符串可以当作注释使用"

