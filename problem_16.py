# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = [45, 89, 12, 78, 34]
# handle duplicates and short lists safely
unique_numbers = sorted(set(numbers))
if len(unique_numbers) < 2:
	print("No second largest number (list too small or all values equal)")
else:
	second_largest = unique_numbers[-2]
	print(f"Second largest: {second_largest}")
