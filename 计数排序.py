def counting_sort(A):
    C=[]
    B=[]
    for i in range(0,max(A)+1):
        C.append(0)
    print(C)#调试C
    for j in range (0,int(len(A))):
        C[A[j]]=C[A[j]]+1
    print(C)#调试C
    for i in range(1,max(A)+1):
        C[i]=C[i]+C[i-1]
    print(C)#调试C

    for i in range(0,max(C)):
        B.append(0)
    print(B)#调试B
    for k in range(int(len(A))-1,-1,-1):
        print(k)#用来做检测用
        B[C[A[k]]-1]=A[k]#C[A[k]]-1是因为 列表B是从索引0开始到索引7，而不是从1-8.
        C[A[k]]=C[A[k]]-1
    return B


print(counting_sort([20,19,8,2,3,2,5,4,6]))

