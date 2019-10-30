A, B, C, D, E = int(input()), int(input()),\
                int(input()), int(input()), int(input())

if A <= D:
    if B <= E or C <= E:
        print("YES")
    else:
        print("NO")
elif A <= E:
    if B <= D or C <= D:
        print("YES")
    else:
        print("NO")
elif B <= D:
    if A <= E or C <= E:
        print("YES")
    else:
        print("NO")
elif B <= E:
    if A <= D or C <= D:
        print("YES")
    else:
        print("NO")
elif C <= D:
    if A <= E or B <= E:
        print("YES")
    else:
        print("NO")
elif C <= E:
    if A <= D or B <= D:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
