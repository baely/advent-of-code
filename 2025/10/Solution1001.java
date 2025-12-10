List<Boolean> parseGoalState(String input) {
    List<Boolean> state = new ArrayList<>();

    for (int i = 1; i < input.length() - 1; i++) {
        char c = input.charAt(i);

        switch (c) {
            case '.':
                state.add(false);
                break;
            case '#':
                state.add(true);
                break;
        }
    }

    return state;
}

List<List<Boolean>> parseButtons(int lightCount, List<String> input) {
    List<List<Boolean>> buttons = new ArrayList<>();

    for (String button : input) {
        List<Boolean> state = new ArrayList<>();

        Set<Integer> buttonLights = new HashSet<>();

        for (String light : button.substring(1, button.length()-1).split(",")) {
            buttonLights.add(Integer.parseInt(light));
        }

        for (int i = 0; i < lightCount; i++) {
            state.add(buttonLights.contains(i));
        }

        buttons.add(state);
    }

    return buttons;
}

List<Boolean> xor (List<Boolean> a, List<Boolean> b) {
    List<Boolean> out = new ArrayList<>();
    for (int i = 0; i < a.size(); i++) {
        out.add(a.get(i) ^ b.get(i));
    }
    return out;
}

boolean isZeroed (List<Boolean> input) {
    for (Boolean light : input) {
        if (light) return false;
    }
    return true;
}

int findMinPresses (List<Boolean> state, List<List<Boolean>> availableButtons) {
    // Check if any single button press is good enough
    for (List<Boolean> button : availableButtons) {
        List<Boolean> newState = xor(state, button);
        if (isZeroed(newState)) return 1;
    }

    int minPresses = Integer.MAX_VALUE;

    for (int i = 0; i < availableButtons.size(); i++) {
        List<Boolean> button = availableButtons.get(i);
        List<Boolean> newState = xor(state, button);

        List<List<Boolean>> newAvailableButtons = availableButtons.subList(i+1, availableButtons.size());

        int presses = findMinPresses(newState, newAvailableButtons);

        if (presses == Integer.MAX_VALUE) continue;

        presses++;

        if (presses < minPresses) minPresses = presses;
    }

    return minPresses;
}

void solve(List<String> input) {
    int minPressSum = 0;

    for (String line : input) {
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

        List<Boolean> goalState = parseGoalState(goalStateString);
        List<List<Boolean>> buttons = parseButtons(lightCount, buttonStrings);

        int minPresses = findMinPresses(goalState, buttons);
        minPressSum += minPresses;
    }

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