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

static class Box {
    Point p1, p2;

    public Box(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public boolean contains(Point p) {
        long top, bottom, left, right;

        if (this.p1.x < this.p2.x) {
            left = this.p1.x;
            right = this.p2.x;
        } else {
            left = this.p2.x;
            right = this.p1.x;
        }

        if (this.p1.y < this.p2.y) {
            top = this.p1.y;
            bottom = this.p2.y;
        } else {
            top = this.p2.y;
            bottom = this.p1.y;
        }

        return top < p.y && p.y < bottom
                && left < p.x && p.x < right;
    }

    public boolean containsAny(List<Point> points) {
        for (Point point : points) {
            if (this.contains(point)) return true;
        }
        return false;
    }

    public List<Point> allPoints() {
        List<Point> points = new ArrayList<>();
        long top, bottom, left, right;
        if (this.p1.x < this.p2.x) {
            left = this.p1.x;
            right = this.p2.x;
        } else {
            left = this.p2.x;
            right = this.p1.x;
        }

        if (this.p1.y < this.p2.y) {
            top = this.p1.y;
            bottom = this.p2.y;
        } else {
            top = this.p2.y;
            bottom = this.p1.y;
        }

        for (long i = top; i <= bottom; i++) {
            for (long j = left; j <= right; j++) {
                points.add(new Point(j, i));
            }
        }

        return points;
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

    List<Point> borderPoints = new ArrayList<>();

    for (int i = 0; i < points.size(); i++) {
        Point p1 = points.get(i);
        Point p2 = points.get((i+1) % points.size());
        Box line = new Box(p1, p2);
        borderPoints.addAll(line.allPoints());
    }

    long maxArea = 0L;

    for (int i = 0; i < points.size() - 1; i++) {
        Point point1 = points.get(i);
        for (int j = i + 1; j < points.size(); j++) {
            Point point2 = points.get(j);

            Box box = new Box(point1, point2);
            if (box.containsAny(borderPoints)) {
                continue;
            }

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