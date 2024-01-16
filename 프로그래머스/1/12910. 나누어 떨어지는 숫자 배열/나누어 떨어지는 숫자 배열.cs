using System;
public class Solution {
    public int[] solution(int[] arr, int divisor) 
    {
        int[] answer = new int[arr.Length];
        int _cnt = 0;
        foreach(var item in arr)
        {
            if(item%divisor == 0)
            {
                answer[_cnt++] = item;
            }
            else
            {
                continue;
            }
        }
        if(_cnt==0)
        {
            Array.Resize(ref answer, 1);
            answer[0] = -1;
        }
        else
        {
            Array.Resize(ref answer, _cnt);
            Array.Sort(answer);
        }

        return answer;
    }
}