package sorting

func MergeSort(arr []int) []int{
	if len(arr) <= 1{
		return arr
	}else{
		middle := int(len(arr) / 2)

		left := MergeSort(arr[0:middle])
		right := MergeSort(arr[middle:len(arr)])

		return merge(left, right)
	}
}

func merge(izq []int, der []int) []int{
	var (
		i = 0
		j = 0
		k = 0
	)

	arr := make([]int, len(izq) + len(der))
	for i = 0; i < len(izq) + len(der); i++ {

		if j >= len(izq){
			arr[i] = der[k]
			k+=1
			continue
		}else if k >=len(der){
				arr[i] = izq[j]
				j+=1
				continue
			}
		
		if izq[j] <= der[k]{
			arr[i] = izq[j]
			j+=1 
		}else{
			arr[i] = der[k]
			k+=1
		}			
	}
 
	return arr
}