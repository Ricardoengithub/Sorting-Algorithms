import sys

def getMaximum(arr):

    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def getMiniimum(arr):

    min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


def countingSort(arr):

    izq = getMiniimum(arr)
    der = getMaximum(arr)
    
    aux = [0] * (der + 1)

    for x in range(0,len(arr)):
        aux[arr[x]]+=1                          #Revisa las frecuencias de cada elemento
    
    final = []
    for i in range(izq, der + 1):        #Une la lista dependiendo la frecuencia de cada elemento
        for j in range(0, aux[i]):
            final.append(i)

    return final


def main():

    try:
        f = open(str(sys.argv[1]),'r')
        text = f.readlines()
        arr = [int(x) for x in text[0].split(",")]
    except:
        text = sys.argv[1]
        arr = [int(x) for x in text.split(",")]

    print("List unsorted: " + str(arr))
    arr = countingSort(arr)  
    print("List sorted: " + str(arr))
  

if __name__ == "__main__":
    main()