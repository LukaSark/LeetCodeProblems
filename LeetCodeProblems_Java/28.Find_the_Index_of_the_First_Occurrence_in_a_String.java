class Solution {
    public int strStr(String haystack, String needle) {
        
        char[] h = haystack.toCharArray();
        char[] n =  needle.toCharArray();

        int count = 0;

        for(int i = 0;i <= h.length - n.length;i++){
            if(h[i] == n[0]){
                count = 0;
                for(int j=0;j<n.length;j++){
                    if(h[i+j] == n[j]){
                        count += 1;
                    }
                    else{
                        break;
                    }
                }
                if(count == n.length){
                    return i;
                }
            }

        }
        return -1;
    }
}