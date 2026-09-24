---
arxiv_id: "2510.21014"
title:
  "ReFESS-QI: Reference-Free Evaluation For Speech Separation With Joint Quality
  And Intelligibility Scoring"
authors:
  - Ari Frummer
  - Helin Wang
  - Tianyu Cao
  - Adi Arbel
  - Yuval Sieradzki
  - Oren Gal
  - Jesús Villalba
  - Thomas Thebaud
  - Najim Dehak
submitted: "2025-10-23"
categories:
  - eess.AS
  - cs.SD
arxiv_url: https://arxiv.org/abs/2510.21014
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:35:11+00:00"
references_parsed: 0
arxiv_version: ""
---

# REFESS-QI: REFERENCE-FREE EVALUATION FOR SPEECH SEPARATION WITH JOINT QUALITY AND INTELLIGIBILITY SCORING

###### Abstract

Source separation is a crucial pre-processing step for various speech processing tasks, such as automatic speech recognition (ASR). Traditionally, the evaluation metrics for speech separation rely on the matched reference audios and corresponding transcriptions to assess audio quality and intelligibility. However, they cannot be used to evaluate real-world mixtures for which no reference exists. This paper introduces a text-free reference-free evaluation framework based on self-supervised learning (SSL) representations. The proposed framework utilize the mixture and separated tracks to predict jointly audio quality, through the Scale Invariant Signal to Noise Ratio (SI-SNR) metric, and speech intelligibility through the Word Error Rate (WER) metric. We conducted experiments on the WHAMR! dataset, which shows a WER estimation with a mean absolute error (MAE) of 17% and a Pearson correlation coefficient (PCC) of 0.77; and SI-SNR estimation with an MAE of 1.38 and PCC of 0.95. We further demonstrate the robustness of our estimator by using various SSL representations.

Index Terms—  Speech Separation, Metric Estimation, Automatic Speech Recognition, SSL representations

## 1 Introduction

