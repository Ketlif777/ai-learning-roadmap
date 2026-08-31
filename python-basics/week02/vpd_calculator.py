"""第 2 周项目：根据温度和相对湿度计算 VPD。"""

import math


def calculate_saturation_vapor_pressure(temperature_c):
    """根据空气温度计算饱和水汽压，返回值单位为 kPa。"""
    # TODO 1：使用 README 中的 FAO-56 公式计算饱和水汽压。
    # 提示：自然指数函数写作 math.exp(...)
    raise NotImplementedError(
        "请完成 calculate_saturation_vapor_pressure()"
    )


def is_valid_relative_humidity(relative_humidity):
    """相对湿度位于 0%～100% 时返回 True，否则返回 False。"""
    # TODO 2：写一个布尔表达式并返回结果。
    raise NotImplementedError("请完成 is_valid_relative_humidity()")


def calculate_vpd(temperature_c, relative_humidity):
    """计算 VPD，返回值单位为 kPa。"""
    # TODO 3：先检查相对湿度；非法时抛出 ValueError。
    # TODO 4：调用饱和水汽压函数，计算实际水汽压和 VPD。
    raise NotImplementedError("请完成 calculate_vpd()")


def main():
    """读取输入、调用计算函数并显示结果。"""
    # TODO 5：读取温度和相对湿度，将输入转换为 float。
    # TODO 6：捕获非数字输入或非法湿度，显示简洁错误信息。
    # TODO 7：正常时把 VPD 输出到小数点后三位，单位为 kPa。
    raise NotImplementedError("请完成 main()")


if __name__ == "__main__":
    main()
