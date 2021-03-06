import sys

def selectionSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr


def main():
    
    try:
        f = open(str(sys.argv[1]),'r')
        text = f.readlines()
        arr = [int(x) for x in text[0].split(",")]
    except:
        text = sys.argv[1]
        arr = [int(x) for x in text.split(",")]

    print("Unsorted: " + str(arr))
    arr = selectionSort(arr)  
    print("Sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
