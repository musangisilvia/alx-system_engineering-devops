#!/usr/bin/env ruby
# Script matches only uppercase letters in string

puts ARGV[0].scan(/[A-Z]+/).join
