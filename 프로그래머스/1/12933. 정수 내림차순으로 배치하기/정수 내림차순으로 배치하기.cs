using System;
public class Solution {
    public long solution(long n) {
            char[] temp = n.ToString().ToCharArray();
            Array.Sort(temp);
            Array.Reverse(temp);
            long answer = Convert.ToInt64(new string(temp));
            return answer;
    }
}