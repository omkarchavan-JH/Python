pos = -1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos'] = i
            return  True
        i +=1
    return False

    # for i in list:
    #     if i==n:
    #         print(i)
    #         return True





list = [5,8,4,6,9,2]
n = 9

if search(list,n):
    print("Found at ",pos)
else:
    print("Not Found")