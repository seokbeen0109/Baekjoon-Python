import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> array = new ArrayList<>();
        for (int i=0; i<arr.length; i++){
            if (i==0 || arr[i]!=arr[i-1]){
                array.add(arr[i]);
            }
        }
        int[] answer = new int[array.size()];
        for (int i=0; i<array.size(); i++){   
            answer[i]=array.get(i);
        }
        return answer;
    }
}