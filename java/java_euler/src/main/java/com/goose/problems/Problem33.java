package com.goose.problems;

import com.goose.util.Fraction;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Michal on 1/17/2015.
 */

/*
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
 */


public class Problem33 {

    public static void main(String[] args) {
        //Problem2 problem2 = new Problem2(new BigInteger("4000000"), Arrays.asList(new BigInteger("2")));
        //BigInteger sum = Timing.timed(problem2.toString(), () -> problem2.sumOfFibonacciUpTo());
        //System.out.println("sum= " + sum);

        List<Fraction> curiousFractions = new ArrayList<>();
        Fraction ONE = new Fraction(BigInteger.ONE);

        for(int num = 10; num <=99; num++) {
            for(int denom = num + 1; denom <= 99; denom++) {
                Fraction f = Fraction.valueOf(num, denom);
                if(f.compareTo(ONE) >= 0 || f.isFractionTrivial() ) { continue; }

                Fraction redF = f.reduceGoffingly();

                if(f.equals(redF)) {
                    System.out.println(num + " " + denom + " " + f + " " + redF);
                    curiousFractions.add(redF);
                }
            }
        }
        Fraction mult = new Fraction(BigInteger.ONE);

        for(Fraction f: curiousFractions) {
            System.out.println(f);
            mult = mult.multiply(f);
        }

        System.out.println(mult);


    }
}
