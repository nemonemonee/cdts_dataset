#  Cross Domain Text Summarization Dataset

## 1. Introduction

Currently, the majority of advanced pre-trained language models excel in downstream Natural Language Processing (NLP) tasks when fine-tuned on specific datasets. However, these models exhibit proficiency only within their designated domains. Even performing on the same task such as text summarization, the performance are affected by slight variations in the domain. Consequently, we propose a novel cross-domain text summarization dataset that encompasses various domains, including news with headlines, dialogue with summaries, scientific papers with abstracts, and legislature bills with summaries. In Section 3, we will elaborate on the selection of datasets and the sampling strategies employed.

### 1.1 Graphs
#### 1.1.1 Histagrams of the tokenized sequence length
<img src="https://github.com/nemonemonee/cdts_dataset/assets/88709397/8d90e337-c3f6-4e9a-b1ef-d62b5c8a5c3a)" width="400" />

<img src="https://github.com/nemonemonee/cdts_dataset/assets/88709397/00285bac-ca67-4666-9198-cecdd6c3b326)" width="400" />

### 1.1.2 Histagrams of the truncated tokenized sequence length
<img src="https://github.com/nemonemonee/cdts_dataset/assets/88709397/1a09280b-1e52-4a06-b03f-6b28ddbb6ef2)" width="400" />

<img src="https://github.com/nemonemonee/cdts_dataset/assets/88709397/78bc76df-9678-40b9-bd4e-86b862e63997)" width="400" />


## 2. Implementation
### 2.1 How to load this dataset?
```
python starter.py
```
### 2.2 How to reproduce this dataset?
#### 2.2.1 Pre-requisite
```
pip install datasets py7zr
```
#### 2.2.2
```
python generate_dataset.py
```
## 3. Datasets


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
