# -*-coding:utf-8

# 함수 사용하기
# 함수는 소스의 재활용을 위해 사용
# 함수를 나타내는 키워드 def를 사용
# 반환값에 반환 타입 선언이 함수의 원형에 없음
# 함수의 매개변수 선언 시 매개변수의 타입을 입력할 필요가 없음

# 함수의 사용법
# 함수명(매개변수)

# 자바에서의 함수 원형
# public int 함수명(int 매개변수, int 매개변수) {
    # 실행코드
    # return 반환값
# }

# 파이썬에서의 함수 원형
# def 함수명(매개변수):
    # 실행 코드
    # return 반환값

# def sum(a, b):
#     return a + b

# a = 3
# b = 4
# c = sum(a, b)
# print("함수 sum의 사용 : {0}".format(c))

print()
def sum(a, b):
    result = a + b
    return result

a = 3
b = 4
c = sum(a, b)
print("함수 sum의 사용 : {0}".format(c))

def func1():
    print("매개변수와 반환값이 없는 함수")

def func2(a, b):
    print("반환값이 없고 매개변수가 {0}, {1} 인 함수".format(a, b))

def func3():
    print("매개변수가 없고 반환값만 있는 함수")
    return "함수 3번"

def func4(a, b):
    print("매개변수가 {0}, {1} 이고 반환값이 있는 함수".format(a, b))
    return "함수 4번"

func1()
func2(10, 20)
x = func3()
print(x)
y = func4(10, 20)
print(y)

# 문제 1) 매개 변수 2개를 입력받고 계산된 값을 반환하는 총 4개의 함수를 생성하여 계산기 프로그램을 생성해라
# print()
# print("문제 1)")


# def plus(x, y):
#     result = x + y
#     print("+식 : {0} + {1} = {2}".format(x, y, result))
#     return result

# def minus(x, y):
#     result = x - y
#     print("-식 : {0} - {1} = {2}".format(x, y, result))
#     return result

# def multi(x, y):
#     result = x * y
#     print("x식 : {0} x {1} = {2}".format(x, y, result))
#     return result

# def divide(x, y):
#     result = x / y
#     print("÷식 : {0} / {1} = {2}".format(x, y, result))
#     return result

# x = input("x값 : ")
# y = input("y값 : ")
# print()
# plus(int(x), int(y))
# minus(int(x), int(y))
# multi(int(x), int(y))
# divide(int(x), int(y))

# 함수의 매개변수가 몇개인지 모를 경우 함수 선언 방법
# 매개 변수의 이름 앞에 * 기호를 붙여서 선언
# 파이썬에서는 함수 오버로딩을 지원하지 않기 때문에 매개변수에 * 기호를 사용하여 매개변수를 튜플로 받고 그 튜플의 데이터 타입과 길이를 확인 하여 오버로딩을 구현함

# 매개변수로 리스트를 받았다고 생각하면 쉬움
print()
def sum_many(*args):
    sum = 0
    for i in args:  #매개 변수의 수 대로 값을 뽑아 냄
        sum += i
    return sum

print("매개변수가 1개인 sum_many의 합 : {0}".format(sum_many(1)))
print("매개변수가 1개인 sum_many의 합 : {0}".format(sum_many(1,2)))

# 반환값
# 기존 언어에서 반환값은 1개만 반환이 가능함
# 파이썬에서는 반환값은 튜플로 받아 2개 이상 반환할수 있음
# (사실 1개의 반환값임)
# 기존 언어에서는 반환값을 2개 이상 받기 위해 배열 및 리스트와 같은 자료 구조를 사용해여 값을 반환 받음

def sum_and_mul(a, b):
    return a + b, a * b

result = sum_and_mul(10, 20)
print(list(result))

print()
def sum_and_mul1(a, b):
    return a + b
    # return a * b 불가능>윗 라인에서 return문을 실행하였기에 함수의 실행이 완전 종료 되어 아래의 return문을 실행 할수 없음
    
# return문은 2개의 기능을 가지고 있다.
# 함수를 실행하고 그 결과값을 함수를 호출한 시점으로 반환하는것
# return문을 만나면 그 즉시 해당 함수를 종료함
result = sum_and_mul(10, 20)
print(list(result))

# 매개변수 초기값 지정하기
# 함수를 실행할 때 필요한 매개변수에 사용자가 모든값을 입력하는 현태가 아니라 기본적으로 필요한 값을 미리 지정해 놓고 사용자가 입력하지 않았을 경우에만 초기값으로 매개 변수가 초기화되어 함수를 실행하는 형태
# 초기값이 지정된 매개변수는 반드시 가장 마지막에 위치해야함
# 초기값이 지정된 매개변수가 중간에 위치하게 되면 함수 사용 시 초기값이 지정된 매개변수를 입력하지 않고 사용하였을 경우 그 다음에 있는 매개변수가 어디에 입력될지 확인이 불가능 하여 오류가 발생하게 됨
print()

def say_myself(name, old = 25 , man=True):
    print("나의 이름은 {0} 입니다.".format(name))
    print("나의 나이는 {0}살 입니다.".format(old))
    if man:
        print("나의 성별은 남자 입니다.")
    else:
        print("나의 성별은 여자 입니다.")

say_myself("윤수영", 27)
say_myself("윤수영", 27, True)
say_myself("윤수영")

# 변수의 사용 범위
# 기본적으로 변수는 변수가 선언된 함수 내부에서만 메모리에 살아있음
# 함수 외부에 선언된 변수와 함수 내부에 선언된 변수의 이름이 동일할 셩우 함수 내부에서는 함수 내부에 선언된 변수만 사용됨
# 함수 내부와 외부에 동일한 이름을 사용한 변수가 있을 경우 함수 외부의 변수를 사용하려면 grobal 키워드를 사용해야함

a = 1
def vartest(a):
    a += 1
    print("함수 내부에서 선언된 변수 a : {0}".format(a))
vartest(a)
print("함수 외부에서 선언된 변수 a : {0}".format(a))

print()
b = 1
def vartest2():
    global b
    b+=1
    print("global 키워드를 사용한 변수 a : {0}".format(b))
vartest2()
print("함수 외부의 변수 b : {0}".format(b))
