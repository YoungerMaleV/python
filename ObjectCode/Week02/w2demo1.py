import sys
import os
import string
import collections

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def load_stoppping_words(filepath):
	sws=[line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
	return set(sws)

def get_terms(filepath,stoppingwords):
	ws=[]
	with open(filepath,'r',encoding='utf-8') as f:
		for line in f:
			for w in jieba.cut(line.strip()):
				if w not in stoppingwords:
					ws.append(w)
	return ws

def get_terms_freq(ws):
	wf={}
	for w in ws:
		if w in wf:
			wf[w]+=1
		else:
			wf[w]=1
	return wf

def get_features(wf,high=100000,low=5):
	features=[]
	for k in wf:
		if wf[k]<=high and wf[k]>=low:
			features.append(k)
	return features

def get_vs_model_weight(wf,features):
	v=[]
	for f in features:
		if f in wf:
			v.append(wf[f])
		else:
			v.append(0)
	return v

def get_vs_model_onehot(wf,features):
	v=[]
	for f in features:
		if f in wf:
			v.append(1)
		else:
			v.append(0)
	return v

def get_topk_terms(wf,topn=10):
	tws=[]
	sorted_dic=collections.OrderedDict(sorted(wf.items(),\
		key=lambda d:d[1],reverse=True))	
	for k in list(sorted_dic.keys())[0:topn]:
		tws.append(k)
	return tws

def draw_cloud(tws,wf):
	freq={}
	for t in tws:
		freq[t]=wf[t]
	wordcloud = WordCloud(font_path='simhei.ttf', max_font_size=40,\
		width=1000,height=700,background_color = 'white').generate_from_frequencies(freq)
	wordcloud.to_file('wc1.png')

def main():
	if len(sys.argv)!=3:
		print("Usage: python w2demo1.py spfile docfile")
	else:
		stoppingwords=load_stoppping_words(sys.argv[1])
		print(len(stoppingwords))
		ws=get_terms(sys.argv[2],stoppingwords)
		print(len(ws))
		wf=get_terms_freq(ws)
		#print(wf)
		print(len(wf))
		features=get_features(wf,high=100000,low=30)
		print(features)
		print(len(features))
		v1=get_vs_model_onehot(wf,features)
		#print(v1)
		v2=get_vs_model_weight(wf,features)
		#print(v2)
		tws=get_topk_terms(wf,100)
		print(tws)
		draw_cloud(tws,wf)

if __name__=='__main__':main()

