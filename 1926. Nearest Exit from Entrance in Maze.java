import java.util.*;

class Node {
    int x;
    int y;

    Node(int x,int y){
        this.x = x;
        this.y = y;
    }
}
class CellData {
    Node node = new Node(-1,-1);
    int len = 0;

    CellData(int x,int y, int len){
        this.node.x = x;
        this.node.y = y;
        this.len = len;
    }

    CellData(int x,int y){
        this.node.x = x;
        this.node.y = y;
    }
}

class Solution {

    HashSet<List<Integer>> set = new HashSet<>();

    private List<Node> fetchNextCells(Node cur,char[][] maze){

        List<Node> nextCells = new ArrayList<>();

        List<Integer> topVals = new ArrayList<>();
        topVals.add(cur.x-1);
        topVals.add(cur.y);

//      Go Top
        if(cur.x-1>=0 && maze[cur.x-1][cur.y] != '+' && !set.contains(topVals)){
            nextCells.add(new Node(cur.x-1,cur.y));
        }

        List<Integer> botVals = new ArrayList<>();
        botVals.add(cur.x+1);
        botVals.add(cur.y);

//      Go Bottom
        if(cur.x+1< maze.length && maze[cur.x+1][cur.y] != '+' && !set.contains(botVals)){
            nextCells.add(new Node(cur.x+1,cur.y));
        }

        List<Integer> rightVals = new ArrayList<>();
        rightVals.add(cur.x);
        rightVals.add(cur.y+1);

//      Go Right
        if(cur.y+1<maze[0].length && maze[cur.x][cur.y+1] != '+' && !set.contains(rightVals)){
            nextCells.add(new Node(cur.x, cur.y+1));
        }

        List<Integer> leftVals = new ArrayList<>();
        leftVals.add(cur.x);
        leftVals.add(cur.y-1);

//      Go Left
        if(cur.y-1>=0 && maze[cur.x][cur.y-1] != '+' && !set.contains(leftVals)){
            nextCells.add(new Node(cur.x,cur.y-1));
        }

        return nextCells;
    }

    private boolean isExit(char[][] maze, int[] entrance, Node cur){

//      Exit cant be entrance
        if(cur.x == entrance[0] && cur.y == entrance[1]){
            return false;
        }

        // Left Column
        if(cur.y==0 && cur.x >= 0 && cur.x <= maze.length){
            return true;
        }

//      Right Column
        if(cur.y==maze[0].length-1 && cur.x >= 0 && cur.x <= maze.length){
            return true;
        }

//      Top Row
        if(cur.x == 0 && cur.y>=0 && cur.y < maze[0].length){
            return true;
        }

//      Bottom Row
        if(cur.x == maze.length-1 && cur.y>=0 && cur.y < maze[0].length){
            return true;
        }


        return false;
    }

    public int nearestExit(char[][] maze, int[] entrance) {

        int notFound = -1;

        Queue<CellData> queue = new LinkedList<>();
        queue.add(new CellData(entrance[0],entrance[1]));

        List<Integer> ent = new ArrayList<>();
        ent.add(entrance[0]);
        ent.add(entrance[1]);
        set.add(ent);

        while(queue.size()>0){

            CellData cur = queue.poll();

            List<Node> nextCells = fetchNextCells(cur.node,maze);

            for(Node node: nextCells){
                if(isExit(maze,entrance,node)){
                    return cur.len+1;
                }

                List<Integer> nodeList = new ArrayList<>();
                nodeList.add(node.x);
                nodeList.add(node.y);

                set.add(nodeList);
                queue.add(new CellData(node.x,node.y,cur.len+1));
            }

        }

        return notFound;
    }
}