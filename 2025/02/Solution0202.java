void solve(List<String> input) {
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

boolean isValid(String num) {
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

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/02/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}