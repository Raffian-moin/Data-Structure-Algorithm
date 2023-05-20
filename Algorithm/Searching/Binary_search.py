#--------------------------
# Iterative Binary Search
#--------------------------

a=[1, 3, 5, 6, 8, 10, 13]
x=6 # element to be searched
l=0
h=len(a)-1

def binarySearch(l, h):
    while l<=h:
        mid=l+(h-l)//2
        if a[mid]==x:
            return mid
        elif a[mid] > x:
            h=mid-1
        elif a[mid]< x:
            l=mid+1
    return -1

print(binarySearch(l, h))


#--------------------------
# Recursive Binary Search
#--------------------------

b=[1, 3, 5, 6, 8, 10, 13]
y=14 # element to be searched
n=0
f=len(b)-1

def recursiveBinarySearch(n, f, y):
    mid=n+(f-n)//2
    if n<=f:
        if b[mid]==y:
            return mid
        elif b[mid] > y:
            return recursiveBinarySearch(n, mid-1, y)
        elif b[mid]< y:
            return recursiveBinarySearch(mid+1, f, y)
    else:
        return -1

print(recursiveBinarySearch(n, f, y))
