package com.goose.util;

/**
 * Created by Michal on 1/18/2015.
 */
public class IntUtils {

    public static boolean isInteger(String string) {
        try {
            Integer.valueOf(string);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static int[] rotations(int num) {

        String s = "" + num;
        int[] ret = new int[s.length()];
        int curr;
        for(int offset = 0; offset < s.length(); offset++) {
            curr = Integer.valueOf(s.substring(offset, s.length()) + s.substring(0, offset));
            ret[offset] = curr;
        }
        return ret;
    }

}
