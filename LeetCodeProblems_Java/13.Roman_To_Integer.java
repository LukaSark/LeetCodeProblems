class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> RomantoInt = new HashMap<Character, Integer>(){{
            put('I',1);
            put('V',5);
            put('X',10);
            put('L',50);
            put('C',100);
            put('D',500);
            put('M',1000);
    }};

        char[] RomanArray = s.toCharArray();
        int count = 0;

        for (int i = 0; i < RomanArray.length;i++){
            if(i + 1 < RomanArray.length && RomanArray[i] == 'I' && (RomanArray[i+1] == 'V' || RomanArray[i+1] == 'X')){
                count += RomantoInt.get(RomanArray[i+1]) - RomantoInt.get(RomanArray[i]);
                i++;
            }
            else if(i + 1 < RomanArray.length && RomanArray[i] == 'X' && (RomanArray[i+1] == 'L' || RomanArray[i+1] == 'C')){
                count += RomantoInt.get(RomanArray[i+1]) - RomantoInt.get(RomanArray[i]);
                i++;
            }
            else if(i + 1 < RomanArray.length && RomanArray[i] == 'C' && (RomanArray[i+1] == 'D' || RomanArray[i+1] == 'M')){
                count += RomantoInt.get(RomanArray[i+1]) - RomantoInt.get(RomanArray[i]);
                i++;
            }
            else{
                count += RomantoInt.get(RomanArray[i]);
            }
        }
        return count;
    }
}