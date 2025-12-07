void solve(List<String> input) {
    String init = input.getFirst();
    Set<Integer> indices = new HashSet<>();
    indices.add(init.indexOf('S'));

    int splitCount = 0;

    for (String line : input) {
        Set<Integer> nextIndices = new HashSet<>();

        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) != '^') continue;

            if (!indices.contains(i)) continue;

            indices.remove(i);
            splitCount++;
            nextIndices.add(i + 1);
            nextIndices.add(i - 1);
        }

        indices.addAll(nextIndices);
    }

    System.out.println(splitCount);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/07/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}