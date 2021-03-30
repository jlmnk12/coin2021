### 아래 전체를 반복 ###
import random
for i in range(1, 4):
    print("밥무러 가자")
    print("메뉴는? ")
    #메뉴 변수
    menulist = '쫄면', '육계장', '비빔밥'
    print("1.쫄면 2.육계장 3.비빔밥 4.랜덤")
    menu = input(str(i) + ".입력: ")
    #만약에 사용자가 입력값이 1 과 같으면
    if menu == '1':
        print("쫄면 먹어라")
    if menu == '2':
        print("육계장 먹어라")
    if menu == '3':
        print("비빔밥 먹어라")
    if menu == '4':
        print(random.choice(menulist))
    # 랜덤을 고르면 위 메뉴중에서 아무거나 #
### 여기까지 반복 ###