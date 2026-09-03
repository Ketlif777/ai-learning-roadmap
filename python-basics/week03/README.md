# 第 3 周：循环、列表、字典与降水数据质控

开始时间：2026 年 9 月 3 日

预计投入：7 小时（CS50P Week 2 已完成，不再重复计时）

本周成果：`precipitation_qc.py`

## 本周目标

完成本周后，你应当能够：

- 使用 `for` 循环依次处理多条降水记录。
- 说明列表中的元素与 CSV 中一行记录之间的关系。
- 使用字典保存有名称的统计结果，而不是依赖多个含义不清的变量。
- 正确初始化、更新和检查计数器与累计值。
- 区分缺测值、非法负值和可疑极端值。
- 读取一个小型 CSV，并输出可复核的质控摘要。
- 使用简单自动测试检查循环和边界条件。
- 在不看原代码的情况下重写核心统计循环。

## 本周质控规则

本周统一使用以下规则，避免一边写代码一边改变定义：

| 情况 | 分类 | 是否计入有效降水统计 |
|---|---|---|
| 空字符串 | `missing` | 否 |
| 小于 0 mm | `negative` | 否 |
| 大于 300 mm | `extreme` | 是，但必须单独标记 |
| 0～300 mm（含边界） | `normal` | 是 |

`300 mm` 是正常值，只有严格大于 `300 mm` 才标记为可疑极端值。极端值只是需要复核，不能在没有依据时直接删除。

样例 CSV 中故意不放入 `abc` 一类非数字文本。文件不存在、列缺失和非法文本将在第 4 周结合异常处理系统学习。

## 学习顺序

不要一次完成所有文件。每完成一步，先运行、解释数据流，再进入下一步。

### 第一部分：确认 CS50P Week 2（已完成）

- [x] 已观看并学习 [CS50P Week 2：Loops](https://cs50.harvard.edu/python/weeks/2/)

开始练习前，先口头回答：

1. `for item in items` 中，`item` 每次保存什么？
2. 为什么计数器通常要在循环开始前初始化？
3. 列表通过位置访问元素，字典通过什么访问值？
4. `break` 和 `continue` 分别会怎样改变循环？

### 第二部分：练习 1——遍历降水列表

文件：`01_precipitation_loop.py`

任务：

1. 使用 `enumerate(..., start=1)` 遍历每日降水量。
2. 分别统计缺测天数、负值天数和有效天数。
3. 只把大于等于 0 的数值计入有效降水总量。
4. 不要为列表中的六个元素分别编写六段条件代码。

完成后的预期结果：

```text
总天数：6
有效天数：4
缺测天数：1
负值天数：1
有效降水总量：335.7 mm
```

### 第三部分：练习 2——使用字典保存质控计数

文件：`02_qc_summary_dictionary.py`

任务：

1. 保留已经给出的 `summary` 字典结构。
2. 每条记录只能归入一个分类。
3. 根据分类名称更新对应的字典值。
4. 检查四类数量之和是否等于总记录数。

完成后的预期字典：

```python
{
    "normal": 3,
    "missing": 1,
    "negative": 1,
    "extreme": 1,
}
```

### 第四部分：降水数据质控程序

文件：

- `precipitation_sample.csv`：11 天样例数据。
- `precipitation_qc.py`：主程序骨架。
- `test_precipitation_qc.py`：基础自动测试骨架。

程序的数据流是：

```text
CSV 文件
→ csv.DictReader 把每行变成字典
→ 列表保存全部行字典
→ 空字符串转换为 None，其余文本转换为 float
→ 对每条记录分类
→ 更新 summary 字典
→ 计算有效降水总量和平均值
→ 打印质控报告
```

`load_precipitation_records()`、`print_qc_report()` 和 `main()` 已经提供。你本周主要完成：

1. `parse_precipitation()`：把文本转换为 `None` 或 `float`。
2. `classify_precipitation()`：根据统一规则返回分类名称。
3. `summarize_precipitation()`：遍历全部记录并更新统计字典。
4. 四个基础测试函数中的断言。

完成后，样例数据的质控结果应为：

```text
总记录数：11
正常记录：7
缺测记录：1
负值记录：1
极端记录：2
有效记录：9
有效降水总量：1079.0 mm
有效降水平均值：119.889 mm
```

## 运行命令

在仓库根目录 `D:\Codex\AILearning\ai-learning-roadmap` 中运行：

```powershell
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week03/01_precipitation_loop.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week03/02_qc_summary_dictionary.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week03/precipitation_qc.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week03/test_precipitation_qc.py
```

## 调试任务

核心程序完成并通过测试后，再让 Agent 制造一个错误。优先选择以下一种：

- 把字典初始化放进循环内部，观察为什么最终只保留一条记录的效果。
- 把 `value > 300` 改成 `value >= 300`，观察边界测试怎样失败。
- 忘记排除负值，观察总量和平均值怎样被污染。

先阅读失败输出并定位，再查看或请求修改建议。

## 本周验收

- [ ] 能解释 `for` 循环变量每次取得什么值。
- [x] `01_precipitation_loop.py` 输出与预期一致。
- [x] `02_qc_summary_dictionary.py` 的四类数量正确。
- [ ] `precipitation_qc.py` 能读取样例 CSV 并输出完整报告。
- [ ] 四个自动测试全部通过。
- [ ] 能说明极端值为什么被标记但仍计入有效统计。
- [ ] 能证明四类记录数量之和等于总记录数。
- [ ] 完成一次核心统计循环的无 Agent 重写。
- [ ] 使用 `git diff` 检查实际修改。

第三周主要内容真正完成后，才编写 `notes/week03.md` 并更新根 README 的完成状态。
