import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        
        StringBuilder sb = new StringBuilder();
        ArrayList<Integer> baseArr = new ArrayList<>();
        
        //a~z ascii     
        for(int i=97; i<=122; i++){
            baseArr.add(i);
        }
        //baseArr: skip 제외한 a~z ascii
        for(int i=0; i<skip.length(); i++){
            int idx = baseArr.indexOf((int) skip.charAt(i));
            baseArr.remove(idx);
        }
        
        for(int i=0; i<s.length(); i++){
            int idx = baseArr.indexOf((int) s.charAt(i)) + index;
            
            if(idx+1 > baseArr.size()){
                idx = idx % baseArr.size();
            }            
            sb.append((char) baseArr.get(idx).intValue());            
        }
        
        return sb.toString();
    }
}