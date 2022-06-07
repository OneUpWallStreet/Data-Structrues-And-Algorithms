class ParkingSystem {

    int smallCount;
    int medCount;
    int bigCount;

    public ParkingSystem(int big, int medium, int small) {
        smallCount = small;
        medCount = medium;
        bigCount = big;
    }

    public boolean addCar(int carType) {

        if(carType == 3){
            if(smallCount==0){
                return false;
            }
            smallCount--;
        }else if(carType == 2){
            if(medCount==0){
                return false;
            }
            medCount--;
        }else{
            if(bigCount==0){
                return false;
            }
            bigCount--;
        }

        return true;
    }
}