import random
from operator import index


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(my_numbers):
    my_numbers_copy=my_numbers.copy()
    n= len(my_numbers_copy)
    for i in range(n):
        current_min=i
        for idx in range(i+1,n):
            if my_numbers_copy[idx]<my_numbers_copy[current_min]:
                current_min=idx
        my_numbers_copy[i], my_numbers_copy[current_min] = my_numbers_copy[current_min], my_numbers_copy[i]

    return my_numbers_copy


def main():
    my_numbers=random_numbers(5)
    sorted_numbers=selection_sort(my_numbers)
    print(sorted_numbers)


if __name__ == "__main__":
    print(selection_sort([52,45,11,0,25,0,32]))
