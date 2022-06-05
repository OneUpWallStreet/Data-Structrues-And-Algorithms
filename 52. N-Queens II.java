import java.util.HashSet;

class Solution {

    private HashSet<Integer> colSet = new HashSet<>();
    private HashSet<Integer> posDiagSet = new HashSet<>();
    private HashSet<Integer> negDiagSet = new HashSet<>();
    private Integer n;
    private Integer result = 0;

    private void backTracking(int row){

        if(row==n){
            System.out.println("addding: "+ row);
            result++;
            return;
        }

        for(int col=0;col<n;col++){

            if(colSet.contains(col) || posDiagSet.contains(col+row) || negDiagSet.contains(row-col)){
                continue;
            }

            colSet.add(col);
            posDiagSet.add(row+col);
            negDiagSet.add(row-col);

            backTracking(row+1);

            colSet.remove(col);
            posDiagSet.remove(row+col);
            negDiagSet.remove(row-col);

        }

    }

    public int totalNQueens(int n) {
        this.n = n;
        backTracking(0);
        return  result;
    }
}