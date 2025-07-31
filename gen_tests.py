import pandas as pd
import datetime

# 1. 读 Excel
df = pd.read_excel('cases.xlsx', engine='openpyxl')

# 2. 生成 run_all.py
with open('run_all.py', 'w', encoding='utf-8') as f:
    # 头部：导入库 + 初始化
    f.write('''import requests
import datetime

report_lines = []
passed = failed = 0
''')

    # 3. 根据 Excel 生成测试步骤
    for _, row in df.iterrows():
        case_id  = row['用例编号']
        method   = row['方法']
        url      = row['URL']
        exp_code = int(row['预期状态码'])
        exp_key  = row['预期字段']
        exp_val  = row['预期值']

        f.write(f'''
# {case_id}
try:
    res = requests.{method.lower()}("{url}")
    ok = res.status_code == {exp_code} and res.json().get("{exp_key}") == {repr(exp_val)}
    if ok:
        report_lines.append("执行 {case_id} ...通过")
        passed += 1
    else:
        report_lines.append("执行 {case_id} ...失败")
        failed += 1
except Exception:
    report_lines.append("执行 {case_id} ...异常")
    failed += 1
''')

    # 4. 生成报告并写入 report.md
    f.write('''
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"# 接口自动化报告\\n- 时间：{now}\\n" + "\\n".join(report_lines)
report += f"\\n- 总计: 通过 {passed} 条, 失败 {failed} 条"
with open("report.md", "w", encoding="utf-8") as f2:
    f2.write(report)
print(report)
''')

print('✅ 已生成 run_all.py（含报告逻辑）')