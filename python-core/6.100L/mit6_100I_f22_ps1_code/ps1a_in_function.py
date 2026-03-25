def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	down_payment_cost = cost_of_dream_home * portion_down_payment
	months = 0
	while (down_payment_cost > amount_saved):
	    amount_saved += amount_saved * r / 12
	    amount_saved += (yearly_salary * portion_saved) / 12
	    months += 1
	print(f"Number of Months: {months}")
	return months