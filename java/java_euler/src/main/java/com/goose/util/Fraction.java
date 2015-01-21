package com.goose.util;

import java.io.Serializable;
import java.math.BigInteger;
import java.util.regex.Pattern;

/**
 * Created by Michal on 1/17/2015.
 */

public class Fraction extends Number implements Comparable<Fraction>, Serializable {

    private final BigInteger num_unreduced;
    private final BigInteger denom_unreduced;

    private final BigInteger numerator;
    private final BigInteger denominator;

    public static final Fraction ONE = new Fraction(BigInteger.ONE);
    public static final Fraction ZERO = new Fraction(BigInteger.ZERO);

    private static final long serialVersionUID = -1385607332548302424L;

    public Fraction(BigInteger numerator, BigInteger denominator) {
        if(numerator == null) {
            throw new IllegalArgumentException("Numerator is null");
        }
        if(denominator == null) {
            throw new IllegalArgumentException("Denominator is null");
        }
        if(denominator.equals(BigInteger.ZERO)) {
            throw new IllegalArgumentException("Denominator is ZERO");
        }

        if(denominator.signum() < 0) {
            this.numerator = this.num_unreduced = numerator.negate();
            this.denominator = this.denom_unreduced = denominator.negate();
        } else if(numerator.signum() == 0) {
            this.numerator = this.num_unreduced = numerator;
            this.denominator = this.denom_unreduced = BigInteger.ONE;
        } else {
            BigInteger gcd = numerator.gcd(denominator);
            this.num_unreduced = numerator;
            this.denom_unreduced = denominator;
            this.numerator = numerator.divide(gcd);
            this.denominator = denominator.divide(gcd);
        }
    }

    public Fraction(BigInteger numerator) {
        this.numerator = this.num_unreduced = numerator;
        this.denominator = this.denom_unreduced = BigInteger.ONE;
    }

    public static Fraction valueOf(String s) {
        int sPos = s.indexOf("/");
        Fraction ret;
        if(sPos < 0) {
            Fraction f = new Fraction(new BigInteger(s));
            ret = new Fraction(f.numerator, f.denominator);
        }
        else {
            BigInteger num = new BigInteger(s.substring(0, sPos));
            BigInteger denom = new BigInteger(s.substring(sPos + 1, s.length()));
            ret = new Fraction(num, denom);
        }
        return ret;
    }

    public static Fraction valueOf(int numerator, int denominator) {
        return new Fraction(new BigInteger("" + numerator), new BigInteger("" + denominator));
    }

    public static Fraction valueOf(long numerator, long denominator) {
        return new Fraction(new BigInteger("" + numerator), new BigInteger("" + denominator));
    }




    private Fraction reduce() {
        BigInteger gcd = numerator.gcd(denominator);
        return new Fraction(numerator.divide(gcd), denominator.divide(gcd));
    }

    public Fraction add(Fraction o) {
        if(o == null) {
            throw new IllegalArgumentException("Argument is null");
        }
        else if(o.numerator.signum() == 0) { return this; }
        else if(this.numerator.signum() == 0) { return o; }
        else if(this.denominator.equals(o.denominator)) { return new Fraction(this.numerator.add(o.numerator), this.denominator); }
        else {
            return new Fraction(numerator.multiply(o.denominator).add(o.numerator.multiply(denominator)), denominator.multiply(o.denominator));
        }
    }

    public Fraction subtract(Fraction o) {
        return this.add(o.negate());
    }
    
    public Fraction multiply(Fraction o) {
        if(o == null) {
            throw new IllegalArgumentException("Argument is null");
        }
        else {
            return new Fraction(numerator.multiply(o.numerator), denominator.multiply(o.denominator));
        }
    }
    
    public Fraction negate() {
        return new Fraction(this.numerator.negate(), this.denominator);
    }

    public int signum() {
        return numerator.signum();
    }

    @Override
    public int compareTo(Fraction o) {
        if(o == null) {
            throw new IllegalArgumentException("Argument is null");
        }
        if(signum() != o.signum()) {
            return signum() - o.signum();
        }
        if(denominator.equals(o.denominator)) { return numerator.compareTo(o.numerator); }

        return numerator.multiply(o.denominator).compareTo(o.numerator.multiply(denominator));

    }

    public boolean isInteger() { return signum() == 0 || denominator.equals(BigInteger.ONE); }

    public boolean isFractionTrivial() {

        BigInteger[] numDR =  num_unreduced.divideAndRemainder(BigInteger.TEN);
        BigInteger[] denomDR =  denom_unreduced.divideAndRemainder(BigInteger.TEN);

        return (numDR[1].compareTo(BigInteger.ZERO) == 0 && denomDR[1].compareTo(BigInteger.ZERO) == 0 )
                || (numDR[1].compareTo(numDR[0]) == 0 && denomDR[1].compareTo(denomDR[0]) == 0 ) ;
    }

    // only for 2-digit numerator & denominator
    public Fraction reduceGoffingly() {
        BigInteger[] numDR =  num_unreduced.divideAndRemainder(BigInteger.TEN);
        BigInteger[] denomDR =  denom_unreduced.divideAndRemainder(BigInteger.TEN);

        //if(num1 == denom10 && denom1 != 0)
        if(numDR[1].compareTo(denomDR[0]) == 0 && denomDR[1].compareTo(BigInteger.ZERO) != 0 ) {
            return new Fraction(numDR[0], denomDR[1]);
        }
        else if(numDR[0].compareTo(denomDR[1]) == 0 && denomDR[0].compareTo(BigInteger.ZERO) != 0) {
            return new Fraction(numDR[1], denomDR[0]);
        } else { return null; }

    }


    public final BigInteger getDenominator() {
        return denominator;
    }

    public final BigInteger getNumerator() {
        return numerator;
    }

    public final BigInteger getNum_unreduced() {
        return num_unreduced;
    }

    public final BigInteger getDenom_unreduced() {
        return denom_unreduced;
    }

    @Override
    public int intValue() {
        return isInteger() ? numerator.intValue() : numerator.divide(denominator).intValue();
    }

    @Override
    public long longValue() {
        return isInteger() ? numerator.longValue() : numerator.divide(denominator).longValue();
    }

    @Override
    public float floatValue() {
        return (float)doubleValue();
    }

    @Override
    public double doubleValue() {
        return isInteger() ? numerator.doubleValue() : numerator.divide(denominator).doubleValue();
    }

    @Override
    public String toString() {
        return isInteger() ? String.format("%,d", numerator) : String.format("%,d / %,d", numerator, denominator);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Fraction fraction = (Fraction) o;

        if (!denominator.equals(fraction.denominator)) return false;
        if (!numerator.equals(fraction.numerator)) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = numerator.hashCode();
        result = 31 * result + denominator.hashCode();
        return result;
    }
}
