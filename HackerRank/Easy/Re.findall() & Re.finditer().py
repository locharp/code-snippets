import re

vowels = "AEIOUaeiou"
pattern = f"[^{vowels}]([{vowels}]{{2,}})[^{vowels}]"

for item in re.findall( pattern, input() ):
    print( item )
