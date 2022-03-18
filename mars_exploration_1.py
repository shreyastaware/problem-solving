"""
This is an easy string problem. Construct the expected string first. It can be done by concatenating SOS  
`n` times where `n = length(s)/3` . Now use a simple loop to count how many characters mismatch. Check the 
problem-setters code for this approach.

If memory is an issue, there is a workaround. The following code uses modulo division against the index in s
to point to the correct character in SOS rather than concatenating the string first.
"""

def marsExploration(s):
    sos = 'SOS'
    n = len(s)
    count = 0
    for i in range(n):
        if not s[i] == sos[i%3]:
            count += 1
    return count
