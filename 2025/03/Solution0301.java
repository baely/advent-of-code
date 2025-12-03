void solve(List<String> input) {
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

    IO.println(joltageSum);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/03/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}