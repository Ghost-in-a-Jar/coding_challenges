class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        tot_len=len(nums1+nums2)
        n1=0
        n2=0
        merged=[]
        if nums1==[] or nums2==[]:
            merged=nums1+nums2
            if len(merged)%2==0:
                return (merged[(tot_len/2)-1]+merged[tot_len/2])/2.0
            else:
                return merged[tot_len/2]
        for i in range(1+tot_len/2):
            try:
                if nums1[n1]<nums2[n2]:
                    merged+=[nums1[n1]]
                    n1+=1
                else:
                    merged+=[nums2[n2]]
                    n2+=1
            except IndexError:
                if n1>len(nums1)-1:
                    merged+=[nums2[n2]]
                    n2+=1
                else:
                    merged+=[nums1[n1]]
                    n1+=1
        if tot_len%2==0:
            return (merged[-1]+merged[-2])/2.0
        else:
            return merged[-1]