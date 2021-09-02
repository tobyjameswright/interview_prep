def fizz_buzz(iterations: int, list_divisor: list = [], list_words: list = []) -> None:
    """
    FizzBuzz: The well known numbers game, for a certain number of iterations
    print the number and then + 1. If the number is divisible by a provided
    divisior then print a given word instead. If the number is divisible by all
    of the provided divisiors then print all the words
    """
    if len(list_divisor) != len(list_words):
        print(len(list_divisor))
        print(len(list_words))
        print(list_divisor)
        print(list_words)
        raise ValueError('The entered lists are of different lengths')
    for i in range(1, iterations+1):
        output = ""
        for j in range(len((list_divisor))):
            if i % int(list_divisor[j]) == 0:
                output += list_words[j].replace(' ', '')
        if output == "":
            print(i)
        else:
            print(output)

def main():
    print('#' * 50)
    print('Welcome to fizzbuzz, please choose you desired set up below')
    iterations = int(input('Please enter the number of iterations for the game:'))
    list_divisor = input('Please enter a list of divisors in the format x, y: ').split(',')
    list_words = input('Please enter the list of words to print in the format x, y: ')
    list_words = list_words.split(',')
    fizz_buzz(iterations, list_divisor, list_words)

if __name__ == '__main__':
    main()
