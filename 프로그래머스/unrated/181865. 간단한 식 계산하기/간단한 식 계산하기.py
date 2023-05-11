def solution(binomial):
    binomial = binomial.split(' ')
    if '+' in binomial:
        return int(binomial[0])+int(binomial[-1])
    elif '-' in binomial:
        return int(binomial[0])-int(binomial[-1])
    elif '*' in binomial:
        return int(binomial[0])*int(binomial[-1])