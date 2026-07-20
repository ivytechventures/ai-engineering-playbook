def appeartwice(s): 
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1 
        
        if freq[ch] == 2:
            return ch
    return None

s = "abccbaacz"
print(appeartwice(s)) #output is c