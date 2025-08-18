if __name__ == '__main__':
    num1 = int(input("num1을 입력 하세요"))
    print(num1)
    num2 = int(input("num2을 입력 하세요"))
    print(num2)
    num3 = int(input("num3을 입력 하세요"))
    print(num3)

    max = 100
    min = 0

    if num1 > num2:
        max = num1
        if num3 > max:
            max = num3
    else:
        max = num2
        if num3 > max:
            max = num3

    print(f"결과는 num1 {num1} num2 {num2} min {min} max {max}")












