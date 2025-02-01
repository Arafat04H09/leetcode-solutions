public int countNumbersWithUniqueDigits(int n) {
    if (n==0){
        return 1;
    }
    if (n>10){
        return countNumbersWithUniqueDigits(10);
    }
    int sum = 1;
    int k =0;
    while(k<n){
        if(k==0){
            sum*=9;
        }else{
            sum*=(10-k);
        }
        k++;
    }
    return sum+countNumbersWithUniqueDigits(n-1);
}