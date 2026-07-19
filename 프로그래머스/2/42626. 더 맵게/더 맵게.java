import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> mix = new PriorityQueue<>();
        for (int s:scoville){
            mix.offer(s);
        }
        while(mix.peek()<K){
            if (mix.size()<2){
                return -1;
            }
            int first = mix.poll();
            int second = mix.poll();
            int mixed = first +(second*2);
            mix.offer(mixed);
            answer++;
        }
        return answer;
    }
}