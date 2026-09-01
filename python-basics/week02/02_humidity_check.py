"""练习 2：使用条件分支检查相对湿度。"""


def check_relative_humidity(relative_humidity):
    """返回相对湿度检查结果。"""
    if relative_humidity < 0:
        return "相对湿度不能小于 0%"
    elif relative_humidity > 100:
        return "相对湿度不能大于 100%"
    else:
        return "相对湿度输入有效"


def main():
    """读取用户输入并显示检查结果。"""
    relative_humidity = float(input("请输入相对湿度（%）："))
    message = check_relative_humidity(relative_humidity)
    print(message)


if __name__ == "__main__":
    main()
