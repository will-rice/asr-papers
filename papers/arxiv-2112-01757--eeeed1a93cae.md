---
arxiv_id: "2112.01757"
title: BBS-KWS:The Mandarin Keyword Spotting System Won the Video Keyword Wakeup Challenge
authors:
  - Yuting Yang
  - Binbin Du
  - Yingxin Zhang
  - Wenxuan Wang
  - Yuke Li
submitted: "2021-12-03"
categories:
  - cs.CL
  - cs.SD
  - eess.AS
arxiv_url: https://arxiv.org/abs/2112.01757
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:34:55+00:00"
references_parsed: 0
arxiv_version: ""
---

# BBS-KWS: The Mandarin Keyword Spotting System Won the Video Keyword Wakeup Challenge^(†)^(†)thanks: \* Equal contributions to this work

###### Abstract

This paper introduces the system submitted by the Yidun NISP team to the video keyword wakeup (VKW) challenge ^(†)^(†)https://www.datatang.com/VMR. We propose a mandarin keyword spotting system (KWS) with several novel and effective improvements, including a big backbone (B) model, a keyword biasing (B) mechanism and the introduction of syllable modeling units (S). By considering this, we term the total system BBS-KWS as an abbreviation. The BBS-KWS system consists of an end-to-end automatic speech recognition (ASR) module and a KWS module. The ASR module converts speech features to text representations, which applies a big backbone network to the acoustic model and takes syllable modeling units into consideration as well. In addition, the keyword biasing mechanism is used to improve the recall rate of keywords in the ASR inference stage. The KWS module applies multiple criteria to determine the absence or presence of the keywords, such as multi-stage matching, fuzzy matching, and connectionist temporal classification (CTC) prefix score. To further improve our system, we conduct semi-supervised learning on the CN-Celeb \[6\] dataset for better generalization. In the VKW task, the BBS-KWS system achieves significant gains over the baseline and won the first place in two tracks.

Index Terms: big backbone, keyword biasing, syllable modeling units, multi stage matching, fuzzy matching

## 1 Introduction

Keyword spotting is a task to detect predefined words from continuous speech. It is of importance for human-computer interaction, and is widely used in various smart devices and voice retrieval systems. In recent years, due to the rapid development of artificial intelligence technology, keyword spotting has also achieved promising developments in many scenarios, such as smart speaker, voice assistant, $`e\hspace{0pt}t\hspace{0pt}c`$.

In the past few decades, researchers have proposed kinds of techniques to improve the performance of keyword spotting systems. The first is the family of Query-by-Example (QbyE) methods \[16\] \[14\] \[22\] \[1\], which utilize the keywords speech samples to get a set of feature templates. As in the detection phase, a feature template is extracted from the test speech sample and matched with the keyword feature template via the pair templates similarity. If the similarity exceeds the threshold, it is considered as a hit. The second is the large vocabulary continuous speech recognition (LVCSR) \[19\] \[3\] \[4\] based methods, which is widely used in audio retrieval tasks. These methods transcribe speeches to texts and indexes for keywords information. In order to improve the recall rate, some improved methods \[15\] \[2\] introduce lattice to save multiple decoded sequences as well as position information.

In the VKW challenge, the organizer provides 1505 hours training data and 15 hours fine-tuning data. The F1 score and the actual term-weighted value (ATWV) are used to evaluate system performance. The challenge mainly focus on evaluating the accuracy and the recall rate of the keyword spotting system. In this case, we choose the LVCSR based method for this challenge.

We introduce a BBS-KWS system, which aims to improve the accuracy and the recall rate of keyword spotting in the entire system. Specifically, the equipped ASR module transcribes input speech feature to text representations, and the KWS module uses both the posterior probability of the ASR module and the transcribed text to query keyword candidates paired with the corresponding scores. Since the acoustic model has taken the custom Chinese characters into consideration, it is unnecessary to retrain the model for different keywords. Our contributions are summarized as follows:

(1) We introduce a big backbone network and syllable modeling units to improve the cross-domain performance.

