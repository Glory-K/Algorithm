using System;

public class Solution {
    public int solution(int[] numbers) {
        int _sum = 0;
        Array.ForEach(numbers, _i => _sum += _i);
        
        return 45-_sum;
    }
}