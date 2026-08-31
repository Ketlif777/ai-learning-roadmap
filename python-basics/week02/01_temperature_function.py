"""练习 1：把摄氏温度转换封装成函数。"""


def celsius_to_fahrenheit(celsius):
    """接收摄氏温度，返回对应的华氏温度。"""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def main():
    """读取用户输入并显示换算结果。"""
    celsius = float(input("请输入摄氏温度："))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:g}°C = {fahrenheit:g}°F")


if __name__ == "__main__":
    main()
