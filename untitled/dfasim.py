import sys
__author__ = 'Samuel'
states = []
#comments
print("give us a state!!!!!!!!! \n" +
       "but do it though in this format please though"
       "('charThatIsRead','numOfStateToGoTo'),('charThatIsRead','numOfStateToGoTo');")

b = 0
while b < 8:
    user_input = raw_input("enter some word swag: ")
    print("you defs said "+ user_input)
    if user_input == "done":
        break
    dirGraph = []

    length = len(user_input)
    numStates = length/6
    i = 0
    while i < numStates:
        #since we are assuming input is always good
        #index 0 is a paren we don't care about
        #index 1 is the char that causes transition
        #index 2 is a comma we don't care about
        #index 3 is the node it goes to
        #index 4 is a paren we could care less about
        #index 6 also another thing that yeah we don't care about

        state = (user_input[(i*6)+1], int(user_input[(i*6)+3]))
        dirGraph.append(state)
        i += 1
    states.append(dirGraph)
    print("this is what your state kinda looks like")
    print(dirGraph)
    b += 1

print("this is what my graphs looks like ")
print(states)
accepts = raw_input("ok now it would be just grand if you could say witch"
                    "states are the accept states: ")
while True:
    string = raw_input("so now you should give a string for us to run: ")
    print("lets see this bad boy run")
    length = len(string)
    i = 0
    sequence = []
    currNode = 0
    sequence.append(currNode)

    while i < length:
        state = states[currNode]
        for trans in state:
            if string[i] == trans[0]:
                currNode = trans[1]
                sequence.append(currNode)
                break
        print("to ", currNode, "by ", string[i])
        i += 1

    print(sequence)
    win = False
    for acceptstates in accepts:
        if int(acceptstates) == currNode:
            print("ACCEPT")
            win = True
            break

    if win == False:
        print("REJECT")
