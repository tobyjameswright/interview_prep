def rec_count(list_to_count: list) -> int:
    if list_to_count == []:
        return 0
    else:
        return 1 + rec_count(list_to_count[1:])


def main() -> None:
    list_to_count = [3, 6, 7, 10]
    print(list_to_count, 'total elements is: ', rec_count(list_to_count))


if __name__ == '__main__':
    main()
