class Solution {
    public int minEatingSpeed(int[] piles, int h) {

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
}
