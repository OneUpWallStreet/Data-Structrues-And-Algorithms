import java.util.HashMap;

class Solution {

    public void sortColors(int[] nums) {

        HashMap<Integer,Integer> map = new HashMap<>();
        map.put(0,0);
        map.put(1,0);
        map.put(2,0);

        for(int key : nums){
            map.put(key, map.get(key) + 1);
        }

        int i = map.get(0);

        int index =0;

        while(i>0){
            nums[index] = 0;
            i--;
            index++;
        }

        i = map.get(1);

        while(i>0){
            nums[index] = 1;
            i--;
            index++;
        }

        i = map.get(2);

        while(i>0){
            nums[index] = 2;
            i--;
            index++;
        }
        

    }
}