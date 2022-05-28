#include<iostream>

using namespace std;
void printArr(int arr[],int N);

void reverse(int arr[],int N){
    int i = 0;
    int j = N-1;
    printArr(arr,4);
    while(i<j){
        swap(arr[i],arr[j]);
        j--;
        i++;
    }
    printArr(arr,4);
}   

void printArr(int arr[],int N){
    for(int i=0;i<N;i++){
        cout << " " << arr[i] << " ";
    }
    cout << endl;
}

int main(){
    int arr[4] = {1,2,3,4};    
    reverse(arr,4);
    return 0;
}

