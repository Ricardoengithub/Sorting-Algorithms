import sys

def quickSort(arr):
    return quick(arr, 0 , len(arr)-1)

def quick(arr, left, right):
    if(right <= left):
        return arr
    else:
        pivote = arr[left]
        izq = left+1
        der = right
        while(izq <= der):
            if(arr[izq] > pivote and arr[der] < pivote):
                tmp = arr[izq]
                arr[izq] = arr[der]
                arr[der] = tmp
                izq+=1
                der+=1
            else:
                if(arr[izq] >= pivote):
                    der-=1
                else:
                    izq+=1

        tmp = arr[left]
        arr[left] = arr[der]
        arr[der] = tmp

        quick(arr, left, der-1)
        quick(arr, izq, right)

    return arr
    
def main():

    try:
        f = open(str(sys.argv[1]),'r')
        text = f.readlines()
        arr = [int(x) for x in text[0].split(",")]
    except:
        text = sys.argv[1]
        arr = [int(x) for x in text.split(",")]

    print("List unsorted: " + str(arr))
    arr = quickSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
