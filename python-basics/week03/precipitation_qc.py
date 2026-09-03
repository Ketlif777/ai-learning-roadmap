"""第 3 周项目：读取每日降水 CSV 并生成简单质控报告。"""

import csv
from pathlib import Path


EXTREME_THRESHOLD_MM = 300.0
SAMPLE_DATA_PATH = Path(__file__).with_name("precipitation_sample.csv")


def load_precipitation_records(file_path):
    """读取 CSV，并以字典列表形式返回全部记录。"""
    with file_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def parse_precipitation(precipitation_text):
    """把空字符串转换为 None，其余文本转换为 float。"""
    # TODO 1：如果 precipitation_text 是空字符串，返回 None。
    # TODO 2：否则使用 float() 转换并返回数值。
    raise NotImplementedError("请完成 parse_precipitation()")


def classify_precipitation(value, extreme_threshold=EXTREME_THRESHOLD_MM):
    """把一个降水值分类为 missing、negative、extreme 或 normal。"""
    # TODO 3：按照 README 中的统一规则返回分类名称。
    # 注意：300 mm 属于 normal，只有严格大于阈值才属于 extreme。
    raise NotImplementedError("请完成 classify_precipitation()")


def summarize_precipitation(records):
    """遍历 CSV 记录并返回质控数量、有效降水总量和平均值。"""
    summary = {
        "total_records": len(records),
        "normal_count": 0,
        "missing_count": 0,
        "negative_count": 0,
        "extreme_count": 0,
        "valid_count": 0,
        "valid_total_mm": 0.0,
        "valid_average_mm": None,
    }

    # TODO 4：遍历 records，从每个 record 中取出 precipitation_mm 文本。
    # TODO 5：调用 parse_precipitation() 和 classify_precipitation()。
    # TODO 6：根据分类更新 normal_count、missing_count、negative_count
    #         或 extreme_count。每条记录只能增加一个分类计数。
    # TODO 7：normal 和 extreme 都计入 valid_count 与 valid_total_mm。
    # TODO 8：循环结束后，如果存在有效记录，计算 valid_average_mm。
    raise NotImplementedError("请完成 summarize_precipitation()")


def print_qc_report(summary):
    """把质控统计字典格式化为终端报告。"""
    print("降水数据质控报告")
    print(f"总记录数：{summary['total_records']}")
    print(f"正常记录：{summary['normal_count']}")
    print(f"缺测记录：{summary['missing_count']}")
    print(f"负值记录：{summary['negative_count']}")
    print(f"极端记录：{summary['extreme_count']}")
    print(f"有效记录：{summary['valid_count']}")
    print(f"有效降水总量：{summary['valid_total_mm']:.1f} mm")

    if summary["valid_average_mm"] is None:
        print("有效降水平均值：无有效数据")
    else:
        print(f"有效降水平均值：{summary['valid_average_mm']:.3f} mm")


def main():
    """读取样例 CSV、汇总质控信息并打印报告。"""
    records = load_precipitation_records(SAMPLE_DATA_PATH)
    summary = summarize_precipitation(records)
    print_qc_report(summary)


if __name__ == "__main__":
    main()
