int lengthOfLongestSubstring(char* s) {
    char count[128] = {0};
    int result = 0;
    int max = 0;

    for(int i = 0;i < strlen(s);i++){
        memset(count, 0, sizeof(count));
        result = 0;
        for(int j = i ;j < strlen(s);j++){
            if(count[s[j]] == 1){
                if(result > max){
                    max = result;
                }
                break;
            }
            else{
                (count[s[j]])++;
                result++;
            }
        }
        if(result > max){
            max = result;
        }
    }
    return max;
}