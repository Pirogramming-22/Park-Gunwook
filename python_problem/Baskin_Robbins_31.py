num = 0

while True:
    try:
        playerNum = float(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
        if playerNum in [1, 2, 3]:
            pass    
        elif playerNum.is_integer():
            print("1, 2, 3 중 하나를 입력하세요.")
            continue
        else:
            print("정수를 입력하세요")
            continue
    except ValueError:
        print("정수를 입력하세요")
        continue