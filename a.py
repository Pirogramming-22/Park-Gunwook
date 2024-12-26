a, b, c, d = map(int, input().split())
if a > 100 or a < 0 or b > 100 or b < 0 or c > 100 or c < 0 or d > 100 or d < 0:
    print('잘못된 점수')
    exit()
if ((a + b + c + d) / 4) >= 80:
    print("합격")
else:
    print("불합격")