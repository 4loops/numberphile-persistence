
def factors_of_237(n):
    factors = [0,0,0]
    while n%2 ==0:
        factors[0] += 1
        n = n//2
    while n%3 ==0:
        factors[1] += 1
        n = n//3
    while n%7 ==0:
        factors[2] += 1
        n = n//7
    if n==1:
        return factors
    else:
        return None #inicates cannot be only factored by 2, 3, 7

#start with the least amount of digits to the most amount of digits

def numbers_from_factors(f,n1=0):
    print("f is",f,"n1 is",n1)
    for n9 in reversed(range(f[1]//2+1)):
        for n8 in reversed(range(f[0]//3+1)):
            for n6 in reversed(range(min(f[0]-3*n8,f[1]-2*n9)+1)):
                for n4 in reversed(range((f[0]-3*n8-n6)//2+1)):
                    n3 = f[1]-2*n9-n6
                    n2 = f[0]-3*n8-n6-2*n4
                    n7 = f[2]
                    yield ["9"]*n9+["8"]*n8+["7"]*n7+["6"]*n6+["4"]*n4+["3"]*n3+["2"]*n2+["1"]*n1

from sympy.utilities.iterables import multiset_permutations
def rec_search(current_num,depth, max_n1=2):
    n1 = -1
    old_num = current_num
    while True:
        if old_num == current_num:
            n1 += 1
        if n1 > max_n1:
            return
        old_num = current_num
        for nums in numbers_from_factors(factors_of_237(current_num),n1=n1):
            for perm in multiset_permutations(nums):
                cand = int("".join(perm))
                if factors_of_237(cand):
                    print("FOUND", cand, depth)
                    rec_search(cand,depth+1)

rec_search(336,4)


