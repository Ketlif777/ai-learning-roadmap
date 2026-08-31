number = float(input("请输入一个数字："))

if number > 0:
    print(f"{number:g} 是正数。")
elif number < 0:
    print(f"{number:g} 是负数。")
else:
    print("这个数字是零。")
