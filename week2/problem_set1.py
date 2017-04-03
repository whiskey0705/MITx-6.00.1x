def annual_pay(balance, annnual_interest_rate, month_pay_rate):
	"""
	函数接收3个参数，分别是贷款总额， 年利率， 月最低还款比率
	"""
	# 总还款金额
	total_pay = 0
	# 将贷款的年利率转换为月利率
	month_interest_rate = annnual_interest_rate / 12
	# 初始化当前的贷款金额， 等于贷款总额
	pre_balance = balance
	# for循环12个月
	for month in range(1, 13):
		# 最低月还款金额 = 当前的贷款金额 × 月最低还款比率
		mini_month_paid = pre_balance * month_pay_rate
		print(f'month: {month} paid {mini_month_paid}')
		# 未还款金额 = 当前的贷款金额 - 最低月还款金额
		unpaid_balance = pre_balance - mini_month_paid
		# 月利息 = 未还款金额 × 月利率
		interest = unpaid_balance * month_interest_rate
		# 当前贷款金额 = 未还款金额 + 月利息
		pre_balance = unpaid_balance + interest
		# 将每个月的还款额度相加
		total_pay += mini_month_paid
	# 12个月结束后， 当前的贷款金额即剩余还需还款的金额
	remaining_balance = pre_balance
	# round()函数保留2位小数
	print('Remaining balance:', round(remaining_balance, 2))

annual_pay(5000, 0.18, 0.02)