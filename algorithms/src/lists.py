def is_oposite_off(current, last):
    if (last == '[' and current == ']') or (last == '(' and current == ')') or (last == '{' and current == '}'):
        return True
    return False


def is_oppen_brack(current):
    if current in ('[', '(', '{'):
        return True
    return False


# Complete the isBalanced function below.
def is_balanced(s):
    processed = []
    chars = [char for char in s]
    for current in chars:
        processed_len = len(processed)
        last = None if not processed else processed[processed_len - 1]
        if is_oppen_brack(current):
            processed.append(current)
        elif is_oposite_off(current, last):
            processed.pop(processed_len - 1)
        else:
            return "NO"
    if processed:
        return "NO"
    return "YES"


if __name__ == "__main__":
    s = '(}]}'
    pr = is_balanced(s)
    print(f">>>>>{pr}")
