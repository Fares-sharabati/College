import random
def main():
    even = 0
    odd = 0
    for counter in range(100):
        number = random.randint(1, 1000)
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
main()
