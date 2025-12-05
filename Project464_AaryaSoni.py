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


# def can_generate_string():
#     return True

# def can_it_work_under_1_minute():
#     return True

if is_cnf("grammar.txt"):
    print("yes")
else:
    print("no")
