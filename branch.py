def greater(x,y):
    if x > y:
        print("x > y")
    elif x < y:
        print("x < y")
    else:
        print("x == y")

greater(5, 4)
greater(-50, -40)
greater(10, 10)

def train_fare(age):
    if age >= 12:
        print(200)
    elif 6 <= age < 12:
        print(100)
    else:
        print(0)

train_fare(12)
train_fare(6)
train_fare(5)

def xor(x,y):
    if x&y | (not x)&(not y):
        print(False)
    else:
        print(True)

xor(True, True)
xor(True, False)
xor(False, True)
xor(False, False)