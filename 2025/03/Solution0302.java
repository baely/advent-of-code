import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Solution0302 {
    public static long findMax(String line, int digs) {
        long i = 9;
        int pos;

        while (true) {
            char c = String.valueOf(i).charAt(0);

            int p = line.indexOf(c);

            if (p >= 0 && p < line.length() - digs + 1) {
                pos = p;
                break;
            }

            i--;
        }

        if (digs == 1) {
            return i;
        }

        i *= Math.powExact((long)10, digs - 1);
        i += findMax(line.substring(pos + 1), digs - 1);

        return i;
    }

    public static void solve(String[] input) {
        long joltageSum = 0;

        for (String line : input) {
            joltageSum += findMax(line, 12);
        }

        System.out.println(joltageSum);
    }

    public static String[] readInput() {
        try {
            List<String> lines = Files.readAllLines(Paths.get("./2025/03/input.txt"));
            return lines.toArray(new String[0]);
        } catch (IOException e) {
            e.printStackTrace();
            return new String[0];
        }
    }

    public static void main(String[] args) {
        String[] input = readInput();
        solve(input);
    }
}