# 第 2 周：函数、条件与 VPD 计算器

建议时间：2026 年 9 月 5—11 日

预计投入：10 小时

本周成果：`vpd_calculator.py`

## 本周目标

完成本周后，你应当能够：

- 说明函数、参数、实参和返回值分别是什么。
- 区分“返回一个值”和“把一个值打印到终端”。
- 使用 `if`、`elif`、`else` 和布尔表达式检查输入。
- 把交互输入、科学计算和结果输出拆成不同职责。
- 根据报错或测试失败定位到具体函数。
- 在不看答案的情况下重写 VPD 核心计算函数。

## 学习顺序

不要一次打开所有答案，也不要先让 Agent 生成完整程序。按以下顺序进行。

### 第一部分：CS50P Week 0—1（3 小时）

学习材料：

- [Week 0：Functions, Variables](https://cs50.harvard.edu/python/weeks/0/)
- [Week 1：Conditionals](https://cs50.harvard.edu/python/weeks/1/)

重点理解：

1. `def` 定义函数，函数名描述它负责的动作。
2. 参数写在函数定义中，实参写在调用位置。
3. `return` 把结果交还给调用者；`print()` 只负责显示。
4. 函数内部创建的变量通常是局部变量。
5. 条件表达式的结果是 `True` 或 `False`。
6. 条件分支要先处理非法范围，再处理正常情况。

### 第二部分：两个短练习（3 小时）

依次完成：

1. `01_temperature_function.py`：把第 1 周的温度换算改写成函数。
2. `02_humidity_check.py`：用三个条件分支检查相对湿度。

每完成一个文件，都要：

1. 在终端运行它。
2. 至少试一个正常输入和一个边界输入。
3. 口头说明数据从哪里进入、在哪里计算、在哪里输出。

### 第三部分：VPD 计算器（3 小时）

VPD 是饱和水汽压与实际水汽压之差。这里使用 FAO-56 中的饱和水汽压关系：

```text
饱和水汽压 es = 0.6108 × exp((17.27 × T) / (T + 237.3))
实际水汽压 ea = es × RH / 100
VPD = es - ea
```

其中：

- `T`：空气温度，单位为 °C。
- `RH`：相对湿度，范围为 0%～100%。
- `es`、`ea` 和 VPD：单位均为 kPa。
- `exp()`：自然指数函数，可使用 `math.exp()`。

参考：[FAO Irrigation and Drainage Paper 56, Chapter 3](https://www.fao.org/4/x0490e/x0490e07.htm)

先在纸上或注释中写出以下数据流，再编辑 `vpd_calculator.py`：

```text
用户输入文本
→ 转换为温度和相对湿度数字
→ 检查相对湿度范围
→ 计算饱和水汽压
→ 计算实际水汽压
→ 计算 VPD
→ 格式化输出
```

### 第四部分：测试、调试与重建（1 小时）

在 `test_vpd_calculator.py` 中完成 3 个测试：

1. `20°C、50% RH`：VPD 约为 `1.169 kPa`。
2. `30°C、100% RH`：VPD 为 `0 kPa`。
3. `20°C、120% RH`：程序应拒绝这个非法湿度。

测试文件包含一个本周暂时不要求完全掌握的小型测试运行器。你只需要完成三个测试函数中的 TODO；循环和更完整的测试框架会在后续正式学习。

## 运行命令

在仓库根目录 `D:\Codex\AILearning\ai-learning-roadmap` 中运行：

```powershell
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week02/01_temperature_function.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week02/02_humidity_check.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week02/vpd_calculator.py
& 'D:\Codex\AILearning\.venv\Scripts\python.exe' python-basics/week02/test_vpd_calculator.py
```

如果虚拟环境命令无法运行，先检查解释器是否存在，不要立即删除或重建环境：

```powershell
Test-Path 'D:\Codex\AILearning\.venv\Scripts\python.exe'
Get-Content 'D:\Codex\AILearning\.venv\pyvenv.cfg'
```

## 本周验收

结束前逐项确认：

- [x] 两个短练习能够运行。
- [x] VPD 程序能处理正常输入。
- [x] 非数字输入不会显示整段 traceback，而是给出友好提示。
- [x] 相对湿度小于 0% 或大于 100% 时会被拒绝。
- [x] 三个自动测试全部通过。
- [x] 能解释每个函数的输入、输出和职责。
- [x] 能说明为什么测试导入模块时不应自动请求输入。
- [ ] 完成一次不看原代码的核心函数重写。
- [x] 使用 `git diff` 检查实际修改。

第二周主要内容真正完成后，才编写 `notes/week02.md` 并更新 README 中的完成状态。
