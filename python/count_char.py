#!/usr/bin/env python
# -*- coding:utf-8 -*-


read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''

'''
第一步: 统计每个字符出现的次数
'''

char_stat_dict = {}
for _char in read_me:
    char_stat_dict.setdefault(_char,0)
    char_stat_dict[_char] += 1

print '每个字符对应的次数:'
print char_stat_dict


'''
第二步: 字典转成列表 dict=>list
'''

print
print '把字典转成列表:'
char_stat_list = char_stat_dict.items()
print char_stat_list


'''
第三步: list排序,冒泡
1. tuple是可以进行比较的
2. 可以用元组中的某个元素代码元组，和其它元组比较
'''

for j in range(len(char_stat_list) - 1):
    for i in range(len(char_stat_list) - 1):
        if char_stat_list[i][1] > char_stat_list[i + 1][1]:
            #a,b = b,a
            char_stat_list[i],char_stat_list[i + 1] = char_stat_list[i + 1],char_stat_list[i]


