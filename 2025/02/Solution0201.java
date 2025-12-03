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
    if (num.length() % 2 == 1) {
        return true;
    }

    int mid = num.length() / 2;

    return !num.substring(0, mid).equals(num.substring(mid));
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