boolean inRange(List<List<Long>> ranges, long x) {
    for (List<Long> range : ranges) {
        long start, end;
        start = range.get(0);
        end = range.get(1);

        if (start <= x && x <= end) {
            return true;
        }
    }

    return false;
}

void solve(List<String> input) {
    List<List<Long>> freshRanges = new ArrayList<>();

    boolean processingRanges = true;

    int freshIds = 0;

    for (String line : input) {
        if (processingRanges) {
            if (line.isEmpty()) {
                processingRanges = false;
                continue;
            }

            List<String> range = List.of(line.split("-"));
            freshRanges.add(List.of(
                    Long.parseLong(range.get(0)),
                    Long.parseLong(range.get(1))
            ));
        } else {
            long id = Long.parseLong(line);

            if (inRange(freshRanges, id)) freshIds++;
        }
    }

    System.out.println(freshIds);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/05/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}