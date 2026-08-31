text = input("请输入一组数字，用英文逗号分隔：")
numbers = [float(item.strip()) for item in text.split(",")]

average = sum(numbers) / len(numbers)

print(f"平均值：{average:g}")
