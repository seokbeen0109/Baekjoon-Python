import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> types = new HashSet<>();
        for (int num : nums) {
            types.add(num);
        }
        
        int canPick = nums.length / 2;
        int uniqueCount = types.size();
        
        return Math.min(canPick, uniqueCount);
    }
}