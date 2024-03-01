# UFineBench
<div align="center"><img src="assets/UFinebench.png" width="900"></div>

**UFineBench** is a new benchmark towards ultra-fine-grained text-based person retrieval. It mainly contains a new manually annotated fine-grained dataset **UFine6926**, a special evaluation set **UFine3C**, a new metric named mSD and a new algorithm CFAM. More details can be found at our paper [UFineBench: Towards Text-based Person Retrieval with Ultra-fine Granularity](https://arxiv.org/abs/2312.03441).

## News
* 🙂[2024.2.27] Good News! Our paper is accepted by **CVPR2024**.
* 🔥[2023.12.18] The UFine6926 and UFine3C are released. Welcome to download and use!
* 🔥[2023.12.7] The paper is released.

## How to obtain the datasets
Please download and sign the license agreement (UFineBench_License.pdf) and send it to jlongzuo@hust.edu.cn or cgao@hust.edu.cn . Once the procedure is approved, the download link will be sent to your email. Please note that if you are a current student, you should have your supervisor sign it.

## UFine6926
UFine6926 is the first **manually annotated** high-quality dataset with ultra-fine granularity for text-based person retrieval. It contains 26,206 images and 52,412 textual descriptions of 6,926 persons totally. The average word count per textual description is 80.8, which is **three to four times** that of previous datasets. The word count distribution and some examples of UFine6926 are shown below.

<div align="center"><img src="assets/UFine6926.png" width="1000"></div>

Annotation format (each image is annotated with two ultra-fine-grained textual descriptions):
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

<div align="center"><img src="assets/UFine3C.png" width="1000"></div>

Annoatation format (every image has multiple text queries with different textual styles):
```
{
  "id": 2250,
  "source": "UFine6926",
  "split": "test",
  "file_path": "images/7446.jpg",
  "captions": [
    "The young man has wheat-colored skin, average height, and a normal build. His short black hair is styled with a pair of black sunglasses perched on his nose. A dark circle of stubble adorns his chin. He dons a pure cotton short-sleeved T-shirt with white letter patterns imprinted on it, which ends just above his rear. Paired with the shirt is a pair of short light gray sports pants that extend up to his knees. His footwear consists of canvas shoes with black soles and white bases.",
    "This young man has a fit build and stands at an average height. His skin has a warm, golden tone, and his short black hair is styled in a neat, tidy way. He's wearing a pair of sleek black sunglasses that complement his sharp features. A faint shadow of stubble graces his chin, giving him a subtle, rugged look.",
    "This young man has a medium height and a fit physique. His skin is a warm, golden brown color, and his short black hair is styled in a neat, tidy manner. He's wearing a pair of sleek black sunglasses and a well-groomed black beard on his chin. His upper body is clad in a black cotton short-sleeved T-shirt with a crisp white letter pattern, which falls just above his belly button. He's paired this with a pair of light gray sports pants that hit just above his knees, creating a stylish and comfortable look. His feet are clad in a pair of black canvas shoes with white soles, adding a touch of sportiness to his overall appearance.",
    "A fit young man with a medium height and warm, golden brown skin dons a black cotton short-sleeved T-shirt with a crisp white letter pattern that falls just above his belly button, paired with sleek black sunglasses and a well-groomed black beard on his chin. His lower body is covered by light gray sports pants that hit just above his knees, completed with a pair of black canvas shoes with white soles for added sportiness.",
    "This is a young man with wheat-colored skin, average height, and an appropriate build. He has short black hair and wears a pair of black sunglasses. There's a circle of dark stubble on his chin. His upper body is wearing a pure cotton short-sleeved T-shirt with white letter patterns printed on it, and the length of the T-shirt reaches just above his butt. His lower body is wearing a short light gray sports pants that reach just above his knees. On his feet, he's wearing a pair of canvas shoes with black soles and white bases.",
    "This young man has a fit physique and stands at a medium height. His skin has a warm, golden brown tone, and his short black hair is styled neatly. He's wearing a pair of black sunglasses and a well-groomed black beard that adds a touch of sophistication to his look. His upper body is clad in a black cotton short-sleeved T-shirt with a crisp white letter pattern, which falls just above his belly button. The T-shirt is paired with light gray sports pants that hit just above his knees, creating a stylish and comfortable look. His feet are clad in black canvas shoes with white soles, adding a touch of sportiness to his overall appearance. Overall, this young man exudes confidence and style."
        ]
}
```


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
