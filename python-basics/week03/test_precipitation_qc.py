"""第 3 周的四个基础测试。运行此文件即可执行测试。"""

import math

from precipitation_qc import classify_precipitation
from precipitation_qc import parse_precipitation
from precipitation_qc import summarize_precipitation


def test_parse_precipitation():
    """空字符串应变成 None，数字文本应变成 float。"""
    # TODO 1：断言空字符串的转换结果 is None。
    # TODO 2：断言 "12.5" 的转换结果等于 12.5。
    raise NotImplementedError("请完成 test_parse_precipitation()")


def test_classification_boundaries():
    """检查缺测、负值、阈值边界和极端值的分类。"""
    # TODO 3：分别检查 None、-0.1、300.0 和 300.1 的分类。
    raise NotImplementedError("请完成 test_classification_boundaries()")


def test_summary_counts_and_total():
    """内存中的五条记录应得到正确分类和有效降水总量。"""
    records = [
        {"date": "2026-08-01", "precipitation_mm": "0"},
        {"date": "2026-08-02", "precipitation_mm": ""},
        {"date": "2026-08-03", "precipitation_mm": "-1"},
        {"date": "2026-08-04", "precipitation_mm": "300"},
        {"date": "2026-08-05", "precipitation_mm": "301"},
    ]

    # TODO 4：调用 summarize_precipitation(records)。
    # TODO 5：检查总数、四个分类数和有效记录数。
    # TODO 6：使用 math.isclose() 检查有效降水总量为 601.0。
    raise NotImplementedError("请完成 test_summary_counts_and_total()")


def test_empty_records():
    """没有记录时，平均值应为 None，且不能发生除零错误。"""
    # TODO 7：汇总空列表，检查 valid_count 为 0、平均值 is None。
    raise NotImplementedError("请完成 test_empty_records()")


def main():
    """依次运行测试，并在终端显示结果。"""
    tests = [
        test_parse_precipitation,
        test_classification_boundaries,
        test_summary_counts_and_total,
        test_empty_records,
    ]

    passed = 0
    for test in tests:
        try:
            test()
        except Exception as error:
            print(f"FAIL: {test.__name__} — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"PASS: {test.__name__}")

    print(f"\n结果：{passed}/{len(tests)} 个测试通过")

    if passed != len(tests):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
