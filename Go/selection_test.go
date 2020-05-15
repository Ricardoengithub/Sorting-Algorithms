package sorting

import (
	"testing"
)

func compare(a, b []int) bool {
    if len(a) != len(b) {
        return false
    }

    for i := 0; i < len(a); i++ {
        if a[i] != b[i] {
            return false
        }
    }
    return true
}

func TestSelection(t *testing.T)  {
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

	if compare(SelectionSort(x), expected) == false {
		t.Errorf("Selection")
	}
}


func TestSelection2(t *testing.T)  {
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

	if compare(SelectionSort(x), expected) == false {
		t.Errorf("Selection2")
	}
}