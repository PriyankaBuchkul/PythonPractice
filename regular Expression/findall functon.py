import re
ex_str="""Jessica is 15 years old ,and  Danial is 27 years old.\n Edward is 97
        years old, and his grandfather,Oscar ,is 102."""
age=re.findall(r'\d[0-9]*',ex_str)
name=re.findall(r'[A-Z][a-z]*',ex_str)

print("Ages Are:",age)
print("Names Are:",name)
