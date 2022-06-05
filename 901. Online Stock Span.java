import java.util.Stack;


class StockSpanner {

    Stack<Integer> stack = new Stack<>();
    Stack<Integer> duplicateStack = new Stack<>();

    public StockSpanner() {}

    public int next(int price) {

        int counter = 1;

        if(stack.isEmpty()){
            stack.push(price);
            return counter;
        }

        duplicateStack = (Stack<Integer>) stack.clone();

        while(!duplicateStack.isEmpty()){
            if(duplicateStack.pop()<=price){
                counter++;
            }
            else{
                break;
            }
        }

        stack.push(price);

        return counter;
    }
}

