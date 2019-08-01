
## select sort
def select(datalist):
    length = len(datalist)
    for i in range(length-1):
        index = i
        for j in range(i+1,length):
            if datalist[j] < datalist[i]:
                index = j
        tmp = datalist[i]
        datalist[i] = datalist[index]
        datalist[index] = tmp
    print(datalist)
    
datalist = [1,6,0,-1,-100,9,100]
select(datalist)
        




## bubble sort
def bubble(datalist):
    length = len(datalist)
    for i in range(length-1):
        for j in range(length-1-i):
            if (datalist[j] > datalist[j+1]):
                tmp = datalist[j]
                datalist[j] = datalist[j+1]
                datalist[j+1] = tmp
    print(datalist)
    
datalist = [1,6,0,-1,-100,9,100]
bubble(datalist)




##insertSort
def insertSort(datalist):
    length = len(datalist)
    for i in range(1,length):
        insertVal = datalist[i]
        index = i-1
        
        while (index >= 0 and insertVal< datalist[index]):
            datalist[index+1] = datalist[index]
            index -=1
        datalist[index+1] = insertVal
    print(datalist)

datalist = [1,6,0,-1,-100,9,100]
insertSort(datalist)






## ShellInsetSort
def ShellInsetSort(array, len_array, dk):  # 直接插入排序
    for i in range(dk, len_array):  # 从下标为dk的数进行插入排序
        position = i
        current_val = array[position]  # 要插入的数

        index = i
        j = int(index / dk)  # index与dk的商
        index = index - j * dk

        # position>index,要插入的数的下标必须得大于第一个下标
        while position > index and current_val < array[position-dk]:
            array[position] = array[position-dk]  # 往后移动
            position = position-dk
        else:
            array[position] = current_val



def ShellSort(array, len_array):  # 希尔排序
    dk = int(len_array/2)  # 增量
    while(dk >= 1):
        ShellInsetSort(array, len_array, dk)
        print(array)
        dk = int(dk/2)

# if __name__ == "__main__":
array = [49, 38, 65, 97, 76, 13, 27, 50, 55, 4]
print( array)
ShellSort(array, len(array))





## quick_sort
def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

L = [49, 38, 65, 97, 76, 13, 27, 50, 55, 4]
print (quick_sort(L))


