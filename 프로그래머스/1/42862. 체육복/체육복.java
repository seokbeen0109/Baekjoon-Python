import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        boolean[] hasClothes = new boolean[n + 2];
        
        for (int i = 1; i <= n; i++) {
            hasClothes[i] = true;
        }
        
        boolean[] isLost = new boolean[n + 2];
        boolean[] isReserve = new boolean[n + 2];
        
        for (int l : lost) {
            isLost[l] = true;
        }
        for (int r : reserve) {
            isReserve[r] = true;
        }
        
        // 도난당했으면서 여벌도 있는 학생은 서로 상쇄 (아무 일도 없었던 것처럼)
        for (int i = 1; i <= n; i++) {
            if (isLost[i] && isReserve[i]) {
                isLost[i] = false;
                isReserve[i] = false;
            }
        }
        
        // 남은 lost 학생을 순회하며 앞/뒤 reserve 학생에게 빌리기
        for (int i = 1; i <= n; i++) {
            if (isLost[i]) {
                if (i - 1 >= 1 && isReserve[i - 1]) {
                    isReserve[i - 1] = false;
                    isLost[i] = false;
                } else if (i + 1 <= n && isReserve[i + 1]) {
                    isReserve[i + 1] = false;
                    isLost[i] = false;
                }
            }
        }
        
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (!isLost[i]) {
                answer++;
            }
        }
        
        return answer;
    }
}