class Solution {

    private int longestCount = 1;

    private void depthFirstTraversal(int index,int currentValue, int pathCount){

        pathCount++;
        longestCount = Math.max(longestCount,pathCount);

        for(int i = index;i<numbers.length;i++){
            if(numbers[i] >= currentValue){
                depthFirstTraversal(i+1,numbers[i],pathCount);
            }
        }


    }

    public int lengthOfLIS(int[] nums) {

        numbers = nums;
        for(int i=0;i<nums.length;i++){
            depthFirstTraversal(i+1,nums[i],0);
        }
        return longestCount;
    }

    private int[] numbers;
}
