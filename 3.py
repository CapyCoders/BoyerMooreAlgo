def BadCharacterTable(p):
    """Create bad character table."""
    table = [-1] * 256  # Initialize all characters with -1 (not found)
    for i in range(len(p)):
        table[ord(p[i])] = i  # Update with the rightmost occurrence
    return table

def BoyerMooreAlgo(txt, patt):
    badChar = BadCharacterTable(patt)
    lengthText = len(txt)
    lengthPattern = len(patt)
    shift = 0
    occurrences = []

    print(f"\nText:    {txt}")
    print(f"Pattern: {patt}\n")
    print("Shift | Comparison Position | Action")

    while shift <= lengthText - lengthPattern:
        print("-" * 40)
        print(f"{shift:5} | {shift} to {shift + lengthPattern - 1}", end=" | ")
        
        RighttoLeft = lengthPattern - 1

        # Inner loop for pattern matching from right to left
        while RighttoLeft >= 0 and patt[RighttoLeft] == txt[shift + RighttoLeft]:
            RighttoLeft -= 1

        # If pattern found
        if RighttoLeft < 0:
            print(f"Pattern found at position {shift}")
            occurrences.append(shift)
            # Calculate next shift using bad character rule
            if shift + lengthPattern < lengthText:
                next_char = txt[shift + lengthPattern]
                bc_shift = lengthPattern - badChar[ord(next_char)]
                shift += max(1, bc_shift)
                print(f"       | Bad character '{next_char}' suggests shift of {bc_shift}")
            else:
                shift += 1
        else:
            # Calculate shift using bad character rule
            mismatch_char = txt[shift + RighttoLeft]
            bc_shift = max(1, RighttoLeft - badChar[ord(mismatch_char)])
            print(f"Mismatch at pos {shift + RighttoLeft} (char '{mismatch_char}'), shifting by {bc_shift}")
            shift += bc_shift

    return occurrences

text = input("Enter text: ")
pattern = input("Enter pattern: ")
occurrences = BoyerMooreAlgo(text, pattern)

if not occurrences:
    print("\nPattern not found in text")
else:
    print(f"\nPattern found at positions: {occurrences}")