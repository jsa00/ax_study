while True:
    print("아무 메세지 입력(q - 종료)", end="") # end="" : 한줄 출력
    massage = input()

    if massage == "q":
        print("종료")
        break

    print(f"입력 메세지: {massage}")