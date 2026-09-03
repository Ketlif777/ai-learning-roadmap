"""练习 2：使用字典保存降水记录的质控分类数量。"""


PRECIPITATION_VALUES_MM = [0.0, 12.5, None, -1.0, 315.2, 300.0]
EXTREME_THRESHOLD_MM = 300.0


def build_qc_summary(values):
    """遍历降水列表，返回四种质控分类的数量。"""
    summary = {
        "normal": 0,
        "missing": 0,
        "negative": 0,
        "extreme": 0,
    }

    # TODO 1：遍历 values。
    # TODO 2：None 归入 missing。
    # TODO 3：小于 0 的数值归入 negative。
    # TODO 4：严格大于 EXTREME_THRESHOLD_MM 的数值归入 extreme。
    # TODO 5：其余数值归入 normal。
    # 提示：分类顺序会影响边界值最终进入哪个分支。
    raise NotImplementedError("请完成 build_qc_summary()")


def main():
    """运行练习并显示字典统计结果。"""
    summary = build_qc_summary(PRECIPITATION_VALUES_MM)
    print(summary)
    print(f"分类合计：{sum(summary.values())}")
    print(f"总记录数：{len(PRECIPITATION_VALUES_MM)}")


if __name__ == "__main__":
    main()
