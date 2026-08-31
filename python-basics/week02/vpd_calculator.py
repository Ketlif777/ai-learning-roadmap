"""第 2 周项目：根据温度和相对湿度计算 VPD。"""

import math


def calculate_saturation_vapor_pressure(temperature_c):
    """根据空气温度计算饱和水汽压，返回值单位为 kPa。"""
    e_s = 0.6108 * math.exp((17.27 * temperature_c) / (temperature_c + 237.3))
    return e_s


def is_valid_relative_humidity(relative_humidity):
    """相对湿度位于 0%～100% 时返回 True，否则返回 False。"""
    return 0 <= relative_humidity <= 100


def calculate_vpd(temperature_c, relative_humidity):
    """计算 VPD，返回值单位为 kPa。"""
    if not is_valid_relative_humidity(relative_humidity):
        raise ValueError("相对湿度必须在 0%～100% 之间")

    e_s = calculate_saturation_vapor_pressure(temperature_c)
    e_a = e_s * relative_humidity / 100
    vpd = e_s - e_a
    return vpd


def main():
    """读取输入、调用计算函数并显示结果。"""

    try:
        temperature_c = float(input("请输入温度（摄氏度）："))
        relative_humidity = float(input("请输入相对湿度（%）："))
        vpd = calculate_vpd(temperature_c, relative_humidity)
    except ValueError:
        print("输入无效：请输入数字，并确保相对湿度在 0%～100% 之间。")
        return

    print(f"VPD = {vpd:.3f} kPa")


if __name__ == "__main__":
    main()
