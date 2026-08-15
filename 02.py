import math
def solvequadratic(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None,None
    elif delta == 0:
        x=(-b)/2*a
        return x,x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1,x2
print("----一元二次方程计算器---")
while True:
    userput=input("请输入 a b c 用空格隔开，输入q退出")
    if userput == "q":
        break
    try:
        a,b,c=map(float,userput.split())
        result1,result2=solvequadratic(a,b,c)
        if result1 is None:
            print("无实数根")
        elif result1==result2:
            print(f"有唯一实数根：x={result1:.3f}")
        else:
            print(f"两根为：x1={result1:.3f},x2={result2:.3f}")
    except ValueError:
        print("错误，请输入3个有效数字，并用空格隔开。\n")