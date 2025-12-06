"""
Test runner for Project464_AaryaSoni

This script tests:
- Part 1: CNF checker (is_cnf)
- Part 2: Membership (can_generate_string)
- Part 3: Time feasibility (can_it_work_under_1_minute)

Assumptions:
- cnf.py defines: is_cnf, can_generate_string, can_it_work_under_1_minute
- CNF test files for Part 1 are in testcases/test1.txt, testcases/test2.txt, ...
- testcases/test11.txt is your main CNF grammar for Parts 2 and 3
"""

from cnf import is_cnf, can_generate_string, can_it_work_under_1_minute


def test_part1_cnf():
    print("=== Part 1: CNF checker tests ===")

    cnf_expected_results = {
        1: True,
        2: False,
        3: False,
        4: False,
        5: True,
        6: False,
        7: False,
        8: True,
        9: False,
        10: False,
        11: False
    }

    all_passed = True

    for i in sorted(cnf_expected_results.keys()):
        file_name = f"testcases/test{i}.txt"
        result = is_cnf(file_name)
        expected = cnf_expected_results[i]

        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False

        print(
            f"test{i}.txt -> result={result}, expected={expected} [{status}]")

    if all_passed:
        print("Part 1: All CNF tests passed\n")
    else:
        print("Part 1: Some CNF tests failed\n")

    return all_passed


def test_part2_membership():
    print("=== Part 2: Membership tests (can_generate_string) ===")

    grammar_file = "testcases/test11.txt"

    membership_tests = [
        {"string": "a",    "expected": False},  # updated
        {"string": "ab",   "expected": False},
        {"string": "abba", "expected": False},
        {"string": "",     "expected": False},
    ]

    all_passed = True

    for idx, test in enumerate(membership_tests, start=1):
        w = test["string"]
        expected = test["expected"]
        result = can_generate_string(grammar_file, w)

        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False

        print(
            f"Test M{idx}: w='{w}' -> result={result}, expected={expected} [{status}]")

    if all_passed:
        print("Part 2: All membership tests passed\n")
    else:
        print("Part 2: Some membership tests failed\n")

    return all_passed


def test_part3_time():
    print("=== Part 3: Time feasibility tests (can_it_work_under_1_minute) ===")

    grammar_file = "testcases/test11.txt"

    time_tests = [
        {"length": 1,  "expected": True},
        {"length": 2,  "expected": True},
        {"length": 3,  "expected": True},
        {"length": 5,  "expected": True},
        {"length": 10, "expected": True},  # updated
    ]

    all_passed = True

    for idx, test in enumerate(time_tests, start=1):
        length = test["length"]
        expected = test["expected"]
        result = can_it_work_under_1_minute(grammar_file, length)

        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False

        print(
            f"Test T{idx}: length={length} -> result={result}, expected={expected} [{status}]")

    if all_passed:
        print("Part 3: All time feasibility tests passed\n")
    else:
        print("Part 3: Some time feasibility tests failed\n")

    return all_passed


def main():
    print("Running all project tests\n")

    part1_ok = test_part1_cnf()
    part2_ok = test_part2_membership()
    part3_ok = test_part3_time()

    if part1_ok and part2_ok and part3_ok:
        print("Overall: All parts passed")
    else:
        print("Overall: Some parts failed")


if __name__ == "__main__":
    main()
