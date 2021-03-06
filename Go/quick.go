package sorting

func QuickSort(arr []int) []int{

	return quick(arr, 0, len(arr) -1)
}

func quick(arr []int, left int, right int) []int{
	if right <= left{
		return arr
	}else{
		pivote := arr[left]
		izq := left+1
		der := right

		for izq <= der{
			if arr[izq] > pivote && arr[der] < pivote{
				tmp := arr[izq]
				arr[izq] = arr[der]
				arr[der] = tmp
				izq++
				der--
			}else if arr[izq] >= pivote{
				der--
			} else{
				izq++
			}
		}
		tmp := arr[left]
		arr[left] = arr[der]
		arr[der] = tmp
		quick(arr, left, der-1)
		quick(arr, izq, right)
	 }
	 
	return arr
}