import requests

passed = failed = 0

# TC01
print("执行 TC01 ...", end="")
try:
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    actual = res.json().get("userId")
    if res.status_code == 200 and actual == 1:
        print("通过")
        passed += 1
    else:
        print("失败")
        failed += 1
except Exception as e:
    print("异常")
    failed += 1

# TC02
print("执行 TC02 ...", end="")
try:
    res = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    actual = res.json().get("userId")
    if res.status_code == 200 and actual == 1:
        print("通过")
        passed += 1
    else:
        print("失败")
        failed += 1
except Exception as e:
    print("异常")
    failed += 1

# TC03
print("执行 TC03 ...", end="")
try:
    res = requests.get("https://jsonplaceholder.typicode.com/users/1")
    actual = res.json().get("username")
    if res.status_code == 200 and actual == 'Bret':
        print("通过")
        passed += 1
    else:
        print("失败")
        failed += 1
except Exception as e:
    print("异常")
    failed += 1

print("="*20)
print(f"总计: 通过 {passed} 条, 失败 {failed} 条")
