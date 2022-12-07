
print(".....................Welcome :).........................")
def prime_pal(n,Candidate=2):
    primes = [2]
    while True:
        flag=0
        Candidate = Candidate + 1
        Candidate_str = str(Candidate)
        for i in primes:
            if Candidate%i == 0:
                flag += 1
        Candidate_str_rev = Candidate_str[len(Candidate_str)::-1]
        if flag == 0 and Candidate_str_rev == Candidate_str:
            primes . append(Candidate)
        elif len(primes) == n:
            break
    return primes[-1]
n=int(input("Enter your value: "))
result=prime_pal(n,Candidate=2)
print("{}th prime pallindrome number will be: {}".format(n,result))
print("              Thank You :)              ")










