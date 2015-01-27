package com.goose.problems;

import com.goose.util.BigIntegerUtils;
import com.goose.util.EratosthenesSieve;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Stream;

/**
 * Created by Michal on 1/18/2015.
 */

/*
Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
 */
public class Problem35 {



    public static void main(String[] args) {
        final int maxNum = 1000 * 1000;

        int circularPrimesCount = 0;

        EratosthenesSieve erSieve = new EratosthenesSieve(maxNum);
        List<Integer> circularPrimes = new ArrayList<>();
        boolean broke;

        for(int candidate = 2; candidate < maxNum; candidate++) {
            int[] rotations = BigIntegerUtils.rotations(candidate);
            broke = false;

            for(int rotation : rotations) {
                if(erSieve.isComposite(rotation)) { broke = true; break; }
            }
            if(broke) { continue; }
            circularPrimes.add(candidate);
            circularPrimesCount++;
        }

        System.out.println("circularPrimesCount: " + circularPrimesCount);

        for(int prime: circularPrimes) {
            System.out.println("circular Prime: " + prime);
        }

    }
}
