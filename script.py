def 计算统计(数字列表):
    total=0
    for n in 数字列表:
        total=total+n
    平均数=total/len(数字列表)
    return total,平均数
def 显示报告(数字列表):
    总和,均值=计算统计(数字列表)
    print("\n---奇偶分析---")
    for n in 数字列表:
        if n%2==0:
            print(f"{n}是偶")
        else:
            print(f"{n}是奇")
    print(f"总和是{总和}")
    print(f"均值是{均值}")
    print("___报告结束--\n")
数据=[14,27,39]
计算结果=计算统计(数据)
print(f"计算器返回的原始包裹：{计算结果}")
总和,平均数=计算统计(数据)
if 平均数>10:
     print(f"平均数{平均数}大于10！")
else:
     print(f"平均数{平均数}正常")
显示报告(数据)

