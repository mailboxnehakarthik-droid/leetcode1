class Solution(object):
    def findMedianSortedArrays(self, a, b):
        i=j=0
        result=[]
        while i<len(a) and j <len(b):
            if a[i]<b[j]:
                result.append(a[i])
                i+=1
            else:
                result.append(b[j])
                j+=1
        result.extend(a[i:]) 
        result.extend(b[j:])
        if len(result)%2==0:
            pos=len(result)//2                       
            median= (result[pos]+result[(pos-1)])/2.0
        else:
            pos=len(result)//2
            median=result[pos]   
        return median     

