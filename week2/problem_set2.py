# 利用http://pythontutor.com可视化工具

def fixed_month_pay(balance, annnual_interest_rate):
	"""
	函数接收2个参数，分别是贷款总额， 年利率
	"""
	
	# 将贷款的年利率转换为月利率
	month_interest_rate = annnual_interest_rate / 12
	# 为while循环设置一个旗帜为True，如果满足条件则把旗帜变为False，退出循环
	flag = True
	# 初始化每月固定还款额为10
	fixed_month_paid = 10
	count = 0
	# 开始while循环
	while flag:
		# 初始化当前贷款额度为贷款总额，确保每次for循环开始时pre_balance值为贷款总额
		pre_balance = balance
		# 进入一年的还款阶段，按照公式计算各个数值	
		for month in range(1, 13):
			count += 1	
			# 未还款金额 = 当前的贷款金额 - 固定月还款金额
			unpaid_balance = pre_balance - fixed_month_paid
			# 月利息 = 未还款金额 × 月利率
			interest = unpaid_balance * month_interest_rate
			# 当前贷款金额 = 未还款金额 + 月利息
			pre_balance = unpaid_balance + interest
			print(f'month: {month}, unpaid: {unpaid_balance}, interest: {interest}, pre_balance: {pre_balance}')
		# for循环结束后，判断pre_balance的值，如果小于0，说明已经还款完成
		# 改变flag的值，退出while循环
		if pre_balance < 0:
			flag = False
		# 如果pre_balance依然大于0， 则每月固定还款金额加10
		else:
			fixed_month_paid += 10

	print(f'月还款额为：{fixed_month_paid}, 运行了：{count}次')

fixed_month_pay(5000, 0.18)