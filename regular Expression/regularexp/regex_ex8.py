##import re
##regex = r"([a-zA-Z]+) (\d+)"
##print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))
import re
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")
if result:
    print(result.start(), result.end())
for result in regex.findall("Hello World, Python World"):
    print(result)

print(regex.sub(r"\1 Earth", "Hello World"))
