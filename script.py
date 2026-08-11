numbers=[]
total=0
print("计算器")
print("输入数字，输入结束，得总和与平均")
while True:
    userinput=input(">>>输入数字或输入‘结束’退出")
    if userinput=="结束":
        break
    if not userinput.isdigit():
        print("警告，请输入纯数字")
        continue
    num=int(userinput)
    numbers.append(num)
    total=total+num
    print(f"已输入{num},共{len(numbers)}")
print("\n"+"="*20)
print(f"共{len(numbers)}")
for num in numbers:
    if num%2==0:
        print(f"{num}是偶")
    else:
        print(f"{num}是奇")
print(f"总和{total}")
print(f"平均数是：{total/len(numbers)}")