Humans can concentrate on a particular voice or speech source in noisy surroundings. This phenomenon is known as the ’cocktail party effect’\[[1](https://arxiv.org/html/2510.21014v2#bib.bib1)\]. In speech processing, the corresponding challenge is accurately separating different sound sources from mixed audio signals, a task referred to as speech separation. Speech separation is typically used as a pre-processing step for speech recognition, as it helps to enhance recognition accuracy \[[2](https://arxiv.org/html/2510.21014v2#bib.bib2)\]. In recent years, deep learning models have emerged as highly effective solutions for speech separation \[[3](https://arxiv.org/html/2510.21014v2#bib.bib3), [4](https://arxiv.org/html/2510.21014v2#bib.bib4), [5](https://arxiv.org/html/2510.21014v2#bib.bib5)\], showcasing considerable advancements in performance compared to conventional techniques\[[6](https://arxiv.org/html/2510.21014v2#bib.bib6)\].

The performance of traditional speech separation is typically evaluated using signal-based metrics, such as the SI-SNR. In addition to the signal level metrics, task-oriented evaluations are widely employed to verify that the separated signals remain useful for downstream applications, such as WER for ASR.

Previous techniques have been proposed to estimate SI-SNR in speech separation and serve as baselines in this study \[[7](https://arxiv.org/html/2510.21014v2#bib.bib7)\] \[[8](https://arxiv.org/html/2510.21014v2#bib.bib8)\]. In addition, unsupervised quality estimation for speech enhancement has been explored \[[9](https://arxiv.org/html/2510.21014v2#bib.bib9)\]. This method evaluates a single output of a general enhancement system. Furthermore, a method for predicting the WER for general speech was introduced \[[10](https://arxiv.org/html/2510.21014v2#bib.bib10)\]. However, this method does not specifically predict WER based on learned relationships between representations of noisy audio and enhanced outputs. To the best of our knowledge, this work is the first to predict WER specifically in the context of speech separation.

This paper introduces a novel reference-free model designed to estimate various speech separation metrics called ReFESS-QI, utilizing the Hugging Face Transformers framework for unsupervised evaluation. The network processes audio features from both the mixed input and the separated sources to predict metrics such as SI-SNR and WER in a 3-dimensional forward pass. This model outperforms existing SI-SNR estimators and achieves comparable WER baselines without relying on text hypotheses obtained from an ASR model.

The key contributions of this paper are as follows: We introduce the first text-free, reference-free WER estimator for speech-separated signals, We leverage self-supervised learning representations (SSLR) to create an improved SI-SNR estimator compared to existing baselines, We generalize our findings by training a set of joint estimators that predict WER and SISNR, indicating that this method can predict joint quality and Intelligibility scores.

## 2 Related Works

### 2.1 Speech Separation

In speech separation, the goal is to extract each speaker’s utterance into a dedicated output channel. Given a mixture

```math
y\in\mathbb{R}^{N},\qquad y=\sum_{k=1}^{K}s_{k}+n
```

We seek to estimate the individual source signals.

```math
s_{k}\in\mathbb{R}^{N},\qquad k=1,\dots,K
```

where $`n\in\mathbb{R}^{N}`$ represents background noise and $`N`$ is the number of time samples. This paper focuses on the two-speaker scenario, i.e., $`K=2`$.

Several models have been proposed to address the phenomenon of speech separation, utilizing diverse architectures and techniques. These include DPRNN, which leverages recurrent neural networks for long-sequence modeling, TasNet, based on an encoder–decoder framework, and SepFormer, which utilizes transformers\[[3](https://arxiv.org/html/2510.21014v2#bib.bib3), [4](https://arxiv.org/html/2510.21014v2#bib.bib4), [5](https://arxiv.org/html/2510.21014v2#bib.bib5)\].

### 2.2 Speech Separation Metrics

Speech-separation performance can be evaluated with generic signal-based metrics, such as the Signal-to-Noise Ratio (SI-SNR) and the Perceptual Evaluation of Speech Quality (PESQ)\[[11](https://arxiv.org/html/2510.21014v2#bib.bib11)\], or with specialized downstream application-related metrics, such as the WER for ASR.

Signal-based metrics are computed directly from the waveform by comparing with a reference. SI-SNR is estimated directly from the signal while PESQ is model-based, comparing the clean and processed signals with the aid of a built-in perceptual model to estimate perceived speech quality.

By opposition, the WER metric is measured for a given ASR system, by comparing the output of the ASR with a text reference, where the proportion of insertions, deletions, and substitutions required to align the recognized text with the reference quantifies the impact of separation on recognition performance.

### 2.3 Metrics estimators

Here we go through three related metric estimators baselines. In the SI-SNR baseline \[[8](https://arxiv.org/html/2510.21014v2#bib.bib8)\], an approach utilizing SSLR models to predict SI-SNR was introduced. This method concatenated temporally the mixture and the two separate audio tracks before feeding them in to the SSLR’s feature extractor. In contrast, our method extracts features from each audio track separately and learns the relationships between the representations in each time bin before making predictions about the metric. Moreover, the baseline is dependent on fine-tuning of the entire SSL model, which consists of millions of parameters, whereas our method does not require full fine-tuning. This allows us to preserve the knowledge from unsupervised training while only requiring light training.

The WER baseline \[[9](https://arxiv.org/html/2510.21014v2#bib.bib9)\] is a method that utilizes both audio and text features from the ASR hypothesis. These features are fed into the MLP head that predicts a WER estimate for a single audio. This cascade approach presents efficiency and accuracy issues. The chaining of the results of the ASR model to the text embedding model is one point of failure when the ASR input is not accurate, and the inference of the three models is considered a heavy task.

Uni-VERSA \[[9](https://arxiv.org/html/2510.21014v2#bib.bib9)\] is a unified network that simultaneously predicts various objective metrics. This framework offers an efficient assessment of speech enhancement across multiple evaluation metrics. However, Uni-VERSA has been optimized for speech enhancement, considering only one audio channel, which is not adapted to the needs of a speech separation task, containing by definition 2+ output channels.

![Refer to caption](https://arxiv.org/html/powerpoint_image1.png)

Fig. 1: Left: Dataset Building Method. Right: Metric-estimator model’s architecture, based on Semi-Supervised Learning Representations (SSLR), followed by a concatenation, a Transformer encoder layer, and a linear layer.

| Dataset | Split | Total Dur. (h) | Avg Dur. (S) | \#Seg   | Avg \#WRD | Avg WER | Std. Dev of WER |
| ------- | ----- | -------------- | ------------ | ------- | --------- | ------- | --------------- |
| REAL-M  | Test  | 1.3            | 5.17         | 924     | 11.2      | 49.99%  | 31.17%          |
| WHAMR!  | Test  | 8.2            | 10.7         | 2,750   | 16.36     | 49.36%  | 20.38%          |
| WHAMR!  | Train | 402.7          | 10.36        | 140,000 | 16.41     | 49.84%  | 31.05%          |

Table 1: Distribution of the data-set splits of the WHAMR! separated tracks. ASR generated with Whisper large-V3.

## 3 Methods

This section describes our automatic WER estimator method, as well as its extensions as an SI-SNR estimator and a joint estimator, applied to speech separation. First, we used multiple speech separation systems to extract pairs of separated audios from mixtures. Second, we compute the metrics from the extracted audios. The SI-SNR is computed directly and the WER from Whisper V3-Large \[[12](https://arxiv.org/html/2510.21014v2#bib.bib12)\] predictions, using the Nemo toolkit\[[13](https://arxiv.org/html/2510.21014v2#bib.bib13)\] for text normalization. Third, the metric estimator model is trained on the triplets of audio (mixture and 2 outputs) to predict the corresponding metrics.

### 3.1 Speech separation systems

To diversify our training set, three different source separation models are used: TasNet\[[3](https://arxiv.org/html/2510.21014v2#bib.bib3)\] using espnet\[[14](https://arxiv.org/html/2510.21014v2#bib.bib14)\], DPRNN\[[4](https://arxiv.org/html/2510.21014v2#bib.bib4)\], and SepFormer\[[5](https://arxiv.org/html/2510.21014v2#bib.bib5)\] using speechbrain \[[15](https://arxiv.org/html/2510.21014v2#bib.bib15)\]. Each separator is trained on the reverberant WHAMR! Dataset\[[16](https://arxiv.org/html/2510.21014v2#bib.bib16)\] to perform two-speaker separation and de-reverberation.

### 3.2 Metric estimator Architecture

The estimator model performs multi-output regression to estimate a target metric, depending on the training task. It uses a SSL encoder \[[17](https://arxiv.org/html/2510.21014v2#bib.bib17), [18](https://arxiv.org/html/2510.21014v2#bib.bib18), [19](https://arxiv.org/html/2510.21014v2#bib.bib19)\] to extract $`T`$ features of dimension $`D_{SSL}`$ from the mixture $`Y`$ and the two separated tracks $`\hat{S_{1}}`$ and $`\hat{S_{2}}`$, then concatenates the features along the feature axis and outputs an array of size $`(T,3\times D_{SSL})`$. Then, the array is processed by a transformer encoder layer, mean pooled across the time dimension, followed by a linear layer, to predict three continuous values: metric value for source 1, source 2, and their average. The model is trained with a mean squared error (MSE) loss and is evaluated using MAE, and Pearson’s correlation. This architecture supports reference-free estimation for any signal-level metrics or downstream model value.

### 3.3 Metric estimator training setup

During training, the entire network undergoes a 10,000 step warm-up period. Following the warm-up, two different learning rate schedulers are implemented to prevent overfitting. The Self-Supervised Learning model is trained using a linearly decreasing learning rate, starting at 1e-5. Meanwhile, the parameters that are trained from scratch begin with a learning rate of 1e-4 after the warm-up stage, following the same linear decreasing schedule. An Adam optimizer is used, with a batch size of 12.

## 4 Experiments

### 4.1 Datasets

We use the reverberant max version of WHAMR! \[[16](https://arxiv.org/html/2510.21014v2#bib.bib16)\] which is a far-field speech separation corpus designed to simulate real-world noisy and reverberant conditions. Each mixture comprises two overlapping speakers with additive environmental noise and reverberation applied through simulated room impulse responses. Additionaly, we use REAL-M\[[7](https://arxiv.org/html/2510.21014v2#bib.bib7)\], a real-life speech source separation dataset for two-speaker mixtures.

The WHAMR! train and validation splits were used to train and validate both the speech separation models and the metric estimators. The performances of our models were evaluated on the WHAMR! test split and the Real M dataset

We use the SS systems to create a dataset of Metrics. To ensure a balanced label distribution, we selected three checkpoints from the beginning, middle, and end epochs for dataset generation. ASR was calculated using Whisper V3-Large\[[12](https://arxiv.org/html/2510.21014v2#bib.bib12)\], and text normalization was carried out with the NeMo toolkit\[[13](https://arxiv.org/html/2510.21014v2#bib.bib13)\]. Additionally, the SISNR was computed using only the reference audio. The distribution of the dataset is described in Table I and Figure 2.

![Refer to caption](https://arxiv.org/html/wer_percentage_bins_bar_plot.png)

Fig. 2: Average WER BIN distribution (percentage) for each mixture across dataset splits

### 4.2 Metric Estimators Training

#### 4.2.1 Single metric estimators training

For each sample, the input to the estimator comprised three-channel audio, consisting of the mixture signal along with the two separated sources. Metric scores, computed using ground-truth references, were employed as regression targets. Initially, estimators were trained separately for the SI-SNR and WER prediction tasks, following the same architecture and data processing pipeline outlined in Section [3.2](https://arxiv.org/html/2510.21014v2#S3.SS2 "3.2 Metric estimator Architecture ‣ 3 Methods ‣ REFESS-QI: REFERENCE-FREE EVALUATION FOR SPEECH SEPARATION WITH JOINT QUALITY AND INTELLIGIBILITY SCORING").

#### 4.2.2 Joint estimators training

In another experiment, we jointly estimated SI-SNR, and WER. To stabilize the training process and ensure consistent scaling across data samples, all labels were min-max normalized to fall within the range of $`[0,1]`$. This normalization was applied globally, utilizing the minimum and maximum values observed in both the training and validation sets.

#### 4.2.3 Ablation Studies

Our ablation study considered three state-of-the-art self-supervised speech models as feature extractors for metric estimation: Wav2Vec 2.0\[[17](https://arxiv.org/html/2510.21014v2#bib.bib17)\], WavLM\[[18](https://arxiv.org/html/2510.21014v2#bib.bib18)\], and HuBERT\[[19](https://arxiv.org/html/2510.21014v2#bib.bib19)\]. We conduct experiments with a trainable and frozen FE.

### 4.3 Generalization to New Data

To assess generalization, we evaluated the trained WER estimator on the REAL-M data set \[[7](https://arxiv.org/html/2510.21014v2#bib.bib7)\], which is a real mixture data set that contains reverberation and noise. REAL-M is for evaluation only, and therefore will be separated using our pretrained models on WHAMR!.

|                                                         |                |       |          |            |      |      |       |       |
| ------------------------------------------------------- | -------------- | ----- | -------- | ---------- | ---- | ---- | ----- | ----- |
| Models                                                  | FE             | FE TR | Test set | Head       | PCC  | MAE  | A.PCC | A.MAE |
| \[[10](https://arxiv.org/html/2510.21014v2#bib.bib10)\] | HuBERT+RoBERTa | ✗     | WHAMR!   | MLP        | .746 | .15  | -     | -     |
| Ours                                                    | W2V2           | ✓     |          | Tr. + Lin. | .762 | 0.19 | .808  | 0.17  |
| Ours                                                    | Hubert         | ✓     |          | Tr. + Lin. | .775 | .17  | .824  | 0.14  |
| Ours                                                    | Hubert         | ✗     |          | Tr. + Lin. | .701 | .21  | .755  | 0.17  |
| Ours                                                    | WavLM          | ✓     |          | Tr. + Lin. | .775 | .17  | .823  | 0.14  |
| Joint                                                   | Hubert         | ✓     |          | Tr. + Lin. | .769 | .17  | .819  | 0.14  |
| \[[10](https://arxiv.org/html/2510.21014v2#bib.bib10)\] | HuBERT+RoBERTa | ✗     | REAL-M   | MLP        | .413 | .28  | -     | -     |
| Ours                                                    | Hubert         | ✓     |          | Tr. + Lin. | .547 | .22  | .510  | 0.22  |
| Joint                                                   | Hubert         | ✓     |          |            | .548 | .25  | .513  | 0.21  |

Table 2: Pearson’s correlation (PCC) and mean-absolute error (MAE) for the single and average WER estimators, for multiple Feature Extractors (FE) with FE trainable or frozen, tested on the WHAMR! dataset.

## 5 Results

### 5.1 WER estimator

In terms of WER estimation, Table [2](https://arxiv.org/html/2510.21014v2#S4.T2 "Table 2 ‣ 4.3 Generalization to New Data ‣ 4 Experiments ‣ REFESS-QI: REFERENCE-FREE EVALUATION FOR SPEECH SEPARATION WITH JOINT QUALITY AND INTELLIGIBILITY SCORING") shows that our method that lightly trains the FE achieves better results than the baseline without using the Text hypothesis. Our method achieves an MAE of 0.17 and a PCC of 0.775 for the single metrics estimation, and an MAE of 0.14 and PCC of 0.824 for the average metrics estimation, while the baseline achieves an MAE of 0.15 and PCC of 0.746 using an additional ASR model and text embedder for the evaluation. Moreover, our estimation method with freezing the FE achieves competitive results to the baseline, which also uses frozen models, but more pretrained models in inference. We achieve our best results by utilizing Hubert representations. In the generalization experiment using new data from the Real-M dataset, our method exceeded the baseline across all metrics.

### 5.2 SI-SNR estimator

For the SI-SNR estimation task, Table [3](https://arxiv.org/html/2510.21014v2#S6.T3 "Table 3 ‣ 6 Conclusion ‣ REFESS-QI: REFERENCE-FREE EVALUATION FOR SPEECH SEPARATION WITH JOINT QUALITY AND INTELLIGIBILITY SCORING") shows that our method performs better than the SOTA baseline. For all the SSLRs, our methods perform better in terms of PCC and MAE. Even when using frozen SSL representations, our method outperforms the baseline, which was using a pre-trained SSL extractor, on both MAE and PCC. Our best performances are obtained using WavLM representations.

### 5.3 Joint estimators

The experiments in Table [1](https://arxiv.org/html/2510.21014v2#S2.T1 "Table 1 ‣ 2.3 Metrics estimators ‣ 2 Related Works ‣ REFESS-QI: REFERENCE-FREE EVALUATION FOR SPEECH SEPARATION WITH JOINT QUALITY AND INTELLIGIBILITY SCORING") show that this method can predict more than one metric. In terms of WER, that joint estimator achieves similar results than the single metrics estimator, both on the WHAMR! test set and the REAL-M datasets.

For the out-of-domain evaluation (REAL-M), the WER estimator achieves an MAE of 0.25 and a PCC of 0.548.

## 6 Conclusion

This paper presents a novel text-free reference-free model designed to estimate separately two metrics: WER and SI-SNR from the outputs of a speech separation system. We proposed a new architecture leveraging self-supervised learning representations that outperformed significantly previous baselines without text nor audio references. We craft our own training dataset from WHAMR! and three different speech separation systems, designed to offer a balanced distribution of WER and SISNR metrics, then train and evaluate our proposed framework on it. The proposed framework demonstrates state of the art performances with different SSL representations, with and without finetuning of the encoder. Furthermore, we show our model can generalize to real mixtures when evaluated on the REAL-M dataset, and can work to estimate jointly both the WER and the SI-SNR.

|                                                               |        |       |            |      |       |       |       |
| ------------------------------------------------------------- | ------ | ----- | ---------- | ---- | ----- | ----- | ----- |
| Model                                                         | FE     | FE TR | Head       | PCC  | MAE   | A.PCC | A.MAE |
| Baseline\[[8](https://arxiv.org/html/2510.21014v2#bib.bib8)\] | W2V2   | ✓     | MLP        | .817 | 2.01  | .916  | 1.70  |
| Baseline\[[8](https://arxiv.org/html/2510.21014v2#bib.bib8)\] | WavLM  | ✓     |            | .823 | 1.616 | .922  | 1.14  |
| Baseline\[[8](https://arxiv.org/html/2510.21014v2#bib.bib8)\] | HuBERT | ✓     |            | .823 | 1.937 | .922  | 1.63  |
| Ours                                                          | W2V2   | ✓     | Tr. + Lin. | .947 | 1.475 | .952  | 1.44  |
| Ours                                                          | WavLM  | ✓     |            | .951 | 1.388 | .956  | 1.34  |
| Ours                                                          | HuBERT | ✓     |            | .949 | 1.474 | .955  | 1.446 |
| Ours                                                          | HuBERT | ✗     |            | .936 | 1.459 | .943  | 1.400 |

Table 3: Pearson’s correlation (PCC) and mean-absolute error (MAE) for single and average SI-SNR estimation, for multiple Feature Extractors (FE), with FE trainable or frozen, tested on the WHAMR! dataset.

This work has certain limitations, on the speech separation systems, the evaluation data and the applications. First, our proposed model used the same dataset to train as the speech separation models (the WHAMR! set), and the same set of speech separation models was used to generate the training and the testing data, limiting the potential generalization on new speech separation systems. Second, we adopted a uniform distribution of the scores in the training data, which may not be best suited to align with the out-of-domain data, and we use a unique model to extract all transcripts for the WER evaluation (Whisper). Finally, the proposed metric estimator is based on self-supervised learning (SSL) systems, which typically requires large GPUs for inference, thus it will not be easy to use during training, only for evaluation.

Future work could explore the possibility of incorporating this estimator as a tool to guide unsupervised speech separation techniques during their training or their evaluation. To improve the usability of this technique, we will use pruning and distillation techniques to reduce the size of the estimator, making it more fit for end to end training of larger speech separation systems without drastically increasing the required size of GPUs.

## References

- \[1\] Haykin, Simon, Chen, and Zhe, “The cocktail party problem,” Neural Computation, vol. 17, no. 9, pp. 1875–1902, 2005.
- \[2\] Cherry and E. Colin, “Some experiments on the recognition of speech, with one, with two ears,” The Journal of the Acoustical Society of America, vol. 25, no. 5, pp. 975–979, 1953.
- \[3\] Luo, Yi, Mesgarani, and Nima, “Tasnet: Time-domain audio separation network for real-time, single-channel speech separation,” in Proceedings of the IEEE International Conference on Acoustics and Speech, Signal Processing (ICASSP), 2018, arXiv:1711.00541.
- \[4\] Luo, Yi, Chen, Zhuo, Yoshioka, and Takuya, “Dual-path rnn: Efficient long sequence modeling for time-domain single-channel speech separation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 46–50.
- \[5\] Subakan, Cem, Ravanelli, Mirco, Cornell, Samuele, Bronzi, Mirko, Zhong, and Jianyuan, “Attention is all you need in speech separation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2021.
- \[6\] Wang, DeLiang, Chen, and Jitong, “Supervised speech separation based on deep learning: An overview,” IEEE/ACM Transactions on Audio, Speech and and Language Processing, vol. 26, no. 10, pp. 1702–1726, 2018.
- \[7\] Subakan, Cem, Ravanelli, Mirco, Cornell, Samuele, Grondin, and François, “Real-m: Towards speech separation on real mixtures,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022.
- \[8\] Dang, Shaoxiang, Matsumoto, Tetsuya, Takeuchi, Yoshinori, Kudo, and Hiroaki, “Using semi-supervised learning for monaural time-domain speech separation with a self-supervised learning-based si-snr estimator,” in Proceedings of Interspeech, 2023.
- \[9\] Shi, Jiatong, Shim, Hye-Jin, Watanabe, and Shinji, “Uni-versa: Versatile speech assessment with a unified network,” in Proceedings of Interspeech, 2025.
- \[10\] Park, Chanho, Lu, Chengsong, Chen, Mingjie, Hain, and Thomas, “Fast word error rate estimation using self-supervised representations for speech and text,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025.
- \[11\] Rix, Antony W., Beerends, John G., Hollier, Michael P., Hekstra, and Andries P., “Perceptual evaluation of speech quality (pesq) – a new method for speech quality assessment of telephone networks, codecs,” in Proceedings of the IEEE International Conference on Acoustics, Speech, Signal Processing (ICASSP), 2001, pp. 749–752.
- \[12\] Radford, Alec, Kim, Jong Wook, Xu, Tao, Brockman, Greg, McLeavey, Christine, Sutskever, and Ilya, “Robust speech recognition via large-scale weak supervision,” in Proceedings of the 40th International Conference on Machine Learning (ICML), 2023, vol. 202 of Proceedings of Machine Learning Research, pp. 28492–28518.
- \[13\] Kuchaiev, Oleksii, Li, Jason, Nguyen, Huyen, Hrinchuk, Oleksii, Leary, Ryan, Ginsburg, Boris, and et al., “Nemo: a toolkit for building ai applications using neural modules,” arXiv preprint arXiv:1909.09577, 2019.
- \[14\] S. Watanabe, T. Hori, S. Karita, T. Hayashi, J. Nishitoba, Y. Unno, N. E. Y. Soplin, J. Heymann, M. Wiesner, and N. Chen et al., ““espnet:end-to-end speech processing toolkit”,” Proc. Interspeech, 2018.
- \[15\] Mirco Ravanelli, Titouan Parcollet, Peter Plantinga, Aku Rouhe, Samuele Cornell, Loren Lugosch, Cem Subakan, Nauman Dawalatabad, Abdelwahab Heba, Jianyuan Zhong, Ju-Chieh Chou, Sung-Lin Yeh, Szu-Wei Fu, Chien-Feng Liao, Elena Rastorgueva, François Grondin, William Aris, Hwidong Na, Yan Gao, Renato De Mori, and Yoshua Bengio., “”speechbrain: A general-purpose speech toolkit”,” arXiv preprint arXiv:2106.04624 and 2021. \[228\] A. Renduchintala and S. Ding, 2021.
- \[16\] Maciejewski, Matthew, Wichern, Gordon, McQuinn, Emmett, Le Roux, and Jonathan, “Whamr​: Noisy and reverberant single-channel speech separation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020.
- \[17\] Baevski, Alexei, Zhou, Yuhao, Mohamed, Abdelrahman, Auli, and Michael, “wav2vec 2.0: A framework for self-supervised learning of speech representations,” in Advances in Neural Information Processing Systems (NeurIPS), 2020, vol. 33, pp. 12449–12460.
- \[18\] Chen, Sanyuan, Wang, Chengyi, Chen, Zheng, Wu, Yu, Liu, Shujie, Chen, Zhuo, Li, Jinyu, Kanda, Naoyuki, Yoshioka, Takuya, Xiao, Xiong, Wu, Jue, Zhou, Long, Ren, Shuo, Qian, Yao, Qian, Yan, Wu, Jian, Zeng, Ming, Yu, Xian, Wei, and Furu, “Wavlm: Large-scale self-supervised pre-training for full stack speech processing,” IEEE Journal of Selected Topics in Signal Processing, vol. 16, no. 6, pp. 1505–1518, 2022.
- \[19\] Hsu, Wei-Ning, Bolte, Benjamin, Tsai, Yao-Hung Hubert, Lakhotia, Kushal, Salakhutdinov, Ruslan, Mohamed, and Abdelrahman, “Hubert: Self-supervised speech representation learning by masked prediction of hidden units,” IEEE/ACM Transactions on Audio, Speech and and Language Processing, vol. 29, pp. 3451–3460, 2021.
