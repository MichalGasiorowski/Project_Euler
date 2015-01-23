package com.goose.util;


import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by Michal on 1/18/2015.
 */
public class EratosthenesSieve {

    private final int maxNum;

    private final boolean[] sieve; // if false -> then is Prime (default value)
    private final List<Integer> primesList = new ArrayList<>();

    public EratosthenesSieve(int maxNum) {
        if(maxNum < 2) { throw new IllegalArgumentException("Sieve below 2 are not allowed."); }
        this.maxNum = maxNum;
        sieve = new boolean[maxNum + 1];
        generateSieve();
        populatePrimesList();
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

    private void populatePrimesList() {

        for(int i = 2; i <= maxNum; i++) {
            if(isPrime(i)) primesList.add(i);
        }
    }

    public boolean isPrimeBasic(int num) {
        if(num > maxNum || num < 0) return false;
        return !sieve[num];
    }

    public boolean isComposite(int num) {
        if(num > maxNum || num < 0) return false;
        return sieve[num];
    }

    public Iterator<Integer> primeIterator() {
        return primesList.iterator();
    }

    public boolean isPrime(long num) {

        if(num <= maxNum) return isPrimeBasic( (int) num);
        int sqrt = (int)Math.sqrt(num);

        Iterator itr = primeIterator();
        while(itr.hasNext()) {
            int prime = (int)itr.next();
            if(prime > sqrt) break;
            if(num % prime == 0) return false;
        }
        return true;

    }






}



