num1 = int(input("1つ目の数字を入力してください: "))
num2 = int(input("2つ目の数字を入力してください: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("同じ値です")