public class Solution {
    public bool solution(int x) {
        
            int _sum = 0;
            int n = x;
            while(true)
            {
                if (n % 10 == 0)
                {
                    _sum += n/10;
                    break;
                }
                else
                {
                    _sum += n % 10;
                    n /= 10;
                }
                
            }
            return (x%_sum==0) ? true : false;
    }
}