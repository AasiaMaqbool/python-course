def highest_even(li):
    evens=[]
    for items in li:
       if items %2 ==0:
        evens.append(items)
    return max(evens)

print(highest_even([10,2,3,6,8,29,20,78]))