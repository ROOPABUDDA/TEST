from itertools import permutations
def answer (arr,N):
    # Write your code here
    #perm = permutations(arr)
    state = "NO"
    listeach = list(arr)
    for each in listeach:
        print(listeach.count(each))
    #for each in perm:
        #print(each)
        #listeach = list(each)
        #print(listeach)
        #print(len(listeach)/2)
     #   half = int(len(each)/2)
        #left = listeach[0:half]
        #right = listeach[half:]
      #  for i in range(half):
       #     if(each[i] == each[i+half]):
        #        state = "YES"
        #if(sum(listeach[0:half) == sum(listeach[half:])):
         #   print(listeach)
    return state

T = int(input())
for _ in range(T):
    arr_size = int(input())
    arr = map(int, input().split())

    out_ = answer(arr,arr_size)
    print (out_)
