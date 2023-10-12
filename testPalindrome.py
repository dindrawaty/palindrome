
#Palindrome
# How to set up two pointers in an array

def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        if (array[left] != array[right]):
           return False 
        left = left + 1
        right = right -1 
    return True

def is_palindrome(s):
  # Write your code here
  s = list(s)
  r = two_pointers(s)
  if (r):
    print("It is polindrome")
  else:
    print("it is not a polindrome")
  # Tip: You may use the code template provided
  # in the two_pointers.py file
  return r

is_palindrome("kayak")