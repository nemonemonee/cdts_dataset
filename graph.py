import pickle
import matplotlib.pyplot as plt
import numpy as np
train = []
for i in range(10):
    f = open('train/balanced_0{}.pkl'.format(i), 'rb')
    train += pickle.load(f)
    f.close()

train_txt, train_sum = list(zip(*train))
train_txt, train_sum = list(train_txt), list(train_sum)


#train_txt_tok, train_sum_tok = [], []
len_txt, len_sum = [], []

for txt in train_txt:
    txt_tok = txt.split(" ")
#    train_txt_tok.append(txt_tok)
#    if  len(txt_tok) > 2048:
#        len_txt.append(2048)
#    else:
    len_txt.append(len(txt_tok))

for sum in train_sum:
    sum_tok = sum.split(" ")
#    if len(sum_tok) > 256:
#        len_sum.append(256)
#    else:
    len_sum.append(len(sum_tok))


n, bins, patches = plt.hist(x=len_txt,bins='auto', color='#0504aa',alpha=0.7,rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Lengths of Text')
plt.ylabel('Frequency')
plt.title('Histogram of length of tokenized text')
plt.xlim([0,8000])
plt.show()

n, bins, patches = plt.hist(x=len_sum,bins='auto', color='#0504aa',alpha=0.7,rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Lengths of Summary')
plt.ylabel('Frequency')
plt.title('Histogram of length of tokenized summary')
plt.xlim([0,600])
plt.show()

