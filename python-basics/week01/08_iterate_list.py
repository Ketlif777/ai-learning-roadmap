daily_precipitation = [0.0, 2.5, 13.2, 0.0, 6.8]

for day, precipitation in enumerate(daily_precipitation, start=1):
    print(f"第 {day} 天：降水量 {precipitation:g} mm")
