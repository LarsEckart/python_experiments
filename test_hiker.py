import pytest


def test_empty_string_throws_exception():
    with pytest.raises(TypeError):
        assert isBalanced() == True


def test_one_pair_of_parentheses_is_balanced():
    assert isBalanced("()") == True


def test_reversed_pair_of_parentheses_is_unbalanced():
    assert isBalanced(")(") == False


def test_uneven_number_of_parentheses_is_unbalanced():
    assert isBalanced("(()") == False


def test_pair_of_parentheses_with_additional_closing_parentheses_is_unbalanced():
    assert isBalanced("()))") == False


def test_reversed_parentheses_after_pair_of_parentheses_is_unbalanced():
    assert isBalanced("())(") == False


def test_reversed_brackets_are_unbalanced():
    assert isBalanced('][') == False


def test_unmatched_brackets_inside_parentheses_are_unbalanced():
    assert isBalanced('([)]') == False


def test_unmatched_parentheses_inside_brackets_are_unbalanced():
    assert isBalanced('[(])') == False


def test_reversed_braces_are_unbalanced():
    assert isBalanced('}{') == False


def isBalanced(input):
    if len(input) % 2 == 1:
        return False

    count = 0
    countBrackets = 0
    for c in input:
        if c == "(":
            count = count + 1
        if c == ")":
            if countBrackets != 0:
                return False
            count = count - 1
        if c == "[":
            countBrackets = countBrackets + 1
        if c == "]":
            if count != 0:
                return False
            countBrackets = countBrackets - 1

        if countBrackets < 0 or count < 0:
            return False

    return count == 0
