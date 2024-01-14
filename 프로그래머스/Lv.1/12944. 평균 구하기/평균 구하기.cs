public class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        foreach(var item in arr){
            answer += item;
        }
        return answer/arr.Length;
    }
}