# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
k = x + y
print(k)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
l = k.pop(4)
print(k)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
k.insert(5, 99)
print(k)

# Print the length of list x
# YOUR CODE HERE
print(len(k))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for elem in k:
  print(elem * 1000)
  