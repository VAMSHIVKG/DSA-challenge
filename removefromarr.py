# remove an element from array without creating second array

def rmv(arr):
    k=0
    cnt=0
    for i in range(len(arr)):
        if arr[i]==e:
            cnt+=1
            continue
        else:
            arr[k]=arr[i]
            k+=1

    for j in range(k,len(arr)):
        arr[j]="_"
    return arr

arr=[3,2,2,7,3]
e=3
print(rmv(arr))