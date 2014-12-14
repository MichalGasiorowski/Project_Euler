package com.goose.util;

import java.math.BigInteger;
import java.util.function.Function;
import java.util.function.Predicate;

/**
 * Created by Michal on 12/13/2014.
 */
public class MyFunctional {

    public static Function<BigInteger, Predicate<BigInteger>> divFunctionTransformBigInteger = (x) -> (num -> num.remainder(x).compareTo(BigInteger.ZERO) == 0);
    public static Function<Long, Predicate<Long>> divFunctionTransformLong = (x) -> (num -> num % x == 0);
    public static Function<Integer, Predicate<Integer>> divFunctionTransformInt = (x) -> (num -> num % x == 0);


}
