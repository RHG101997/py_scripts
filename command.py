# action = input("\n->")
# if str(action) == "info":
#    print("Information")
# else:
#     print(str(action))


def bytes_to_decimal(i,d):
    xx = i - 127
    dec = (-d if xx < 0 else d)/100
    return xx + dec
 