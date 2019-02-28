# -*-coding:utf-8

# 파일 입출력
# 파이썬에서 파일을 일을 때 사용하는 명령어 open() 함수
# open(파일명, 사용모드)
# 사용모드 : r(읽기모드),w(쓰기모드),a(추가모드)

# 맥이나 리눅스 같은 경우는 파일 경로 시스템이 다름
# 맥이나 리눅스는 드라이브라는 개념이 없고 모두 디렉토리(폴더)로 구성되어있다.
# 파이썬 3버전 대에서 유니코드 파일 읷는 벙법
# open() 은 지정한 파일을 열때 사용하는 명령어
# 첫번째 매개변수는 파일의 경로와 파일명을 입력함
# 현재 실행파일 같은 위치에 파일이 있을 경우는 경로를 무시해도됨
# f = open("C:/SooYoung(don't delete)/Python/chap04/test.txt", "r", encoding="utf-8")
# f = open("test.txt", "r", encoding="utf-8")

# # 파일에서 내용 한줄 읽어옴
# line = f.readline()
# # 읽어온 내용 출력
# print(line)
# 열었던 파일을 닫아줘야함
# 파일을 닫지 않으면 메모리를 지속적으로 사용 되 메모리 누수현상이 발생됨

# f.close()

f = open("C:/SooYoung(don't delete)/Python/chap04/test.txt", "a", encoding="utf8")
for i in range(1, 11):
    data = "{0}번째 줄입니다. \n".format(i)
    f.write(data)
f.close()