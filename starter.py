import pickle

train = []
for i in range(10):
    f = open('train/balanced_0{}.pkl'.format(i), 'rb')
    train += pickle.load(f)
    f.close()

f = open('valid/balanced.pkl', 'rb')
valid = pickle.load(f)
f.close()

f = open('test/balanced.pkl', 'rb')
test = pickle.load(f)
f.close()

