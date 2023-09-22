# Write a function that takes 2 arrays and prints the members of the first array that are present in the second array.
def get_common_numbers(numbers1, numbers2):
    common_numbers = list()
    for number in numbers1:
        if number in numbers2:
            common_numbers.append(number)
    print(common_numbers)
    
numbers1 = [number for number in range(1,11)]
numbers2 = [number for number in range(5,16)]

get_common_numbers(numbers1, numbers2)