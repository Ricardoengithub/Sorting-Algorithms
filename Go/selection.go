package main

import "fmt"

func selection(arr []int) []int{

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

func main()  {
	x := []int{
		10,
		5,
		9,
		1,
		4,
		3,
		2,
		7,
		8,
		6,
		100,
		0,
		-100,
	}

	fmt.Println(selection(x))	
}