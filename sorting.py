import random


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
        if current_min != i:
            my_numbers_copy[i], my_numbers_copy[current_min] = my_numbers_copy[current_min], my_numbers_copy[i]

    return my_numbers_copy


def bubble_sort(my_numbers):
    my_numbers_bubble = my_numbers.copy()
    n=len(my_numbers_bubble)
    #swtich=1

    for i in range(n-1): #šlo by to taky přes počet výměn, while switch !=0
        for idx in range(n-1-i):
            if my_numbers_bubble[idx]>my_numbers_bubble[idx+1]: #switch +=1
                my_numbers_bubble[idx],my_numbers_bubble[idx+1] = my_numbers_bubble[idx+1], my_numbers_bubble[idx]

    return my_numbers_bubble


def main():
    my_numbers=random_numbers(20)

    sorted_numbers_selection=selection_sort(my_numbers)
    print(sorted_numbers_selection)

    sorted_numbers_bubble=bubble_sort(my_numbers)
    print(sorted_numbers_bubble)



if __name__ == "__main__":
    print(main())