(2) We introduce a keyword biasing mechanism to improve the recall rate of keywords in the speech recognition stage.

(3) In the KWS module, we utilize a series of methods to improve the recall rate of the keyword detection, including multi-stage matching and fuzzy matching.

Inspired by the references \[13\] \[20\], we use semi-supervised learning on the CN-Celeb dataset \[6\] to solve the problem of data sparsity and the domain mismatch between the training set and the validation set. Specifically, we first train a model on the labeled data and then use it as the initial teacher model. We generate pseudo-labels for the unlabeled CN-Celeb dataset via a teacher model, and then use synthesized data to fine-tune the model. This step will be repeated for multiple rounds, and the performance of the new model on the validation set can be greatly improved.

This paper is organized as follows: In Section 2, we describe the structure of the overall BBS-KWS system, including the ASR module and the KWS module. In Section 3, we introduce the experimental setup, the semi-supervised learning and the experimental results on the VKW challenge.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2112.01757/assets/x1.png)

Figure 1: The pipeline of BBS-KWS system.

## 2 BBS-KWS Model

The BBS-KWS system consists of a ASR module and a KWS module, the schematic diagram of the system is provided in Figure 1. In the whole keyword spotting process, the ASR module converts the speech features into N-best hypotheses, and the KWS module continuously match each candidate keywords on the N-best candidate sequences. Once a keyword hits, it uses the results of the ASR acoustic model to calculate the CTC forward score as the confidence score.

### 2.1 ASR Module

The acoustic model converts the input audio features into the probability distribution over the modeling units, which is the most important part in the entire system. In our system, the N-best candidate sequences are generated by the acoustic model.

```math
{l\hspace{0pt}o\hspace{0pt}s\hspace{0pt}s} = {{\lambda\hspace{0pt}l\hspace{0pt}o\hspace{0pt}s\hspace{0pt}s_{c\hspace{0pt}t\hspace{0pt}c}} + {\left( {1 - \lambda} \right)\hspace{0pt}l\hspace{0pt}o\hspace{0pt}s\hspace{0pt}s_{a\hspace{0pt}t\hspace{0pt}t}}}
```

The acoustic model is based on a hybrid CTC/Attention structure \[7\] \[10\] \[18\]. The input of the model is 80-dimensional filterbank features. The output of the encoder is used to calculate the CTC objective, and the output of the decoder together with the ground-truth label are utilized to obtain the CE loss. During training, the loss functions of the two branches will be linearly combined in a certain proportion. As shown in Eq.(1), where $`\lambda`$ denotes the weight of different loss.

Different from the training process, the inference phase of BBS-KWS only uses the branch of CTC module to generate N-best hypotheses. It uses prefix beam search to generate N-best hypotheses, and uses a 4-gram language model (LM) for shallow fusion, and finally obtain N-best sequences.

#### 2.1.1 Big backbone

In recent years, it is common to use the deeper models to improve the performance. For example, researchers have investigated the Transformer \[17\] \[5\] \[11\] model in the field of speech recognition. They usually adopt several layers of CNN plus multiple stacked transformer sublayers. However, it is hard to further improve the model accuracy with increasing the depth of the network. Therefore, the depth of the transformer is generally in the range of 6-24, which is less than the number of network layers in the image field.

To achieve a trade-off between the accuracy and the training efficiency, the BBS-KWS system does not extend the depth of the model, but expand the width of the conformer network \[8\]. Specifically, the encoder adopt the conformer structure with a depth of 12, while the decoder has 6 identical layers. The attention dimension is increased from 256 to 512, and the number of attention heads is also increased from 4 to 8. The width of the feed-forward layer is 2048.

#### 2.1.2 Keyword biasing

Due to the factors such as context information and the frequency of tokens appearing in the training set, the rarely-used words are usually under-estimated and thus leading to the absence of them in N-best paths. This makes keyword spotting a challenging task as the rarely-used words can’t pass into the final keyword determining process. To solve this issue, we utilize keyword biasing technology to perform keyword matching in real time on the process of generating N-best hypotheses. If a certain keyword is matched, the corresponding candidate sentence will be awarded with a certain score.

