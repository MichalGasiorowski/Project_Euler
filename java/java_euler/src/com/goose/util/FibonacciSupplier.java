package com.goose.util;

import java.math.BigInteger;
import java.util.function.Supplier;

/**
 * Created by Michal on 12/13/2014.
 */

public class FibonacciSupplier implements Supplier<BigInteger> {

    private BigInteger a;
    private BigInteger b;

    public FibonacciSupplier() {
        a = new BigInteger("0");
        b = BigInteger.ONE;

    }

    @Override
    public BigInteger get() {
        BigInteger res = a.add(b);
        a = b;
        b = res;
        //System.out.println(res);
        return res;
    }
}
