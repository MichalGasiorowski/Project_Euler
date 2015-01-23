package com.goose.util;

/**
 * Created by Michal on 1/18/2015.
 */
public class StringUtils {

    public static boolean isPalindrome(String s) {
        if(s == null ) return false;
        if(s.length() <= 1) return true;

        for(int i = 0; i<s.length()/2; i++) {
            if(s.charAt(i) != s.charAt(s.length() - 1 - i)) return false;
        }

        return true;
    }

    public static boolean isPandigital(String s) {
        for(int i=0; i < s.length(); i++) {
            if(s.indexOf(s.charAt(i), i+1) != -1) return false;
        }
        return true;
    }

    public static boolean isPandigital(long num) {
        return isPandigital(String.valueOf(num));
    }

    public static boolean isPandigital(int num) {
        return isPandigital(String.valueOf(num));
    }

    public static boolean areDisjoint(String s1, String s2) {
        if(s1 == null || s2 == null) return true;
        for(int i=0; i< s1.length(); i++) {
            if(s2.indexOf(s1.charAt(i)) != -1) return false;
        }
        return true;
    }

    public static boolean differentDigits(int a, int b) {
        return areDisjoint(String.valueOf(a), String.valueOf(b));
    }

    public static boolean allDifferentDigits(long a, long b) {
        return areDisjoint(String.valueOf(a), String.valueOf(b));
    }

    public static int numberOfDigits(int a, int b, int c) {
        return String.valueOf(a).length() + String.valueOf(b).length() + String.valueOf(c).length();
    }

    public static boolean is12AndLastSecLastDistinct(String s) {
        if(s == null || s.length() < 2) return true;
        int first = 0;
        int last = s.length() - 1;

        return s.charAt(first) != s.charAt(first + 1) && s.charAt(last) != s.charAt(last - 1);

    }

}
