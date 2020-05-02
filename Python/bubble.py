import sys

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
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
    arr = bubbleSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
