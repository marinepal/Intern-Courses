# Assuming s is a string of lower case characters,
# this program prints the number of times the string 'bob' occurs in s.
# s will be defined below to avoid unresolved reference errors
s = "azcbobobegghakl"  # the answer to this test case is 2
count = sum(s[index:index + 3] == 'bob' for index in range(len(s) - 2))
print("Number of times bob occurs is:", count)
