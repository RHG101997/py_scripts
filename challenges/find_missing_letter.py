'''
Coding war
    **Only works if missing 1 letter
    **the sequence needs to be in order with 1 letter
       missing in between
    **It is not the best way to solve this problem


    HOW IT WORKS:

    ord() -> change char to Unicode(numbers)

    truth[] -> get first number from toUnicode
            and loop adding one until the #
            is equal to the last # in toUnicode[]

    return [1 char](the missing one by comparing
            both list and seen the missing # in toUnicode)
            **chr() the reverse from ord()
'''

def find_missing_letter(chars):
    toUnicode =[ord(letter) for letter in chars]
    truth =[toUnicode[0]]
    while truth[-1] != toUnicode[-1]:
        truth.append(truth[-1]+1)
    
    # print(str(toUnicode))
    # print(str(truth))
    print(chars, end="")
    print(" missing->" + str(chr([x for x in truth if x not in toUnicode][0])))    
    


find_missing_letter(['a','b','c','d','f'])
find_missing_letter(['a','b','e','d','f'])
find_missing_letter(['o','p','q','s','t'])