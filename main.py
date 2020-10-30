import copy

# Subset Construction
def nextstate(currentstate, symbol):
    tempset = set()
    stk = copy.deepcopy(currentstate)

    if symbol != 'eps':
        tempstk = set()
        for j in range(len(currentstate)):
            current = stk.pop()
            for i in delta:
                if i[0] == current and (i[1] == symbol):
                    tempset.add(i[2])
                    tempstk.add(i[2])
        stk = tempstk

    while(stk):
        current = stk.pop()
        tempset.add(current)
        for i in delta:
            if i[0] == current and (i[1] == "eps"):
                stk.add(i[2])
    return tempset

# Accept or Reject Sentence
def syntaxcheck(str):
    currentstate = dfastartstate
    for i in range(len(str)):
        for j in dfadelta:
            if j[0] == currentstate and j[1] == str[i]:
                currentstate = j[2]
                break
    if currentstate in dfafinalstate:
        print("Sentence '" + str + "' Accepted")
    else:
        print("Sentence '" + str + "' Rejected")



if __name__ == "__main__":

    # Input Data
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
             [5, 'eps', 7],
             [7, 'a', 9],
             [9, 'b', 11],
             [11, 'b', 13]]
    startstate = {6}
    finalstate = {13}

    Q = list(range(0, len(delta)))
    sigmalist = set([i[1] for i in delta])
    sigmalist.discard('eps')
    changestatelist = set([i[2] for i in delta])
    prestatelist = set([i[0] for i in delta])
    statelist = changestatelist | prestatelist

    # Print Input Data
    print("e-NFA to DFA")
    print("\nNFA STATES\n")
    print("Regexp: " + Regexp)
    print("Q:", statelist)
    print("q0:", startstate)
    print("F:", finalstate, "\n")
    for x, y, z in delta:
        print('Delta(' + str(x) + ', ' + y + ') = ' + str(z))

    checked = 0
    state = []
    statechanged = True
    state.append(nextstate(startstate, 'eps'))
    dfastartstate = state[0]
    dfadelta = []

    while statechanged or checked != len(state):
        statechanged = False

        for i in sigmalist:
            result = nextstate(state[checked], i)
            dfadelta.append([state[checked], i, result])
            if result not in state:
                statechanged = True
                state.append(result)
        checked += 1

    dfafinalstate = []
    for i in state:
        if finalstate.issubset(i):
            dfafinalstate.append(i)

    # print output data
    print("\n\nDFA STATES\n")
    print("Regexp: " + Regexp)
    print("Q: ", state)
    print("Sigma:", sigmalist)
    print("q0: ", dfastartstate)
    print("F: ", dfafinalstate, "\n")
    for x, y, z in dfadelta:
        print('Delta(' + str(x) + ', ' + y + ') = ' + str(z))

    syntaxcheck('abb')
    syntaxcheck('ababababaaaabb')
    syntaxcheck('babbbabaab')
    syntaxcheck('abababababb')
    syntaxcheck('ababababababbb')
