if __name__ == '__main__':
    num1 = int(input("num1을 입력 하세요"))
    print(num1)
    num2 = int(input("num2을 입력 하세요"))
    print(num2)

    max = 100
    min = 0

    if num1 > num2:
        max = num1
        min = num2
    else:
        max = num2
        min = num1

    print(f"결과는 num1 {num1} num2 {num2} min {min} max {max}")












