import requests
import datetime

report_lines = []
passed = failed = 0

# TC01
try:
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    ok = res.status_code == 200 and res.json().get("userId") == 1
    if ok:
        report_lines.append("执行 TC01 ...通过")
        passed += 1
    else:
        report_lines.append("执行 TC01 ...失败")
        failed += 1
except Exception:
    report_lines.append("执行 TC01 ...异常")
    failed += 1

# TC02
try:
    res = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    ok = res.status_code == 200 and res.json().get("userId") == 1
    if ok:
        report_lines.append("执行 TC02 ...通过")
        passed += 1
    else:
        report_lines.append("执行 TC02 ...失败")
        failed += 1
except Exception:
    report_lines.append("执行 TC02 ...异常")
    failed += 1

# TC03
try:
    res = requests.get("https://jsonplaceholder.typicode.com/users/1")
    ok = res.status_code == 200 and res.json().get("username") == 'Bret'
    if ok:
        report_lines.append("执行 TC03 ...通过")
        passed += 1
    else:
        report_lines.append("执行 TC03 ...失败")
        failed += 1
except Exception:
    report_lines.append("执行 TC03 ...异常")
    failed += 1

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"# 接口自动化报告\n- 时间：{now}\n" + "\n".join(report_lines)
report += f"\n- 总计: 通过 {passed} 条, 失败 {failed} 条"
with open("report.md", "w", encoding="utf-8") as f2:
    f2.write(report)
print(report)
