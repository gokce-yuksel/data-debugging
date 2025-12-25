# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    first = first_name.capitalize() if first_name else ""
    last = last_name.capitalize() if last_name else ""
    return " ".join(part for part in [first, last] if part)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # => ['hello.py']
        print(f'Hello{full_name("", "")}!')
    elif len(sys.argv) == 2:
        # => ['hello.py', 'John' ]
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # => ['hello.py', 'John', 'Lennon']
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
