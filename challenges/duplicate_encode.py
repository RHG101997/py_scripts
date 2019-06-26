'''
The goal of this exercise is to convert a string to a new
 string where each character in the new string is
  "(" if that character appears only once in the original 
  string, or ")" if that character appears more than once in the original string.
   Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

'''


# def duplicate_encode(word):
#     encode =[] 
#     word = word.lower()
#     print(word)
#     for letter in  word:
#         if word.count(letter) < 2:
#             encode.append("(")
#         else:
#             encode.append(")")
#     return "".join(str(x)for x in encode)



def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))