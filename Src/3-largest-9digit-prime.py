def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True  
def isPal(n):
    og = n
    rev = 0
    while(n!=0):
        digit = n%10
        rev = rev*10 + digit
        n = n//10
    return(rev==og)
maxNineDigit = 999999999
minNineDigit = 100000000
palPrimeList = []
for i in range(maxNineDigit,minNineDigit,-1):
    if(isPal(i)):
        if(isPrime(i)):
            palPrimeList.append(i)
            if(len(palPrimeList)==3):
                break
print(palPrimeList)    