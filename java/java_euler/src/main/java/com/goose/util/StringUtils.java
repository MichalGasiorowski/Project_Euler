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
}
