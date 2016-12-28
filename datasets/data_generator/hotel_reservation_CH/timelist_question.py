# -*- coding: utf8 -*-
import jieba
__author__ = 'shin & jacoxu'

timelist_question_female = []
timelist_question_female.append('请问女士您什么时间入住？')
timelist_question_female.append('小姐，您需要预定哪天的宾馆？')
timelist_question_female.append('小姐，请告诉我您预计的入住时间是？')
timelist_question_female.append('请问女士您的入住时间是？')
timelist_question_female.append('请告知您的入住时间，女士')
timelist_question_female.append('小姐，您什么时候入住？')
timelist_question_female.append('小姐，您要订哪天的宾馆？')
timelist_question_female.append('小姐，您要订什么时候的房间？')
timelist_question_female.append('女士，您想订什么时候？')
timelist_question_female.append('女士，您什么时候入住？')
timelist_question_female.append('小姐，何时入住？')
timelist_question_female.append('小姐，什么时候的？')
timelist_question_female.append('女士，什么时间的？')
timelist_question_female.append('好的女士，请提供入住时间。')
timelist_question_female.append('小姐，时间是？')
timelist_question_female.append('小姐，几号的？')
timelist_question_female.append('女士，您需要什么时候入住？')
timelist_question_female.append('说一下您的入住时间，谢谢女士。')

timelist_question_male = []
timelist_question_male.append('请问先生您什么时间入住？')
timelist_question_male.append('先生，您需要预定哪天的宾馆？')
timelist_question_male.append('先生，请告诉我您预计的入住时间是？')
timelist_question_male.append('请问先生您的入住时间是？')
timelist_question_male.append('请告知您的入住时间，先生')
timelist_question_male.append('先生，您什么时候入住？')
timelist_question_male.append('先生，您要订哪天的宾馆？')
timelist_question_male.append('先生，您要订什么时候的房间？')
timelist_question_male.append('先生，您想订什么时候？')
timelist_question_male.append('先生，您什么时候入住？')
timelist_question_male.append('先生，何时入住？')
timelist_question_male.append('先生，什么时候的？')
timelist_question_male.append('先生，什么时间的？')
timelist_question_male.append('好的先生，请提供入住时间。')
timelist_question_male.append('先生，时间是？')
timelist_question_male.append('先生，几号的？')
timelist_question_male.append('先生，您需要什么时候入住？')
timelist_question_male.append('说一下您的入住时间，谢谢先生。')

timelist_question_unisex = []
timelist_question_unisex.append('请问您需要预订什么时间的房间？')
timelist_question_unisex.append('您需要预定哪个时间的房间？')
timelist_question_unisex.append('请告诉我您预计的入住时间是？')
timelist_question_unisex.append('请问您的入住时间是？')
timelist_question_unisex.append('请告知您的入住时间。')
timelist_question_unisex.append('您什么时候入住？')
timelist_question_unisex.append('您要订哪天的房间？')
timelist_question_unisex.append('您要订什么时候的房间？')
timelist_question_unisex.append('您想订什么时候？')
timelist_question_unisex.append('您什么时候住？')
timelist_question_unisex.append('何时入住？')
timelist_question_unisex.append('什么时候的？')
timelist_question_unisex.append('什么时间的？')
timelist_question_unisex.append('好的，请提供入住时间。')
timelist_question_unisex.append('时间是？')
timelist_question_unisex.append('几号的？')
timelist_question_unisex.append('您需要什么时候住？')
timelist_question_unisex.append('说一下您的入住时间，谢谢。')

timelist_question_female_split = []
for ans in timelist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_female_split.append(w_sent)

timelist_question_male_split = []
for ans in timelist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_male_split.append(w_sent)

timelist_question_unisex_split = []
for ans in timelist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_unisex_split.append(w_sent)

timelist_question_female_split += timelist_question_unisex_split
timelist_question_male_split += timelist_question_unisex_split
pass
