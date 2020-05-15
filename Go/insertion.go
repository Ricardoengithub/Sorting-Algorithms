package sorting

func InsertionSort(arr []int) []int{

	var index int
	for i:=1; i < len(arr); i++{		
		index = i

		for index > 0{
			if arr[index] < arr[index-1] {
				var tmp int = arr[index]
				arr[index] = arr[index-1]
				arr[index-1] = tmp
				index--
			}else{
				break
			}				
		}
	}
	return arr
}