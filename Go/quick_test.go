package sorting

import (
	"testing"
)

func TestQuick(t *testing.T)  {
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
	}

	expected := []int{
		1,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9,
		10,
		100,
	}

	if compare(QuickSort(x), expected) == false {
		t.Errorf("Quick")
	}
}


func TestQuick2(t *testing.T)  {
	x := []int{
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
	}

	expected := []int{
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
		1,
	}

	if compare(QuickSort(x), expected) == false {
		t.Errorf("Quick2")
	}
}