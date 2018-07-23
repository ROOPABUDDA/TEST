def solve (S, N):
    # write your code here
    # print(S,N)
    my_dict = {}
    for each in S:
        if each in my_dict:
            my_dict[each] += 1
        else:
            my_dict[each] = 1
    myList = [v[0] for v in sorted(my_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    
    print(len(myList))
    for each in myList:
        print(each)
    

N = int(input())
S = []
for _ in range(N):
    S.append(input())

out_ = solve(S, N)
print (len(out_))
for i_out_ in out_:
    print (i_out_)
