package main

import "fmt"

func insertion(arr []int) []int{

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

	fmt.Println(insertion(x))	
}