def quicksort(list_of_ints: list) -> list:
    if len(list_of_ints) < 2:
        return list_of_ints
    else:
        pivot_val = list_of_ints[0]
        less = [i for i in list_of_ints[1:] if i <= pivot_val]
        greater = [i for i in list_of_ints[1:] if i > pivot_val]
        return quicksort(less) + [pivot_val] + quicksort(greater)


def main() -> None:
    list_of_ints = [100, 44, 100, 77, 1, 10, 12]
    sorted_list = quicksort(list_of_ints)
    print(list_of_ints, ' sorted is: ', sorted_list)


if __name__ == '__main__':
    main()
