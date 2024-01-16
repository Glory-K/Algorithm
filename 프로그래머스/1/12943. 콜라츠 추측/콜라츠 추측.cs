public class Solution {
    public int solution(int num) {
        int _cnt = 0;
        long _temp = num;
        
        while(_cnt < 500)
        {
            if(_temp==1)
            {
                return _cnt;
            }
            else
            {
                _temp = (_temp%2==0) ? _temp/2 : (_temp*3)+1;
                _cnt++;
            }
        }
        return -1;
    }
}