```math
{W\hspace{0pt}\left( {k\hspace{0pt}e\hspace{0pt}y\hspace{0pt}w\hspace{0pt}o\hspace{0pt}r\hspace{0pt}d} \right)} = {{- {\alpha\hspace{0pt}L\hspace{0pt}M\hspace{0pt}\left( {k\hspace{0pt}e\hspace{0pt}y\hspace{0pt}w\hspace{0pt}o\hspace{0pt}r\hspace{0pt}d} \right)}} + \beta}
```

We introduce a language model and use the predicted scores to adaptively assign weights to words. The N-gram language model counts the word frequency in the training data. By taking a negative number for the score of the language model, the low-frequency keyword will be assigned with high weight. Especially for long keywords, it will be segmented into several parts before calculating weights, thus avoiding the situation that some keywords cannot be matched because of their excessive lengths. As shown in Eq.(2), where $`L\hspace{0pt}M`$ is the N-gram language model, $`\alpha`$ and $`\beta`$ are parameters of the affine transformation.

#### 2.1.3 Syllable modeling units

Another problem in the VKW task is that there are less in-domain data matching the test set. It is extremely difficult to fine-tune the effect of the large model on such a small amount of data. To solve this problem, we follow \[21\] \[9\] \[23\] to introduce the smaller syllable modeling units than character units. At the same time, in order to maintain the accuracy at the expected character level, the character-level modeling unit is also retained.

The CTC classifier considers syllables as modeling units, and the decoder deal with characters units. Therefore, the entire loss function is a linear combination between the syllable-based CTC loss and the character-based CE loss. The specific structure is shown in Figure 2.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2112.01757/assets/x2.png)

Figure 2: Hybrid syllable-character model.

### 2.2 KWS Module

The KWS module aims to detect whether the keywords exist in the speech according to the results of the ASR module, which can be divided into two steps: matching and scoring. In the matching stage, the BBS-KWS system uses fuzzy matching and multi-stage matching to improve the recall rate of the keywords. And in the scoring stage, the BBS-KWS system uses the CTC algorithm to calculate the confidence score of the keywords.

#### 2.2.1 Keyword matching and scoring

|                                        |        |        |        |        |        |        |
| -------------------------------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Methods                                | F1     |        |        | ATWV   |        |        |
|                                        | lgv    | liv    | stv    | lgv    | liv    | stv    |
| Chain model baseline                   | 0.6781 | 0.6565 | 0.7006 | 0.5171 | 0.6027 | 0.5644 |
| Conformer with character modeling unit | 0.7646 | 0.7899 | 0.8154 | 0.5534 | 0.6479 | 0.6222 |
| + LM                                   | 0.7988 | 0.8249 | 0.839  | 0.6191 | 0.7183 | 0.6997 |
| + Length normalization                 | 0.8236 | 0.849  | 0.8579 | 0.6703 | 0.7784 | 0.7711 |
| + N-best matching                      | 0.8247 | 0.8476 | 0.8531 | 0.7019 | 0.8066 | 0.7933 |
| + SSL round 1                          | 0.8543 | 0.886  | 0.8969 | 0.7192 | 0.8271 | 0.8129 |
| + keyword biasing                      | 0.857  | 0.8813 | 0.8898 | 0.7587 | 0.8457 | 0.8356 |
| + SSL round 4                          | 0.8644 | 0.8897 | 0.8893 | 0.7677 | 0.8538 | 0.8335 |
| + Fuzzy matching                       | 0.8681 | 0.8937 | 0.8987 | 0.8078 | 0.8693 | 0.8579 |
| + Syllable modeling units              | 0.8886 | 0.9059 | 0.91   | 0.82   | 0.8809 | 0.8683 |
| Ensemble                               | 0.8839 | 0.8973 | 0.8965 | 0.8495 | 0.9024 | 0.8895 |

