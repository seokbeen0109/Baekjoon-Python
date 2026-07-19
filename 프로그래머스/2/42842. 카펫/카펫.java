import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        List<int[]> pairset = new ArrayList<>();
        for (int i=1; i*i<=yellow; i++){
            if(yellow%i==0){
                pairset.add(new int[]{i,yellow/i});
            }
        }
        for(int[] pair:pairset){
            if((pair[0]+pair[1])*2+4==brown){
                answer[0]=pair[1]+2;
                answer[1]=pair[0]+2;
            }
        }
        return answer;
    }
}