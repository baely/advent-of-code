List<List<Integer>> parseButtons(int lightCount, List<String> input) {
    List<List<Integer>> buttons = new ArrayList<>();

    for (String button : input) {
        List<Integer> state = new ArrayList<>();

        Set<Integer> buttonLights = new HashSet<>();

        for (String light : button.substring(1, button.length()-1).split(",")) {
            buttonLights.add(Integer.parseInt(light));
        }

        for (int i = 0; i < lightCount; i++) {
            if (buttonLights.contains(i)) {
                state.add(1);
            } else {
                state.add(0);
            }
        }

        buttons.add(state);
    }

    return buttons;
}

List<Integer> parseJoltageRequirements(String input) {
    List<Integer> joltageLights = new ArrayList<>();

    for (String light : input.substring(1, input.length()-1).split(",")) {
        joltageLights.add(Integer.parseInt(light));
    }

    return joltageLights;
}

List<Integer> pressButton (List<Integer> joltages, List<Integer> b) {
    List<Integer> out = new ArrayList<>();
    for (int i = 0; i < joltages.size(); i++) {
        out.add(joltages.get(i) - b.get(i));
    }
    return out;
}

boolean isZeroed (List<Integer> input) {
    for (int light : input) {
        if (light != 0) return false;
    }
    return true;
}

int findMinPresses (List<Integer> state, List<List<Integer>> availableButtons) {
    // Early return on invalid state
    for (int light : state) {
        if (light < 0) {
            return Integer.MAX_VALUE;
        }
    }

    // Check if any single button press is good enough
    for (List<Integer> button : availableButtons) {
        List<Integer> newState = pressButton(state, button);
        if (isZeroed(newState)) return 1;
    }

    int minPresses = Integer.MAX_VALUE;

    for (List<Integer> button : availableButtons) {
        List<Integer> newState = pressButton(state, button);

        int presses = findMinPresses(newState, availableButtons);

        if (presses == Integer.MAX_VALUE) continue;

        presses++;

        if (presses < minPresses) minPresses = presses;
    }

    return minPresses;
}

void solve(List<String> input) {
    int minPressSum = input.parallelStream()
        .mapToInt(line -> {
            List<String> lineParts = List.of(line.split(" "));

            String goalStateString = "", jolatageRequirementsString = "";
            List<String> buttonStrings = new ArrayList<>();

            for (int i = 0; i < lineParts.size(); i++) {
                String part = lineParts.get(i);
                if (i == 0) {
                    goalStateString = part;
                } else if (i == lineParts.size() - 1) {
                    jolatageRequirementsString = part;
                } else {
                    buttonStrings.add(part);
                }
            }

            int lightCount = goalStateString.length() - 2;

            List<List<Integer>> buttons = parseButtons(lightCount, buttonStrings);
            List<Integer> joltageRequirements = parseJoltageRequirements(jolatageRequirementsString);

            return findMinPresses(joltageRequirements, buttons);
        })
        .sum();

    System.out.println(minPressSum);
}

List<String> readInput() {
    try {
        return Files.readAllLines(Paths.get("./2025/10/input.txt"));
    } catch (IOException e) {
        e.printStackTrace();
        return List.of();
    }
}

void main() {
    solve(readInput());
}