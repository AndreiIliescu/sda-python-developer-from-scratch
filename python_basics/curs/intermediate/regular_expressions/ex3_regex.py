import re
# 40123456789
# 40374829383
# +40123456789
# 0040123456789

tests = ["401234567890000", "40374829383", "+40123456789", "0040123456!789"]
pattern = r"(\+|00)?40\d{9}"

for elem in tests:
    result = re.fullmatch(pattern, elem)
    print(elem, result is not None)
