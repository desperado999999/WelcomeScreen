numbers=[12,5,7,8,10]
total=0
for n in numbers:
    if n%2==0:
        print(f"{n} 是偶")
    else:
        print(f"{n}是奇")
    total=total+n
print("-"*10)
print(f"这组数的总和为{total}")
print(f"even num is:{total/len(numbers)}")