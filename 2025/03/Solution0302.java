long findMax(String line, int digs) {
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

    i *= Math.powExact((long) 10, digs - 1);
    i += findMax(line.substring(pos + 1), digs - 1);

    return i;
}

void solve(List<String> input) {
    long joltageSum = 0;

    for (String line : input) {
        joltageSum += findMax(line, 12);
    }

    IO.println(joltageSum);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/03/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return new ArrayList<>();
    }
}

void main() {
    solve(readInput());
}
