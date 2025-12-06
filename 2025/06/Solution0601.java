void solve(List<String> input) {
    List<List<Integer>> grid = new ArrayList<>();

    long totals = 0;

    for (String line : input) {
        List<String> nums = List.of(line.split(" "));

        if (nums.size() <= 0) continue;

        boolean ops = false;
        if (nums.getFirst().equals("*") || nums.getFirst().equals("+")) {
            int i = 0;
            for (String op : nums) {
                if (op.isEmpty()) continue;

                long calc = 0;

                switch (op) {
                    case "*":
                        calc = 1;
                        for (List<Integer> row : grid) {
                            int num = row.get(i);
                            calc *= num;
                        }
                        break;
                    case "+":
                        calc = 0;
                        for (List<Integer> row : grid) {
                            int num = row.get(i);
                            calc += num;
                        }
                }
                totals += calc;
                i++;
            }

            continue;
        }

        List<Integer> row = new ArrayList<>();

        for (String num : nums) {
            if (num.isEmpty()) continue;

            int intNum = Integer.parseInt(num);
            row.add(intNum);
        }

        grid.add(row);
    }

    System.out.println(totals);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/06/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}