Table 1: Comparison of methods

The KWS module performs to query keywords from the N-best results decoded by the acoustic model. If the keyword appears more than once in the N-best sequences, it is considered as a hit and passed into the next step of scoring.

Keyword Matching: During the matching process, BBS-KWS introduces a multi-stage matching strategy and a fuzzy matching strategy to improve the recall rate. Multi-stage matching uses the model with hybrid syllable and character modeling units for syllable matching and character matching. Keywords will be matched in both the syllable N-best sequences and the character N-best sequences, respectively. At the same time, fuzzy matching is used to improve the recall rate of keyword spotting. The dimsim ^(†)^(†)https://github.com/System-T/DimSim.git library is used to calculate the pronunciation similarity between the decoded vocabulary and the keywords. If the distance is less than a certain threshold, the keyword is also considered as a hit.

Keyword Scoring: Once the keyword hits, it will be passed to the consequent scoring stage. The CTC classifier outputs the probability distribution of each frame, and uses the CTC peak information to obtain the position offset of the keyword in the speech as well as computes the probability of the keyword path.

```math
{S\hspace{0pt}\left( {k\hspace{0pt}w} \right)} = {\sum\limits_{\pi:{{\beta\hspace{0pt}{(\pi)}} = {k\hspace{0pt}w}}}{\rho\hspace{0pt}(\pi)}}
```

As shown in Eq.(3), where _kw_ stands for keywords, $`\beta`$ is the CTC path compression algorithm, $`\pi`$ is the keyword’s state path of the CTC prefix beam search, and $`\rho\hspace{0pt}{()}`$ calculate the path score. In particular, if multi-stage matching is used, once the syllable keyword and the character keyword hit at the same time, the result with a higher score will be reserved.

The BBS-KWS applies the length normalization to the confidence score.

```math
{S\hspace{0pt}c\hspace{0pt}o\hspace{0pt}r\hspace{0pt}e\hspace{0pt}\left( {k\hspace{0pt}w} \right)} = {\left. {S\hspace{0pt}\left( {k\hspace{0pt}w} \right)}/l \right.\hspace{0pt}e\hspace{0pt}n\hspace{0pt}g\hspace{0pt}t\hspace{0pt}h\hspace{0pt}\left( {k\hspace{0pt}w} \right)}
```

## 3 Experiments And Results

### 3.1 Experimental Setup

The training data consists of the following three parts: (1) 1505 hours of training set (2) 15 hours of fine-tune dataset collected from Long video, short video, and live broadcast (3) 560h unlabeled data randomly selected from CN-Celeb dataset for semi-supervised learning. We use the SpecAug method \[12\] during training process and speed augmentation with coefficient (0.9, 1.0, 1.1) for training data respectively.

The text corpus for language model consists of two parts: (1) labeled data provided by the contestant. (2) the text corpus are collected from the public website, including Wikipedia, Weibo, Douban, and Netease News. The language model is trained on 40M sentences. Both the training data and the text corpus used in restricted and unrestricted tracks are the same.

The BBS-KWS adopt the conformer structure, the attention dimension is 512, and the number of attention heads are 8. We used a 12-layer encoder and a 6-layer decoder. The $`\lambda`$ in Eq.(1) is 0.9. During decoding, ($`\alpha`$,$`\beta`$) in Eq.(2) is (1,4), the beam size is 10. The threshold of dimsim is 0.5.

The system uses voice keywords F1 and actual term-weighted value (ATWV) to measure system performance. Among them, F1 reflects both the accuracy and the recall rate of the system. ATWV mainly evaluates the average TWV value of the system on each keyword, which reflects the system’s detection effect on the keywords with different frequencies.

The final submitted system is the ensemble of the three well-trained models.

### 3.2 Semi-supervised Learning

In order to solve the problem of domain mismatch between the training set and the validation set, the CN-Celeb dataset \[6\] is used for semi-supervised learning (SSL). We randomly select 560h CN-Celeb data for semi-supervised learning. The method we used are inspired by the noisy student training (NST). Formally, the selected unlabeled data and the well-trained teacher model are denoted as $`U`$ and $`M_{0}`$, respectively. The semi-supervised learning algorithm is summarized as follow:

