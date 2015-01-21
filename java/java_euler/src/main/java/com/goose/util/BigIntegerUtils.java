package com.goose.util;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Michal on 1/17/2015.
 */
public class BigIntegerUtils {

    public static int[] getDigits(BigInteger num) {
        if(num == null) { throw new IllegalArgumentException("Argument is null"); }

        String s = num.toString();
        int[] ret = new int[s.length()];
        for(int i =0; i< s.length(); i++) {
            ret[i] = Character.getNumericValue(s.charAt(i));
        }
        return ret;
    }

    public static int[] getDigits(int num) {

        String s = "" + num;

        int[] ret = new int[s.length()];
        for(int i =0; i< s.length(); i++) {
            ret[i] = Character.getNumericValue(s.charAt(i));
        }
        return ret;
    }

    public static BigInteger factorial(int number) {
        if(number <= 1) { return BigInteger.ONE; }
        BigInteger ret = BigInteger.ONE;

        for(int curr = 2; curr <= number; curr++) {
            ret = ret.multiply(BigInteger.valueOf(curr));
        }
        return ret;
    }

    public static BigInteger factorial(BigInteger number) {
        if(number.compareTo(BigInteger.valueOf(1)) <= 0) { return BigInteger.ONE; }
        BigInteger ret = BigInteger.ONE;

        for(BigInteger curr = BigInteger.valueOf(2); curr.compareTo(number) <= 0; curr = curr.add(BigInteger.ONE)) {
            ret = ret.multiply(curr);
        }
        return ret;
    }

    public static BigInteger factorial(int[] digits) {
        if(digits == null) { return null; }

        BigInteger ret = BigInteger.ZERO;

        for(int digit: digits) {
            ret = ret.add(factorial(digit));
        }
        return ret;
    }


    public static boolean isNumberFactorialyCurious(BigInteger num) {
        return factorial(getDigits(num)).compareTo(num) == 0;
    }

    public static boolean isNumberFactorialyCurious(int num) {
        return factorial(getDigits(num)).compareTo(BigInteger.valueOf(num)) == 0;
    }

    public static int[] rotations(int num) {

        String s = "" + num;
        int[] ret = new int[s.length()];
        int curr;
        for(int offset = 0; offset < s.length(); offset++) {
            curr = Integer.valueOf(s.substring(offset, s.length()) + s.substring(0, offset));
            ret[offset] = curr;
        }
        return ret;
    }
    public static BigInteger[] rotations(BigInteger num) {

        String s = num.toString();
        BigInteger[] ret = new BigInteger[s.length()];
        BigInteger curr;
        for(int offset = 0; offset < s.length(); offset++) {
            curr = new BigInteger(s.substring(offset, s.length()) + s.substring(0, offset));
            ret[offset] = curr;
        }
        return ret;
    }

    public static boolean isPalindrome(int num) {
        if(num < 10 && num > -10) return true;

        int[] digits = getDigits(num);

        for(int i = 0; i<digits.length/2; i++) {
            if(digits[i] != digits[digits.length - 1 - i]) return false;
        }

        return true;
    }





}
