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
    
    // Build sets
    List<Set<Junction>> junctionSets = new ArrayList<>();
    
    for (Junction junction : junctions) {
        Set<Junction> set = new HashSet<>();
        set.add(junction);
        junctionSets.add(set);
    }

    // Merge by closest
    for (Pair<List<Junction>, Double> junctionPairDistance : junctionPairDistances) {
        Junction junction1 = junctionPairDistance.key.get(0);
        Junction junction2 = junctionPairDistance.key.get(1);

        Set<Junction> match1 = new HashSet<>();
        Set<Junction> match2 = new HashSet<>();

        for (Set<Junction> set : junctionSets) {
            if (set.contains(junction1)) {
                match1 = set;
            }

            if (set.contains(junction2)) {
                match2 = set;
            }
        }

        if (match1.equals(match2)) continue;

        match1.addAll(match2);
        junctionSets.remove(match2);

        if (junctionSets.size() == 1) {
            System.out.println((long)junction1.x * (long)junction2.x);
            break;
        }
    }
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