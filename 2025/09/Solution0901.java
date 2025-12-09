static class Point {
    long x, y;

    public Point(long x, long y) {
        this.x = x;
        this.y = y;
    }

    public long area(Point other) {
        return (Math.abs(this.x - other.x) + 1) * (Math.abs(this.y - other.y) + 1);
    }
}

void solve(List<String> input) {
    List<Point> points = new ArrayList<>();

    for (String line : input) {
        List<String> coords = List.of(line.split(","));
        int x = Integer.parseInt(coords.get(0));
        int y = Integer.parseInt(coords.get(1));
        Point point = new Point(x, y);
        points.add(point);
    }

    long maxArea = 0L;

    for (int i = 0; i < points.size() - 1; i++) {
        Point point1 = points.get(i);
        for (int j = i + 1; j < points.size(); j++) {
            Point point2 = points.get(j);
            long area = point1.area(point2);

            if (area > maxArea) {
                maxArea = area;
            }
        }
    }

    System.out.println(maxArea);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/09/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}