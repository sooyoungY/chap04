#-*-coding:utf-8

# 연습문제 1

# 연습문제 2

# 

print("연습문제 1)")

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 2) + fib(n - 1)

for n in range(0, 11):
    print("{0},".format(fib(n)), end="")
print("\n")

# print("연습문제 2)")

# count = 0

# f = open("C:/SooYoung(don't delete)/Python/chap04/sample.txt", "r", encoding="utf8")
# datas = f.readlines()
# for data in datas:
#     count += int(data)
#     aver = count/len(datas)
# f.close()

# print(count)
# print(aver)

# f = open("C:/SooYoung(don't delete)/Python/chap04/sample.txt", "r", encoding="utf8")
# lines = f.readlines()
# f.close()

# total = 0
# for line in lines:
#     score = int(line)
#     total += score

# average = total / len(lines)

# print(total)
# print(average)

# f = open("result.txt", "w")

# f.write(str(average))
# f.close

# print()
# print("연습문제 3)")

# f = open("memory.txt", "w")
# f.close

# f = open("memory.txt", "w", encoding="utf8")
# while True:
#     w = input("")
#     if not w:
#         f.close()
#         break
#     f.write(w + "\n")

# f = open("memory.txt", "r", encoding="utf8")
# line = f.readlines()
# f.close()
# for val in line:
#     print(val)


# print()
# print("문제 4)")

# def memoryWrite():
#     f = open("memory.txt", "a", encoding="utf8")
#     while True:
#         w = input("")
#         if not w:
#             f.close()
#             break
#         f.write(w + "\n")

# def memoryRead():    
#     f = open("memory.txt", "r", encoding="utf8")
#     line = f.readlines()
#     f.close()
#     for val in line:
#         print(val)

# while 1:
#     print("메뉴 | 1. 내용입력 | 2. 내용출력 | 3. 종료")
#     num = input("입력하세요 : ")
#     num = int(num)
#     if num == 1:
#         memoryWrite()
#     elif num == 2:
#         memoryRead()
#     elif num == 3:
#         print("프로그램 종료합니다.")
#         break
#     else:
#         print("잘못된 입력입니다. \n")

# 성적표 출력 함수를 사용하여 프로그램 제작
# 5점에 한단계식 낮아짐
# 96점 이상 A+ ...
# 60점 미만은 F

# score = int(input("성적을 입력 하세요 : "))

# if score > 95:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "A+"))
# elif score > 89:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "A"))
# elif score > 84:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "B+"))
# elif score > 79:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "B"))
# elif score > 74:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "C+"))
# elif score > 69:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "C"))
# elif score > 64:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "D+"))
# elif score > 59:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "D"))
# else:
#     print("성적은 {0}이며 등급은 {1} 입니다.".format(score, "F"))


print()

def scorePrint(score, level):
    print("성적은 {0}이며 등급은 {1} 입니다.".format(score, level))

def selectScore(score):
    if score > 95:
        scorePrint(score, "A+")
    elif score > 89:
        scorePrint(score, "A")
    elif score > 84:
        scorePrint(score, "B+")
    elif score > 79:
        scorePrint(score, "B")
    elif score > 74:
        scorePrint(score, "C+")
    elif score > 69:
        scorePrint(score, "C")
    elif score > 64:
        scorePrint(score, "D+")
    elif score > 59:
        scorePrint(score, "D")
    else:
        scorePrint(score, "F")

def inputScore():
    score = int(input("성적을 입력 하세요 : "))
    return score

selectScore(inputScore())