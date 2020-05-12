package main

import "fmt"

func bubble(arr []int) []int{

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

	fmt.Println(bubble(x))	
}