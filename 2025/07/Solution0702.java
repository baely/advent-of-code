void solve(List<String> input) {
    String init = input.getFirst();

    Map<Integer, Long> indexCount = new HashMap<>();
    indexCount.put(init.indexOf('S'), 1L);

    for (String line : input) {
        Map<Integer, Long> nextIndexCount = new HashMap<>();

        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) != '^') continue;

            long prevCount = indexCount.getOrDefault(i, 0L);
            indexCount.remove(i);

            long leftCount = nextIndexCount.getOrDefault(i-1, 0L);
            long rightCount = nextIndexCount.getOrDefault(i+1, 0L);

            nextIndexCount.put(i-1, prevCount + leftCount);
            nextIndexCount.put(i+1, prevCount + rightCount);
        }

        for (int i = 0; i < line.length(); i++) {
            long existing = indexCount.getOrDefault(i, 0L);
            long newCount = nextIndexCount.getOrDefault(i, 0L);

            indexCount.put(i, existing + newCount);
        }
    }

    long splitCount = 0L;

    for (long count : indexCount.values()) {
        splitCount += count;
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