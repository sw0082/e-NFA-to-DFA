if __name__ == "__main__":

    Regexp = '(a+b)*'
    # prestate, symbol, changestate
    delta = [[0, 'a', 1],
             [2, 'b', 3],
             [4, 'eps', 0],
             [4, 'eps', 2],
             [1, 'eps', 5],
             [3, 'eps', 5],
             [6, 'eps', 4],
             [6, 'eps', 7],
             [5, 'eps', 4],
             [5, 'eps', 7]]
    startstate = 0
    finalstate = {7}

    Q = list(range(0, len(delta)))
    sigmalist = set([i[1] for i in delta])
    sigmalist.discard('eps')
    changestatelist = set([i[2] for i in delta])
    prestatelist = set([i[0] for i in delta])
    statelist = changestatelist | prestatelist

    print("e-NFA to DFA")
    print("Regexp: " + Regexp)
    print("Q:", statelist)
    print("Sigma:", sigmalist)
    print("q0:", startstate)
    print("F:", finalstate)
    for x, y, z in delta:
        print('Delta(' + str(x) + ', ' + y + ') = ' + str(z))
