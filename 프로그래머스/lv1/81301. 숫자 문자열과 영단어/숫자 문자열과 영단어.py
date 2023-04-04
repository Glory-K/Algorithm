def solution(s):
    num_dict={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
              'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
    
    test=[]
    ans=str()
    for i in list(s):
        test.append(i)
        check=''.join(test)
        if check.isdigit():
            ans+=check
            check=''
            test.clear()
        elif check in num_dict:
            ans+=str(num_dict[check])
            check=''
            test.clear()
            
    return int(ans)