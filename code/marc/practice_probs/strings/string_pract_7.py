# Convert input strings to lowercase without any surrounding whitespace.

# lower_case("SUPER!") → 'super!'
# lower_case("        NANNANANANA BATMAN        ") → 'nannananana batman'

def strip_white_lower (string):
    stripped = string.lower().strip()
    return stripped
print(strip_white_lower("   MONKEY MAN "))