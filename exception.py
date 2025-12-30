def calculate(num1, num2, operator):
    # 関数を完成させてください
    try:
        n1 = int(num1)
        n2 = int(num2)
    except ValueError:
        raise ValueError("num1、num2には整数を入力してください")

    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        if n2 == 0:
            raise ZeroDivisionError("ゼロによる割り算は許可されていません")
        return n1 / n2
    else:
        raise ValueError("演算子には +、-、*、/ のいずれかを使用してください")


print("1番目の整数を入力してください:")
num1 = input()

print("2番目の整数を入力してください:")
num2 = input()

print("演算子(+, -, *, /)を入力してください:")
operator = input()

try:
    result = calculate(num1, num2, operator)
    print(result)
except Exception as e:
    print(e)
