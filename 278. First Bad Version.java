class Solution {

    private boolean isBadVersion(int version) {
        if(version >=1){
            return true;
        }
        return false;
    }
    
    private int binarySearch(int min,int left,int right) {
        if(left<=right){
            int mid = left + (right-left)/2;
            if(isBadVersion(mid)){
                min = Math.min(min,mid);
                return binarySearch(min,left,mid-1);
            }else{
                return binarySearch(min,mid+1,right);
            }
        }
        return min;
    }

    public int firstBadVersion(int n) {
        return binarySearch(Integer.MAX_VALUE,0,n);
    }
}