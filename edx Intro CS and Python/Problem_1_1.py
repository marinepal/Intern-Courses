# Assuming s is a string of lower case characters,
# this program counts up the number of vowels contained in the string s.
# s will be defined below to avoid unresolved reference errors
s = "azcbobobegghakl"  # the answer to this test case is 5
vowels = ['a', 'e', 'i', 'o', 'u']
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)
