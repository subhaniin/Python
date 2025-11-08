while True:
    num = map(int, input().replace(',', ' ').split())  
    print(sum(num))