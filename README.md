# UFineBench
<div align="center"><img src="assets/UFinebench.png" width="900"></div>

**UFineBench** is a new benchmark towards ultra-fine-grained text-based person retrieval. It mainly contains a new manually annotated fine-grained dataset **UFine6926**, a special evaluation set **UFine3C**, a new metric named mSD and a new algorithm CFAM. More details can be found at our paper [UFineBench: Towards Text-based Person Retrieval with Ultra-fine Granularity](https://arxiv.org/abs/2312.03441).

## News
* 🔥[12.7] The paper is released. The UFine6926 and UFine3C will be released in a few days.
  
## UFine6926
UFine6926 is the first **manually annotated** high-quality dataset with ultra-fine granularity for text-based person retrieval. It contains 26,206 images and 52,412 textual descriptions of 6,926 persons totally. The average word count per textual description is 80.8, which is **three to four times** that of previous datasets. The word count distribution and some examples of UFine6926 are shown below.

<div align="center"><img src="assets/UFine6926.png" width="1000"></div>

Annotation format:
```
{
  "split": "train",
  "id": 1,
  "file_path": "images/1.jpg",
  "captions": [
    "A middle-aged woman with a moderate build, her brown hair falls below her shoulders. She is dressed in a white jacket and a pair of dark blue, ankle-length tight pants. She wears a pair of black sandals without socks and carries a camouflage backpack with a black label, which bears some letters, slung over her shoulder. The backpack has two layers. She walks forward, her gait confident and purposeful, on a bustling street.",
    "A middle-aged woman with a medium-built body had brown hair, which exceeded her shoulders, and was wearing a white long-sleeved jacket and a pair of dak blue tight-fitting jeans. The length of the jeans reached her ankles, and she was also wearing a pair of dark brown sandals, without socks. She was carrying a camouflage backpack on her back, with a black label on it. It seemed that there were some letters on the black label."
        ]
}
```

## UFine3C
UFine3C is a special **evaluation** set with cross domains, cross textual granularity and cross textual styles. It is more representative of the huge variations in real scenarios and can be utilized to better evaluate the model's performance in practical applications. It contains 7,446 images, 37,939 text queries of 2,250 persons totally. The word count distribution and some examples of UFine3C are shown below.




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
