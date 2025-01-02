num = 0
playerATurn = True

def brGame():
    while True:
        try:
            playerNum = float(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            if playerNum in [1, 2, 3]:
                return int(playerNum)
            elif playerNum.is_integer():
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                print("정수를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
        

while True:
    playerNum = brGame()
    
    for _ in range(playerNum):
        num += 1
        print(f"{'playerA' if playerATurn else 'playerB'} : {num}")
        if num >= 31:
            break
        
    if num >= 31:
        print(f"{'playerB' if playerATurn else 'playerA'} 승리!")
        break
    
    playerATurn = not playerATurn
    