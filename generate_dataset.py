from datasets import load_dataset
import random
import pickle

random.seed(0)

def sample_from_dataset(dataset, num):
  return dataset.shuffle()[:num]

cnn_dm = load_dataset('cnn_dailymail', '3.0.0')
samsum = load_dataset('samsum')
arxiv = load_dataset('scientific_papers', 'arxiv')
pubmed = load_dataset('scientific_papers', 'pubmed')
billsum = load_dataset('billsum')

n_train = 10000
n_valid = 800
n_test = 800

cnn_train = sample_from_dataset(cnn_dm['train'], n_train)
sam_train = sample_from_dataset(samsum['train'], n_train)
arx_train = sample_from_dataset(arxiv['train'], n_train // 2)
pub_train = sample_from_dataset(pubmed['train'], n_train // 2)
bill_sample = sample_from_dataset(billsum['train'], n_train + n_valid)
balanced_train_txt = cnn_train['article'] + sam_train['dialogue'] + arx_train['article'] + pub_train['article'] + bill_sample['text'][:n_train]
balanced_train_sum = cnn_train['highlights'] + sam_train['dialogue'] + arx_train['abstract'] + pub_train['abstract'] + bill_sample['summary'][:n_train]

cnn_valid = sample_from_dataset(cnn_dm['validation'], n_valid)
sam_valid = sample_from_dataset(samsum['validation'], n_valid)
arx_valid = sample_from_dataset(arxiv['validation'], n_valid // 2)
pub_valid = sample_from_dataset(pubmed['validation'], n_valid // 2)
balanced_valid_txt = cnn_valid['article'] + sam_valid['dialogue'] + arx_valid['article'] + pub_valid['article'] + bill_sample['text'][n_train:]
balanced_valid_sum = cnn_valid['highlights'] + sam_valid['dialogue'] + arx_valid['abstract'] + pub_valid['abstract'] + bill_sample['summary'][n_train:]

cnn_test = sample_from_dataset(cnn_dm['test'], n_test)
sam_test = sample_from_dataset(samsum['test'], n_test)
arx_test = sample_from_dataset(arxiv['test'], n_test // 2)
pub_test = sample_from_dataset(pubmed['test'], n_test // 2)
bill_test = sample_from_dataset(billsum['test'], n_test)
balanced_test_txt = cnn_test['article'] + sam_test['dialogue'] + arx_test['article'] + pub_test['article'] + bill_test['text']
balanced_test_sum = cnn_test['highlights'] + sam_test['dialogue'] + arx_test['abstract'] + pub_test['abstract'] + bill_test['summary']

f = open('balanced_train.pkl', 'wb')
pickle.dump(list(zip(balanced_train_txt, balanced_train_sum)), f)
f.close()

f = open('balanced_valid.pkl', 'wb')
pickle.dump(list(zip(balanced_valid_txt, balanced_valid_sum)), f)
f.close()

f = open('balanced_test.pkl', 'wb')
pickle.dump(list(zip(balanced_test_txt, balanced_test_sum)), f)
f.close()

all_train_txt = cnn_dm['train']['article'] + samsum['train']['dialogue'] + arxiv['train']['article'] + pubmed['train']['article'] + billsum['train']['text']
all_train_sum = cnn_dm['train']['highlights'] + samsum['train']['dialogue'] + arxiv['train']['abstract'] + pubmed['train']['abstract'] + billsum['train']['summary']

all_train = list(zip(all_train_txt, all_train_sum))

f = open('all_train.pkl', 'wb')
pickle.dump(all_train, f)
f.close()

random.seed(0)
random.shuffle(all_train)
train_40k = all_train[:40000]
random.shuffle(all_train)
train_100k = all_train[:100000]

f = open('40k_train.pkl', 'wb')
pickle.dump(train_40k, f)
f.close()

f = open('100k_train.pkl', 'wb')
pickle.dump(train_100k, f)
f.close()

