def small():
    li =list()
    while True:
        input_num1= input('처음 숫자입력:')
        input_num2= input('두번째 숫자입력:')
        N = int(input_num1.split(' ')[0])
        X = int(input_num1.split(' ')[1])
        if N > 1 or X <=10000or len(input_num2) is 2*N-1:
            break
        else:
            continue
    for i in input_num2.split(' '):
        if int(i) < X:
            li.append(i)
    print(*li)
small()