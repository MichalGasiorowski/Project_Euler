package com.goose.problems;

import com.goose.util.StringUtils;
import org.javatuples.Triplet;

import java.util.*;

/**
 * Created by Michal on 1/21/2015.
 */
/*
Pandigital products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 */

public class Problem32 {


    public static void main(String[] args) {
        int a, b, c;

        //Map<Integer, Triplet<Integer, Integer, Integer>> pandigitalTriplets = new ArrayList<Triplet<Integer, Integer, Integer>>();
        Set<Integer> pandigitalProducts = new HashSet<>();
        int sum = 0;


        for(a = 2; a < 1000; a++) {
            if(!StringUtils.isPandigital(a) || String.valueOf(a).contains("0")) continue;
            //System.out.println("a=" + a);
            for(b = a + 1; b < 9999; b++) {
                if(!StringUtils.isPandigital(b) || !StringUtils.allDifferentDigits(a, b) || String.valueOf(b).contains("0")) continue;
                //System.out.println("\tb=" + b);
                c = a * b;
                if(!StringUtils.isPandigital(c) || String.valueOf(c).contains("0") || !StringUtils.allDifferentDigits(a, c)
                        || !StringUtils.allDifferentDigits(b, c) || StringUtils.numberOfDigits(a,b,c) != 9) continue;
                pandigitalProducts.add(c);
                System.out.println(String.format("a=%d\tb=%d\tc=%d", a, b, c));
                //pandigitalTriplets.add(new Triplet<>(a, b, c));
            }
        }
        for(Integer product: pandigitalProducts) {
            sum += product;
        }

        System.out.println(String.format("sum=%d", sum));

    }
}
