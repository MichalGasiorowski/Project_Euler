package com.goose.problems;

import com.goose.util.StringUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;
import java.util.stream.Collectors;

/**
 * Created by Michal on 1/24/2015.
 */

/*
Pandigital multiples
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

 */

public class Problem38 {

    public static void main(String[] args) {

        int num;
        List<Long> productList;
        String productStr;
        TreeSet<Long> pandigitalSet = new TreeSet<>();

        for(num = 1; num < 9999; num++) {
            for(int n = 1; n < 10; n++) {
                productList = new ArrayList<>();
                for(int i = 1; i<= n; i++ ) { productList.add((long)num * i); }
                productStr = productList.stream().map(p -> p.toString()).collect(Collectors.joining(""));
                if(!productStr.contains("0") && productStr.length() == 9 && StringUtils.isPandigital(productStr)) {
                    pandigitalSet.add(Long.valueOf(productStr));
                }
            }
        }

        System.out.println(String.format("Max 1 to 9 pandigital number is: %d", pandigitalSet.last()));

    }
}
