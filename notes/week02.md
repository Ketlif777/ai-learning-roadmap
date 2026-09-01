# 第 2 周学习笔记：函数、条件与 VPD 计算器

实际完成时间：2026 年 8 月 31 日—9 月 1 日

## 本周目标与成果

本周完成了 CS50P Week 0（Functions, Variables）和 Week 1（Conditionals），并把函数、条件、输入检查和测试用于一个水文领域小程序。

实际成果包括：

- 完成温度换算函数练习 `01_temperature_function.py`。
- 完成相对湿度范围检查练习 `02_humidity_check.py`。
- 完成温度与相对湿度到 VPD 的计算程序 `vpd_calculator.py`。
- 对非数字输入和超出 0%～100% 的相对湿度给出友好提示。
- 完成 `test_vpd_calculator.py` 中的 3 个自动测试。
- 使用正常值、边界值和非法值对程序进行了实际运行验收。

## 文件导航

| 文件 | 用途 |
|---|---|
| `python-basics/week02/01_temperature_function.py` | 练习参数、返回值和 `main()` |
| `python-basics/week02/02_humidity_check.py` | 练习 `if/elif/else` 与边界检查 |
| `python-basics/week02/vpd_calculator.py` | VPD 主程序与输入处理 |
| `python-basics/week02/test_vpd_calculator.py` | 正常、边界和非法输入测试 |

## 函数与程序入口

函数把一项计算封装成可重复调用的操作。例如，温度转换函数只负责接收摄氏温度并返回华氏温度，输入和输出留给 `main()` 组织。

本周明确区分了：

- 参数：函数定义中接收值的名称。
- 实参：调用函数时传入的具体值。
- `return`：把结果交还给调用者，以便继续计算或测试。
- `print()`：把内容显示到终端，不代替函数返回值。

程序入口采用：

```python
if __name__ == "__main__":
    main()
```

直接运行文件时，`__name__` 的值是 `"__main__"`，因此执行 `main()`；文件被测试程序导入时，`__name__` 是模块名，因此不会自动请求用户输入。这使同一个文件既能作为程序运行，也能作为模块被测试和复用。

## 条件与边界

相对湿度的有效范围用一个连续比较表达：

```python
0 <= relative_humidity <= 100
```

这里的 0 和 100 都是有效边界，所以使用 `<=`。范围外的数据在进入科学计算前被拒绝，避免产生没有意义的结果。

`calculate_vpd()` 正常时始终返回数字；非法相对湿度则抛出 `ValueError`，而不是返回错误字符串。这样可以保持函数返回类型和职责稳定。

## VPD 计算的数据流

本周采用的计算关系为：

```text
饱和水汽压 es = 0.6108 × exp((17.27 × T) / (T + 237.3))
实际水汽压 ea = es × RH / 100
VPD = es - ea
```

程序中的数据流为：

```text
温度和相对湿度输入
→ 转换为 float
→ 检查相对湿度范围
→ 计算饱和水汽压 es
→ 计算实际水汽压 ea
→ 计算并返回 VPD
→ main() 格式化为三位小数并输出
```

## 本周真实错误：`try` 没有包住函数调用

第一次编写 `main()` 时，`try` 只包住了两个 `float(input(...))`，而 `calculate_vpd()` 位于 `try` 外部。非数字输入能够被捕获，但相对湿度为 120% 时，`calculate_vpd()` 抛出的 `ValueError` 没有对应的 `except`，程序仍然显示 traceback。

错误路径是：

```text
成功读取 20 和 120
→ 离开 try 代码块
→ calculate_vpd(20, 120)
→ 相对湿度检查失败并抛出 ValueError
→ 当前没有 except 捕获
→ 程序终止并显示 traceback
```

修复方法是把可能抛出 `ValueError` 的 `calculate_vpd()` 调用也放入 `try`。这次问题说明：

> `except` 不会自动捕获文件中所有同类异常，只能捕获对应 `try` 范围内产生的异常。

## 测试与浮点数

三个自动测试覆盖了不同代码路径：

| 测试 | 输入 | 预期结果 | 验证内容 |
|---|---|---|---|
| 正常情况 | 20°C、50% RH | 约 1.169 kPa | 主要公式 |
| 饱和空气 | 30°C、100% RH | 0 kPa | 边界值 |
| 非法湿度 | 20°C、120% RH | 抛出 `ValueError` | 输入验证 |

浮点数结果可能包含更多小数，因此没有直接使用 `actual == 1.169`，而是使用：

```python
math.isclose(actual, 1.169, abs_tol=0.001)
```

非法湿度测试只有在捕获到 `ValueError` 时才返回；如果函数错误地接受了 120%，测试会主动抛出 `AssertionError`。

最终运行结果：

```text
PASS: test_typical_condition
PASS: test_saturated_air
PASS: test_invalid_relative_humidity

结果：3/3 个测试通过
```

## 本周掌握程度

已经能够：

- 定义和调用简单函数，并使用参数和返回值。
- 区分计算函数与交互入口的职责。
- 使用条件表达式检查数值范围和边界。
- 使用 `main()` 和 `__name__` 入口保护组织程序。
- 根据 traceback 判断异常产生位置和未被捕获的原因。
- 使用正常值、边界值和非法值设计基本测试。
- 使用 `git diff` 审查修改，并以独立提交保存练习和项目成果。

初次接触、后续还需练习：

- `try/except` 的范围和异常信息设计。
- 自动测试运行器的内部逻辑。
- 浮点数误差与测试容差的选择。

本周没有单独进行“关闭 Agent 后从空文件重写 VPD 核心函数”，因此不把这一项标记为完成。核心函数均由本人根据公式和分步提示实际编写。

## 关键命令

```powershell
python .\python-basics\week02\vpd_calculator.py
python .\python-basics\week02\test_vpd_calculator.py
git diff
git diff --staged
git log --oneline
```

## 下一周衔接

第 3 周进入循环、列表和字典，目标是读取小型降水数据、遍历多日记录、统计缺失值和异常值，并生成一个简单的质控报告。计划成果为 `precipitation_qc.py`。
