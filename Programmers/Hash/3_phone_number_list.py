# 3_phone_number_list
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution0(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


"""
답은 맞으나 효율성 테스트 시간 초과 : n^2 번 비교하였기 때문
=> 시간을 줄일 수 있는 방법은??
"""


def solution1(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


"""
사전 순으로 나열 후 연속된 전화번호만 비교해보면 됨
=> why? 사전 순으로 나열 시 연속된 두 번호가 성립 안한다면 뒤에있는 전화번호는 반드시 성립 안함 
"""


def solution2(phone_book):
    prefix_dict = {}
    for p in phone_book:
        for i in range(1, len(p)):
            prefix_dict[p[:i]] = 1

    for p in phone_book:
        if p in prefix_dict:
            return False
    return True


"""
phone_book 의 접두사 후보군을 dict 로 생성
이후 phone_book 내의 전화번호가 dict 에 있는지 확인. 즉, 접두사 목록안에 전화번호가 있는지 확인
자기 자신을 넣지 않는 이유? 자기 자신을 넣으면 해당 단어가 자기 자신인지 접두어인지 구분 불가. 또한 자기 자신이 다른 단어의 접두어가
되는 경우, 자기 자신을 넣지 않더라도 다른 단어에 의해 접두사 후보군에 생성될 것

hash 를 사용한다고 하여 phone_book 을 dict 으로 만들어 접두사를 찾을 생각만 하였음. 이런 풀이는 적합하지 않아 다른 풀이 시도
"""


def solution3(phone_book):
    map = {}
    for phone_number in phone_book:
        map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in map and temp != phone_number:
                return False
    return True


"""
phone_book 을 dict 으로 생성
전화번호의 접두사 후보가 dict 에 있는지 확인
"""

phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
# phone_book = ["12", "123", "1235", "567", "88"]

print(solution2(phone_book))
