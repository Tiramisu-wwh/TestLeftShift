import pandas as pd
import os

# 1. 读 Excel
df = pd.read_excel('cases.xlsx')

# 2. 生成一个总脚本 run_all.py
with open('run_all.py', 'w', encoding='utf-8') as f:
    f.write("import requests\n\n")
    f.write("passed = failed = 0\n")

    for _, row in df.iterrows():
        case_id  = row['用例编号']
        method   = row['方法']
        url      = row['URL']
        exp_code = int(row['预期状态码'])
        exp_key  = row['预期字段']
        exp_val  = row['预期值']

        f.write(f"""
# {case_id}
print("执行 {case_id} ...", end="")
try:
    res = requests.{method.lower()}("{url}")
    actual = res.json().get("{exp_key}")
    if res.status_code == {exp_code} and actual == {repr(exp_val)}:
        print("通过")
        passed += 1
    else:
        print("失败")
        failed += 1
except Exception as e:
    print("异常")
    failed += 1
""")

    f.write("""
print("="*20)
print(f"总计: 通过 {passed} 条, 失败 {failed} 条")
""")
print("✅ 已生成 run_all.py")