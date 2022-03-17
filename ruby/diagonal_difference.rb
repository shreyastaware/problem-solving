#!/bin/ruby

n = gets.strip.to_i
a = Array.new(n)
(0..n-1).each do |i|
    a[i] = gets.strip.split(' ').map(&:to_i)
end

d1 = 0
d2 = 0
(0..n-1).each do |i|
    d1 = d1 + a[i][i]
    d2 = d2 + a[-i-1][i]
end

print (d1-d2).abs
