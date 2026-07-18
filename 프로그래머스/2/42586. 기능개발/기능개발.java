import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n=progresses.length;
        int[] days = new int [n];
        
        for (int i=0; i<n; i++){
            int remain = 100-progresses[i];
            days[i] = (remain+speeds[i]-1)/speeds[i];
        }
        
        List<Integer> answerList = new ArrayList<>();
        int maxDay = days[0];
        int count = 1;
        
        for (int i=1; i<n; i++){
            if(days[i]<=maxDay){
                count++;
            } else {
                answerList.add(count);
                maxDay = days[i];
                count = 1;
            }
        }
        answerList.add(count);
        
        int[] answer = new int[answerList.size()];
        for (int i=0; i<answerList.size(); i++){
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}