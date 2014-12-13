package com.goose.problems;

import com.goose.util.Timing;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

import static com.goose.util.MyFunctional.divFunctionTransformLong;

/**
 * Created by Michal on 12/12/2014.
 */
/*
https://projecteuler.net/problem=1
*/
public class Problem1 {

    private Long upperLimit;
    private List<Long> multiplies;

    List<Predicate<Long>> multiplierPredicates;

    public Problem1(Long upperLimit, List<Long> multiplies) {
        this.upperLimit = upperLimit;
        this.multiplies = multiplies;

        multiplierPredicates = this.multiplies.stream()
                .map(num -> divFunctionTransformLong.apply(num))
                .collect(Collectors.toList());
    }

    public Long sumOfMultipliesUpTo() {
        return LongStream.range(1, upperLimit)
                .filter(num -> multiplierPredicates.stream().anyMatch(f -> f.test(num)))
                .sum();
    }

    @Override
    public String toString() {
        return "Problem1{" +
                "upperLimit=" + upperLimit +
                ", multiplies=" + multiplies +
                '}';
    }

    public static void main(String[] args) {
        Problem1 problem1 = new Problem1(100L, Arrays.asList(3L, 5L));
        Long sum = Timing.timed(problem1.toString(), () -> problem1.sumOfMultipliesUpTo());
        System.out.println(sum);

    }

}
