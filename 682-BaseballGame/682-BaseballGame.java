class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String operation: operations) {
            switch(operation) {
                case "+": 
                    int x = stack.pop();
                    int y = stack.peek();
                    stack.push(x);
                    stack.push(x + y);
                    break;
                case "D":
                    int newScore = 2 * stack.peek();
                    stack.push(newScore);
                    break;
                case "C":
                    stack.pop();
                    break;
                default:
                    stack.push(Integer.parseInt(operation));
            }   
        }

        int ans = 0;

        while (!stack.isEmpty()) {
            ans += stack.pop();
        }

        return ans;
    }
}