def rec_get_max(list_of_ints: list) -> int:
    if list_of_ints == []:
        max_value = 0
        return max_value
    else:
        max_value = rec_get_max(list_of_ints[1:])
        if list_of_ints[0] > max_value:
            return list_of_ints[0]
        else:
            return max_value

def main() -> None:
    list_of_ints = [100, 3, 6, 7, 10]
    print(list_of_ints, 'largest value is: ', rec_get_max(list_of_ints))


if __name__ == '__main__':
    main()
