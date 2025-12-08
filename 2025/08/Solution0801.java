static class Junction implements Comparable<Junction> {
    int x, y, z;

    public Junction(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double distance(Junction other) {
        return Math.sqrt(
                Math.pow(this.x - other.x, 2)
                + Math.pow(this.y - other.y, 2)
                + Math.pow(this.z - other.z, 2)
        );
    }

    public String toString() {
        return String.format("(%d, %d, %d)", this.x, this.y, this.z);
    }

    @Override
    public int compareTo(Junction o) {
        int c;

        c = Integer.compare(this.x, o.x);

        if (c != 0) {
            return c;
        }

        c = Integer.compare(this.y, o.y);

        if (c != 0) {
            return c;
        }

        return Integer.compare(this.z, o.z);
    }
}

static public class Pair<K, V extends Comparable<V>> implements Comparable<Pair<K, V>> {
    K key;
    V val;

    public Pair(K key, V val) {
        this.key = key;
        this.val = val;
    }

    @Override
    public int compareTo(Pair<K, V> o) {
        return this.val.compareTo(o.val);
    }
}

static final int CONNECTION_COUNT = 1_000;

void solve(List<String> input) {
    // Parse input
    List<Junction> junctions = new ArrayList<>();

    for (String line : input) {
        List<String> coords = List.of(line.split(","));

        int x = Integer.parseInt(coords.get(0));
        int y = Integer.parseInt(coords.get(1));
        int z = Integer.parseInt(coords.get(2));

        Junction junction = new Junction(x, y, z);
        junctions.add(junction);
    }

    // Calculate distances
    List<Pair<List<Junction>, Double>> junctionPairDistances = new ArrayList<>();

    for (int i = 0; i < junctions.size() - 1; i++) {
        for (int j = i + 1; j < junctions.size(); j++) {
            Junction j1 = junctions.get(i);
            Junction j2 = junctions.get(j);

            List<Junction> pair = List.of(j1, j2);
            double distance = j1.distance(j2);

            junctionPairDistances.add(
                    new Pair<>(pair, distance)
            );
        }
    }

    junctionPairDistances.sort(Pair::compareTo);

    List<Set<Junction>> junctionSets = new ArrayList<>();

    for (Pair<List<Junction>, Double> pair : junctionPairDistances) {
        Set<Junction> junctionSet = new HashSet<>();

        junctionSet.add(pair.key.get(0));
        junctionSet.add(pair.key.get(1));

        junctionSets.add(junctionSet);

        if (junctionSets.size() >= CONNECTION_COUNT) {
            break;
        }
    }

    // Merge sets
    for (int i = junctionSets.size() - 1; i > 0; i--) {
        Set<Junction> set1 = junctionSets.get(i);
        for (int j = 0; j < i; j++) {
            Set<Junction> set2 = junctionSets.get(j);

            boolean overlap = false;

            for (Junction junction : set1) {
                if (set2.contains(junction)) {
                    overlap = true;
                    break;
                }
            }

            if (overlap) {
                set2.addAll(set1);
                junctionSets.remove(i);

                break;
            }
        }
    }

    // Build sorted sizes list
    List<Integer> sizes = new ArrayList<>();
    for (Set<Junction> junctionSet : junctionSets) {
        sizes.add(junctionSet.size());
    }
    sizes.sort(Integer::compare);

    int output = 1;
    int count = 0;

    for (int size : sizes.reversed()) {
        output *= size;
        count++;

        if (count == 3) {
            break;
        }
    }

    System.out.println(output);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/08/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}