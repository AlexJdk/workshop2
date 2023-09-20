def findmax(a):
    if len(a) == 0:
        return 0
    curr_max = a[0]
    for i in a:
        if i > curr_max:
            curr_max = i
    return curr_max
