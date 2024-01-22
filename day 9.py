array_size = int(input("Enter the size of the array: "))

data = []

for i in range(array_size):
  num = int(input(f"Enter element {i+1}: "))
  data.append(num)

def find_max_min(data):
  """
  Finds the maximum and minimum elements in a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    A tuple containing the maximum and minimum elements in the list.
  """
  if len(data) == 0:
    return None, None

  max_value = data[0]
  min_value = data[0]

  for element in data:
    if element > max_value:
      max_value = element
    if element < min_value:
      min_value = element

  return max_value, min_value

max_value, min_value = find_max_min(data)

print(f"Maximum element: {max_value}")
print(f"Minimum element: {min_value}")
