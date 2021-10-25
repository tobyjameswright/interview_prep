import math


def guess_number(total_number: int, number: int) -> tuple[int, int]:
    """ set up the sorted list of length total_number
        use binary search to guess the number until the guessed number is
        correct
    """
    sorted_list = create_list(total_number)
    number, steps = binary_search(number, sorted_list)
    return number, steps


def binary_search(number: int, sorted_list: list, steps: int = 0) -> tuple[int, int]:
    length = len(sorted_list)
    guess = sorted_list[length // 2]
    print('Guess; ', guess, 'Number; ', number, 'Equality; ', guess == number,
          'Steps; ',  steps)
    steps += 1
    if guess > number:
        guess, steps = binary_search(number, sorted_list[:length//2], steps)
    elif guess < number:
        guess, steps = binary_search(number, sorted_list[length//2:], steps)
    return guess, steps


def create_list(total_number: int) -> list:
    sorted_list = [num + 1 for num in range(total_number)]
    return sorted_list


def main() -> None:
    print('Python script that implements binary search to guess a number')
    total_number = int(input('Please enter the total elements in the numbered list: '))
    number = int(input('Please enter your number to be guessed: '))
    number, steps = guess_number(total_number, number)
    print(f"Your number is {number}")
    print(f"Total steps taken = {steps}")
    print(f'Maximum possible steps = {math.ceil(math.log(total_number, 2))}')


if __name__ == '__main__':
    main()
