linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))
# print(sortedes)  # ['c', 'js', 'java', 'python', 'csharp']

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# print(sortedes)  # ['csharp', 'python', 'java', 'js', 'c']

print(linguagens)  # ['python', 'js', 'c', 'java', 'csharp']