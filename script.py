num=[12,3,5,6,8]
total=0
index=0
while index<len(num):
    n=num[index]
    total=total+n
    print(f"加了第{index+1}个数：{n},当前总和{total}")
    index=index+1
print(f"最终总和{total}")