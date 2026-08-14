print("this program illustrates a chaotic function\n")
x=float(input("enter a number between 0 and 1"))#the input value is 0.25
for i in range(1,10):
    x=1.3*x*(1-x)
    print("{0:.17f}".format(x))

