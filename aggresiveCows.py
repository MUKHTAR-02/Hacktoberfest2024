def cows_can_place(diff,a,cows,n):
    count=1
    curr=0
    for i in range(1,n):
        if(a[i]-a[curr]>=diff):
            count+=1
            curr=i
        if(count==cows):
            return True
    return False        

n=4
a=[1,2,4,8,9]
cows=3
a.sort()
low=1
high=a[n-1]-a[0]
res=-1
while(low<=high):
    mid=(low+high)/2
    if(cows_can_place(mid,a,cows,n)):
        res=mid
        low=mid+1
    else:
        high=mid-1
if(res==-1):
    print(False)
else:
    print(True)
