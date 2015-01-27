package com.goose.problems;

import com.goose.util.EratosthenesSieve;
import com.goose.util.IntUtils;
import com.goose.util.StringUtils;

import java.util.*;

/**
 * Created by Michal on 1/22/2015.
 */

/*
Truncatable primes
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
*/

public class Problem37 {

    public static boolean isTruncatable(String possTrunc, EratosthenesSieve sieve) {
        int first = 0;
        int last = possTrunc.length();
        Long possibleTruncatableNum = Long.valueOf(possTrunc);

        if(!sieve.isPrime(possibleTruncatableNum) ) return false;
        /*
        if(last < 6) {
            System.out.println("##possTrunc = " + possTrunc);
            for(int index = first + 1; index < last; index++) {
                System.out.println("LEFT:" + possTrunc.substring(index, last) + " is PRIME: " + sieve.isPrime(Long.valueOf(possTrunc.substring(index, last)) ));
            }

            for(int index = first + 1; index < last; index++) {
                System.out.println("RIGHT:" + possTrunc.substring(0, last - index) + " is PRIME: " + sieve.isPrime(Long.valueOf(possTrunc.substring(0, last - index)) ));
            }
        }
        */

        for(int index = first + 1; index < last; index++) {
            if(!sieve.isPrime(Long.valueOf(possTrunc.substring(index, last)) ) ) return false;
            if(!sieve.isPrime(Long.valueOf(possTrunc.substring(0, last - index)) ) ) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        EratosthenesSieve sieve = new EratosthenesSieve(3000*1000);

        Long max_val = Long.valueOf(3000*1000*3000);

        List<Character> extensionDigits = new ArrayList<>(Arrays.asList('1', '2', '3', '5', '7', '9'));

        Set<Long> truncatablePrimes = new HashSet<>();

        Stack<Long> primeSeedStack = new Stack<>();
        primeSeedStack.push(33L);
        primeSeedStack.push(37L);
        primeSeedStack.push(73L);
        primeSeedStack.push(77L);

        primeSeedStack.push(23L);
        primeSeedStack.push(53L);

        String possibleTruncatable;
        Long possibleTruncatableNum;

        String nextItemStr;
        Long nextSeedPrime;

        List<String> possibleTruncatableList = new ArrayList<>();

        while(!primeSeedStack.empty()) {
            nextSeedPrime = primeSeedStack.pop();
            if(truncatablePrimes.contains(nextSeedPrime)) continue;

            nextItemStr = nextSeedPrime.toString();
            if(isTruncatable(nextItemStr, sieve)) truncatablePrimes.add(nextSeedPrime);

            possibleTruncatableList = new ArrayList<>();
            boolean isTrunc;
            for(Character s: extensionDigits) {
                possibleTruncatable = nextItemStr.substring(0, 1) + s + nextItemStr.substring(1, nextItemStr.length());
                possibleTruncatableList.add(possibleTruncatable);
                possibleTruncatable = nextItemStr.substring(0, nextItemStr.length() - 1) + s + nextItemStr.substring(nextItemStr.length() - 1, nextItemStr.length());
                possibleTruncatableList.add(possibleTruncatable);
            }

            for(String possTrunc: possibleTruncatableList) {
                possibleTruncatableNum = Long.valueOf(possTrunc);
                if(possibleTruncatableNum > max_val) continue;
                if(!sieve.isPrime(possibleTruncatableNum) ) continue;
                primeSeedStack.push(possibleTruncatableNum);
            }

        }

        System.out.println(truncatablePrimes);
        Long sum = 0L;
        for(Long num : truncatablePrimes) {
            sum += num;
            //System.out.println(String.format("num %d is Prime: %b ", num, sieve.isPrime(num)));
        }
        System.out.println(String.format("Sum of truncatable primes is %d", sum));

    }
}
