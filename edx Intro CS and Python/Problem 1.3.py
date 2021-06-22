# Assuming s is a string of lower case characters,
# the program prints the longest substring of s in which the letters occur in alphabetical order.
# s will be defined below to avoid unresolved reference errors
s = "azcbobobegghakl"  # the answer to this test case is beggh
start = 0
length = 1
index = 0
while index < len(s) - 1:
    if s[index] <= s[index + 1]:
        temp_start = index
        temp_length = 2
        index += 1
        while index + 1 < len(s) and s[index] <= s[index + 1]:
            temp_length += 1
            index += 1
        if temp_length > length:
            start = temp_start
            length = temp_length
    else:
        index += 1
print("Longest substring in alphabetical order is:", s[start: start + length])
