import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Solution0202 {
    public static void solve(String[] input) {
        long invalidSum = 0;

        for (String line : input) {
            for (String range : line.split(",")) {
                String left, right;

                left = range.split("-")[0];
                right = range.split("-")[1];

                long leftInt = Long.parseLong(left);
                long rightInt = Long.parseLong(right);

                for (long x = leftInt; x <= rightInt; x++) {
                    if (!isValid(String.valueOf(x))) {
                        invalidSum += x;
                    }
                }
            }
        }

        System.out.println(invalidSum);
    }

    private static boolean isValid(String num) {
        for (int i = 1; i < num.length(); i++) {
            if (num.length() % i != 0) continue;

            int repeats = num.length() / i;

            String pattern = num.substring(0, i);
            String full = pattern.repeat(repeats);

            if (num.equals(full)) {
                return false;
            }
        }

        return true;
    }

    public static String[] readInput() {
        try {
            List<String> lines = Files.readAllLines(Paths.get("./2025/02/input.txt"));
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