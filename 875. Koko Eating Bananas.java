import java.util.Arrays;

class Solution {
    public int minEatingSpeedBruteForce(int[] piles, int h) {

        int speed = 1;
        int hours;
        while (true){
            hours =0;

            for(int pile : piles){
                hours += Math.ceil((double) pile / speed);
            }

            if(hours<=h){
                return  speed;
            }else{
                speed++;
            }
        }
    }

    public int minEatingSpeedBinary(int[] piles, int h) {

        Arrays.sort(piles);
        int mid;
        int left = 0;
        int right = piles[piles.length-1];
        int hours;
        int result = piles[piles.length-1];


        while(left<=right){
            mid = left + (right - left) / 2;
            hours = 0;

            for (int pile : piles ){
                hours += Math.ceil((double) pile/mid);
            }

            if(hours<=h){
                result = Math.min(mid,result);
                right = mid-1;
            }else{
                left = mid+1;
            }
        }

        return  result;

    }
}


