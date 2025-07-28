class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        satisfied=left=right=cus=maxcus=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                satisfied+=customers[i]
        for right in range(len(grumpy)):
            if grumpy[right]!=0:
                cus+=customers[right]
            if right-left+1 > minutes:
                if grumpy[left]==1:
                   cus-=customers[left]
                left+=1
            maxcus=max(cus,maxcus)
        return maxcus+satisfied



            
        