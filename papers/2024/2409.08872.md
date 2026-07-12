---
arxiv_id: "2409.08872"
title: Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages
authors:
  - Yao-Fei Cheng
  - Li-Wei Chen
  - Hung-Shin Lee
  - Hsin-Min Wang
submitted: "2024-09-13"
categories:
  - cs.CL
  - cs.SD
  - eess.AS
arxiv_url: https://arxiv.org/abs/2409.08872
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:52:37+00:00"
references_parsed: 0
arxiv_version: ""
---

¹University of Washington, ²National Tsing Hua University\
³United Link Co., Ltd., ⁴Academia Sinica\
nlp5566@uw.edu

# Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages

###### Abstract

This study investigates the efficacy of data augmentation techniques for low-resource automatic speech recognition (ASR), focusing on two endangered Austronesian languages, Amis and Seediq. Recognizing the potential of self-supervised learning (SSL) in low-resource settings, we explore the impact of data volume on the continued pre-training of SSL models. We propose a novel data-selection scheme leveraging a multilingual corpus to augment the limited target language data. This scheme utilizes a language classifier to extract utterance embeddings and employs one-class classifiers to identify utterances phonetically and phonologically proximate to the target languages. Utterances are ranked and selected based on their decision scores, ensuring the inclusion of highly relevant data in the SSL-ASR pipeline. Our experimental results demonstrate the effectiveness of this approach, yielding substantial improvements in ASR performance for both Amis and Seediq. These findings underscore the feasibility and promise of data augmentation through cross-lingual transfer learning for low-resource language ASR.

Index Terms—  self-supervised learning, low-resource language, automatic speech recognition

## 1 Introduction

