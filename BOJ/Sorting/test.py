# 2751_수 정렬하기 2
import sys
from typing import List

sys.setrecursionlimit(10 ** 6)

# Function Sort
def function_sort(num_list):
    num_list.sort()
    return num_list


# Merge Sort
def merge_sort(num_list: List[int]) -> List[int]:

    # Devide
    if len(num_list) <= 1:  # 배열에 숫자가 한 개 이하면 리턴
        return num_list

    # 중간을 기준으로 두 그룹으로 나눔
    mid = len(num_list) // 2
    list_left = merge_sort(num_list[:mid])
    list_right = merge_sort(num_list[mid:])

    # Merge
    result = []
    li, ri = 0, 0
    while li < len(list_left) and ri < len(list_right):  # 두 배열에 모두 숫자가 남아있는 동안 반복
        if list_left[li] < list_right[ri]:  # 맨 앞 숫자 비교후 작은 것을 결과에 추가
            result.append(list_left[li])
            li += 1
        else:
            result.append(list_right[ri])
            ri += 1

    # 남아있는 것들 모두 결과에 추가
    result += list_left[li:]
    result += list_right[ri:]

    return result


# Quick Sort
def quick_sort(num_list):
    pass


# Heap Sort
def heap_sort(num_list):
    pass


N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
print("\n".join(map(str, function_sort(num_list))))
