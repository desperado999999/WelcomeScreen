def 自动分析(数字列表):
    """给数字，立刻算"""
    print("\n---自动分析报告")
    total=0
    for n in 数字列表:
        if n%2==0:
            print(f"{n}是偶")
        else:
            print(f"{n}是奇")
        total=total+n
    print(f"总和是{total}")
    print(f"平均数是{total/len(数字列表)}")
    print("---报告结束---")
def 交互输入():
    """输入，边输边分析"""
    numbers=[]
    total=0
    print("输入数字，输入‘结束’退出")
    while True:
        userinput=input()
        if userinput=="结束":
            break
        if not userinput.isdigit():
            print("警告")
            continue
        num=int(userinput)
        numbers.append(num)
        total=total+num
        print(f"已收录{num},共{len(numbers)}个数")
    自动分析(numbers)
print("欢迎来到数据分析工具箱")
自动分析([10,28,90])
交互输入()
print("感谢使用，下次再见")
