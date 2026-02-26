char* reverseVowels(char* s) {
    int left = 0;
    int right = strlen(s) - 1;
    char temp;

    while(left < right){
        if(!(s[left] == 97 || s[left] == 101 || s[left] == 105 || s[left] == 111 || s[left] == 117 || s[left] == 65 || s[left] == 69 || s[left] == 73 || s[left] == 79 || s[left] == 85)){
            left++;
            continue;
        }

        if(!(s[right] == 97 || s[right] == 101 || s[right] == 105 || s[right] == 111 || s[right] == 117 || s[right] == 65 || s[right] == 69 || s[right] == 73 || s[right] == 79 || s[right] == 85)){
            right--;
            continue;
        }

        temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;

    }

    return s;
}

bool isVowel(char c){
    c = tolower(c);
    if(c=='a'|| c =='o' || c=='i'||c=='u'||c=='e'){
        return true;
    }
    return false;
}

char* reverseVowels(char* s) {
    int left = 0;
    int right = strlen(s) -1;
    char temp;
    
    while(left < right){
        if(!(isVowel(s[left]))){
            left++;
            continue;
        }
        if(!(isVowel(s[right]))){
            right--;
            continue;
        }

        temp = s[left];
        s[left] =s[right];
        s[right] = temp;

        left++;
        right--;
    }
    return s;
}
