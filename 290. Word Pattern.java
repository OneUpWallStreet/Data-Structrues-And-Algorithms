import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

class Solution {
    public boolean wordPattern(String pattern, String s) {

        String[] strArr =  s.split(" ");
        HashMap<Character,String> map = new HashMap<>();
        HashSet<String> set = new HashSet<>();

        if(pattern.length() != strArr.length){
            return  false;
        }

        for(int i=0;i<pattern.length();i++){
            if(map.containsKey(pattern.charAt(i)) && !Objects.equals(map.get(pattern.charAt(i)), strArr[i])){
                return  false;
            }else{

                if(!map.containsKey(pattern.charAt(i)) && set.contains(strArr[i])){
                    return  false;
                }
                map.put(pattern.charAt(i),strArr[i]);
                set.add(strArr[i]);
            }

        }

        return  true;
    }
}