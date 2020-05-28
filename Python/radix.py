import sys

def radixSort(k, arr):

    diccionario = {'0' : 0, '1' : 1, '2': 2 ,
                    '3' : 3, '4' : 4, '5': 5,
                    '6' : 6, '7' : 7, '8': 8,
                    '9' : 9, 'A' : 10, 'B': 11,
                    'C' : 12, 'D' : 13, 'E': 14,
                    'F' : 15,
                    }

    for j in range(0,k):
        for i in range(1, len(arr)):
            index = i
            while(index > 0): 
                if(diccionario[arr[index][j]] < diccionario[arr[index - 1][j]] and arr[index][:j] == arr[index-1][:j]):
                    tmp = arr[index - 1]
                    arr[index - 1] = arr[index]
                    arr[index] = tmp
                    index-=1
                else:
                    break
        
        print(f"\nEn la posicion {j}th (De izquierda a derecha)")

        for x in arr: 
            print("".join(x))

    s = ""
    for x in arr:
        s+=  "".join(x)
        s+=","
    return s[:len(s)-1]


def main():

    try:
        f = open("radix.txt",'r')
        text = f.readlines()
        arr = [list(x) for x in text[1].split(",")]
    except:
        text = sys.argv[1]
        arr = [list(x) for x in text.split(",")]

    print("List unsorted: " + str(text[1]))
    arr = radixSort(int(text[0]), arr)  
    print("\nList sorted: " + str(arr))
  

if __name__ == "__main__":
    main()