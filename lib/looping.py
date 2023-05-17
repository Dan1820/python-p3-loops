#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
        print("Happy New Year")


def square_integers(int_list):
    # code goes here!
    square_num = [num**2 for num in int_list]
    return square_num


def fizzbuzz(num):
    # code goes here!
    for i in range(1, 101):
        if num % 3 == 0 & num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num


# # i=0
# # while i<5:
# #     print("Looping")
# #     i+=1

# for i in range(10):
#     print("looping")
#     print(f"i is:{i}")
