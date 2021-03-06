def find_same_number(some_list, start=1, end=None):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    if end==None:
        end = len(some_list)-1
    if start == end:
        return start
    mid = (start+end)//2
    left_count=0
    for element in some_list:
        if start<=element and element<=mid:
            left_count+=1
    if left_count>mid-start+1:
        return find_same_number(some_list,start,mid)
    return find_same_number(some_list,mid+1,end)
# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))