#!/usr/bin/env ruby
# Script matches string that has hb followed by at least 2
# occurences of t (at most 5) then n

puts ARGV[0].scan(/hbt{2,5}n/).join
