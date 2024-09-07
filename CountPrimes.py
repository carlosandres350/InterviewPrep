class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primeNums = 0
        if n <=2:
            return 0

        primes = [True] * n
        primes[0], primes[1] = False,False

        for i in range(2, int(n**.5)+ 1):
            if primes[i] == True:
                #set all the multiples off i in the array equal to False
                for x in range(i+i, n, i ):
                    primes[x] = False
        
        for val in primes:
            if val == True:
                primeNums += 1

        return primeNums