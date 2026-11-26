"""The Worst Pizza Topping -- make.fun one-liner entry.

The line pitches a topping that has no business on a pizza: gummy
bears, melted straight into the cheese. The joke turns on the sales
voice colliding with the reality of the topping -- it is presented
like a premium feature, but every promised benefit is actually a
defect: the slice stretches, it squeaks, and it glues itself to
your teeth for a week. The humour lands in a single vivid beat, it
could only be about this topping (cheese, stretch, squeak, stuck
teeth), and the pitch sounds like something a shameless pizzeria
would actually say out loud.

The line avoids the tired pineapple debate entirely and picks a
topping nobody asked for, which is what makes it the worst: candy
that was designed to be chewy, now fused with hot cheese, so the
pizza fights back every time you try to eat it.
"""

import os

# The entry: a sales pitch for the worst pizza topping ever -- gummy
# bears melted into the cheese. The stretch, the squeak and the
# week-long tooth glue are all sold as features, which is exactly
# why the topping is terrible.
LINE = "Our new topping: gummy bears melted into the cheese, so every slice stretches, squeaks, and sticks to your teeth for a week."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()


