if __name__ == '__main__':
    # set
    t1 = {1,2,3,4,5}
    print(type(t1))
    print(t1)
    t1.add(6)
    t1.add(5)
    print(t1)

    # tuple
    print("------- Tuple ------------")
    t2 = (1,2,3,4,5)
    print(type(t2))
    print(t2)
    print(t2[1])

    # 딕셔너리 key, value
    # JavaScript JSON
    d1 = {"a":1, "b":2, "c": 3}
    print(type(d1))
    print(d1)
    print(d1["a"])

    d2 = {"name":"이말숙", "age": 21, "major": "sw" }
    print(d2["name"])
    print(d2["age"])

    # 응용
    sts = [
        {"name": "이말숙", "age": 21, "major": "sw"},
        {"name": "김말숙", "age": 22, "major": "sw"},
        {"name": "홍말숙", "age": 23, "major": "se"},
        {"name": "정말숙", "age": 24, "major": "sw"}
    ]
    # 전체 학생들의 나이의 합과 평균을 출력 하시오
    sum = 0
    for st in sts:
        sum += st["age"]
    print(f" 합 {sum}  평균 {sum/len(sts)} ")

    # SW 학과 학생들의 나이의 합과 평균을 출력 하시오
    sum = 0
    count = 0
    for data in sts:
        if data["major"] == "sw":
            sum += data["age"]
            count = count + 1

    print(f"결과: 합 {sum} 평균{sum/count}")
    print("결과 합 %d, 평균 %.2f"%(sum, sum/count))
