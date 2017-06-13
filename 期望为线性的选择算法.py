def random(A,p,r,i):
    if p==r:
        return A[p]
    q=part(A,p,r)
    k=q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return random(A,p,q-1,i)
    elif i>k:
        return random(A,q+1,r,i-k)


def part(A,p,r):

    temp=0#中间变量，用来交换下面的A[i]和A[j]的顺序
    x=A[r]
    i=p-1

    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp

    temp=A[r]
    A[r]=A[i+1]
    A[i+1]=temp
    return i+1


array = [1,2,3,5,0,4,6,9,8,7]
print(random(array,0,len(array)-1,4))