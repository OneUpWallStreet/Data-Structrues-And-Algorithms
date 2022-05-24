import java.util.Stack;

class Solution {
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        for(int i=0;i<s.length();i++){
            Character current = s.charAt(i);

            if( current.equals('(') || current.equals('{') || current.equals('[')){
                stack.push(current);
            }
            else{
                Character lastOpen;
                if(stack.empty()){
                    return false;
                }
                else{
                    lastOpen = stack.peek();
                }

                if(current.equals(')') && !lastOpen.equals('(')){
                    return false;
                }
                else if (current.equals(']') && !lastOpen.equals('[')){
                    return false;
                }

                else if (current.equals('}') && !lastOpen.equals('{')){
                    return false;
                }

                stack.pop();
            }
        }

        return stack.isEmpty();

    }
}