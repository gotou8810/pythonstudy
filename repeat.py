def hello():
    for _ in range(100):
        print("こんにちは！")

hello()

def sheep(n):
    for i in range(1,n+1):
        print(f'羊が{i}匹')

sheep(3)

def sum_1_100():
    count = 0
    for i in range(1,101):
        count += i
    print(count)

sum_1_100()

def sum_range(x,y):
    count = 0
    for i in range(x,y+1):
        count += i
    print(count)

sum_range(10, 80)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(7)
fibonacci(30)
    