(1) Set the initial teacher model $`M = M_{0}`$.

(2) Generate pseudo-label $`M\hspace{0pt}(U)`$ via the teacher model $`M`$.

(3) Mix $`M\hspace{0pt}(U)`$ and the VKW data to fine-tune the model $`M_{0}`$ and get a new model $`M'`$.

(4) Set $`M = M'`$ and repeat step (2) (3) until convergence.

### 3.3 Experimental Results

Table 1 shows the performance of the BBS-KWS system in three scenarios: long video (lgv), short video (stv), and live broadcast (liv). We can draw the following conclusions from the table. First, the language model, length normalization and syllable modeling units brought significant improvements. Second, compared to the chain baseline model, the F1 score of the BBS-KWS system is improved from (67.81%, 65.65%, 70.06%) to (88.39%, 89.73%, 89.65%) in the three scenarios respectively. And the ATWV score of the BBS-KWS system is improved from (51.71%, 60.27%, 56.44%) to (84.95%, 90.24%, 88.95%). Overall, the BBS-KWS achieves 31% F1 relative increase, and 56% ATWV increase. Among them, the best performance of the single system achieved 32% F1 relative increase, and 52% ATWV increase.

Furthermore, the semi-supervised learning uses the CN-Celeb data to increase the diversity of training data, thereby improving the performance of the model. This experiment is repeated four times, and the accuracy of pseudo-labels are improved through multiple rounds of iteration. As can be see from the Table 1, the SSL have brought a great improvement.

## 4 Conclusions

The BBS-KWS system exploits a hybrid CTC/Attention acoustic model, combined with a big backbone, syllable modeling units, and keyword biasing technology to improve the performance of the ASR module. In the KWS module, it uses the fuzzy matching and multi-stage matching methods, achieving promising performance. And we adopt the semi-supervised learning to further improve the robustness of the system. In the VKW task, the BBS-KWS system achieves significant gains over the baseline, which achieves 31% F1 increase and 56% ATWV increase.

## References