The development of contemporary end-to-end automatic speech recognition (ASR) systems has achieved remarkable success in high-resource languages such as English, French, and Chinese, largely due to the availability of extensive speech-text paired data \[[1](https://arxiv.org/html/2409.08872v2#bib.bibx1), [2](https://arxiv.org/html/2409.08872v2#bib.bibx2)\]. However, this abundance does not extend to endangered languages like Amis and Seediq, where acquiring high-quality transcriptions is particularly challenging and resource-intensive. The scarcity of annotated data, coupled with factors such as limited speaker populations and non-standardized writing systems, poses significant obstacles to building effective ASR systems. In response, self-supervised learning (SSL) has emerged as a promising approach to mitigate data sparsity in low-resource ASR settings \[[3](https://arxiv.org/html/2409.08872v2#bib.bibx3), [4](https://arxiv.org/html/2409.08872v2#bib.bibx4), [5](https://arxiv.org/html/2409.08872v2#bib.bibx5)\]. SSL models, pre-trained on large amounts of unlabeled speech, can be fine-tuned with limited labeled data. However, the pre-training stage typically requires far more data than supervised methods—for instance, the wav2vec 2.0 base model demands 960 hours of speech for effective pre-training \[[4](https://arxiv.org/html/2409.08872v2#bib.bibx4)\]. This makes training SSL models from scratch impractical for endangered languages, where large-scale data collection is often infeasible.

To address the broader issue of resource scarcity in natural language processing, researchers have explored various strategies, including language representation tools like lang2vec \[[6](https://arxiv.org/html/2409.08872v2#bib.bibx6)\] and data augmentation techniques \[[7](https://arxiv.org/html/2409.08872v2#bib.bibx7), [8](https://arxiv.org/html/2409.08872v2#bib.bibx8)\]. However, these approaches face limitations when applied to low-resourced languages like Amis and Seediq. lang2vec currently lacks support for these languages, while data augmentation often depends on textual data, which is scarce or unavailable for many spoken and low-resource languages.

Consequently, recent research has shifted towards leveraging multilingual SSL models for low-resource ASR \[[9](https://arxiv.org/html/2409.08872v2#bib.bibx9), [10](https://arxiv.org/html/2409.08872v2#bib.bibx10)\]. This approach capitalizes on phonetic similarities across languages, enabling knowledge transfer and improved transcription accuracy during fine-tuning. Further emphasizing the potential of this approach, Nowakowski et al. demonstrated the effectiveness of continuing pre-training with target language data, albeit with a significant data requirement exceeding $`234`$ hours \[[11](https://arxiv.org/html/2409.08872v2#bib.bibx11)\]. Their work also explored leveraging phonetically similar languages for data augmentation, achieving promising results. Similarly, San et al. proposed utilizing donor speech data from related languages for fine-tuning, highlighting the potential of cross-lingual transfer learning in low-resource settings \[[12](https://arxiv.org/html/2409.08872v2#bib.bibx12)\].

This research diverges from previous studies by exploring the feasibility of achieving robust ASR performance with minimal paired and unpaired data for the target language. Focusing on the severely low-resource Austronesian languages, Amis and Seediq, we aim to develop effective ASR systems using a modest multilingual corpus and limited paired data (less than one hour per language). Our approach centers on a novel data-selection strategy designed to identify and incorporate utterances from the multilingual corpus that exhibit close phonetic and phonological similarity to the target languages, thus refining the SSL-ASR pipeline. We achieve this by first employing a language classifier to extract language-specific embeddings for each utterance \[[13](https://arxiv.org/html/2409.08872v2#bib.bibx13), [14](https://arxiv.org/html/2409.08872v2#bib.bibx14)\]. Then, leveraging a suite of one-class classifiers – One-class SVM \[[15](https://arxiv.org/html/2409.08872v2#bib.bibx15)\], Isolation Forest \[[16](https://arxiv.org/html/2409.08872v2#bib.bibx16)\], and Deep SVDD \[[17](https://arxiv.org/html/2409.08872v2#bib.bibx17)\] – we rank and select utterances based on their decision scores, prioritizing those most similar to the target languages. Our results demonstrate the effectiveness of this approach for both Amis and Seediq, yielding promising ASR performance despite the significant data constraints.

## 2 Data Description

![Refer to caption](https://arxiv.org/html/x1.png)

Fig. 1: Diagram for picking the top-$`k`$ hours data.

Taiwan is home to $`16`$ indigenous ethnic groups, encompassing $`42`$ dialects. The Indigenous Languages Research and Development Foundation (ILRDF) introduced Klokah¹¹1[https://web.klokah.tw](https://web.klokah.tw), an e-learning platform with abundant audio materials to foster native language use among the younger generation. For ASR system development, we curated a multi-speaker dataset from two subjects: reading-and-writing and contextual-language, chosen based on their suitable audio lengths. We selected Amis and Seediq for experimentation, allocating 1 hour or 10 minutes of speech for training and 10 minutes each for validation and testing.

### 2.1 Amis

Amis has approximately $`218,500`$ speakers in Taiwan. It is one of the endangered languages identified by the United Nations Educational, Scientific, and Cultural Organization (UNESCO). Its writing system consists of $`21`$ Latin letters and one digraph (ng). Another $`5`$ Latin letters (b, g, j, q, and v) are used only for loanwords. The epiglottal stop // and glottal stop // are marked as ’ and ^, respectively. The vowel length // is marked as a colon symbol $`\colon`$, meaning semantic emphasis.

Amis has five dialect groups: 'Amisay a Pangcah, Siwkolan 'Amis, Pasawalian Pangcah, Farangaw Amis, and Palidaw 'Amis. Its written system can be vague, i.e., the same pronunciation has different written symbols. For instance, only 'Amisay a Pangcah uses the symbol o to represent /o/, and the other four groups use the symbol u to represent /o/.

### 2.2 Seediq

Seediq is also an endangered language identified by UNESCO. Its language population in Taiwan is about $`10,970`$. The written system of Seediq consists of $`23`$ Latin letters and seven diphthongs (aw, ay, ey, ow, uy, ug, and ng). The Seediq text is written in syllabic units of semantic words, with an apostrophe ' to mark where the syllables in the same word have to be separated because of the sound level or where there is still a problem with the attribution of the pronunciation, or where the vowel sound // is indicated.

## 3 Method

Inspired by Nowakowski et al.'s work \[[11](https://arxiv.org/html/2409.08872v2#bib.bibx11)\], which demonstrated that continued pre-training with a related language (Japanese) significantly improved ASR performance for Ainu, a low-resource language²²2Interestingly, the Ainu speech data utilized for continued pre-training of the SSL model exceeded 200 hours., we propose a novel data augmentation strategy. Since lang2vec \[[6](https://arxiv.org/html/2409.08872v2#bib.bibx6)\]—the tool they used to identify related languages—does not support our target languages, we present an alternative approach: leveraging multilingual fine-tuning of an SSL model with data from languages that share phonetic and phonological similarities with our target languages. This strategy aims to enhance speech recognition performance by enriching the training data with acoustically similar utterances from related languages.

Our methodology, illustrated in [Fig. 1](https://arxiv.org/html/2409.08872v2#S2.F1 "In 2 Data Description ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages"), employs a two-phase approach. In the first phase, a neural spoken language identification model analyzes utterances to extract language-specific embeddings \[[13](https://arxiv.org/html/2409.08872v2#bib.bibx13), [14](https://arxiv.org/html/2409.08872v2#bib.bibx14)\] (orange box in [Fig. 1](https://arxiv.org/html/2409.08872v2#S2.F1 "In 2 Data Description ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")). These embeddings, derived from the penultimate layer of the classifier, encapsulate rich phonetic and phonological information. The second phase leverages these embeddings to train a suite of one-class classifiers (red box in [Fig. 1](https://arxiv.org/html/2409.08872v2#S2.F1 "In 2 Data Description ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")). These classifiers are then employed to identify and select utterances from a larger multilingual dataset that exhibit high similarity to the target language, thereby enriching the training data for subsequent SSL model fine-tuning.

1:Given three lists of utterances $`U_{1}`$, $`U_{2}`$, and $`U_{3}`$ sorted by decision scores of Deep SVDD, One-class SVM, and Isolation Forest

2:Initial ranking limit $`L_{0}`$, final list $`R`$, and specified hours $`k`$.

3:$`L\leftarrow L_{0}`$

4:while the total length in $`R<k`$ hours do

5:  $`\widehat{U}_{1}\leftarrow U_{1}[:L]`$

6:  $`\widehat{U}_{2}\leftarrow U_{2}[:L]`$

7:  $`\widehat{U}_{3}\leftarrow U_{3}[:L]`$

8:  for $`u\in\widehat{U}_{1}`$ do

9:    if $`u\notin R`$ and $`u\in\widehat{U}_{2}`$ and $`u\in\widehat{U}_{3}`$ then

10:     $`R`$.append($`u`$)

11:    end if

12:  end for

13:  $`L\leftarrow L+L_{0}`$

14:end while

Algorithm 1 Multi-list Utterance Selection

First, One-class Support Vector Machine (OcSVM) aims to construct a hyperplane in a high-dimensional feature space that encloses the majority of data points while maximizing the distance between this hyperplane and the origin \[[15](https://arxiv.org/html/2409.08872v2#bib.bibx15)\]. This approach effectively separates the data from regions with a sparse data density. Data points falling outside the hyperplane's boundary are then classified as anomalies.

Second, Isolation Forest (IF) leverages an ensemble of isolation trees to detect anomalies \[[18](https://arxiv.org/html/2409.08872v2#bib.bibx18)\]. Each tree is constructed by recursively partitioning the data based on randomly selected features and split points. The algorithm aggregates these path lengths to provide an anomaly score for each data point.

Finally, Deep Support Vector Data Description (D-SVDD) utilizes a deep neural network to learn a hypersphere in the feature space that encapsulates the training data while minimizing the volume of this hypersphere \[[17](https://arxiv.org/html/2409.08872v2#bib.bibx17)\].

Given the potential for variation in the rankings produced by each classifier, we introduce an ensemble algorithm to harmonize their predictions and enhance the reliability of the utterance selection process (see [Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")). This algorithm prioritizes consistently flagged utterances similar to those of all three classifiers, ensuring a more robust and confident data selection for augmenting the SSL model's training set.

[Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") aims to create a list of utterances ($`R`$), given three pre-sorted lists ($`U_{1}`$, $`U_{2}`$, $`U_{3}`$) based on the scores of Deep SVDD, One-class SVM, and Isolation Forest. The algorithm prioritizes utterances appearing high in all three lists.

The process begins by initializing $`L`$ with an initial ranking limit ($`L_{0}`$). It iteratively expands $`L`$ until the total duration of utterances in $`R`$ meets a predefined time limit ($`k`$ hours). Each iteration involves selecting top $`L`$ utterances from each list ($`U_{1}`$, $`U_{2}`$, $`U_{3}`$), denoted as $`\widehat{U_{1}}`$, $`\widehat{U_{2}}`$, and $`\widehat{U_{3}}`$. Subsequently, each utterance ($`u`$) in $`\widehat{U_{1}}`$ is evaluated. If $`u`$ is not already in $`R`$ and is present in both $`\widehat{U_{2}}`$ and $`\widehat{U_{3}}`$, it signifies high ranking across all three lists and is appended to $`R`$. After processing all utterances in $`\widehat{U_{1}}`$, $`L`$ is incremented by $`L_{0}`$ for the next iteration. This cycle continues until the time constraint of $`R`$ is met.

## 4 Experiments

Our experimental procedure unfolds as follows: In addition to leveraging the existing, limited volume of target language data, we employ the top-$`k`$ hours of sampled data from the ML-SUPERB multilingual corpus. This selection is facilitated by a one-class classifier or [Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages"), intended for the continued pre-training of the SSL model. The refined model is then utilized to generate SSL features, enabling fine-tuning of the downstream ASR model using target language speech data accompanied by transcriptions. For our framework, Fairseq is used for pre-training, while both S3PRL and ESPnet are employed for downstream ASR tasks \[[19](https://arxiv.org/html/2409.08872v2#bib.bibx19), [20](https://arxiv.org/html/2409.08872v2#bib.bibx20), [21](https://arxiv.org/html/2409.08872v2#bib.bibx21)\].

### 4.1 Continued Pre-training

Following the methodology outlined by Nowakowski et al., we continued to pre-train the entire SSL model with the curated data. The training utterances were curated from the ML-SUPERB benchmark using one-class classifiers. This process involved $`100,000`$ updates, including $`10,000`$ warmup steps, with a batch size of $`256`$ and a learning rate set at $`10^{-4}`$. All settings were aligned with those of the wav2vec 2.0 large model. The optimal configuration was identified using validation data from the ML-SUPERB benchmark.

### 4.2 One-class Classification

Our process commenced using NVIDIA's pre-trained TitaNet-LID to derive language embeddings for each utterance \[[14](https://arxiv.org/html/2409.08872v2#bib.bibx14)\]. This model attains a $`7.0`$% error rate on the $`103`$ languages test set. The obtained embeddings are situated in a 512-dimensional space, originating from the penultimate layer.

|                                                                                                                                                |                |              |            |         |              |           |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ | ---------- | ------- | ------------ | --------- |
| SSL/Acoustic Features                                                                                                                          | \# Params. (M) | \# Languages | Amis-10min | Amis-1h | Seediq-10min | Seediq-1h |
| Mel-filterbank                                                                                                                                 | N/A            | N/A          | 40.5       | 28.5    | 49.4         | 36.0      |
| wav2vec2-base \[[4](https://arxiv.org/html/2409.08872v2#bib.bibx4)\]                                                                           | 95             | 1            | 14.6       | 9.8     | 19.8         | 11.9      |
| wav2vec2-large \[[4](https://arxiv.org/html/2409.08872v2#bib.bibx4)\]                                                                          | 317            | 1            | 13.4       | 9.5     | 18.5         | 11.4      |
| robust-wav2vec2-large \[[22](https://arxiv.org/html/2409.08872v2#bib.bibx22)\]                                                                 | 317            | 1            | 13.5       | 9.3     | 18.6         | 11.5      |
| chinese-wav2vec2-base³³3https://huggingface.co/TencentGameMate/chinese-wav2vec2-base\[[23](https://arxiv.org/html/2409.08872v2#bib.bibx23)\]   | 95             | 1            | 14.4       | 9.4     | 18.7         | 11.2      |
| chinese-wav2vec2-large⁴⁴4https://huggingface.co/TencentGameMate/chinese-wav2vec2-large\[[23](https://arxiv.org/html/2409.08872v2#bib.bibx23)\] | 317            | 1            | 89.4       | 10.0    | 22.2         | 12.5      |
| chinese-wav2vec2-large^(∗) \[[23](https://arxiv.org/html/2409.08872v2#bib.bibx23)\]                                                            | 317            | 1            | 15.3       | 10.0    | 21.6         | 12.3      |
| wav2vec2-base-23 \[[10](https://arxiv.org/html/2409.08872v2#bib.bibx10)\]                                                                      | 95             | 23           | 14.5       | 9.2     | 19.6         | 12.1      |
| wav2vec2-large-23 \[[10](https://arxiv.org/html/2409.08872v2#bib.bibx10)\]                                                                     | 317            | 23           | 103.4      | 9.6     | 19.2         | 11.3      |
| wav2vec2-large-23^(∗) \[[10](https://arxiv.org/html/2409.08872v2#bib.bibx10)\]                                                                 | 317            | 23           | 13.5       | 9.2     | 18.4         | 11.4      |
| XLSR-53 \[[24](https://arxiv.org/html/2409.08872v2#bib.bibx24)\]                                                                               | 317            | 53           | 81.4       | 10.4    | 18.6         | 14.0      |
| XLSR-300M⁵⁵5https://huggingface.co/facebook/wav2vec2-xls-r-300m\[[25](https://arxiv.org/html/2409.08872v2#bib.bibx25)\]                        | 317            | 128          | 90.8       | 7.7     | 14.0         | 8.4       |
| XLSR-300M^(∗) \[[25](https://arxiv.org/html/2409.08872v2#bib.bibx25)\]                                                                         | 317            | 128          | 10.9       | 7.9     | 13.7         | 8.6       |
| HuBERT-base \[[5](https://arxiv.org/html/2409.08872v2#bib.bibx5)\]                                                                             | 95             | 1            | 12.6       | 8.8     | 18.2         | 11.0      |
| HuBERT-large \[[5](https://arxiv.org/html/2409.08872v2#bib.bibx5)\]                                                                            | 317            | 1            | 80.6       | 7.4     | 84.1         | 8.9       |
| HuBERT-large^(∗) \[[5](https://arxiv.org/html/2409.08872v2#bib.bibx5)\]                                                                        | 317            | 1            | 10.3       | 7.5     | 14.0         | 9.1       |
| chinese-hubert-base⁶⁶6https://huggingface.co/TencentGameMate/chinese-hubert-base\[[23](https://arxiv.org/html/2409.08872v2#bib.bibx23)\]       | 317            | 1            | 13.2       | 9.0     | 18.4         | 10.9      |
| chinese-hubert-large⁷⁷7https://huggingface.co/TencentGameMate/chinese-hubert-large\[[23](https://arxiv.org/html/2409.08872v2#bib.bibx23)\]     | 317            | 1            | 11.0       | 7.3     | 14.7         | 8.1       |
| mHuBERT-base \[[26](https://arxiv.org/html/2409.08872v2#bib.bibx26)\]                                                                          | 95             | 3            | 12.9       | 8.9     | 17.3         | 11.5      |

Table 1: CER (%) evaluated on Amis and Seediq using SSL models. ^(∗) indicates a smaller downstream ASR model. 10min and 1h mean the amount of training data used in downstream ASR models.

For the classifiers, we utilized scikit-learn to train the One-class SVM and Isolation Forest, largely sticking to the default parameters. In the case of Deep SVDD, we implemented a modification by substituting the original 2D convolution for a 1D variant. The autoencoder was pre-trained for $`2,500`$ epochs with a learning rate of $`10^{-2}`$, and the encoder was further trained for $`1,000`$ epochs at a reduced learning rate of $`10^{-3}`$. Negative samples were selected from the ML-SUPERB training data and combined with the original test utterances from Amis and Seediq as positive samples. Our experiments demonstrated the superior performance of Deep SVDD in this setup.

### 4.3 Fine-tuning

The downstream ASR task followed ML-SUPERB's design. The frozen SSL representations were weighted summed with learnable weights. The ASR model consisted of a CNN layer that downsamples the SSL feature sequence to half the original length and two Transformer encoders with an attention dimension of $`256`$, a feedforward layer with a dimension of $`1,024`$, and $`8`$ heads. The model is trained with connectionist temporal classification (CTC) and Adam optimizer with a learning rate of $`10^{-4}`$ and $`10^{-6}`$ weight decay \[[27](https://arxiv.org/html/2409.08872v2#bib.bibx27), [28](https://arxiv.org/html/2409.08872v2#bib.bibx28)\]. We set dropout to $`0.1`$, batch size to $`8`$, and gradient accumulation to $`4`$. SpecAugment was applied to SSL features \[[29](https://arxiv.org/html/2409.08872v2#bib.bibx29)\].

## 5 Results

### 5.1 ASR Results on Amis and Seediq

![Refer to caption](https://arxiv.org/html/x2.png)

(a)

![Refer to caption](https://arxiv.org/html/x3.png)

(b)

Fig. 2: The effect of data amount and selection on continued pre-training XLSR-128 for Amis and Seediq. The x-axis represents the amount of sampled data (in hours), and \`1' means 1 hour of non-target language data is used together with 1 hour of target language data in continued pre-training. The shades in blue and red represent the amount of pre-training data.

[Table 1](https://arxiv.org/html/2409.08872v2#S4.T1 "In 4.2 One-class Classification ‣ 4 Experiments ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") presents an overview of ASR results for both Amis and Seediq, where the downstream ASR models are directly fine-tuned from SSL models in various settings (see [Section 4.3](https://arxiv.org/html/2409.08872v2#S4.SS3 "4.3 Fine-tuning ‣ 4 Experiments ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") for details). We have compared models that were pre-trained with utterances in multilingual, English-only, and Mandarin Chinese-only. Additionally, we evaluated the effectiveness of the model architecture and parameter size.

chinese-hubert-large (Hubert-large fine-tuned with Mandarin Chinese data) consistently outperformed other models across different training data volumes, except for the Seediq 10-minute task. This superior performance was observed despite using identical training data for wav2vec2 (see results of chinese-hubert-large vs. chinese-wav2vec2-large), suggesting potential advantages of the HuBERT architecture for these low-resource scenarios. Furthermore, XLSR-300M demonstrated comparable effectiveness, achieving the lowest CER of 13.7% on the Seediq 10-minute task. These results highlight several noteworthy trends:

- •
  HuBERT generally outperform wav2vec2 when trained on the same data.
- •
  Larger SSL models yield modest but consistent gains, especially in the 1-hour training setup.
- •
  Multilingual pre-training contributes positively to ASR performance in low-resource settings.

As observed in [Table 1](https://arxiv.org/html/2409.08872v2#S4.T1 "In 4.2 One-class Classification ‣ 4 Experiments ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages"), large SSL models, while generally outperforming their smaller counterparts, exhibit a tendency to overfit when trained on limited data. This overfitting was particularly evident for models like wav2vec2-large-23, chinese-wav2vec2-large, XLSR-53, XLSR-300M, and\
HuBERT-large. To mitigate this issue, we modified the downstream ASR model architecture by halving the number of attention heads to $`4`$, reducing the feedforward dimension to $`512`$, and increasing the dropout rate to $`0.3`$. These adjustments, as demonstrated in [Table 1](https://arxiv.org/html/2409.08872v2#S4.T1 "In 4.2 One-class Classification ‣ 4 Experiments ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") (models denoted by ^(∗)), enabled the smaller ASR model to achieve comparable performance even when paired with larger SSL models, effectively addressing the overfitting problem.

### 5.2 Proposed Data Augmentation Method

This section explores the effectiveness of our proposed data augmentation method. Specifically, we attempt to improve the downstream ASR results that we discussed previously (see [Section 5.1](https://arxiv.org/html/2409.08872v2#S5.SS1 "5.1 ASR Results on Amis and Seediq ‣ 5 Results ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")) by leveraging our proposed data augmentation method (see [Section 3](https://arxiv.org/html/2409.08872v2#S3 "3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") for more details).

While XLSR-300M did not consistently achieve the highest performance across all experimental settings, we selected it as our primary benchmark model. This decision stems from the fact that XLSR-300M is a multilingual model not specifically pre-trained on languages closely related to Amis and Seediq, making it a more generalizable choice for broader low-resource language research where such closely related pre-trained models might not be readily available.

[Fig. 2](https://arxiv.org/html/2409.08872v2#S5.F2 "In 5.1 ASR Results on Amis and Seediq ‣ 5 Results ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") illustrates the impact of data volume and selection strategy on the performance of XLSR-300M after continued pre-training for both Amis and Seediq. We evaluated three data selection approaches: random sampling, Deep SVDD, and our proposed ensemble algorithm ([Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")). As expected, increasing the amount of pre-training data generally leads to improved ASR performance, mitigating the risk of overfitting. Notably, using only $`1`$ hour of data from ML-SUPERB resulted in suboptimal performance across all selection methods, underscoring the importance of sufficient training data volume. Expanding the pre-training data to $`64`$ hours significantly reduced character error rate (CER) for both languages, highlighting the consistent benefit of larger datasets across languages.

Our proposed methods (SVDD and [Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")) consistently outperform the random selection baseline across nearly all experiments. The only exception is noted in the Seediq 1-hour experiments, where our methods demonstrate their effectiveness after selecting $`128`$ hours of non-target language data. Specifically, in both the Seediq 10-minute and 1-hour scenarios with $`128`$ hours of data selection, [Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") consistently yields superior results compared to both random selection and SVDD. In contrast, SVDD performs the best in Amis 10-minute and 1-hour scenarios with $`128`$ hours of data selection. However, increasing the data size to $`128`$ hours yielded only marginal improvements, suggesting that the model might be approaching saturation given the limited representation of the target languages within the available multilingual speech data.

Our findings for Amis reveal that when pre-training data is limited (e.g., $`16`$ hours), utilizing [Algorithm 1](https://arxiv.org/html/2409.08872v2#alg1 "In 3 Method ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages")) for data selection significantly outperforms both random sampling and Deep SVDD, particularly in the 10-minute and 1-hour training scenarios. Moreover, [Fig. 2](https://arxiv.org/html/2409.08872v2#S5.F2 "In 5.1 ASR Results on Amis and Seediq ‣ 5 Results ‣ Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages") demonstrates that the SSL model pre-trained with data selected using our algorithm exhibits greater robustness across almost all experimental conditions than models trained with randomly selected or Deep SVDD-sampled data.

## 6 Conclusions

This study introduces speech corpora for two low-resource Austronesian languages, Amis and Seediq, and presents a data augmentation strategy for enhancing low-resource ASR. We propose leveraging a novel ensemble algorithm to select acoustically similar utterances from a multilingual corpus for continued pre-training of the XLSR-300M model. Our results demonstrate that while the performance improvements are currently modest, the positive correlation between pre-training data volume and ASR accuracy highlights the potential of this approach.

## References

- \[1\] Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar, Yu Zhang, Jiahui Yu, Wei Han, Shibo Wang, Zhengdong Zhang, Yonghui Wu and Ruoming Pang \`\`Conformer: Convolution-augmented transformer for speech recognition'' In _Proc. Interspeech_, 2020
- \[2\] Kwangyoun Kim, Felix Wu, Yifan Peng, Jing Pan, Prashant Sridhar, Kyu J. Han and Shinji Watanabe \`\`E-Branchformer: Branchformer with Enhanced merging for speech recognition'' In _Proc. SLT_, 2022
- \[3\] Steffen Schneider, Alexei Baevski, Ronan Collobert and Michael Auli \`\`Wav2vec: Unsupervised pre-training for speech recognition'' In _Proc. Interspeech_, 2019
- \[4\] Alexei Baevski, Henry Zhou, Abdelrahman Mohamed and Michael Auli \`\`Wav2vec 2.0: A framework for self-supervised learning of speech representations'' In _Proc. NeurIPS_, 2020
- \[5\] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal Lakhotia, Ruslan Salakhutdinov and Abdelrahman Mohamed \`\`HuBERT: self-supervised speech representation learning by masked prediction of hidden units'' In _IEEE/ACM Trans. Audio Speech Lang. Process._ 29, 2021, pp. 3451–3460
- \[6\] Patrick Littell, David R. Mortensen, Ke Lin, Katherine Kairis, Carlisle Turner and Lori Levin \`\`URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors'' In _Proc. EACL_, 2017
- \[7\] Martijn Bartelds, Dan Jurafsky and Martijn Wieling \`\`Making More of Little Data: Improving Low-Resource Automatic Speech Recognition Using Data Augmentation'' In _Proc. ACL_, 2023
- \[8\] Johan Safri, Wawan Sahrozi, Ben Foley, Bradley McDonnell and Dan Jurafsky \`\`Leveraging supplementary text data to kick-start automatic speech recognition system development with limited transcriptions'' In _Proc. the Sixth Workshop on the Use of Computational Methods in the Study of Endangered Languages_, 2023
- \[9\] Alexis Conneau, Alexei Baevski, Ronan Collobert, Abdelrahman Mohamed and Michael Auli \`\`Unsupervised cross-lingual representation learning for speech recognition'' In _Proc. Interspeech_, 2021
- \[10\] Changhan Wang, Morgane Riviere, Ann Lee, Anne Wu, Chaitanya Talnikar, Daniel Haziza, Mary Williamson, Juan Pino and Emmanuel Dupoux \`\`VoxPopuli: A large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation'' In _Proc. ACL_, 2021
- \[11\] Karol Nowakowski, Michal Ptaszynski, Kyoko Murasaki and Jagna Nieuważny \`\`Adapting multilingual speech representation model for a enw, underresourced language through multilingual fine-tuning and continued pretraining'' In _Inf. Process. Manag._ 60.2, 2023, pp. 103148
- \[12\] Nay San, Georgios Paraskevopoulos, Aryaman Arora, Xiluo He, Prabhjot Kaur, Oliver Adams and Dan Jurafsky \`\`Predicting positive transfer for improved low-resource speech recognition using acoustic pseudo-tokens'' In _Proc. SIGTYP_, 2024
- \[13\] Fei Jia, Nithin Rao Koluguri, Jagadeesh Balam and Boris Ginsburg \`\`AmberNet: A compact end-to-end model for spoken language identification'' In _Arxiv preprint arXiv:2210.15781_, 2022
- \[14\] Fei Jia, Nithin Rao Koluguri, Jagadeesh Balam and Boris Ginsburg \`\`A compact end-to-end model with local and global context for spoken language identification'' In _Proc. Interspeech_, 2023
- \[15\] Bernhard Schölkopf, John C. Platt, John Shawe-Taylor, Alex J. Smola and Robert C. Williamson \`\`Estimating the support of a high-dimensional distribution'' In _Neural. Comput._ 13.7, 2001, pp. 1443–1471
- \[16\] Fei Tony Liu, Kai Ming Ting and Zhi-Hua Zhou \`\`Isolation forest'' In _Proc. ICDM_, 2008
- \[17\] Lukas Ruff, Robert Vandermeulen, Nico Goernitz, Lucas Deecke, Shoaib Ahmed Siddiqui, Alexander Binder, Emmanuel Müller and Marius Kloft \`\`Deep one-class classification'' In _Proc. ICML_, 2018
- \[18\] Fei Tony Liu, Kai Ming Ting and Zhi-Hua Zhou \`\`Isolation-based anomaly detection'' In _ACM Trans. Knowl. Discov. Data_ 6.1, 2012, pp. 1–39
- \[19\] Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier and Michael Auli \`\`fairseq: A fast, extensible toolkit for sequence modeling'' In _Proc. NAACL_, 2019
- \[20\] Shinji Watanabe, Takaaki Hori, Shigeki Karita, Tomoki Hayashi, Jiro Nishitoba, Yuya Unno, Nelson Enrique Yalta Soplin, Jahn Heymann, Matthew Wiesner, Nanxin Chen, Adithya Renduchintala and Tsubasa Ochiai \`\`ESPnet: End-to-end speech processing toolkit'' In _Proc. Interspeech_, 2018
- \[21\] Shu-wen Yang, Po-Han Chi, Yung-Sung Chuang, Cheng-I. Lai, Kushal Lakhotia, Yist Y. Lin, Andy T. Liu, Jiatong Shi, Xuankai Chang, Guan-Ting Lin, Tzu-Hsien Huang, Wei-Cheng Tseng, Ko-tik Lee, Da-Rong Liu, Zili Huang, Shuyan Dong, Shang-Wen Li, Shinji Watanabe, Abdelrahman Mohamed and Hung-yi Lee \`\`SUPERB: Speech processing universal performance benchmark'' In _Proc. Interspeech_, 2021
- \[22\] Wei-Ning Hsu, Anuroop Sriram, Alexei Baevski, Tatiana Likhomanenko, Qiantong Xu, Vineel Pratap, Jacob Kahn, Ann Lee, Ronan Collobert, Gabriel Synnaeve and Michael Auli \`\`Robust wav2vec 2.0: Analyzing domain shift in self-supervised pre-training'' In _Proc. Interspeech_, 2021
- \[23\] Binbin Zhang, Hang Lv, Pengcheng Guo, Qijie Shao, Chao Yang, Lei Xie, Xin Xu, Hui Bu, Xiaoyu Chen, Chenchen Zeng, Di Wu and Zhendong Peng \`\`WenetSpeech: A 10000+ hours multi-domain mandarin corpus for speech recognition'' In _Proc. ICASSP_, 2022
- \[24\] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer and Veselin Stoyanov \`\`Unsupervised cross-lingual depresentation learning at scale'' In _Proc. ACL_, 2020
- \[25\] Arun Babu, Changhan Wang, Andros Tjandra, Kushal Lakhotia, Qiantong Xu, Naman Goyal, Kritika Singh, Patrick Platen, Yatharth Saraf, Juan Pino, Alexei Baevski, Alexis Conneau and Michael Auli \`\`XLS-R: Self-supervised cross-lingual speech representation learning at scale'' In _Proc. Interspeech_, 2022
- \[26\] Ann Lee, Hongyu Gong, Paul-Ambroise Duquenne, Holger Schwenk, Peng-Jen Chen, Changhan Wang, Sravya Popuri, Yossi Adi, Juan Pino, Jiatao Gu and Wei-Ning Hsu \`\`Textless speech-to-speech translation on real data'' In _Proc. NAACL_, 2022
- \[27\] Diederik P. Kingma and Jimmy Ba \`\`Adam: A method for stochastic optimization'' In _Proc. ICLR_, 2015
- \[28\] Alex Graves, Santiago Fernandez, Faustino Gomez and Jurgen Schmidhuber \`\`Connectionist temporal classiﬁcation: Labelling unsegmented sequence data with recurrent neural networks'' In _Proc. ICML_, 2006
- \[29\] Daniel S. Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D. Cubuk and Quoc V. Le \`\`SpecAugment: A simple data augmentation method for automatic speech recognition'' In _Proc. Interspeech_, 2019
