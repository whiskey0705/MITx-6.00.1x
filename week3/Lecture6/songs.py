she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

def lyrics2frequencies(lyrics):
    """
    将歌词转换为词：词频，以字典的形式输出
    lyrics的格式为列表
    """
    # 初始化空字典
    mydict = {}
    for word in lyrics:
        # 如果字典里有这个word+1，没有初始化为0
        mydict[word] = mydict.get(word, 0) + 1
    return mydict

def most_common_words(freqs):
    """
    传入字典（词：词频）
    返回频率最高的词和词频（元组）
    """
    # <class 'dict_values'>
    values = freqs.values()
    # 通过max函数取得最大value
    most = max(values)
    word = []
    for k in freqs.keys():
        if freqs[k] == most:
            word.append(k)
    return (word, most)

def words_often(freqs, min_times):
    """
    接收一个字典和最小词频数
    返回过滤后的词和词频（列表）
    """
    often_words = []
    flag = True
    while flag:
        # 临时的最大词：词频
        temp = most_common_words(freqs)
        # 只要词频大于临界值， 就把temp加到空数组里
        if temp[1] >= min_times:
            often_words.append(temp)
            # 然后根据temp的第一个参数‘词’，从字典里删除这个键
            for k in temp[0]:
                # 这里的k是list里的值，也就是字符串，不可变元素
                print(type(k))
                del freqs[k]
        else:
            flag = False
    return often_words
    
    
battle = lyrics2frequencies(she_loves_you)
#most_common_words(battle)

print(words_often(battle, 5))





