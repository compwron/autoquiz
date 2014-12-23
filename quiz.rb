MAX = 13

def _rand_sym
  a = ['+', '-', '*', '*'] # I want extra multiplication
  a[rand(a.length)]
end

continue = true
wins = 0
tries = 0
start_time = Time.now
while continue
  equation = "#{rand(MAX)} #{_rand_sym} #{rand(MAX)}"
  puts equation
  answer = eval(equation)
  user_says = gets.chomp
  tries += 1
  if user_says == 'done'
  	continue = false
  	end_time = Time.now
  elsif user_says.to_i == answer
    wins += 1
    puts 'Correct!'
  else
    puts "Wrong. Answer is: #{answer}"
  end
end
total_time = end_time - start_time
puts "#{wins} wins / #{tries} tries in #{total_time.round(2)} sec (#{(total_time / tries).round(2)} sec per try)"