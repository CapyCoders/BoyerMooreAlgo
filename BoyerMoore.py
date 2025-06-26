def BadCharacterTable(p):
    """
    Preprocesses the pattern to create a bad character table.
    The table stores the last occurrence index of each character in the pattern.
    Characters not in the pattern are marked with -1.
    """
    table = [-1] * 256  # Initialize table for all ASCII characters with -1 (not found)
    for i in range(len(p)):
        table[ord(p[i])] = i  # Update with the rightmost occurrence of each character
    return table

def BoyerMooreAlgo(txt, patt):
    """
    Implements the Boyer-Moore string search algorithm using the bad character heuristic.
    Returns a list of starting indices where the pattern is found in the text.
    """
    # Preprocess the pattern to create bad character lookup table
    badChar = BadCharacterTable(patt)
    lengthText = len(txt)
    lengthPattern = len(patt)
    shift = 0  # Current alignment position in text
    occurrences = []  # Stores matching positions

    # Print search parameters
    print(f"\nText:    {txt}")
    print(f"Pattern: {patt}\n")
    print("Shift | Comparison Position | Action")

    # Main search loop
    while shift <= lengthText - lengthPattern:
        print("-" * 40)
        print(f"{shift:5} | {shift} to {shift + lengthPattern - 1}", end=" | ")
        
        RighttoLeft = lengthPattern - 1  # Start comparing from end of pattern

        # Compare pattern to text from right to left
        while RighttoLeft >= 0 and patt[RighttoLeft] == txt[shift + RighttoLeft]:
            RighttoLeft -= 1  # Move left while characters match

        # Check if entire pattern matched
        if RighttoLeft < 0:
            print(f"Pattern found at position {shift}")
            occurrences.append(shift)
            
            # Calculate shift for next potential match
            if shift + lengthPattern < lengthText:
                next_char = txt[shift + lengthPattern]
                bc_shift = lengthPattern - badChar[ord(next_char)]
                shift += max(1, bc_shift)  # Ensure at least 1 position shift
                print(f"       | Bad character '{next_char}' suggests shift of {bc_shift}")
            else:
                shift += 1  # Reached end of text
        else:
            # Handle mismatch case
            mismatch_char = txt[shift + RighttoLeft]
            # Calculate shift using bad character rule
            bc_shift = max(1, RighttoLeft - badChar[ord(mismatch_char)])
            print(f"Mismatch at pos {shift + RighttoLeft} (char '{mismatch_char}'), shifting by {bc_shift}")
            shift += bc_shift

    return occurrences

# Get user input and run search
text = input("Enter text: ")
pattern = input("Enter pattern: ")
occurrences = BoyerMooreAlgo(text, pattern)

# Print final results
if not occurrences:
    print("\nPattern not found in text")
else:
    print(f"\nPattern found at positions: {occurrences}")
