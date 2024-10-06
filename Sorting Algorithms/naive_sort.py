
def naive_sort_ascending(arr: list[int]):
	i = 0
	c = 0
	while True:
		print(arr)
		if arr[i] > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
			i = -1
		if i == len(arr) - 2:
			break
		i += 1
		c += 1
	return arr, c
	

unsorted = [7,10,6,5,4,8,3,9,2,1]
print(naive_sort_ascending(unsorted))
		

