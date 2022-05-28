class Solution {

    private int counter = 0;

    private void countSteps(int num){
        if(num==0){
            return;
        }
        counter++;
        if(num%2==0){
            countSteps(num/2);
        }
        else{
            countSteps(num-1);
        }
    }

    public int numberOfSteps(int num) {
        countSteps(num);
        return counter;

    }
}
