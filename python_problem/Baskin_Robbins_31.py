from random import randint

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
    if not playerATurn:
        playerNum = brGame()
    else:
        playerNum = randint(1, 3)
    
    for _ in range(playerNum):
        num += 1
        print(f"{'computer' if playerATurn else 'player'} : {num}")
        if num >= 31:
            break
        
    if num >= 31:
        print(f"{'player' if playerATurn else 'computer'} 승리!")
        break
    
    playerATurn = not playerATurn
    