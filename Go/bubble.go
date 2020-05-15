package sorting

func BubbleSort(arr []int) []int{

	for i:=1; i < len(arr); i++{		
		for j := 0; j < len(arr)-1; j++ {
			for arr[j] > arr[j+1]{
				var tmp int = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp
			}
		}
	}
	return arr
}