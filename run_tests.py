"""
Simple test runner for CNF checker.
Assumes:
- is_cnf(fileName) is defined in project464.py
- test grammar files are in testcases/test1.txt ... testcases/test10.txt
"""

from cnf import is_cnf


def main():
    # Expected results based on our earlier discussion
    expected_results = {
        1: True,   # Test 1  -> yes
        2: False,  # Test 2  -> no
        3: False,  # Test 3  -> no
        4: False,  # Test 4  -> no
        5: True,   # Test 5  -> yes
        6: False,  # Test 6  -> no
        7: False,  # Test 7  -> no
        8: True,   # Test 8  -> yes
        9: False,  # Test 9  -> no
        10: False,  # Test 10 -> no
        11: False  # Test 11 -> no
    }

    all_passed = True

    for i in range(1, 12):
        file_name = f"testcases/test{i}.txt"
        result = is_cnf(file_name)
        expected = expected_results[i]

        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False

        print(
            f"test{i}.txt -> result={result}, expected={expected} [{status}]")

    if all_passed:
        print("\nAll tests passed")
    else:
        print("\nSome tests failed")


if __name__ == "__main__":
    main()
