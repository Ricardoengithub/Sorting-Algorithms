package sorting

func SelectionSort(arr []int) []int{

	var minimo int = 0
	for i:=0; i < len(arr); i++{		
		minimo = i

		for j:=i+1; j < len(arr); j++{

			if(arr[j] < arr[minimo]){
				minimo = j
			}
		}
		var tmp int = arr[i]
		arr[i] = arr[minimo]
		arr[minimo] = tmp
	}
	return arr
}