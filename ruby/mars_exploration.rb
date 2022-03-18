#!/bin/ruby

S = gets.strip
n = S.size/3
exp = "SOS" * n 
ans = 0
(0..S.size-1).each do |i|
    if exp[i] != S[i]
        ans = ans + 1
    end
end
print ans