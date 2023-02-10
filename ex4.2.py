def replace(array,index,newvalue):
    last=len(array)-1
    array[index],array[last]=array[last],array[index]

    array.pop()
    array.append(newvalue)

    array[index],array[last]=array[last],array[index]

    return array

