import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Integer[] sorted = new Integer[citations.length];
        for (int i = 0; i < citations.length; i++) {
            sorted[i] = citations[i];
        }
        Arrays.sort(sorted, Collections.reverseOrder());
        
        int h = 0;
        for (int i = 0; i < sorted.length; i++) {
            int rank = i + 1;
            if (sorted[i] >= rank) {
                h = rank;
            } else {
                break;
            }
        }
        
        return h;
    }
}