// bool isPalindrome(char* s) {
//     int left = 0;
//     int right = strlen(s) - 1;


//     while(left < right){
//         if(!(tolower(s[left]) >= 'a' && tolower(s[left]) <= 'z' || s[left] >= '0' && s[left] <= '9')){
//             left++;
//         }
//         else if(!(tolower(s[right]) >= 'a' && tolower(s[right]) <= 'z' || s[right] >= '0' && s[right] <= '9')){
//             right--;
//         }
//         else if(tolower(s[left]) != tolower(s[right])){
//             return false;
//         }
//         else{
//             left++;
//             right--;
//         }

//     }
//     return true;


// }

bool isPalindrome(char* s){
    int left = 0;
    int right = strlen(s) -1;

    while (left < right){
        if(!isalnum(s[left])){
            left++;
        }
        else if(!isalnum(s[right])){
            right--;
        }
        else if(tolower(s[left]) != tolower(s[right])){
            return false;
        }
        else{
            left++;
            right--;
        }
    }
    return true;
}