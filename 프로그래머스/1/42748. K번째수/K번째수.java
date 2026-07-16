import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int a=0; a<commands.length; a++){
            int i = commands[a][0];
            int j = commands[a][1];
            int k = commands[a][2];
            int[] sliced = new int [j-i+1];
            for (int idx=i; idx<=j; idx++){
                sliced[idx-i]=array[idx-1];
            }
            Arrays.sort(sliced);
            answer[a]=sliced[k-1];
        }
        return answer;
    }
}