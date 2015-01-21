package com.goose.problems;

import com.goose.util.BigIntegerUtils;

import java.math.BigInteger;

/**
 * Created by Michal on 1/17/2015.
 */

/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

 */
public class Problem34 {


    public static void main(String[] args) {

        int num;

        BigInteger sum = BigInteger.ZERO;
        int maxToCheck = 9999999;

        for(num = 3; num < maxToCheck; num++) {
            if(BigIntegerUtils.isNumberFactorialyCurious(num)) {
                System.out.println(num);
                sum = sum.add(BigInteger.valueOf(num));
            }
        }

        System.out.println("SUM is: " + sum);

    }
}
