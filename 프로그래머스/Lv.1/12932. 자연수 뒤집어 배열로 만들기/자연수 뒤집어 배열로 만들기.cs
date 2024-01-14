public class Solution {
    public int[] solution(long n) {
        string str = n.ToString();
        int len = str.Length;
        
        int[] answer = new int[len];
        
        for(int i = 0; i < len; i++)
            answer[len-i-1] = int.Parse(str[i].ToString());      
        
        return answer;
    }
}