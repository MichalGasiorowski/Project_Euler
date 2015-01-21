package com.goose.problems;

import com.goose.util.FibonacciSupplier;
import com.goose.util.Timing;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.LongStream;
import java.util.stream.Stream;

import static com.goose.util.MyFunctional.divFunctionTransformBigInteger;
import static com.goose.util.MyFunctional.divFunctionTransformLong;

/**
 * Created by Michal on 12/13/2014.
 */
/*
https://projecteuler.net/problem=2
 */
public class Problem2 {

    private BigInteger valueLimit;
    private List<BigInteger> divList;

    List<Predicate<BigInteger>> multiplierPredicates;

    public Problem2(BigInteger valueLimit, List<BigInteger> divList ) {
        this.divList = divList;
        this.valueLimit = valueLimit;

        multiplierPredicates = this.divList.stream()
                .map(num -> divFunctionTransformBigInteger.apply(num))
                .collect(Collectors.toList());
    }

    public BigInteger sumOfFibonacciUpTo() {
        // ugly - can't limit stream on element
        return Stream.generate(new FibonacciSupplier())
                .limit(100)
                .filter(num -> multiplierPredicates.stream().anyMatch(f -> f.test(num)))
                .filter(num -> num.compareTo(valueLimit) < 1)
                .reduce(BigInteger.ZERO, (x, y) -> x.add(y));
    }

    @Override
    public String toString() {
        return "Problem2{" +
                "valueLimit=" + valueLimit +
                ", divList=" + divList +
                '}';
    }

    public static void main(String[] args) {
        Problem2 problem2 = new Problem2(new BigInteger("4000000"), Arrays.asList(new BigInteger("2")));
        BigInteger sum = Timing.timed(problem2.toString(), () -> problem2.sumOfFibonacciUpTo());
        System.out.println("sum= " + sum);

    }
}
