# DayDayUpQ2.py
day_factor = 0.01
day_up = pow(1 + day_factor, 365)
day_down = pow(1 - day_factor, 365)
print(f"DayDayUp:{day_up:.2f}, DayDayDown:{day_down:.2f}")
