while True:    
    try:
        n= int(input("please enter the number(enter 0 to exit) "))
        if n == 0:
            break
        if n<0:
            print('please enter positive numbers only')
            continue
        for _ in range(n):
            print(" "*(n-_),' *'*_)
        for _ in range(n):
            print(" "*_,' *'*(n-_))
    except ValueError:
        print("ValueError:","Please enter numbers only")