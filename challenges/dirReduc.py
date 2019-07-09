def dirReduc(arr):
    # new_arr = [x for x in arr if ]
    index = []
    count =0
    while count<len(arr):    
        for i , dir in enumerate(arr):
            if i != len(arr)-1:     
                if dir == "NORTH":
                    if arr[i+1] == "SOUTH":
                        index.append(i)
                        index.append(i+1)
                if dir == "SOUTH":
                    if arr[i+1] == "NORTH":
                        index.append(i)
                        index.append(i+1)

                if dir == "EAST":
                    if arr[i+1] == "WEST":
                        index.append(i)
                        index.append(i+1)
                if dir == "WEST":
                    if arr[i+1] == "EAST":
                        index.append(i)
                        index.append(i+1)
        count += 1
    print(str(index))
    while len(index ):
        arr.pop(index[len(index)-1])
        index.pop() 

    return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#  ['WEST']
print(dirReduc(a))
