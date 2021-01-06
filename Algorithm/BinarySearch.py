
def BinarySearch(List,tar):
    left=0
    right=len(List)
    mid = (left+right)//2
    while right-left>1:
        print(left,right)
        if List[mid] >tar:
            right=mid
            mid = (left+mid)//2
        else:
            left=mid
            mid = (right+mid)//2
    if List[left]==tar:
        print(List[left])
        print(left)
        return True
    else:
        return False