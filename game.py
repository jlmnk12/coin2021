print("도라에몽 게임")
print("도라에몽이 길을 가다가 퉁퉁이를 만났다")
print("1.싸운다 2.도망간다")
a = input("입력: ")
print("당신이 입력한 값은?",a)
if a == "1":
    print("싸운다")
if a == "2":
    print("도망간다")

#밥 먹기
#메뉴 1, 2, 3
#메뉴 선택시 음식이름 출력

print("밥을 먹으러간다.")
print("1~3중에 고르시오")
menu = input("번호 : ")
print("고른 번호 : ",menu)

if menu == "1":
    print("햄버거")
if menu == "2":
    print("짜장면")
if menu == "3":
    print("피자")