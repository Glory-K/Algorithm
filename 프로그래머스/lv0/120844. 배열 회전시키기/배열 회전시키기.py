def solution(numbers, direction):
    if direction=='left':
        a = [numbers.pop(0)]
        return numbers[0:] + a
    else:
        a = [numbers.pop(-1)]
        return a + numbers[0:]
        