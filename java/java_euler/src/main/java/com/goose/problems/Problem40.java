package com.goose.problems;

import com.goose.util.BigIntegerUtils;
import com.sun.xml.internal.stream.buffer.stax.StreamReaderBufferProcessor;

import java.math.BigInteger;
import java.util.*;

/**
 * Created by Michal on 1/24/2015.
 */

/*
Champernowne's constant
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
 */
public class Problem40 {

    public static int getDigit(BigInteger[] digitsTillNumber, BigInteger digitNumber) {
        if(digitNumber.compareTo(BigInteger.TEN) < 0) return digitNumber.intValue();
        int maxP = 0;
        while(digitsTillNumber[maxP].compareTo(digitNumber) < 0) { maxP++; }
        maxP--;

        BigInteger maxVal = digitsTillNumber[maxP];

        BigInteger[] divRem = digitNumber.subtract(maxVal).divideAndRemainder(BigInteger.valueOf(maxP+2));
        BigInteger dd = divRem[0].add(BigInteger.TEN.pow(maxP+1));
        BigInteger nextNum = dd.add(BigInteger.ONE);
        int rem = divRem[1].intValue();
        //System.out.println("maxP: " + maxP + " maxVal: " + maxVal + " nextNum: "+ nextNum + " rem: " + rem);
        int len = dd.toString().length();

        if(rem == 0) return Character.getNumericValue(dd.toString().charAt(len-1));
        return Character.getNumericValue(nextNum.toString().charAt(rem-1));
    }

    public static void main(String[] args) {
        int maxExp = 6;
        BigInteger[] digitsTillNumber = new BigInteger[maxExp+1];

        digitsTillNumber[0] = BigInteger.valueOf(9);

        for(int p = 1; p <= maxExp; p++) {
            BigInteger prev = digitsTillNumber[p-1];
            digitsTillNumber[p] = prev.add(BigInteger.valueOf(9 * (p + 1) ).multiply(BigInteger.TEN.pow(p)));
        }

        BigInteger ret = BigInteger.ONE;

        for(int p = 0; p <= maxExp; p++) {
            ret = ret.multiply(BigInteger.valueOf(getDigit(digitsTillNumber, BigInteger.TEN.pow(p))) );
            //System.out.println(getDigit(digitsTillNumber, BigInteger.TEN.pow(p)) );
        }

        System.out.println(ret);
    }
}
