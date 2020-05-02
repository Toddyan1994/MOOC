# DayDayUpQ3.py
base = 1.0
up_factor = 0.01
down_factor = -0.01
for i in range(365):
    if i % 7 in [6, 0]:
        base *= (1 + down_factor)  # weekends
    else:
        base *= (1 + up_factor)  # weekday
print(f"DayDayUp:{base:.2f}")
