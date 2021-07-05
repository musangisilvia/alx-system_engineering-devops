#!/usr/bin/env ruby
# Script outputs: [SENDER], [RECEIVER], [FLAGS]
# Sender phone number or name
# receiver phone number or name
# flags used

puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(',')
