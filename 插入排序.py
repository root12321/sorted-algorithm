
def charu(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0:
            if A[j]>=key:
                A[j+1]=A[j]
                A[j]=key
            j=j-1
    return A




print(charu([2,1,5,4,6,7,5]))