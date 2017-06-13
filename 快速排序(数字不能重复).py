def quick(A,p,r):
    if p<r:
        q=part(A,p,r)

        quick(A,p,q-1)
        quick(A,q+1,r)
    return A

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


A=[4,5,8,6,2]

print(quick(A,0,4))





