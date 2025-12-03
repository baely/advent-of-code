import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Solution0301 {
    public static void solve(String[] input) {
        int joltageSum = 0;

        for (String line : input) {
            int i = 9;
            int pos;

            while (true) {
                char c = String.valueOf(i).charAt(0);

                int p = line.indexOf(c);

                if (p >= 0 && p < line.length() - 1) {
                    pos = p;
                    break;
                }

                i--;
            }

            char[] remChars = line.substring(pos + 1).toCharArray();

            char maxC = '0';

            for (char c : remChars) {
                maxC = (char) Math.max(maxC, c);
            }

            joltageSum += i * 10;
            joltageSum += maxC - '0';
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