s = "9" * 127

while s.count("999") or s.count("333"):
    if s.count("333"):
        s = s.replace("333", "9", 1)
    else:
        s = s.replace("999", "3", 1)

print(s)
