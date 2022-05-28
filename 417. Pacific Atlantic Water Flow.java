import java.util.*;

class Cell {
    public int X;
    public int Y;

    Cell(Integer x, Integer y){
        X = x;
        Y = y;
    }
}

class Status {
    public boolean visitedAtlantic = false;
    public boolean visitedPacific = false;
}

class Solution {

    private int rows;
    private int columns;

    private List<Cell> calculateNextCells(Cell currentCell,int[][] heights,HashSet<List<Integer>> set){
        List<Cell> nextCells = new ArrayList<>();

        int currentHeight = heights[currentCell.X][currentCell.Y];

//      Go Bottom
        if(currentCell.X+1<rows && heights[currentCell.X+1][currentCell.Y] <= currentHeight){
            List<Integer> nextB = new ArrayList<>();
            nextB.add(currentCell.X+1);
            nextB.add(currentCell.Y);
            if(!set.contains(nextB)) {
                nextCells.add(new Cell(currentCell.X + 1, currentCell.Y));
            }
        }


//      Go Top
        if(currentCell.X-1>=0 && heights[currentCell.X-1][currentCell.Y] <= currentHeight){
            List<Integer> nextT = new ArrayList<>();
            nextT.add(currentCell.X-1);
            nextT.add(currentCell.Y);
            if(!set.contains(nextT)) {
                nextCells.add(new Cell(currentCell.X - 1, currentCell.Y));
            }
        }

//      Go Left
        if(currentCell.Y-1>=0 && heights[currentCell.X][currentCell.Y-1] <= currentHeight){
            List<Integer> nextL = new ArrayList<>();
            nextL.add(currentCell.X);
            nextL.add(currentCell.Y-1);
            if(!set.contains(nextL)) {
                nextCells.add(new Cell(currentCell.X, currentCell.Y-1));
            }
        }

//      Go Right
        if(currentCell.Y+1<columns && heights[currentCell.X][currentCell.Y+1] <= currentHeight){
            List<Integer> nextR = new ArrayList<>();
            nextR.add(currentCell.X);
            nextR.add(currentCell.Y+1);
            if(!set.contains(nextR)) {
                nextCells.add(new Cell(currentCell.X, currentCell.Y+1));
            }
        }

        return nextCells;
    }

    private Status checkForWaterFlow(Cell cell,Status status){

//      Check For Pacific Ocean ( Top Row & Left Row )
        if((cell.X == 0) && (cell.Y>=0 && cell.Y<columns)){
            status.visitedPacific = true;
        }

        if((cell.Y == 0) && (cell.X>= 0 && cell.X < rows)){
            status.visitedPacific = true;
        }

//      Check In Atlantic Ocean ( Bottom Row & Right Row )
        if((cell.X == rows-1) && (cell.Y>=0 && cell.Y<columns)){
            status.visitedAtlantic = true;
        }

        if((cell.Y == columns-1) && (cell.X>=0 && cell.X < rows)){
            status.visitedAtlantic = true;
        }

        return status;
    }

    private boolean depthFirstSearch(int[][] heights,Cell cell,Status status,HashSet<List<Integer>> set){

        List<Integer> nextB = new ArrayList<>();
        nextB.add(cell.X);
        nextB.add(cell.Y);

        set.add(nextB);

        List<Cell> nextCells = calculateNextCells(cell,heights,set);
        Status newStatus = checkForWaterFlow(cell,status);

        if(nextCells.size()==0){
//          If this is true, then add cell to result
            return (newStatus.visitedAtlantic && newStatus.visitedPacific);
        }

        for(Cell nextCell : nextCells){
            if(depthFirstSearch(heights,nextCell,newStatus,set)){
                return true;
            }
        }

//      Return with all directions i.e. north-south-east-west
        return false;
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {

        rows = heights.length;
        columns = heights[0].length;
        List<List<Integer>> result = new ArrayList<>();

        for(int i=0;i<heights.length;i++){
            for(int j=0;j<heights[i].length;j++){
                Cell cell = new Cell(i,j);
                Status status = new Status();
                HashSet<List<Integer>> set  = new HashSet<>();
                if(depthFirstSearch(heights,cell,status,set)){
                    List<Integer> res = new ArrayList<>();
                    res.add(i);
                    res.add(j);
                    result.add(res);
                }
            }
        }

        return result;
    }
}