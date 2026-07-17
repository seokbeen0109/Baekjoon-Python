import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int [][] visited = new int[n][m];
        for (int[] row : visited){
            Arrays.fill(row,-1);
        }
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0,0});
        visited[0][0]=1;
        
        while (!queue.isEmpty()){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            
            for (int dir=0; dir<4; dir++){
                int nx = x+dx[dir];
                int ny = y+dy[dir];
                
                if (nx<0 || nx>=n || ny<0 || ny>=m){
                    continue;
                }
                if (maps[nx][ny]==0){
                    continue;
                }
                if (visited[nx][ny]!= -1){
                    continue;
                }
                visited[nx][ny]=visited[x][y]+1;
                queue.offer(new int[]{nx,ny});
            }
        }
        return visited[n-1][m-1];
    }
}