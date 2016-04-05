from collections import Counter
words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]
word_counts = Counter(words) #底层实现为一个dict
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['eyes'])
morewords = ['why','are','you','not','looking','in','my','eyes'] #可通过修改字典手动增加次数
word_counts.update(morewords)
top_three=word_counts.most_common(3)
print(top_three)
#可进行加减直接将次数相加减
word_counts+=word_counts
print(word_counts)