import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int n = priorities.length;
        Queue<int[]> queue = new LinkedList<>();
        
        for (int i = 0; i < n; i++) {
            queue.offer(new int[]{i, priorities[i]});
        }
        
        int order = 0;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            
            boolean hasHigher = false;
            for (int[] p : queue) {
                if (p[1] > cur[1]) {
                    hasHigher = true;
                    break;
                }
            }
            
            if (hasHigher) {
                queue.offer(cur);
            } else {
                order++;
                if (cur[0] == location) {
                    return order;
                }
            }
        }
        
        return order;
    }
}