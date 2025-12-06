'''
Project Name: Project464_AaryaSoni
Author: Aarya Soni
Date: 2024-06-15

'''


def parse_grammar(fileName):
    rules = []
    with open(fileName) as file:
        n = int(file.readline().strip())

        for _ in range(n):
            line = file.readline().strip()
            lhs, rhs = line.split("=")
            rules.append((lhs, rhs))

    return rules


def is_terminal(symbol):
    return symbol.islower() or symbol.isdigit()


def is_non_terminal(symbol):
    return symbol.isupper()


def is_cnf(fileName):
    rules = parse_grammar(fileName)

    # finding the start variable
    start_variable = "S"

    for lhs, rhs in rules:

        # LHS must be a single non-terminal
        if len(lhs) != 1 or not lhs.isupper():
            return False

        for rhs in rhs.split("|"):
            # Case 1: epsilon
            if rhs == "$":
                if lhs != start_variable:
                    return False
                continue

            # Case 2: one symbol: must be terminal
            if len(rhs) == 1:
                if not is_terminal(rhs):
                    return False
                continue

            # Case 3: two symbols: must both be variables
            if len(rhs) == 2:
                if not (is_non_terminal(rhs[0]) and is_non_terminal(rhs[1])):
                    return False
                continue

            # Anything longer than 2 symbols is not CNF
            return False
    return True


def can_generate_string(fileName, w):
    """
    Part 2
    Given a CNF grammar in fileName and a string w,
    return True if the grammar can generate w using brute force.
    """

    rules = parse_grammar(fileName)
    start_variable = "S"

    # Build productions: variable -> list of rhs strings
    productions = {}
    for lhs, rhs_full in rules:
        alts = rhs_full.split("|")
        if lhs not in productions:
            productions[lhs] = []
        for alt in alts:
            productions[lhs].append(alt)

    # Handle empty string case
    if w == "":
        if start_variable in productions:
            for rhs in productions[start_variable]:
                if rhs == "$":
                    return True
        return False

    n = len(w)
    max_steps = 2 * n - 1

    def dfs(sentential, steps):
        """
        sentential is a list of symbols, for example ['S'] or ['A','B'] or ['a','b']
        steps is how many production applications have happened so far
        """

        # If we used all steps, check if we exactly got w with only terminals
        if steps == max_steps:
            current = "".join(sentential)
            if current == w:
                # make sure there are no non terminals left
                for s in sentential:
                    if is_non_terminal(s):
                        return False
                return True
            else:
                return False

        # Find first non terminal in the sentential form
        var_index = -1
        for i, sym in enumerate(sentential):
            if is_non_terminal(sym):
                var_index = i
                break

        # If no non terminal is left but we still have steps remaining, we cannot continue
        if var_index == -1:
            return False

        var = sentential[var_index]

        # If this variable has no productions, this path fails
        if var not in productions:
            return False

        # Try each production for this variable
        for rhs in productions[var]:
            # For non empty w we can skip epsilon, it will never be used in a valid 2n-1 derivation
            if rhs == "$":
                continue

            # Replace the variable at var_index with the symbols of rhs
            new_sentential = (
                sentential[:var_index]
                + list(rhs)
                + sentential[var_index + 1:]
            )

            if dfs(new_sentential, steps + 1):
                return True

        return False

    # Start from the start symbol S
    return dfs([start_variable], 0)


def can_it_work_under_1_minute(fileName, length):
    """
    Part 3:
    Given a CNF grammar file and a string length,
    return True if the brute force algorithm from Part 2
    is definitely safe to run (rough estimate).
    """

    # Read the grammar
    rules = parse_grammar(fileName)

    # Build productions: variable -> list of right hand sides
    productions = {}
    for lhs, rhs_full in rules:
        alts = rhs_full.split("|")
        if lhs not in productions:
            productions[lhs] = []
        for alt in alts:
            productions[lhs].append(alt)

    # Find the maximum number of alternatives any variable has
    max_branching = 0
    for lhs in productions:
        count = len(productions[lhs])
        if count > max_branching:
            max_branching = count

    # If there is at most 1 production per variable,
    # there is basically only one path to explore.
    if max_branching <= 1:
        return True

    # Empty string case is always cheap
    if length == 0:
        return True

    # Worst case number of derivation steps
    steps = 2 * length - 1

    # Very rough limit for how many possibilities we are willing to explore
    MAX_NODES = 10_000_000  # 10 million

    # Estimate max_branching ** steps, but stop early if it gets too big
    total = 1
    for _ in range(steps):
        total *= max_branching
        if total > MAX_NODES:
            return False

    return True
