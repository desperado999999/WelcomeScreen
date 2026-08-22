def consert():
    userinput=input()
    while True:
        if userinput=="stop":
            break
        

        
            
        
        
        try:
            a=int(userinput)
            b=float(userinput)
            print(f"int is {a},float is {b}")
        except ValueError:
            print("please enter numbers")
consert()   