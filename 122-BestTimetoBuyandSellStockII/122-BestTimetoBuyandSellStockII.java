class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int maxProfit = 0;

        for(int price: prices){
            if (price < min) {
                min = price;
                continue;
            } else if (price > min) {
                maxProfit += (price - min);
                min = price;
            }
        }
        return maxProfit;
    }
}