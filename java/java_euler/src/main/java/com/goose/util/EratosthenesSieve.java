package com.goose.util;


/**
 * Created by Michal on 1/18/2015.
 */
public class EratosthenesSieve {

    private final int maxNum;

    private final boolean[] sieve; // if false -> then is Prime (default value)

    public EratosthenesSieve(int maxNum) {
        if(maxNum < 2) { throw new IllegalArgumentException("Sieve below 2 are not allowed."); }
        this.maxNum = maxNum;
        sieve = new boolean[maxNum + 1];
        generateSieve();
    }

    private void generateSieve() {
        sieve[0] = sieve[1] = true;

        int num = 2;

        for(num = 2; num <= maxNum; num++) {
            if(sieve[num]) continue; // non-prime

            for(int non_prime = 2*num; non_prime < maxNum; non_prime = non_prime + num) {
                sieve[non_prime] = true;
            }
        }
    }

    public boolean isPrime(int num) {
        if(num > maxNum || num < 0) return false;
        return !sieve[num];
    }

    public boolean isComposite(int num) {
        if(num > maxNum || num < 0) return false;
        return sieve[num];
    }







}



