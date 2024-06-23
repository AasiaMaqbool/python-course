import re

pattern = re.compile(r"[A-Za-z0-9@#$%]{8,}\d")
password= 'aasia1234567'
check=pattern.fullmatch(password)
print(check)