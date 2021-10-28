from random import randint

def quicksort(list_of_ints: list) -> list:
    if len(list_of_ints) < 2:
        return list_of_ints
    else:
        rand_index = randint(0, len(list_of_ints)-1)
        pivot_val = list_of_ints[rand_index]
        less = [j for i, j in enumerate(list_of_ints) if j <= pivot_val and
                i != rand_index]
        greater = [i for i in list_of_ints if i > pivot_val]
        print(rand_index)
        print('list',  list_of_ints)
        print('pivot', pivot_val)
        print('less_list', less)
        print('greater_list', greater)
        return quicksort(less) + [pivot_val] + quicksort(greater)


def main() -> None:
    list_of_ints = [100, 44, 100, 77, 1, 10, 12]
    sorted_list = quicksort(list_of_ints)
    print(list_of_ints, ' sorted is: ', sorted_list)


if __name__ == '__main__':
    main()
