List<Integer> overlappingRanges(List<List<Long>> ranges, long start, long end) {
    List<Integer> overlaps = new ArrayList<>();

    for (int i = 0; i < ranges.size(); i++) {
        List<Long> range = ranges.get(i);
        Long rangeStart = range.get(0);
        Long rangeEnd = range.get(1);

        if (
                (rangeStart <= start && start <= rangeEnd)
                || (rangeStart <= end && end <= rangeEnd)
                || (start <= rangeStart && rangeStart <= end)
                || (start <= rangeEnd && rangeEnd <= end)
        ) {
            overlaps.add(i);
        }
    }

    overlaps.sort(Integer::compare);
    return overlaps;
}

void solve(List<String> input) {
    List<List<Long>> freshRanges = new ArrayList<>();

    for (String line : input) {
        if (line.isEmpty()) break;

        List<String> range = List.of(line.split("-"));
        long start = Long.parseLong(range.get(0));
        long end = Long.parseLong(range.get(1));

        List<Integer> overlaps = overlappingRanges(freshRanges, start, end);

        long minStart = start;
        long maxEnd = end;

        for (int i : overlaps.reversed()) {
            List<Long> overlapRange = freshRanges.get(i);
            long rangeStart = overlapRange.get(0);
            long rangeEnd = overlapRange.get(1);

            if (rangeStart < minStart) minStart = rangeStart;
            if (rangeEnd > maxEnd) maxEnd = rangeEnd;

            freshRanges.remove(i);
        }

        freshRanges.add(List.of(minStart, maxEnd));
    }

    long freshIds = 0;

    for (List<Long> range : freshRanges) {
        long start = range.get(0);
        long end = range.get(1);

        freshIds += end - start + 1;
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