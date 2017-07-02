import math

A = [10, 5, 2, 4, 6, 1, 3, 9, 7, 8]

def merge_sort(arr):
	if(len(arr) > 1):
		middle = int(len(arr)/2)
		before_list = arr[:middle]
		after_list = arr[middle:]
		merge_sort(before_list)
		merge_sort(after_list)

		i = 0
		j = 0
		k = 0

		while(i < len(before_list) and j < len(after_list)):
			if(before_list[i] < after_list[j]):
				arr[k] = before_list[i]
				i = i + 1
			else:
				arr[k] = after_list[j]
				j = j + 1
			k = k + 1

		while(i < len(before_list)):
			arr[k] = before_list[i]
			i = i + 1
			k = k + 1

		while(j < len(after_list)):
			arr[k] = after_list[j]
			j = j + 1
			k = k + 1
		if(len(arr) == 10):
			print(arr)

merge_sort(A)