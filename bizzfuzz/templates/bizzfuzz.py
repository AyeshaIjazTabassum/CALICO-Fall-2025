def solve(W1: str, W2: str) -> str:
    """
    Return the string containing the word you should say
 
    W1: the second-to-last word said 
    W2: the last word said
    """
    possible = set()
    for x in range(1,101):
        if isinstance(W1, int) or (isinstance(W1, str) and W1.isdigit()):
            W1 = int(W1)
            if W1 != x:
                continue
        else:
            if x % 3 == 0 and x % 5 == 0:
                label1="bizzfuzz"
            elif x % 3 == 0:
                label1="bizz"
            elif x % 5 == 0:
                label1="fuzz"
            else:
                label1=str(x)
            if label1 != W1:
                continue
            y = x+1
            if y > 100:
                continue
            if isinstance(W2, int) or (isinstance(W2, str) and W2.isdigit()):
                W2 = int(W2)
                if W2 != y:
                    continue
            else:
                if y % 3 == 0 and y % 5 == 0:
                    label2="bizzfuzz"
                elif y % 3 == 0:
                    label2="bizz"
                elif y % 5 == 0:
                    label2="fuzz"
                else:
                    label2=str(y)
                if label2 != W2:
                    continue
                if label2 != W2:
                    continue
            z = x+2
            if z % 3 == 0 and z % 5 == 0:
                nextlabel = "bizzfuzz"
            elif z % 3 == 0:
                nextlabel = "bizz"
            elif z % 5 == 0:
                nextlabel = "fuzz"
            else:
                nextlabel = str(z)
            possible.add(nextlabel)
    if len(possible) == 1:
        return possible.pop()
    else:
        return "crap"

    # return ""


def main():
    T = int(input())
    for _ in range(T):
        W1 = input()
        W2 = input()
        print(solve(W1, W2))

if __name__ == '__main__':
    main()
