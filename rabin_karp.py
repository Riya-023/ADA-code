def RabinKarpstringMatch(text, pattern, prime):

    n= len(text)
    m=len(pattern)
    p=0
    t=0
    h=1
    d=256
    matches = []

    for i in range(m-1):
        h=(h*d) % prime

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime
    
    for i in range(n-m+1):
        if p==t:
            match = True
            for j in range(m):
                if text[i+j]!= pattern[j]:
                    match = False
                    break

            if match:
                matches.append(i)

        if i< n-m:
            t =(d * (t - ord(text[i]) * h ) + ord(text[i+m])) % prime
            if t < 0:
                t += prime
    
    return matches

text ="BBXXASDFGHIUYASDSDCVHJ"
pattern="ASD"
prime = 101
matches = RabinKarpstringMatch(text, pattern , prime)
print("Matches found at positions : " , matches)
