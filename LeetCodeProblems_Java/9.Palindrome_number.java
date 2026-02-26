class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        
        String stringx = Integer.toString(x);
        int left = 0;
        int right = stringx.length() - 1;

        while (left < right){
            if (stringx.charAt(left) != stringx.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}