"""Binary search #TC O(log n) 
source : https://leetcode.com/problems/binary-search/"""

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left,right=0,len(arr)-1        
        while left<=right:
            mid =(left+right)//2 
            if arr[mid]==target :
                return mid 
            elif arr[mid]< target :
                left=mid+1 
            else: 
                right = mid-1
        return -1
