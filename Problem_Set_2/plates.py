#plates.py
#https://cs50.harvard.edu/python/2022/psets/2/plates/
import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
  #Check start with at least two letters
  if s[:2].isalpha():
    #check length requirement
    if 1 < len(s) <= 6:
      #check if only alphabetical, it is valid
      if s.isalpha():
        return True
      #else additional checks need to be conducted  
      else:
        spec_char = set(string.punctuation)
        if not any (i in spec_char for i in s):
          for x in range(len(s)):
            if s[-1:].isalpha():
              return False
            elif s[x].isdigit():
              if s[x:].isdigit():
                if (s[x])!='0':
                  return True
                else:
                  return False
