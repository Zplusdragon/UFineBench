# UFineBench
**UFineBench** is a new benchmark towards ultra-fine-grained text-based person retrieval. It mainly contains a new manually annotated fine-grained dataset **UFine6926**, a special evaluation set **UFine3C**, a new metric named mSD and a new algorithm CFAM. More details can be found at our paper [UFineBench: Towards Text-based Person Retrieval with Ultra-fine Granualrity](https://arxiv.org/abs/2312.03441).

## News
* 🔥[12.7] The paper is released. The UFine6926 and UFine3C will be released in a few days.
  
## UFine6926
UFine6926 is the first manually annotated high-quality dataset with ultra-fine granularity for text-based person retrieval. It contains 26,206 images and 52,412 textual descriptions of 6,926 persons totally. The average word count per textual description is 80.8, which is three to four times that of previous datasets.

## UFine3C
UFine3C is a special evaluation set with cross domains, cross textual granularity and cross textual styles. It is more representative of the huge variations in real scenarios and can be utilized to better evaluate the model's performance in practical applications. It contains 7,446 images, 37,939 text queris of 2,250 persons totally. 

## Reference
If you use this work in your research, please cite it by the following BibTeX entry:
```
@misc{zuo2023ufinebench,
      title={UFineBench: Towards Text-based Person Retrieval with Ultra-fine Granularity}, 
      author={Jialong Zuo and Hanyu Zhou and Ying Nie and Feng Zhang and Tianyu Guo and Nong Sang and Yunhe Wang and Changxin Gao},
      year={2023},
      eprint={2312.03441},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
