# Write a function to take an array and return another array that contains the members of the first array that are even.
def get_even_numbers(numbers):
    even_numbers = list()
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)
    
numbers1 = [number for number in range(1,11)]
numbers2 = [number for number in range(50,101)]
    
get_even_numbers(numbers1)
get_even_numbers(numbers2) 