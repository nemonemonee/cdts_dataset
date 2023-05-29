#  Cross Domain Text Summarization Dataset

## 1. Introduction

Currently, advanced pre-trained language models have demonstrated their prowess in downstream Natural Language Processing (NLP) tasks by achieving remarkable performance when fine-tuned on specific datasets. However, it is important to note that these models excel primarily within their designated domains. Even when performing the same task, such as text summarization, the model's performance can be influenced by subtle variations in the domain.

To further study this demanding task, we propose a novel and challenging dataset for the NLP field: a cross-domain text summarization dataset. This comprehensive dataset encompasses various domains, including news articles with headlines, dialogues with summaries, scientific papers with abstracts, and legislature bills with summaries. In Section 3, we will delve into the details of the dataset selection process and the sampling strategies employed.

By examining the distribution of tokenized text and summary lengths within our cross-domain dataset. It is evident that the observed distribution significantly deviates from a normal distribution, indicating the presence of considerable complexity. Moreover, the inclusion of diverse domains in the dataset, coupled with the high variance observed in the lengths of tokenized sequences, presents additional challenges.

### 1.1 Graphs
For simple tokenization, we currently employ space separation as our method. We proceed to visualize the tokenized data accordingly. However, for future analysis, it is recommended to utilize a more advanced tokenizer from the transformer package, which can enhance the tokenization process.

#### 1.1.1 Histograms of the tokenized sequence length
<img width="400" src="https://github.com/nemonemonee/cdts_dataset/blob/main/graphs/Figure_1.png"/> <img width="400" src="https://github.com/nemonemonee/cdts_dataset/blob/main/graphs/Figure_2.png"/>


Analyzing the histograms presented above, we observe that the tokenized sequence lengths of both the text and summarization pairs exhibit a significant skew towards the right. It is important to note that the right limit on the x-axis does not represent the maximum sequence length. Rather, it is selected for the purpose of visualization.

#### 1.1.2 Histograms of the truncated tokenized sequence length
<img width="400" src="https://github.com/nemonemonee/cdts_dataset/blob/main/graphs/Figure_3.png"/> <img width="400" src="https://github.com/nemonemonee/cdts_dataset/blob/main/graphs/Figure_4.png"/>

In practical applications, encoder-decoder transformer-based models often require a fixed input length. Therefore, for the second pair of histograms, we opt to truncate  tokenized text and summary sequences at a maximum length of 2048 and 256, respectively. 


## 2. Implementation
### 2.1 How to load this dataset?
```
python starter.py
```
Please review the starter.py file. The saved files can be loaded using pickle, which allows for easy retrieval of the dataset.

### 2.2 How to reproduce this dataset?
#### 2.2.1 Pre-requisite
```
pip install datasets py7zr
```
#### 2.2.2 Reproduction
```
python generate_dataset.py
```

You have the option to modify the random seed in the file, which will generate a dataset of the same size but with different data instances. Additionally, apart from the balanced dataset, the file has the capability to generate a full training set as well as unbalanced datasets with sizes of 40k and 100k instances respectively.

## 3. Datasets and Sampling
### 3.1 Datasets chosen
-  news articles with headlines : CNN and DailyMail
-  dialogues with summaries : Samsum
-  scientific papers with abstracts : Arxiv and Pubmed
-  legislature bills with summaries : BillSum

### 3.2 Sampling method
- balanced: we randomly sampled (10000, 800, 800) entries of the (train, validation, test) set from each of the dataset representing the 4 diverse domains.
- unbalanced: for the train set, we want to also provide the unbalanced options, which include
    - all: all the text and summary pairs from the chosen datasets
    - 40k: randomly sample 40k entries from `all`
    - 100k: randomly sample 100k entries from `all`


The unbalanced datasets is not included in the repo because the size of those file is too large. We do provide the code to generate these unbalanced datasets in `generate_dataset.py`

## 4. Reference
```
@inproceedings{see-etal-2017-get,
    title = "Get To The Point: Summarization with Pointer-Generator Networks",
    author = "See, Abigail  and
      Liu, Peter J.  and
      Manning, Christopher D.",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P17-1099",
    doi = "10.18653/v1/P17-1099",
    pages = "1073--1083",
    abstract = "Neural sequence-to-sequence models have provided a viable new approach for abstractive text summarization (meaning they are not restricted to simply selecting and rearranging passages from the original text). However, these models have two shortcomings: they are liable to reproduce factual details inaccurately, and they tend to repeat themselves. In this work we propose a novel architecture that augments the standard sequence-to-sequence attentional model in two orthogonal ways. First, we use a hybrid pointer-generator network that can copy words from the source text via pointing, which aids accurate reproduction of information, while retaining the ability to produce novel words through the generator. Second, we use coverage to keep track of what has been summarized, which discourages repetition. We apply our model to the CNN / Daily Mail summarization task, outperforming the current abstractive state-of-the-art by at least 2 ROUGE points.",
}
```

```
@inproceedings{DBLP:conf/nips/HermannKGEKSB15,
  author={Karl Moritz Hermann and Tomás Kociský and Edward Grefenstette and Lasse Espeholt and Will Kay and Mustafa Suleyman and Phil Blunsom},
  title={Teaching Machines to Read and Comprehend},
  year={2015},
  cdate={1420070400000},
  pages={1693-1701},
  url={http://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend},
  booktitle={NIPS},
  crossref={conf/nips/2015}
}
```

```
@inproceedings{gliwa-etal-2019-samsum,
    title = "{SAMS}um Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization",
    author = "Gliwa, Bogdan  and
      Mochol, Iwona  and
      Biesek, Maciej  and
      Wawer, Aleksander",
    booktitle = "Proceedings of the 2nd Workshop on New Frontiers in Summarization",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-5409",
    doi = "10.18653/v1/D19-5409",
    pages = "70--79"
}
```

```
@article{Cohan_2018,
   title={A Discourse-Aware Attention Model for Abstractive Summarization of
            Long Documents},
   url={http://dx.doi.org/10.18653/v1/n18-2097},
   DOI={10.18653/v1/n18-2097},
   journal={Proceedings of the 2018 Conference of the North American Chapter of
          the Association for Computational Linguistics: Human Language
          Technologies, Volume 2 (Short Papers)},
   publisher={Association for Computational Linguistics},
   author={Cohan, Arman and Dernoncourt, Franck and Kim, Doo Soon and Bui, Trung and Kim, Seokhwan and Chang, Walter and Goharian, Nazli},
   year={2018}
}
```

```
@misc{kornilova2019billsum,
    title={BillSum: A Corpus for Automatic Summarization of US Legislation},
    author={Anastassia Kornilova and Vlad Eidelman},
    year={2019},
    eprint={1910.00523},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
