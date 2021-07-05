#!/usr/bin/env ruby
# Script matches string that starts with h followed by any single character
# ends with n

puts ARGV[0].scan(/^h.n$/).join
