public class Solution {
    public long[] solution(long n) {
        int len = n.ToString().Length;
        
        long[] answer = new long[len];
        
        for(int i = 0; i < len; i++)
        {
            answer[i] = n%10;
            n/=10;
        }
        
        return answer;
    }
}