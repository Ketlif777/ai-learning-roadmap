score = float(input("请输入 0～100 分的成绩："))

if not 0 <= score <= 100:
    print("成绩必须在 0～100 之间。")
elif score >= 90:
    print("等级：A")
elif score >= 80:
    print("等级：B")
elif score >= 60:
    print("等级：C")
else:
    print("等级：D")
