def move_zeros(array):
    # Pass evrything except 0 and include [False (since python 
    # thinks False == 0 )]
    # is -singelton 
    new_array = [x for x in array if x is False or x != 0]
    # get the diferences on the sizes and add those as 0 at the end.
    numberOfZeros = len(array)-len(new_array)
    i = 0
    while i < numberOfZeros:
        new_array.append(0)
        i += 1
    return new_array



array = move_zeros(["a",0.0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
print(array)
