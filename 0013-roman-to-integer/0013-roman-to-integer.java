
class Solution {
    public static int output(char s) {
        int value = 0;
        if (s == 'I')
            value = 1;
        if (s == 'V')
            value = 5;
        if (s == 'X')
            value = 10;
        if (s =='L')
            value = 50;
        if (s == 'C')
            value = 100;
        if ( s == 'D')
            value = 500;
        if ( s == 'M')
            value = 1000;
        return value;
    
}
    public static int romanToInt(String s){
        int sum = 0, prev = 0;
        for (int i = s.length() -1; i >= 0; i--){
            char c = s.charAt(i);
            int num = output(c);
            if ( num < prev)
                sum -= num;
            else
                sum += num;
            prev = num;
        }
        return sum;
}

    public static void main(String[] args) {
       // To take input from the user
        System.out.println("Output: " +Solution.romanToInt("III"));
    }
}
