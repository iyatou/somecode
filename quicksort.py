#快速排序思想：一句话总结就是东拆西补，西拆东补。
#对原始数组设置两个指针头和尾，以头作为基准，首先从右指针开始找到第一个比基准小的数，停止移动。
#覆盖移动左指针找到第一个比基准大的数，停止移动，覆盖，再次移动左指针，直到左右指针重合。记录基准位置。
#重复调用此函数对记录位置左右两侧进行如上操作，知道左指针和右指针重合。
def Sort(arraylist,_left,_right):
	left=_left
	right=_right
	if left<=right:
		temp=arraylist[left]
		while left<right:
			while left<right and arraylist[right]>=temp:
				right-=1
			arraylist[left]=arraylist[right]
			while left<right and arraylist[left]<=temp:
				left+=1
			arraylist[right]=arraylist[left]
		arraylist[right]=temp
		Sort(arraylist,_left,left-1)
		Sort(arraylist,right+1,_right)
	return arraylist
arraylist=[4,5,7,3,7,1,8,0,6]
left=0
right=len(arraylist)-1
arraylist1=Sort(arraylist,left,right)
print(arraylist1)