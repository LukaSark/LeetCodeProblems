// Brute force
int maxArea(int* height, int heightSize) {
    int result = 0;
    int h;
    int w;
    int a;
    for(int i = 0;i < heightSize;i++){
        for (int j = 1;j < heightSize;j++){
            w = j - i;
            if(height[i] < height[j]){
                h = height[i];
            }
            else{
                h = height[j];
            }
            a = h * w;
            if(a > result){
                result = a;
            }
        }
    }
    return result;
}

//Two pointer Method
int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int result = 0;

    while(left < right){
        int h = height[left] < height[right] ? height[left] : height[right];
        int w = right - left;

        int area = h*w;
        if(area > result){
            result = area;
        }

        if(height[left] < height[right]){
            left++;
        }
        else{
            right--;
        }
    }
    return result;
}