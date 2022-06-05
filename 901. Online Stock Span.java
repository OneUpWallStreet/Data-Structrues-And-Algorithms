import java.util.ArrayList;

class StockSpanner {

    ArrayList<Integer> data = new ArrayList<>();
    int index = -1;

    public StockSpanner() {}

    public int next(int price) {

        int counter = 1;

        if(index==-1){
            data.add(price);
            index++;
            return counter;
        }

        for(int i=index;i>=0;i--){
            if(data.get(i)<=price){
                counter++;
                continue;
            }
            break;
        }

        index++;
        data.add(price);

        return counter;
    }
}