import sys

def getMaximum(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def insertionSort(arr):
    
    for i in range(1, len(arr)):
        index = i

        while(index > 0):
            if(arr[index] < arr[index - 1]):
                tmp = arr[index - 1]
                arr[index - 1] = arr[index]
                arr[index] = tmp
                index-=1
            else:
                break

    return arr

def bucketSort(arr):
    bucket = len(arr)
    max = getMaximum(arr)
    arrAux = [None] * (bucket + 1)

    for i in range(0,len(arr)):
        index = int(arr[i] * (bucket / max))

        if arrAux[index] == None:
            arrAux[index] = [arr[i]]
        else:
            arrAux[index].append(arr[i])

    arr = []
    for i in range (0, len(arrAux)):
        if arrAux[i] == None:
            continue
        elif len(arrAux[i]) > 1:
            x = insertionSort(arrAux[i])
            for j in x:
                arr.append(j)
        else:
            arr.append(arrAux[i][0])
    
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
    arr = bucketSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
