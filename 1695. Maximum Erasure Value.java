import java.util.HashSet;

class Solution {

    HashSet<Integer> set = new HashSet<>();
    public int maximumUniqueSubarray(int[] nums) {

        int currentSum = 0;
        int result = 0;

        int left = 0;
        int right = 0;

        while(right < nums.length){

            while(set.contains(nums[right])){
                currentSum -= nums[left];
                set.remove(nums[left]);
                left++;
            }

            currentSum += nums[right];
            set.add(nums[right]);
            result = Math.max(result,currentSum);
            right++;
        }

        return result;
    }
}