import sys

def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    else:
        middle = len(arr)//2
        left = mergeSort(arr[0:middle])
        right = mergeSort(arr[middle:(len(arr))])
        merge(arr, left, right )
        return arr
    

def merge(arr, left, right):
    i, j, k = 0,0,0

    while(i < len(arr)):
        if(k >= len(left)):
            arr[i] = right[j]
            j+=1
        else:
            if(j >= len(right)):
                arr[i] = left[k]
                k+=1
            else:
                if(left[k] < right[j]):
                    arr[i] = left[k]
                    k+=1
                else:
                    arr[i] = right[j]
                    j+=1
        i+=1
    

def main():

    try:
        f = open(str(sys.argv[1]),'r')
        text = f.readlines()
        arr = [int(x) for x in text[0].split(",")]
    except:
        text = sys.argv[1]
        arr = [int(x) for x in text.split(",")]
        
    print("List unsorted: " + str(arr))
    arr = mergeSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
