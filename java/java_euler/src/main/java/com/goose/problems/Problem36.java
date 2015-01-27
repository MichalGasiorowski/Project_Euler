package com.goose.problems;

import com.goose.util.BigIntegerUtils;
import com.goose.util.StringUtils;

import java.math.BigInteger;

/**
 * Created by Michal on 1/18/2015.
 */

/*
Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
 */
public class Problem36 {

    public static void main(String[] args) {
        int maxNum = 1000 * 1000;

        long sum = 0;

        for (int num = 1; num <= maxNum; num++) {
            if(BigIntegerUtils.isPalindrome(num) && StringUtils.isPalindrome(Integer.toBinaryString(num))) {

                sum += num;
            }
        }

        System.out.println("Sum is:" + sum);

    }
}
