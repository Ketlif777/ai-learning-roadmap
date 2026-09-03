"""练习 1：遍历每日降水列表并累计基础统计。"""


DAILY_PRECIPITATION_MM = [0.0, 12.5, None, -1.0, 315.2, 8.0]


def analyze_precipitation(values):
    """返回总天数、有效天数、缺测天数、负值天数和有效降水总量。"""
    # TODO 1：在循环外初始化四个计数或累计变量。
    # TODO 2：使用 enumerate(values, start=1) 遍历列表。
    # TODO 3：None 计入缺测，小于 0 的数值计入负值。
    # TODO 4：大于等于 0 的数值计入有效天数和有效降水总量。
    # TODO 5：使用字典返回全部统计结果。
    raise NotImplementedError("请完成 analyze_precipitation()")


def main():
    """运行练习并显示统计结果。"""
    result = analyze_precipitation(DAILY_PRECIPITATION_MM)
    print(f"总天数：{result['total_days']}")
    print(f"有效天数：{result['valid_days']}")
    print(f"缺测天数：{result['missing_days']}")
    print(f"负值天数：{result['negative_days']}")
    print(f"有效降水总量：{result['valid_total_mm']:.1f} mm")


if __name__ == "__main__":
    main()
