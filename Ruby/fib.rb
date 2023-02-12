require 'benchmark'

def fib(n)
  return 0 if n == 0 || n == 1
  p, q = 0, 1
  if n > 0
    (n-1).times do
      p, q = q, p+q
    end
    return q
  else
    (-1-n).times do
      p, q = q-p, p
    end
    return q - p
  end
end

print "Enter the lower range of the Fibonacci series: "
lo = gets.chomp.to_i
print "Enter the higher range of the Fibonacci series: "
hi = gets.chomp.to_i

time = Benchmark.realtime do
  for i in lo..hi
    puts "#{i}: #{fib(i)}"
  end
end

puts time
