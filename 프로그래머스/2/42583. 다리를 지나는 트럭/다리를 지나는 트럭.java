import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        for (int i=0; i<bridge_length; i++){
            bridge.offer(0);
        }
        int time=0;
        int nowweight=0;
        int index=0;
        int n=truck_weights.length;
        
        while (index<n){
            time++;
            nowweight -=bridge.poll();
            if (nowweight+truck_weights[index]<=weight){
                nowweight+=truck_weights[index];
                bridge.offer(truck_weights[index]);
                index++;
            } else{
                bridge.offer(0);
            }
        }
        time+=bridge_length;
        return time;
    }
}