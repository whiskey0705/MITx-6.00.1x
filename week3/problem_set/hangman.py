import random, string


def load_words():
	"""
	读取txt文档里的词，存入list里
	"""
	print('Loading word list from file...')
	with open('words.txt') as f:
		words = f.read().split()
	print(f'{len(words)} words loaded.')
	return words # return语句后面的内容就不执行了


def choice_word(wordlist):
	"""
	随机从wordlist里选择一个词
	"""
	return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
	"""
	secret_word: string, 随机生成的要猜的词
	letters_guessed: list, 到目前为止已经猜过的字母
	return: boolean, 如果构成secret_word的全部字母可以在letters_guessed里
			找到，说明猜对了，返回True, 否则返回False
	"""
	# set.issubset(iterable) 如果set是iterable的子集，返回True
	return set(secret_word).issubset(letters_guessed)


def get_guessed_word(secret_word, letters_guessed):
	"""
	secret_word: string, 随机生成的要猜的词
	letters_guessed: list, 到目前为止已经猜过的字母
	return: string， 返回secret_word的一个副本，猜中了的字母正常显示，
			没猜中的字母以下划线显示
	"""
	# 这个副本是由"_ "乘以secret_word长度，再去掉末尾的空格组成
	secret_word_copy = (len(secret_word) * '_ ')[:-1]
	# 以空格分隔符，返回一个和secret_word一一对应的数组(方便后续替换字母)
	secret_word_copy_list = secret_word_copy.split(' ')
	
	# 循环遍历letters_guessed中的每一个字母
	for lt in letters_guessed:
		# 如果这个字母也在secret_word中, 就开始把copy_list中的下划线替换成对应的字母
		if lt in secret_word:
			# 初始化.find()方法的索引位置，如果找不到返回-1
			start = 0
			# 循环遍历，因为find()找到1个就会停止，但有可能会有重叠的字母比如PPP
			while True:
				index = secret_word.find(lt, start)
				if index != -1:
					# 因为copy_list的下标和secret_word是一致的，所以只要找到就替换
					secret_word_copy_list[index] = lt
					# 然后重置下索引的位置为当前位置+1
					start = index + 1
				# 如果没了就退出循环
				else:
					break
	# 这时的copy_list应该是一个和secret_word长度一致，部分下划线已经替换为字母
	# 通过1个空格join(), 再把list变回string
	guessed_word = ' '.join(secret_word_copy_list)
	# 返回guessed_word字符串
	return guessed_word


def get_remaining_letters(letters_guessed):
	"""
	letters_guessed: list, 到目前为止已经猜过的字母
	alpha: string, 26个小写字母按顺序排列的字符串
	return: string, 剩余还没猜过的字母组成的字符串
	"""
	# 生成一个由26个小写字母按升序组成的字符串
	alpha = string.ascii_lowercase
	# 转换为list， 方便替换
	alpha_list = list(alpha)
	
	# 循环遍历letters_guessed
	for lt in letters_guessed:
		# 如果该字母在alpha_list里，就移除
		if lt in alpha_list:
			alpha_list.remove(lt)
	# 把列表重新组合为string, 并返回
	remaining_letters = ''.join(alpha_list)
	return remaining_letters




def hangman(secret_word, times):
	"""
	secret_word: string, 随机生成的要猜的词
	times: int, 允许竞猜的次数

	* At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

	"""
	# 初始化letters_guessed为空，后续只要用户输入一次就把结果加进去
	letters_guessed = []
	# 初始化胜利的条件， 结果是一个Boolean值
	success = is_word_guessed(secret_word, letters_guessed)
	# 初始化竞猜次数
	guess_num = times
	# 初始化guessed_word
	guessed_word = get_guessed_word(secret_word, letters_guessed)
	# 初始化剩余字母
	remaining_letters = get_remaining_letters(letters_guessed)
	# 设置循环条件，只要竞猜次数大于0就可以继续游戏
	
	while guess_num > 0:
		print(f'You have {guess_num} guesses left.')
		print(f'Available letters: {remaining_letters}')
        # 把用户竞猜的字母转换为小写存入变量guess
		guess = input('Please guess a letter: ').lower()
        # 把guess添加到letters_guessed
		letters_guessed.append(guess)
        # 如果成功了，打印恭喜跳出循环
		if success:
			print('Congratulations, you won!')
			break
    	# 如果guess在secret_word里，这里分两种情况，一种是猜过，一种是没猜过
		elif guess in secret_word:
			if guess in remaining_letters:
        		# 更新remaining_letters，也就是把这个字母删掉
				remaining_letters = get_remaining_letters(letters_guessed)
				# 更新guessed_word
				guessed_word = get_guessed_word(secret_word, letters_guessed)
				print(f'Good guess: {guessed_word}')
				print('-' * 30)
    		# 如果该字母不在remaining_letters里，说明之前猜过
			else:
				print(f'Oops! You\'ve already guessed that letter: {guessed_word}')
				print('-' * 30)
        # 说明猜错了，这里分两种情况，第一次猜错，扣一次竞猜次数，同一的错误算一次，不扣次数
		elif guess not in secret_word:
			if guess in remaining_letters:
				guess_num -= 1
				remaining_letters = get_remaining_letters(letters_guessed)
				guessed_word = get_guessed_word(secret_word, letters_guessed)
				print(f'Oops! That letter is not in my word: {guessed_word}')
				print('-' * 30)
			else:
				print(f'Oops! You\'ve already guessed that letter: {guessed_word}')
				print('-' * 30)
    # 如果走到这一步，说明竞猜次数用完了，也就是输了
	print(f'Sorry, you ran out of guesses. The word is {secret_word}')

def start():
	"""
	初始化词组list
	初始化随机生成的secret_word
	打印基础信息
	"""
	wordlist = load_words()
	secret_word = choice_word(wordlist).lower() # 将要精彩的单词转化为小写
	print('Welcome to the game, Hangman!')
	print(f'I am thinking of a word that is {len(secret_word)} letters long.')
	print('-' * 30)
	hangman(secret_word, 8)


start()