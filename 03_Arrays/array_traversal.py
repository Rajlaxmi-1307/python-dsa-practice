# Create a list of student marks
marks = [75, 82, 68, 96, 77]

# Print the complete list
print("Complete array:", marks)

# Access and print the first element (index 0)
print("First element:", marks[0])

# Access and print the second element (index 1)
print("Second element:", marks[1])

# Access and print the third element (index 2)
print("Third element:", marks[2])

# Access and print the fourth element (index 3)
print("Fourth element:", marks[3])

# Insert 77 at index 3 (fourth position)
# Existing elements from index 3 onwards shift to the right
marks.insert(3, 77)

# Print the updated list
print("Updated array:", marks)