package com.goose.util;

import java.util.Date;
import java.util.function.Consumer;
import java.util.function.Supplier;

/**
 * Created by Michal on 12/13/2014.
 */
public class Timing {

    public static <T> T timed(String description, Supplier<T> code) {
        Consumer<String> defaultOutput = System.out::println;
        return timed(description, defaultOutput, code);
    }

    public static <T> T timed(String description, Consumer<String> output,
                              Supplier<T> code) {
        final Date start = new Date();
        T result = code.get();
        final Long duration = new Date().getTime() - start.getTime();
        output.accept(description + " took " + duration + " milliseconds");

        return result;
    }

}
