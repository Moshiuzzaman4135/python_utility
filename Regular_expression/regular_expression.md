# Regular Expression

### Cheat Sheet
```
.          Any character except newline
^          Start of string
$          End of string
*          0 or more occurrences of the previous character or group
+          1 or more occurrences of the previous character or group
?          0 or 1 occurrence of the previous character or group
{n}        Exactly n occurrences of the previous character or group
{n,}       At least n occurrences of the previous character or group
{n,m}      Between n and m occurrences of the previous character or group
|          Alternation (either the expression before or after the vertical bar)
[...]      Matches any character inside the brackets (character class)
[^...]     Matches any character not inside the brackets (negated character class)
\d         Any digit (equivalent to [0-9])
\D         Any non-digit character (equivalent to [^0-9])
\w         Any word character (equivalent to [a-zA-Z0-9_])
\W         Any non-word character (equivalent to [^a-zA-Z0-9_])
\s         Any whitespace character (equivalent to [\t\n\r\f\v])
\S         Any non-whitespace character (equivalent to [^\t\n\r\f\v])
\b         Word boundary (matches the empty string at the beginning or end of a word)
\B         Non-word boundary (matches the empty string at any position that is not a word boundary)
(...)     Grouping (creates a capture group)
(?:...)   Non-capturing grouping (does not create a capture group)
\1, \2, ... Backreferences to capture groups (refers to the content of a previously captured group)
```

### Starts with 3 digits
> If the first 3 digits are digits then replace them with blank 
```
import re
text = '014 Contra.nes'
regex_pattern = r'^\d{3}'
text = re.sub(regex_pattern, '', text).strip()
```
Output :
```
Contra.nes
```
### Bracket with substring
> The regular expression that starts and ends with bracket and contains a substring
```
import re

text = '014 Contra (substring).nes'
regex_pattern = r'\([^)]*substring[^)]*\)'
text = re.sub(regex_pattern, '', text).strip()
print(text)
```
Output :
```
014 Contra .nes
```
# Substring in string
```
import re

text = '014 Contra (USA).nes'
regex_pattern = r'\bUSA\b'
text = re.sub(regex_pattern, '', text).strip()
print(text)
```
Output : 
```
014 Contra ().nes
```

### Bracket with substring no space
> The regular expression that starts and ends with bracket and contains a substring
```
import re

text = '014 Contra (USA).nes'
regex_pattern = r'\(\bUSA\b\)'
text = re.sub(regex_pattern, '', text).strip()
print(text)
```
Output :
```
014 Contra .nes
```
> As there is space the regular expression searches for the substring just after the bracket without any space
So if the input is
```
import re

text = '014 Contra (USA).nes'
regex_pattern = r'\(\bUSA\b\)'
text = re.sub(regex_pattern, '', text).strip()
print(text)
```
Output :
```
014 Contra ( USA).nes
```
