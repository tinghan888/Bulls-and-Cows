# my medium: https://medium.com/@dinkjessica56
#有四十四隻石獅子，四十四隻石獅子，吃了四十四個澀柿子。
import random                               # 匯入 random 亂數函式

                                            # 正確答案為 隨機的亂數~99, randint為將亂數設為整數
ans=random.randint(0,99)
min=0                                       # 最小值為0
max=99                                      # 最大值為99
gameStart=True                              # 遊戲開始為 真
while gameStart:                            # gameStart只要為 真 就持續迴圈
    # 猜的數字 為 min(0) max(99)或是 "q"離開遊戲
    inputNumber=input(f"請輸入要猜的數字({min}~{max})或是輸入q離開遊戲:")
    if inputNumber == "q":                  # 如果 猜的數字為 字串 q
        print("你的人生已經沒了!!")                  # 印出 遊戲結束
        gameStart=False                    # gameStart 不為 真
        break                              # 跳出迴圈
    else:
        inputNumber = int(inputNumber)                  # 宣告 輸入的數字為整數
        if (inputNumber > max) or (inputNumber < min):  # 若猜的數字超過 max or min
            print(f"符合條件的數字({min}~{max})")          # 印出符合條件的數字為 min ~ max
        else:
            if inputNumber > ans :                      # 如果 輸入的數字 超過 答案
                max = inputNumber                       # 將 猜的數字的值放入 max
                print(f"符合條件的數字({min}~{max})")      # 印出 min~max(也就是猜的數字)
            elif inputNumber < ans :                    # 又如果 輸入的數字 小於 答案
                min = inputNumber                       # 將 輸入的值放入 min
                print(f"符合條件的數字({min}~{max})")      # 印出 min(猜的數字)~max
            else:                                       # 以上皆非
                print("可惡!讓你猜對了")                        # 印出 正確!
                min = 0                                 # 重製最小值 min 為 0
                max = 99                                # 重製最大值 max 為99
                ans = random.randint(0, 99)             # 再放入一個隨機的答案,繼續下一場遊戲














