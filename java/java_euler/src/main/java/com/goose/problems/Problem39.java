package com.goose.problems;

import org.javatuples.Pair;
import org.javatuples.Triplet;

import java.util.*;

/**
 * Created by Michal on 1/20/2015.
 */

/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

 */

public class Problem39 {


    //  integer triangles p^2 / 48 when p is even and to (p + 3)^2 / 48 when p is odd ??

    public static void main(String[] args) {
        Integer maxP = 1000;

        Map<Integer, List<Triplet<Integer, Integer, Integer>>> pMap = new HashMap<>();

        int a, b, c, p;
        Pair<Integer, Integer> maxSolution = new Pair<>(0, 0);
        int a2, b2, c2;

        for(p = 6; p <= maxP; p++) {
            for(a = 1; a < p/2; a++ ) {
                a2 = a*a;
                for(b = a + 1; b < p / 2; b++) {
                    c = p - a - b;
                    if(c < 1) break;
                    if(a2 + b*b == c*c) {
                        if(pMap.containsKey(p)) { pMap.get(p).add(new Triplet<>(a,b,c)); }
                        else {
                            pMap.put(p, new ArrayList<Triplet<Integer, Integer, Integer>>(
                                    Arrays.asList(new Triplet<>(a, b, c))));
                        }
                    }
                }
            }
            if(pMap.containsKey(p) && maxSolution.getValue1() < pMap.get(p).size()) {
                maxSolution = new Pair<>(p, pMap.get(p).size());
            }
        }

        System.out.println(String.format("p: %d, count: %d", maxSolution.getValue0(), maxSolution.getValue1()));
        System.out.println(pMap.get(maxSolution.getValue0()));

    }
}
