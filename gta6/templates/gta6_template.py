def solve(E: str, Y: int, M: int, D: int) -> str:
    """

    E: The name of the event
    Y: Year
    M: Month
    D: Day
    """
    # YOUR CODE HERE
    gtaY=2026
    gtaM=11
    gtaD=19
    # print(Y,M,D)
    if (Y<gtaY) or (Y==gtaY and M<gtaM) or (Y==gtaY and M==gtaM and D<=gtaD):
        return f"we got {E} before gta6"
    else:
        return f"we got gta6 before {E}"
    # return ""

def main():
    T = int(input())
    for _ in range(T):
        E = input()
        temp = input().split()
        Y, M, D = int(temp[0]), int(temp[1]), int(temp[2])
        print(solve(E, Y, M, D))

if __name__ == '__main__':
    main()