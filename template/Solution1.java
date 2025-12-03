void solve(List<String> input) {
    //
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./YYYY/DD/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}