def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)
    return matches

if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    print("Text:", text)
    print("Pattern:", pattern)
    print("Pattern found at indices:", naive_string_match(text, pattern))
