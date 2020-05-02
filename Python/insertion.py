import sys

def insertionSort(arr):
    index = 1

    while(index < len(arr)):
        if(arr[index] < arr[index - 1]):
            tmp = arr[index - 1]
            arr[index - 1] = arr[index]
            arr[index] = tmp
            if(index == 1):
                index+=1
            else:
                index-=1
        else:
            index+=1

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
    arr = insertionSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()
