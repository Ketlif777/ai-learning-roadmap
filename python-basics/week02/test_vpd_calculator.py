"""第 2 周的三个自动测试。运行此文件即可执行测试。"""

import math

from vpd_calculator import calculate_vpd


def test_typical_condition():
    """20°C、50% RH 时，VPD 应约为 1.169 kPa。"""
    # TODO 1：调用 calculate_vpd()，再用 math.isclose() 检查结果。
    # 提示：math.isclose(actual, 1.169, abs_tol=0.001)
    raise NotImplementedError("请完成 test_typical_condition()")


def test_saturated_air():
    """30°C、100% RH 时，VPD 应为 0 kPa。"""
    # TODO 2：调用 calculate_vpd()，并断言结果接近 0。
    raise NotImplementedError("请完成 test_saturated_air()")


def test_invalid_relative_humidity():
    """相对湿度为 120% 时，calculate_vpd() 应抛出 ValueError。"""
    # TODO 3：调用 calculate_vpd(20, 120)。
    # 如果捕获到 ValueError，就直接 return。
    # 如果没有捕获到，则 raise AssertionError("非法湿度没有被拒绝")。
    raise NotImplementedError("请完成 test_invalid_relative_humidity()")


def main():
    """依次运行测试，并在终端显示结果。"""
    tests = [
        test_typical_condition,
        test_saturated_air,
        test_invalid_relative_humidity,
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
