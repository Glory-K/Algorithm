using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr) {
        List<int> arrList = new List<int>(arr);
        int _min = arrList.Min();
        arrList.RemoveAll(_num => _num==_min);
        if(arrList.Count==0)
        {
            arrList.Add(-1);
        }
        else
        {
            
        }
        
        return arrList.ToArray();
    }
}