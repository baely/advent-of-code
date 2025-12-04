void solve(List<String> input) {
    int total = 0;

    for (int i = 0; i < input.size(); i++) {
        String row = input.get(i);

        for (int j = 0; j < input.size(); j++) {

            if (row.charAt(j) != '@') continue;

            int thisCount = 0;

            for (int m = -1; m < 2; m++) {
                for (int n = -1; n < 2; n++) {
                    int ni, nj;
                    ni = i + m;
                    nj = j + n;

                    if (i == ni && j == nj) continue;
                    if (ni < 0 || ni >= input.size()) continue;
                    if (nj < 0 || nj >= row.length()) continue;

                    char neighbour = input.get(ni).charAt(nj);

                    if (neighbour == '@') thisCount++;
                }
            }

            if (thisCount < 4) total++;
        }
    }

    System.out.println(total);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/04/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}