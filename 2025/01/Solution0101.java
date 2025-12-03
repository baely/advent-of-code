void solve(List<String> input) {
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

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/01/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}