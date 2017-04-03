# 利用http://pythontutor.com可视化工具

def fixed_month_pay(balance, annnual_interest_rate):
	"""
	函数接收2个参数，分别是贷款总额， 年利率
	"""
	
	# 将贷款的年利率转换为月利率
	month_interest_rate = annnual_interest_rate / 12
	# 为while循环设置一个旗帜为True，如果满足条件则把旗帜变为False，退出循环
	flag = True
	# 设置精确度
	epsilon = 0.01
	# 假设不产生利息，那么每个月还款额为贷款总额/12
	low = balance / 12
	# 假设每个月没有还款，根据复利公式计算一年后贷款总额和利息总额
	# 再除以12得到每个月应还款的额度
	high = (balance * (1 + month_interest_rate)**12) / 12
	# 用2分法确定月还款额
	fixed_month_paid = (low + high) / 2
	# 统计运行的次数
	count = 0
                
                    
	# 开始while循环
	while flag:

		pre_balance = balance

		for month in range(1, 13):	
			count += 1
			unpaid_balance = pre_balance - fixed_month_paid
			interest = unpaid_balance * month_interest_rate
			pre_balance = unpaid_balance + interest
			print(f'month: {month}, low: {low}, high: {high}, interest: {interest}, pre_balance: {pre_balance}')

		# 精确度达标， 退出循环
		if abs(pre_balance) < epsilon:
			flag = False
		# 如果当前额度大于0， 说明月还款额太低，设置low=fixed_month_paid			
		elif pre_balance > 0:
			low = fixed_month_paid
		# 如果当前额度小于0， 说明月还款额太高，设置high=fixed_month_paid
		elif pre_balance < 0:
			high = fixed_month_paid
		# 根据上面新的low和high，重新制定fixed_month_paid
		fixed_month_paid = (low + high) / 2

	print(f'月还款额为：{round(fixed_month_paid, 2)}, 运行了：{count}次')

fixed_month_pay(5000, 0.18)