from random import randint
from typing import List

"""
선택정렬
"""

array: List[int] = []

for _ in range(10000):
    array.append(randint(1, 100))


for i in range(len(array)):
    min_index = i

    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]


"""
기본 정렬
"""

array: List[int] = []

for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 사용
array.sort()

print(array)