- \[1\] Mohamed S Barakat, Christian H Ritz, and David A Stirling. An improved template-based approach to keyword spotting applied to the spoken content of user generated video blogs. In 2012 IEEE International Conference on Multimedia and Expo, pages 723–728. IEEE, 2012.
- \[2\] Peter S Cardillo, Mark Clements, and Michael S Miller. Phonetic searching vs. lvcsr: How to find what you really want in audio archives. International Journal of Speech Technology, 5(1):9–22, 2002.
- \[3\] Guoguo Chen, Sanjeev Khudanpur, Daniel Povey, Jan Trmal, David Yarowsky, and Oguz Yilmaz. Quantifying the value of pronunciation lexicons for keyword search in lowresource languages. In 2013 IEEE International Conference on Acoustics, Speech and Signal Processing, pages 8560–8564. IEEE, 2013.
- \[4\] Guoguo Chen, Oguz Yilmaz, Jan Trmal, Daniel Povey, and Sanjeev Khudanpur. Using proxies for oov keywords in the keyword search task. In 2013 IEEE Workshop on Automatic Speech Recognition and Understanding, pages 416–421. IEEE, 2013.
- \[5\] Linhao Dong, Shuang Xu, and Bo Xu. Speech-transformer: a no-recurrence sequence-to-sequence model for speech recognition. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 5884–5888. IEEE, 2018.
- \[6\] Yue Fan, JW Kang, LT Li, KC Li, HL Chen, ST Cheng, PY Zhang, ZY Zhou, YQ Cai, and Dong Wang. Cn-celeb: a challenging chinese speaker recognition dataset. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 7604–7608. IEEE, 2020.
- \[7\] Alex Graves, Santiago Fernández, Faustino Gomez, and Jürgen Schmidhuber. Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks. In Proceedings of the 23rd international conference on Machine learning, pages 369–376, 2006.
- \[8\] Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar, Yu Zhang, Jiahui Yu, Wei Han, Shibo Wang, Zhengdong Zhang, Yonghui Wu, et al. Conformer: Convolution-augmented transformer for speech recognition. arXiv preprint arXiv:2005.08100, 2020.
- \[9\] Abdelwahab Heba, Thomas Pellegrini, Jean Pierre Lorre, and Régine André-Obrecht. Char+cv-ctc: Combining graphemes and consonant/vowel units for ctc-based asr using multitask learning. In Interspeech 2019, 2019.
- \[10\] Suyoun Kim, Takaaki Hori, and Shinji Watanabe. Joint ctc-attention based end-to-end speech recognition using multi-task learning. In 2017 IEEE international conference on acoustics, speech and signal processing (ICASSP), pages 4835–4839. IEEE, 2017.
- \[11\] Abdelrahman Mohamed, Dmytro Okhonko, and Luke Zettlemoyer. Transformers with convolutional context for asr. arXiv preprint arXiv:1904.11660, 2019.
- \[12\] Daniel S Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D Cubuk, and Quoc V Le. Specaugment: A simple data augmentation method for automatic speech recognition. arXiv preprint arXiv:1904.08779, 2019.
- \[13\] Daniel S Park, Yu Zhang, Ye Jia, Wei Han, Chung-Cheng Chiu, Bo Li, Yonghui Wu, and Quoc V Le. Improved noisy student training for automatic speech recognition. arXiv preprint arXiv:2005.09629, 2020.
- \[14\] Shane Settle, Keith Levin, Herman Kamper, and Karen Livescu. Query-by-example search with discriminative neural acoustic word embeddings. In Interspeech 2017, 2017.
- \[15\] Kishan Thambiratnam and Sridha Sridharan. Dynamic match phone-lattice searches for very fast and accurate unrestricted vocabulary keyword spotting. In Proceedings.(ICASSP’05). IEEE International Conference on Acoustics, Speech, and Signal Processing, 2005., volume 1, pages I–465. IEEE, 2005.
- \[16\] Drisya Vasudev, Suryakanth V Gangashetty, KK Anish Babu, and KS Riyas. Query-by-example spoken term detection using bessel features. In 2015 IEEE International Conference on Signal Processing, Informatics, Communication and Energy Systems (SPICES), pages 1–4. IEEE, 2015.
- \[17\] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in neural information processing systems, pages 5998–6008, 2017.
- \[18\] Shinji Watanabe, Takaaki Hori, Suyoun Kim, John R Hershey, and Tomoki Hayashi. Hybrid ctc/attention architecture for end-to-end speech recognition. IEEE Journal of Selected Topics in Signal Processing, 11(8):1240–1253, 2017.
- \[19\] Mitchel Weintraub. Lvcsr log-likelihood ratio scoring for keyword spotting. In 1995 International Conference on Acoustics, Speech, and Signal Processing, volume 1, pages 297–300. IEEE, 1995.
- \[20\] Qizhe Xie, Minh-Thang Luong, Eduard Hovy, and Quoc V Le. Self-training with noisy student improves imagenet classification. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10687–10698, 2020.
- \[21\] Shiliang Zhang, Ming Lei, Yuan Liu, and Wei Li. Investigation of modeling units for mandarin speech recognition using dfsmn-ctc-smbr. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 7085–7089. IEEE, 2019.
- \[22\] Yaodong Zhang and James R Glass. Unsupervised spoken keyword spotting via segmental dtw on gaussian posteriorgrams. In 2009 IEEE Workshop on Automatic Speech Recognition & Understanding, pages 398–403. IEEE, 2009.
- \[23\] Wei Zou, Dongwei Jiang, Shuaijiang Zhao, Guilin Yang, and Xiangang Li. Comparable study of modeling units for end-to-end mandarin speech recognition. In 2018 11th International Symposium on Chinese Spoken Language Processing (ISCSLP), pages 369–373. IEEE, 2018.
