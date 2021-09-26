# 2750_수 정렬하기

# Selection Sort
def selection_sort(num_list):
    for i in range(len(num_list)):
        min_num_idx = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_num_idx] > num_list[j]:
                min_num_idx = j
        num_list[i], num_list[min_num_idx] = num_list[min_num_idx], num_list[i]


# Bubble Sort
def bubble_sort(num_list):
    for i in range(len(num_list) - 1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]


# Insertion Sort
def insertion_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i, 0, -1):
            if num_list[j - 1] > num_list[j]:
                num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]


N = int(input())
num_list = [int(input()) for _ in range(N)]
insertion_sort(num_list)
print("\n".join(map(str, num_list)))
