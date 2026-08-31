"""练习 2：使用条件分支检查相对湿度。"""


def check_relative_humidity(relative_humidity):
    """返回相对湿度检查结果。"""
    # TODO 1：小于 0 时返回“相对湿度不能小于 0%”。
    # TODO 2：大于 100 时返回“相对湿度不能大于 100%”。
    # TODO 3：其余情况返回“相对湿度输入有效”。
    raise NotImplementedError("请完成 check_relative_humidity()")


def main():
    """读取用户输入并显示检查结果。"""
    relative_humidity = float(input("请输入相对湿度（%）："))
    message = check_relative_humidity(relative_humidity)
    print(message)


if __name__ == "__main__":
    main()
