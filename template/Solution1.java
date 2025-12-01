import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Solution1 {
    public static void solve(String[] input) {
        //
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