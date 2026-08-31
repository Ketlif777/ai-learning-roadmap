# 第 1 周学习笔记：计算机基础与 GitHub

时间：2026 年 8 月 29 日—2026 年 9 月 4 日

## 本周目标

- 固定编辑器和 Python 环境。
- 熟悉文件、目录、路径和基础命令行操作。
- 理解 GitHub 仓库、分支、commit 和 Pull Request。
- 建立正式学习仓库。
- 编写并运行 10 个小型 Python 程序。
- 完成一次完整的分支开发和 PR 合并流程。

## 本周成果

- 建立了 `ai-learning-roadmap` 仓库。
- 创建并使用了 `python-week01` 分支。
- 完成了两次 Python 练习提交和一次 README 进度提交。
- 将 10 个 Python 程序通过 PR 合并进 `main`。
- 学会了使用 GitHub CLI 创建、查看和合并 PR。
- 配置了 Git 提交身份、隐私邮箱和安全的 TLS 校验。

## 10 个 Python 小程序

| 文件 | 内容 | 主要知识点 |
|---|---|---|
| `01_hello.py` | 输出学习目标 | `print()`、字符串 |
| `02_add.py` | 两数相加 | `input()`、`float()`、变量 |
| `03_temperature.py` | 摄氏度转华氏度 | 算术表达式、f-string |
| `04_circle.py` | 计算圆面积和周长 | `import`、`math.pi`、乘方 |
| `05_even_or_odd.py` | 判断奇偶数 | `%`、`if/else` |
| `06_number_sign.py` | 判断正数、负数或零 | `if/elif/else` |
| `07_grade.py` | 成绩分级 | 条件顺序、范围判断 |
| `08_iterate_list.py` | 遍历每日降水量 | 列表、`for`、`enumerate()` |
| `09_average.py` | 计算一组数字的平均值 | `split()`、列表推导式、`sum()`、`len()` |
| `10_precipitation_converter.py` | 降水单位换算 | 水文单位、格式化输出 |

## Python 报错的阅读方法

本周使用非法输入 `abc` 触发了 `ValueError`：

```text
Traceback (most recent call last):
  File ".../02_add.py", line 1, in <module>
    first_number = float(input("请输入第一个数字："))
ValueError: could not convert string to float: 'abc'
```

阅读 traceback 时从下向上看：

1. 最后一行说明异常类型和具体原因。
2. 最后一个 `File` 说明出错文件、行号和函数。
3. 对照源代码，追踪该表达式使用的输入和变量。
4. 有多层函数调用时，再逐层向上寻找调用来源。

这次错误的数据流是：

```text
input() 得到字符串 "abc"
→ float("abc") 尝试转换
→ 转换失败并抛出 ValueError
→ 程序没有捕获异常，因此终止
```

## Git 的三个区域

```text
工作区 ── git add ──> 暂存区 ── git commit ──> 本地提交历史
                                                   │
                                                git push
                                                   │
                                                   ▼
                                               GitHub 远程仓库
```

- 工作区：磁盘上正在编辑的文件。
- 暂存区：下一次 commit 准备包含的文件快照。
- commit：带作者、时间和说明的项目快照。
- push：将本地 commit 上传到远程仓库。

常用检查命令：

```powershell
git status
git diff
git diff --staged
git log --oneline
```

## 分支与 Pull Request

- `main` 保存已经验收的稳定内容。
- 功能分支用于隔离尚未完成的修改。
- PR 用于比较分支、审查变更并提出合并请求。
- push 功能分支不会自动修改 `main`。
- PR 合并完成后，可以删除已经完成任务的分支。

本周使用的流程：

```text
main
→ 创建 python-week01
→ 添加并提交练习文件
→ push 到 GitHub
→ 创建 PR
→ 审查 Files changed
→ 合并进 main
→ 删除功能分支
```

## `.gitignore` 与 Python 缓存

Python 在导入模块或执行编译检查时可能创建：

```text
__pycache__/
*.pyc
```

它们是可以自动重建的字节码缓存，不属于项目源代码，因此使用 `.gitignore` 排除：

```gitignore
__pycache__/
*.py[cod]
```

如果缓存已经进入暂存区，应先使用 `git restore --staged` 将其移出，再提交 `.gitignore`。

## 本周遇到的问题

### LF 与 CRLF

- LF 是 Linux、macOS 和 Git 仓库常见的换行格式。
- CRLF 是 Windows 常见的换行格式。
- Git 提示换行符转换通常是 warning，而不是代码错误。

### 作者身份未知

第一次 commit 因为没有设置 `user.name` 和 `user.email` 而失败。配置仓库级身份后重新 commit 即可。为保护隐私，命令行 commit 使用 GitHub 提供的 `noreply` 邮箱。

### TLS 校验被关闭

发现全局配置 `http.sslVerify=false` 后恢复为 `true`。网络超时不应通过关闭证书校验解决。

### push 网络超时

commit 已经安全保存在本地，但 push 可能因网络中断失败。此时不需要重复 commit，只需在网络恢复后重新执行 `git push`。

### PowerShell 找不到 `gh`

GitHub CLI 已安装，但安装目录未加入 `PATH`。将 `C:\Program Files\GitHub CLI` 加入用户 PATH 后，新终端可以直接运行 `gh`。

## 本周掌握程度

现在我能够：

- 从终端进入项目目录并运行 Python 文件。
- 根据 traceback 找到错误类型、文件和行号。
- 区分工作区、暂存区、本地提交和远程仓库。
- 在提交前使用 `git diff --staged` 审查变更。
- 创建分支并完成 add、commit、push、PR 和 merge。
- 判断哪些自动生成文件不应进入仓库。
- 使用 `gh` 在 PowerShell 中管理 PR。

## 下一周

第 2 周进入函数与条件，主要成果是 `vpd_calculator.py`：

- 完成 CS50P Week 0～1 或主课程对应内容。
- 编写温度、相对湿度到 VPD 的计算程序。
- 增加输入检查。
- 将计算过程拆成函数。
- 编写 3 个测试。
