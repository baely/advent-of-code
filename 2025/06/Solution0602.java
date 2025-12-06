void solve(List<String> input) {
    int length = input.size();
    for (String row : input) {
        if (row.length() > length) {
            length = row.length();
        }
    }

    int i = 0;
    int j = length - 1;

    long total = 0;

    StringBuilder numBuffer = new StringBuilder();
    List<Integer> currColumn = new ArrayList<>();

    while (j >= 0) {
        String row = input.get(i);

        if (i < input.size() - 1) {
            char c;

            if (j >= row.length()) {
                c = ' ';
            } else {
                c = row.charAt(j);
            }

            numBuffer.append(c);
        } else {
            String num = numBuffer.toString();
            numBuffer = new StringBuilder();

            int actualNum = Integer.parseInt(num.strip());
            currColumn.add(actualNum);

            char c;

            if (j >= row.length()) {
                c = ' ';
            } else {
                c = row.charAt(j);
            }

            if (c != ' ') {
                long start = 0;

                switch (c) {
                    case '+':
                        for (int numnum : currColumn) {
                            start += numnum;
                        }
                        total += start;
                        break;
                    case '*':
                        start = 1;
                        for (int numnum : currColumn) {
                            start *= numnum;
                        }
                        total += start;
                        break;
                }

                currColumn = new ArrayList<>();

                j--;
            }
        }

        if (i == input.size() - 1) {
            i = 0;
            j--;
        } else {
            i++;
        }
    }

    System.out.println(total);
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