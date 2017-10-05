
def partition(nums,left,right):
    if left >= right:
        return nums
    pivot=nums[left]
    low=left
    high=right
    while low<high:
        while nums[high]>=pivot and low<high:
            high-=1
        while nums[low]<=pivot and low<high:
            low+=1
        if low<high:
            nums[low],nums[high]=nums[high],nums[low]
    mid=high
    nums[left],nums[mid]=nums[mid],nums[left]
    partition(nums,left,mid-1)
    partition(nums,mid+1,right)
    return nums

def quick_sort2(lists, left, right):

    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort2(lists, low, left - 1)
    quick_sort2(lists, left + 1, high)
    return lists
if __name__=='__main__':
    nums=[6,1,2,7,9,3,4,5,10,8]
    #print nums
    #print quick_sort2(nums,0,len(nums)-1)
    print partition(nums,0,len(nums)-1)


