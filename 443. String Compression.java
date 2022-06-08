import java.util.*;

class Node {
    char c;
    int count;
    Node(char c){
        this.c = c;
        this.count = 1;
    }
}

class Solution {

    Stack<Node> stack = new Stack<>();
    int output = 0;
    int indexCounter = 0;
    
    private char[] intToArray(int num){
        String s = String.valueOf(num);
        char[] digits = s.toCharArray();
        return digits;
    }
    
    private ArrayList<Character> handleOldFreq(){

        ArrayList<Character> newArr = new ArrayList<>();
        Node node = stack.pop();
        newArr.add(node.c);
        if(node.count==1){
            output++;
            return newArr;
        }
        char[] nums = intToArray(node.count);

        output+= nums.length + 1;

        for (char num : nums){
            newArr.add(num);
        }

        return newArr;
    }



    public int compress(char[] chars) {

        stack.push(new Node(chars[0]));

        for(int i=1;i<chars.length;i++){
            if(stack.peek().c == chars[i]){
                Node node = stack.pop();
                node.count++;
                stack.push(node);
            }else{
                ArrayList<Character> characters =  handleOldFreq();
                for(char c : characters){
                    chars[indexCounter] = c;
                    indexCounter++;
                }
                stack.push(new Node(chars[i]));
            }
        }

        if(!stack.isEmpty()){
            ArrayList<Character> characters =  handleOldFreq();
            for(char c : characters){
                chars[indexCounter] = c;
                indexCounter++;
            }
        }

        return output;
    }
}