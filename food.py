#밥 먹기
#메뉴 1, 2, 3
#메뉴 선택시 음식이름 출력
## 아래를 전체 반복 ##
for i in range(1,4):
    print("밥을 먹으러간다.")
    print("메뉴는?")
    print("1.학식 2.분식 3.중식")
    menu = input(str(i)+".입력 : ")
    #만약에 사용자의 입력값이 1 이면
    if menu == "1":
        print("학식")
    if menu == "2":
        print("분식")
    if menu == "3":
        print("중식")
    ## 여기까지 반복 ##