import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Solution1 {
    public static void solve(String[] input) {
        int position = 50;
        int zeroCounts = 0;

        for (String line : input) {
            char dir = line.charAt(0);
            int delta = Integer.parseInt(line.substring(1));

            if (dir == 'L') {
                delta = -delta;
            }

            position += delta;
            position = position % 100;

            if (position == 0) {
                zeroCounts++;
            }
        }

        System.out.println(zeroCounts);
    }

    public static String[] readInput() {
        try {
            List<String> lines = Files.readAllLines(Paths.get("input.txt"));
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