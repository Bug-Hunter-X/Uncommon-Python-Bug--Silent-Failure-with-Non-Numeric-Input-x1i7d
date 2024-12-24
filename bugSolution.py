def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1, 2, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1, 2, 3, 4, 'a', 6, 7, 8, 'b', 10]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 