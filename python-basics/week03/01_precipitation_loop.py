"""练习 1：遍历每日降水列表并累计基础统计。"""


DAILY_PRECIPITATION_MM = [0.0, 12.5, None, -1.0, 315.2, 8.0]


def analyze_precipitation(values):
    """返回总天数、有效天数、缺测天数、负值天数和有效降水总量。"""
    # TODO 1：在循环外初始化四个计数或累计变量。
    total_days = 0
    valid_days = 0
    missing_days = 0
    negative_days = 0
    valid_total_mm = 0.0

    # TODO 2：使用 enumerate(values, start=1) 遍历列表。
    for day, value in enumerate(values, start=1):
        total_days += 1
        if value is None:
            missing_days += 1
        elif value < 0:
            negative_days += 1
        else:
            valid_days += 1
            valid_total_mm += value

    # TODO 5：使用字典返回全部统计结果。
    return {
        "total_days": total_days,
        "valid_days": valid_days,
        "missing_days": missing_days,
        "negative_days": negative_days,
        "valid_total_mm": valid_total_mm
    }


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
