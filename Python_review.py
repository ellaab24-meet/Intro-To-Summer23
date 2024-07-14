import random 
temperatures = []
good_days_counter=0
days_of_the_week=["Sunday","Monday", "Tuesday", "Wendseday", "Thursday", "Friday", "Saturday"]
even_days=[]
odd_days = []
highest_temp = 0
highest_temp_day = ''
lowest_temp = 88
avg_temp = []

for i in range(7):
	temperatures.append(random.randint(26,40))
	if temperatures[i] % 2== 0:	
		good_days_counter=good_days_counter+1
		even_days.append(days_of_the_week[i])
	else: 
		odd_days.append(days_of_the_week[i])


print(temperatures)

for i in range(len(temperatures)):
	print (i)
	if highest_temp < temperatures[i]:
		print(highest_temp)
		highest_temp = temperatures [i]
		highest_temp_day = days_of_the_week[i]
	else: 
		print(temperatures[i])
	if lowest_temp > temperatures[i]:
		print(lowest_temp)
		lowest_temp = temperatures [i]
		lowest_temp_day = days_of_the_week [i]
	else: 
		print(temperatures[i])

print ("highest temp = " , highest_temp)
print ("highest temp day = " , highest_temp_day)
print ("lowest temp = " , lowest_temp)
print ("lowest temp day = " , lowest_temp_day)

print (even_days)
print (good_days_counter)

for i in range(7):
	avg_temp = sum(temperatures) / 7

print("the average temperature is = " , avg_temp)

