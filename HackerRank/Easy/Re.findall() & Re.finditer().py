import re

vowels = "aeiou"
pattern = f"(?<=[^{vowels}])[{vowels}]{{2,}}(?=[^{vowels}])"
matches = re.findall( pattern, input(), re.IGNORECASE )

if len( matches ) > 0:
    for match in matches:
        print( match )
else:
    print( -1 )
