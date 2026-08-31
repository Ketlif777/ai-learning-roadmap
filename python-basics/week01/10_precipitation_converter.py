millimeters = float(input("请输入降水量（mm）："))

inches = millimeters / 25.4
meters = millimeters / 1000

print(f"{millimeters:g} mm = {inches:.3f} inches")
print(f"{millimeters:g} mm = {meters:.4f} m")
