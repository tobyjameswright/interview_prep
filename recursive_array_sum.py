def rec_sum(list_to_sum: list) -> int:
    if list_to_sum == []:
        return 0
    else:
        return list_to_sum[0] + rec_sum(list_to_sum[1:])


def main() -> None:
    list_to_sum = [3, 6, 7, 10]
    print(list_to_sum, 'summed is: ', rec_sum(list_to_sum))


if __name__ == '__main__':
    main()
