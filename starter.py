import pickle

f = open('train/balanced.pkl', 'rb')
train_balanced = pickle.load(f)
f.close()

f = open('train/40k.pkl', 'rb')
train_40k = pickle.load(f)
f.close()

f = open('train/100k.pkl', 'rb')
train_100k = pickle.load(f)
f.close()

f = open('valid/balanced.pkl', 'rb')
valid = pickle.load(f)
f.close()

f = open('test/balanced.pkl', 'rb')
test = pickle.load(f)
f.close()
