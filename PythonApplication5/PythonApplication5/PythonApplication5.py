
string1 = input("enter any word: ")
def palindrome_example(string1):
   actual_string= list(string1)
   Reverse_string = list(string1)
   Reverse_string.reverse()
   if actual_string == Reverse_string:
      return True
   else:
      return False
print (palindrome_example(string1))
