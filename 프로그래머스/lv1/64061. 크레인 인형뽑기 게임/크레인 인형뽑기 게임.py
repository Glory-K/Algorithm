def solution(board, moves):
    # list to dict
    new_board={}

    for i in board:
        for idx,j in enumerate(i):
            if j != 0:
                if idx+1 in new_board:
                    new_board[idx+1].append(j)
                else:
                    new_board[idx+1]=[j]
                    
    # 원소 뽑아내기?
    res_list=[]

    for move in moves:
        if new_board[move]:
            pick=new_board[move].pop(0)
            res_list.append(pick)
        else:
            continue
    # 터지는 수 세기
    cnt=0
    res=0
    while True:
        print('cnt', cnt)
        if res_list[cnt+1:cnt+2]:
            if res_list[cnt] in res_list[cnt+1:cnt+2]:
                res_list.pop(cnt)
                res_list.pop(cnt)
                print('pop', res_list)
                res+=2
                cnt=0
            else:
                cnt+=1
        else:
            break
            
    return res