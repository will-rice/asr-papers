# 2022

658 papers in this year.

### [Memory Augmented Lookup Dictionary based Language Modeling for Automatic Speech Recognition](2301.00066.md)
**Yukun Feng, Ming Tu, Rui Xia, Chuanzeng Huang et al.** · 2022-12-30

<details>
<summary>Abstract</summary>

Recent studies have shown that using an external Language Model (LM) benefits the end-to-end Automatic Speech Recognition (ASR). However, predicting tokens that appear less frequently in the training set is still quite challenging. The long-tail prediction problems have been widely studied in many applications, but only been addressed by a few studies for ASR and LMs. In this paper, we propose a new memory augmented lookup dictionary based Transformer architecture for LM. The newly introduced lookup dictionary incorporates rich contextual information in training set, which is vital to correctly predict long-tail tokens. With intensive experiments on Chinese and English data sets, our proposed method is proved to outperform the baseline Transformer LM by a great margin on both word/character error rate and tail tokens error rate. This is achieved without impact on the decoding efficiency. Overall, we demonstrate the effectiveness of our proposed method in boosting the ASR decoding performance, especially for long-tail tokens.

</details>

### [Macro-block dropout for improved regularization in training end-to-end speech recognition models](2212.14149.md)
**Chanwoo Kim, Sathish Indurti, Jinhwan Park, Wonyong Sung** · 2022-12-29

<details>
<summary>Abstract</summary>

This paper proposes a new regularization algorithm referred to as macro-block dropout. The overfitting issue has been a difficult problem in training large neural network models. The dropout technique has proven to be simple yet very effective for regularization by preventing complex co-adaptations during training. In our work, we define a macro-block that contains a large number of units from the input to a Recurrent Neural Network (RNN). Rather than applying dropout to each unit, we apply random dropout to each macro-block. This algorithm has the effect of applying different drop out rates for each layer even if we keep a constant average dropout rate, which has better regularization effects. In our experiments using Recurrent Neural Network-Transducer (RNN-T), this algorithm shows relatively 4.30 % and 6.13 % Word Error Rates (WERs) improvement over the conventional dropout on LibriSpeech test-clean and test-other. With an Attention-based Encoder-Decoder (AED) model, this algorithm shows relatively 4.36 % and 5.85 % WERs improvement over the conventional dropout on the same test sets.

</details>

### [Learning to Detect Noisy Labels Using Model-Based Features](2212.13767.md)
**Zhihao Wang, Zongyu Lin, Peiqi Liu, Guidong ZHeng et al.** · 2022-12-28

<details>
<summary>Abstract</summary>

Label noise is ubiquitous in various machine learning scenarios such as self-labeling with model predictions and erroneous data annotation. Many existing approaches are based on heuristics such as sample losses, which might not be flexible enough to achieve optimal solutions. Meta learning based methods address this issue by learning a data selection function, but can be hard to optimize. In light of these pros and cons, we propose Selection-Enhanced Noisy label Training (SENT) that does not rely on meta learning while having the flexibility of being data-driven. SENT transfers the noise distribution to a clean set and trains a model to distinguish noisy labels from clean ones using model-based features. Empirically, on a wide range of tasks including text classification and speech recognition, SENT improves performance over strong baselines under the settings of self-training and label corruption.

</details>

### [Don't Be So Sure! Boosting ASR Decoding via Confidence Relaxation](2212.13378.md)
**Tomer Wullach, Shlomo E. Chazan** · 2022-12-27

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems frequently use a search-based decoding strategy aiming to find the best attainable transcript by considering multiple candidates. One prominent speech recognition decoding heuristic is beam search, which seeks the transcript with the greatest likelihood computed using the predicted distribution. While showing substantial performance gains in various tasks, beam search loses some of its effectiveness when the predicted probabilities are highly confident, i.e., the predicted distribution is massed for a single or very few classes. We show that recently proposed Self-Supervised Learning (SSL)-based ASR models tend to yield exceptionally confident predictions that may hamper beam search from truly considering a diverse set of candidates. We perform a layer analysis to reveal and visualize how predictions evolve, and propose a decoding procedure that improves the performance of fine-tuned ASR models. Our proposed approach does not require further training beyond the original fine-tuning, nor additional model parameters. In fact, we find that our proposed method requires significantly less inference computation than current approaches. We propose aggregating the top M layers, potentially leveraging useful information encoded in intermediate layers, and relaxing model confidence. We demonstrate the effectiveness of our approach by conducting an empirical study on varying amounts of labeled resources and different model sizes, showing consistent improvements in particular when applied to low-resource scenarios.

</details>

### [Skit-S2I: An Indian Accented Speech to Intent dataset](2212.13015.md)
**Shangeth Rajaa, Swaraj Dalmia, Kumarmanas Nethil** · 2022-12-26

<details>
<summary>Abstract</summary>

Conventional conversation assistants extract text transcripts from the speech signal using automatic speech recognition (ASR) and then predict intent from the transcriptions. Using end-to-end spoken language understanding (SLU), the intents of the speaker are predicted directly from the speech signal without requiring intermediate text transcripts. As a result, the model can optimize directly for intent classification and avoid cascading errors from ASR. The end-to-end SLU system also helps in reducing the latency of the intent prediction model. Although many datasets are available publicly for text-to-intent tasks, the availability of labeled speech-to-intent datasets is limited, and there are no datasets available in the Indian accent. In this paper, we release the Skit-S2I dataset, the first publicly available Indian-accented SLU dataset in the banking domain in a conversational tonality. We experiment with multiple baselines, compare different pretrained speech encoder's representations, and find that SSL pretrained representations perform slightly better than ASR pretrained representations lacking prosodic features for speech-to-intent classification. The dataset and baseline code is available at \url{https://github.com/skit-ai/speech-to-intent-dataset}

</details>

### [Technical Evaluation of HoloLens for Multimedia: A First Look](2212.12907.md)
**Yang Liu, Haiwei Dong, Longyu Zhang, Abdulmotaleb El Saddik** · 2022-12-25

<details>
<summary>Abstract</summary>

A recently released cutting-edge AR device, Microsoft HoloLens, has attracted considerable attention with its advanced capabilities. In this article, we report the design and execution of a series of experiments to quantitatively evaluate HoloLens' performance in head localization, real environment reconstruction, spatial mapping, hologram visualization, and speech recognition.

</details>

### [ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Enhancement](2212.11377.md)
**Wei-Ning Hsu, Tal Remez, Bowen Shi, Jacob Donley et al.** · 2022-12-21

<details>
<summary>Abstract</summary>

Prior works on improving speech quality with visual input typically study each type of auditory distortion separately (e.g., separation, inpainting, video-to-speech) and present tailored algorithms. This paper proposes to unify these subjects and study Generalized Speech Enhancement, where the goal is not to reconstruct the exact reference clean signal, but to focus on improving certain aspects of speech. In particular, this paper concerns intelligibility, quality, and video synchronization. We cast the problem as audio-visual speech resynthesis, which is composed of two steps: pseudo audio-visual speech recognition (P-AVSR) and pseudo text-to-speech synthesis (P-TTS). P-AVSR and P-TTS are connected by discrete units derived from a self-supervised speech model. Moreover, we utilize self-supervised audio-visual speech model to initialize P-AVSR. The proposed model is coined ReVISE. ReVISE is the first high-quality model for in-the-wild video-to-speech synthesis and achieves superior performance on all LRS3 audio-visual enhancement tasks with a single model. To demonstrates its applicability in the real world, ReVISE is also evaluated on EasyCom, an audio-visual benchmark collected under challenging acoustic conditions with only 1.6 hours of training data. Similarly, ReVISE greatly suppresses noise and improves quality. Project page: https://wnhsu.github.io/ReVISE.

</details>

### [End-to-End Automatic Speech Recognition model for the Sudanese Dialect](2212.10826.md)
**Ayman Mansour, Wafaa F. Mukhtar** · 2022-12-21

<details>
<summary>Abstract</summary>

Designing a natural voice interface rely mostly on Speech recognition for interaction between human and their modern digital life equipment. In addition, speech recognition narrows the gap between monolingual individuals to better exchange communication. However, the field lacks wide support for several universal languages and their dialects, while most of the daily conversations are carried out using them. This paper comes to inspect the viability of designing an Automatic Speech Recognition model for the Sudanese dialect, which is one of the Arabic Language dialects, and its complexity is a product of historical and social conditions unique to its speakers. This condition is reflected in both the form and content of the dialect, so this paper gives an overview of the Sudanese dialect and the tasks of collecting represented resources and pre-processing performed to construct a modest dataset to overcome the lack of annotated data. Also proposed end- to-end speech recognition model, the design of the model was formed using Convolution Neural Networks. The Sudanese dialect dataset would be a stepping stone to enable future Natural Language Processing research targeting the dialect. The designed model provided some insights into the current recognition task and reached an average Label Error Rate of 73.67%.

</details>

### [4D ASR: Joint modeling of CTC, Attention, Transducer, and Mask-Predict decoders](2212.10818.md)
**Yui Sudo, Muhammad Shakeel, Brian Yan, Jiatong Shi et al.** · 2022-12-21

<details>
<summary>Abstract</summary>

The network architecture of end-to-end (E2E) automatic speech recognition (ASR) can be classified into several models, including connectionist temporal classification (CTC), recurrent neural network transducer (RNN-T), attention mechanism, and non-autoregressive mask-predict models. Since each of these network architectures has pros and cons, a typical use case is to switch these separate models depending on the application requirement, resulting in the increased overhead of maintaining all models. Several methods for integrating two of these complementary models to mitigate the overhead issue have been proposed; however, if we integrate more models, we will further benefit from these complementary models and realize broader applications with a single system. This paper proposes four-decoder joint modeling (4D) of CTC, attention, RNN-T, and mask-predict, which has the following three advantages: 1) The four decoders are jointly trained so that they can be easily switched depending on the application scenarios. 2) Joint training may bring model regularization and improve the model robustness thanks to their complementary properties. 3) Novel one-pass joint decoding methods using CTC, attention, and RNN-T further improves the performance. The experimental results showed that the proposed model consistently reduced the WER.

</details>

### [SLUE Phase-2: A Benchmark Suite of Diverse Spoken Language Understanding Tasks](2212.10525.md)
**Suwon Shon, Siddhant Arora, Chyi-Jiunn Lin, Ankita Pasad et al.** · 2022-12-20

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) tasks have been studied for many decades in the speech research community, but have not received as much attention as lower-level tasks like speech and speaker recognition. In particular, there are not nearly as many SLU task benchmarks, and many of the existing ones use data that is not freely available to all researchers. Recent work has begun to introduce such benchmark datasets for several tasks. In this work, we introduce several new annotated SLU benchmark tasks based on freely available speech data, which complement existing benchmarks and address gaps in the SLU evaluation landscape. We contribute four tasks: question answering and summarization involve inference over longer speech sequences; named entity localization addresses the speech-specific task of locating the targeted content in the signal; dialog act classification identifies the function of a given speech utterance. We follow the blueprint of the Spoken Language Understanding Evaluation (SLUE) benchmark suite. In order to facilitate the development of SLU models that leverage the success of pre-trained speech representations, we will be publishing for each task (i) annotations for a relatively small fine-tuning set, (ii) annotated development and test sets, and (iii) baseline models for easy reproducibility and comparisons. In this work, we present the details of data collection and annotation and the performance of the baseline models. We also perform sensitivity analysis of pipeline models' performance (speech recognizer + text model) to the speech recognition accuracy, using more than 20 state-of-the-art speech recognition models.

</details>

### [Mu$^{2}$SLAM: Multitask, Multilingual Speech and Language Models](2212.09553.md)
**Yong Cheng, Yu Zhang, Melvin Johnson, Wolfgang Macherey et al.** · 2022-12-19

<details>
<summary>Abstract</summary>

We present Mu$^{2}$SLAM, a multilingual sequence-to-sequence model pre-trained jointly on unlabeled speech, unlabeled text and supervised data spanning Automatic Speech Recognition (ASR), Automatic Speech Translation (AST) and Machine Translation (MT), in over 100 languages. By leveraging a quantized representation of speech as a target, Mu$^{2}$SLAM trains the speech-text models with a sequence-to-sequence masked denoising objective similar to T5 on the decoder and a masked language modeling (MLM) objective on the encoder, for both unlabeled speech and text, while utilizing the supervised tasks to improve cross-lingual and cross-modal representation alignment within the model. On CoVoST AST, Mu$^{2}$SLAM establishes a new state-of-the-art for models trained on public datasets, improving on xx-en translation over the previous best by 1.9 BLEU points and on en-xx translation by 1.1 BLEU points. On Voxpopuli ASR, our model matches the performance of an mSLAM model fine-tuned with an RNN-T decoder, despite using a relatively weaker sequence-to-sequence architecture. On text understanding tasks, our model improves by more than 6\% over mSLAM on XNLI, getting closer to the performance of mT5 models of comparable capacity on XNLI and TydiQA, paving the way towards a single model for all speech and text understanding tasks.

</details>

### [WACO: Word-Aligned Contrastive Learning for Speech Translation](2212.09359.md)
**Siqi Ouyang, Rong Ye, Lei Li** · 2022-12-19

<details>
<summary>Abstract</summary>

End-to-end Speech Translation (E2E ST) aims to directly translate source speech into target text. Existing ST methods perform poorly when only extremely small speech-text data are available for training. We observe that an ST model's performance closely correlates with its embedding similarity between speech and source transcript. In this paper, we propose Word-Aligned COntrastive learning (WACO), a simple and effective method for extremely low-resource speech-to-text translation. Our key idea is bridging word-level representations for both speech and text modalities via contrastive learning. We evaluate WACO and other methods on the MuST-C dataset, a widely used ST benchmark, and on a low-resource direction Maltese-English from IWSLT 2023. Our experiments demonstrate that WACO outperforms the best baseline by 9+ BLEU points with only 1-hour parallel ST data. Code is available at https://github.com/owaski/WACO.

</details>

### [AdaTranS: Adapting with Boundary-based Shrinking for End-to-End Speech Translation](2212.08911.md)
**Xingshan Zeng, Liangyou Li, Qun Liu** · 2022-12-17

<details>
<summary>Abstract</summary>

To alleviate the data scarcity problem in End-to-end speech translation (ST), pre-training on data for speech recognition and machine translation is considered as an important technique. However, the modality gap between speech and text prevents the ST model from efficiently inheriting knowledge from the pre-trained models. In this work, we propose AdaTranS for end-to-end ST. It adapts the speech features with a new shrinking mechanism to mitigate the length mismatch between speech and text features by predicting word boundaries. Experiments on the MUST-C dataset demonstrate that AdaTranS achieves better performance than the other shrinking-based methods, with higher inference speed and lower memory usage. Further experiments also show that AdaTranS can be equipped with additional alignment losses to further improve performance.

</details>

### [Speech Aware Dialog System Technology Challenge (DSTC11)](2212.08704.md)
**Hagen Soltau, Izhak Shafran, Mingqiu Wang, Abhinav Rastogi et al.** · 2022-12-16

<details>
<summary>Abstract</summary>

Most research on task oriented dialog modeling is based on written text input. However, users interact with practical dialog systems often using speech as input. Typically, systems convert speech into text using an Automatic Speech Recognition (ASR) system, introducing errors. Furthermore, these systems do not address the differences in written and spoken language. The research on this topic is stymied by the lack of a public corpus. Motivated by these considerations, our goal in hosting the speech-aware dialog state tracking challenge was to create a public corpus or task which can be used to investigate the performance gap between the written and spoken forms of input, develop models that could alleviate this gap, and establish whether Text-to-Speech-based (TTS) systems is a reasonable surrogate to the more-labor intensive human data collection. We created three spoken versions of the popular written-domain MultiWoz task -- (a) TTS-Verbatim: written user inputs were converted into speech waveforms using a TTS system, (b) Human-Verbatim: humans spoke the user inputs verbatim, and (c) Human-paraphrased: humans paraphrased the user inputs. Additionally, we provided different forms of ASR output to encourage wider participation from teams that may not have access to state-of-the-art ASR systems. These included ASR transcripts, word time stamps, and latent representations of the audio (audio encoder outputs). In this paper, we describe the corpus, report results from participating teams, provide preliminary analyses of their results, and summarize the current state-of-the-art in this domain.

</details>

### [Fast Entropy-Based Methods of Word-Level Confidence Estimation for End-To-End Automatic Speech Recognition](2212.08703.md)
**Aleksandr Laptev, Boris Ginsburg** · 2022-12-16

<details>
<summary>Abstract</summary>

This paper presents a class of new fast non-trainable entropy-based confidence estimation methods for automatic speech recognition. We show how per-frame entropy values can be normalized and aggregated to obtain a confidence measure per unit and per word for Connectionist Temporal Classification (CTC) and Recurrent Neural Network Transducer (RNN-T) models. Proposed methods have similar computational complexity to the traditional method based on the maximum per-frame probability, but they are more adjustable, have a wider effective threshold range, and better push apart the confidence distributions of correct and incorrect words. We evaluate the proposed confidence measures on LibriSpeech test sets, and show that they are up to 2 and 4 times better than confidence estimation based on the maximum per-frame probability at detecting incorrect words for Conformer-CTC and Conformer-RNN-T models, respectively.

</details>

### [Context-aware Fine-tuning of Self-supervised Speech Models](2212.08542.md)
**Suwon Shon, Felix Wu, Kwangyoun Kim, Prashant Sridhar et al.** · 2022-12-16

<details>
<summary>Abstract</summary>

Self-supervised pre-trained transformers have improved the state of the art on a variety of speech tasks. Due to the quadratic time and space complexity of self-attention, they usually operate at the level of relatively short (e.g., utterance) segments. In this paper, we study the use of context, i.e., surrounding segments, during fine-tuning and propose a new approach called context-aware fine-tuning. We attach a context module on top of the last layer of a pre-trained model to encode the whole segment into a context embedding vector which is then used as an additional feature for the final prediction. During the fine-tuning stage, we introduce an auxiliary loss that encourages this context embedding vector to be similar to context vectors of surrounding segments. This allows the model to make predictions without access to these surrounding segments at inference time and requires only a tiny overhead compared to standard fine-tuned models. We evaluate the proposed approach using the SLUE and Libri-light benchmarks for several downstream tasks: Automatic speech recognition (ASR), named entity recognition (NER), and sentiment analysis (SA). The results show that context-aware fine-tuning not only outperforms a standard fine-tuning baseline but also rivals a strong context injection baseline that uses neighboring speech segments during inference.

</details>

### [Effectiveness of Text, Acoustic, and Lattice-based representations in Spoken Language Understanding tasks](2212.08489.md)
**Esaú Villatoro-Tello, Srikanth Madikeri, Juan Zuluaga-Gomez, Bidisha Sharma et al.** · 2022-12-16

<details>
<summary>Abstract</summary>

In this paper, we perform an exhaustive evaluation of different representations to address the intent classification problem in a Spoken Language Understanding (SLU) setup. We benchmark three types of systems to perform the SLU intent detection task: 1) text-based, 2) lattice-based, and a novel 3) multimodal approach. Our work provides a comprehensive analysis of what could be the achievable performance of different state-of-the-art SLU systems under different circumstances, e.g., automatically- vs. manually-generated transcripts. We evaluate the systems on the publicly available SLURP spoken language resource corpus. Our results indicate that using richer forms of Automatic Speech Recognition (ASR) outputs, namely word-consensus-networks, allows the SLU system to improve in comparison to the 1-best setup (5.5% relative improvement). However, crossmodal approaches, i.e., learning from acoustic and text embeddings, obtains performance similar to the oracle setup, a relative improvement of 17.8% over the 1-best configuration, being a recommended alternative to overcome the limitations of working with automatically generated transcripts.

</details>

### [Improving Fast-slow Encoder based Transducer with Streaming Deliberation](2212.07650.md)
**Ke Li, Jay Mahadeokar, Jinxi Guo, Yangyang Shi et al.** · 2022-12-15

<details>
<summary>Abstract</summary>

This paper introduces a fast-slow encoder based transducer with streaming deliberation for end-to-end automatic speech recognition. We aim to improve the recognition accuracy of the fast-slow encoder based transducer while keeping its latency low by integrating a streaming deliberation model. Specifically, the deliberation model leverages partial hypotheses from the streaming fast encoder and implicitly learns to correct recognition errors. We modify the parallel beam search algorithm for fast-slow encoder based transducer to be efficient and compatible with the deliberation model. In addition, the deliberation model is designed to process streaming data. To further improve the deliberation performance, a simple text augmentation approach is explored. We also compare LSTM and Conformer models for encoding partial hypotheses. Experiments on Librispeech and in-house data show relative WER reductions (WERRs) from 3% to 5% with a slight increase in model size and negligible extra token emission latency compared with fast-slow encoder based transducer. Compared with vanilla neural transducers, the proposed deliberation model together with fast-slow encoder based transducer obtains relative 10-11% WERRs on Librispeech and around relative 6% WERR on in-house data with smaller emission delays.

</details>

### [Efficient Self-supervised Learning with Contextualized Target Representations for Vision, Speech and Language](2212.07525.md)
**Alexei Baevski, Arun Babu, Wei-Ning Hsu, Michael Auli** · 2022-12-14

<details>
<summary>Abstract</summary>

Current self-supervised learning algorithms are often modality-specific and require large amounts of computational resources. To address these issues, we increase the training efficiency of data2vec, a learning objective that generalizes across several modalities. We do not encode masked tokens, use a fast convolutional decoder and amortize the effort to build teacher representations. data2vec 2.0 benefits from the rich contextualized target representations introduced in data2vec which enable a fast self-supervised learner. Experiments on ImageNet-1K image classification show that data2vec 2.0 matches the accuracy of Masked Autoencoders in 16.4x lower pre-training time, on Librispeech speech recognition it performs as well as wav2vec 2.0 in 10.6x less time, and on GLUE natural language understanding it matches a retrained RoBERTa model in half the time. Trading some speed for accuracy results in ImageNet-1K top-1 accuracy of 86.8\% with a ViT-L model trained for 150 epochs.

</details>

### [Tackling the Cocktail Fork Problem for Separation and Transcription of Real-World Soundtracks](2212.07327.md)
**Darius Petermann, Gordon Wichern, Aswin Shanmugam Subramanian, Zhong-Qiu Wang et al.** · 2022-12-14

<details>
<summary>Abstract</summary>

Emulating the human ability to solve the cocktail party problem, i.e., focus on a source of interest in a complex acoustic scene, is a long standing goal of audio source separation research. Much of this research investigates separating speech from noise, speech from speech, musical instruments from each other, or sound events from each other. In this paper, we focus on the cocktail fork problem, which takes a three-pronged approach to source separation by separating an audio mixture such as a movie soundtrack or podcast into the three broad categories of speech, music, and sound effects (SFX - understood to include ambient noise and natural sound events). We benchmark the performance of several deep learning-based source separation models on this task and evaluate them with respect to simple objective measures such as signal-to-distortion ratio (SDR) as well as objective metrics that better correlate with human perception. Furthermore, we thoroughly evaluate how source separation can influence downstream transcription tasks. First, we investigate the task of activity detection on the three sources as a way to both further improve source separation and perform transcription. We formulate the transcription tasks as speech recognition for speech and audio tagging for music and SFX. We observe that, while the use of source separation estimates improves transcription performance in comparison to the original soundtrack, performance is still sub-optimal due to artifacts introduced by the separation process. Therefore, we thoroughly investigate how remixing of the three separated source stems at various relative levels can reduce artifacts and consequently improve the transcription performance. We find that remixing music and SFX interferences at a target SNR of 17.5 dB reduces speech recognition word error rate, and similar impact from remixing is observed for tagging music and SFX content.

</details>

### [Efficient Speech Representation Learning with Low-Bit Quantization](2301.00652.md)
**Ching-Feng Yeh, Wei-Ning Hsu, Paden Tomasello, Abdelrahman Mohamed** · 2022-12-14

<details>
<summary>Abstract</summary>

With the development of hardware for machine learning, newer models often come at the cost of both increased sizes and computational complexity. In effort to improve the efficiency for these models, we apply and investigate recent quantization techniques on speech representation learning models. The quantization techniques were evaluated on the SUPERB benchmark. On the ASR task, with aggressive quantization to 1 bit, we achieved 86.32% storage reduction (184.42 -> 25.23), 88% estimated runtime reduction (1.00 -> 0.12) with increased word error rate (7.06 -> 15.96). In comparison with DistillHuBERT which also aims for model compression, the 2-bit configuration yielded slightly smaller storage (35.84 vs. 46.98), better word error rate (12.68 vs. 13.37) and more efficient estimated runtime (0.15 vs. 0.73).

</details>

### [RT-1: Robotics Transformer for Real-World Control at Scale](2212.06817.md)
**Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar et al.** · 2022-12-13

<details>
<summary>Abstract</summary>

By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

</details>

### [Jointly Learning Visual and Auditory Speech Representations from Raw Data](2212.06246.md)
**Alexandros Haliassos, Pingchuan Ma, Rodrigo Mira, Stavros Petridis et al.** · 2022-12-12

<details>
<summary>Abstract</summary>

We present RAVEn, a self-supervised multi-modal approach to jointly learn visual and auditory speech representations. Our pre-training objective involves encoding masked inputs, and then predicting contextualised targets generated by slowly-evolving momentum encoders. Driven by the inherent differences between video and audio, our design is asymmetric w.r.t. the two modalities' pretext tasks: Whereas the auditory stream predicts both the visual and auditory targets, the visual one predicts only the auditory targets. We observe strong results in low- and high-resource labelled data settings when fine-tuning the visual and auditory encoders resulting from a single pre-training stage, in which the encoders are jointly trained. Notably, RAVEn surpasses all self-supervised methods on visual speech recognition (VSR) on LRS3, and combining RAVEn with self-training using only 30 hours of labelled data even outperforms a recent semi-supervised method trained on 90,000 hours of non-public data. At the same time, we achieve state-of-the-art results in the LRS3 low-resource setting for auditory speech recognition (as well as for VSR). Our findings point to the viability of learning powerful speech representations entirely from raw video and audio, i.e., without relying on handcrafted features. Code and models are available at https://github.com/ahaliassos/raven.

</details>

### [TriNet: stabilizing self-supervised learning from complete or slow collapse on ASR](2301.00656.md)
**Lixin Cao, Jun Wang, Ben Yang, Dan Su et al.** · 2022-12-12

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models confront challenges of abrupt informational collapse or slow dimensional collapse. We propose TriNet, which introduces a novel triple-branch architecture for preventing collapse and stabilizing the pre-training. TriNet learns the SSL latent embedding space and incorporates it to a higher level space for predicting pseudo target vectors generated by a frozen teacher. Our experimental results show that the proposed method notably stabilizes and accelerates pre-training and achieves a relative word error rate reduction (WERR) of 6.06% compared to the state-of-the-art (SOTA) Data2vec for a downstream benchmark ASR task. We will release our code at https://github.com/tencent-ailab/.

</details>

### [End-to-End Speech Translation of Arabic to English Broadcast News](2212.05479.md)
**Fethi Bougares, Salim Jouili** · 2022-12-11

<details>
<summary>Abstract</summary>

Speech translation (ST) is the task of directly translating acoustic speech signals in a source language into text in a foreign language. ST task has been addressed, for a long time, using a pipeline approach with two modules : first an Automatic Speech Recognition (ASR) in the source language followed by a text-to-text Machine translation (MT). In the past few years, we have seen a paradigm shift towards the end-to-end approaches using sequence-to-sequence deep neural network models. This paper presents our efforts towards the development of the first Broadcast News end-to-end Arabic to English speech translation system. Starting from independent ASR and MT LDC releases, we were able to identify about 92 hours of Arabic audio recordings for which the manual transcription was also translated into English at the segment level. These data was used to train and compare pipeline and end-to-end speech translation systems under multiple scenarios including transfer learning and data augmentation techniques.

</details>

### [Punctuation Restoration for Singaporean Spoken Languages: English, Malay, and Mandarin](2212.05356.md)
**Abhinav Rao, Ho Thi-Nga, Chng Eng-Siong** · 2022-12-10

<details>
<summary>Abstract</summary>

This paper presents the work of restoring punctuation for ASR transcripts generated by multilingual ASR systems. The focus languages are English, Mandarin, and Malay which are three of the most popular languages in Singapore. To the best of our knowledge, this is the first system that can tackle punctuation restoration for these three languages simultaneously. Traditional approaches usually treat the task as a sequential labeling task, however, this work adopts a slot-filling approach that predicts the presence and type of punctuation marks at each word boundary. The approach is similar to the Masked-Language Model approach employed during the pre-training stages of BERT, but instead of predicting the masked word, our model predicts masked punctuation. Additionally, we find that using Jieba1 instead of only using the built-in SentencePiece tokenizer of XLM-R can significantly improve the performance of punctuating Mandarin transcripts. Experimental results on English and Mandarin IWSLT2022 datasets and Malay News show that the proposed approach achieved state-of-the-art results for Mandarin with 73.8% F1-score while maintaining a reasonable F1-score for English and Malay, i.e. 74.7% and 78% respectively. Our source code that allows reproducing the results and building a simple web-based application for demonstration purposes is available on Github.

</details>

### [Lattice-Free Sequence Discriminative Training for Phoneme-Based Neural Transducers](2212.04325.md)
**Zijian Yang, Wei Zhou, Ralf Schlüter, Hermann Ney** · 2022-12-07

<details>
<summary>Abstract</summary>

Recently, RNN-Transducers have achieved remarkable results on various automatic speech recognition tasks. However, lattice-free sequence discriminative training methods, which obtain superior performance in hybrid models, are rarely investigated in RNN-Transducers. In this work, we propose three lattice-free training objectives, namely lattice-free maximum mutual information, lattice-free segment-level minimum Bayes risk, and lattice-free minimum Bayes risk, which are used for the final posterior output of the phoneme-based neural transducer with a limited context dependency. Compared to criteria using N-best lists, lattice-free methods eliminate the decoding step for hypotheses generation during training, which leads to more efficient training. Experimental results show that lattice-free methods gain up to 6.5% relative improvement in word error rate compared to a sequence-level cross-entropy trained model. Compared to the N-best-list based minimum Bayes risk objectives, lattice-free methods gain 40% - 70% relative training time speedup with a small degradation in performance.

</details>

### [Improved Speech Pre-Training with Supervision-Enhanced Acoustic Unit](2212.03482.md)
**Pengcheng Li, Genshun Wan, Fenglin Ding, Hang Chen et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

Speech pre-training has shown great success in learning useful and general latent representations from large-scale unlabeled data. Based on a well-designed self-supervised learning pattern, pre-trained models can be used to serve lots of downstream speech tasks such as automatic speech recognition. In order to take full advantage of the labed data in low resource task, we present an improved pre-training method by introducing a supervision-enhanced acoustic unit (SEAU) pattern to intensify the expression of comtext information and ruduce the training cost. Encoder representations extracted from the SEAU pattern are used to generate more representative target units for HuBERT pre-training process. The proposed method, named SeHuBERT, achieves a relative word error rate reductions of 10.5% and 4.9% comared with the standard HuBERT on Turkmen speech recognition task with 500 hours and 100 hours fine-tuning data respectively. Extended to more languages and more data, SeHuBERT can aslo achieve a relative word error rate reductions of approximately 10% at half of the training cost compared with HuBERT.

</details>

### [Progressive Multi-Scale Self-Supervised Learning for Speech Recognition](2212.03480.md)
**Genshun Wan, Tan Liu, Hang Chen, Jia Pan et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models have achieved considerable improvements in automatic speech recognition (ASR). In addition, ASR performance could be further improved if the model is dedicated to audio content information learning theoretically. To this end, we propose a progressive multi-scale self-supervised learning (PMS-SSL) method, which uses fine-grained target sets to compute SSL loss at top layer while uses coarse-grained target sets at intermediate layers. Furthermore, PMS-SSL introduces multi-scale structure into multi-head self-attention for better speech representation, which restricts the attention area into a large scope at higher layers while restricts the attention area into a small scope at lower layers. Experiments on Librispeech dataset indicate the effectiveness of our proposed method. Compared with HuBERT, PMS-SSL achieves 13.7% / 12.7% relative WER reduction on test other evaluation subsets respectively when fine-tuned on 10hours / 100hours subsets.

</details>

### [Improved Self-Supervised Multilingual Speech Representation Learning Combined with Auxiliary Language Information](2212.03476.md)
**Fenglin Ding, Genshun Wan, Pengcheng Li, Jia Pan et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

Multilingual end-to-end models have shown great improvement over monolingual systems. With the development of pre-training methods on speech, self-supervised multilingual speech representation learning like XLSR has shown success in improving the performance of multilingual automatic speech recognition (ASR). However, similar to the supervised learning, multilingual pre-training may also suffer from language interference and further affect the application of multilingual system. In this paper, we introduce several techniques for improving self-supervised multilingual pre-training by leveraging auxiliary language information, including the language adversarial training, language embedding and language adaptive training during the pre-training stage. We conduct experiments on a multilingual ASR task consisting of 16 languages. Our experimental results demonstrate 14.3% relative gain over the standard XLSR model, and 19.8% relative gain over the no pre-training multilingual model.

</details>

### [M3ST: Mix at Three Levels for Speech Translation](2212.03657.md)
**Xuxin Cheng, Qianqian Dong, Fengpeng Yue, Tom Ko et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

How to solve the data scarcity problem for end-to-end speech-to-text translation (ST)? It's well known that data augmentation is an efficient method to improve performance for many tasks by enlarging the dataset. In this paper, we propose Mix at three levels for Speech Translation (M^3ST) method to increase the diversity of the augmented training corpus. Specifically, we conduct two phases of fine-tuning based on a pre-trained model using external machine translation (MT) data. In the first stage of fine-tuning, we mix the training corpus at three levels, including word level, sentence level and frame level, and fine-tune the entire model with mixed data. At the second stage of fine-tuning, we take both original speech sequences and original text sequences in parallel into the model to fine-tune the network, and use Jensen-Shannon divergence to regularize their outputs. Experiments on MuST-C speech translation benchmark and analysis show that M^3ST outperforms current strong baselines and achieves state-of-the-art results on eight directions with an average BLEU of 29.9.

</details>

### [Robust Speech Recognition via Large-Scale Weak Supervision](2212.04356.md)
**Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman et al.** · 2022-12-06

<details>
<summary>Abstract</summary>

We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.

</details>

### [SoftCTC -- Semi-Supervised Learning for Text Recognition using Soft Pseudo-Labels](2212.02135.md)
**Martin Kišš, Michal Hradiš, Karel Beneš, Petr Buchal et al.** · 2022-12-05

<details>
<summary>Abstract</summary>

This paper explores semi-supervised training for sequence tasks, such as Optical Character Recognition or Automatic Speech Recognition. We propose a novel loss function $\unicode{x2013}$ SoftCTC $\unicode{x2013}$ which is an extension of CTC allowing to consider multiple transcription variants at the same time. This allows to omit the confidence based filtering step which is otherwise a crucial component of pseudo-labeling approaches to semi-supervised learning. We demonstrate the effectiveness of our method on a challenging handwriting recognition task and conclude that SoftCTC matches the performance of a finely-tuned filtering based pipeline. We also evaluated SoftCTC in terms of computational efficiency, concluding that it is significantly more efficient than a naïve CTC-based approach for training on multiple transcription variants, and we make our GPU implementation public.

</details>

### [LMEC: Learnable Multiplicative Absolute Position Embedding Based Conformer for Speech Recognition](2212.02099.md)
**Yuguang Yang, Yu Pan, Jingjing Yin, Heng Lu** · 2022-12-05

<details>
<summary>Abstract</summary>

This paper proposes a Learnable Multiplicative absolute position Embedding based Conformer (LMEC). It contains a kernelized linear attention (LA) module called LMLA to solve the time-consuming problem for long sequence speech recognition as well as an alternative to the FFN structure. First, the ELU function is adopted as the kernel function of our proposed LA module. Second, we propose a novel Learnable Multiplicative Absolute Position Embedding (LM-APE) based re-weighting mechanism that can reduce the well-known quadratic temporal-space complexity of softmax self-attention. Third, we use Gated Linear Units (GLU) to substitute the Feed Forward Network (FFN) for better performance. Extensive experiments have been conducted on the public LibriSpeech datasets. Compared to the Conformer model with cosFormer style linear attention, our proposed method can achieve up to 0.63% word-error-rate improvement on test-other and improve the inference speed by up to 13% (left product) and 33% (right product) on the LA module.

</details>

### [Fast and accurate factorized neural transducer for text adaption of end-to-end speech recognition models](2212.01992.md)
**Rui Zhao, Jian Xue, Partha Parthasarathy, Veljko Miljanic et al.** · 2022-12-05

<details>
<summary>Abstract</summary>

Neural transducer is now the most popular end-to-end model for speech recognition, due to its naturally streaming ability. However, it is challenging to adapt it with text-only data. Factorized neural transducer (FNT) model was proposed to mitigate this problem. The improved adaptation ability of FNT on text-only adaptation data came at the cost of lowered accuracy compared to the standard neural transducer model. We propose several methods to improve the performance of the FNT model. They are: adding CTC criterion during training, adding KL divergence loss during adaptation, using a pre-trained language model to seed the vocabulary predictor, and an efficient adaptation approach by interpolating the vocabulary predictor with the n-gram language model. A combination of these approaches results in a relative word-error-rate reduction of 9.48\% from the standard FNT model. Furthermore, n-gram interpolation with the vocabulary predictor improves the adaptation speed hugely with satisfactory adaptation performance.

</details>

### [Unsupervised Fine-Tuning Data Selection for ASR Using Self-Supervised Speech Models](2212.01661.md)
**Reem Gody, David Harwath** · 2022-12-03

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has been able to leverage unlabeled data to boost the performance of automatic speech recognition (ASR) models when we have access to only a small amount of transcribed speech data. However, this raises the question of which subset of the available unlabeled data should be selected for transcription. Our work investigates different unsupervised data selection techniques for fine-tuning the HuBERT model under a limited transcription budget. We investigate the impact of speaker diversity, gender bias, and topic diversity on the downstream ASR performance. We also devise two novel techniques for unsupervised data selection: pre-training loss based data selection and the perplexity of byte pair encoded clustered units (PBPE) and we show how these techniques compare to pure random data selection. Finally, we analyze the correlations between the inherent characteristics of the selected fine-tuning subsets as well as how these characteristics correlate with the resultant word error rate. We demonstrate the importance of token diversity, speaker diversity, and topic diversity in achieving the best performance in terms of WER.

</details>

### [Cross-Modal Mutual Learning for Cued Speech Recognition](2212.01083.md)
**Lei Liu, Li Liu** · 2022-12-02

<details>
<summary>Abstract</summary>

Automatic Cued Speech Recognition (ACSR) provides an intelligent human-machine interface for visual communications, where the Cued Speech (CS) system utilizes lip movements and hand gestures to code spoken language for hearing-impaired people. Previous ACSR approaches often utilize direct feature concatenation as the main fusion paradigm. However, the asynchronous modalities i.e., lip, hand shape and hand position) in CS may cause interference for feature concatenation. To address this challenge, we propose a transformer based cross-modal mutual learning framework to prompt multi-modal interaction. Compared with the vanilla self-attention, our model forces modality-specific information of different modalities to pass through a modality-invariant codebook, collating linguistic representations for tokens of each modality. Then the shared linguistic knowledge is used to re-synchronize multi-modal sequences. Moreover, we establish a novel large-scale multi-speaker CS dataset for Mandarin Chinese. To our knowledge, this is the first work on ACSR for Mandarin Chinese. Extensive experiments are conducted for different languages i.e., Chinese, French, and British English). Results demonstrate that our model exhibits superior recognition performance to the state-of-the-art by a large margin.

</details>

### [SoftCorrect: Error Correction with Soft Detection for Automatic Speech Recognition](2212.01039.md)
**Yichong Leng, Xu Tan, Wenjie Liu, Kaitao Song et al.** · 2022-12-02

<details>
<summary>Abstract</summary>

Error correction in automatic speech recognition (ASR) aims to correct those incorrect words in sentences generated by ASR models. Since recent ASR models usually have low word error rate (WER), to avoid affecting originally correct tokens, error correction models should only modify incorrect words, and therefore detecting incorrect words is important for error correction. Previous works on error correction either implicitly detect error words through target-source attention or CTC (connectionist temporal classification) loss, or explicitly locate specific deletion/substitution/insertion errors. However, implicit error detection does not provide clear signal about which tokens are incorrect and explicit error detection suffers from low detection accuracy. In this paper, we propose SoftCorrect with a soft error detection mechanism to avoid the limitations of both explicit and implicit error detection. Specifically, we first detect whether a token is correct or not through a probability produced by a dedicatedly designed language model, and then design a constrained CTC loss that only duplicates the detected incorrect tokens to let the decoder focus on the correction of error tokens. Compared with implicit error detection with CTC loss, SoftCorrect provides explicit signal about which words are incorrect and thus does not need to duplicate every token but only incorrect tokens; compared with explicit error detection, SoftCorrect does not detect specific deletion/substitution/insertion errors but just leaves it to CTC loss. Experiments on AISHELL-1 and Aidatatang datasets show that SoftCorrect achieves 26.1% and 9.4% CER reduction respectively, outperforming previous works by a large margin, while still enjoying fast speed of parallel generation.

</details>

### [Surrogate Gradient Spiking Neural Networks as Encoders for Large Vocabulary Continuous Speech Recognition](2212.01187.md)
**Alexandre Bittar, Philip N. Garner** · 2022-12-01

<details>
<summary>Abstract</summary>

Compared to conventional artificial neurons that produce dense and real-valued responses, biologically-inspired spiking neurons transmit sparse and binary information, which can also lead to energy-efficient implementations. Recent research has shown that spiking neural networks can be trained like standard recurrent neural networks using the surrogate gradient method. They have shown promising results on speech command recognition tasks. Using the same technique, we show that they are scalable to large vocabulary continuous speech recognition, where they are capable of replacing LSTMs in the encoder with only minor loss of performance. This suggests that they may be applicable to more involved sequence-to-sequence tasks. Moreover, in contrast to their recurrent non-spiking counterparts, they show robustness to exploding gradient problems without the need to use gates.

</details>

### [EURO: ESPnet Unsupervised ASR Open-source Toolkit](2211.17196.md)
**Dongji Gao, Jiatong Shi, Shun-Po Chuang, Leibny Paola Garcia et al.** · 2022-11-30

<details>
<summary>Abstract</summary>

This paper describes the ESPnet Unsupervised ASR Open-source Toolkit (EURO), an end-to-end open-source toolkit for unsupervised automatic speech recognition (UASR). EURO adopts the state-of-the-art UASR learning method introduced by the Wav2vec-U, originally implemented at FAIRSEQ, which leverages self-supervised speech representations and adversarial training. In addition to wav2vec2, EURO extends the functionality and promotes reproducibility for UASR tasks by integrating S3PRL and k2, resulting in flexible frontends from 27 self-supervised models and various graph-based decoding strategies. EURO is implemented in ESPnet and follows its unified pipeline to provide UASR recipes with a complete setup. This improves the pipeline's efficiency and allows EURO to be easily applied to existing datasets in ESPnet. Extensive experiments on three mainstream self-supervised models demonstrate the toolkit's effectiveness and achieve state-of-the-art UASR performance on TIMIT and LibriSpeech datasets. EURO will be publicly available at https://github.com/espnet/espnet, aiming to promote this exciting and emerging research area based on UASR through open-source activity.

</details>

### [Better Transcription of UK Supreme Court Hearings](2211.17094.md)
**Hadeel Saadany, Catherine Breslin, Constantin Orăsan, Sophie Walker** · 2022-11-29

<details>
<summary>Abstract</summary>

Transcription of legal proceedings is very important to enable access to justice. However, speech transcription is an expensive and slow process. In this paper we describe part of a combined research and industrial project for building an automated transcription tool designed specifically for the Justice sector in the UK. We explain the challenges involved in transcribing court room hearings and the Natural Language Processing (NLP) techniques we employ to tackle these challenges. We will show that fine-tuning a generic off-the-shelf pre-trained Automatic Speech Recognition (ASR) system with an in-domain language model as well as infusing common phrases extracted with a collocation detection model can improve not only the Word Error Rate (WER) of the transcribed hearings but avoid critical errors that are specific of the legal jargon and terminology commonly used in British courts.

</details>

### [Neural Transducer Training: Reduced Memory Consumption with Sample-wise Computation](2211.16270.md)
**Stefan Braun, Erik McDermott, Roger Hsiao** · 2022-11-29

<details>
<summary>Abstract</summary>

The neural transducer is an end-to-end model for automatic speech recognition (ASR). While the model is well-suited for streaming ASR, the training process remains challenging. During training, the memory requirements may quickly exceed the capacity of state-of-the-art GPUs, limiting batch size and sequence lengths. In this work, we analyze the time and space complexity of a typical transducer training setup. We propose a memory-efficient training method that computes the transducer loss and gradients sample by sample. We present optimizations to increase the efficiency and parallelism of the sample-wise method. In a set of thorough benchmarks, we show that our sample-wise method significantly reduces memory usage, and performs at competitive speed when compared to the default batched computation. As a highlight, we manage to compute the transducer loss and gradients for a batch size of 1024, and audio length of 40 seconds, using only 6 GB of memory.

</details>

### [MMSpeech: Multi-modal Multi-task Encoder-Decoder Pre-training for Speech Recognition](2212.00500.md)
**Xiaohuan Zhou, Jiaming Wang, Zeyu Cui, Shiliang Zhang et al.** · 2022-11-29

<details>
<summary>Abstract</summary>

In this paper, we propose a novel multi-modal multi-task encoder-decoder pre-training framework (MMSpeech) for Mandarin automatic speech recognition (ASR), which employs both unlabeled speech and text data. The main difficulty in speech-text joint pre-training comes from the significant difference between speech and text modalities, especially for Mandarin speech and text. Unlike English and other languages with an alphabetic writing system, Mandarin uses an ideographic writing system where character and sound are not tightly mapped to one another. Therefore, we propose to introduce the phoneme modality into pre-training, which can help capture modality-invariant information between Mandarin speech and text. Specifically, we employ a multi-task learning framework including five self-supervised and supervised tasks with speech and text data. For end-to-end pre-training, we introduce self-supervised speech-to-pseudo-codes (S2C) and phoneme-to-text (P2T) tasks utilizing unlabeled speech and text data, where speech-pseudo-codes pairs and phoneme-text pairs are a supplement to the supervised speech-text pairs. To train the encoder to learn better speech representation, we introduce self-supervised masked speech prediction (MSP) and supervised phoneme prediction (PP) tasks to learn to map speech into phonemes. Besides, we directly add the downstream supervised speech-to-text (S2T) task into the pre-training process, which can further improve the pre-training performance and achieve better recognition results even without fine-tuning. Experiments on AISHELL-1 show that our proposed method achieves state-of-the-art performance, with a more than 40% relative improvement compared with other pre-training methods.

</details>

### [Inter-KD: Intermediate Knowledge Distillation for CTC-Based Automatic Speech Recognition](2211.15075.md)
**Ji Won Yoon, Beom Jun Woo, Sunghwan Ahn, Hyeonseung Lee et al.** · 2022-11-28

<details>
<summary>Abstract</summary>

Recently, the advance in deep learning has brought a considerable improvement in the end-to-end speech recognition field, simplifying the traditional pipeline while producing promising results. Among the end-to-end models, the connectionist temporal classification (CTC)-based model has attracted research interest due to its non-autoregressive nature. However, such CTC models require a heavy computational cost to achieve outstanding performance. To mitigate the computational burden, we propose a simple yet effective knowledge distillation (KD) for the CTC framework, namely Inter-KD, that additionally transfers the teacher's knowledge to the intermediate CTC layers of the student network. From the experimental results on the LibriSpeech, we verify that the Inter-KD shows better achievements compared to the conventional KD methods. Without using any language model (LM) and data augmentation, Inter-KD improves the word error rate (WER) performance from 8.85 % to 6.30 % on the test-clean.

</details>

### [Bidirectional Representations for Low Resource Spoken Language Understanding](2211.14320.md)
**Quentin Meeus, Marie-Francine Moens, Hugo Van hamme** · 2022-11-24

<details>
<summary>Abstract</summary>

Most spoken language understanding systems use a pipeline approach composed of an automatic speech recognition interface and a natural language understanding module. This approach forces hard decisions when converting continuous inputs into discrete language symbols. Instead, we propose a representation model to encode speech in rich bidirectional encodings that can be used for downstream tasks such as intent prediction. The approach uses a masked language modelling objective to learn the representations, and thus benefits from both the left and right contexts. We show that the performance of the resulting encodings before fine-tuning is better than comparable models on multiple datasets, and that fine-tuning the top layers of the representation model improves the current state of the art on the Fluent Speech Command dataset, also in a low-data regime, when a limited amount of labelled data is used for training. Furthermore, we propose class attention as a spoken language understanding module, efficient both in terms of speed and number of parameters. Class attention can be used to visually explain the predictions of our model, which goes a long way in understanding how the model makes predictions. We perform experiments in English and in Dutch.

</details>

### [Multitask Learning for Low Resource Spoken Language Understanding](2211.13703.md)
**Quentin Meeus, Marie-Francine Moens, Hugo Van hamme** · 2022-11-24

<details>
<summary>Abstract</summary>

We explore the benefits that multitask learning offer to speech processing as we train models on dual objectives with automatic speech recognition and intent classification or sentiment classification. Our models, although being of modest size, show improvements over models trained end-to-end on intent classification. We compare different settings to find the optimal disposition of each task module compared to one another. Finally, we study the performance of the models in low-resource scenario by training the models with as few as one example per class. We show that multitask learning in these scenarios compete with a baseline model trained on text features and performs considerably better than a pipeline model. On sentiment classification, we match the performance of an end-to-end model with ten times as many parameters. We consider 4 tasks and 4 datasets in Dutch and English.

</details>

### [TESSP: Text-Enhanced Self-Supervised Speech Pre-training](2211.13443.md)
**Zhuoyuan Yao, Shuo Ren, Sanyuan Chen, Ziyang Ma et al.** · 2022-11-24

<details>
<summary>Abstract</summary>

Self-supervised speech pre-training empowers the model with the contextual structure inherent in the speech signal while self-supervised text pre-training empowers the model with linguistic information. Both of them are beneficial for downstream speech tasks such as ASR. However, the distinct pre-training objectives make it challenging to jointly optimize the speech and text representation in the same model. To solve this problem, we propose Text-Enhanced Self-Supervised Speech Pre-training (TESSP), aiming to incorporate the linguistic information into speech pre-training. Our model consists of three parts, i.e., a speech encoder, a text encoder and a shared encoder. The model takes unsupervised speech and text data as the input and leverages the common HuBERT and MLM losses respectively. We also propose phoneme up-sampling and representation swapping to enable joint modeling of the speech and text information. Specifically, to fix the length mismatching problem between speech and text data, we phonemize the text sequence and up-sample the phonemes with the alignment information extracted from a small set of supervised data. Moreover, to close the gap between the learned speech and text representations, we swap the text representation with the speech representation extracted by the respective private encoders according to the alignment information. Experiments on the Librispeech dataset shows the proposed TESSP model achieves more than 10% improvement compared with WavLM on the test-clean and test-other sets. We also evaluate our model on the SUPERB benchmark, showing our model has better performance on Phoneme Recognition, Acoustic Speech Recognition and Speech Translation compared with WavLM.

</details>

### [Device Directedness with Contextual Cues for Spoken Dialog Systems](2211.13280.md)
**Dhanush Bekal, Sundararajan Srinivasan, Sravan Bodapati, Srikanth Ronanki et al.** · 2022-11-23

<details>
<summary>Abstract</summary>

In this work, we define barge-in verification as a supervised learning task where audio-only information is used to classify user spoken dialogue into true and false barge-ins. Following the success of pre-trained models, we use low-level speech representations from a self-supervised representation learning model for our downstream classification task. Further, we propose a novel technique to infuse lexical information directly into speech representations to improve the domain-specific language information implicitly learned during pre-training. Experiments conducted on spoken dialog data show that our proposed model trained to validate barge-in entirely from speech representations is faster by 38% relative and achieves 4.5% relative F1 score improvement over a baseline LSTM model that uses both audio and Automatic Speech Recognition (ASR) 1-best hypotheses. On top of this, our best proposed model with lexically infused representations along with contextual features provides a further relative improvement of 5.7% in the F1 score but only 22% faster than the baseline.

</details>

### [Mask the Correct Tokens: An Embarrassingly Simple Approach for Error Correction](2211.13252.md)
**Kai Shen, Yichong Leng, Xu Tan, Siliang Tang et al.** · 2022-11-23

<details>
<summary>Abstract</summary>

Text error correction aims to correct the errors in text sequences such as those typed by humans or generated by speech recognition models. Previous error correction methods usually take the source (incorrect) sentence as encoder input and generate the target (correct) sentence through the decoder. Since the error rate of the incorrect sentence is usually low (e.g., 10\%), the correction model can only learn to correct on limited error tokens but trivially copy on most tokens (correct tokens), which harms the effective training of error correction. In this paper, we argue that the correct tokens should be better utilized to facilitate effective training and then propose a simple yet effective masking strategy to achieve this goal. Specifically, we randomly mask out a part of the correct tokens in the source sentence and let the model learn to not only correct the original error tokens but also predict the masked tokens based on their context information. Our method enjoys several advantages: 1) it alleviates trivial copy; 2) it leverages effective training signals from correct tokens; 3) it is a plug-and-play module and can be applied to different models and tasks. Experiments on spelling error correction and speech recognition error correction on Mandarin datasets and grammar error correction on English datasets with both autoregressive and non-autoregressive generation models show that our method improves the correction accuracy consistently.

</details>

### [Whose Emotion Matters? Speaking Activity Localisation without Prior Knowledge](2211.15377.md)
**Hugo Carneiro, Cornelius Weber, Stefan Wermter** · 2022-11-23

<details>
<summary>Abstract</summary>

The task of emotion recognition in conversations (ERC) benefits from the availability of multiple modalities, as provided, for example, in the video-based Multimodal EmotionLines Dataset (MELD). However, only a few research approaches use both acoustic and visual information from the MELD videos. There are two reasons for this: First, label-to-video alignments in MELD are noisy, making those videos an unreliable source of emotional speech data. Second, conversations can involve several people in the same scene, which requires the localisation of the utterance source. In this paper, we introduce MELD with Fixed Audiovisual Information via Realignment (MELD-FAIR) by using recent active speaker detection and automatic speech recognition models, we are able to realign the videos of MELD and capture the facial expressions from speakers in 96.92% of the utterances provided in MELD. Experiments with a self-supervised voice recognition model indicate that the realigned MELD-FAIR videos more closely match the transcribed utterances given in the MELD dataset. Finally, we devise a model for emotion recognition in conversations trained on the realigned MELD-FAIR videos, which outperforms state-of-the-art models for ERC based on vision alone. This indicates that localising the source of speaking activities is indeed effective for extracting facial expressions from the uttering speakers and that faces provide more informative visual cues than the visual features state-of-the-art models have been using so far. The MELD-FAIR realignment data, and the code of the realignment procedure and of the emotional recognition, are available at https://github.com/knowledgetechnologyuhh/MELD-FAIR.

</details>

### [Complex-Valued Time-Frequency Self-Attention for Speech Dereverberation](2211.12632.md)
**Vinay Kothapally, John H. L. Hansen** · 2022-11-22

<details>
<summary>Abstract</summary>

Several speech processing systems have demonstrated considerable performance improvements when deep complex neural networks (DCNN) are coupled with self-attention (SA) networks. However, the majority of DCNN-based studies on speech dereverberation that employ self-attention do not explicitly account for the inter-dependencies between real and imaginary features when computing attention. In this study, we propose a complex-valued T-F attention (TFA) module that models spectral and temporal dependencies by computing two-dimensional attention maps across time and frequency dimensions. We validate the effectiveness of our proposed complex-valued TFA module with the deep complex convolutional recurrent network (DCCRN) using the REVERB challenge corpus. Experimental findings indicate that integrating our complex-TFA module with DCCRN improves overall speech quality and performance of back-end speech applications, such as automatic speech recognition, compared to earlier approaches for self-attention.

</details>

### [SpeechNet: Weakly Supervised, End-to-End Speech Recognition at Industrial Scale](2211.11740.md)
**Raphael Tang, Karun Kumar, Gefei Yang, Akshat Pandey et al.** · 2022-11-21

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition systems represent the state of the art, but they rely on thousands of hours of manually annotated speech for training, as well as heavyweight computation for inference. Of course, this impedes commercialization since most companies lack vast human and computational resources. In this paper, we explore training and deploying an ASR system in the label-scarce, compute-limited setting. To reduce human labor, we use a third-party ASR system as a weak supervision source, supplemented with labeling functions derived from implicit user feedback. To accelerate inference, we propose to route production-time queries across a pool of CUDA graphs of varying input lengths, the distribution of which best matches the traffic's. Compared to our third-party ASR, we achieve a relative improvement in word-error rate of 8% and a speedup of 600%. Our system, called SpeechNet, currently serves 12 million queries per day on our voice-enabled smart television. To our knowledge, this is the first time a large-scale, Wav2vec-based deployment has been described in the academic literature.

</details>

### [Towards continually learning new languages](2211.11703.md)
**Ngoc-Quan Pham, Jan Niehues, Alexander Waibel** · 2022-11-21

<details>
<summary>Abstract</summary>

Multilingual speech recognition with neural networks is often implemented with batch-learning, when all of the languages are available before training. An ability to add new languages after the prior training sessions can be economically beneficial, but the main challenge is catastrophic forgetting. In this work, we combine the qualities of weight factorization and elastic weight consolidation in order to counter catastrophic forgetting and facilitate learning new languages quickly. Such combination allowed us to eliminate catastrophic forgetting while still achieving performance for the new languages comparable with having all languages at once, in experiments of learning from an initial 10 languages to achieve 26 languages without catastrophic forgetting and a reasonable performance compared to training all languages from scratch.

</details>

### [Constructing Effective Machine Learning Models for the Sciences: A Multidisciplinary Perspective](2211.11680.md)
**Alice E. A. Allen, Alexandre Tkatchenko** · 2022-11-21

<details>
<summary>Abstract</summary>

Learning from data has led to substantial advances in a multitude of disciplines, including text and multimedia search, speech recognition, and autonomous-vehicle navigation. Can machine learning enable similar leaps in the natural and social sciences? This is certainly the expectation in many scientific fields and recent years have seen a plethora of applications of non-linear models to a wide range of datasets. However, flexible non-linear solutions will not always improve upon manually adding transforms and interactions between variables to linear regression models. We discuss how to recognize this before constructing a data-driven model and how such analysis can help us move to intrinsically interpretable regression models. Furthermore, for a variety of applications in the natural and social sciences we demonstrate why improvements may be seen with more complex regression models and why they may not.

</details>

### [SSCFormer: Push the Limit of Chunk-wise Conformer for Streaming ASR Using Sequentially Sampled Chunks and Chunked Causal Convolution](2211.11419.md)
**Fangyuan Wang, Bo Xu, Bo Xu** · 2022-11-21

<details>
<summary>Abstract</summary>

Currently, the chunk-wise schemes are often used to make Automatic Speech Recognition (ASR) models to support streaming deployment. However, existing approaches are unable to capture the global context, lack support for parallel training, or exhibit quadratic complexity for the computation of multi-head self-attention (MHSA). On the other side, the causal convolution, no future context used, has become the de facto module in streaming Conformer. In this paper, we propose SSCFormer to push the limit of chunk-wise Conformer for streaming ASR using the following two techniques: 1) A novel cross-chunks context generation method, named Sequential Sampling Chunk (SSC) scheme, to re-partition chunks from regular partitioned chunks to facilitate efficient long-term contextual interaction within local chunks. 2)The Chunked Causal Convolution (C2Conv) is designed to concurrently capture the left context and chunk-wise future context. Evaluations on AISHELL-1 show that an End-to-End (E2E) CER 5.33% can achieve, which even outperforms a strong time-restricted baseline U2. Moreover, the chunk-wise MHSA computation in our model enables it to train with a large batch size and perform inference with linear complexity.

</details>

### [VATLM: Visual-Audio-Text Pre-Training with Unified Masked Prediction for Speech Representation Learning](2211.11275.md)
**Qiushi Zhu, Long Zhou, Ziqiang Zhang, Shujie Liu et al.** · 2022-11-21

<details>
<summary>Abstract</summary>

Although speech is a simple and effective way for humans to communicate with the outside world, a more realistic speech interaction contains multimodal information, e.g., vision, text. How to design a unified framework to integrate different modal information and leverage different resources (e.g., visual-audio pairs, audio-text pairs, unlabeled speech, and unlabeled text) to facilitate speech representation learning was not well explored. In this paper, we propose a unified cross-modal representation learning framework VATLM (Visual-Audio-Text Language Model). The proposed VATLM employs a unified backbone network to model the modality-independent information and utilizes three simple modality-dependent modules to preprocess visual, speech, and text inputs. In order to integrate these three modalities into one shared semantic space, VATLM is optimized with a masked prediction task of unified tokens, given by our proposed unified tokenizer. We evaluate the pre-trained VATLM on audio-visual related downstream tasks, including audio-visual speech recognition (AVSR), visual speech recognition (VSR) tasks. Results show that the proposed VATLM outperforms previous the state-of-the-art models, such as audio-visual pre-trained AV-HuBERT model, and analysis also demonstrates that VATLM is capable of aligning different modalities into the same space. To facilitate future research, we release the code and pre-trained models at https://aka.ms/vatlm.

</details>

### [Exploring WavLM on Speech Enhancement](2211.09988.md)
**Hyungchan Song, Sanyuan Chen, Zhuo Chen, Yu Wu et al.** · 2022-11-18

<details>
<summary>Abstract</summary>

There is a surge in interest in self-supervised learning approaches for end-to-end speech encoding in recent years as they have achieved great success. Especially, WavLM showed state-of-the-art performance on various speech processing tasks. To better understand the efficacy of self-supervised learning models for speech enhancement, in this work, we design and conduct a series of experiments with three resource conditions by combining WavLM and two high-quality speech enhancement systems. Also, we propose a regression-based WavLM training objective and a noise-mixing data configuration to further boost the downstream enhancement performance. The experiments on the DNS challenge dataset and a simulation dataset show that the WavLM benefits the speech enhancement task in terms of both speech quality and speech recognition accuracy, especially for low fine-tuning resources. For the high fine-tuning resource condition, only the word error rate is substantially improved.

</details>

### [AVATAR submission to the Ego4D AV Transcription Challenge](2211.09966.md)
**Paul Hongsuck Seo, Arsha Nagrani, Cordelia Schmid** · 2022-11-18

<details>
<summary>Abstract</summary>

In this report, we describe our submission to the Ego4D AudioVisual (AV) Speech Transcription Challenge 2022. Our pipeline is based on AVATAR, a state of the art encoder-decoder model for AV-ASR that performs early fusion of spectrograms and RGB images. We describe the datasets, experimental settings and ablations. Our final method achieves a WER of 68.40 on the challenge test set, outperforming the baseline by 43.7%, and winning the challenge.

</details>

### [LongFNT: Long-form Speech Recognition with Factorized Neural Transducer](2211.09412.md)
**Xun Gong, Yu Wu, Jinyu Li, Shujie Liu et al.** · 2022-11-17

<details>
<summary>Abstract</summary>

Traditional automatic speech recognition~(ASR) systems usually focus on individual utterances, without considering long-form speech with useful historical information, which is more practical in real scenarios. Simply attending longer transcription history for a vanilla neural transducer model shows no much gain in our preliminary experiments, since the prediction network is not a pure language model. This motivates us to leverage the factorized neural transducer structure, containing a real language model, the vocabulary predictor. We propose the {LongFNT-Text} architecture, which fuses the sentence-level long-form features directly with the output of the vocabulary predictor and then embeds token-level long-form features inside the vocabulary predictor, with a pre-trained contextual encoder RoBERTa to further boost the performance. Moreover, we propose the {LongFNT} architecture by extending the long-form speech to the original speech input and achieve the best performance. The effectiveness of our LongFNT approach is validated on LibriSpeech and GigaSpeech corpora with 19% and 12% relative word error rate~(WER) reduction, respectively.

</details>

### [Unsupervised Model-based speaker adaptation of end-to-end lattice-free MMI model for speech recognition](2211.09313.md)
**Xurong Xie, Xunying Liu, Hui Chen, Hongan Wang** · 2022-11-17

<details>
<summary>Abstract</summary>

Modeling the speaker variability is a key challenge for automatic speech recognition (ASR) systems. In this paper, the learning hidden unit contributions (LHUC) based adaptation techniques with compact speaker dependent (SD) parameters are used to facilitate both speaker adaptive training (SAT) and unsupervised test-time speaker adaptation for end-to-end (E2E) lattice-free MMI (LF-MMI) models. An unsupervised model-based adaptation framework is proposed to estimate the SD parameters in E2E paradigm using LF-MMI and cross entropy (CE) criterions. Various regularization methods of the standard LHUC adaptation, e.g., the Bayesian LHUC (BLHUC) adaptation, are systematically investigated to mitigate the risk of overfitting, on E2E LF-MMI CNN-TDNN and CNN-TDNN-BLSTM models. Lattice-based confidence score estimation is used for adaptation data selection to reduce the supervision label uncertainty. Experiments on the 300-hour Switchboard task suggest that applying BLHUC in the proposed unsupervised E2E adaptation framework to byte pair encoding (BPE) based E2E LF-MMI systems consistently outperformed the baseline systems by relative word error rate (WER) reductions up to 10.5% and 14.7% on the NIST Hub5'00 and RT03 evaluation sets, and achieved the best performance in WERs of 9.0% and 9.7%, respectively. These results are comparable to the results of state-of-the-art adapted LF-MMI hybrid systems and adapted Conformer-based E2E systems.

</details>

### [L2 proficiency assessment using self-supervised speech representations](2211.08849.md)
**Stefano Bannò, Kate M. Knill, Marco Matassoni, Vyas Raina et al.** · 2022-11-16

<details>
<summary>Abstract</summary>

There has been a growing demand for automated spoken language assessment systems in recent years. A standard pipeline for this process is to start with a speech recognition system and derive features, either hand-crafted or based on deep-learning, that exploit the transcription and audio. Though these approaches can yield high performance systems, they require speech recognition systems that can be used for L2 speakers, and preferably tuned to the specific form of test being deployed. Recently a self-supervised speech representation based scheme, requiring no speech recognition, was proposed. This work extends the initial analysis conducted on this approach to a large scale proficiency test, Linguaskill, that comprises multiple parts, each designed to assess different attributes of a candidate's speaking proficiency. The performance of the self-supervised, wav2vec 2.0, system is compared to a high performance hand-crafted assessment system and a BERT-based text system both of which use speech transcriptions. Though the wav2vec 2.0 based system is found to be sensitive to the nature of the response, it can be configured to yield comparable performance to systems requiring a speech transcription, and yields gains when appropriately combined with standard approaches.

</details>

### [Speaker Adaptation for End-To-End Speech Recognition Systems in Noisy Environments](2211.08774.md)
**Dominik Wagner, Ilja Baumann, Sebastian P. Bayerl, Korbinian Riedhammer et al.** · 2022-11-16

<details>
<summary>Abstract</summary>

We analyze the impact of speaker adaptation in end-to-end automatic speech recognition models based on transformers and wav2vec 2.0 under different noise conditions. By including speaker embeddings obtained from x-vector and ECAPA-TDNN systems, as well as i-vectors, we achieve relative word error rate improvements of up to 16.3% on LibriSpeech and up to 14.5% on Switchboard. We show that the proven method of concatenating speaker vectors to the acoustic features and supplying them as auxiliary model inputs remains a viable option to increase the robustness of end-to-end architectures. The effect on transformer models is stronger, when more noise is added to the input speech. The most substantial benefits for systems based on wav2vec 2.0 are achieved under moderate or no noise conditions. Both x-vectors and ECAPA-TDNN embeddings outperform i-vectors as speaker representations. The optimal embedding size depends on the dataset and also varies with the noise condition.

</details>

### [Streaming Joint Speech Recognition and Disfluency Detection](2211.08726.md)
**Hayato Futami, Emiru Tsunoo, Kentaro Shibata, Yosuke Kashiwagi et al.** · 2022-11-16

<details>
<summary>Abstract</summary>

Disfluency detection has mainly been solved in a pipeline approach, as post-processing of speech recognition. In this study, we propose Transformer-based encoder-decoder models that jointly solve speech recognition and disfluency detection, which work in a streaming manner. Compared to pipeline approaches, the joint models can leverage acoustic information that makes disfluency detection robust to recognition errors and provide non-verbal clues. Moreover, joint modeling results in low-latency and lightweight inference. We investigate two joint model variants for streaming disfluency detection: a transcript-enriched model and a multi-task model. The transcript-enriched model is trained on text with special tags indicating the starting and ending points of the disfluent part. However, it has problems with latency and standard language model adaptation, which arise from the additional disfluency tags. We propose a multi-task model to solve such problems, which has two output layers at the Transformer decoder; one for speech recognition and the other for disfluency detection. It is modeled to be conditioned on the currently recognized token with an additional token-dependency mechanism. We show that the proposed joint models outperformed a BERT-based pipeline approach in both accuracy and latency, on both the Switchboard and the corpus of spontaneous Japanese.

</details>

### [Introducing Semantics into Speech Encoders](2211.08402.md)
**Derek Xu, Shuyan Dong, Changhan Wang, Suyoun Kim et al.** · 2022-11-15

<details>
<summary>Abstract</summary>

Recent studies find existing self-supervised speech encoders contain primarily acoustic rather than semantic information. As a result, pipelined supervised automatic speech recognition (ASR) to large language model (LLM) systems achieve state-of-the-art results on semantic spoken language tasks by utilizing rich semantic representations from the LLM. These systems come at the cost of labeled audio transcriptions, which is expensive and time-consuming to obtain. We propose a task-agnostic unsupervised way of incorporating semantic information from LLMs into self-supervised speech encoders without labeled audio transcriptions. By introducing semantics, we improve existing speech encoder spoken language understanding performance by over 10\% on intent classification, with modest gains in named entity resolution and slot filling, and spoken question answering FF1 score by over 2\%. Our unsupervised approach achieves similar performance as supervised methods trained on over 100 hours of labeled audio transcripts, demonstrating the feasibility of unsupervised semantic augmentations to existing speech encoders.

</details>

### [Improving Children's Speech Recognition by Fine-tuning Self-supervised Adult Speech Representations](2211.07769.md)
**Renee Lu, Mostafa Shahin, Beena Ahmed** · 2022-11-14

<details>
<summary>Abstract</summary>

Children's speech recognition is a vital, yet largely overlooked domain when building inclusive speech technologies. The major challenge impeding progress in this domain is the lack of adequate child speech corpora; however, recent advances in self-supervised learning have created a new opportunity for overcoming this problem of data scarcity. In this paper, we leverage self-supervised adult speech representations and use three well-known child speech corpora to build models for children's speech recognition. We assess the performance of fine-tuning on both native and non-native children's speech, examine the effect of cross-domain child corpora, and investigate the minimum amount of child speech required to fine-tune a model which outperforms a state-of-the-art adult model. We also analyze speech recognition performance across children's ages. Our results demonstrate that fine-tuning with cross-domain child corpora leads to relative improvements of up to 46.08% and 45.53% for native and non-native child speech respectively, and absolute improvements of 14.70% and 31.10%. We also show that with as little as 5 hours of transcribed children's speech, it is possible to fine-tune a children's speech recognition system that outperforms a state-of-the-art adult model fine-tuned on 960 hours of adult speech.

</details>

### [FullPack: Full Vector Utilization for Sub-Byte Quantized Inference on General Purpose CPUs](2211.06982.md)
**Hossein Katebi, Navidreza Asadi, Maziar Goudarzi** · 2022-11-13

<details>
<summary>Abstract</summary>

Although prior art has demonstrated negligible accuracy drop in sub-byte quantization -- where weights and/or activations are represented by less than 8 bits -- popular SIMD instructions of CPUs do not natively support these datatypes. While recent methods, such as ULPPACK, are already using sub-byte quantization on general-purpose CPUs with vector units, they leave out several empty bits between the sub-byte values in memory and in vector registers to avoid overflow to the neighbours during the operations. This results in memory footprint and bandwidth-usage inefficiencies and suboptimal performance. In this paper, we present memory layouts for storing, and mechanisms for processing sub-byte (4-, 2-, or 1-bit) models that utilize all the bits in the memory as well as in the vector registers for the actual data. We provide compute kernels for the proposed layout for the GEMV (GEneral Matrix-Vector multiplication) operations between weights and activations of different datatypes (e.g., 8-bit activations and 4-bit weights). For evaluation, we extended the TFLite package and added our methods to it, then ran the models on the cycle-accurate gem5 simulator to compare detailed memory and CPU cycles of each method. We compare against nine other methods that are actively used in production including GEMLOWP, Ruy, XNNPack, and ULPPACK. Furthermore, we explore the effect of different input and output sizes of deep learning layers on the performance of our proposed method. Experimental results show 0.96-2.1x speedup for small sizes and 1.2-6.7x speedup for mid to large sizes. Applying our proposal to a real-world speech recognition model, Mozilla DeepSpeech, we proved that our method achieves 1.56-2.11x end-to-end speedup compared to the state-of-the-art, depending on the bit-width employed.

</details>

### [Computable Bounds and Monte Carlo Estimates of the Expected Edit Distance](2211.07644.md)
**Gianfranco Bilardi, Michele Schimd** · 2022-11-13

<details>
<summary>Abstract</summary>

The edit distance is a metric of dissimilarity between strings, widely applied in computational biology, speech recognition, and machine learning. Let $e_k(n)$ denote the average edit distance between random, independent strings of $n$ characters from an alphabet of size $k$. For $k \geq 2$, it is an open problem how to efficiently compute the exact value of $α_{k}(n) = e_k(n)/n$ as well as of $α_{k} = \lim_{n \to \infty} α_{k}(n)$, a limit known to exist. This paper shows that $α_k(n)-Q(n) \leq α_k \leq α_k(n)$, for a specific $Q(n)=Θ(\sqrt{\log n / n})$, a result which implies that $α_k$ is computable. The exact computation of $α_k(n)$ is explored, leading to an algorithm running in time $T=\mathcal{O}(n^2k\min(3^n,k^n))$, a complexity that makes it of limited practical use. An analysis of statistical estimates is proposed, based on McDiarmid's inequality, showing how $α_k(n)$ can be evaluated with good accuracy, high confidence level, and reasonable computation time, for values of $n$ say up to a quarter million. Correspondingly, 99.9\% confidence intervals of width approximately $10^{-2}$ are obtained for $α_k$. Combinatorial arguments on edit scripts are exploited to analytically characterize an efficiently computable lower bound $β_k^*$ to $α_k$, such that $ \lim_{k \to \infty} β_k^*=1$. In general, $β_k^* \leq α_k \leq 1-1/k$; for $k$ greater than a few dozens, computing $β_k^*$ is much faster than generating good statistical estimates with confidence intervals of width $1-1/k-β_k^*$. The techniques developed in the paper yield improvements on most previously published numerical values as well as results for alphabet sizes and string lengths not reported before.

</details>

### [An Adapter based Multi-label Pre-training for Speech Separation and Enhancement](2211.06041.md)
**Tianrui Wang, Xie Chen, Zhuo Chen, Shu Yu et al.** · 2022-11-11

<details>
<summary>Abstract</summary>

In recent years, self-supervised learning (SSL) has achieved tremendous success in various speech tasks due to its power to extract representations from massive unlabeled data. However, compared with tasks such as speech recognition (ASR), the improvements from SSL representation in speech separation (SS) and enhancement (SE) are considerably smaller. Based on HuBERT, this work investigates improving the SSL model for SS and SE. We first update HuBERT's masked speech prediction (MSP) objective by integrating the separation and denoising terms, resulting in a multiple pseudo label pre-training scheme, which significantly improves HuBERT's performance on SS and SE but degrades the performance on ASR. To maintain its performance gain on ASR, we further propose an adapter-based architecture for HuBERT's Transformer encoder, where only a few parameters of each layer are adjusted to the multiple pseudo label MSP while other parameters remain frozen as default HuBERT. Experimental results show that our proposed adapter-based multiple pseudo label HuBERT yield consistent and significant performance improvements on SE, SS, and ASR tasks, with a faster pre-training speed, at only marginal parameters increase.

</details>

### [Continuous Soft Pseudo-Labeling in ASR](2211.06007.md)
**Tatiana Likhomanenko, Ronan Collobert, Navdeep Jaitly, Samy Bengio** · 2022-11-11

<details>
<summary>Abstract</summary>

Continuous pseudo-labeling (PL) algorithms such as slimIPL have recently emerged as a powerful strategy for semi-supervised learning in speech recognition. In contrast with earlier strategies that alternated between training a model and generating pseudo-labels (PLs) with it, here PLs are generated in end-to-end manner as training proceeds, improving training speed and the accuracy of the final model. PL shares a common theme with teacher-student models such as distillation in that a teacher model generates targets that need to be mimicked by the student model being trained. However, interestingly, PL strategies in general use hard-labels, whereas distillation uses the distribution over labels as the target to mimic. Inspired by distillation we expect that specifying the whole distribution (aka soft-labels) over sequences as the target for unlabeled data, instead of a single best pass pseudo-labeled transcript (hard-labels) should improve PL performance and convergence. Surprisingly and unexpectedly, we find that soft-labels targets can lead to training divergence, with the model collapsing to a degenerate token distribution per frame. We hypothesize that the reason this does not happen with hard-labels is that training loss on hard-labels imposes sequence-level consistency that keeps the model from collapsing to the degenerate solution. In this paper, we show several experiments that support this hypothesis, and experiment with several regularization approaches that can ameliorate the degenerate collapse when using soft-labels. These approaches can bring the accuracy of soft-labels closer to that of hard-labels, and while they are unable to outperform them yet, they serve as a useful framework for further improvements.

</details>

### [Align, Write, Re-order: Explainable End-to-End Speech Translation via Operation Sequence Generation](2211.05967.md)
**Motoi Omachi, Brian Yan, Siddharth Dalmia, Yuya Fujita et al.** · 2022-11-11

<details>
<summary>Abstract</summary>

The black-box nature of end-to-end speech translation (E2E ST) systems makes it difficult to understand how source language inputs are being mapped to the target language. To solve this problem, we would like to simultaneously generate automatic speech recognition (ASR) and ST predictions such that each source language word is explicitly mapped to a target language word. A major challenge arises from the fact that translation is a non-monotonic sequence transduction task due to word ordering differences between languages -- this clashes with the monotonic nature of ASR. Therefore, we propose to generate ST tokens out-of-order while remembering how to re-order them later. We achieve this by predicting a sequence of tuples consisting of a source word, the corresponding target words, and post-editing operations dictating the correct insertion points for the target word. We examine two variants of such operation sequences which enable generation of monotonic transcriptions and non-monotonic translations from the same speech input simultaneously. We apply our approach to offline and real-time streaming models, demonstrating that we can provide explainable translations without sacrificing quality or latency. In fact, the delayed re-ordering ability of our approach improves performance during streaming. As an added benefit, our method performs ASR and ST simultaneously, making it faster than using two separate systems to perform these tasks.

</details>

### [A Study on the Integration of Pre-trained SSL, ASR, LM and SLU Models for Spoken Language Understanding](2211.05869.md)
**Yifan Peng, Siddhant Arora, Yosuke Higuchi, Yushi Ueda et al.** · 2022-11-10

<details>
<summary>Abstract</summary>

Collecting sufficient labeled data for spoken language understanding (SLU) is expensive and time-consuming. Recent studies achieved promising results by using pre-trained models in low-resource scenarios. Inspired by this, we aim to ask: which (if any) pre-training strategies can improve performance across SLU benchmarks? To answer this question, we employ four types of pre-trained models and their combinations for SLU. We leverage self-supervised speech and language models (LM) pre-trained on large quantities of unpaired data to extract strong speech and text representations. We also explore using supervised models pre-trained on larger external automatic speech recognition (ASR) or SLU corpora. We conduct extensive experiments on the SLU Evaluation (SLUE) benchmark and observe self-supervised pre-trained models to be more powerful, with pre-trained LM and speech models being most beneficial for the Sentiment Analysis and Named Entity Recognition task, respectively.

</details>

### [Self-supervised learning with bi-label masked speech prediction for streaming multi-talker speech recognition](2211.05564.md)
**Zili Huang, Zhuo Chen, Naoyuki Kanda, Jian Wu et al.** · 2022-11-10

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL), which utilizes the input data itself for representation learning, has achieved state-of-the-art results for various downstream speech tasks. However, most of the previous studies focused on offline single-talker applications, with limited investigations in multi-talker cases, especially for streaming scenarios. In this paper, we investigate SSL for streaming multi-talker speech recognition, which generates transcriptions of overlapping speakers in a streaming fashion. We first observe that conventional SSL techniques do not work well on this task due to the poor representation of overlapping speech. We then propose a novel SSL training objective, referred to as bi-label masked speech prediction, which explicitly preserves representations of all speakers in overlapping speech. We investigate various aspects of the proposed system including data configuration and quantizer selection. The proposed SSL setup achieves substantially better word error rates on the LibriSpeechMix dataset.

</details>

### [Massively Multilingual ASR on 70 Languages: Tokenization, Architecture, and Generalization Capabilities](2211.05756.md)
**Andros Tjandra, Nayan Singhal, David Zhang, Ozlem Kalinli et al.** · 2022-11-10

<details>
<summary>Abstract</summary>

End-to-end multilingual ASR has become more appealing because of several reasons such as simplifying the training and deployment process and positive performance transfer from high-resource to low-resource languages. However, scaling up the number of languages, total hours, and number of unique tokens is not a trivial task. This paper explores large-scale multilingual ASR models on 70 languages. We inspect two architectures: (1) Shared embedding and output and (2) Multiple embedding and output model. In the shared model experiments, we show the importance of tokenization strategy across different languages. Later, we use our optimal tokenization strategy to train multiple embedding and output model to further improve our result. Our multilingual ASR achieves 13.9%-15.6% average WER relative improvement compared to monolingual models. We show that our multilingual ASR generalizes well on an unseen dataset and domain, achieving 9.5% and 7.5% WER on Multilingual Librispeech (MLS) with zero-shot and finetuning, respectively.

</details>

### [Improving Noisy Student Training on Non-target Domain Data for Automatic Speech Recognition](2211.04717.md)
**Yu Chen, Wen Ding, Junjie Lai** · 2022-11-09

<details>
<summary>Abstract</summary>

Noisy Student Training (NST) has recently demonstrated extremely strong performance in Automatic Speech Recognition(ASR). In this paper, we propose a data selection strategy named LM Filter to improve the performance of NST on non-target domain data in ASR tasks. Hypotheses with and without a Language Model are generated and the CER differences between them are utilized as a filter threshold. Results reveal that significant improvements of 10.4% compared with no data filtering baselines. We can achieve 3.31% CER in AISHELL-1 test set, which is best result from our knowledge without any other supervised data. We also perform evaluations on the supervised 1000 hour AISHELL-2 dataset and competitive results of 4.73% CER can be achieved.

</details>

### [Adaptive Multi-Corpora Language Model Training for Speech Recognition](2211.05121.md)
**Yingyi Ma, Zhe Liu, Xuedong Zhang** · 2022-11-09

<details>
<summary>Abstract</summary>

Neural network language model (NNLM) plays an essential role in automatic speech recognition (ASR) systems, especially in adaptation tasks when text-only data is available. In practice, an NNLM is typically trained on a combination of data sampled from multiple corpora. Thus, the data sampling strategy is important to the adaptation performance. Most existing works focus on designing static sampling strategies. However, each corpus may show varying impacts at different NNLM training stages. In this paper, we introduce a novel adaptive multi-corpora training algorithm that dynamically learns and adjusts the sampling probability of each corpus along the training process. The algorithm is robust to corpora sizes and domain relevance. Compared with static sampling strategy baselines, the proposed approach yields remarkable improvement by achieving up to relative 7% and 9% word error rate (WER) reductions on in-domain and out-of-domain adaptation tasks, respectively.

</details>

### [Speech separation with large-scale self-supervised learning](2211.05172.md)
**Zhuo Chen, Naoyuki Kanda, Jian Wu, Yu Wu et al.** · 2022-11-09

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) methods such as WavLM have shown promising speech separation (SS) results in small-scale simulation-based experiments. In this work, we extend the exploration of the SSL-based SS by massively scaling up both the pre-training data (more than 300K hours) and fine-tuning data (10K hours). We also investigate various techniques to efficiently integrate the pre-trained model with the SS network under a limited computation budget, including a low frame rate SSL model training setup and a fine-tuning scheme using only the part of the pre-trained model. Compared with a supervised baseline and the WavLM-based SS model using feature embeddings obtained with the previously released 94K hours trained WavLM, our proposed model obtains 15.9% and 11.2% of relative word error rate (WER) reductions, respectively, for a simulated far-field speech mixture test set. For conversation transcription on real meeting recordings using continuous speech separation, the proposed model achieves 6.8% and 10.6% of relative WER reductions over the purely supervised baseline on AMI and ICSI evaluation sets, respectively, while reducing the computational cost by 38%.

</details>

### [Robust Unstructured Knowledge Access in Conversational Dialogue with ASR Errors](2211.03990.md)
**Yik-Cheung Tam, Jiacheng Xu, Jiakai Zou, Zecheng Wang et al.** · 2022-11-08

<details>
<summary>Abstract</summary>

Performance of spoken language understanding (SLU) can be degraded with automatic speech recognition (ASR) errors. We propose a novel approach to improve SLU robustness by randomly corrupting clean training text with an ASR error simulator, followed by self-correcting the errors and minimizing the target classification loss in a joint manner. In the proposed error simulator, we leverage confusion networks generated from an ASR decoder without human transcriptions to generate a variety of error patterns for model training. We evaluate our approach on the DSTC10 challenge targeted for knowledge-grounded task-oriented conversational dialogues with ASR errors. Experimental results show the effectiveness of our proposed approach, boosting the knowledge-seeking turn detection (KTD) F1 significantly from 0.9433 to 0.9904. Knowledge cluster classification is boosted from 0.7924 to 0.9333 in Recall@1. After knowledge document re-ranking, our approach shows significant improvement in all knowledge selection metrics, from 0.7358 to 0.7806 in Recall@1, from 0.8301 to 0.9333 in Recall@5, and from 0.7798 to 0.8460 in MRR@5 on the test set. In the recent DSTC10 evaluation, our approach demonstrates significant improvement in knowledge selection, boosting Recall@1 from 0.495 to 0.7144 compared to the official baseline. Our source code is released in GitHub https://github.com/yctam/dstc10_track2_task2.git.

</details>

### [Comparative layer-wise analysis of self-supervised speech models](2211.03929.md)
**Ankita Pasad, Bowen Shi, Karen Livescu** · 2022-11-08

<details>
<summary>Abstract</summary>

Many self-supervised speech models, varying in their pre-training objective, input modality, and pre-training data, have been proposed in the last few years. Despite impressive successes on downstream tasks, we still have a limited understanding of the properties encoded by the models and the differences across models. In this work, we examine the intermediate representations for a variety of recent models. Specifically, we measure acoustic, phonetic, and word-level properties encoded in individual layers, using a lightweight analysis tool based on canonical correlation analysis (CCA). We find that these properties evolve across layers differently depending on the model, and the variations relate to the choice of pre-training objective. We further investigate the utility of our analyses for downstream tasks by comparing the property trends with performance on speech recognition and spoken language understanding tasks. We discover that CCA trends provide reliable guidance to choose layers of interest for downstream tasks and that single-layer performance often matches or improves upon using all layers, suggesting implications for more efficient use of pre-trained models.

</details>

### [Towards Improved Room Impulse Response Estimation for Speech Recognition](2211.04473.md)
**Anton Ratnarajah, Ishwarya Ananthabhotla, Vamsi Krishna Ithapu, Pablo Hoffmann et al.** · 2022-11-08

<details>
<summary>Abstract</summary>

We propose a novel approach for blind room impulse response (RIR) estimation systems in the context of a downstream application scenario, far-field automatic speech recognition (ASR). We first draw the connection between improved RIR estimation and improved ASR performance, as a means of evaluating neural RIR estimators. We then propose a generative adversarial network (GAN) based architecture that encodes RIR features from reverberant speech and constructs an RIR from the encoded features, and uses a novel energy decay relief loss to optimize for capturing energy-based properties of the input reverberant speech. We show that our model outperforms the state-of-the-art baselines on acoustic benchmarks (by 17\% on the energy decay relief and 22\% on an early-reflection energy metric), as well as in an ASR evaluation task (by 6.9\% in word error rate).

</details>

### [Cross-Attention is all you need: Real-Time Streaming Transformers for Personalised Speech Enhancement](2211.04346.md)
**Shucong Zhang, Malcolm Chadwick, Alberto Gil C. P. Ramos, S. Bhattacharya** · 2022-11-08

<details>
<summary>Abstract</summary>

Personalised speech enhancement (PSE), which extracts only the speech of a target user and removes everything else from a recorded audio clip, can potentially improve users' experiences of audio AI modules deployed in the wild. To support a large variety of downstream audio tasks, such as real-time ASR and audio-call enhancement, a PSE solution should operate in a streaming mode, i.e., input audio cleaning should happen in real-time with a small latency and real-time factor. Personalisation is typically achieved by extracting a target speaker's voice profile from an enrolment audio, in the form of a static embedding vector, and then using it to condition the output of a PSE model. However, a fixed target speaker embedding may not be optimal under all conditions. In this work, we present a streaming Transformer-based PSE model and propose a novel cross-attention approach that gives adaptive target speaker representations. We present extensive experiments and show that our proposed cross-attention approach outperforms competitive baselines consistently, even when our model is only approximately half the size.

</details>

### [Streaming, fast and accurate on-device Inverse Text Normalization for Automatic Speech Recognition](2211.03721.md)
**Yashesh Gaur, Nick Kibre, Jian Xue, Kangyuan Shu et al.** · 2022-11-07

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems typically yield output in lexical form. However, humans prefer a written form output. To bridge this gap, ASR systems usually employ Inverse Text Normalization (ITN). In previous works, Weighted Finite State Transducers (WFST) have been employed to do ITN. WFSTs are nicely suited to this task but their size and run-time costs can make deployment on embedded applications challenging. In this paper, we describe the development of an on-device ITN system that is streaming, lightweight & accurate. At the core of our system is a streaming transformer tagger, that tags lexical tokens from ASR. The tag informs which ITN category might be applied, if at all. Following that, we apply an ITN-category-specific WFST, only on the tagged text, to reliably perform the ITN conversion. We show that the proposed ITN solution performs equivalent to strong baselines, while being significantly smaller in size and retaining customization capabilities.

</details>

### [End-to-End Evaluation of a Spoken Dialogue System for Learning Basic Mathematics](2211.03511.md)
**Eda Okur, Saurav Sahay, Roddy Fuentes Alba, Lama Nachman** · 2022-11-07

<details>
<summary>Abstract</summary>

The advances in language-based Artificial Intelligence (AI) technologies applied to build educational applications can present AI for social-good opportunities with a broader positive impact. Across many disciplines, enhancing the quality of mathematics education is crucial in building critical thinking and problem-solving skills at younger ages. Conversational AI systems have started maturing to a point where they could play a significant role in helping students learn fundamental math concepts. This work presents a task-oriented Spoken Dialogue System (SDS) built to support play-based learning of basic math concepts for early childhood education. The system has been evaluated via real-world deployments at school while the students are practicing early math concepts with multimodal interactions. We discuss our efforts to improve the SDS pipeline built for math learning, for which we explore utilizing MathBERT representations for potential enhancement to the Natural Language Understanding (NLU) module. We perform an end-to-end evaluation using real-world deployment outputs from the Automatic Speech Recognition (ASR), Intent Recognition, and Dialogue Manager (DM) components to understand how error propagation affects the overall performance in real-world scenarios.

</details>

### [Bridging Speech and Textual Pre-trained Models with Unsupervised ASR](2211.03025.md)
**Jiatong Shi, Chan-Jan Hsu, Holam Chung, Dongji Gao et al.** · 2022-11-06

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) is a task aiming to extract high-level semantics from spoken utterances. Previous works have investigated the use of speech self-supervised models and textual pre-trained models, which have shown reasonable improvements to various SLU tasks. However, because of the mismatched modalities between speech signals and text tokens, previous methods usually need complex designs of the frameworks. This work proposes a simple yet efficient unsupervised paradigm that connects speech and textual pre-trained models, resulting in an unsupervised speech-to-semantic pre-trained model for various tasks in SLU. To be specific, we propose to use unsupervised automatic speech recognition (ASR) as a connector that bridges different modalities used in speech and textual pre-trained models. Our experiments show that unsupervised ASR itself can improve the representations from speech self-supervised models. More importantly, it is shown as an efficient connector between speech and textual pre-trained models, improving the performances of five different SLU tasks. Notably, on spoken question answering, we reach the state-of-the-art result over the challenging NMSQA benchmark.

</details>

### [LAMASSU: Streaming Language-Agnostic Multilingual Speech Recognition and Translation Using Neural Transducers](2211.02809.md)
**Peidong Wang, Eric Sun, Jian Xue, Yu Wu et al.** · 2022-11-05

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) and speech translation (ST) can both use neural transducers as the model structure. It is thus possible to use a single transducer model to perform both tasks. In real-world applications, such joint ASR and ST models may need to be streaming and do not require source language identification (i.e. language-agnostic). In this paper, we propose LAMASSU, a streaming language-agnostic multilingual speech recognition and translation model using neural transducers. Based on the transducer model structure, we propose four methods, a unified joint and prediction network for multilingual output, a clustered multilingual encoder, target language identification for encoder, and connectionist temporal classification regularization. Experimental results show that LAMASSU not only drastically reduces the model size but also reaches the performances of monolingual ASR and bilingual ST models.

</details>

### [Stutter-TTS: Controlled Synthesis and Improved Recognition of Stuttered Speech](2211.09731.md)
**Xin Zhang, Iván Vallés-Pérez, Andreas Stolcke, Chengzhu Yu et al.** · 2022-11-04

<details>
<summary>Abstract</summary>

Stuttering is a speech disorder where the natural flow of speech is interrupted by blocks, repetitions or prolongations of syllables, words and phrases. The majority of existing automatic speech recognition (ASR) interfaces perform poorly on utterances with stutter, mainly due to lack of matched training data. Synthesis of speech with stutter thus presents an opportunity to improve ASR for this type of speech. We describe Stutter-TTS, an end-to-end neural text-to-speech model capable of synthesizing diverse types of stuttering utterances. We develop a simple, yet effective prosody-control strategy whereby additional tokens are introduced into source text during training to represent specific stuttering characteristics. By choosing the position of the stutter tokens, Stutter-TTS allows word-level control of where stuttering occurs in the synthesized utterance. We are able to synthesize stutter events with high accuracy (F1-scores between 0.63 and 0.84, depending on stutter type). By fine-tuning an ASR model on synthetic stuttered speech we are able to reduce word error by 5.7% relative on stuttered utterances, with only minor (<0.2% relative) degradation for fluent utterances.

</details>

### [Resource-Efficient Transfer Learning From Speech Foundation Model Using Hierarchical Feature Fusion](2211.02712.md)
**Zhouyuan Huo, Khe Chai Sim, Bo Li, Dongseong Hwang et al.** · 2022-11-04

<details>
<summary>Abstract</summary>

Self-supervised pre-training of a speech foundation model, followed by supervised fine-tuning, has shown impressive quality improvements on automatic speech recognition (ASR) tasks. Fine-tuning separate foundation models for many downstream tasks are expensive since the foundation model is usually very big. Parameter-efficient fine-tuning methods (e.g. adapter, sparse update methods) offer an alternative paradigm where a small set of parameters are updated to adapt the foundation model to new tasks. However, these methods still suffer from a high computational memory cost and slow training speed because they require backpropagation through the entire neural network at each step. In the paper, we analyze the performance of features at different layers of a foundation model on the speech recognition task and propose a novel hierarchical feature fusion method for resource-efficient transfer learning from speech foundation models. Experimental results show that the proposed method can achieve better performance on speech recognition task than existing algorithms with fewer number of trainable parameters, less computational memory cost and faster training speed. After combining with Adapters at all layers, the proposed method can achieve the same performance as fine-tuning the whole model with $97\%$ fewer trainable encoder parameters and $53\%$ faster training speed.

</details>

### [Biased Self-supervised learning for ASR](2211.02536.md)
**Florian L. Kreyssig, Yangyang Shi, Jinxi Guo, Leda Sari et al.** · 2022-11-04

<details>
<summary>Abstract</summary>

Self-supervised learning via masked prediction pre-training (MPPT) has shown impressive performance on a range of speech-processing tasks. This paper proposes a method to bias self-supervised learning towards a specific task. The core idea is to slightly finetune the model that is used to obtain the target sequence. This leads to better performance and a substantial increase in training speed. Furthermore, this paper proposes a variant of MPPT that allows low-footprint streaming models to be trained effectively by computing the MPPT loss on masked and unmasked frames. These approaches are evaluated for automatic speech recognition on the Librispeech corpus, where 100 hours of data served as the labelled data and 860 hours as the unlabelled data. The biased training outperforms the unbiased training by 15.5% after 250k updates and 23.8% after 100k updates on test-other. For the streaming models, the pre-training approach yields a reduction in word error rate of 44.1%.

</details>

### [A Weakly-Supervised Streaming Multilingual Speech Model with Truly Zero-Shot Capability](2211.02499.md)
**Jian Xue, Peidong Wang, Jinyu Li, Eric Sun** · 2022-11-04

<details>
<summary>Abstract</summary>

In this paper, we introduce our work of building a Streaming Multilingual Speech Model (SM2), which can transcribe or translate multiple spoken languages into texts of the target language. The backbone of SM2 is Transformer Transducer, which has high streaming capability. Instead of human labeled speech translation (ST) data, SM2 models are trained using weakly supervised data generated by converting the transcriptions in speech recognition corpora with a machine translation service. With 351 thousand hours of anonymized speech training data from 25 languages, SM2 models achieve comparable or even better ST quality than some recent popular large-scale non-streaming speech models. More importantly, we show that SM2 has the truly zero-shot capability when expanding to new target languages, yielding high quality ST results for {source-speech, target-text} pairs that are not seen during training.

</details>

### [Minimum Latency Training of Sequence Transducers for Streaming End-to-End Speech Recognition](2211.02333.md)
**Yusuke Shinohara, Shinji Watanabe** · 2022-11-04

<details>
<summary>Abstract</summary>

Sequence transducers, such as the RNN-T and the Conformer-T, are one of the most promising models of end-to-end speech recognition, especially in streaming scenarios where both latency and accuracy are important. Although various methods, such as alignment-restricted training and FastEmit, have been studied to reduce the latency, latency reduction is often accompanied with a significant degradation in accuracy. We argue that this suboptimal performance might be caused because none of the prior methods explicitly model and reduce the latency. In this paper, we propose a new training method to explicitly model and reduce the latency of sequence transducer models. First, we define the expected latency at each diagonal line on the lattice, and show that its gradient can be computed efficiently within the forward-backward algorithm. Then we augment the transducer loss with this expected latency, so that an optimal trade-off between latency and accuracy is achieved. Experimental results on the WSJ dataset show that the proposed minimum latency training reduces the latency of causal Conformer-T from 220 ms to 27 ms within a WER degradation of 0.7%, and outperforms conventional alignment-restricted training (110 ms) and FastEmit (67 ms) methods.

</details>

### [Streaming Audio-Visual Speech Recognition with Alignment Regularization](2211.02133.md)
**Pingchuan Ma, Niko Moritz, Stavros Petridis, Christian Fuegen et al.** · 2022-11-03

<details>
<summary>Abstract</summary>

In this work, we propose a streaming AV-ASR system based on a hybrid connectionist temporal classification (CTC)/attention neural network architecture. The audio and the visual encoder neural networks are both based on the conformer architecture, which is made streamable using chunk-wise self-attention (CSA) and causal convolution. Streaming recognition with a decoder neural network is realized by using the triggered attention technique, which performs time-synchronous decoding with joint CTC/attention scoring. Additionally, we propose a novel alignment regularization technique that promotes synchronization of the audio and visual encoder, which in turn results in better word error rates (WERs) at all SNR levels for streaming and offline AV-ASR models. The proposed AV-ASR model achieves WERs of 2.0% and 2.6% on the Lip Reading Sentences 3 (LRS3) dataset in an offline and online setup, respectively, which both present state-of-the-art results when no external training data are used.

</details>

### [Probing Statistical Representations For End-To-End ASR](2211.01993.md)
**Anna Ollerenshaw, Md Asif Jalal, Thomas Hain** · 2022-11-03

<details>
<summary>Abstract</summary>

End-to-End automatic speech recognition (ASR) models aim to learn a generalised speech representation to perform recognition. In this domain there is little research to analyse internal representation dependencies and their relationship to modelling approaches. This paper investigates cross-domain language model dependencies within transformer architectures using SVCCA and uses these insights to exploit modelling approaches. It was found that specific neural representations within the transformer layers exhibit correlated behaviour which impacts recognition performance. Altogether, this work provides analysis of the modelling approaches affecting contextual dependencies and ASR performance, and can be used to create or adapt better performing End-to-End ASR models and also for downstream tasks.

</details>

### [Adversarial Data Augmentation Using VAE-GAN for Disordered Speech Recognition](2211.01646.md)
**Zengrui Jin, Xurong Xie, Mengzhe Geng, Tianzi Wang et al.** · 2022-11-03

<details>
<summary>Abstract</summary>

Automatic recognition of disordered speech remains a highly challenging task to date. The underlying neuro-motor conditions, often compounded with co-occurring physical disabilities, lead to the difficulty in collecting large quantities of impaired speech required for ASR system development. This paper presents novel variational auto-encoder generative adversarial network (VAE-GAN) based personalized disordered speech augmentation approaches that simultaneously learn to encode, generate and discriminate synthesized impaired speech. Separate latent features are derived to learn dysarthric speech characteristics and phoneme context representations. Self-supervised pre-trained Wav2vec 2.0 embedding features are also incorporated. Experiments conducted on the UASpeech corpus suggest the proposed adversarial data augmentation approach consistently outperformed the baseline speed perturbation and non-VAE GAN augmentation methods with trained hybrid TDNN and End-to-end Conformer systems. After LHUC speaker adaptation, the best system using VAE-GAN based augmentation produced an overall WER of 27.78% on the UASpeech test set of 16 dysarthric speakers, and the lowest published WER of 57.31% on the subset of speakers with "Very Low" intelligibility.

</details>

### [Leveraging Domain Features for Detecting Adversarial Attacks Against Deep Speech Recognition in Noise](2211.01621.md)
**Christian Heider Nielsen, Zheng-Hua Tan** · 2022-11-03

<details>
<summary>Abstract</summary>

In recent years, significant progress has been made in deep model-based automatic speech recognition (ASR), leading to its widespread deployment in the real world. At the same time, adversarial attacks against deep ASR systems are highly successful. Various methods have been proposed to defend ASR systems from these attacks. However, existing classification based methods focus on the design of deep learning models while lacking exploration of domain specific features. This work leverages filter bank-based features to better capture the characteristics of attacks for improved detection. Furthermore, the paper analyses the potentials of using speech and non-speech parts separately in detecting adversarial attacks. In the end, considering adverse environments where ASR systems may be deployed, we study the impact of acoustic noise of various types and signal-to-noise ratios. Extensive experiments show that the inverse filter bank features generally perform better in both clean and noisy environments, the detection is effective using either speech or non-speech part, and the acoustic noise can largely degrade the detection performance.

</details>

### [Phonetic-assisted Multi-Target Units Modeling for Improving Conformer-Transducer ASR system](2211.01571.md)
**Li Li, Dongxing Xu, Haoran Wei, Yanhua Long** · 2022-11-03

<details>
<summary>Abstract</summary>

Exploiting effective target modeling units is very important and has always been a concern in end-to-end automatic speech recognition (ASR). In this work, we propose a phonetic-assisted multi target units (PMU) modeling approach, to enhance the Conformer-Transducer ASR system in a progressive representation learning manner. Specifically, PMU first uses the pronunciation-assisted subword modeling (PASM) and byte pair encoding (BPE) to produce phonetic-induced and text-induced target units separately; Then, three new frameworks are investigated to enhance the acoustic encoder, including a basic PMU, a paraCTC and a pcaCTC, they integrate the PASM and BPE units at different levels for CTC and transducer multi-task training. Experiments on both LibriSpeech and accented ASR tasks show that, the proposed PMU significantly outperforms the conventional BPE, it reduces the WER of LibriSpeech clean, other, and six accented ASR testsets by relative 12.7%, 6.0% and 7.7%, respectively.

</details>

### [Losses Can Be Blessings: Routing Self-Supervised Speech Representations Towards Efficient Multilingual and Multitask Speech Processing](2211.01522.md)
**Yonggan Fu, Yang Zhang, Kaizhi Qian, Zhifan Ye et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) for rich speech representations has achieved empirical success in low-resource Automatic Speech Recognition (ASR) and other speech processing tasks, which can mitigate the necessity of a large amount of transcribed speech and thus has driven a growing demand for on-device ASR and other speech processing. However, advanced speech SSL models have become increasingly large, which contradicts the limited on-device resources. This gap could be more severe in multilingual/multitask scenarios requiring simultaneously recognizing multiple languages or executing multiple speech processing tasks. Additionally, strongly overparameterized speech SSL models tend to suffer from overfitting when being finetuned on low-resource speech corpus. This work aims to enhance the practical usage of speech SSL models towards a win-win in both enhanced efficiency and alleviated overfitting via our proposed S$^3$-Router framework, which for the first time discovers that simply discarding no more than 10\% of model weights via only finetuning model connections of speech SSL models can achieve better accuracy over standard weight finetuning on downstream speech processing tasks. More importantly, S$^3$-Router can serve as an all-in-one technique to enable (1) a new finetuning scheme, (2) an efficient multilingual/multitask solution, (3) a state-of-the-art ASR pruning technique, and (4) a new tool to quantitatively analyze the learned speech representation. We believe S$^3$-Router has provided a new perspective for practical deployment of speech SSL models. Our codes are available at: https://github.com/GATECH-EIC/S3-Router.

</details>

### [Towards Zero-Shot Code-Switched Speech Recognition](2211.01458.md)
**Brian Yan, Matthew Wiesner, Ondrej Klejch, Preethi Jyothi et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

In this work, we seek to build effective code-switched (CS) automatic speech recognition systems (ASR) under the zero-shot setting where no transcribed CS speech data is available for training. Previously proposed frameworks which conditionally factorize the bilingual task into its constituent monolingual parts are a promising starting point for leveraging monolingual data efficiently. However, these methods require the monolingual modules to perform language segmentation. That is, each monolingual module has to simultaneously detect CS points and transcribe speech segments of one language while ignoring those of other languages -- not a trivial task. We propose to simplify each monolingual module by allowing them to transcribe all speech segments indiscriminately with a monolingual script (i.e. transliteration). This simple modification passes the responsibility of CS point detection to subsequent bilingual modules which determine the final output by considering multiple monolingual transliterations along with external language model information. We apply this transliteration-based approach in an end-to-end differentiable neural network and demonstrate its efficacy for zero-shot CS ASR on Mandarin-English SEAME test sets.

</details>

### [Variable Attention Masking for Configurable Transformer Transducer Speech Recognition](2211.01438.md)
**Pawel Swietojanski, Stefan Braun, Dogan Can, Thiago Fraga da Silva et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

This work studies the use of attention masking in transformer transducer based speech recognition for building a single configurable model for different deployment scenarios. We present a comprehensive set of experiments comparing fixed masking, where the same attention mask is applied at every frame, with chunked masking, where the attention mask for each frame is determined by chunk boundaries, in terms of recognition accuracy and latency. We then explore the use of variable masking, where the attention masks are sampled from a target distribution at training time, to build models that can work in different configurations. Finally, we investigate how a single configurable model can be used to perform both first pass streaming recognition and second pass acoustic rescoring. Experiments show that chunked masking achieves a better accuracy vs latency trade-off compared to fixed masking, both with and without FastEmit. We also show that variable masking improves the accuracy by up to 8% relative in the acoustic re-scoring scenario.

</details>

### [Intermediate Fine-Tuning Using Imperfect Synthetic Speech for Improving Electrolaryngeal Speech Recognition](2211.01079.md)
**Lester Phillip Violeta, Ding Ma, Wen-Chin Huang, Tomoki Toda** · 2022-11-02

<details>
<summary>Abstract</summary>

Research on automatic speech recognition (ASR) systems for electrolaryngeal speakers has been relatively unexplored due to small datasets. When training data is lacking in ASR, a large-scale pretraining and fine tuning framework is often sufficient to achieve high recognition rates; however, in electrolaryngeal speech, the domain shift between the pretraining and fine-tuning data is too large to overcome, limiting the maximum improvement of recognition rates. To resolve this, we propose an intermediate fine-tuning step that uses imperfect synthetic speech to close the domain shift gap between the pretraining and target data. Despite the imperfect synthetic data, we show the effectiveness of this on electrolaryngeal speech datasets, with improvements of 6.1% over the baseline that did not use imperfect synthetic speech. Results show how the intermediate fine-tuning stage focuses on learning the high-level inherent features of the imperfect synthetic data rather than the low-level features such as intelligibility.

</details>

### [Monolingual Recognizers Fusion for Code-switching Speech Recognition](2211.01046.md)
**Tongtong Song, Qiang Xu, Haoyu Lu, Longbiao Wang et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

The bi-encoder structure has been intensively investigated in code-switching (CS) automatic speech recognition (ASR). However, most existing methods require the structures of two monolingual ASR models (MAMs) should be the same and only use the encoder of MAMs. This leads to the problem that pre-trained MAMs cannot be timely and fully used for CS ASR. In this paper, we propose a monolingual recognizers fusion method for CS ASR. It has two stages: the speech awareness (SA) stage and the language fusion (LF) stage. In the SA stage, acoustic features are mapped to two language-specific predictions by two independent MAMs. To keep the MAMs focused on their own language, we further extend the language-aware training strategy for the MAMs. In the LF stage, the BELM fuses two language-specific predictions to get the final prediction. Moreover, we propose a text simulation strategy to simplify the training process of the BELM and reduce reliance on CS data. Experiments on a Mandarin-English corpus show the efficiency of the proposed method. The mix error rate is significantly reduced on the test set after using open-source pre-trained MAMs.

</details>

### [Fast-U2++: Fast and Accurate End-to-End Speech Recognition in Joint CTC/Attention Frames](2211.00941.md)
**Chengdong Liang, Xiao-Lei Zhang, BinBin Zhang, Di Wu et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

Recently, the unified streaming and non-streaming two-pass (U2/U2++) end-to-end model for speech recognition has shown great performance in terms of streaming capability, accuracy and latency. In this paper, we present fast-U2++, an enhanced version of U2++ to further reduce partial latency. The core idea of fast-U2++ is to output partial results of the bottom layers in its encoder with a small chunk, while using a large chunk in the top layers of its encoder to compensate the performance degradation caused by the small chunk. Moreover, we use knowledge distillation method to reduce the token emission latency. We present extensive experiments on Aishell-1 dataset. Experiments and ablation studies show that compared to U2++, fast-U2++ reduces model latency from 320ms to 80ms, and achieves a character error rate (CER) of 5.06% with a streaming setup.

</details>

### [Conversation-oriented ASR with multi-look-ahead CBS architecture](2211.00858.md)
**Huaibo Zhao, Shinya Fujie, Tetsuji Ogawa, Jin Sakuma et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

During conversations, humans are capable of inferring the intention of the speaker at any point of the speech to prepare the following action promptly. Such ability is also the key for conversational systems to achieve rhythmic and natural conversation. To perform this, the automatic speech recognition (ASR) used for transcribing the speech in real-time must achieve high accuracy without delay. In streaming ASR, high accuracy is assured by attending to look-ahead frames, which leads to delay increments. To tackle this trade-off issue, we propose a multiple latency streaming ASR to achieve high accuracy with zero look-ahead. The proposed system contains two encoders that operate in parallel, where a primary encoder generates accurate outputs utilizing look-ahead frames, and the auxiliary encoder recognizes the look-ahead portion of the primary encoder without look-ahead. The proposed system is constructed based on contextual block streaming (CBS) architecture, which leverages block processing and has a high affinity for the multiple latency architecture. Various methods are also studied for architecting the system, including shifting the network to perform as different encoders; as well as generating both encoders' outputs in one encoding pass.

</details>

### [More Speaking or More Speakers?](2211.00854.md)
**Dan Berrebbi, Ronan Collobert, Navdeep Jaitly, Tatiana Likhomanenko** · 2022-11-02

<details>
<summary>Abstract</summary>

Self-training (ST) and self-supervised learning (SSL) methods have demonstrated strong improvements in automatic speech recognition (ASR). In spite of these advances, to the best of our knowledge, there is no analysis of how the composition of the labelled and unlabelled datasets used in these methods affects the results. In this work we aim to analyse the effect of number of speakers in the training data on a recent SSL algorithm (wav2vec 2.0), and a recent ST algorithm (slimIPL). We perform a systematic analysis on both labeled and unlabeled data by varying the number of speakers while keeping the number of hours fixed and vice versa. Our findings suggest that SSL requires a large amount of unlabeled data to produce high accuracy results, while ST requires a sufficient number of speakers in the labelled data, especially in the low-regime setting. In this manner these two approaches improve supervised learning in different regimes of data composition.

</details>

### [InterMPL: Momentum Pseudo-Labeling with Intermediate CTC Loss](2211.00795.md)
**Yosuke Higuchi, Tetsuji Ogawa, Tetsunori Kobayashi, Shinji Watanabe** · 2022-11-02

<details>
<summary>Abstract</summary>

This paper presents InterMPL, a semi-supervised learning method of end-to-end automatic speech recognition (ASR) that performs pseudo-labeling (PL) with intermediate supervision. Momentum PL (MPL) trains a connectionist temporal classification (CTC)-based model on unlabeled data by continuously generating pseudo-labels on the fly and improving their quality. In contrast to autoregressive formulations, such as the attention-based encoder-decoder and transducer, CTC is well suited for MPL, or PL-based semi-supervised ASR in general, owing to its simple/fast inference algorithm and robustness against generating collapsed labels. However, CTC generally yields inferior performance than the autoregressive models due to the conditional independence assumption, thereby limiting the performance of MPL. We propose to enhance MPL by introducing intermediate loss, inspired by the recent advances in CTC-based modeling. Specifically, we focus on self-conditional and hierarchical conditional CTC, that apply auxiliary CTC losses to intermediate layers such that the conditional independence assumption is explicitly relaxed. We also explore how pseudo-labels should be generated and used as supervision for intermediate losses. Experimental results in different semi-supervised settings demonstrate that the proposed approach outperforms MPL and improves an ASR model by up to a 12.1% absolute performance gain. In addition, our detailed analysis validates the importance of the intermediate loss.

</details>

### [BECTRA: Transducer-based End-to-End ASR with BERT-Enhanced Encoder](2211.00792.md)
**Yosuke Higuchi, Tetsuji Ogawa, Tetsunori Kobayashi, Shinji Watanabe** · 2022-11-02

<details>
<summary>Abstract</summary>

We present BERT-CTC-Transducer (BECTRA), a novel end-to-end automatic speech recognition (E2E-ASR) model formulated by the transducer with a BERT-enhanced encoder. Integrating a large-scale pre-trained language model (LM) into E2E-ASR has been actively studied, aiming to utilize versatile linguistic knowledge for generating accurate text. One crucial factor that makes this integration challenging lies in the vocabulary mismatch; the vocabulary constructed for a pre-trained LM is generally too large for E2E-ASR training and is likely to have a mismatch against a target ASR domain. To overcome such an issue, we propose BECTRA, an extended version of our previous BERT-CTC, that realizes BERT-based E2E-ASR using a vocabulary of interest. BECTRA is a transducer-based model, which adopts BERT-CTC for its encoder and trains an ASR-specific decoder using a vocabulary suitable for a target task. With the combination of the transducer and BERT-CTC, we also propose a novel inference algorithm for taking advantage of both autoregressive and non-autoregressive decoding. Experimental results on several ASR tasks, varying in amounts of data, speaking styles, and languages, demonstrate that BECTRA outperforms BERT-CTC by effectively dealing with the vocabulary mismatch while exploiting BERT knowledge.

</details>

### [Unified End-to-End Speech Recognition and Endpointing for Fast and Efficient Speech Systems](2211.00786.md)
**Shaan Bijwadia, Shuo-yiin Chang, Bo Li, Tara Sainath et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems typically rely on an external endpointer (EP) model to identify speech boundaries. In this work, we propose a method to jointly train the ASR and EP tasks in a single end-to-end (E2E) multitask model, improving EP quality by optionally leveraging information from the ASR audio encoder. We introduce a "switch" connection, which trains the EP to consume either the audio frames directly or low-level latent representations from the ASR model. This results in a single E2E model that can be used during inference to perform frame filtering at low cost, and also make high quality end-of-query (EOQ) predictions based on ongoing ASR computation. We present results on a voice search test set showing that, compared to separate single-task models, this approach reduces median endpoint latency by 120 ms (30.8% reduction), and 90th percentile latency by 170 ms (23.0% reduction), without regressing word error rate. For continuous recognition, WER improves by 10.6% (relative).

</details>

### [Avoid Overthinking in Self-Supervised Models for Speech Recognition](2211.08989.md)
**Dan Berrebbi, Brian Yan, Shinji Watanabe** · 2022-11-01

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models reshaped our approach to speech, language and vision. However their huge size and the opaque relations between their layers and tasks result in slow inference and network overthinking, where predictions made from the last layer of large models is worse than those made from intermediate layers. Early exit (EE) strategies can solve both issues by dynamically reducing computations at inference time for certain samples. Although popular for classification tasks in vision and language, EE has seen less use for sequence-to-sequence speech recognition (ASR) tasks where outputs from early layers are often degenerate. This challenge is further compounded when speech SSL models are applied on out-of-distribution (OOD) data. This paper first shows that SSL models do overthinking in ASR. We then motivate further research in EE by computing an optimal bound for performance versus speed trade-offs. To approach this bound we propose two new strategies for ASR: (1) we adapt the recently proposed patience strategy to ASR; and (2) we design a new EE strategy specific to ASR that performs better than all strategies previously introduced.

</details>

### [A Comparative Study on Multichannel Speaker-Attributed Automatic Speech Recognition in Multi-party Meetings](2211.00511.md)
**Mohan Shi, Jie Zhang, Zhihao Du, Fan Yu et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

Speaker-attributed automatic speech recognition (SA-ASR) in multi-party meeting scenarios is one of the most valuable and challenging ASR task. It was shown that single-channel frame-level diarization with serialized output training (SC-FD-SOT), single-channel word-level diarization with SOT (SC-WD-SOT) and joint training of single-channel target-speaker separation and ASR (SC-TS-ASR) can be exploited to partially solve this problem. In this paper, we propose three corresponding multichannel (MC) SA-ASR approaches, namely MC-FD-SOT, MC-WD-SOT and MC-TS-ASR. For different tasks/models, different multichannel data fusion strategies are considered, including channel-level cross-channel attention for MC-FD-SOT, frame-level cross-channel attention for MC-WD-SOT and neural beamforming for MC-TS-ASR. Results on the AliMeeting corpus reveal that our proposed models can consistently outperform the corresponding single-channel counterparts in terms of the speaker-dependent character error rate.

</details>

### [Adapting self-supervised models to multi-talker speech recognition using speaker embeddings](2211.00482.md)
**Zili Huang, Desh Raj, Paola García, Sanjeev Khudanpur** · 2022-11-01

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) methods which learn representations of data without explicit supervision have gained popularity in speech-processing tasks, particularly for single-talker applications. However, these models often have degraded performance for multi-talker scenarios -- possibly due to the domain mismatch -- which severely limits their use for such applications. In this paper, we investigate the adaptation of upstream SSL models to the multi-talker automatic speech recognition (ASR) task under two conditions. First, when segmented utterances are given, we show that adding a target speaker extraction (TSE) module based on enrollment embeddings is complementary to mixture-aware pre-training. Second, for unsegmented mixtures, we propose a novel joint speaker modeling (JSM) approach, which aggregates information from all speakers in the mixture through their embeddings. With controlled experiments on Libri2Mix, we show that using speaker embeddings provides relative WER improvements of 9.1% and 42.1% over strong baselines for the segmented and unsegmented cases, respectively. We also demonstrate the effectiveness of our models for real conversational mixtures through experiments on the AMI dataset.

</details>

### [Speech-text based multi-modal training with bidirectional attention for improved speech recognition](2211.00325.md)
**Yuhang Yang, Haihua Xu, Hao Huang, Eng Siong Chng et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

To let the state-of-the-art end-to-end ASR model enjoy data efficiency, as well as much more unpaired text data by multi-modal training, one needs to address two problems: 1) the synchronicity of feature sampling rates between speech and language (aka text data); 2) the homogeneity of the learned representations from two encoders. In this paper we propose to employ a novel bidirectional attention mechanism (BiAM) to jointly learn both ASR encoder (bottom layers) and text encoder with a multi-modal learning method. The BiAM is to facilitate feature sampling rate exchange, realizing the quality of the transformed features for the one kind to be measured in another space, with diversified objective functions. As a result, the speech representations are enriched with more linguistic information, while the representations generated by the text encoder are more similar to corresponding speech ones, and therefore the shared ASR models are more amenable for unpaired text data pretraining. To validate the efficacy of the proposed method, we perform two categories of experiments with or without extra unpaired text data. Experimental results on Librispeech corpus show it can achieve up to 6.15% word error rate reduction (WERR) with only paired data learning, while 9.23% WERR when more unpaired text data is employed.

</details>

### [TrimTail: Low-Latency Streaming ASR with Simple but Effective Spectrogram-Level Length Penalty](2211.00522.md)
**Xingchen Song, Di Wu, Zhiyong Wu, Binbin Zhang et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

In this paper, we present TrimTail, a simple but effective emission regularization method to improve the latency of streaming ASR models. The core idea of TrimTail is to apply length penalty (i.e., by trimming trailing frames, see Fig. 1-(b)) directly on the spectrogram of input utterances, which does not require any alignment. We demonstrate that TrimTail is computationally cheap and can be applied online and optimized with any training loss or any model architecture on any dataset without any extra effort by applying it on various end-to-end streaming ASR networks either trained with CTC loss [1] or Transducer loss [2]. We achieve 100 $\sim$ 200ms latency reduction with equal or even better accuracy on both Aishell-1 and Librispeech. Moreover, by using TrimTail, we can achieve a 400ms algorithmic improvement of User Sensitive Delay (USD) with an accuracy loss of less than 0.2.

</details>

### [Joint Audio/Text Training for Transformer Rescorer of Streaming Speech Recognition](2211.00174.md)
**Suyoun Kim, Ke Li, Lucas Kabela, Rongqing Huang et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

Recently, there has been an increasing interest in two-pass streaming end-to-end speech recognition (ASR) that incorporates a 2nd-pass rescoring model on top of the conventional 1st-pass streaming ASR model to improve recognition accuracy while keeping latency low. One of the latest 2nd-pass rescoring model, Transformer Rescorer, takes the n-best initial outputs and audio embeddings from the 1st-pass model, and then choose the best output by re-scoring the n-best initial outputs. However, training this Transformer Rescorer requires expensive paired audio-text training data because the model uses audio embeddings as input. In this work, we present our Joint Audio/Text training method for Transformer Rescorer, to leverage unpaired text-only data which is relatively cheaper than paired audio-text data. We evaluate Transformer Rescorer with our Joint Audio/Text training on Librispeech dataset as well as our large-scale in-house dataset and show that our training method can improve word error rate (WER) significantly compared to standard Transformer Rescorer without requiring any extra model parameters or latency.

</details>

### [Audio-Visual Speech Enhancement and Separation by Utilizing Multi-Modal Self-Supervised Embeddings](2210.17456.md)
**I-Chun Chern, Kuo-Hsuan Hung, Yi-Ting Chen, Tassadaq Hussain et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

AV-HuBERT, a multi-modal self-supervised learning model, has been shown to be effective for categorical problems such as automatic speech recognition and lip-reading. This suggests that useful audio-visual speech representations can be obtained via utilizing multi-modal self-supervised embeddings. Nevertheless, it is unclear if such representations can be generalized to solve real-world multi-modal AV regression tasks, such as audio-visual speech enhancement (AVSE) and audio-visual speech separation (AVSS). In this study, we leveraged the pre-trained AV-HuBERT model followed by an SE module for AVSE and AVSS. Comparative experimental results demonstrate that our proposed model performs better than the state-of-the-art AVSE and traditional audio-only SE models. In summary, our results confirm the effectiveness of our proposed model for the AVSS task with proper fine-tuning strategies, demonstrating that multi-modal self-supervised embeddings obtained from AV-HuBERT can be generalized to audio-visual regression tasks.

</details>

### [DiaCorrect: End-to-end error correction for speaker diarization](2210.17189.md)
**Jiangyu Han, Yuhang Cao, Heng Lu, Yanhua Long** · 2022-10-31

<details>
<summary>Abstract</summary>

In recent years, speaker diarization has attracted widespread attention. To achieve better performance, some studies propose to diarize speech in multiple stages. Although these methods might bring additional benefits, most of them are quite complex. Motivated by spelling correction in automatic speech recognition (ASR), in this paper, we propose an end-to-end error correction framework, termed DiaCorrect, to refine the initial diarization results in a simple but efficient way. By exploiting the acoustic interactions between input mixture and its corresponding speaker activity, DiaCorrect could automatically adapt the initial speaker activity to minimize the diarization errors. Without bells and whistles, experiments on LibriSpeech based 2-speaker meeting-like data show that, the self-attentitive end-to-end neural diarization (SA-EEND) baseline with DiaCorrect could reduce its diarization error rate (DER) by over 62.4% from 12.31% to 4.63%. Our source code is available online at https://github.com/jyhan03/diacorrect.

</details>

### [Predicting Multi-Codebook Vector Quantization Indexes for Knowledge Distillation](2211.00508.md)
**Liyong Guo, Xiaoyu Yang, Quandong Wang, Yuxiang Kong et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

Knowledge distillation(KD) is a common approach to improve model performance in automatic speech recognition (ASR), where a student model is trained to imitate the output behaviour of a teacher model. However, traditional KD methods suffer from teacher label storage issue, especially when the training corpora are large. Although on-the-fly teacher label generation tackles this issue, the training speed is significantly slower as the teacher model has to be evaluated every batch. In this paper, we reformulate the generation of teacher label as a codec problem. We propose a novel Multi-codebook Vector Quantization (MVQ) approach that compresses teacher embeddings to codebook indexes (CI). Based on this, a KD training framework (MVQ-KD) is proposed where a student model predicts the CI generated from the embeddings of a self-supervised pre-trained teacher model. Experiments on the LibriSpeech clean-100 hour show that MVQ-KD framework achieves comparable performance as traditional KD methods (l1, l2), while requiring 256 times less storage. When the full LibriSpeech dataset is used, MVQ-KD framework results in 13.8% and 8.2% relative word error rate reductions (WERRs) for non -streaming transducer on test-clean and test-other and 4.0% and 4.9% for streaming transducer. The implementation of this work is already released as a part of the open-source project icefall.

</details>

### [Structured State Space Decoder for Speech Recognition and Synthesis](2210.17098.md)
**Koichi Miyazaki, Masato Murata, Tomoki Koriyama** · 2022-10-31

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems developed in recent years have shown promising results with self-attention models (e.g., Transformer and Conformer), which are replacing conventional recurrent neural networks. Meanwhile, a structured state space model (S4) has been recently proposed, producing promising results for various long-sequence modeling tasks, including raw speech classification. The S4 model can be trained in parallel, same as the Transformer model. In this study, we applied S4 as a decoder for ASR and text-to-speech (TTS) tasks by comparing it with the Transformer decoder. For the ASR task, our experimental results demonstrate that the proposed model achieves a competitive word error rate (WER) of 1.88%/4.25% on LibriSpeech test-clean/test-other set and a character error rate (CER) of 3.80%/2.63%/2.98% on the CSJ eval1/eval2/eval3 set. Furthermore, the proposed model is more robust than the standard Transformer model, particularly for long-form speech on both the datasets. For the TTS task, the proposed method outperforms the Transformer baseline.

</details>

### [FusionFormer: Fusing Operations in Transformer for Efficient Streaming Speech Recognition](2210.17079.md)
**Xingchen Song, Di Wu, Binbin Zhang, Zhiyong Wu et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

The recently proposed Conformer architecture which combines convolution with attention to capture both local and global dependencies has become the \textit{de facto} backbone model for Automatic Speech Recognition~(ASR). Inherited from the Natural Language Processing (NLP) tasks, the architecture takes Layer Normalization~(LN) as a default normalization technique. However, through a series of systematic studies, we find that LN might take 10\% of the inference time despite that it only contributes to 0.1\% of the FLOPs. This motivates us to replace LN with other normalization techniques, e.g., Batch Normalization~(BN), to speed up inference with the help of operator fusion methods and the avoidance of calculating the mean and variance statistics during inference. After examining several plain attempts which directly remove all LN layers or replace them with BN in the same place, we find that the divergence issue is mainly caused by the unstable layer output. We therefore propose to append a BN layer to each linear or convolution layer where stabilized training results are observed. We also propose to simplify the activations in Conformer, such as Swish and GLU, by replacing them with ReLU. All these exchanged modules can be fused into the weights of the adjacent linear/convolution layers and hence have zero inference cost. Therefore, we name it FusionFormer. Our experiments indicate that FusionFormer is as effective as the LN-based Conformer and is about 10\% faster.

</details>

### [Modular Hybrid Autoregressive Transducer](2210.17049.md)
**Zhong Meng, Tongzhou Chen, Rohit Prabhavalkar, Yu Zhang et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

Text-only adaptation of a transducer model remains challenging for end-to-end speech recognition since the transducer has no clearly separated acoustic model (AM), language model (LM) or blank model. In this work, we propose a modular hybrid autoregressive transducer (MHAT) that has structurally separated label and blank decoders to predict label and blank distributions, respectively, along with a shared acoustic encoder. The encoder and label decoder outputs are directly projected to AM and internal LM scores and then added to compute label posteriors. We train MHAT with an internal LM loss and a HAT loss to ensure that its internal LM becomes a standalone neural LM that can be effectively adapted to text. Moreover, text adaptation of MHAT fosters a much better LM fusion than internal LM subtraction-based methods. On Google's large-scale production data, a multi-domain MHAT adapted with 100B sentences achieves relative WER reductions of up to 12.4% without LM fusion and 21.5% with LM fusion from 400K-hour trained HAT.

</details>

### [Blank Collapse: Compressing CTC emission for the faster decoding](2210.17017.md)
**Minkyu Jung, Ohhyeok Kwon, Seunghyun Seo, Soonshin Seo** · 2022-10-31

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) model is a very efficient method for modeling sequences, especially for speech data. In order to use CTC model as an Automatic Speech Recognition (ASR) task, the beam search decoding with an external language model like n-gram LM is necessary to obtain reasonable results. In this paper we analyze the blank label in CTC beam search deeply and propose a very simple method to reduce the amount of calculation resulting in faster beam search decoding speed. With this method, we can get up to 78% faster decoding speed than ordinary beam search decoding with a very small loss of accuracy in LibriSpeech datasets. We prove this method is effective not only practically by experiments but also theoretically by mathematical reasoning. We also observe that this reduction is more obvious if the accuracy of the model is higher.

</details>

### [Improved acoustic-to-articulatory inversion using representations from pretrained self-supervised learning models](2210.16871.md)
**Sathvik Udupa, Siddarth C, Prasanta Kumar Ghosh** · 2022-10-30

<details>
<summary>Abstract</summary>

In this work, we investigate the effectiveness of pretrained Self-Supervised Learning (SSL) features for learning the mapping for acoustic to articulatory inversion (AAI). Signal processing-based acoustic features such as MFCCs have been predominantly used for the AAI task with deep neural networks. With SSL features working well for various other speech tasks such as speech recognition, emotion classification, etc., we experiment with its efficacy for AAI. We train on SSL features with transformer neural networks-based AAI models of 3 different model complexities and compare its performance with MFCCs in subject-specific (SS), pooled and fine-tuned (FT) configurations with data from 10 subjects, and evaluate with correlation coefficient (CC) score on the unseen sentence test set. We find that acoustic feature reconstruction objective-based SSL features such as TERA and DeCoAR work well for AAI, with SS CCs of these SSL features reaching close to the best FT CCs of MFCC. We also find the results consistent across different model sizes.

</details>

### [DuDe: Dual-Decoder Multilingual ASR for Indian Languages using Common Label Set](2210.16739.md)
**Arunkumar A, Mudit Batra, Umesh S** · 2022-10-30

<details>
<summary>Abstract</summary>

In a multilingual country like India, multilingual Automatic Speech Recognition (ASR) systems have much scope. Multilingual ASR systems exhibit many advantages like scalability, maintainability, and improved performance over the monolingual ASR systems. However, building multilingual systems for Indian languages is challenging since different languages use different scripts for writing. On the other hand, Indian languages share a lot of common sounds. Common Label Set (CLS) exploits this idea and maps graphemes of various languages with similar sounds to common labels. Since Indian languages are mostly phonetic, building a parser to convert from native script to CLS is easy. In this paper, we explore various approaches to build multilingual ASR models. We also propose a novel architecture called Encoder-Decoder-Decoder for building multilingual systems that use both CLS and native script labels. We also analyzed the effectiveness of CLS-based multilingual systems combined with machine transliteration.

</details>

### [token2vec: A Joint Self-Supervised Pre-training Framework Using Unpaired Speech and Text](2210.16755.md)
**Xianghu Yue, Junyi Ao, Xiaoxue Gao, Haizhou Li** · 2022-10-30

<details>
<summary>Abstract</summary>

Self-supervised pre-training has been successful in both text and speech processing. Speech and text offer different but complementary information. The question is whether we are able to perform a speech-text joint pre-training on unpaired speech and text. In this paper, we take the idea of self-supervised pre-training one step further and propose token2vec, a novel joint pre-training framework for unpaired speech and text based on discrete representations of speech. Firstly, due to the distinct characteristics between speech and text modalities, where speech is continuous while text is discrete, we first discretize speech into a sequence of discrete speech tokens to solve the modality mismatch problem. Secondly, to solve the length mismatch problem, where the speech sequence is usually much longer than text sequence, we convert the words of text into phoneme sequences and randomly repeat each phoneme in the sequences. Finally, we feed the discrete speech and text tokens into a modality-agnostic Transformer encoder and pre-train with token-level masking language modeling (tMLM). Experiments show that token2vec is significantly superior to various speech-only pre-training baselines, with up to 17.7% relative WER reduction. Token2vec model is also validated on a non-ASR task, i.e., spoken intent classification, and shows good transferability.

</details>

### [BERT Meets CTC: New Formulation of End-to-End Speech Recognition with Pre-trained Masked Language Model](2210.16663.md)
**Yosuke Higuchi, Brian Yan, Siddhant Arora, Tetsuji Ogawa et al.** · 2022-10-29

<details>
<summary>Abstract</summary>

This paper presents BERT-CTC, a novel formulation of end-to-end speech recognition that adapts BERT for connectionist temporal classification (CTC). Our formulation relaxes the conditional independence assumptions used in conventional CTC and incorporates linguistic knowledge through the explicit output dependency obtained by BERT contextual embedding. BERT-CTC attends to the full contexts of the input and hypothesized output sequences via the self-attention mechanism. This mechanism encourages a model to learn inner/inter-dependencies between the audio and token representations while maintaining CTC's training efficiency. During inference, BERT-CTC combines a mask-predict algorithm with CTC decoding, which iteratively refines an output sequence. The experimental results reveal that BERT-CTC improves over conventional approaches across variations in speaking styles and languages. Finally, we show that the semantic representations in BERT-CTC are beneficial towards downstream spoken language understanding tasks.

</details>

### [XNOR-FORMER: Learning Accurate Approximations in Long Speech Transformers](2210.16643.md)
**Roshan Sharma, Bhiksha Raj** · 2022-10-29

<details>
<summary>Abstract</summary>

Transformers are among the state of the art for many tasks in speech, vision, and natural language processing, among others. Self-attentions, which are crucial contributors to this performance have quadratic computational complexity, which makes training on longer input sequences challenging. Prior work has produced state-of-the-art transformer variants with linear attention, however, current models sacrifice performance to achieve efficient implementations. In this work, we develop a novel linear transformer by examining the properties of the key-query product within self-attentions. Our model outperforms state of the art approaches on speech recognition and speech summarization, resulting in 1 % absolute WER improvement on the Librispeech-100 speech recognition benchmark and a new INTERVIEW speech recognition benchmark, and 5 points on ROUGE for summarization with How2.

</details>

### [End-to-end Spoken Language Understanding with Tree-constrained Pointer Generator](2210.16554.md)
**Guangzhi Sun, Chao Zhang, Philip C. Woodland** · 2022-10-29

<details>
<summary>Abstract</summary>

End-to-end spoken language understanding (SLU) suffers from the long-tail word problem. This paper exploits contextual biasing, a technique to improve the speech recognition of rare words, in end-to-end SLU systems. Specifically, a tree-constrained pointer generator (TCPGen), a powerful and efficient biasing model component, is studied, which leverages a slot shortlist with corresponding entities to extract biasing lists. Meanwhile, to bias the SLU model output slot distribution, a slot probability biasing (SPB) mechanism is proposed to calculate a slot distribution from TCPGen. Experiments on the SLURP dataset showed consistent SLU-F1 improvements using TCPGen and SPB, especially on unseen entities. On a new split by holding out 5 slot types for the test, TCPGen with SPB achieved zero-shot learning with an SLU-F1 score over 50% compared to baselines which can not deal with it. In addition to slot filling, the intent classification accuracy was also improved.

</details>

### [Accelerating RNN-T Training and Inference Using CTC guidance](2210.16481.md)
**Yongqiang Wang, Zhehuai Chen, Chengjian Zheng, Yu Zhang et al.** · 2022-10-29

<details>
<summary>Abstract</summary>

We propose a novel method to accelerate training and inference process of recurrent neural network transducer (RNN-T) based on the guidance from a co-trained connectionist temporal classification (CTC) model. We made a key assumption that if an encoder embedding frame is classified as a blank frame by the CTC model, it is likely that this frame will be aligned to blank for all the partial alignments or hypotheses in RNN-T and it can be discarded from the decoder input. We also show that this frame reduction operation can be applied in the middle of the encoder, which result in significant speed up for the training and inference in RNN-T. We further show that the CTC alignment, a by-product of the CTC decoder, can also be used to perform lattice reduction for RNN-T during training. Our method is evaluated on the Librispeech and SpeechStew tasks. We demonstrate that the proposed method is able to accelerate the RNN-T inference by 2.2 times with similar or slightly better word error rates (WER).

</details>

### [Filter and evolve: progressive pseudo label refining for semi-supervised automatic speech recognition](2210.16318.md)
**Zezhong Jin, Dading Zhong, Xiao Song, Zhaoyi Liu et al.** · 2022-10-28

<details>
<summary>Abstract</summary>

Fine tuning self supervised pretrained models using pseudo labels can effectively improve speech recognition performance. But, low quality pseudo labels can misguide decision boundaries and degrade performance. We propose a simple yet effective strategy to filter low quality pseudo labels to alleviate this problem. Specifically, pseudo-labels are produced over the entire training set and filtered via average probability scores calculated from the model output. Subsequently, an optimal percentage of utterances with high probability scores are considered reliable training data with trustworthy labels. The model is iteratively updated to correct the unreliable pseudo labels to minimize the effect of noisy labels. The process above is repeated until unreliable pseudo abels have been adequately corrected. Extensive experiments on LibriSpeech show that these filtered samples enable the refined model to yield more correct predictions, leading to better ASR performances under various experimental settings.

</details>

### [Dysfluencies Seldom Come Alone -- Detection as a Multi-Label Problem](2210.15982.md)
**Sebastian P. Bayerl, Dominik Wagner, Florian Hönig, Tobias Bocklet et al.** · 2022-10-28

<details>
<summary>Abstract</summary>

Specially adapted speech recognition models are necessary to handle stuttered speech. For these to be used in a targeted manner, stuttered speech must be reliably detected. Recent works have treated stuttering as a multi-class classification problem or viewed detecting each dysfluency type as an isolated task; that does not capture the nature of stuttering, where one dysfluency seldom comes alone, i.e., co-occurs with others. This work explores an approach based on a modified wav2vec 2.0 system for end-to-end stuttering detection and classification as a multi-label problem. The method is evaluated on combinations of three datasets containing English and German stuttered speech, yielding state-of-the-art results for stuttering detection on the SEP-28k-Extended dataset. Experimental results provide evidence for the transferability of features and the generalizability of the method across datasets and languages.

</details>

### [Random Utterance Concatenation Based Data Augmentation for Improving Short-video Speech Recognition](2210.15876.md)
**Yist Y. Lin, Tao Han, Haihua Xu, Van Tung Pham et al.** · 2022-10-28

<details>
<summary>Abstract</summary>

One of limitations in end-to-end automatic speech recognition (ASR) framework is its performance would be compromised if train-test utterance lengths are mismatched. In this paper, we propose an on-the-fly random utterance concatenation (RUC) based data augmentation method to alleviate train-test utterance length mismatch issue for short-video ASR task. Specifically, we are motivated by observations that our human-transcribed training utterances tend to be much shorter for short-video spontaneous speech (~3 seconds on average), while our test utterance generated from voice activity detection front-end is much longer (~10 seconds on average). Such a mismatch can lead to suboptimal performance. Empirically, it's observed the proposed RUC method significantly improves long utterance recognition without performance drop on short one. Overall, it achieves 5.72% word error rate reduction on average for 15 languages and improved robustness to various utterance length.

</details>

### [Efficient Speech Translation with Dynamic Latent Perceivers](2210.16264.md)
**Ioannis Tsiamas, Gerard I. Gállego, José A. R. Fonollosa, Marta R. Costa-jussà** · 2022-10-28

<details>
<summary>Abstract</summary>

Transformers have been the dominant architecture for Speech Translation in recent years, achieving significant improvements in translation quality. Since speech signals are longer than their textual counterparts, and due to the quadratic complexity of the Transformer, a down-sampling step is essential for its adoption in Speech Translation. Instead, in this research, we propose to ease the complexity by using a Perceiver encoder to map the speech inputs to a fixed-length latent representation. Furthermore, we introduce a novel way of training Perceivers, with Dynamic Latent Access (DLA), unlocking larger latent spaces without any additional computational overhead. Speech-to-Text Perceivers with DLA can match the performance of Transformer baselines across three language pairs in MuST-C. Finally, a DLA-trained model is easily adaptable to DLA at inference, and can be flexibly deployed with various computational budgets, without significant drops in translation quality.

</details>

### [Evaluating context-invariance in unsupervised speech representations](2210.15775.md)
**Mark Hallap, Emmanuel Dupoux, Ewan Dunbar** · 2022-10-27

<details>
<summary>Abstract</summary>

Unsupervised speech representations have taken off, with benchmarks (SUPERB, ZeroSpeech) demonstrating major progress on semi-supervised speech recognition, speech synthesis, and speech-only language modelling. Inspiration comes from the promise of ``discovering the phonemes'' of a language or a similar low-bitrate encoding. However, one of the critical properties of phoneme transcriptions is context-invariance: the phonetic context of a speech sound can have massive influence on the way it is pronounced, while the text remains stable. This is what allows tokens of the same word to have the same transcriptions -- key to language understanding. Current benchmarks do not measure context-invariance. We develop a new version of the ZeroSpeech ABX benchmark that measures context-invariance, and apply it to recent self-supervised representations. We demonstrate that the context-independence of representations is predictive of the stability of word-level representations. We suggest research concentrate on improving context-independence of self-supervised and unsupervised representations.

</details>

### [Simulating realistic speech overlaps improves multi-talker ASR](2210.15715.md)
**Muqiao Yang, Naoyuki Kanda, Xiaofei Wang, Jian Wu et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

Multi-talker automatic speech recognition (ASR) has been studied to generate transcriptions of natural conversation including overlapping speech of multiple speakers. Due to the difficulty in acquiring real conversation data with high-quality human transcriptions, a naïve simulation of multi-talker speech by randomly mixing multiple utterances was conventionally used for model training. In this work, we propose an improved technique to simulate multi-talker overlapping speech with realistic speech overlaps, where an arbitrary pattern of speech overlaps is represented by a sequence of discrete tokens. With this representation, speech overlapping patterns can be learned from real conversations based on a statistical language model, such as N-gram, which can be then used to generate multi-talker speech for training. In our experiments, multi-talker ASR models trained with the proposed method show consistent improvement on the word error rates across multiple datasets.

</details>

### [Exploring Effective Distillation of Self-Supervised Speech Models for Automatic Speech Recognition](2210.15631.md)
**Yujin Wang, Changli Tang, Ziyang Ma, Zhisheng Zheng et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

Recent years have witnessed great strides in self-supervised learning (SSL) on the speech processing. The SSL model is normally pre-trained on a great variety of unlabelled data and a large model size is preferred to increase the modeling capacity. However, this might limit its potential applications due to the expensive computation and memory costs introduced by the oversize model. Miniaturization for SSL models has become an important research direction of practical value. To this end, we explore the effective distillation of HuBERT-based SSL models for automatic speech recognition (ASR). First, in order to establish a strong baseline, a comprehensive study on different student model structures is conducted. On top of this, as a supplement to the regression loss widely adopted in previous works, a discriminative loss is introduced for HuBERT to enhance the distillation performance, especially in low-resource scenarios. In addition, we design a simple and effective algorithm to distill the front-end input from waveform to Fbank feature, resulting in 17% parameter reduction and doubling inference speed, at marginal performance degradation.

</details>

### [Virtuoso: Massive Multilingual Speech-Text Joint Semi-Supervised Learning for Text-To-Speech](2210.15447.md)
**Takaaki Saeki, Heiga Zen, Zhehuai Chen, Nobuyuki Morioka et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

This paper proposes Virtuoso, a massively multilingual speech-text joint semi-supervised learning framework for text-to-speech synthesis (TTS) models. Existing multilingual TTS typically supports tens of languages, which are a small fraction of the thousands of languages in the world. One difficulty to scale multilingual TTS to hundreds of languages is collecting high-quality speech-text paired data in low-resource languages. This study extends Maestro, a speech-text joint pretraining framework for automatic speech recognition (ASR), to speech generation tasks. To train a TTS model from various types of speech and text data, different training schemes are designed to handle supervised (paired TTS and ASR data) and unsupervised (untranscribed speech and unspoken text) datasets. Experimental evaluation shows that 1) multilingual TTS models trained on Virtuoso can achieve significantly better naturalness and intelligibility than baseline ones in seen languages, and 2) they can synthesize reasonably intelligible and naturally sounding speech for unseen languages where no high-quality paired TTS data is available.

</details>

### [Make More of Your Data: Minimal Effort Data Augmentation for Automatic Speech Recognition and Translation](2210.15398.md)
**Tsz Kin Lam, Shigehiko Schamoni, Stefan Riezler** · 2022-10-27

<details>
<summary>Abstract</summary>

Data augmentation is a technique to generate new training data based on existing data. We evaluate the simple and cost-effective method of concatenating the original data examples to build new training instances. Continued training with such augmented data is able to improve off-the-shelf Transformer and Conformer models that were optimized on the original data only. We demonstrate considerable improvements on the LibriSpeech-960h test sets (WER 2.83 and 6.87 for test-clean and test-other), which carry over to models combined with shallow fusion (WER 2.55 and 6.27). Our method of continued training also leads to improvements of up to 0.9 WER on the ASR part of CoVoST-2 for four non English languages, and we observe that the gains are highly dependent on the size of the original training data. We compare different concatenation strategies and found that our method does not need speaker information to achieve its improvements. Finally, we demonstrate on two datasets that our methods also works for speech translation tasks.

</details>

### [Automatic Severity Classification of Dysarthric speech by using Self-supervised Model with Multi-task Learning](2210.15387.md)
**Eun Jung Yeo, Kwanghee Choi, Sunhee Kim, Minhwa Chung** · 2022-10-27

<details>
<summary>Abstract</summary>

Automatic assessment of dysarthric speech is essential for sustained treatments and rehabilitation. However, obtaining atypical speech is challenging, often leading to data scarcity issues. To tackle the problem, we propose a novel automatic severity assessment method for dysarthric speech, using the self-supervised model in conjunction with multi-task learning. Wav2vec 2.0 XLS-R is jointly trained for two different tasks: severity classification and auxiliary automatic speech recognition (ASR). For the baseline experiments, we employ hand-crafted acoustic features and machine learning classifiers such as SVM, MLP, and XGBoost. Explored on the Korean dysarthric speech QoLT database, our model outperforms the traditional baseline methods, with a relative percentage increase of 1.25% for F1-score. In addition, the proposed model surpasses the model trained without ASR head, achieving 10.61% relative percentage improvements. Furthermore, we present how multi-task learning affects the severity classification performance by analyzing the latent representations and regularization effect.

</details>

### [Explicit Intensity Control for Accented Text-to-speech](2210.15364.md)
**Rui Liu, Haolin Zuo, De Hu, Guanglai Gao et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

Accented text-to-speech (TTS) synthesis seeks to generate speech with an accent (L2) as a variant of the standard version (L1). How to control the intensity of accent in the process of TTS is a very interesting research direction, and has attracted more and more attention. Recent work design a speaker-adversarial loss to disentangle the speaker and accent information, and then adjust the loss weight to control the accent intensity. However, such a control method lacks interpretability, and there is no direct correlation between the controlling factor and natural accent intensity. To this end, this paper propose a new intuitive and explicit accent intensity control scheme for accented TTS. Specifically, we first extract the posterior probability, called as ``goodness of pronunciation (GoP)'' from the L1 speech recognition model to quantify the phoneme accent intensity for accented speech, then design a FastSpeech2 based TTS model, named Ai-TTS, to take the accent intensity expression into account during speech generation. Experiments show that the our method outperforms the baseline model in terms of accent rendering and intensity control.

</details>

### [Robust Data2vec: Noise-robust Speech Representation Learning for ASR by Combining Regression and Improved Contrastive Learning](2210.15324.md)
**Qiu-Shi Zhu, Long Zhou, Jie Zhang, Shu-Jie Liu et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

Self-supervised pre-training methods based on contrastive learning or regression tasks can utilize more unlabeled data to improve the performance of automatic speech recognition (ASR). However, the robustness impact of combining the two pre-training tasks and constructing different negative samples for contrastive learning still remains unclear. In this paper, we propose a noise-robust data2vec for self-supervised speech representation learning by jointly optimizing the contrastive learning and regression tasks in the pre-training stage. Furthermore, we present two improved methods to facilitate contrastive learning. More specifically, we first propose to construct patch-based non-semantic negative samples to boost the noise robustness of the pre-training model, which is achieved by dividing the features into patches at different sizes (i.e., so-called negative samples). Second, by analyzing the distribution of positive and negative samples, we propose to remove the easily distinguishable negative samples to improve the discriminative capacity for pre-training models. Experimental results on the CHiME-4 dataset show that our method is able to improve the performance of the pre-trained model in noisy scenarios. We find that joint training of the contrastive learning and regression tasks can avoid the model collapse to some extent compared to only training the regression task.

</details>

### [SAN: a robust end-to-end ASR model architecture](2210.15285.md)
**Zeping Min, Qian Ge, Guanhua Huang** · 2022-10-27

<details>
<summary>Abstract</summary>

In this paper, we propose a novel Siamese Adversarial Network (SAN) architecture for automatic speech recognition, which aims at solving the difficulty of fuzzy audio recognition. Specifically, SAN constructs two sub-networks to differentiate the audio feature input and then introduces a loss to unify the output distribution of these sub-networks. Adversarial learning enables the network to capture more essential acoustic features and helps the models achieve better performance when encountering fuzzy audio input. We conduct numerical experiments with the SAN model on several datasets for the automatic speech recognition task. All experimental results show that the siamese adversarial nets significantly reduce the character error rate (CER). Specifically, we achieve a new state of art 4.37 CER without language model on the AISHELL-1 dataset, which leads to around 5% relative CER reduction. To reveal the generality of the siamese adversarial net, we also conduct experiments on the phoneme recognition task, which also shows the superiority of the siamese adversarial network.

</details>

### [Weight Averaging: A Simple Yet Effective Method to Overcome Catastrophic Forgetting in Automatic Speech Recognition](2210.15282.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2022-10-27

<details>
<summary>Abstract</summary>

Adapting a trained Automatic Speech Recognition (ASR) model to new tasks results in catastrophic forgetting of old tasks, limiting the model's ability to learn continually and to be extended to new speakers, dialects, languages, etc. Focusing on End-to-End ASR, in this paper, we propose a simple yet effective method to overcome catastrophic forgetting: weight averaging. By simply taking the average of the previous and the adapted model, our method achieves high performance on both the old and new tasks. It can be further improved by introducing a knowledge distillation loss during the adaptation. We illustrate the effectiveness of our method on both monolingual and multilingual ASR. In both cases, our method strongly outperforms all baselines, even in its simplest form.

</details>

### [Contextual-Utterance Training for Automatic Speech Recognition](2210.16238.md)
**Alejandro Gomez-Alanis, Lukas Drude, Andreas Schwarz, Rupak Vignesh Swaminathan et al.** · 2022-10-27

<details>
<summary>Abstract</summary>

Recent studies of streaming automatic speech recognition (ASR) recurrent neural network transducer (RNN-T)-based systems have fed the encoder with past contextual information in order to improve its word error rate (WER) performance. In this paper, we first propose a contextual-utterance training technique which makes use of the previous and future contextual utterances in order to do an implicit adaptation to the speaker, topic and acoustic environment. Also, we propose a dual-mode contextual-utterance training technique for streaming automatic speech recognition (ASR) systems. This proposed approach allows to make a better use of the available acoustic context in streaming models by distilling "in-place" the knowledge of a teacher, which is able to see both past and future contextual utterances, to the student which can only see the current and past contextual utterances. The experimental results show that a conformer-transducer system trained with the proposed techniques outperforms the same system trained with the classical RNN-T loss. Specifically, the proposed technique is able to reduce both the WER and the average last token emission latency by more than 6% and 40ms relative, respectively.

</details>

### [Iterative pseudo-forced alignment by acoustic CTC loss for self-supervised ASR domain adaptation](2210.15226.md)
**Fernando López, Jordi Luque** · 2022-10-27

<details>
<summary>Abstract</summary>

High-quality data labeling from specific domains is costly and human time-consuming. In this work, we propose a self-supervised domain adaptation method, based upon an iterative pseudo-forced alignment algorithm. The produced alignments are employed to customize an end-to-end Automatic Speech Recognition (ASR) and iteratively refined. The algorithm is fed with frame-wise character posteriors produced by a seed ASR, trained with out-of-domain data, and optimized throughout a Connectionist Temporal Classification (CTC) loss. The alignments are computed iteratively upon a corpus of broadcast TV. The process is repeated by reducing the quantity of text to be aligned or expanding the alignment window until finding the best possible audio-text alignment. The starting timestamps, or temporal anchors, are produced uniquely based on the confidence score of the last aligned utterance. This score is computed with the paths of the CTC-alignment matrix. With this methodology, no human-revised text references are required. Alignments from long audio files with low-quality transcriptions, like TV captions, are filtered out by confidence score and ready for further ASR adaptation. The obtained results, on both the Spanish RTVE2022 and CommonVoice databases, underpin the feasibility of using CTC-based systems to perform: highly accurate audio-text alignments, domain adaptation and semi-supervised training of end-to-end ASR.

</details>

### [Training Autoregressive Speech Recognition Models with Limited in-domain Supervision](2210.15135.md)
**Chak-Fai Li, Francis Keith, William Hartmann, Matthew Snover** · 2022-10-27

<details>
<summary>Abstract</summary>

Advances in self-supervised learning have significantly reduced the amount of transcribed audio required for training. However, the majority of work in this area is focused on read speech. We explore limited supervision in the domain of conversational speech. While we assume the amount of in-domain data is limited, we augment the model with open source read speech data. The XLS-R model has been shown to perform well with limited adaptation data and serves as a strong baseline. We use untranscribed data for self-supervised learning and semi-supervised training in an autoregressive encoder-decoder model. We demonstrate that by using the XLS-R model for pseudotranscription, a much smaller autoregressive model can outperform a finetuned XLS-R model when transcribed in-domain data is limited, reducing WER by as much as 8% absolute.

</details>

### [Four-in-One: A Joint Approach to Inverse Text Normalization, Punctuation, Capitalization, and Disfluency for Automatic Speech Recognition](2210.15063.md)
**Sharman Tan, Piyush Behre, Nick Kibre, Issac Alphonso et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

Features such as punctuation, capitalization, and formatting of entities are important for readability, understanding, and natural language processing tasks. However, Automatic Speech Recognition (ASR) systems produce spoken-form text devoid of formatting, and tagging approaches to formatting address just one or two features at a time. In this paper, we unify spoken-to-written text conversion via a two-stage process: First, we use a single transformer tagging model to jointly produce token-level tags for inverse text normalization (ITN), punctuation, capitalization, and disfluencies. Then, we apply the tags to generate written-form text and use weighted finite state transducer (WFST) grammars to format tagged ITN entity spans. Despite joining four models into one, our unified tagging approach matches or outperforms task-specific models across all four tasks on benchmark test sets across several domains.

</details>

### [Efficient Utilization of Large Pre-Trained Models for Low Resource ASR](2210.15445.md)
**Peter Vieting, Christoph Lüscher, Julian Dierkes, Ralf Schlüter et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

Unsupervised representation learning has recently helped automatic speech recognition (ASR) to tackle tasks with limited labeled data. Following this, hardware limitations and applications give rise to the question how to take advantage of large pre-trained models efficiently and reduce their complexity. In this work, we study a challenging low resource conversational telephony speech corpus from the medical domain in Vietnamese and German. We show the benefits of using unsupervised techniques beyond simple fine-tuning of large pre-trained models, discuss how to adapt them to a practical telephony task including bandwidth transfer and investigate different data conditions for pre-training and fine-tuning. We outperform the project baselines by 22% relative using pretraining techniques. Further gains of 29% can be achieved by refinements of architecture and training and 6% by adding 0.8 h of in-domain adaptation data.

</details>

### [Monotonic segmental attention for automatic speech recognition](2210.14742.md)
**Albert Zeyer, Robin Schmitt, Wei Zhou, Ralf Schlüter et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

We introduce a novel segmental-attention model for automatic speech recognition. We restrict the decoder attention to segments to avoid quadratic runtime of global attention, better generalize to long sequences, and eventually enable streaming. We directly compare global-attention and different segmental-attention modeling variants. We develop and compare two separate time-synchronous decoders, one specifically taking the segmental nature into account, yielding further improvements. Using time-synchronous decoding for segmental models is novel and a step towards streaming applications. Our experiments show the importance of a length model to predict the segment boundaries. The final best segmental-attention model using segmental decoding performs better than global-attention, in contrast to other monotonic attention approaches in the literature. Further, we observe that the segmental model generalizes much better to long sequences of up to several minutes.

</details>

### [Pronunciation Generation for Foreign Language Words in Intra-Sentential Code-Switching Speech Recognition](2210.14691.md)
**Wei Wang, Chao Zhang, Xiaopei Wu** · 2022-10-26

<details>
<summary>Abstract</summary>

Code-Switching refers to the phenomenon of switching languages within a sentence or discourse. However, limited code-switching , different language phoneme-sets and high rebuilding costs throw a challenge to make the specialized acoustic model for code-switching speech recognition. In this paper, we make use of limited code-switching data as driving materials and explore a shortcut to quickly develop intra-sentential code-switching recognition skill on the commissioned native language acoustic model, where we propose a data-driven method to make the seed lexicon which is used to train grapheme-to-phoneme model to predict mapping pronunciations for foreign language word in code-switching sentences. The core work of the data-driven technology in this paper consists of a phonetic decoding method and different selection methods. And for imbalanced word-level driving materials problem, we have an internal assistance inspiration that learning the good pronunciation rules in the words that possess sufficient materials using the grapheme-to-phoneme model to help the scarce. Our experiments show that the Mixed Error Rate in intra-sentential Chinese-English code-switching recognition reduced from 29.15\%, acquired on the pure Chinese recognizer, to 12.13\% by adding foreign language words' pronunciation through our data-driven approach, and finally get the best result 11.14\% with the combination of different selection methods and internal assistance tactic.

</details>

### [Reducing Language confusion for Code-switching Speech Recognition with Token-level Language Diarization](2210.14567.md)
**Hexin Liu, Haihua Xu, Leibny Paola Garcia, Andy W. H. Khong et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

Code-switching (CS) refers to the phenomenon that languages switch within a speech signal and leads to language confusion for automatic speech recognition (ASR). This paper aims to address language confusion for improving CS-ASR from two perspectives: incorporating and disentangling language information. We incorporate language information in the CS-ASR model by dynamically biasing the model with token-level language posteriors which are outputs of a sequence-to-sequence auxiliary language diarization module. In contrast, the disentangling process reduces the difference between languages via adversarial training so as to normalize two languages. We conduct the experiments on the SEAME dataset. Compared to the baseline model, both the joint optimization with LD and the language posterior bias achieve performance improvement. The comparison of the proposed methods indicates that incorporating language information is more effective than disentangling for reducing language confusion in CS speech.

</details>

### [UFO2: A unified pre-training framework for online and offline speech recognition](2210.14515.md)
**Li Fu, Siqi Li, Qingtao Li, Liping Deng et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

In this paper, we propose a Unified pre-training Framework for Online and Offline (UFO2) Automatic Speech Recognition (ASR), which 1) simplifies the two separate training workflows for online and offline modes into one process, and 2) improves the Word Error Rate (WER) performance with limited utterance annotating. Specifically, we extend the conventional offline-mode Self-Supervised Learning (SSL)-based ASR approach to a unified manner, where the model training is conditioned on both the full-context and dynamic-chunked inputs. To enhance the pre-trained representation model, stop-gradient operation is applied to decouple the online-mode objectives to the quantizer. Moreover, in both the pre-training and the downstream fine-tuning stages, joint losses are proposed to train the unified model with full-weight sharing for the two modes. Experimental results on the LibriSpeech dataset show that UFO2 outperforms the SSL-based baseline method by 29.7% and 18.2% relative WER reduction in offline and online modes, respectively.

</details>

### [The NPU-ASLP System for The ISCSLP 2022 Magichub Code-Swiching ASR Challenge](2210.14448.md)
**Yuhao Liang, Peikun Chen, Fan Yu, Xinfa Zhu et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

This paper describes our NPU-ASLP system submitted to the ISCSLP 2022 Magichub Code-Switching ASR Challenge. In this challenge, we first explore several popular end-to-end ASR architectures and training strategies, including bi-encoder, language-aware encoder (LAE) and mixture of experts (MoE). To improve our system's language modeling ability, we further attempt the internal language model as well as the long context language model. Given the limited training data in the challenge, we further investigate the effects of data augmentation, including speed perturbation, pitch shifting, speech codec, SpecAugment and synthetic data from text-to-speech (TTS). Finally, we explore ROVER-based score fusion to make full use of complementary hypotheses from different models. Our submitted system achieves 16.87% on mix error rate (MER) on the test set and comes to the 2nd place in the challenge ranking.

</details>

### [Linguistic-Enhanced Transformer with CTC Embedding for Speech Recognition](2210.14725.md)
**Xulong Zhang, Jianzong Wang, Ning Cheng, Mengyuan Zhao et al.** · 2022-10-25

<details>
<summary>Abstract</summary>

The recent emergence of joint CTC-Attention model shows significant improvement in automatic speech recognition (ASR). The improvement largely lies in the modeling of linguistic information by decoder. The decoder joint-optimized with an acoustic encoder renders the language model from ground-truth sequences in an auto-regressive manner during training. However, the training corpus of the decoder is limited to the speech transcriptions, which is far less than the corpus needed to train an acceptable language model. This leads to poor robustness of decoder. To alleviate this problem, we propose linguistic-enhanced transformer, which introduces refined CTC information to decoder during training process, so that the decoder can be more robust. Our experiments on AISHELL-1 speech corpus show that the character error rate (CER) is relatively reduced by up to 7%. We also find that in joint CTC-Attention ASR model, decoder is more sensitive to linguistic information than acoustic information.

</details>

### [ESB: A Benchmark For Multi-Domain End-to-End Speech Recognition](2210.13352.md)
**Sanchit Gandhi, Patrick von Platen, Alexander M. Rush** · 2022-10-24

<details>
<summary>Abstract</summary>

Speech recognition applications cover a range of different audio and text distributions, with different speaking styles, background noise, transcription punctuation and character casing. However, many speech recognition systems require dataset-specific tuning (audio filtering, punctuation removal and normalisation of casing), therefore assuming a-priori knowledge of both the audio and text distributions. This tuning requirement can lead to systems failing to generalise to other datasets and domains. To promote the development of multi-domain speech systems, we introduce the End-to-end Speech Benchmark (ESB) for evaluating the performance of a single automatic speech recognition (ASR) system across a broad set of speech datasets. Benchmarked systems must use the same data pre- and post-processing algorithm across datasets - assuming the audio and text data distributions are a-priori unknown. We compare a series of state-of-the-art (SoTA) end-to-end (E2E) systems on this benchmark, demonstrating how a single speech system can be applied and evaluated on a wide range of data distributions. We find E2E systems to be effective across datasets: in a fair comparison, E2E systems achieve within 2.6% of SoTA systems tuned to a specific dataset. Our analysis reveals that transcription artefacts, such as punctuation and casing, pose difficulties for ASR systems and should be included in evaluation. We believe E2E benchmarking over a range of datasets promotes the research of multi-domain speech recognition systems. ESB is available at https://huggingface.co/esb.

</details>

### [Time-Domain Speech Enhancement for Robust Automatic Speech Recognition](2210.13318.md)
**Yufeng Yang, Ashutosh Pandey, DeLiang Wang** · 2022-10-24

<details>
<summary>Abstract</summary>

It has been shown that the intelligibility of noisy speech can be improved by speech enhancement algorithms. However, speech enhancement has not been established as an effective frontend for robust automatic speech recognition (ASR) in noisy conditions compared to an ASR model trained on noisy speech directly. The divide between speech enhancement and ASR impedes the progress of robust ASR systems especially as speech enhancement has made big strides in recent years. In this work, we focus on eliminating this divide with an ARN (attentive recurrent network) based time-domain enhancement model. The proposed system fully decouples speech enhancement and an acoustic model trained only on clean speech. Results on the CHiME-2 corpus show that ARN enhanced speech translates to improved ASR results. The proposed system achieves $6.28\%$ average word error rate, outperforming the previous best by $19.3\%$ relatively.

</details>

### [Brouhaha: multi-task training for voice activity detection, speech-to-noise ratio, and C50 room acoustics estimation](2210.13248.md)
**Marvin Lavechin, Marianne Métais, Hadrien Titeux, Alodie Boissonnet et al.** · 2022-10-24

<details>
<summary>Abstract</summary>

Most automatic speech processing systems register degraded performance when applied to noisy or reverberant speech. But how can one tell whether speech is noisy or reverberant? We propose Brouhaha, a neural network jointly trained to extract speech/non-speech segments, speech-to-noise ratios, and C50room acoustics from single-channel recordings. Brouhaha is trained using a data-driven approach in which noisy and reverberant audio segments are synthesized. We first evaluate its performance and demonstrate that the proposed multi-task regime is beneficial. We then present two scenarios illustrating how Brouhaha can be used on naturally noisy and reverberant data: 1) to investigate the errors made by a speaker diarization model (pyannote.audio); and 2) to assess the reliability of an automatic speech recognition model (Whisper from OpenAI). Both our pipeline and a pretrained model are open source and shared with the speech community.

</details>

### [Does Joint Training Really Help Cascaded Speech Translation?](2210.13700.md)
**Viet Anh Khoa Tran, David Thulke, Yingbo Gao, Christian Herold et al.** · 2022-10-24

<details>
<summary>Abstract</summary>

Currently, in speech translation, the straightforward approach - cascading a recognition system with a translation system - delivers state-of-the-art results. However, fundamental challenges such as error propagation from the automatic speech recognition system still remain. To mitigate these problems, recently, people turn their attention to direct data and propose various joint training methods. In this work, we seek to answer the question of whether joint training really helps cascaded speech translation. We review recent papers on the topic and also investigate a joint training criterion by marginalizing the transcription posterior probabilities. Our findings show that a strong cascaded baseline can diminish any improvements obtained using joint training, and we suggest alternatives to joint training. We hope this work can serve as a refresher of the current speech translation landscape, and motivate research in finding more efficient and creative ways to utilize the direct data for speech translation.

</details>

### [Investigating self-supervised, weakly supervised and fully supervised training approaches for multi-domain automatic speech recognition: a study on Bangladeshi Bangla](2210.12921.md)
**Ahnaf Mozib Samin, M. Humayon Kobir, Md. Mushtaq Shahriyar Rafee, M. Firoz Ahmed et al.** · 2022-10-24

<details>
<summary>Abstract</summary>

Despite huge improvements in automatic speech recognition (ASR) employing neural networks, ASR systems still suffer from a lack of robustness and generalizability issues due to domain shifting. This is mainly because principal corpus design criteria are often not identified and examined adequately while compiling ASR datasets. In this study, we investigate the robustness of the state-of-the-art transfer learning approaches such as self-supervised wav2vec 2.0 and weakly supervised Whisper as well as fully supervised convolutional neural networks (CNNs) for multi-domain ASR. We also demonstrate the significance of domain selection while building a corpus by assessing these models on a novel multi-domain Bangladeshi Bangla ASR evaluation benchmark - BanSpeech, which contains approximately 6.52 hours of human-annotated speech and 8085 utterances from 13 distinct domains. SUBAK.KO, a mostly read speech corpus for the morphologically rich language Bangla, has been used to train the ASR systems. Experimental evaluation reveals that self-supervised cross-lingual pre-training is the best strategy compared to weak supervision and full supervision to tackle the multi-domain ASR task. Moreover, the ASR models trained on SUBAK.KO face difficulty recognizing speech from domains with mostly spontaneous speech. The BanSpeech will be publicly available to meet the need for a challenging evaluation benchmark for Bangla ASR.

</details>

### [Don't Discard Fixed-Window Audio Segmentation in Speech-to-Text Translation](2210.13363.md)
**Chantal Amrhein, Barry Haddow** · 2022-10-24

<details>
<summary>Abstract</summary>

For real-life applications, it is crucial that end-to-end spoken language translation models perform well on continuous audio, without relying on human-supplied segmentation. For online spoken language translation, where models need to start translating before the full utterance is spoken, most previous work has ignored the segmentation problem. In this paper, we compare various methods for improving models' robustness towards segmentation errors and different segmentation strategies in both offline and online settings and report results on translation quality, flicker and delay. Our findings on five different language pairs show that a simple fixed-window audio segmentation can perform surprisingly well given the right conditions.

</details>

### [Guided contrastive self-supervised pre-training for automatic speech recognition](2210.12335.md)
**Aparna Khare, Minhua Wu, Saurabhchand Bhati, Jasha Droppo et al.** · 2022-10-22

<details>
<summary>Abstract</summary>

Contrastive Predictive Coding (CPC) is a representation learning method that maximizes the mutual information between intermediate latent representations and the output of a given model. It can be used to effectively initialize the encoder of an Automatic Speech Recognition (ASR) model. We present a novel modification of CPC called Guided Contrastive Predictive Coding (GCPC). Our proposed method maximizes the mutual information between representations from a prior-knowledge model and the output of the model being pre-trained, allowing prior knowledge injection during pre-training. We validate our method on 3 ASR tasks: German, French and English. Our method outperforms CPC pre-training on all three datasets, reducing the Word Error Rate (WER) by 4.44%, 6.55% and 15.43% relative on the German, French and English (Librispeech) tasks respectively, compared to training from scratch, while CPC pre-training only brings 2.96%, 1.01% and 14.39% relative WER reduction respectively.

</details>

### [Optimizing Bilingual Neural Transducer with Synthetic Code-switching Text Generation](2210.12214.md)
**Thien Nguyen, Nathalie Tran, Liuhui Deng, Thiago Fraga da Silva et al.** · 2022-10-21

<details>
<summary>Abstract</summary>

Code-switching describes the practice of using more than one language in the same sentence. In this study, we investigate how to optimize a neural transducer based bilingual automatic speech recognition (ASR) model for code-switching speech. Focusing on the scenario where the ASR model is trained without supervised code-switching data, we found that semi-supervised training and synthetic code-switched data can improve the bilingual ASR system on code-switching speech. We analyze how each of the neural transducer's encoders contributes towards code-switching performance by measuring encoder-specific recall values, and evaluate our English/Mandarin system on the ASCEND data set. Our final system achieves 25% mixed error rate (MER) on the ASCEND English/Mandarin code-switching test set -- reducing the MER by 2.1% absolute compared to the previous literature -- while maintaining good accuracy on the monolingual test sets.

</details>

### [Deep LSTM Spoken Term Detection using Wav2Vec 2.0 Recognizer](2210.11885.md)
**Jan Švec, Jan Lehečka, Luboš Šmídl** · 2022-10-21

<details>
<summary>Abstract</summary>

In recent years, the standard hybrid DNN-HMM speech recognizers are outperformed by the end-to-end speech recognition systems. One of the very promising approaches is the grapheme Wav2Vec 2.0 model, which uses the self-supervised pretraining approach combined with transfer learning of the fine-tuned speech recognizer. Since it lacks the pronunciation vocabulary and language model, the approach is suitable for tasks where obtaining such models is not easy or almost impossible. In this paper, we use the Wav2Vec speech recognizer in the task of spoken term detection over a large set of spoken documents. The method employs a deep LSTM network which maps the recognized hypothesis and the searched term into a shared pronunciation embedding space in which the term occurrences and the assigned scores are easily computed. The paper describes a bootstrapping approach that allows the transfer of the knowledge contained in traditional pronunciation vocabulary of DNN-HMM hybrid ASR into the context of grapheme-based Wav2Vec. The proposed method outperforms the previously published system based on the combination of the DNN-HMM hybrid ASR and phoneme recognizer by a large margin on the MALACH data in both English and Czech languages.

</details>

### [Can Visual Context Improve Automatic Speech Recognition for an Embodied Agent?](2210.13189.md)
**Pradip Pramanick, Chayan Sarkar** · 2022-10-21

<details>
<summary>Abstract</summary>

The usage of automatic speech recognition (ASR) systems are becoming omnipresent ranging from personal assistant to chatbots, home, and industrial automation systems, etc. Modern robots are also equipped with ASR capabilities for interacting with humans as speech is the most natural interaction modality. However, ASR in robots faces additional challenges as compared to a personal assistant. Being an embodied agent, a robot must recognize the physical entities around it and therefore reliably recognize the speech containing the description of such entities. However, current ASR systems are often unable to do so due to limitations in ASR training, such as generic datasets and open-vocabulary modeling. Also, adverse conditions during inference, such as noise, accented, and far-field speech makes the transcription inaccurate. In this work, we present a method to incorporate a robot's visual information into an ASR system and improve the recognition of a spoken utterance containing a visible entity. Specifically, we propose a new decoder biasing technique to incorporate the visual context while ensuring the ASR output does not degrade for incorrect context. We achieve a 59% relative reduction in WER from an unmodified ASR system.

</details>

### [Named Entity Detection and Injection for Direct Speech Translation](2210.11981.md)
**Marco Gaido, Yun Tang, Ilia Kulikov, Rongqing Huang et al.** · 2022-10-21

<details>
<summary>Abstract</summary>

In a sentence, certain words are critical for its semantic. Among them, named entities (NEs) are notoriously challenging for neural models. Despite their importance, their accurate handling has been neglected in speech-to-text (S2T) translation research, and recent work has shown that S2T models perform poorly for locations and notably person names, whose spelling is challenging unless known in advance. In this work, we explore how to leverage dictionaries of NEs known to likely appear in a given context to improve S2T model outputs. Our experiments show that we can reliably detect NEs likely present in an utterance starting from S2T encoder outputs. Indeed, we demonstrate that the current detection quality is sufficient to improve NE accuracy in the translation with a 31% reduction in person name errors.

</details>

### [Audio-to-Intent Using Acoustic-Textual Subword Representations from End-to-End ASR](2210.12134.md)
**Pranay Dighe, Prateeth Nayak, Oggi Rudovic, Erik Marchi et al.** · 2022-10-21

<details>
<summary>Abstract</summary>

Accurate prediction of the user intent to interact with a voice assistant (VA) on a device (e.g. on the phone) is critical for achieving naturalistic, engaging, and privacy-centric interactions with the VA. To this end, we present a novel approach to predict the user's intent (the user speaking to the device or not) directly from acoustic and textual information encoded at subword tokens which are obtained via an end-to-end ASR model. Modeling directly the subword tokens, compared to modeling of the phonemes and/or full words, has at least two advantages: (i) it provides a unique vocabulary representation, where each token has a semantic meaning, in contrast to the phoneme-level representations, (ii) each subword token has a reusable "sub"-word acoustic pattern (that can be used to construct multiple full words), resulting in a largely reduced vocabulary space than of the full words. To learn the subword representations for the audio-to-intent classification, we extract: (i) acoustic information from an E2E-ASR model, which provides frame-level CTC posterior probabilities for the subword tokens, and (ii) textual information from a pre-trained continuous bag-of-words model capturing the semantic meaning of the subword tokens. The key to our approach is the way it combines acoustic subword-level posteriors with text information using the notion of positional-encoding in order to account for multiple ASR hypotheses simultaneously. We show that our approach provides more robust and richer representations for audio-to-intent classification, and is highly accurate with correctly mitigating 93.3% of unintended user audio from invoking the smart assistant at 99% true positive rate.

</details>

### [Improving Semi-supervised End-to-end Automatic Speech Recognition using CycleGAN and Inter-domain Losses](2210.11642.md)
**Chia-Yu Li, Ngoc Thang Vu** · 2022-10-20

<details>
<summary>Abstract</summary>

We propose a novel method that combines CycleGAN and inter-domain losses for semi-supervised end-to-end automatic speech recognition. Inter-domain loss targets the extraction of an intermediate shared representation of speech and text inputs using a shared network. CycleGAN uses cycle-consistent loss and the identity mapping loss to preserve relevant characteristics of the input feature after converting from one domain to another. As such, both approaches are suitable to train end-to-end models on unpaired speech-text inputs. In this paper, we exploit the advantages from both inter-domain loss and CycleGAN to achieve better shared representation of unpaired speech and text inputs and thus improve the speech-to-text mapping. Our experimental results on the WSJ eval92 and Voxforge (non English) show 8~8.5% character error rate reduction over the baseline, and the results on LibriSpeech test_clean also show noticeable improvement.

</details>

### [Anchored Speech Recognition with Neural Transducers](2210.11588.md)
**Desh Raj, Junteng Jia, Jay Mahadeokar, Chunyang Wu et al.** · 2022-10-20

<details>
<summary>Abstract</summary>

Neural transducers have achieved human level performance on standard speech recognition benchmarks. However, their performance significantly degrades in the presence of cross-talk, especially when the primary speaker has a low signal-to-noise ratio. Anchored speech recognition refers to a class of methods that use information from an anchor segment (e.g., wake-words) to recognize device-directed speech while ignoring interfering background speech. In this paper, we investigate anchored speech recognition to make neural transducers robust to background speech. We extract context information from the anchor segment with a tiny auxiliary network, and use encoder biasing and joiner gating to guide the transducer towards the target speech. Moreover, to improve the robustness of context embedding extraction, we propose auxiliary training objectives to disentangle lexical content from speaking style. We evaluate our methods on synthetic LibriSpeech-based mixtures comprising several SNR and overlap conditions; they improve relative word error rates by 19.6% over a strong baseline, when averaged over all conditions.

</details>

### [G-Augment: Searching for the Meta-Structure of Data Augmentation Policies for ASR](2210.10879.md)
**Gary Wang, Ekin D. Cubuk, Andrew Rosenberg, Shuyang Cheng et al.** · 2022-10-19

<details>
<summary>Abstract</summary>

Data augmentation is a ubiquitous technique used to provide robustness to automatic speech recognition (ASR) training. However, even as so much of the ASR training process has become automated and more "end-to-end", the data augmentation policy (what augmentation functions to use, and how to apply them) remains hand-crafted. We present Graph-Augment, a technique to define the augmentation space as directed acyclic graphs (DAGs) and search over this space to optimize the augmentation policy itself. We show that given the same computational budget, policies produced by G-Augment are able to perform better than SpecAugment policies obtained by random search on fine-tuning tasks on CHiME-6 and AMI. G-Augment is also able to establish a new state-of-the-art ASR performance on the CHiME-6 evaluation set (30.7% WER). We further demonstrate that G-Augment policies show better transfer properties across warm-start to cold-start training and model size compared to random-searched SpecAugment policies.

</details>

### [End-to-End Integration of Speech Recognition, Dereverberation, Beamforming, and Self-Supervised Learning Representation](2210.10742.md)
**Yoshiki Masuyama, Xuankai Chang, Samuele Cornell, Shinji Watanabe et al.** · 2022-10-19

<details>
<summary>Abstract</summary>

Self-supervised learning representation (SSLR) has demonstrated its significant effectiveness in automatic speech recognition (ASR), mainly with clean speech. Recent work pointed out the strength of integrating SSLR with single-channel speech enhancement for ASR in noisy environments. This paper further advances this integration by dealing with multi-channel input. We propose a novel end-to-end architecture by integrating dereverberation, beamforming, SSLR, and ASR within a single neural network. Our system achieves the best performance reported in the literature on the CHiME-4 6-channel track with a word error rate (WER) of 1.77%. While the WavLM-based strong SSLR demonstrates promising results by itself, the end-to-end integration with the weighted power minimization distortionless response beamformer, which simultaneously performs dereverberation and denoising, improves WER significantly. Its effectiveness is also validated on the REVERB dataset.

</details>

### [Speaker- and Age-Invariant Training for Child Acoustic Modeling Using Adversarial Multi-Task Learning](2210.10231.md)
**Mostafa Shahin, Beena Ahmed, Julien Epps** · 2022-10-19

<details>
<summary>Abstract</summary>

One of the major challenges in acoustic modelling of child speech is the rapid changes that occur in the children's articulators as they grow up, their differing growth rates and the subsequent high variability in the same age group. These high acoustic variations along with the scarcity of child speech corpora have impeded the development of a reliable speech recognition system for children. In this paper, a speaker- and age-invariant training approach based on adversarial multi-task learning is proposed. The system consists of one generator shared network that learns to generate speaker- and age-invariant features connected to three discrimination networks, for phoneme, age, and speaker. The generator network is trained to minimize the phoneme-discrimination loss and maximize the speaker- and age-discrimination losses in an adversarial multi-task learning fashion. The generator network is a Time Delay Neural Network (TDNN) architecture while the three discriminators are feed-forward networks. The system was applied to the OGI speech corpora and achieved a 13% reduction in the WER of the ASR.

</details>

### [Simple and Effective Unsupervised Speech Translation](2210.10191.md)
**Changhan Wang, Hirofumi Inaguma, Peng-Jen Chen, Ilia Kulikov et al.** · 2022-10-18

<details>
<summary>Abstract</summary>

The amount of labeled data to train models for speech tasks is limited for most languages, however, the data scarcity is exacerbated for speech translation which requires labeled data covering two different languages. To address this issue, we study a simple and effective approach to build speech translation systems without labeled data by leveraging recent advances in unsupervised speech recognition, machine translation and speech synthesis, either in a pipeline approach, or to generate pseudo-labels for training end-to-end speech translation models. Furthermore, we present an unsupervised domain adaptation technique for pre-trained speech models which improves the performance of downstream unsupervised speech recognition, especially for low-resource settings. Experiments show that unsupervised speech-to-text translation outperforms the previous unsupervised state of the art by 3.2 BLEU on the Libri-Trans benchmark, on CoVoST 2, our best systems outperform the best supervised end-to-end models (without pre-training) from only two years ago by an average of 5.0 BLEU over five X-En directions. We also report competitive results on MuST-C and CVSS benchmarks.

</details>

### [Maestro-U: Leveraging joint speech-text representation learning for zero supervised speech ASR](2210.10027.md)
**Zhehuai Chen, Ankur Bapna, Andrew Rosenberg, Yu Zhang et al.** · 2022-10-18

<details>
<summary>Abstract</summary>

Training state-of-the-art Automated Speech Recognition (ASR) models typically requires a substantial amount of transcribed speech. In this work, we demonstrate that a modality-matched joint speech and text model can be leveraged to train a massively multilingual ASR model without any supervised (manually transcribed) speech for some languages. This paper explores the use of jointly learnt speech and text representations in a massively multilingual, zero supervised speech, real-world setting to expand the set of languages covered by ASR with only unlabeled speech and text in the target languages. Using the FLEURS dataset, we define the task to cover $102$ languages, where transcribed speech is available in $52$ of these languages and can be used to improve end-to-end ASR quality on the remaining $50$. First, we show that by combining speech representations with byte-level text representations and use of language embeddings, we can dramatically reduce the Character Error Rate (CER) on languages with no supervised speech from 64.8\% to 30.8\%, a relative reduction of 53\%. Second, using a subset of South Asian languages we show that Maestro-U can promote knowledge transfer from languages with supervised speech even when there is limited to no graphemic overlap. Overall, Maestro-U closes the gap to oracle performance by 68.5\% relative and reduces the CER of 19 languages below 15\%.

</details>

### [Layer-wise Relevance Propagation for Echo State Networks applied to Earth System Variability](2210.09958.md)
**Marco Landt-Hayen, Peer Kröger, Martin Claus, Willi Rath** · 2022-10-18

<details>
<summary>Abstract</summary>

Artificial neural networks (ANNs) are known to be powerful methods for many hard problems (e.g. image classification, speech recognition or time series prediction). However, these models tend to produce black-box results and are often difficult to interpret. Layer-wise relevance propagation (LRP) is a widely used technique to understand how ANN models come to their conclusion and to understand what a model has learned. Here, we focus on Echo State Networks (ESNs) as a certain type of recurrent neural networks, also known as reservoir computing. ESNs are easy to train and only require a small number of trainable parameters, but are still black-box models. We show how LRP can be applied to ESNs in order to open the black-box. We also show how ESNs can be used not only for time series prediction but also for image classification: Our ESN model serves as a detector for El Nino Southern Oscillation (ENSO) from sea surface temperature anomalies. ENSO is actually a well-known problem and has been extensively discussed before. But here we use this simple problem to demonstrate how LRP can significantly enhance the explainablility of ESNs.

</details>

### [Generalizing in the Real World with Representation Learning](2210.09925.md)
**Tegan Maharaj** · 2022-10-18

<details>
<summary>Abstract</summary>

Machine learning (ML) formalizes the problem of getting computers to learn from experience as optimization of performance according to some metric(s) on a set of data examples. This is in contrast to requiring behaviour specified in advance (e.g. by hard-coded rules). Formalization of this problem has enabled great progress in many applications with large real-world impact, including translation, speech recognition, self-driving cars, and drug discovery. But practical instantiations of this formalism make many assumptions - for example, that data are i.i.d.: independent and identically distributed - whose soundness is seldom investigated. And in making great progress in such a short time, the field has developed many norms and ad-hoc standards, focused on a relatively small range of problem settings. As applications of ML, particularly in artificial intelligence (AI) systems, become more pervasive in the real world, we need to critically examine these assumptions, norms, and problem settings, as well as the methods that have become de-facto standards. There is much we still do not understand about how and why deep networks trained with stochastic gradient descent are able to generalize as well as they do, why they fail when they do, and how they will perform on out-of-distribution data. In this thesis I cover some of my work towards better understanding deep net generalization, identify several ways assumptions and problem settings fail to generalize to the real world, and propose ways to address those failures in practice.

</details>

### [Discrete Cross-Modal Alignment Enables Zero-Shot Speech Translation](2210.09556.md)
**Chen Wang, Yuchen Liu, Boxing Chen, Jiajun Zhang et al.** · 2022-10-18

<details>
<summary>Abstract</summary>

End-to-end Speech Translation (ST) aims at translating the source language speech into target language text without generating the intermediate transcriptions. However, the training of end-to-end methods relies on parallel ST data, which are difficult and expensive to obtain. Fortunately, the supervised data for automatic speech recognition (ASR) and machine translation (MT) are usually more accessible, making zero-shot speech translation a potential direction. Existing zero-shot methods fail to align the two modalities of speech and text into a shared semantic space, resulting in much worse performance compared to the supervised ST methods. In order to enable zero-shot ST, we propose a novel Discrete Cross-Modal Alignment (DCMA) method that employs a shared discrete vocabulary space to accommodate and match both modalities of speech and text. Specifically, we introduce a vector quantization module to discretize the continuous representations of speech and text into a finite set of virtual tokens, and use ASR data to map corresponding speech and text to the same virtual token in a shared codebook. This way, source language speech can be embedded in the same semantic space as the source language text, which can be then transformed into target language text with an MT module. Experiments on multiple language pairs demonstrate that our zero-shot ST method significantly improves the SOTA, and even performers on par with the strong supervised ST baselines.

</details>

### [Towards Personalization of CTC Speech Recognition Models with Contextual Adapters and Adaptive Boosting](2210.09510.md)
**Saket Dingliwal, Monica Sunkara, Sravan Bodapati, Srikanth Ronanki et al.** · 2022-10-18

<details>
<summary>Abstract</summary>

End-to-end speech recognition models trained using joint Connectionist Temporal Classification (CTC)-Attention loss have gained popularity recently. In these models, a non-autoregressive CTC decoder is often used at inference time due to its speed and simplicity. However, such models are hard to personalize because of their conditional independence assumption that prevents output tokens from previous time steps to influence future predictions. To tackle this, we propose a novel two-way approach that first biases the encoder with attention over a predefined list of rare long-tail and out-of-vocabulary (OOV) words and then uses dynamic boosting and phone alignment network during decoding to further bias the subword predictions. We evaluate our approach on open-source VoxPopuli and in-house medical datasets to showcase a 60% improvement in F1 score on domain-specific rare words over a strong CTC baseline.

</details>

### [Sub-8-bit quantization for on-device speech recognition: a regularization-free approach](2210.09188.md)
**Kai Zhen, Martin Radfar, Hieu Duy Nguyen, Grant P. Strimel et al.** · 2022-10-17

<details>
<summary>Abstract</summary>

For on-device automatic speech recognition (ASR), quantization aware training (QAT) is ubiquitous to achieve the trade-off between model predictive performance and efficiency. Among existing QAT methods, one major drawback is that the quantization centroids have to be predetermined and fixed. To overcome this limitation, we introduce a regularization-free, "soft-to-hard" compression mechanism with self-adjustable centroids in a mu-Law constrained space, resulting in a simpler yet more versatile quantization scheme, called General Quantizer (GQ). We apply GQ to ASR tasks using Recurrent Neural Network Transducer (RNN-T) and Conformer architectures on both LibriSpeech and de-identified far-field datasets. Without accuracy degradation, GQ can compress both RNN-T and Conformer into sub-8-bit, and for some RNN-T layers, to 1-bit for fast and accurate inference. We observe a 30.73% memory footprint saving and 31.75% user-perceived latency reduction compared to 8-bit QAT via physical device benchmarking.

</details>

### [Language-agnostic Code-Switching in Sequence-To-Sequence Speech Recognition](2210.08992.md)
**Enes Yavuz Ugan, Christian Huber, Juan Hussain, Alexander Waibel** · 2022-10-17

<details>
<summary>Abstract</summary>

Code-Switching (CS) is referred to the phenomenon of alternately using words and phrases from different languages. While today's neural end-to-end (E2E) models deliver state-of-the-art performances on the task of automatic speech recognition (ASR) it is commonly known that these systems are very data-intensive. However, there is only a few transcribed and aligned CS speech available. To overcome this problem and train multilingual systems which can transcribe CS speech, we propose a simple yet effective data augmentation in which audio and corresponding labels of different source languages are concatenated. By using this training data, our E2E model improves on transcribing CS speech. It also surpasses monolingual models on monolingual tests. The results show that this augmentation technique can even improve the model's performance on inter-sentential language switches not seen during training by 5,03% WER.

</details>

### [Towards Relation Extraction From Speech](2210.08759.md)
**Tongtong Wu, Guitao Wang, Jinming Zhao, Zhaoran Liu et al.** · 2022-10-17

<details>
<summary>Abstract</summary>

Relation extraction typically aims to extract semantic relationships between entities from the unstructured text. One of the most essential data sources for relation extraction is the spoken language, such as interviews and dialogues. However, the error propagation introduced in automatic speech recognition (ASR) has been ignored in relation extraction, and the end-to-end speech-based relation extraction method has been rarely explored. In this paper, we propose a new listening information extraction task, i.e., speech relation extraction. We construct the training dataset for speech relation extraction via text-to-speech systems, and we construct the testing dataset via crowd-sourcing with native English speakers. We explore speech relation extraction via two approaches: the pipeline approach conducting text-based extraction with a pretrained ASR module, and the end2end approach via a new proposed encoder-decoder model, or what we called SpeechRE. We conduct comprehensive experiments to distinguish the challenges in speech relation extraction, which may shed light on future explorations. We share the code and data on https://github.com/wutong8023/SpeechRE.

</details>

### [Continuous Pseudo-Labeling from the Start](2210.08711.md)
**Dan Berrebbi, Ronan Collobert, Samy Bengio, Navdeep Jaitly et al.** · 2022-10-17

<details>
<summary>Abstract</summary>

Self-training (ST), or pseudo-labeling has sparked significant interest in the automatic speech recognition (ASR) community recently because of its success in harnessing unlabeled data. Unlike prior semi-supervised learning approaches that relied on iteratively regenerating pseudo-labels (PLs) from a trained model and using them to train a new model, recent state-of-the-art methods perform `continuous training' where PLs are generated using a very recent version of the model being trained. Nevertheless, these approaches still rely on bootstrapping the ST using an initial supervised learning phase where the model is trained on labeled data alone. We believe this has the potential for over-fitting to the labeled dataset in low resource settings and that ST from the start of training should reduce over-fitting. In this paper we show how we can do this by dynamically controlling the evolution of PLs during the training process in ASR. To the best of our knowledge, this is the first study that shows the feasibility of generating PLs from the very start of the training. We are able to achieve this using two techniques that avoid instabilities which lead to degenerate models that do not generalize. Firstly, we control the evolution of PLs through a curriculum that uses the online changes in PLs to control the membership of the cache of PLs and improve generalization. Secondly, we find that by sampling transcriptions from the predictive distribution, rather than only using the best transcription, we can stabilize training further. With these techniques, our ST models match prior works without an external language model.

</details>

### [Acoustic-aware Non-autoregressive Spell Correction with Mask Sample Decoding](2210.08665.md)
**Ruchao Fan, Guoli Ye, Yashesh Gaur, Jinyu Li** · 2022-10-16

<details>
<summary>Abstract</summary>

Masked language model (MLM) has been widely used for understanding tasks, e.g. BERT. Recently, MLM has also been used for generation tasks. The most popular one in speech is using Mask-CTC for non-autoregressive speech recognition. In this paper, we take one step further, and explore the possibility of using MLM as a non-autoregressive spell correction (SC) model for transformer-transducer (TT), denoted as MLM-SC. Our initial experiments show that MLM-SC provides no improvements on Librispeech data. The problem might be the choice of modeling units (word pieces) and the inaccuracy of the TT confidence scores for English data. To solve the problem, we propose a mask sample decoding (MS-decode) method where the masked tokens can have the choice of being masked or not to compensate for the inaccuracy. As a result, we reduce the WER of a streaming TT from 7.6% to 6.5% on the Librispeech test-other data and the CER from 7.3% to 6.1% on the Aishell test data, respectively.

</details>

### [Learning to Jointly Transcribe and Subtitle for End-to-End Spontaneous Speech Recognition](2210.07771.md)
**Jakob Poncelet, Hugo Van hamme** · 2022-10-14

<details>
<summary>Abstract</summary>

TV subtitles are a rich source of transcriptions of many types of speech, ranging from read speech in news reports to conversational and spontaneous speech in talk shows and soaps. However, subtitles are not verbatim (i.e. exact) transcriptions of speech, so they cannot be used directly to improve an Automatic Speech Recognition (ASR) model. We propose a multitask dual-decoder Transformer model that jointly performs ASR and automatic subtitling. The ASR decoder (possibly pre-trained) predicts the verbatim output and the subtitle decoder generates a subtitle, while sharing the encoder. The two decoders can be independent or connected. The model is trained to perform both tasks jointly, and is able to effectively use subtitle data. We show improvements on regular ASR and on spontaneous and conversational ASR by incorporating the additional subtitle decoder. The method does not require preprocessing (aligning, filtering, pseudo-labeling, ...) of the subtitles.

</details>

### [LeVoice ASR Systems for the ISCSLP 2022 Intelligent Cockpit Speech Recognition Challenge](2210.07749.md)
**Yan Jia, Mi Hong, Jingyu Hou, Kailong Ren et al.** · 2022-10-14

<details>
<summary>Abstract</summary>

This paper describes LeVoice automatic speech recognition systems to track2 of intelligent cockpit speech recognition challenge 2022. Track2 is a speech recognition task without limits on the scope of model size. Our main points include deep learning based speech enhancement, text-to-speech based speech generation, training data augmentation via various techniques and speech recognition model fusion. We compared and fused the hybrid architecture and two kinds of end-to-end architecture. For end-to-end modeling, we used models based on connectionist temporal classification/attention-based encoder-decoder architecture and recurrent neural network transducer/attention-based encoder-decoder architecture. The performance of these models is evaluated with an additional language model to improve word error rates. As a result, our system achieved 10.2\% character error rate on the challenge test set data and ranked third place among the submitted systems in the challenge.

</details>

### [Experiments on Turkish ASR with Self-Supervised Speech Representation Learning](2210.07323.md)
**Ali Safaya, Engin Erzin** · 2022-10-13

<details>
<summary>Abstract</summary>

While the Turkish language is listed among low-resource languages, literature on Turkish automatic speech recognition (ASR) is relatively old. In this report, we present our findings on Turkish ASR with speech representation learning using HUBERT. We investigate pre-training HUBERT for Turkish with large-scale data curated from online resources. We pre-train our model using 6,500 hours of speech data from YouTube. The results show that the models are not ready for commercial use since they are not robust against disturbances that typically occur in real-world settings such as variations in accents, slang, background noise and interference. We analyze typical errors and the limitations of the models for use in commercial settings.

</details>

### [Multilingual Zero Resource Speech Recognition Base on Self-Supervise Pre-Trained Acoustic Models](2210.06936.md)
**Haoyu Wang, Wei-Qiang Zhang, Hongbin Suo, Yulong Wan** · 2022-10-13

<details>
<summary>Abstract</summary>

Labeled audio data is insufficient to build satisfying speech recognition systems for most of the languages in the world. There have been some zero-resource methods trying to perform phoneme or word-level speech recognition without labeled audio data of the target language, but the error rate of these methods is usually too high to be applied in real-world scenarios. Recently, the representation ability of self-supervise pre-trained models has been found to be extremely beneficial in zero-resource phoneme recognition. As far as we are concerned, this paper is the first attempt to extend the use of pre-trained models into word-level zero-resource speech recognition. This is done by fine-tuning the pre-trained models on IPA phoneme transcriptions and decoding with a language model trained on extra texts. Experiments on Wav2vec 2.0 and HuBERT models show that this method can achieve less than 20% word error rate on some languages, and the average error rate on 8 languages is 33.77%.

</details>

### [JOIST: A Joint Speech and Text Streaming Model For ASR](2210.07353.md)
**Tara N. Sainath, Rohit Prabhavalkar, Ankur Bapna, Yu Zhang et al.** · 2022-10-13

<details>
<summary>Abstract</summary>

We present JOIST, an algorithm to train a streaming, cascaded, encoder end-to-end (E2E) model with both speech-text paired inputs, and text-only unpaired inputs. Unlike previous works, we explore joint training with both modalities, rather than pre-training and fine-tuning. In addition, we explore JOIST using a streaming E2E model with an order of magnitude more data, which are also novelties compared to previous works. Through a series of ablation studies, we explore different types of text modeling, including how to model the length of the text sequence and the appropriate text sub-word unit representation. We find that best text representation for JOIST improves WER across a variety of search and rare-word test sets by 4-14% relative, compared to a model not trained with text. In addition, we quantitatively show that JOIST maintains streaming capabilities, which is important for good user-level experience.

</details>

### [Anonymizing Speech with Generative Adversarial Networks to Preserve Speaker Privacy](2210.07002.md)
**Sarina Meyer, Pascal Tilli, Pavel Denisov, Florian Lux et al.** · 2022-10-13

<details>
<summary>Abstract</summary>

In order to protect the privacy of speech data, speaker anonymization aims for hiding the identity of a speaker by changing the voice in speech recordings. This typically comes with a privacy-utility trade-off between protection of individuals and usability of the data for downstream applications. One of the challenges in this context is to create non-existent voices that sound as natural as possible. In this work, we propose to tackle this issue by generating speaker embeddings using a generative adversarial network with Wasserstein distance as cost function. By incorporating these artificial embeddings into a speech-to-text-to-speech pipeline, we outperform previous approaches in terms of privacy and utility. According to standard objective metrics and human evaluation, our approach generates intelligible and content-preserving yet privacy-protecting versions of the original recordings.

</details>

### [Foundation Transformers](2210.06423.md)
**Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong et al.** · 2022-10-12

<details>
<summary>Abstract</summary>

A big convergence of model architectures across language, vision, speech, and multimodal is emerging. However, under the same name "Transformers", the above areas use different implementations for better performance, e.g., Post-LayerNorm for BERT, and Pre-LayerNorm for GPT and vision Transformers. We call for the development of Foundation Transformer for true general-purpose modeling, which serves as a go-to architecture for various tasks and modalities with guaranteed training stability. In this work, we introduce a Transformer variant, named Magneto, to fulfill the goal. Specifically, we propose Sub-LayerNorm for good expressivity, and the initialization strategy theoretically derived from DeepNet for stable scaling up. Extensive experiments demonstrate its superior performance and better stability than the de facto Transformer variants designed for various applications, including language modeling (i.e., BERT, and GPT), machine translation, vision pretraining (i.e., BEiT), speech recognition, and multimodal pretraining (i.e., BEiT-3).

</details>

### [A context-aware knowledge transferring strategy for CTC-based ASR](2210.06244.md)
**Ke-Han Lu, Kuan-Yu Chen** · 2022-10-12

<details>
<summary>Abstract</summary>

Non-autoregressive automatic speech recognition (ASR) modeling has received increasing attention recently because of its fast decoding speed and superior performance. Among representatives, methods based on the connectionist temporal classification (CTC) are still a dominating stream. However, the theoretically inherent flaw, the assumption of independence between tokens, creates a performance barrier for the school of works. To mitigate the challenge, we propose a context-aware knowledge transferring strategy, consisting of a knowledge transferring module and a context-aware training strategy, for CTC-based ASR. The former is designed to distill linguistic information from a pre-trained language model, and the latter is framed to modulate the limitations caused by the conditional independence assumption. As a result, a knowledge-injected context-aware CTC-based ASR built upon the wav2vec2.0 is presented in this paper. A series of experiments on the AISHELL-1 and AISHELL-2 datasets demonstrate the effectiveness of the proposed method.

</details>

### [Comparison of Soft and Hard Target RNN-T Distillation for Large-scale ASR](2210.05793.md)
**Dongseong Hwang, Khe Chai Sim, Yu Zhang, Trevor Strohman** · 2022-10-11

<details>
<summary>Abstract</summary>

Knowledge distillation is an effective machine learning technique to transfer knowledge from a teacher model to a smaller student model, especially with unlabeled data. In this paper, we focus on knowledge distillation for the RNN-T model, which is widely used in state-of-the-art (SoTA) automatic speech recognition (ASR). Specifically, we compared using soft and hard target distillation to train large-scaleRNN-T models on the LibriSpeech/LibriLight public dataset (60k hours) and our in-house data (600k hours). We found that hard tar-gets are more effective when the teacher and student have different architecture, such as large teacher and small streaming student. On the other hand, soft target distillation works better in self-training scenario like iterative large teacher training. For a large model with0.6B weights, we achieve a new SoTA word error rate (WER) on LibriSpeech (8% relative improvement on dev-other) using Noisy Student Training with soft target distillation. It also allows our production teacher to adapt new data domain continuously.

</details>

### [Scaling Up Deliberation for Multilingual ASR](2210.05785.md)
**Ke Hu, Bo Li, Tara N. Sainath** · 2022-10-11

<details>
<summary>Abstract</summary>

Multilingual end-to-end automatic speech recognition models are attractive due to its simplicity in training and deployment. Recent work on large-scale training of such models has shown promising results compared to monolingual models. However, the work often focuses on multilingual models themselves in a single-pass setup. In this work, we investigate second-pass deliberation for multilingual speech recognition. Our proposed deliberation is multilingual, i.e., the text encoder encodes hypothesis text from multiple languages, and the decoder attends to multilingual text and audio. We investigate scaling the deliberation text encoder and decoder, and compare scaling the deliberation decoder and the first-pass cascaded encoder. We show that deliberation improves the average WER on 9 languages by 4% relative compared to the single-pass model. By increasing the size of the deliberation up to 1B parameters, the average WER improvement increases to 9%, with up to 14% for certain languages. Our deliberation rescorer is based on transformer layers and can be parallelized during rescoring.

</details>

### [Streaming Punctuation for Long-form Dictation with Transformers](2210.05756.md)
**Piyush Behre, Sharman Tan, Padma Varadharajan, Shuangyu Chang** · 2022-10-11

<details>
<summary>Abstract</summary>

While speech recognition Word Error Rate (WER) has reached human parity for English, long-form dictation scenarios still suffer from segmentation and punctuation problems resulting from irregular pausing patterns or slow speakers. Transformer sequence tagging models are effective at capturing long bi-directional context, which is crucial for automatic punctuation. Automatic Speech Recognition (ASR) production systems, however, are constrained by real-time requirements, making it hard to incorporate the right context when making punctuation decisions. In this paper, we propose a streaming approach for punctuation or re-punctuation of ASR output using dynamic decoding windows and measure its impact on punctuation and segmentation accuracy across scenarios. The new system tackles over-segmentation issues, improving segmentation F0.5-score by 13.9%. Streaming punctuation achieves an average BLEU-score improvement of 0.66 for the downstream task of Machine Translation (MT).

</details>

### [An Experimental Study on Private Aggregation of Teacher Ensemble Learning for End-to-End Speech Recognition](2210.05614.md)
**Chao-Han Huck Yang, I-Fan Chen, Andreas Stolcke, Sabato Marco Siniscalchi et al.** · 2022-10-11

<details>
<summary>Abstract</summary>

Differential privacy (DP) is one data protection avenue to safeguard user information used for training deep models by imposing noisy distortion on privacy data. Such a noise perturbation often results in a severe performance degradation in automatic speech recognition (ASR) in order to meet a privacy budget $\varepsilon$. Private aggregation of teacher ensemble (PATE) utilizes ensemble probabilities to improve ASR accuracy when dealing with the noise effects controlled by small values of $\varepsilon$. We extend PATE learning to work with dynamic patterns, namely speech utterances, and perform a first experimental demonstration that it prevents acoustic data leakage in ASR training. We evaluate three end-to-end deep models, including LAS, hybrid CTC/attention, and RNN transducer, on the open-source LibriSpeech and TIMIT corpora. PATE learning-enhanced ASR models outperform the benchmark DP-SGD mechanisms, especially under strict DP budgets, giving relative word error rate reductions between 26.2% and 27.5% for an RNN transducer model evaluated with LibriSpeech. We also introduce a DP-preserving ASR solution for pretraining on public speech corpora.

</details>

### [CTC Alignments Improve Autoregressive Translation](2210.05200.md)
**Brian Yan, Siddharth Dalmia, Yosuke Higuchi, Graham Neubig et al.** · 2022-10-11

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) is a widely used approach for automatic speech recognition (ASR) that performs conditionally independent monotonic alignment. However for translation, CTC exhibits clear limitations due to the contextual and non-monotonic nature of the task and thus lags behind attentional decoder approaches in terms of translation quality. In this work, we argue that CTC does in fact make sense for translation if applied in a joint CTC/attention framework wherein CTC's core properties can counteract several key weaknesses of pure-attention models during training and decoding. To validate this conjecture, we modify the Hybrid CTC/Attention model originally proposed for ASR to support text-to-text translation (MT) and speech-to-text translation (ST). Our proposed joint CTC/attention models outperform pure-attention baselines across six benchmark translation tasks.

</details>

### [ArabSign: A Multi-modality Dataset and Benchmark for Continuous Arabic Sign Language Recognition](2210.03951.md)
**Hamzah Luqman** · 2022-10-08

<details>
<summary>Abstract</summary>

Sign language recognition has attracted the interest of researchers in recent years. While numerous approaches have been proposed for European and Asian sign languages recognition, very limited attempts have been made to develop similar systems for the Arabic sign language (ArSL). This can be attributed partly to the lack of a dataset at the sentence level. In this paper, we aim to make a significant contribution by proposing ArabSign, a continuous ArSL dataset. The proposed dataset consists of 9,335 samples performed by 6 signers. The total time of the recorded sentences is around 10 hours and the average sentence's length is 3.1 signs. ArabSign dataset was recorded using a Kinect V2 camera that provides three types of information (color, depth, and skeleton joint points) recorded simultaneously for each sentence. In addition, we provide the annotation of the dataset according to ArSL and Arabic language structures that can help in studying the linguistic characteristics of ArSL. To benchmark this dataset, we propose an encoder-decoder model for Continuous ArSL recognition. The model has been evaluated on the proposed dataset, and the obtained results show that the encoder-decoder model outperformed the attention mechanism with an average word error rate (WER) of 0.50 compared with 0.62 with the attention mechanism. The data and code are available at github.com/Hamzah-Luqman/ArabSign

</details>

### [SpeechUT: Bridging Speech and Text with Hidden-Unit for Encoder-Decoder Based Speech-Text Pre-training](2210.03730.md)
**Ziqiang Zhang, Long Zhou, Junyi Ao, Shujie Liu et al.** · 2022-10-07

<details>
<summary>Abstract</summary>

The rapid development of single-modal pre-training has prompted researchers to pay more attention to cross-modal pre-training methods. In this paper, we propose a unified-modal speech-unit-text pre-training model, SpeechUT, to connect the representations of a speech encoder and a text decoder with a shared unit encoder. Leveraging hidden-unit as an interface to align speech and text, we can decompose the speech-to-text model into a speech-to-unit model and a unit-to-text model, which can be jointly pre-trained with unpaired speech and text data respectively. Our proposed SpeechUT is fine-tuned and evaluated on automatic speech recognition (ASR) and speech translation (ST) tasks. Experimental results show that SpeechUT gets substantial improvements over strong baselines, and achieves state-of-the-art performance on both the LibriSpeech ASR and MuST-C ST tasks. To better understand the proposed SpeechUT, detailed analyses are conducted. The code and pre-trained models are available at https://aka.ms/SpeechUT.

</details>

### [Pronunciation Modeling of Foreign Words for Mandarin ASR by Considering the Effect of Language Transfer](2210.03603.md)
**Lei Wang, Rong Tong** · 2022-10-07

<details>
<summary>Abstract</summary>

One of the challenges in automatic speech recognition is foreign words recognition. It is observed that a speaker's pronunciation of a foreign word is influenced by his native language knowledge, and such phenomenon is known as the effect of language transfer. This paper focuses on examining the phonetic effect of language transfer in automatic speech recognition. A set of lexical rules is proposed to convert an English word into Mandarin phonetic representation. In this way, a Mandarin lexicon can be augmented by including English words. Hence, the Mandarin ASR system becomes capable to recognize English words without retraining or re-estimation of the acoustic model parameters. Using the lexicon that derived from the proposed rules, the ASR performance of Mandarin English mixed speech is improved without harming the accuracy of Mandarin only speech. The proposed lexical rules are generalized and they can be directly applied to unseen English words.

</details>

### [Damage Control During Domain Adaptation for Transducer Based Automatic Speech Recognition](2210.03255.md)
**Somshubra Majumdar, Shantanu Acharya, Vitaly Lavrukhin, Boris Ginsburg** · 2022-10-06

<details>
<summary>Abstract</summary>

Automatic speech recognition models are often adapted to improve their accuracy in a new domain. A potential drawback of model adaptation to new domains is catastrophic forgetting, where the Word Error Rate on the original domain is significantly degraded. This paper addresses the situation when we want to simultaneously adapt automatic speech recognition models to a new domain and limit the degradation of accuracy on the original domain without access to the original training dataset. We propose several techniques such as a limited training strategy and regularized adapter modules for the Transducer encoder, prediction, and joiner network. We apply these methods to the Google Speech Commands and to the UK and Ireland English Dialect speech data set and obtain strong results on the new target domain while limiting the degradation on the original domain.

</details>

### [Synthetic Dataset Generation for Privacy-Preserving Machine Learning](2210.03205.md)
**Efstathia Soufleri, Gobinda Saha, Kaushik Roy** · 2022-10-06

<details>
<summary>Abstract</summary>

Machine Learning (ML) has achieved enormous success in solving a variety of problems in computer vision, speech recognition, object detection, to name a few. The principal reason for this success is the availability of huge datasets for training deep neural networks (DNNs). However, datasets can not be publicly released if they contain sensitive information such as medical or financial records. In such cases, data privacy becomes a major concern. Encryption methods offer a possible solution to this issue, however their deployment on ML applications is non-trivial, as they seriously impact the classification accuracy and result in substantial computational overhead.Alternatively, obfuscation techniques can be used, but maintaining a good balance between visual privacy and accuracy is challenging. In this work, we propose a method to generate secure synthetic datasets from the original private datasets. In our method, given a network with Batch Normalization (BN) layers pre-trained on the original dataset, we first record the layer-wise BN statistics. Next, using the BN statistics and the pre-trained model, we generate the synthetic dataset by optimizing random noises such that the synthetic data match the layer-wise statistical distribution of the original model. We evaluate our method on image classification dataset (CIFAR10) and show that our synthetic data can be used for training networks from scratch, producing reasonable classification performance.

</details>

### [JoeyS2T: Minimalistic Speech-to-Text Modeling with JoeyNMT](2210.02545.md)
**Mayumi Ohta, Julia Kreutzer, Stefan Riezler** · 2022-10-05

<details>
<summary>Abstract</summary>

JoeyS2T is a JoeyNMT extension for speech-to-text tasks such as automatic speech recognition and end-to-end speech translation. It inherits the core philosophy of JoeyNMT, a minimalist NMT toolkit built on PyTorch, seeking simplicity and accessibility. JoeyS2T's workflow is self-contained, starting from data pre-processing, over model training and prediction to evaluation, and is seamlessly integrated into JoeyNMT's compact and simple code base. On top of JoeyNMT's state-of-the-art Transformer-based encoder-decoder architecture, JoeyS2T provides speech-oriented components such as convolutional layers, SpecAugment, CTC-loss, and WER evaluation. Despite its simplicity compared to prior implementations, JoeyS2T performs competitively on English speech recognition and English-to-German speech translation benchmarks. The implementation is accompanied by a walk-through tutorial and available on https://github.com/may-/joeys2t.

</details>

### [Code-Switching without Switching: Language Agnostic End-to-End Speech Translation](2210.01512.md)
**Christian Huber, Enes Yavuz Ugan, Alexander Waibel** · 2022-10-04

<details>
<summary>Abstract</summary>

We propose a) a Language Agnostic end-to-end Speech Translation model (LAST), and b) a data augmentation strategy to increase code-switching (CS) performance. With increasing globalization, multiple languages are increasingly used interchangeably during fluent speech. Such CS complicates traditional speech recognition and translation, as we must recognize which language was spoken first and then apply a language-dependent recognizer and subsequent translation component to generate the desired target language output. Such a pipeline introduces latency and errors. In this paper, we eliminate the need for that, by treating speech recognition and translation as one unified end-to-end speech translation problem. By training LAST with both input languages, we decode speech into one target language, regardless of the input language. LAST delivers comparable recognition and speech translation accuracy in monolingual usage, while reducing latency and error rate considerably when CS is observed.

</details>

### [Learning with Limited Samples -- Meta-Learning and Applications to Communication Systems](2210.02515.md)
**Lisha Chen, Sharu Theresa Jose, Ivana Nikoloska, Sangwoo Park et al.** · 2022-10-03

<details>
<summary>Abstract</summary>

Deep learning has achieved remarkable success in many machine learning tasks such as image classification, speech recognition, and game playing. However, these breakthroughs are often difficult to translate into real-world engineering systems because deep learning models require a massive number of training samples, which are costly to obtain in practice. To address labeled data scarcity, few-shot meta-learning optimizes learning algorithms that can efficiently adapt to new tasks quickly. While meta-learning is gaining significant interest in the machine learning literature, its working principles and theoretic fundamentals are not as well understood in the engineering community. This review monograph provides an introduction to meta-learning by covering principles, algorithms, theory, and engineering applications. After introducing meta-learning in comparison with conventional and joint learning, we describe the main meta-learning algorithms, as well as a general bilevel optimization framework for the definition of meta-learning techniques. Then, we summarize known results on the generalization capabilities of meta-learning from a statistical learning viewpoint. Applications to communication systems, including decoding and power allocation, are discussed next, followed by an introduction to aspects related to the integration of meta-learning with emerging computing technologies, namely neuromorphic and quantum computing. The monograph is concluded with an overview of open research challenges.

</details>

### [Efficient acoustic feature transformation in mismatched environments using a Guided-GAN](2210.00721.md)
**Walter Heymans, Marelie H. Davel, Charl van Heerden** · 2022-10-03

<details>
<summary>Abstract</summary>

We propose a new framework to improve automatic speech recognition (ASR) systems in resource-scarce environments using a generative adversarial network (GAN) operating on acoustic input features. The GAN is used to enhance the features of mismatched data prior to decoding, or can optionally be used to fine-tune the acoustic model. We achieve improvements that are comparable to multi-style training (MTR), but at a lower computational cost. With less than one hour of data, an ASR system trained on good quality data, and evaluated on mismatched audio is improved by between 11.5% and 19.7% relative word error rate (WER). Experiments demonstrate that the framework can be very useful in under-resourced environments where training data and computational resources are limited. The GAN does not require parallel training data, because it utilises a baseline acoustic model to provide an additional loss term that guides the generator to create acoustic features that are better classified by the baseline.

</details>

### [A Comparison of Transformer, Convolutional, and Recurrent Neural Networks on Phoneme Recognition](2210.00367.md)
**Kyuhong Shim, Wonyong Sung** · 2022-10-01

<details>
<summary>Abstract</summary>

Phoneme recognition is a very important part of speech recognition that requires the ability to extract phonetic features from multiple frames. In this paper, we compare and analyze CNN, RNN, Transformer, and Conformer models using phoneme recognition. For CNN, the ContextNet model is used for the experiments. First, we compare the accuracy of various architectures under different constraints, such as the receptive field length, parameter size, and layer depth. Second, we interpret the performance difference of these models, especially when the observable sequence length varies. Our analyses show that Transformer and Conformer models benefit from the long-range accessibility of self-attention through input frames.

</details>

### [Multi-stage Progressive Compression of Conformer Transducer for On-device Speech Recognition](2210.00169.md)
**Jash Rathod, Nauman Dawalatabad, Shatrughan Singh, Dhananjaya Gowda** · 2022-10-01

<details>
<summary>Abstract</summary>

The smaller memory bandwidth in smart devices prompts development of smaller Automatic Speech Recognition (ASR) models. To obtain a smaller model, one can employ the model compression techniques. Knowledge distillation (KD) is a popular model compression approach that has shown to achieve smaller model size with relatively lesser degradation in the model performance. In this approach, knowledge is distilled from a trained large size teacher model to a smaller size student model. Also, the transducer based models have recently shown to perform well for on-device streaming ASR task, while the conformer models are efficient in handling long term dependencies. Hence in this work we employ a streaming transducer architecture with conformer as the encoder. We propose a multi-stage progressive approach to compress the conformer transducer model using KD. We progressively update our teacher model with the distilled student model in a multi-stage setup. On standard LibriSpeech dataset, our experimental results have successfully achieved compression rates greater than 60% without significant degradation in the performance compared to the larger teacher model.

</details>

### [Improving Automatic Speech Recognition Performance for Low-Resource Languages With Self-Supervised Models](s2:b4a9bf5dc675fdf5d6d18043d6b566ee5481710f.md)
**Jing Zhao, Weiqiang Zhang** · 2022-10-01

<details>
<summary>Abstract</summary>

Speech self-supervised learning has attracted much attention due to its promising performance in multiple downstream tasks, and has become a new growth engine for speech recognition in low-resource languages. In this paper, we exploit and analyze a series of wav2vec pre-trained models for speech recognition in 15 low-resource languages in the OpenASR21 Challenge. The investigation covers two important variables during pre-training, three fine-tuning methods, as well as applications in End-to-End and hybrid systems. First, pre-trained models with different pre-training audio data and architectures (wav2vec2.0, HuBERT and WavLM) are explored for their speech recognition performance in low-resource languages. Second, we investigate data utilization, multilingual learning, and the use of a phoneme-level recognition task in fine-tuning. Furthermore, we explore what effect fine-tuning has on the similarity of representations extracted from different transformer layers. The similarity analyses cover different pre-trained architectures and fine-tuning languages. We apply pre-trained representations to End-to-End and hybrid systems to confirm our representation analyses, which have obtained better performances as well.

</details>

### [E-Branchformer: Branchformer with Enhanced merging for speech recognition](2210.00077.md)
**Kwangyoun Kim, Felix Wu, Yifan Peng, Jing Pan et al.** · 2022-09-30

<details>
<summary>Abstract</summary>

Conformer, combining convolution and self-attention sequentially to capture both local and global information, has shown remarkable performance and is currently regarded as the state-of-the-art for automatic speech recognition (ASR). Several other studies have explored integrating convolution and self-attention but they have not managed to match Conformer's performance. The recently introduced Branchformer achieves comparable performance to Conformer by using dedicated branches of convolution and self-attention and merging local and global context from each branch. In this paper, we propose E-Branchformer, which enhances Branchformer by applying an effective merging method and stacking additional point-wise modules. E-Branchformer sets new state-of-the-art word error rates (WERs) 1.81% and 3.65% on LibriSpeech test-clean and test-other sets without using any external training data.

</details>

### [SpeechLM: Enhanced Speech Pre-Training with Unpaired Textual Data](2209.15329.md)
**Ziqiang Zhang, Sanyuan Chen, Long Zhou, Yu Wu et al.** · 2022-09-30

<details>
<summary>Abstract</summary>

How to boost speech pre-training with textual data is an unsolved problem due to the fact that speech and text are very different modalities with distinct characteristics. In this paper, we propose a cross-modal Speech and Language Model (SpeechLM) to explicitly align speech and text pre-training with a pre-defined unified discrete representation. Specifically, we introduce two alternative discrete tokenizers to bridge the speech and text modalities, including phoneme-unit and hidden-unit tokenizers, which can be trained using a small amount of paired speech-text data. Based on the trained tokenizers, we convert the unlabeled speech and text data into tokens of phoneme units or hidden units. The pre-training objective is designed to unify the speech and the text into the same discrete semantic space with a unified Transformer network. We evaluate SpeechLM on various spoken language processing tasks including speech recognition, speech translation, and universal representation evaluation framework SUPERB, demonstrating significant improvements on content-related tasks. Code and models are available at https://aka.ms/SpeechLM.

</details>

### [Adaptive Sparse and Monotonic Attention for Transformer-based Automatic Speech Recognition](2209.15176.md)
**Chendong Zhao, Jianzong Wang, Wen qi Wei, Xiaoyang Qu et al.** · 2022-09-30

<details>
<summary>Abstract</summary>

The Transformer architecture model, based on self-attention and multi-head attention, has achieved remarkable success in offline end-to-end Automatic Speech Recognition (ASR). However, self-attention and multi-head attention cannot be easily applied for streaming or online ASR. For self-attention in Transformer ASR, the softmax normalization function-based attention mechanism makes it impossible to highlight important speech information. For multi-head attention in Transformer ASR, it is not easy to model monotonic alignments in different heads. To overcome these two limits, we integrate sparse attention and monotonic attention into Transformer-based ASR. The sparse mechanism introduces a learned sparsity scheme to enable each self-attention structure to fit the corresponding head better. The monotonic attention deploys regularization to prune redundant heads for the multi-head attention structure. The experiments show that our method can effectively improve the attention mechanism on widely used benchmarks of speech recognition.

</details>

### [ConvRNN-T: Convolutional Augmented Recurrent Neural Network Transducers for Streaming Speech Recognition](2209.14868.md)
**Martin Radfar, Rohit Barnwal, Rupak Vignesh Swaminathan, Feng-Ju Chang et al.** · 2022-09-29

<details>
<summary>Abstract</summary>

The recurrent neural network transducer (RNN-T) is a prominent streaming end-to-end (E2E) ASR technology. In RNN-T, the acoustic encoder commonly consists of stacks of LSTMs. Very recently, as an alternative to LSTM layers, the Conformer architecture was introduced where the encoder of RNN-T is replaced with a modified Transformer encoder composed of convolutional layers at the frontend and between attention layers. In this paper, we introduce a new streaming ASR model, Convolutional Augmented Recurrent Neural Network Transducers (ConvRNN-T) in which we augment the LSTM-based RNN-T with a novel convolutional frontend consisting of local and global context CNN encoders. ConvRNN-T takes advantage of causal 1-D convolutional layers, squeeze-and-excitation, dilation, and residual blocks to provide both global and local audio context representation to LSTM layers. We show ConvRNN-T outperforms RNN-T, Conformer, and ContextNet on Librispeech and in-house data. In addition, ConvRNN-T offers less computational complexity compared to Conformer. ConvRNN-T's superior accuracy along with its low footprint make it a promising candidate for on-device streaming ASR technologies.

</details>

### [TVLT: Textless Vision-Language Transformer](2209.14156.md)
**Zineng Tang, Jaemin Cho, Yixin Nie, Mohit Bansal** · 2022-09-28

<details>
<summary>Abstract</summary>

In this work, we present the Textless Vision-Language Transformer (TVLT), where homogeneous transformer blocks take raw visual and audio inputs for vision-and-language representation learning with minimal modality-specific design, and do not use text-specific modules such as tokenization or automatic speech recognition (ASR). TVLT is trained by reconstructing masked patches of continuous video frames and audio spectrograms (masked autoencoding) and contrastive modeling to align video and audio. TVLT attains performance comparable to its text-based counterpart on various multimodal tasks, such as visual question answering, image retrieval, video retrieval, and multimodal sentiment analysis, with 28x faster inference speed and only 1/3 of the parameters. Our findings suggest the possibility of learning compact and efficient visual-linguistic representations from low-level visual and audio signals without assuming the prior existence of text. Our code and checkpoints are available at: https://github.com/zinengtang/TVLT

</details>

### [Audio Classification with Skyrmion Reservoirs](2209.13946.md)
**Robin Msiska, Jake Love, Jeroen Mulkers, Jonathan Leliaert et al.** · 2022-09-28

<details>
<summary>Abstract</summary>

Physical reservoir computing is a computational paradigm that enables spatio-temporal pattern recognition to be performed directly in matter. The use of physical matter leads the way towards energy-efficient devices capable of solving machine learning problems without having to build a system of millions of interconnected neurons. We propose a high performance "skyrmion mixture reservoir" that implements the reservoir computing model with multi-dimensional inputs. We show that our implementation solves spoken digit classification tasks at the nanosecond timescale, with an overall model accuracy of 97.4% and a less that 1% word error rate; the best performance ever reported for in-materio reservoir computers. Due to the quality of the results and the low power properties of magnetic texture reservoirs, we argue that skyrmion fabrics are a compelling candidate for reservoir computing.

</details>

### [On the Impact of Speech Recognition Errors in Passage Retrieval for Spoken Question Answering](2209.12944.md)
**Georgios Sidiropoulos, Svitlana Vakulenko, Evangelos Kanoulas** · 2022-09-26

<details>
<summary>Abstract</summary>

Interacting with a speech interface to query a Question Answering (QA) system is becoming increasingly popular. Typically, QA systems rely on passage retrieval to select candidate contexts and reading comprehension to extract the final answer. While there has been some attention to improving the reading comprehension part of QA systems against errors that automatic speech recognition (ASR) models introduce, the passage retrieval part remains unexplored. However, such errors can affect the performance of passage retrieval, leading to inferior end-to-end performance. To address this gap, we augment two existing large-scale passage ranking and open domain QA datasets with synthetic ASR noise and study the robustness of lexical and dense retrievers against questions with ASR noise. Furthermore, we study the generalizability of data augmentation techniques across different domains; with each domain being a different language dialect or accent. Finally, we create a new dataset with questions voiced by human users and use their transcriptions to show that the retrieval performance can further degrade when dealing with natural ASR noise instead of synthetic ASR noise.

</details>

### [Unsupervised domain adaptation for speech recognition with unsupervised error correction](2209.12043.md)
**Long Mai, Julie Carson-Berndsen** · 2022-09-24

<details>
<summary>Abstract</summary>

The transcription quality of automatic speech recognition (ASR) systems degrades significantly when transcribing audios coming from unseen domains. We propose an unsupervised error correction method for unsupervised ASR domain adaption, aiming to recover transcription errors caused by domain mismatch. Unlike existing correction methods that rely on transcribed audios for training, our approach requires only unlabeled data of the target domains in which a pseudo-labeling technique is applied to generate correction training samples. To reduce over-fitting to the pseudo data, we also propose an encoder-decoder correction model that can take into account additional information such as dialogue context and acoustic features. Experiment results show that our method obtains a significant word error rate (WER) reduction over non-adapted ASR systems. The correction model can also be applied on top of other adaptation approaches to bring an additional improvement of 10% relatively.

</details>

### [A Deep Investigation of RNN and Self-attention for the Cyrillic-Traditional Mongolian Bidirectional Conversion](2209.11963.md)
**Muhan Na, Rui Liu, Feilong, Guanglai Gao** · 2022-09-24

<details>
<summary>Abstract</summary>

Cyrillic and Traditional Mongolian are the two main members of the Mongolian writing system. The Cyrillic-Traditional Mongolian Bidirectional Conversion (CTMBC) task includes two conversion processes, including Cyrillic Mongolian to Traditional Mongolian (C2T) and Traditional Mongolian to Cyrillic Mongolian conversions (T2C). Previous researchers adopted the traditional joint sequence model, since the CTMBC task is a natural Sequence-to-Sequence (Seq2Seq) modeling problem. Recent studies have shown that Recurrent Neural Network (RNN) and Self-attention (or Transformer) based encoder-decoder models have shown significant improvement in machine translation tasks between some major languages, such as Mandarin, English, French, etc. However, an open problem remains as to whether the CTMBC quality can be improved by utilizing the RNN and Transformer models. To answer this question, this paper investigates the utility of these two powerful techniques for CTMBC task combined with agglutinative characteristics of Mongolian language. We build the encoder-decoder based CTMBC model based on RNN and Transformer respectively and compare the different network configurations deeply. The experimental results show that both RNN and Transformer models outperform the traditional joint sequence model, where the Transformer achieves the best performance. Compared with the joint sequence baseline, the word error rate (WER) of the Transformer for C2T and T2C decreased by 5.72\% and 5.06\% respectively.

</details>

### [Relaxed Attention for Transformer Models](2209.09735.md)
**Timo Lohrenz, Björn Möller, Zhengyang Li, Tim Fingscheidt** · 2022-09-20

<details>
<summary>Abstract</summary>

The powerful modeling capabilities of all-attention-based transformer architectures often cause overfitting and - for natural language processing tasks - lead to an implicitly learned internal language model in the autoregressive transformer decoder complicating the integration of external language models. In this paper, we explore relaxed attention, a simple and easy-to-implement smoothing of the attention weights, yielding a two-fold improvement to the general transformer architecture: First, relaxed attention provides regularization when applied to the self-attention layers in the encoder. Second, we show that it naturally supports the integration of an external language model as it suppresses the implicitly learned internal language model by relaxing the cross attention in the decoder. We demonstrate the benefit of relaxed attention across several tasks with clear improvement in combination with recent benchmark approaches. Specifically, we exceed the former state-of-the-art performance of 26.90% word error rate on the largest public lip-reading LRS3 benchmark with a word error rate of 26.31%, as well as we achieve a top-performing BLEU score of 37.67 on the IWSLT14 (DE$\rightarrow$EN) machine translation task without external language models and virtually no additional model parameters. Code and models will be made publicly available.

</details>

### [HAPI: A Large-scale Longitudinal Dataset of Commercial ML API Predictions](2209.08443.md)
**Lingjiao Chen, Zhihua Jin, Sabri Eyuboglu, Christopher Ré et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

Commercial ML APIs offered by providers such as Google, Amazon and Microsoft have dramatically simplified ML adoption in many applications. Numerous companies and academics pay to use ML APIs for tasks such as object detection, OCR and sentiment analysis. Different ML APIs tackling the same task can have very heterogeneous performance. Moreover, the ML models underlying the APIs also evolve over time. As ML APIs rapidly become a valuable marketplace and a widespread way to consume machine learning, it is critical to systematically study and compare different APIs with each other and to characterize how APIs change over time. However, this topic is currently underexplored due to the lack of data. In this paper, we present HAPI (History of APIs), a longitudinal dataset of 1,761,417 instances of commercial ML API applications (involving APIs from Amazon, Google, IBM, Microsoft and other providers) across diverse tasks including image tagging, speech recognition and text mining from 2020 to 2022. Each instance consists of a query input for an API (e.g., an image or text) along with the API's output prediction/annotation and confidence scores. HAPI is the first large-scale dataset of ML API usages and is a unique resource for studying ML-as-a-service (MLaaS). As examples of the types of analyses that HAPI enables, we show that ML APIs' performance change substantially over time--several APIs' accuracies dropped on specific benchmark datasets. Even when the API's aggregate performance stays steady, its error modes can shift across different subtypes of data between 2020 and 2022. Such changes can substantially impact the entire analytics pipelines that use some ML API as a component. We further use HAPI to study commercial APIs' performance disparities across demographic subgroups over time. HAPI can stimulate more research in the growing field of MLaaS.

</details>

### [Bring dialogue-context into RNN-T for streaming ASR](s2:e926060cfef925abd4445e0cb6b5c9f6d465269e.md)
**Junfeng Hou, Jinkun Chen, Wanyu Li, Yufeng Tang et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

Recently the conversational end-to-end (E2E) automatic speech recognition (ASR) models, which directly integrate dialogue-context such as historical utterances into E2E models, have shown superior performance than single-utterance E2E models. However, few works investigate how to inject the dialogue-context into the recurrent neural network transducer (RNN-T) model. In this work, we bring dialogue-context into a streaming RNN-T model and explore various structures of contextual RNN-T model as well as training strategies to better utilize the dialogue-context. Firstly, we propose a deep fusion architecture which efficiently integrates the dialogue-context within the encoder and predictor of RNN-T. Secondly, we propose contextual & non-contextual model joint training as regularization, and propose context perturbation to relieve the context mismatch between training and inference. Moreover, we adopt a context-aware language model (CLM) for contextual RNN-T decoding to take full advantage of the dialogue-context for conversational ASR. We conduct experiments on the Switchboard-2000h task and observe performance gains from the proposed techniques. Compared with non-contextual RNN-T, our contextual RNN-T model yields 4.8% / 6.0% relative improvement on Switchboard and Callhome Hub5’00 testsets. By additionally integrating a CLM, the gain is further increased to 10.6% / 7.8%.

</details>

### [Streaming Automatic Speech Recognition with Re-blocking Processing Based on Integrated Voice Activity Detection](s2:8abcc9457a3fc14ab6af0e6e0e75f7318a95ff47.md)
**Yui Sudo, Muhammad Shakeel, K. Nakadai, Jiatong Shi et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

This paper proposes streaming automatic speech recognition (ASR) with re-blocking processing based on integrated voice activity detection (VAD). End-to-end (E2E) ASR models are promising for practical ASR. One of the key issues in realizing such a system is the detection of voice segments to cope with streaming input. There are three challenges for speech segmentation in streaming applications: 1) the extra VAD module in addition to the ASR model increases the system complexity and the number of parameters, 2) inappropriate segmentation of speech for block-based streaming methods dete-riorates the performance, 3) non-voice segments that are not discarded results in the increase of unnecessary computational costs. This paper proposes a model that integrates a VAD branch into a block processing-based streaming ASR system and a re-blocking technique to avoid inappropriate isolation of the utterances. Experiments show that the proposed method reduces the detection error rate (ER) by 25.8% on the AMI dataset with a less than 1% of increase in the number of parameters. Furthermore, the proposed method show 7.5% relative improvement in character error rate (CER) on the CSJ dataset with 27.3% reduction in real-time factor (RTF).

</details>

### [Global RNN Transducer Models For Multi-dialect Speech Recognition](s2:28eaac4eff4c78313b11e0b76e5ed9f1fa3cf23a.md)
**Takashi Fukuda, Samuel Thomas, Masayuki Suzuki, Gakuto Kurata et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

Constructing single, uniﬁed automatic speech recognition (ASR) models that work effectively across various dialects of a language is a challenging problem. Although many recently proposed approaches are effective, they are computationally more expensive compared to the conventional approach of us-ing ASR models designed separately for each dialect. In this paper, we propose a novel modeling technique for constructing accurate, multi-dialect, speech recognition systems with a single uniﬁed model, based on recurrent neural network transducers (RNN-T), which does not incur any extra computational costs at decoding time. Once a model has been created, the same decoding settings can also be used across all dialects. In our proposed approach, an RNN-T model with a shared encoder, common joint network and multi-branch prediction networks is ﬁrst constructed. After training each prediction network on an ASR task corresponding to various dialects, an effective interpolation step combines the multi-branch prediction networks back into a computationally-efﬁcient single branch. The effectiveness of the proposed technique is shown on ASR tasks on major English dialects. The proposed method approaches oracle performance and improves by 15-30% relative over dialect-speciﬁc models in dialect agnostic conditions.

</details>

### [RNN Transducers for Named Entity Recognition with constraints on alignment for understanding medical conversations](s2:2fec02d05c646b752a3081e6ad90b5ef1124ce19.md)
**H. Soltau, Izhak Shafran, Mingqiu Wang, Laurent El Shafey** · 2022-09-18

<details>
<summary>Abstract</summary>

Understanding medical conversations requires detecting entities such as Medications, Symptoms, Treatment, Conditions and Diagnosis, which leads to large ontologies with overlapping spans. Moreover, for ease of adoption by the clinicians, the inference also needs to locate the position of the entities in the conversations. Popular solutions to Named Entity Recognition (NER) such as conditional random ﬁelds, sequence-to-sequence models, or the question-answering framework are not suitable for this task. We address this problem by proposing a new model for NER task – an RNN transducer (RNN-T), which has hitherto been used only in speech recognition. These models are trained using paired input and output sequences without explicitly specifying the alignment between them, similar to other seq-to-seq models. RNN-T models learn the alignment using a loss function that sums over all alignments. In NER tasks, however, the alignment between words and target labels are available from the human annotations. We propose a ﬁxed alignment RNN-T model that utilizes the given alignment, while preserving the beneﬁts of RNN-Ts such as modeling output dependencies. As a more general case, we also propose a constrained alignment model where users can specify a relaxation of the given input alignment and the model will learn an alignment within the given constraints. In other words, we propose a family of seq-to-seq models which can leverage alignments between input and target sequences when available. Through empirical experiments on a challenging real-world medical NER task with multiple nested ontologies, we demonstrate that our ﬁxed alignment model out-performs the standard RNN-T model, improving F1-score from 0 . 70 to 0 . 74 .

</details>

### [Knowledge Distillation via Module Replacing for Automatic Speech Recognition with Recurrent Neural Network Transducer](s2:7c0c9d8c446c1619912b1f543fdc3a15955e1ac2.md)
**Kaiqi Zhao, H. Nguyen, Animesh Jain, Nathan Susanj et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is increasingly used by edge applications such as intelligent virtual assistants. However, state-of-the-art ASR models such as Recurrent Neural Network - Transducer (RNN-T) are computationally intensive on resource-constrained edge devices. Knowledge Distillation (KD) is a promising approach to compress large models by us-ing a large model (”teacher”) to train a small model (”student”). This paper proposes a novel KD method called Log-Curriculum based Module Replacing (LCMR) for RNN-T. LCMR compresses RNN-T and addresses its unique characteristics by re-placing teacher modules including multiple LSTM/Dense layers with substitutional student modules that contain less Long Short Term Memory (LSTM)/Dense layers. LCMR employs a novel nonlinear Curriculum Learning driven replacement strategy to further improve the performance by updating replacing rates with a dynamic, smoothing mechanism. Under LCMR, the student and teacher are able to interact at gradient level, and tranfser knowledge more effectively than conventional KD. Evaluation shows that LCMR reduces word-error-rate (WER) by 14.47%-33.24% relative compared to conventional KD.

</details>

### [Watch What You Pretrain For: Targeted, Transferable Adversarial Examples on Self-Supervised Speech Recognition models](2209.13523.md)
**Raphael Olivier, Hadi Abdullah, Bhiksha Raj** · 2022-09-17

<details>
<summary>Abstract</summary>

A targeted adversarial attack produces audio samples that can force an Automatic Speech Recognition (ASR) system to output attacker-chosen text. To exploit ASR models in real-world, black-box settings, an adversary can leverage the transferability property, i.e. that an adversarial sample produced for a proxy ASR can also fool a different remote ASR. However recent work has shown that transferability against large ASR models is very difficult. In this work, we show that modern ASR architectures, specifically ones based on Self-Supervised Learning, are in fact vulnerable to transferability. We successfully demonstrate this phenomenon by evaluating state-of-the-art self-supervised ASR models like Wav2Vec2, HuBERT, Data2Vec and WavLM. We show that with low-level additive noise achieving a 30dB Signal-Noise Ratio, we can achieve target transferability with up to 80% accuracy. Next, we 1) use an ablation study to show that Self-Supervised learning is the main cause of that phenomenon, and 2) we provide an explanation for this phenomenon. Through this we show that modern ASR architectures are uniquely vulnerable to adversarial security threats.

</details>

### [Parameter-Efficient Conformers via Sharing Sparsely-Gated Experts for End-to-End Speech Recognition](2209.08326.md)
**Ye Bai, Jie Li, Wenjing Han, Hao Ni et al.** · 2022-09-17

<details>
<summary>Abstract</summary>

While transformers and their variant conformers show promising performance in speech recognition, the parameterized property leads to much memory cost during training and inference. Some works use cross-layer weight-sharing to reduce the parameters of the model. However, the inevitable loss of capacity harms the model performance. To address this issue, this paper proposes a parameter-efficient conformer via sharing sparsely-gated experts. Specifically, we use sparsely-gated mixture-of-experts (MoE) to extend the capacity of a conformer block without increasing computation. Then, the parameters of the grouped conformer blocks are shared so that the number of parameters is reduced. Next, to ensure the shared blocks with the flexibility of adapting representations at different levels, we design the MoE routers and normalization individually. Moreover, we use knowledge distillation to further improve the performance. Experimental results show that the proposed model achieves competitive performance with 1/3 of the parameters of the encoder, compared with the full-parameter model.

</details>

### [An Automatic Speech Recognition System for Bengali Language based on Wav2Vec2 and Transfer Learning](2209.08119.md)
**Tushar Talukder Showrav** · 2022-09-16

<details>
<summary>Abstract</summary>

An independent, automated method of decoding and transcribing oral speech is known as automatic speech recognition (ASR). A typical ASR system extracts feature from audio recordings or streams and run one or more algorithms to map the features to corresponding texts. Numerous of research has been done in the field of speech signal processing in recent years. When given adequate resources, both conventional ASR and emerging end-to-end (E2E) speech recognition have produced promising results. However, for low-resource languages like Bengali, the current state of ASR lags behind, although the low resource state does not reflect upon the fact that this language is spoken by over 500 million people all over the world. Despite its popularity, there aren't many diverse open-source datasets available, which makes it difficult to conduct research on Bengali speech recognition systems. This paper is a part of the competition named `BUET CSE Fest DL Sprint'. The purpose of this paper is to improve the speech recognition performance of the Bengali language by adopting speech recognition technology on the E2E structure based on the transfer learning framework. The proposed method effectively models the Bengali language and achieves 3.819 score in `Levenshtein Mean Distance' on the test dataset of 7747 samples, when only 1000 samples of train dataset were used to train.

</details>

### [ESSumm: Extractive Speech Summarization from Untranscribed Meeting](2209.06913.md)
**Jun Wang** · 2022-09-14

<details>
<summary>Abstract</summary>

In this paper, we propose a novel architecture for direct extractive speech-to-speech summarization, ESSumm, which is an unsupervised model without dependence on intermediate transcribed text. Different from previous methods with text presentation, we are aimed at generating a summary directly from speech without transcription. First, a set of smaller speech segments are extracted based on speech signal's acoustic features. For each candidate speech segment, a distance-based summarization confidence score is designed for latent speech representation measure. Specifically, we leverage the off-the-shelf self-supervised convolutional neural network to extract the deep speech features from raw audio. Our approach automatically predicts the optimal sequence of speech segments that capture the key information with a target summary length. Extensive results on two well-known meeting datasets (AMI and ICSI corpora) show the effectiveness of our direct speech-based method to improve the summarization quality with untranscribed data. We also observe that our unsupervised speech-based method even performs on par with recent transcript-based summarization approaches, where extra speech recognition is required.

</details>

### [A Universally-Deployable ASR Frontend for Joint Acoustic Echo Cancellation, Speech Enhancement, and Voice Separation](2209.06410.md)
**Tom O'Malley, Arun Narayanan, Quan Wang** · 2022-09-14

<details>
<summary>Abstract</summary>

Recent work has shown that it is possible to train a single model to perform joint acoustic echo cancellation (AEC), speech enhancement, and voice separation, thereby serving as a unified frontend for robust automatic speech recognition (ASR). The joint model uses contextual information, such as a reference of the playback audio, noise context, and speaker embedding. In this work, we propose a number of novel improvements to such a model. First, we improve the architecture of the Cross-Attention Conformer that is used to ingest noise context into the model. Second, we generalize the model to be able to handle varying lengths of noise context. Third, we propose Signal Dropout, a novel strategy that models missing contextual information. In the absence of one or more signals, the proposed model performs nearly as well as task-specific models trained without these signals; and when such signals are present, our system compares well against systems that require all context signals. Over the baseline, the final model retains a relative word error rate reduction of 25.0% on background speech when speaker embedding is absent, and 61.2% on AEC when device playback is absent.

</details>

### [Federated Pruning: Improving Neural Network Efficiency with Federated Learning](2209.06359.md)
**Rongmei Lin, Yonghui Xiao, Tien-Ju Yang, Ding Zhao et al.** · 2022-09-14

<details>
<summary>Abstract</summary>

Automatic Speech Recognition models require large amount of speech data for training, and the collection of such data often leads to privacy concerns. Federated learning has been widely used and is considered to be an effective decentralized technique by collaboratively learning a shared prediction model while keeping the data local on different clients devices. However, the limited computation and communication resources on clients devices present practical difficulties for large models. To overcome such challenges, we propose Federated Pruning to train a reduced model under the federated setting, while maintaining similar performance compared to the full model. Moreover, the vast amount of clients data can also be leveraged to improve the pruning results compared to centralized training. We explore different pruning schemes and provide empirical evidence of the effectiveness of our methods.

</details>

### [Bangla-Wave: Improving Bangla Automatic Speech Recognition Utilizing N-gram Language Models](2209.12650.md)
**Mohammed Rakib, Md. Ismail Hossain, Nabeel Mohammed, Fuad Rahman** · 2022-09-13

<details>
<summary>Abstract</summary>

Although over 300M around the world speak Bangla, scant work has been done in improving Bangla voice-to-text transcription due to Bangla being a low-resource language. However, with the introduction of the Bengali Common Voice 9.0 speech dataset, Automatic Speech Recognition (ASR) models can now be significantly improved. With 399hrs of speech recordings, Bengali Common Voice is the largest and most diversified open-source Bengali speech corpus in the world. In this paper, we outperform the SOTA pretrained Bengali ASR models by finetuning a pretrained wav2vec2 model on the common voice dataset. We also demonstrate how to significantly improve the performance of an ASR model by adding an n-gram language model as a post-processor. Finally, we do some experiments and hyperparameter tuning to generate a robust Bangla ASR model that is better than the existing ASR models.

</details>

### [Analysis of Self-Attention Head Diversity for Conformer-based Automatic Speech Recognition](2209.06096.md)
**Kartik Audhkhasi, Yinghui Huang, Bhuvana Ramabhadran, Pedro J. Moreno** · 2022-09-13

<details>
<summary>Abstract</summary>

Attention layers are an integral part of modern end-to-end automatic speech recognition systems, for instance as part of the Transformer or Conformer architecture. Attention is typically multi-headed, where each head has an independent set of learned parameters and operates on the same input feature sequence. The output of multi-headed attention is a fusion of the outputs from the individual heads. We empirically analyze the diversity between representations produced by the different attention heads and demonstrate that the heads become highly correlated during the course of training. We investigate a few approaches to increasing attention head diversity, including using different attention mechanisms for each head and auxiliary training loss functions to promote head diversity. We show that introducing diversity-promoting auxiliary loss functions during training is a more effective approach, and obtain WER improvements of up to 6% relative on the Librispeech corpus. Finally, we draw a connection between the diversity of attention heads and the similarity of the gradients of head parameters.

</details>

### [Streaming End-to-End Multilingual Speech Recognition with Joint Language Identification](2209.06058.md)
**Chao Zhang, Bo Li, Tara Sainath, Trevor Strohman et al.** · 2022-09-13

<details>
<summary>Abstract</summary>

Language identification is critical for many downstream tasks in automatic speech recognition (ASR), and is beneficial to integrate into multilingual end-to-end ASR as an additional task. In this paper, we propose to modify the structure of the cascaded-encoder-based recurrent neural network transducer (RNN-T) model by integrating a per-frame language identifier (LID) predictor. RNN-T with cascaded encoders can achieve streaming ASR with low latency using first-pass decoding with no right-context, and achieve lower word error rates (WERs) using second-pass decoding with longer right-context. By leveraging such differences in the right-contexts and a streaming implementation of statistics pooling, the proposed method can achieve accurate streaming LID prediction with little extra test-time cost. Experimental results on a voice search dataset with 9 language locales shows that the proposed method achieves an average of 96.2% LID prediction accuracy and the same second-pass WER as that obtained by including oracle LID in the input.

</details>

### [Learning ASR pathways: A sparse multilingual ASR model](2209.05735.md)
**Mu Yang, Andros Tjandra, Chunxi Liu, David Zhang et al.** · 2022-09-13

<details>
<summary>Abstract</summary>

Neural network pruning compresses automatic speech recognition (ASR) models effectively. However, in multilingual ASR, language-agnostic pruning may lead to severe performance drops on some languages because language-agnostic pruning masks may not fit all languages and discard important language-specific parameters. In this work, we present ASR pathways, a sparse multilingual ASR model that activates language-specific sub-networks ("pathways"), such that the parameters for each language are learned explicitly. With the overlapping sub-networks, the shared parameters can also enable knowledge transfer for lower-resource languages via joint multilingual training. We propose a novel algorithm to learn ASR pathways, and evaluate the proposed method on 4 languages with a streaming RNN-T model. Our proposed ASR pathways outperform both dense models and a language-agnostically pruned model, and provide better performance on low-resource languages compared to the monolingual sparse models.

</details>

### [Deep Speech Synthesis from Articulatory Representations](2209.06337.md)
**Peter Wu, Shinji Watanabe, Louis Goldstein, Alan W Black et al.** · 2022-09-13

<details>
<summary>Abstract</summary>

In the articulatory synthesis task, speech is synthesized from input features containing information about the physical behavior of the human vocal tract. This task provides a promising direction for speech synthesis research, as the articulatory space is compact, smooth, and interpretable. Current works have highlighted the potential for deep learning models to perform articulatory synthesis. However, it remains unclear whether these models can achieve the efficiency and fidelity of the human speech production system. To help bridge this gap, we propose a time-domain articulatory synthesis methodology and demonstrate its efficacy with both electromagnetic articulography (EMA) and synthetic articulatory feature inputs. Our model is computationally efficient and achieves a transcription word error rate (WER) of 18.5% for the EMA-to-speech task, yielding an improvement of 11.6% compared to prior work. Through interpolation experiments, we also highlight the generalizability and interpretability of our approach.

</details>

### [Applying wav2vec2 for Speech Recognition on Bengali Common Voices Dataset](2209.06581.md)
**H. A. Z. Sameen Shahgir, Khondker Salman Sayeed, Tanjeem Azwad Zaman** · 2022-09-11

<details>
<summary>Abstract</summary>

Speech is inherently continuous, where discrete words, phonemes and other units are not clearly segmented, and so speech recognition has been an active research problem for decades. In this work we have fine-tuned wav2vec 2.0 to recognize and transcribe Bengali speech -- training it on the Bengali Common Voice Speech Dataset. After training for 71 epochs, on a training set consisting of 36919 mp3 files, we achieved a training loss of 0.3172 and WER of 0.2524 on a validation set of size 7,747. Using a 5-gram language model, the Levenshtein Distance was 2.6446 on a test set of size 7,747. Then the training set and validation set were combined, shuffled and split into 85-15 ratio. Training for 7 more epochs on this combined dataset yielded an improved Levenshtein Distance of 2.60753 on the test set. Our model was the best performing one, achieving a Levenshtein Distance of 6.234 on a hidden dataset, which was 1.1049 units lower than other competing submissions.

</details>

### [Lexicon and Attention based Handwritten Text Recognition System](2209.04817.md)
**Lalita Kumari, Sukhdeep Singh, VVS Rathore, Anuj Sharma** · 2022-09-11

<details>
<summary>Abstract</summary>

The handwritten text recognition problem is widely studied by the researchers of computer vision community due to its scope of improvement and applicability to daily lives, It is a sub-domain of pattern recognition. Due to advancement of computational power of computers since last few decades neural networks based systems heavily contributed towards providing the state-of-the-art handwritten text recognizers. In the same direction, we have taken two state-of-the art neural networks systems and merged the attention mechanism with it. The attention technique has been widely used in the domain of neural machine translations and automatic speech recognition and now is being implemented in text recognition domain. In this study, we are able to achieve 4.15% character error rate and 9.72% word error rate on IAM dataset, 7.07% character error rate and 16.14% word error rate on GW dataset after merging the attention and word beam search decoder with existing Flor et al. architecture. To analyse further, we have also used system similar to Shi et al. neural network system with greedy decoder and observed 23.27% improvement in character error rate from the base model.

</details>

### [Streaming Target-Speaker ASR with Neural Transducer](2209.04175.md)
**Takafumi Moriya, Hiroshi Sato, Tsubasa Ochiai, Marc Delcroix et al.** · 2022-09-09

<details>
<summary>Abstract</summary>

Although recent advances in deep learning technology have boosted automatic speech recognition (ASR) performance in the single-talker case, it remains difficult to recognize multi-talker speech in which many voices overlap. One conventional approach to tackle this problem is to use a cascade of a speech separation or target speech extraction front-end with an ASR back-end. However, the extra computation costs of the front-end module are a critical barrier to quick response, especially for streaming ASR. In this paper, we propose a target-speaker ASR (TS-ASR) system that implicitly integrates the target speech extraction functionality within a streaming end-to-end (E2E) ASR system, i.e. recurrent neural network-transducer (RNNT). Our system uses a similar idea as adopted for target speech extraction, but implements it directly at the level of the encoder of RNNT. This allows TS-ASR to be realized without placing extra computation costs on the front-end. Note that this study presents two major differences between prior studies on E2E TS-ASR; we investigate streaming models and base our study on Conformer models, whereas prior studies used RNN-based systems and considered only offline processing. We confirm in experiments that our TS-ASR achieves comparable recognition performance with conventional cascade systems in the offline setting, while reducing computation costs and realizing streaming TS-ASR.

</details>

### [Non-autoregressive Error Correction for CTC-based ASR with Phone-conditioned Masked LM](2209.04062.md)
**Hayato Futami, Hirofumi Inaguma, Sei Ueno, Masato Mimura et al.** · 2022-09-08

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) -based models are attractive in automatic speech recognition (ASR) because of their non-autoregressive nature. To take advantage of text-only data, language model (LM) integration approaches such as rescoring and shallow fusion have been widely used for CTC. However, they lose CTC's non-autoregressive nature because of the need for beam search, which slows down the inference speed. In this study, we propose an error correction method with phone-conditioned masked LM (PC-MLM). In the proposed method, less confident word tokens in a greedy decoded output from CTC are masked. PC-MLM then predicts these masked word tokens given unmasked words and phones supplementally predicted from CTC. We further extend it to Deletable PC-MLM in order to address insertion errors. Since both CTC and PC-MLM are non-autoregressive models, the method enables fast LM integration. Experimental evaluations on the Corpus of Spontaneous Japanese (CSJ) and TED-LIUM2 in domain adaptation setting shows that our proposed method outperformed rescoring and shallow fusion in terms of inference speed, and also in terms of recognition accuracy on CSJ.

</details>

### [Multilingual Transformer Language Model for Speech Recognition in Low-resource Languages](2209.04041.md)
**Li Miao, Jian Wu, Piyush Behre, Shuangyu Chang et al.** · 2022-09-08

<details>
<summary>Abstract</summary>

It is challenging to train and deploy Transformer LMs for hybrid speech recognition 2nd pass re-ranking in low-resource languages due to (1) data scarcity in low-resource languages, (2) expensive computing costs for training and refreshing 100+ monolingual models, and (3) hosting inefficiency considering sparse traffic. In this study, we present a new way to group multiple low-resource locales together and optimize the performance of Multilingual Transformer LMs in ASR. Our Locale-group Multilingual Transformer LMs outperform traditional multilingual LMs along with reducing maintenance costs and operating expenses. Further, for low-resource but high-traffic locales where deploying monolingual models is feasible, we show that fine-tuning our locale-group multilingual LMs produces better monolingual LM candidates than baseline monolingual LMs.

</details>

### [Plant Species Classification Using Transfer Learning by Pretrained Classifier VGG-19](2209.03076.md)
**Thiru Siddharth, Bhupendra Singh Kirar, Dheeraj Kumar Agrawal** · 2022-09-07

<details>
<summary>Abstract</summary>

Deep learning is currently the most important branch of machine learning, with applications in speech recognition, computer vision, image classification, and medical imaging analysis. Plant recognition is one of the areas where image classification can be used to identify plant species through their leaves. Botanists devote a significant amount of time to recognizing plant species by personally inspecting. This paper describes a method for dissecting color images of Swedish leaves and identifying plant species. To achieve higher accuracy, the task is completed using transfer learning with the help of pre-trained classifier VGG-19. The four primary processes of classification are image preprocessing, image augmentation, feature extraction, and recognition, which are performed as part of the overall model evaluation. The VGG-19 classifier grasps the characteristics of leaves by employing pre-defined hidden layers such as convolutional layers, max pooling layers, and fully connected layers, and finally uses the soft-max layer to generate a feature representation for all plant classes. The model obtains knowledge connected to aspects of the Swedish leaf dataset, which contains fifteen tree classes, and aids in predicting the proper class of an unknown plant with an accuracy of 99.70% which is higher than previous research works reported.

</details>

### [ASR2K: Speech Recognition for Around 2000 Languages without Audio](2209.02842.md)
**Xinjian Li, Florian Metze, David R Mortensen, Alan W Black et al.** · 2022-09-06

<details>
<summary>Abstract</summary>

Most recent speech recognition models rely on large supervised datasets, which are unavailable for many low-resource languages. In this work, we present a speech recognition pipeline that does not require any audio for the target language. The only assumption is that we have access to raw text datasets or a set of n-gram statistics. Our speech pipeline consists of three components: acoustic, pronunciation, and language models. Unlike the standard pipeline, our acoustic and pronunciation models use multilingual models without any supervision. The language model is built using n-gram statistics or the raw text dataset. We build speech recognition for 1909 languages by combining it with Crubadan: a large endangered languages n-gram database. Furthermore, we test our approach on 129 languages across two datasets: Common Voice and CMU Wilderness dataset. We achieve 50% CER and 74% WER on the Wilderness dataset with Crubadan statistics only and improve them to 45% CER and 69% WER when using 10000 raw text utterances.

</details>

### [Distilling the Knowledge of BERT for CTC-based ASR](2209.02030.md)
**Hayato Futami, Hirofumi Inaguma, Masato Mimura, Shinsuke Sakai et al.** · 2022-09-05

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) -based models are attractive because of their fast inference in automatic speech recognition (ASR). Language model (LM) integration approaches such as shallow fusion and rescoring can improve the recognition accuracy of CTC-based ASR by taking advantage of the knowledge in text corpora. However, they significantly slow down the inference of CTC. In this study, we propose to distill the knowledge of BERT for CTC-based ASR, extending our previous study for attention-based ASR. CTC-based ASR learns the knowledge of BERT during training and does not use BERT during testing, which maintains the fast inference of CTC. Different from attention-based models, CTC-based models make frame-level predictions, so they need to be aligned with token-level predictions of BERT for distillation. We propose to obtain alignments by calculating the most plausible CTC paths. Experimental evaluations on the Corpus of Spontaneous Japanese (CSJ) and TED-LIUM2 show that our method improves the performance of CTC-based ASR without the cost of inference speed.

</details>

### [Towards Deep Learning-aided Wireless Channel Estimation and Channel State Information Feedback for 6G](2209.01724.md)
**Wonjun Kim, Yongjun Ahn, Jinhong Kim, Byonghyo Shim** · 2022-09-05

<details>
<summary>Abstract</summary>

Deep learning (DL), a branch of artificial intelligence (AI) techniques, has shown great promise in various disciplines such as image classification and segmentation, speech recognition, language translation, among others. This remarkable success of DL has stimulated increasing interest in applying this paradigm to wireless channel estimation in recent years. Since DL principles are inductive in nature and distinct from the conventional rule-based algorithms, when one tries to use DL technique to the channel estimation, one might easily get stuck and confused by so many knobs to control and small details to be aware of. The primary purpose of this paper is to discuss key issues and possible solutions in DL-based wireless channel estimation and channel state information (CSI) feedback including the DL model selection, training data acquisition, and neural network design for 6G. Specifically, we present several case studies together with the numerical experiments to demonstrate the effectiveness of the DL-based wireless channel estimation framework.

</details>

### [A Review of Sparse Expert Models in Deep Learning](2209.01667.md)
**William Fedus, Jeff Dean, Barret Zoph** · 2022-09-04

<details>
<summary>Abstract</summary>

Sparse expert models are a thirty-year old concept re-emerging as a popular architecture in deep learning. This class of architecture encompasses Mixture-of-Experts, Switch Transformers, Routing Networks, BASE layers, and others, all with the unifying idea that each example is acted on by a subset of the parameters. By doing so, the degree of sparsity decouples the parameter count from the compute per example allowing for extremely large, but efficient models. The resulting models have demonstrated significant improvements across diverse domains such as natural language processing, computer vision, and speech recognition. We review the concept of sparse expert models, provide a basic description of the common algorithms, contextualize the advances in the deep learning era, and conclude by highlighting areas for future work.

</details>

### [Improving Contextual Recognition of Rare Words with an Alternate Spelling Prediction Model](2209.01250.md)
**Jennifer Drexler Fox, Natalie Delworth** · 2022-09-02

<details>
<summary>Abstract</summary>

Contextual ASR, which takes a list of bias terms as input along with audio, has drawn recent interest as ASR use becomes more widespread. We are releasing contextual biasing lists to accompany the Earnings21 dataset, creating a public benchmark for this task. We present baseline results on this benchmark using a pretrained end-to-end ASR model from the WeNet toolkit. We show results for shallow fusion contextual biasing applied to two different decoding algorithms. Our baseline results confirm observations that end-to-end models struggle in particular with words that are rarely or never seen during training, and that existing shallow fusion techniques do not adequately address this problem. We propose an alternate spelling prediction model that improves recall of rare words by 34.7% relative and of out-of-vocabulary words by 97.2% relative, compared to contextual biasing without alternate spellings. This model is conceptually similar to ones used in prior work, but is simpler to implement as it does not rely on either a pronunciation dictionary or an existing text-to-speech system.

</details>

### [Attention Enhanced Citrinet for Speech Recognition](2209.00261.md)
**Xianchao Wu** · 2022-09-01

<details>
<summary>Abstract</summary>

Citrinet is an end-to-end convolutional Connectionist Temporal Classification (CTC) based automatic speech recognition (ASR) model. To capture local and global contextual information, 1D time-channel separable convolutions combined with sub-word encoding and squeeze-and-excitation (SE) are used in Citrinet, making the whole architecture to be as deep as including 23 blocks with 235 convolution layers and 46 linear layers. This pure convolutional and deep architecture makes Critrinet relatively slow at convergence. In this paper, we propose to introduce multi-head attentions together with feed-forward networks in the convolution module in Citrinet blocks while keeping the SE module and residual module unchanged. For speeding up, we remove 8 convolution layers in each attention-enhanced Citrinet block and reduce 23 blocks to 13. Experiments on the Japanese CSJ-500h and Magic-1600h dataset show that the attention-enhanced Citrinet with less layers and blocks and converges faster with lower character error rates than (1) Citrinet with 80\% training time and (2) Conformer with 40\% training time and 29.8\% model size.

</details>

### [Deep Sparse Conformer for Speech Recognition](2209.00260.md)
**Xianchao Wu** · 2022-09-01

<details>
<summary>Abstract</summary>

Conformer has achieved impressive results in Automatic Speech Recognition (ASR) by leveraging transformer's capturing of content-based global interactions and convolutional neural network's exploiting of local features. In Conformer, two macaron-like feed-forward layers with half-step residual connections sandwich the multi-head self-attention and convolution modules followed by a post layer normalization. We improve Conformer's long-sequence representation ability in two directions, \emph{sparser} and \emph{deeper}. We adapt a sparse self-attention mechanism with $\mathcal{O}(L\text{log}L)$ in time complexity and memory usage. A deep normalization strategy is utilized when performing residual connections to ensure our training of hundred-level Conformer blocks. On the Japanese CSJ-500h dataset, this deep sparse Conformer achieves respectively CERs of 5.52\%, 4.03\% and 4.50\% on the three evaluation sets and 4.16\%, 2.84\% and 3.20\% when ensembling five deep sparse Conformer variants from 12 to 16, 17, 50, and finally 100 encoder layers.

</details>

### [RecLight: A Recurrent Neural Network Accelerator with Integrated Silicon Photonics](2209.00084.md)
**Febin Sunny, Mahdi Nikdast, Sudeep Pasricha** · 2022-08-31

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are used in applications that learn dependencies in data sequences, such as speech recognition, human activity recognition, and anomaly detection. In recent years, newer RNN variants, such as GRUs and LSTMs, have been used for implementing these applications. As many of these applications are employed in real-time scenarios, accelerating RNN/LSTM/GRU inference is crucial. In this paper, we propose a novel photonic hardware accelerator called RecLight for accelerating simple RNNs, GRUs, and LSTMs. Simulation results indicate that RecLight achieves 37x lower energy-per-bit and 10% better throughput compared to the state-of-the-art.

</details>

### [A Language Agnostic Multilingual Streaming On-Device ASR System](2208.13916.md)
**Bo Li, Tara N. Sainath, Ruoming Pang, Shuo-yiin Chang et al.** · 2022-08-29

<details>
<summary>Abstract</summary>

On-device end-to-end (E2E) models have shown improvements over a conventional model on English Voice Search tasks in both quality and latency. E2E models have also shown promising results for multilingual automatic speech recognition (ASR). In this paper, we extend our previous capacity solution to streaming applications and present a streaming multilingual E2E ASR system that runs fully on device with comparable quality and latency to individual monolingual models. To achieve that, we propose an Encoder Endpointer model and an End-of-Utterance (EOU) Joint Layer for a better quality and latency trade-off. Our system is built in a language agnostic manner allowing it to natively support intersentential code switching in real time. To address the feasibility concerns on large models, we conducted on-device profiling and replaced the time consuming LSTM decoder with the recently developed Embedding decoder. With these changes, we managed to run such a system on a mobile device in less than real time.

</details>

### [Turn-Taking Prediction for Natural Conversational Speech](2208.13321.md)
**Shuo-yiin Chang, Bo Li, Tara N. Sainath, Chao Zhang et al.** · 2022-08-29

<details>
<summary>Abstract</summary>

While a streaming voice assistant system has been used in many applications, this system typically focuses on unnatural, one-shot interactions assuming input from a single voice query without hesitation or disfluency. However, a common conversational utterance often involves multiple queries with turn-taking, in addition to disfluencies. These disfluencies include pausing to think, hesitations, word lengthening, filled pauses and repeated phrases. This makes doing speech recognition with conversational speech, including one with multiple queries, a challenging task. To better model the conversational interaction, it is critical to discriminate disfluencies and end of query in order to allow the user to hold the floor for disfluencies while having the system respond as quickly as possible when the user has finished speaking. In this paper, we present a turntaking predictor built on top of the end-to-end (E2E) speech recognizer. Our best system is obtained by jointly optimizing for ASR task and detecting when the user is paused to think or finished speaking. The proposed approach demonstrates over 97% recall rate and 85% precision rate on predicting true turn-taking with only 100 ms latency on a test set designed with 4 types of disfluencies inserted in conversational utterances.

</details>

### [Bayesian Neural Network Language Modeling for Speech Recognition](2208.13259.md)
**Boyang Xue, Shoukang Hu, Junhao Xu, Mengzhe Geng et al.** · 2022-08-28

<details>
<summary>Abstract</summary>

State-of-the-art neural network language models (NNLMs) represented by long short term memory recurrent neural networks (LSTM-RNNs) and Transformers are becoming highly complex. They are prone to overfitting and poor generalization when given limited training data. To this end, an overarching full Bayesian learning framework encompassing three methods is proposed in this paper to account for the underlying uncertainty in LSTM-RNN and Transformer LMs. The uncertainty over their model parameters, choice of neural activations and hidden output representations are modeled using Bayesian, Gaussian Process and variational LSTM-RNN or Transformer LMs respectively. Efficient inference approaches were used to automatically select the optimal network internal components to be Bayesian learned using neural architecture search. A minimal number of Monte Carlo parameter samples as low as one was also used. These allow the computational costs incurred in Bayesian NNLM training and evaluation to be minimized. Experiments are conducted on two tasks: AMI meeting transcription and Oxford-BBC LipReading Sentences 2 (LRS2) overlapped speech recognition using state-of-the-art LF-MMI trained factored TDNN systems featuring data augmentation, speaker adaptation and audio-visual multi-channel beamforming for overlapped speech. Consistent performance improvements over the baseline LSTM-RNN and Transformer LMs with point estimated model parameters and drop-out regularization were obtained across both tasks in terms of perplexity and word error rate (WER). In particular, on the LRS2 data, statistically significant WER reductions up to 1.3% and 1.2% absolute (12.1% and 11.3% relative) were obtained over the baseline LSTM-RNN and Transformer LMs respectively after model combination between Bayesian NNLMs and their respective baselines.

</details>

### [Effectiveness of Mining Audio and Text Pairs from Public Data for Improving ASR Systems for Low-Resource Languages](2208.12666.md)
**Kaushal Santosh Bhogale, Abhigyan Raman, Tahir Javed, Sumanth Doddapaneni et al.** · 2022-08-26

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have become the default choice for state-of-the-art speech recognition systems. Such models are trained on large amounts of labelled data, which are often not available for low-resource languages. Techniques such as self-supervised learning and transfer learning hold promise, but have not yet been effective in training accurate models. On the other hand, collecting labelled datasets on a diverse set of domains and speakers is very expensive. In this work, we demonstrate an inexpensive and effective alternative to these approaches by ``mining'' text and audio pairs for Indian languages from public sources, specifically from the public archives of All India Radio. As a key component, we adapt the Needleman-Wunsch algorithm to align sentences with corresponding audio segments given a long audio and a PDF of its transcript, while being robust to errors due to OCR, extraneous text, and non-transcribed speech. We thus create Shrutilipi, a dataset which contains over 6,400 hours of labelled audio across 12 Indian languages totalling to 4.95M sentences. On average, Shrutilipi results in a 2.3x increase over publicly available labelled data. We establish the quality of Shrutilipi with 21 human evaluators across the 12 languages. We also establish the diversity of Shrutilipi in terms of represented regions, speakers, and mentioned named entities. Significantly, we show that adding Shrutilipi to the training set of Wav2Vec models leads to an average decrease in WER of 5.8\% for 7 languages on the IndicSUPERB benchmark. For Hindi, which has the most benchmarks (7), the average WER falls from 18.8% to 13.5%. This improvement extends to efficient models: We show a 2.3% drop in WER for a Conformer model (10x smaller than Wav2Vec). Finally, we demonstrate the diversity of Shrutilipi by showing that the model trained with it is more robust to noisy input.

</details>

### [Convolutional Neural Network (CNN) to reduce construction loss in JPEG compression caused by Discrete Fourier Transform (DFT)](2209.03475.md)
**Suman Kunwar** · 2022-08-26

<details>
<summary>Abstract</summary>

In recent decades, digital image processing has gained enormous popularity. Consequently, a number of data compression strategies have been put forth, with the goal of minimizing the amount of information required to represent images. Among them, JPEG compression is one of the most popular methods that has been widely applied in multimedia and digital applications. The periodic nature of DFT makes it impossible to meet the periodic condition of an image's opposing edges without producing severe artifacts, which lowers the image's perceptual visual quality. On the other hand, deep learning has recently achieved outstanding results for applications like speech recognition, image reduction, and natural language processing. Convolutional Neural Networks (CNN) have received more attention than most other types of deep neural networks. The use of convolution in feature extraction results in a less redundant feature map and a smaller dataset, both of which are crucial for image compression. In this work, an effective image compression method is purposed using autoencoders. The study's findings revealed a number of important trends that suggested better reconstruction along with good compression can be achieved using autoencoders.

</details>

### [Kencorpus: A Kenyan Language Corpus of Swahili, Dholuo and Luhya for Natural Language Processing Tasks](2208.12081.md)
**Barack Wanjawa, Lilian Wanzare, Florence Indede, Owen McOnyango et al.** · 2022-08-25

<details>
<summary>Abstract</summary>

Indigenous African languages are categorized as under-served in Natural Language Processing. They therefore experience poor digital inclusivity and information access. The processing challenge with such languages has been how to use machine learning and deep learning models without the requisite data. The Kencorpus project intends to bridge this gap by collecting and storing text and speech data that is good enough for data-driven solutions in applications such as machine translation, question answering and transcription in multilingual communities. The Kencorpus dataset is a text and speech corpus for three languages predominantly spoken in Kenya: Swahili, Dholuo and Luhya. Data collection was done by researchers from communities, schools, media, and publishers. The Kencorpus' dataset has a collection of 5,594 items - 4,442 texts (5.6M words) and 1,152 speech files (177hrs). Based on this data, Part of Speech tagging sets for Dholuo and Luhya (50,000 and 93,000 words respectively) were developed. We developed 7,537 Question-Answer pairs for Swahili and created a text translation set of 13,400 sentences from Dholuo and Luhya into Swahili. The datasets are useful for downstream machine learning tasks such as model training and translation. We also developed two proof of concept systems: for Kiswahili speech-to-text and machine learning system for Question Answering task, with results of 18.87% word error rate and 80% Exact Match (EM) respectively. These initial results give great promise to the usability of Kencorpus to the machine learning community. Kencorpus is one of few public domain corpora for these three low resource languages and forms a basis of learning and sharing experiences for similar works especially for low resource languages.

</details>

### [Low-Level Physiological Implications of End-to-End Learning of Speech Recognition](2208.11700.md)
**Louise Coppieters de Gibson, Philip N. Garner** · 2022-08-22

<details>
<summary>Abstract</summary>

Current speech recognition architectures perform very well from the point of view of machine learning, hence user interaction. This suggests that they are emulating the human biological system well. We investigate whether the inference can be inverted to provide insights into that biological system; in particular the hearing mechanism. Using SincNet, we confirm that end-to-end systems do learn well known filterbank structures. However, we also show that wider band-width filters are important in the learned structure. Whilst some benefits can be gained by initialising both narrow and wide-band filters, physiological constraints suggest that such filters arise in mid-brain rather than the cochlea. We show that standard machine learning architectures must be modified to allow this process to be emulated neurally.

</details>

### [DualVoice: Speech Interaction that Discriminates between Normal and Whispered Voice Input](2208.10499.md)
**Jun Rekimoto** · 2022-08-22

<details>
<summary>Abstract</summary>

Interactions based on automatic speech recognition (ASR) have become widely used, with speech input being increasingly utilized to create documents. However, as there is no easy way to distinguish between commands being issued and text required to be input in speech, misrecognitions are difficult to identify and correct, meaning that documents need to be manually edited and corrected. The input of symbols and commands is also challenging because these may be misrecognized as text letters. To address these problems, this study proposes a speech interaction method called DualVoice, by which commands can be input in a whispered voice and letters in a normal voice. The proposed method does not require any specialized hardware other than a regular microphone, enabling a complete hands-free interaction. The method can be used in a wide range of situations where speech recognition is already available, ranging from text input to mobile/wearable computing. Two neural networks were designed in this study, one for discriminating normal speech from whispered speech, and the second for recognizing whisper speech. A prototype of a text input system was then developed to show how normal and whispered voice can be used in speech text input. Other potential applications using DualVoice are also discussed.

</details>

### [Analyzing Robustness of End-to-End Neural Models for Automatic Speech Recognition](2208.08509.md)
**Goutham Rajendran, Wei Zou** · 2022-08-17

<details>
<summary>Abstract</summary>

We investigate robustness properties of pre-trained neural models for automatic speech recognition. Real life data in machine learning is usually very noisy and almost never clean, which can be attributed to various factors depending on the domain, e.g. outliers, random noise and adversarial noise. Therefore, the models we develop for various tasks should be robust to such kinds of noisy data, which led to the thriving field of robust machine learning. We consider this important issue in the setting of automatic speech recognition. With the increasing popularity of pre-trained models, it's an important question to analyze and understand the robustness of such models to noise. In this work, we perform a robustness analysis of the pre-trained neural models wav2vec2, HuBERT and DistilHuBERT on the LibriSpeech and TIMIT datasets. We use different kinds of noising mechanisms and measure the model performances as quantified by the inference time and the standard Word Error Rate metric. We also do an in-depth layer-wise analysis of the wav2vec2 model when injecting noise in between layers, enabling us to predict at a high level what each layer learns. Finally for this model, we visualize the propagation of errors across the layers and compare how it behaves on clean versus noisy data. Our experiments conform the predictions of Pasad et al. [2021] and also raise interesting directions for future work.

</details>

### [Uconv-Conformer: High Reduction of Input Sequence Length for End-to-End Speech Recognition](2208.07657.md)
**Andrei Andrusenko, Rauf Nasretdinov, Aleksei Romanenko** · 2022-08-16

<details>
<summary>Abstract</summary>

Optimization of modern ASR architectures is among the highest priority tasks since it saves many computational resources for model training and inference. The work proposes a new Uconv-Conformer architecture based on the standard Conformer model. It consistently reduces the input sequence length by 16 times, which results in speeding up the work of the intermediate layers. To solve the convergence issue connected with such a significant reduction of the time dimension, we use upsampling blocks like in the U-Net architecture to ensure the correct CTC loss calculation and stabilize network training. The Uconv-Conformer architecture appears to be not only faster in terms of training and inference speed but also shows better WER compared to the baseline Conformer. Our best Uconv-Conformer model shows 47.8% and 23.5% inference acceleration on the CPU and GPU, respectively. Relative WER reduction is 7.3% and 9.2% on LibriSpeech test_clean and test_other respectively.

</details>

### [Comparison and Analysis of New Curriculum Criteria for End-to-End ASR](2208.05782.md)
**Georgios Karakasidis, Tamás Grósz, Mikko Kurimo** · 2022-08-10

<details>
<summary>Abstract</summary>

It is common knowledge that the quantity and quality of the training data play a significant role in the creation of a good machine learning model. In this paper, we take it one step further and demonstrate that the way the training examples are arranged is also of crucial importance. Curriculum Learning is built on the observation that organized and structured assimilation of knowledge has the ability to enable faster training and better comprehension. When humans learn to speak, they first try to utter basic phones and then gradually move towards more complex structures such as words and sentences. This methodology is known as Curriculum Learning, and we employ it in the context of Automatic Speech Recognition. We hypothesize that end-to-end models can achieve better performance when provided with an organized training set consisting of examples that exhibit an increasing level of difficulty (i.e. a curriculum). To impose structure on the training set and to define the notion of an easy example, we explored multiple scoring functions that either use feedback from an external neural network or incorporate feedback from the model itself. Empirical results show that with different curriculums we can balance the training times and the network's performance.

</details>

### [Thai Wav2Vec2.0 with CommonVoice V8](2208.04799.md)
**Wannaphong Phatthiyaphaibun, Chompakorn Chaksangchaichot, Peerat Limkonchotiwat, Ekapol Chuangsuwanich et al.** · 2022-08-09

<details>
<summary>Abstract</summary>

Recently, Automatic Speech Recognition (ASR), a system that converts audio into text, has caught a lot of attention in the machine learning community. Thus, a lot of publicly available models were released in HuggingFace. However, most of these ASR models are available in English; only a minority of the models are available in Thai. Additionally, most of the Thai ASR models are closed-sourced, and the performance of existing open-sourced models lacks robustness. To address this problem, we train a new ASR model on a pre-trained XLSR-Wav2Vec model with the Thai CommonVoice corpus V8 and train a trigram language model to boost the performance of our ASR model. We hope that our models will be beneficial to individuals and the ASR community in Thailand.

</details>

### [ASR Error Correction with Constrained Decoding on Operation Prediction](2208.04641.md)
**Jingyuan Yang, Rongjun Li, Wei Peng** · 2022-08-09

<details>
<summary>Abstract</summary>

Error correction techniques remain effective to refine outputs from automatic speech recognition (ASR) models. Existing end-to-end error correction methods based on an encoder-decoder architecture process all tokens in the decoding phase, creating undesirable latency. In this paper, we propose an ASR error correction method utilizing the predictions of correction operations. More specifically, we construct a predictor between the encoder and the decoder to learn if a token should be kept ("K"), deleted ("D"), or changed ("C") to restrict decoding to only part of the input sequence embeddings (the "C" tokens) for fast inference. Experiments on three public datasets demonstrate the effectiveness of the proposed approach in reducing the latency of the decoding process in ASR correction. It enhances the inference speed by at least three times (3.4 and 5.7 times) while maintaining the same level of accuracy (with WER reductions of 0.53% and 1.69% respectively) for our two proposed models compared to a solid encoder-decoder baseline. In the meantime, we produce and release a benchmark dataset contributing to the ASR error correction community to foster research along this line.

</details>

### [Large vocabulary speech recognition for languages of Africa: multilingual modeling and self-supervised learning](2208.03067.md)
**Sandy Ritchie, You-Chi Cheng, Mingqing Chen, Rajiv Mathews et al.** · 2022-08-05

<details>
<summary>Abstract</summary>

Almost none of the 2,000+ languages spoken in Africa have widely available automatic speech recognition systems, and the required data is also only available for a few languages. We have experimented with two techniques which may provide pathways to large vocabulary speech recognition for African languages: multilingual modeling and self-supervised learning. We gathered available open source data and collected data for 15 languages, and trained experimental models using these techniques. Our results show that pooling the small amounts of data available in multilingual end-to-end models, and pre-training on unsupervised data can help improve speech recognition quality for many African languages.

</details>

### [Model Blending for Text Classification](2208.02819.md)
**Ramit Pahwa** · 2022-08-05

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have proven successful in a wide variety of applications such as speech recognition and synthesis, computer vision, machine translation, and game playing, to name but a few. However, existing deep neural network models are computationally expensive and memory intensive, hindering their deployment in devices with low memory resources or in applications with strict latency requirements. Therefore, a natural thought is to perform model compression and acceleration in deep networks without significantly decreasing the model performance, which is what we call reducing the complexity. In the following work, we try reducing the complexity of state of the art LSTM models for natural language tasks such as text classification, by distilling their knowledge to CNN based models, thus reducing the inference time(or latency) during testing.

</details>

### [Adversarial Attacks on ASR Systems: An Overview](2208.02250.md)
**Xiao Zhang, Hao Tan, Xuan Huang, Denghui Zhang et al.** · 2022-08-03

<details>
<summary>Abstract</summary>

With the development of hardware and algorithms, ASR(Automatic Speech Recognition) systems evolve a lot. As The models get simpler, the difficulty of development and deployment become easier, ASR systems are getting closer to our life. On the one hand, we often use APPs or APIs of ASR to generate subtitles and record meetings. On the other hand, smart speaker and self-driving car rely on ASR systems to control AIoT devices. In past few years, there are a lot of works on adversarial examples attacks against ASR systems. By adding a small perturbation to the waveforms, the recognition results make a big difference. In this paper, we describe the development of ASR system, different assumptions of attacks, and how to evaluate these attacks. Next, we introduce the current works on adversarial examples attacks from two attack assumptions: white-box attack and black-box attack. Different from other surveys, we pay more attention to which layer they perturb waveforms in ASR system, the relationship between these attacks, and their implementation methods. We focus on the effect of their works.

</details>

### [Multiclass ASMA vs Targeted PGD Attack in Image Segmentation](2208.01844.md)
**Johnson Vo, Jiabao Xie, Sahil Patel** · 2022-08-03

<details>
<summary>Abstract</summary>

Deep learning networks have demonstrated high performance in a large variety of applications, such as image classification, speech recognition, and natural language processing. However, there exists a major vulnerability exploited by the use of adversarial attacks. An adversarial attack imputes images by altering the input image very slightly, making it nearly undetectable to the naked eye, but results in a very different classification by the network. This paper explores the projected gradient descent (PGD) attack and the Adaptive Mask Segmentation Attack (ASMA) on the image segmentation DeepLabV3 model using two types of architectures: MobileNetV3 and ResNet50, It was found that PGD was very consistent in changing the segmentation to be its target while the generalization of ASMA to a multiclass target was not as effective. The existence of such attack however puts all of image classification deep learning networks in danger of exploitation.

</details>

### [VQ-T: RNN Transducers using Vector-Quantized Prediction Network States](2208.01818.md)
**Jiatong Shi, George Saon, David Haws, Shinji Watanabe et al.** · 2022-08-03

<details>
<summary>Abstract</summary>

Beam search, which is the dominant ASR decoding algorithm for end-to-end models, generates tree-structured hypotheses. However, recent studies have shown that decoding with hypothesis merging can achieve a more efficient search with comparable or better performance. But, the full context in recurrent networks is not compatible with hypothesis merging. We propose to use vector-quantized long short-term memory units (VQ-LSTM) in the prediction network of RNN transducers. By training the discrete representation jointly with the ASR network, hypotheses can be actively merged for lattice generation. Our experiments on the Switchboard corpus show that the proposed VQ RNN transducers improve ASR performance over transducers with regular prediction networks while also producing denser lattices with a very low oracle word error rate (WER) for the same beam size. Additional language model rescoring experiments also demonstrate the effectiveness of the proposed lattice generation scheme.

</details>

### [Thutmose Tagger: Single-pass neural model for Inverse Text Normalization](2208.00064.md)
**Alexandra Antonova, Evelina Bakhturina, Boris Ginsburg** · 2022-07-29

<details>
<summary>Abstract</summary>

Inverse text normalization (ITN) is an essential post-processing step in automatic speech recognition (ASR). It converts numbers, dates, abbreviations, and other semiotic classes from the spoken form generated by ASR to their written forms. One can consider ITN as a Machine Translation task and use neural sequence-to-sequence models to solve it. Unfortunately, such neural models are prone to hallucinations that could lead to unacceptable errors. To mitigate this issue, we propose a single-pass token classifier model that regards ITN as a tagging task. The model assigns a replacement fragment to every input token or marks it for deletion or copying without changes. We present a dataset preparation method based on the granular alignment of ITN examples. The proposed model is less prone to hallucination errors. The model is trained on the Google Text Normalization dataset and achieves state-of-the-art sentence accuracy on both English and Russian test sets. One-to-one correspondence between tags and input words improves the interpretability of the model's predictions, simplifies debugging, and allows for post-processing corrections. The model is simpler than sequence-to-sequence models and easier to optimize in production settings. The model and the code to prepare the dataset is published as part of NeMo project.

</details>

### [Multiple-hypothesis RNN-T Loss for Unsupervised Fine-tuning and Self-training of Neural Transducer](2207.14736.md)
**Cong-Thanh Do, Mohan Li, Rama Doddipatla** · 2022-07-29

<details>
<summary>Abstract</summary>

This paper proposes a new approach to perform unsupervised fine-tuning and self-training using unlabeled speech data for recurrent neural network (RNN)-Transducer (RNN-T) end-to-end (E2E) automatic speech recognition (ASR) systems. Conventional systems perform fine-tuning/self-training using ASR hypothesis as the targets when using unlabeled audio data and are susceptible to the ASR performance of the base model. Here in order to alleviate the influence of ASR errors while using unlabeled data, we propose a multiple-hypothesis RNN-T loss that incorporates multiple ASR 1-best hypotheses into the loss function. For the fine-tuning task, ASR experiments on Librispeech show that the multiple-hypothesis approach achieves a relative reduction of 14.2% word error rate (WER) when compared to the single-hypothesis approach, on the test_other set. For the self-training task, ASR models are trained using supervised data from Wall Street Journal (WSJ), Aurora-4 along with CHiME-4 real noisy data as unlabeled data. The multiple-hypothesis approach yields a relative reduction of 3.3% WER on the CHiME-4's single-channel real noisy evaluation set when compared with the single-hypothesis approach.

</details>

### [Pronunciation-aware unique character encoding for RNN Transducer-based Mandarin speech recognition](2207.14578.md)
**Peng Shen, Xugang Lu, Hisashi Kawai** · 2022-07-29

<details>
<summary>Abstract</summary>

For Mandarin end-to-end (E2E) automatic speech recognition (ASR) tasks, compared to character-based modeling units, pronunciation-based modeling units could improve the sharing of modeling units in model training but meet homophone problems. In this study, we propose to use a novel pronunciation-aware unique character encoding for building E2E RNN-T-based Mandarin ASR systems. The proposed encoding is a combination of pronunciation-base syllable and character index (CI). By introducing the CI, the RNN-T model can overcome the homophone problem while utilizing the pronunciation information for extracting modeling units. With the proposed encoding, the model outputs can be converted into the final recognition result through a one-to-one mapping. We conducted experiments on Aishell and MagicData datasets, and the experimental results showed the effectiveness of the proposed method.

</details>

### [Extending RNN-T-based speech recognition systems with emotion and language classification](2207.13965.md)
**Zvi Kons, Hagai Aronowitz, Edmilson Morais, Matheus Damasceno et al.** · 2022-07-28

<details>
<summary>Abstract</summary>

Speech transcription, emotion recognition, and language identification are usually considered to be three different tasks. Each one requires a different model with a different architecture and training process. We propose using a recurrent neural network transducer (RNN-T)-based speech-to-text (STT) system as a common component that can be used for emotion recognition and language identification as well as for speech recognition. Our work extends the STT system for emotion classification through minimal changes, and shows successful results on the IEMOCAP and MELD datasets. In addition, we demonstrate that by adding a lightweight component to the RNN-T module, it can also be used for language identification. In our evaluations, this new classifier demonstrates state-of-the-art accuracy for the NIST-LRE-07 dataset.

</details>

### [Knowledge-driven Subword Grammar Modeling for Automatic Speech Recognition in Tamil and Kannada](2207.13333.md)
**Madhavaraj A, Bharathi Pilar, Ramakrishnan A G** · 2022-07-27

<details>
<summary>Abstract</summary>

In this paper, we present specially designed automatic speech recognition (ASR) systems for the highly agglutinative and inflective languages of Tamil and Kannada that can recognize unlimited vocabulary of words. We use subwords as the basic lexical units for recognition and construct subword grammar weighted finite state transducer (SG-WFST) graphs for word segmentation that captures most of the complex word formation rules of the languages. We have identified the following category of words (i) verbs, (ii) nouns, (ii) pronouns, and (iv) numbers. The prefix, infix and suffix lists of subwords are created for each of these categories and are used to design the SG-WFST graphs. We also present a heuristic segmentation algorithm that can even segment exceptional words that do not follow the rules encapsulated in the SG-WFST graph. Most of the data-driven subword dictionary creation algorithms are computation driven, and hence do not guarantee morpheme-like units and so we have used the linguistic knowledge of the languages and manually created the subword dictionaries and the graphs. Finally, we train a deep neural network acoustic model and combine it with the pronunciation lexicon of the subword dictionary and the SG-WFST graph to build the subword-ASR systems. Since the subword-ASR produces subword sequences as output for a given test speech, we post-process its output to get the final word sequence, so that the actual number of words that can be recognized is much higher. Upon experimenting the subword-ASR system with the IISc-MILE Tamil and Kannada ASR corpora, we observe an absolute word error rate reduction of 12.39% and 13.56% over the baseline word-based ASR systems for Tamil and Kannada, respectively.

</details>

### [Subword Dictionary Learning and Segmentation Techniques for Automatic Speech Recognition in Tamil and Kannada](2207.13331.md)
**Madhavaraj A, Bharathi Pilar, Ramakrishnan A G** · 2022-07-27

<details>
<summary>Abstract</summary>

We present automatic speech recognition (ASR) systems for Tamil and Kannada based on subword modeling to effectively handle unlimited vocabulary due to the highly agglutinative nature of the languages. We explore byte pair encoding (BPE), and proposed a variant of this algorithm named extended-BPE, and Morfessor tool to segment each word as subwords. We have effectively incorporated maximum likelihood (ML) and Viterbi estimation techniques with weighted finite state transducers (WFST) framework in these algorithms to learn the subword dictionary from a large text corpus. Using the learnt subword dictionary, the words in training data transcriptions are segmented to subwords and we train deep neural network ASR systems which recognize subword sequence for any given test speech utterance. The output subword sequence is then post-processed using deterministic rules to get the final word sequence such that the actual number of words that can be recognized is much larger. For Tamil ASR, We use 152 hours of data for training and 65 hours for testing, whereas for Kannada ASR, we use 275 hours for training and 72 hours for testing. Upon experimenting with different combination of segmentation and estimation techniques, we find that the word error rate (WER) reduces drastically when compared to the baseline word-level ASR, achieving a maximum absolute WER reduction of 6.24% and 6.63% for Tamil and Kannada respectively.

</details>

### [SoundChoice: Grapheme-to-Phoneme Models with Semantic Disambiguation](2207.13703.md)
**Artem Ploujnikov, Mirco Ravanelli** · 2022-07-27

<details>
<summary>Abstract</summary>

End-to-end speech synthesis models directly convert the input characters into an audio representation (e.g., spectrograms). Despite their impressive performance, such models have difficulty disambiguating the pronunciations of identically spelled words. To mitigate this issue, a separate Grapheme-to-Phoneme (G2P) model can be employed to convert the characters into phonemes before synthesizing the audio. This paper proposes SoundChoice, a novel G2P architecture that processes entire sentences rather than operating at the word level. The proposed architecture takes advantage of a weighted homograph loss (that improves disambiguation), exploits curriculum learning (that gradually switches from word-level to sentence-level G2P), and integrates word embeddings from BERT (for further performance improvement). Moreover, the model inherits the best practices in speech recognition, including multi-task learning with Connectionist Temporal Classification (CTC) and beam search with an embedded language model. As a result, SoundChoice achieves a Phoneme Error Rate (PER) of 2.65% on whole-sentence transcription using data from LibriSpeech and Wikipedia. Index Terms grapheme-to-phoneme, speech synthesis, text-tospeech, phonetics, pronunciation, disambiguation.

</details>

### [Perception-Aware Attack: Creating Adversarial Music via Reverse-Engineering Human Perception](2207.13192.md)
**Rui Duan, Zhe Qu, Shangqing Zhao, Leah Ding et al.** · 2022-07-26

<details>
<summary>Abstract</summary>

Recently, adversarial machine learning attacks have posed serious security threats against practical audio signal classification systems, including speech recognition, speaker recognition, and music copyright detection. Previous studies have mainly focused on ensuring the effectiveness of attacking an audio signal classifier via creating a small noise-like perturbation on the original signal. It is still unclear if an attacker is able to create audio signal perturbations that can be well perceived by human beings in addition to its attack effectiveness. This is particularly important for music signals as they are carefully crafted with human-enjoyable audio characteristics. In this work, we formulate the adversarial attack against music signals as a new perception-aware attack framework, which integrates human study into adversarial attack design. Specifically, we conduct a human study to quantify the human perception with respect to a change of a music signal. We invite human participants to rate their perceived deviation based on pairs of original and perturbed music signals, and reverse-engineer the human perception process by regression analysis to predict the human-perceived deviation given a perturbed signal. The perception-aware attack is then formulated as an optimization problem that finds an optimal perturbation signal to minimize the prediction of perceived deviation from the regressed human perception model. We use the perception-aware framework to design a realistic adversarial music attack against YouTube's copyright detector. Experiments show that the perception-aware attack produces adversarial music with significantly better perceptual quality than prior work.

</details>

### [Learning a Dual-Mode Speech Recognition Model via Self-Pruning](2207.11906.md)
**Chunxi Liu, Yuan Shangguan, Haichuan Yang, Yangyang Shi et al.** · 2022-07-25

<details>
<summary>Abstract</summary>

There is growing interest in unifying the streaming and full-context automatic speech recognition (ASR) networks into a single end-to-end ASR model to simplify the model training and deployment for both use cases. While in real-world ASR applications, the streaming ASR models typically operate under more storage and computational constraints - e.g., on embedded devices - than any server-side full-context models. Motivated by the recent progress in Omni-sparsity supernet training, where multiple subnetworks are jointly optimized in one single model, this work aims to jointly learn a compact sparse on-device streaming ASR model, and a large dense server non-streaming model, in a single supernet. Next, we present that, performing supernet training on both wav2vec 2.0 self-supervised learning and supervised ASR fine-tuning can not only substantially improve the large non-streaming model as shown in prior works, and also be able to improve the compact sparse streaming model.

</details>

### [Automatic Speech Recognition Using Limited Vocabulary: A Survey](s2:eae8bb1f3b9ec32e62c670c9f2a95c7815a2beb5.md)
**J. Ebongue, D. Tala, B. Yenke, M. Atemkeng** · 2022-07-25

<details>
<summary>Abstract</summary>

ABSTRACT Automatic Speech Recognition (ASR) is an active field of research due to its large number of applications and the proliferation of interfaces or computing devices that can support speech processing. However, the bulk of applications are based on well-resourced languages that overshadow under-resourced ones. Yet, ASR represents an undeniable means to promote such languages, especially when designing human-to-human or human-to-machine systems involving illiterate people. An approach to design an ASR system targeting under-resourced languages is to start with a limited vocabulary. ASR using a limited vocabulary is a subset of the speech recognition problem that focuses on the recognition of a small number of words or sentences. This paper aims to provide a comprehensive view of mechanisms behind ASR systems as well as techniques, tools, projects, recent contributions, and possible future directions in ASR using a limited vocabulary. This work consequently provides a way forward when designing an ASR system using limited vocabulary. Although an emphasis is put on limited vocabulary, most of the tools and techniques reported in this survey can be applied to ASR systems in general. AbbreviationsACC: Accuracy; AM: Acoustic Model; ASR: Automatic Speech Recognition; BD-4SK-ASR: Basic Dataset for Sorani Kurdish Automatic Speech Recognition; CER: Character Error Rate; CMU: Carnegie Mellon University; CNN: Convolutional Neural Network; CNTK: CogNitive ToolKit; CUED: Cambridge University Engineering Department; DCT:Discrete Cosine Transformation; DL: Deep Learning; DNN: Deep Neural Network; DRL: Deep Reinforcement Learning; DWT: Discrete Wavelet Transform; FFT: Fast Fourier Transformation; GMM: Gaussian Mixture Model; HMM: Hidden Markov Model; HTK: Hidden Markov Model ToolKit; JASPER: Just Another Speech Recognizer; LDA: Linear Discriminant Analysis; LER: Letter Error Rate; LGB: Light Gradient Boosting Machine; LM:Language Model; LPC: Linear Predictive Coding; LVCSR: Large Vocabulary Continuous Speech Recognition; LVQ: Learning Vector Quantization Algorithm; MFCC: Mel-Frequency Cepstrum Coefficient; ML: Machine Learning; PCM:Pulse-Code Modulation; PPVT: Peabody Picture Vocabulary Test; RASTA: RelAtive SpecTral; RLAT: Rapid Language Adaptation Toolkit; S2ST: Speech-to-Speech Translation; SAPI: Speech Application Programming Interface; SDK: Software Development Kit; SVASR:Small Vocabulary Automatic Speech Recognition; WER: Word Error Rate

</details>

### [A Deep Dive into Deep Cluster](2207.11839.md)
**Ahmad Mustapha, Wael Khreich, Wasim Masr** · 2022-07-24

<details>
<summary>Abstract</summary>

Deep Learning has demonstrated a significant improvement against traditional machine learning approaches in different domains such as image and speech recognition. Their success on benchmark datasets is transferred to the real-world through pretrained models by practitioners. Pretraining visual models using supervised learning requires a significant amount of expensive data annotation. To tackle this limitation, DeepCluster - a simple and scalable unsupervised pretraining of visual representations - has been proposed. However, the underlying work of the model is not yet well understood. In this paper, we analyze DeepCluster internals and exhaustively evaluate the impact of various hyperparameters over a wide range of values on three different datasets. Accordingly, we propose an explanation of why the algorithm works in practice. We also show that DeepCluster convergence and performance highly depend on the interplay between the quality of the randomly initialized filters of the convolutional layer and the selected number of clusters. Furthermore, we demonstrate that continuous clustering is not critical for DeepCluster convergence. Therefore, early stopping of the clustering phase will reduce the training time and allow the algorithm to scale to large datasets. Finally, we derive plausible hyperparameter selection criteria in a semi-supervised setting.

</details>

### [Improving Mandarin Speech Recogntion with Block-augmented Transformer](2207.11697.md)
**Xiaoming Ren, Huifeng Zhu, Liuwei Wei, Minghui Wu et al.** · 2022-07-24

<details>
<summary>Abstract</summary>

Recently Convolution-augmented Transformer (Conformer) has shown promising results in Automatic Speech Recognition (ASR), outperforming the previous best published Transformer Transducer. In this work, we believe that the output information of each block in the encoder and decoder is not completely inclusive, in other words, their output information may be complementary. We study how to take advantage of the complementary information of each block in a parameter-efficient way, and it is expected that this may lead to more robust performance. Therefore we propose the Block-augmented Transformer for speech recognition, named Blockformer. We have implemented two block ensemble methods: the base Weighted Sum of the Blocks Output (Base-WSBO), and the Squeeze-and-Excitation module to Weighted Sum of the Blocks Output (SE-WSBO). Experiments have proved that the Blockformer significantly outperforms the state-of-the-art Conformer-based models on AISHELL-1, our model achieves a CER of 4.29\% without using a language model and 4.05\% with an external language model on the testset.

</details>

### [Implementation Of Tiny Machine Learning Models On Arduino 33 BLE For Gesture And Speech Recognition](2207.12866.md)
**Viswanatha V, Ramachandra A. C, Raghavendra Prasanna, Prem Chowdary Kakarla et al.** · 2022-07-23

<details>
<summary>Abstract</summary>

In this article gesture recognition and speech recognition applications are implemented on embedded systems with Tiny Machine Learning (TinyML). It features 3-axis accelerometer, 3-axis gyroscope and 3-axis magnetometer. The gesture recognition,provides an innovative approach nonverbal communication. It has wide applications in human-computer interaction and sign language. Here in the implementation of hand gesture recognition, TinyML model is trained and deployed from EdgeImpulse framework for hand gesture recognition and based on the hand movements, Arduino Nano 33 BLE device having 6-axis IMU can find out the direction of movement of hand. The Speech is a mode of communication. Speech recognition is a way by which the statements or commands of human speech is understood by the computer which reacts accordingly. The main aim of speech recognition is to achieve communication between man and machine. Here in the implementation of speech recognition, TinyML model is trained and deployed from EdgeImpulse framework for speech recognition and based on the keywords pronounced by human, Arduino Nano 33 BLE device having built-in microphone can make an RGB LED glow like red, green or blue based on keyword pronounced. The results of each application are obtained and listed in the results section and given the analysis upon the results.

</details>

### [ASR Error Detection via Audio-Transcript entailment](2207.10849.md)
**Nimshi Venkat Meripo, Sandeep Konam** · 2022-07-22

<details>
<summary>Abstract</summary>

Despite improved performances of the latest Automatic Speech Recognition (ASR) systems, transcription errors are still unavoidable. These errors can have a considerable impact in critical domains such as healthcare, when used to help with clinical documentation. Therefore, detecting ASR errors is a critical first step in preventing further error propagation to downstream applications. To this end, we propose a novel end-to-end approach for ASR error detection using audio-transcript entailment. To the best of our knowledge, we are the first to frame this problem as an end-to-end entailment task between the audio segment and its corresponding transcript segment. Our intuition is that there should be a bidirectional entailment between audio and transcript when there is no recognition error and vice versa. The proposed model utilizes an acoustic encoder and a linguistic encoder to model the speech and transcript respectively. The encoded representations of both modalities are fused to predict the entailment. Since doctor-patient conversations are used in our experiments, a particular emphasis is placed on medical terms. Our proposed model achieves classification error rates (CER) of 26.2% on all transcription errors and 23% on medical errors specifically, leading to improvements upon a strong baseline by 12% and 15.4%, respectively.

</details>

### [DNN-Free Low-Latency Adaptive Speech Enhancement Based on Frame-Online Beamforming Powered by Block-Online FastMNMF](2207.10934.md)
**Aditya Arie Nugraha, Kouhei Sekiguchi, Mathieu Fontaine, Yoshiaki Bando et al.** · 2022-07-22

<details>
<summary>Abstract</summary>

This paper describes a practical dual-process speech enhancement system that adapts environment-sensitive frame-online beamforming (front-end) with help from environment-free block-online source separation (back-end). To use minimum variance distortionless response (MVDR) beamforming, one may train a deep neural network (DNN) that estimates time-frequency masks used for computing the covariance matrices of sources (speech and noise). Backpropagation-based run-time adaptation of the DNN was proposed for dealing with the mismatched training-test conditions. Instead, one may try to directly estimate the source covariance matrices with a state-of-the-art blind source separation method called fast multichannel non-negative matrix factorization (FastMNMF). In practice, however, neither the DNN nor the FastMNMF can be updated in a frame-online manner due to its computationally-expensive iterative nature. Our DNN-free system leverages the posteriors of the latest source spectrograms given by block-online FastMNMF to derive the current source covariance matrices for frame-online beamforming. The evaluation shows that our frame-online system can quickly respond to scene changes caused by interfering speaker movements and outperformed an existing block-online system with DNN-based beamforming by 5.0 points in terms of the word error rate.

</details>

### [Bayesian Recurrent Units and the Forward-Backward Algorithm](2207.10486.md)
**Alexandre Bittar, Philip N. Garner** · 2022-07-21

<details>
<summary>Abstract</summary>

Using Bayes's theorem, we derive a unit-wise recurrence as well as a backward recursion similar to the forward-backward algorithm. The resulting Bayesian recurrent units can be integrated as recurrent neural networks within deep learning frameworks, while retaining a probabilistic interpretation from the direct correspondence with hidden Markov models. Whilst the contribution is mainly theoretical, experiments on speech recognition indicate that adding the derived units at the end of state-of-the-art recurrent architectures can improve the performance at a very low cost in terms of trainable parameters.

</details>

### [AutoDiCE: Fully Automated Distributed CNN Inference at the Edge](2207.12113.md)
**Xiaotian Guo, Andy D. Pimentel, Todor Stefanov** · 2022-07-20

<details>
<summary>Abstract</summary>

Deep Learning approaches based on Convolutional Neural Networks (CNNs) are extensively utilized and very successful in a wide range of application areas, including image classification and speech recognition. For the execution of trained CNNs, i.e. model inference, we nowadays witness a shift from the Cloud to the Edge. Unfortunately, deploying and inferring large, compute and memory intensive CNNs on edge devices is challenging because these devices typically have limited power budgets and compute/memory resources. One approach to address this challenge is to leverage all available resources across multiple edge devices to deploy and execute a large CNN by properly partitioning the CNN and running each CNN partition on a separate edge device. Although such distribution, deployment, and execution of large CNNs on multiple edge devices is a desirable and beneficial approach, there currently does not exist a design and programming framework that takes a trained CNN model, together with a CNN partitioning specification, and fully automates the CNN model splitting and deployment on multiple edge devices to facilitate distributed CNN inference at the Edge. Therefore, in this paper, we propose a novel framework, called AutoDiCE, for automated splitting of a CNN model into a set of sub-models and automated code generation for distributed and collaborative execution of these sub-models on multiple, possibly heterogeneous, edge devices, while supporting the exploitation of parallelism among and within the edge devices. Our experimental results show that AutoDiCE can deliver distributed CNN inference with reduced energy consumption and memory usage per edge device, and improved overall system throughput at the same time.

</details>

### [Transfer Learning of wav2vec 2.0 for Automatic Lyric Transcription](2207.09747.md)
**Longshen Ou, Xiangming Gu, Ye Wang** · 2022-07-20

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has progressed significantly in recent years due to the emergence of large-scale datasets and the self-supervised learning (SSL) paradigm. However, as its counterpart problem in the singing domain, the development of automatic lyric transcription (ALT) suffers from limited data and degraded intelligibility of sung lyrics. To fill in the performance gap between ALT and ASR, we attempt to exploit the similarities between speech and singing. In this work, we propose a transfer-learning-based ALT solution that takes advantage of these similarities by adapting wav2vec 2.0, an SSL ASR model, to the singing domain. We maximize the effectiveness of transfer learning by exploring the influence of different transfer starting points. We further enhance the performance by extending the original CTC model to a hybrid CTC/attention model. Our method surpasses previous approaches by a large margin on various ALT benchmark datasets. Further experiments show that, with even a tiny proportion of training data, our method still achieves competitive performance.

</details>

### [Improving Data Driven Inverse Text Normalization using Data Augmentation](2207.09674.md)
**Laxmi Pandey, Debjyoti Paul, Pooja Chitkara, Yutong Pang et al.** · 2022-07-20

<details>
<summary>Abstract</summary>

Inverse text normalization (ITN) is used to convert the spoken form output of an automatic speech recognition (ASR) system to a written form. Traditional handcrafted ITN rules can be complex to transcribe and maintain. Meanwhile neural modeling approaches require quality large-scale spoken-written pair examples in the same or similar domain as the ASR system (in-domain data), to train. Both these approaches require costly and complex annotations. In this paper, we present a data augmentation technique that effectively generates rich spoken-written numeric pairs from out-of-domain textual data with minimal human annotation. We empirically demonstrate that ITN model trained using our data augmentation technique consistently outperform ITN model trained using only in-domain data across all numeric surfaces like cardinal, currency, and fraction, by an overall accuracy of 14.44%.

</details>

### [ILASR: Privacy-Preserving Incremental Learning for Automatic Speech Recognition at Production Scale](2207.09078.md)
**Gopinath Chennupati, Milind Rao, Gurpreet Chadha, Aaron Eakin et al.** · 2022-07-19

<details>
<summary>Abstract</summary>

Incremental learning is one paradigm to enable model building and updating at scale with streaming data. For end-to-end automatic speech recognition (ASR) tasks, the absence of human annotated labels along with the need for privacy preserving policies for model building makes it a daunting challenge. Motivated by these challenges, in this paper we use a cloud based framework for production systems to demonstrate insights from privacy preserving incremental learning for automatic speech recognition (ILASR). By privacy preserving, we mean, usage of ephemeral data which are not human annotated. This system is a step forward for production levelASR models for incremental/continual learning that offers near real-time test-bed for experimentation in the cloud for end-to-end ASR, while adhering to privacy-preserving policies. We show that the proposed system can improve the production models significantly(3%) over a new time period of six months even in the absence of human annotated labels with varying levels of weak supervision and large batch sizes in incremental learning. This improvement is 20% over test sets with new words and phrases in the new time period. We demonstrate the effectiveness of model building in a privacy-preserving incremental fashion for ASR while further exploring the utility of having an effective teacher model and use of large batch sizes.

</details>

### [End-to-End Spoken Language Understanding: Performance analyses of a voice command task in a low resource setting](2207.08179.md)
**Thierry Desot, François Portet, Michel Vacher** · 2022-07-17

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is a core task in most human-machine interaction systems. With the emergence of smart homes, smart phones and smart speakers, SLU has become a key technology for the industry. In a classical SLU approach, an Automatic Speech Recognition (ASR) module transcribes the speech signal into a textual representation from which a Natural Language Understanding (NLU) module extracts semantic information. Recently End-to-End SLU (E2E SLU) based on Deep Neural Networks has gained momentum since it benefits from the joint optimization of the ASR and the NLU parts, hence limiting the cascade of error effect of the pipeline architecture. However, little is known about the actual linguistic properties used by E2E models to predict concepts and intents from speech input. In this paper, we present a study identifying the signal features and other linguistic properties used by an E2E model to perform the SLU task. The study is carried out in the application domain of a smart home that has to handle non-English (here French) voice commands. The results show that a good E2E SLU performance does not always require a perfect ASR capability. Furthermore, the results show the superior capabilities of the E2E model in handling background noise and syntactic variation compared to the pipeline model. Finally, a finer-grained analysis suggests that the E2E model uses the pitch information of the input signal to identify voice command concepts. The results and methodology outlined in this paper provide a springboard for further analyses of E2E models in speech processing.

</details>

### [2D Self-Organized ONN Model For Handwritten Text Recognition](2207.08139.md)
**Hanadi Hassen Mohammed, Junaid Malik, Somaya Al-Madeed, Serkan Kiranyaz** · 2022-07-17

<details>
<summary>Abstract</summary>

Deep Convolutional Neural Networks (CNNs) have recently reached state-of-the-art Handwritten Text Recognition (HTR) performance. However, recent research has shown that typical CNNs' learning performance is limited since they are homogeneous networks with a simple (linear) neuron model. With their heterogeneous network structure incorporating non-linear neurons, Operational Neural Networks (ONNs) have recently been proposed to address this drawback. Self-ONNs are self-organized variations of ONNs with the generative neuron model that can generate any non-linear function using the Taylor approximation. In this study, in order to improve the state-of-the-art performance level in HTR, the 2D Self-organized ONNs (Self-ONNs) in the core of a novel network model are proposed. Moreover, deformable convolutions, which have recently been demonstrated to tackle variations in the writing styles better, are utilized in this study. The results over the IAM English dataset and HADARA80P Arabic dataset show that the proposed model with the operational layers of Self-ONNs significantly improves Character Error Rate (CER) and Word Error Rate (WER). Compared with its counterpart CNNs, Self-ONNs reduce CER and WER by 1.2% and 3.4 % in the HADARA80P and 0.199% and 1.244% in the IAM dataset. The results over the benchmark IAM demonstrate that the proposed model with the operational layers of Self-ONNs outperforms recent deep CNN models by a significant margin while the use of Self-ONNs with deformable convolutions demonstrates exceptional results.

</details>

### [Sotto Voce: Federated Speech Recognition with Differential Privacy Guarantees](2207.07816.md)
**Michael Shoemate, Kevin Jett, Ethan Cowan, Sean Colbath et al.** · 2022-07-16

<details>
<summary>Abstract</summary>

Speech data is expensive to collect, and incredibly sensitive to its sources. It is often the case that organizations independently collect small datasets for their own use, but often these are not performant for the demands of machine learning. Organizations could pool these datasets together and jointly build a strong ASR system; sharing data in the clear, however, comes with tremendous risk, in terms of intellectual property loss as well as loss of privacy of the individuals who exist in the dataset. In this paper, we offer a potential solution for learning an ML model across multiple organizations where we can provide mathematical guarantees limiting privacy loss. We use a Federated Learning approach built on a strong foundation of Differential Privacy techniques. We apply these to a senone classification prototype and demonstrate that the model improves with the addition of private data while still respecting privacy.

</details>

### [Position Prediction as an Effective Pretraining Strategy](2207.07611.md)
**Shuangfei Zhai, Navdeep Jaitly, Jason Ramapuram, Dan Busbridge et al.** · 2022-07-15

<details>
<summary>Abstract</summary>

Transformers have gained increasing popularity in a wide range of applications, including Natural Language Processing (NLP), Computer Vision and Speech Recognition, because of their powerful representational capacity. However, harnessing this representational capacity effectively requires a large amount of data, strong regularization, or both, to mitigate overfitting. Recently, the power of the Transformer has been unlocked by self-supervised pretraining strategies based on masked autoencoders which rely on reconstructing masked inputs, directly, or contrastively from unmasked content. This pretraining strategy which has been used in BERT models in NLP, Wav2Vec models in Speech and, recently, in MAE models in Vision, forces the model to learn about relationships between the content in different parts of the input using autoencoding related objectives. In this paper, we propose a novel, but surprisingly simple alternative to content reconstruction~-- that of predicting locations from content, without providing positional information for it. Doing so requires the Transformer to understand the positional relationships between different parts of the input, from their content alone. This amounts to an efficient implementation where the pretext task is a classification problem among all possible positions for each input token. We experiment on both Vision and Speech benchmarks, where our approach brings improvements over strong supervised training baselines and is comparable to modern unsupervised/self-supervised pretraining methods. Our method also enables Transformers trained without position embeddings to outperform ones trained with full position information.

</details>

### [Direction-Aware Joint Adaptation of Neural Speech Enhancement and Recognition in Real Multiparty Conversational Environments](2207.07273.md)
**Yicheng Du, Aditya Arie Nugraha, Kouhei Sekiguchi, Yoshiaki Bando et al.** · 2022-07-15

<details>
<summary>Abstract</summary>

This paper describes noisy speech recognition for an augmented reality headset that helps verbal communication within real multiparty conversational environments. A major approach that has actively been studied in simulated environments is to sequentially perform speech enhancement and automatic speech recognition (ASR) based on deep neural networks (DNNs) trained in a supervised manner. In our task, however, such a pretrained system fails to work due to the mismatch between the training and test conditions and the head movements of the user. To enhance only the utterances of a target speaker, we use beamforming based on a DNN-based speech mask estimator that can adaptively extract the speech components corresponding to a head-relative particular direction. We propose a semi-supervised adaptation method that jointly updates the mask estimator and the ASR model at run-time using clean speech signals with ground-truth transcriptions and noisy speech signals with highly-confident estimated transcriptions. Comparative experiments using the state-of-the-art distant speech recognition system show that the proposed method significantly improves the ASR performance.

</details>

### [Direction-Aware Adaptive Online Neural Speech Enhancement with an Augmented Reality Headset in Real Noisy Conversational Environments](2207.07296.md)
**Kouhei Sekiguchi, Aditya Arie Nugraha, Yicheng Du, Yoshiaki Bando et al.** · 2022-07-15

<details>
<summary>Abstract</summary>

This paper describes the practical response- and performance-aware development of online speech enhancement for an augmented reality (AR) headset that helps a user understand conversations made in real noisy echoic environments (e.g., cocktail party). One may use a state-of-the-art blind source separation method called fast multichannel nonnegative matrix factorization (FastMNMF) that works well in various environments thanks to its unsupervised nature. Its heavy computational cost, however, prevents its application to real-time processing. In contrast, a supervised beamforming method that uses a deep neural network (DNN) for estimating spatial information of speech and noise readily fits real-time processing, but suffers from drastic performance degradation in mismatched conditions. Given such complementary characteristics, we propose a dual-process robust online speech enhancement method based on DNN-based beamforming with FastMNMF-guided adaptation. FastMNMF (back end) is performed in a mini-batch style and the noisy and enhanced speech pairs are used together with the original parallel training data for updating the direction-aware DNN (front end) with backpropagation at a computationally-allowable interval. This method is used with a blind dereverberation method called weighted prediction error (WPE) for transcribing the noisy reverberant speech of a speaker, which can be detected from video or selected by a user's hand gesture or eye gaze, in a streaming manner and spatially showing the transcriptions with an AR technique. Our experiment showed that the word error rate was improved by more than 10 points with the run-time adaptation using only twelve minutes of observation.

</details>

### [Efficient spike encoding algorithms for neuromorphic speech recognition](2207.07073.md)
**Sidi Yaya Arnaud Yarga, Jean Rouat, Sean U. N. Wood** · 2022-07-14

<details>
<summary>Abstract</summary>

Spiking Neural Networks (SNN) are known to be very effective for neuromorphic processor implementations, achieving orders of magnitude improvements in energy efficiency and computational latency over traditional deep learning approaches. Comparable algorithmic performance was recently made possible as well with the adaptation of supervised training algorithms to the context of SNN. However, information including audio, video, and other sensor-derived data are typically encoded as real-valued signals that are not well-suited to SNN, preventing the network from leveraging spike timing information. Efficient encoding from real-valued signals to spikes is therefore critical and significantly impacts the performance of the overall system. To efficiently encode signals into spikes, both the preservation of information relevant to the task at hand as well as the density of the encoded spikes must be considered. In this paper, we study four spike encoding methods in the context of a speaker independent digit classification system: Send on Delta, Time to First Spike, Leaky Integrate and Fire Neuron and Bens Spiker Algorithm. We first show that all encoding methods yield higher classification accuracy using significantly fewer spikes when encoding a bio-inspired cochleagram as opposed to a traditional short-time Fourier transform. We then show that two Send On Delta variants result in classification results comparable with a state of the art deep convolutional neural network baseline, while simultaneously reducing the encoded bit rate. Finally, we show that several encoding methods result in improved performance over the conventional deep learning baseline in certain cases, further demonstrating the power of spike encoding algorithms in the encoding of real-valued signals and that neuromorphic implementation has the potential to outperform state of the art techniques.

</details>

### [u-HuBERT: Unified Mixed-Modal Speech Pretraining And Zero-Shot Transfer to Unlabeled Modality](2207.07036.md)
**Wei-Ning Hsu, Bowen Shi** · 2022-07-14

<details>
<summary>Abstract</summary>

While audio-visual speech models can yield superior performance and robustness compared to audio-only models, their development and adoption are hindered by the lack of labeled and unlabeled audio-visual data and the cost to deploy one model per modality. In this paper, we present u-HuBERT, a self-supervised pre-training framework that can leverage both multimodal and unimodal speech with a unified masked cluster prediction objective. By utilizing modality dropout during pre-training, we demonstrate that a single fine-tuned model can achieve performance on par or better than the state-of-the-art modality-specific models. Moreover, our model fine-tuned only on audio can perform well with audio-visual and visual speech input, achieving zero-shot modality generalization for multiple speech processing tasks. In particular, our single model yields 1.2%/1.4%/27.2% speech recognition word error rate on LRS3 with audio-visual/audio/visual input. Codes and models are available at https://github.com/facebookresearch/av_hubert

</details>

### [Data Augmentation for Low-Resource Quechua ASR Improvement](2207.06872.md)
**Rodolfo Zevallos, Nuria Bel, Guillermo Cámbara, Mireia Farrús et al.** · 2022-07-14

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is a key element in new services that helps users to interact with an automated system. Deep learning methods have made it possible to deploy systems with word error rates below 5% for ASR of English. However, the use of these methods is only available for languages with hundreds or thousands of hours of audio and their corresponding transcriptions. For the so-called low-resource languages to speed up the availability of resources that can improve the performance of their ASR systems, methods of creating new resources on the basis of existing ones are being investigated. In this paper we describe our data augmentation approach to improve the results of ASR models for low-resource and agglutinative languages. We carry out experiments developing an ASR for Quechua using the wav2letter++ model. We reduced WER by 8.73% through our approach to the base model. The resulting ASR model obtained 22.75% WER and was trained with 99 hours of original resources and 99 hours of synthetic data obtained with a combination of text augmentation and synthetic speech generati

</details>

### [Two-Pass Low Latency End-to-End Spoken Language Understanding](2207.06670.md)
**Siddhant Arora, Siddharth Dalmia, Xuankai Chang, Brian Yan et al.** · 2022-07-14

<details>
<summary>Abstract</summary>

End-to-end (E2E) models are becoming increasingly popular for spoken language understanding (SLU) systems and are beginning to achieve competitive performance to pipeline-based approaches. However, recent work has shown that these models struggle to generalize to new phrasings for the same intent indicating that models cannot understand the semantic content of the given utterance. In this work, we incorporated language models pre-trained on unlabeled text data inside E2E-SLU frameworks to build strong semantic representations. Incorporating both semantic and acoustic information can increase the inference time, leading to high latency when deployed for applications like voice assistants. We developed a 2-pass SLU system that makes low latency prediction using acoustic information from the few seconds of the audio in the first pass and makes higher quality prediction in the second pass by combining semantic and acoustic representations. We take inspiration from prior work on 2-pass end-to-end speech recognition systems that attends on both audio and first-pass hypothesis using a deliberation network. The proposed 2-pass SLU system outperforms the acoustic-based SLU model on the Fluent Speech Commands Challenge Set and SLURP dataset and reduces latency, thus improving user experience. Our code and models are publicly available as part of the ESPnet-SLU toolkit.

</details>

### [RSD-GAN: Regularized Sobolev Defense GAN Against Speech-to-Text Adversarial Attacks](2207.06858.md)
**Mohammad Esmaeilpour, Nourhene Chaalia, Patrick Cardinal** · 2022-07-14

<details>
<summary>Abstract</summary>

This paper introduces a new synthesis-based defense algorithm for counteracting with a varieties of adversarial attacks developed for challenging the performance of the cutting-edge speech-to-text transcription systems. Our algorithm implements a Sobolev-based GAN and proposes a novel regularizer for effectively controlling over the functionality of the entire generative model, particularly the discriminator network during training. Our achieved results upon carrying out numerous experiments on the victim DeepSpeech, Kaldi, and Lingvo speech transcription systems corroborate the remarkable performance of our defense approach against a comprehensive range of targeted and non-targeted adversarial attacks.

</details>

### [MM-ALT: A Multimodal Automatic Lyric Transcription System](2207.06127.md)
**Xiangming Gu, Longshen Ou, Danielle Ong, Ye Wang** · 2022-07-13

<details>
<summary>Abstract</summary>

Automatic lyric transcription (ALT) is a nascent field of study attracting increasing interest from both the speech and music information retrieval communities, given its significant application potential. However, ALT with audio data alone is a notoriously difficult task due to instrumental accompaniment and musical constraints resulting in degradation of both the phonetic cues and the intelligibility of sung lyrics. To tackle this challenge, we propose the MultiModal Automatic Lyric Transcription system (MM-ALT), together with a new dataset, N20EM, which consists of audio recordings, videos of lip movements, and inertial measurement unit (IMU) data of an earbud worn by the performing singer. We first adapt the wav2vec 2.0 framework from automatic speech recognition (ASR) to the ALT task. We then propose a video-based ALT method and an IMU-based voice activity detection (VAD) method. In addition, we put forward the Residual Cross Attention (RCA) mechanism to fuse data from the three modalities (i.e., audio, video, and IMU). Experiments show the effectiveness of our proposed MM-ALT system, especially in terms of noise robustness. Project page is at https://n20em.github.io.

</details>

### [Visual Context-driven Audio Feature Enhancement for Robust End-to-End Audio-Visual Speech Recognition](2207.06020.md)
**Joanna Hong, Minsu Kim, Daehun Yoo, Yong Man Ro** · 2022-07-13

<details>
<summary>Abstract</summary>

This paper focuses on designing a noise-robust end-to-end Audio-Visual Speech Recognition (AVSR) system. To this end, we propose Visual Context-driven Audio Feature Enhancement module (V-CAFE) to enhance the input noisy audio speech with a help of audio-visual correspondence. The proposed V-CAFE is designed to capture the transition of lip movements, namely visual context and to generate a noise reduction mask by considering the obtained visual context. Through context-dependent modeling, the ambiguity in viseme-to-phoneme mapping can be refined for mask generation. The noisy representations are masked out with the noise reduction mask resulting in enhanced audio features. The enhanced audio features are fused with the visual features and taken to an encoder-decoder model composed of Conformer and Transformer for speech recognition. We show the proposed end-to-end AVSR with the V-CAFE can further improve the noise-robustness of AVSR. The effectiveness of the proposed method is evaluated in noisy speech recognition and overlapped speech recognition experiments using the two largest audio-visual datasets, LRS2 and LRS3.

</details>

### [End-to-end speech recognition modeling from de-identified data](2207.05469.md)
**Martin Flechl, Shou-Chun Yin, Junho Park, Peter Skala** · 2022-07-12

<details>
<summary>Abstract</summary>

De-identification of data used for automatic speech recognition modeling is a critical component in protecting privacy, especially in the medical domain. However, simply removing all personally identifiable information (PII) from end-to-end model training data leads to a significant performance degradation in particular for the recognition of names, dates, locations, and words from similar categories. We propose and evaluate a two-step method for partially recovering this loss. First, PII is identified, and each occurrence is replaced with a random word sequence of the same category. Then, corresponding audio is produced via text-to-speech or by splicing together matching audio fragments extracted from the corpus. These artificial audio/label pairs, together with speaker turns from the original data without PII, are used to train models. We evaluate the performance of this method on in-house data of medical conversations and observe a recovery of almost the entire performance degradation in the general word error rate while still maintaining a strong diarization performance. Our main focus is the improvement of recall and precision in the recognition of PII-related words. Depending on the PII category, between $50\% - 90\%$ of the performance degradation can be recovered using our proposed method.

</details>

### [Speaker Anonymization with Phonetic Intermediate Representations](2207.04834.md)
**Sarina Meyer, Florian Lux, Pavel Denisov, Julia Koch et al.** · 2022-07-11

<details>
<summary>Abstract</summary>

In this work, we propose a speaker anonymization pipeline that leverages high quality automatic speech recognition and synthesis systems to generate speech conditioned on phonetic transcriptions and anonymized speaker embeddings. Using phones as the intermediate representation ensures near complete elimination of speaker identity information from the input while preserving the original phonetic content as much as possible. Our experimental results on LibriSpeech and VCTK corpora reveal two key findings: 1) although automatic speech recognition produces imperfect transcriptions, our neural speech synthesis system can handle such errors, making our system feasible and robust, and 2) combining speaker embeddings from different resources is beneficial and their appropriate normalization is crucial. Overall, our final best system outperforms significantly the baselines provided in the Voice Privacy Challenge 2020 in terms of privacy robustness against a lazy-informed attacker while maintaining high intelligibility and naturalness of the anonymized speech.

</details>

### [Speaker consistency loss and step-wise optimization for semi-supervised joint training of TTS and ASR using unpaired text data](2207.04659.md)
**Naoki Makishima, Satoshi Suzuki, Atsushi Ando, Ryo Masumura** · 2022-07-11

<details>
<summary>Abstract</summary>

In this paper, we investigate the semi-supervised joint training of text to speech (TTS) and automatic speech recognition (ASR), where a small amount of paired data and a large amount of unpaired text data are available. Conventional studies form a cycle called the TTS-ASR pipeline, where the multispeaker TTS model synthesizes speech from text with a reference speech and the ASR model reconstructs the text from the synthesized speech, after which both models are trained with a cycle-consistency loss. However, the synthesized speech does not reflect the speaker characteristics of the reference speech and the synthesized speech becomes overly easy for the ASR model to recognize after training. This not only decreases the TTS model quality but also limits the ASR model improvement. To solve this problem, we propose improving the cycleconsistency-based training with a speaker consistency loss and step-wise optimization. The speaker consistency loss brings the speaker characteristics of the synthesized speech closer to that of the reference speech. In the step-wise optimization, we first freeze the parameter of the TTS model before both models are trained to avoid over-adaptation of the TTS model to the ASR model. Experimental results demonstrate the efficacy of the proposed method.

</details>

### [Online Continual Learning of End-to-End Speech Recognition Models](2207.05071.md)
**Muqiao Yang, Ian Lane, Shinji Watanabe** · 2022-07-11

<details>
<summary>Abstract</summary>

Continual Learning, also known as Lifelong Learning, aims to continually learn from new data as it becomes available. While prior research on continual learning in automatic speech recognition has focused on the adaptation of models across multiple different speech recognition tasks, in this paper we propose an experimental setting for \textit{online continual learning} for automatic speech recognition of a single task. Specifically focusing on the case where additional training data for the same task becomes available incrementally over time, we demonstrate the effectiveness of performing incremental model updates to end-to-end speech recognition models with an online Gradient Episodic Memory (GEM) method. Moreover, we show that with online continual learning and a selective sampling strategy, we can maintain an accuracy that is similar to retraining a model from scratch while requiring significantly lower computation costs. We have also verified our method with self-supervised learning (SSL) features.

</details>

### [A Lexicon and Depth-wise Separable Convolution Based Handwritten Text Recognition System](2207.04651.md)
**Lalita Kumari, Sukhdeep Singh, VVS Rathore, Anuj Sharma** · 2022-07-11

<details>
<summary>Abstract</summary>

Cursive handwritten text recognition is a challenging research problem in the domain of pattern recognition. The current state-of-the-art approaches include models based on convolutional recurrent neural networks and multi-dimensional long short-term memory recurrent neural networks techniques. These methods are highly computationally extensive as well model is complex at design level. In recent studies, combination of convolutional neural network and gated convolutional neural networks based models demonstrated less number of parameters in comparison to convolutional recurrent neural networks based models. In the direction to reduced the total number of parameters to be trained, in this work, we have used depthwise convolution in place of standard convolutions with a combination of gated-convolutional neural network and bidirectional gated recurrent unit to reduce the total number of parameters to be trained. Additionally, we have also included a lexicon based word beam search decoder at testing step. It also helps in improving the the overall accuracy of the model. We have obtained 3.84% character error rate and 9.40% word error rate on IAM dataset; 4.88% character error rate and 14.56% word error rate in George Washington dataset, respectively.

</details>

### [Intermediate-layer output Regularization for Attention-based Speech Recognition with Shared Decoder](2207.04177.md)
**Jicheng Zhang, Yizhou Peng, Haihua Xu, Yi He et al.** · 2022-07-09

<details>
<summary>Abstract</summary>

Intermediate layer output (ILO) regularization by means of multitask training on encoder side has been shown to be an effective approach to yielding improved results on a wide range of end-to-end ASR frameworks. In this paper, we propose a novel method to do ILO regularized training differently. Instead of using conventional multitask methods that entail more training overhead, we directly make the intermediate layer output as input to the decoder, that is, our decoder not only accepts the output of the final encoder layer as input, it also takes the output of the encoder ILO as input during training. With the proposed method, as both encoder and decoder are simultaneously "regularized", the network is more sufficiently trained, consistently leading to improved results, over the ILO-based CTC method, as well as over the original attention-based modeling method without the proposed method employed.

</details>

### [Internal Language Model Estimation based Language Model Fusion for Cross-Domain Code-Switching Speech Recognition](2207.04176.md)
**Yizhou Peng, Yufei Liu, Jicheng Zhang, Haihua Xu et al.** · 2022-07-09

<details>
<summary>Abstract</summary>

Internal Language Model Estimation (ILME) based language model (LM) fusion has been shown significantly improved recognition results over conventional shallow fusion in both intra-domain and cross-domain speech recognition tasks. In this paper, we attempt to apply our ILME method to cross-domain code-switching speech recognition (CSSR) work. Specifically, our curiosity comes from several aspects. First, we are curious about how effective the ILME-based LM fusion is for both intra-domain and cross-domain CSSR tasks. We verify this with or without merging two code-switching domains. More importantly, we train an end-to-end (E2E) speech recognition model by means of merging two monolingual data sets and observe the efficacy of the proposed ILME-based LM fusion for CSSR. Experimental results on SEAME that is from Southeast Asian and another Chinese Mainland CS data set demonstrate the effectiveness of the proposed ILME-based LM fusion method.

</details>

### [Tandem Multitask Training of Speaker Diarisation and Speech Recognition for Meeting Transcription](2207.03852.md)
**Xianrui Zheng, Chao Zhang, Philip C. Woodland** · 2022-07-08

<details>
<summary>Abstract</summary>

Self-supervised-learning-based pre-trained models for speech data, such as Wav2Vec 2.0 (W2V2), have become the backbone of many speech tasks. In this paper, to achieve speaker diarisation and speech recognition using a single model, a tandem multitask training (TMT) method is proposed to fine-tune W2V2. For speaker diarisation, the tasks of voice activity detection (VAD) and speaker classification (SC) are required, and connectionist temporal classification (CTC) is used for ASR. The multitask framework implements VAD, SC, and ASR using an early layer, middle layer, and late layer of W2V2, which coincides with the order of segmenting the audio with VAD, clustering the segments based on speaker embeddings, and transcribing each segment with ASR. Experimental results on the augmented multi-party (AMI) dataset showed that using different W2V2 layers for VAD, SC, and ASR from the earlier to later layers for TMT not only saves computational cost, but also reduces diarisation error rates (DERs). Joint fine-tuning of VAD, SC, and ASR yielded 16%/17% relative reductions of DER with manual/automatic segmentation respectively, and consistent reductions in speaker attributed word error rate, compared to the baseline with separately fine-tuned models.

</details>

### [Non-Linear Pairwise Language Mappings for Low-Resource Multilingual Acoustic Model Fusion](2207.03391.md)
**Muhammad Umar Farooq, Darshan Adiga Haniya Narayana, Thomas Hain** · 2022-07-07

<details>
<summary>Abstract</summary>

Multilingual speech recognition has drawn significant attention as an effective way to compensate data scarcity for low-resource languages. End-to-end (e2e) modelling is preferred over conventional hybrid systems, mainly because of no lexicon requirement. However, hybrid DNN-HMMs still outperform e2e models in limited data scenarios. Furthermore, the problem of manual lexicon creation has been alleviated by publicly available trained models of grapheme-to-phoneme (G2P) and text to IPA transliteration for a lot of languages. In this paper, a novel approach of hybrid DNN-HMM acoustic models fusion is proposed in a multilingual setup for the low-resource languages. Posterior distributions from different monolingual acoustic models, against a target language speech signal, are fused together. A separate regression neural network is trained for each source-target language pair to transform posteriors from source acoustic model to the target language. These networks require very limited data as compared to the ASR training. Posterior fusion yields a relative gain of 14.65% and 6.5% when compared with multilingual and monolingual baselines respectively. Cross-lingual model fusion shows that the comparable results can be achieved without using posteriors from the language dependent ASR.

</details>

### [Investigating the Impact of Cross-lingual Acoustic-Phonetic Similarities on Multilingual Speech Recognition](2207.03390.md)
**Muhammad Umar Farooq, Thomas Hain** · 2022-07-07

<details>
<summary>Abstract</summary>

Multilingual automatic speech recognition (ASR) systems mostly benefit low resource languages but suffer degradation in performance across several languages relative to their monolingual counterparts. Limited studies have focused on understanding the languages behaviour in the multilingual speech recognition setups. In this paper, a novel data-driven approach is proposed to investigate the cross-lingual acoustic-phonetic similarities. This technique measures the similarities between posterior distributions from various monolingual acoustic models against a target speech signal. Deep neural networks are trained as mapping networks to transform the distributions from different acoustic models into a directly comparable form. The analysis observes that the languages closeness can not be truly estimated by the volume of overlapping phonemes set. Entropy analysis of the proposed mapping networks exhibits that a language with lesser overlap can be more amenable to cross-lingual transfer, and hence more beneficial in the multilingual setup. Finally, the proposed posterior transformation approach is leveraged to fuse monolingual models for a target language. A relative improvement of ~8% over monolingual counterpart is achieved.

</details>

### [End-to-end Speech-to-Punctuated-Text Recognition](2207.03169.md)
**Jumon Nozaki, Tatsuya Kawahara, Kenkichi Ishizuka, Taiichi Hashimoto** · 2022-07-07

<details>
<summary>Abstract</summary>

Conventional automatic speech recognition systems do not produce punctuation marks which are important for the readability of the speech recognition results. They are also needed for subsequent natural language processing tasks such as machine translation. There have been a lot of works on punctuation prediction models that insert punctuation marks into speech recognition results as post-processing. However, these studies do not utilize acoustic information for punctuation prediction and are directly affected by speech recognition errors. In this study, we propose an end-to-end model that takes speech as input and outputs punctuated texts. This model is expected to predict punctuation robustly against speech recognition errors while using acoustic information. We also propose to incorporate an auxiliary loss to train the model using the output of the intermediate layer and unpunctuated texts. Through experiments, we compare the performance of the proposed model to that of a cascaded system. The proposed model achieves higher punctuation prediction accuracy than the cascaded system without sacrificing the speech recognition error rate. It is also demonstrated that the multi-task learning using the intermediate output against the unpunctuated text is effective. Moreover, the proposed model has only about 1/7th of the parameters compared to the cascaded system.

</details>

### [Branchformer: Parallel MLP-Attention Architectures to Capture Local and Global Context for Speech Recognition and Understanding](2207.02971.md)
**Yifan Peng, Siddharth Dalmia, Ian Lane, Shinji Watanabe** · 2022-07-06

<details>
<summary>Abstract</summary>

Conformer has proven to be effective in many speech processing tasks. It combines the benefits of extracting local dependencies using convolutions and global dependencies using self-attention. Inspired by this, we propose a more flexible, interpretable and customizable encoder alternative, Branchformer, with parallel branches for modeling various ranged dependencies in end-to-end speech processing. In each encoder layer, one branch employs self-attention or its variant to capture long-range dependencies, while the other branch utilizes an MLP module with convolutional gating (cgMLP) to extract local relationships. We conduct experiments on several speech recognition and spoken language understanding benchmarks. Results show that our model outperforms both Transformer and cgMLP. It also matches with or outperforms state-of-the-art results achieved by Conformer. Furthermore, we show various strategies to reduce computation thanks to the two-branch architecture, including the ability to have variable inference complexity in a single trained model. The weights learned for merging branches indicate how local and global dependencies are utilized in different layers, which benefits model designing.

</details>

### [Low-resource Low-footprint Wake-word Detection using Knowledge Distillation](2207.03331.md)
**Arindam Ghosh, Mark Fuhs, Deblin Bagchi, Bahman Farahani et al.** · 2022-07-06

<details>
<summary>Abstract</summary>

As virtual assistants have become more diverse and specialized, so has the demand for application or brand-specific wake words. However, the wake-word-specific datasets typically used to train wake-word detectors are costly to create. In this paper, we explore two techniques to leverage acoustic modeling data for large-vocabulary speech recognition to improve a purpose-built wake-word detector: transfer learning and knowledge distillation. We also explore how these techniques interact with time-synchronous training targets to improve detection latency. Experiments are presented on the open-source "Hey Snips" dataset and a more challenging in-house far-field dataset. Using phone-synchronous targets and knowledge distillation from a large acoustic model, we are able to improve accuracy across dataset sizes for both datasets while reducing latency.

</details>

### [Kaggle Competition: Cantonese Audio-Visual Speech Recognition for In-car Commands](2207.02663.md)
**Wenliang Dai, Samuel Cahyawijaya, Tiezheng Yu, Elham J Barezi et al.** · 2022-07-06

<details>
<summary>Abstract</summary>

With the rise of deep learning and intelligent vehicles, the smart assistant has become an essential in-car component to facilitate driving and provide extra functionalities. In-car smart assistants should be able to process general as well as car-related commands and perform corresponding actions, which eases driving and improves safety. However, in this research field, most datasets are in major languages, such as English and Chinese. There is a huge data scarcity issue for low-resource languages, hindering the development of research and applications for broader communities. Therefore, it is crucial to have more benchmarks to raise awareness and motivate the research in low-resource languages. To mitigate this problem, we collect a new dataset, namely Cantonese In-car Audio-Visual Speech Recognition (CI-AVSR), for in-car speech recognition in the Cantonese language with video and audio data. Together with it, we propose Cantonese Audio-Visual Speech Recognition for In-car Commands as a new challenge for the community to tackle low-resource speech recognition under in-car scenarios.

</details>

### [Improving Streaming End-to-End ASR on Transformer-based Causal Models with Encoder States Revision Strategies](2207.02495.md)
**Zehan Li, Haoran Miao, Keqi Deng, Gaofeng Cheng et al.** · 2022-07-06

<details>
<summary>Abstract</summary>

There is often a trade-off between performance and latency in streaming automatic speech recognition (ASR). Traditional methods such as look-ahead and chunk-based methods, usually require information from future frames to advance recognition accuracy, which incurs inevitable latency even if the computation is fast enough. A causal model that computes without any future frames can avoid this latency, but its performance is significantly worse than traditional methods. In this paper, we propose corresponding revision strategies to improve the causal model. Firstly, we introduce a real-time encoder states revision strategy to modify previous states. Encoder forward computation starts once the data is received and revises the previous encoder states after several frames, which is no need to wait for any right context. Furthermore, a CTC spike position alignment decoding algorithm is designed to reduce time costs brought by the revision strategy. Experiments are all conducted on Librispeech datasets. Fine-tuning on the CTC-based wav2vec2.0 model, our best method can achieve 3.7/9.2 WERs on test-clean/other sets, which is also competitive with the chunk-based methods and the knowledge distillation methods.

</details>

### [Compute Cost Amortized Transformer for Streaming ASR](2207.02393.md)
**Yi Xie, Jonathan Macoskey, Martin Radfar, Feng-Ju Chang et al.** · 2022-07-05

<details>
<summary>Abstract</summary>

We present a streaming, Transformer-based end-to-end automatic speech recognition (ASR) architecture which achieves efficient neural inference through compute cost amortization. Our architecture creates sparse computation pathways dynamically at inference time, resulting in selective use of compute resources throughout decoding, enabling significant reductions in compute with minimal impact on accuracy. The fully differentiable architecture is trained end-to-end with an accompanying lightweight arbitrator mechanism operating at the frame-level to make dynamic decisions on each input while a tunable loss function is used to regularize the overall level of compute against predictive performance. We report empirical results from experiments using the compute amortized Transformer-Transducer (T-T) model conducted on LibriSpeech data. Our best model can achieve a 60% compute cost reduction with only a 3% relative word error rate (WER) increase.

</details>

### [DEFORMER: Coupling Deformed Localized Patterns with Global Context for Robust End-to-end Speech Recognition](2207.01732.md)
**Jiamin Xie, John H. L. Hansen** · 2022-07-04

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNN) have improved speech recognition performance greatly by exploiting localized time-frequency patterns. But these patterns are assumed to appear in symmetric and rigid kernels by the conventional CNN operation. It motivates the question: What about asymmetric kernels? In this study, we illustrate adaptive views can discover local features which couple better with attention than fixed views of the input. We replace depthwise CNNs in the Conformer architecture with a deformable counterpart, dubbed this "Deformer". By analyzing our best-performing model, we visualize both local receptive fields and global attention maps learned by the Deformer and show increased feature associations on the utterance level. The statistical analysis of learned kernel offsets provides an insight into the change of information in features with the network depth. Finally, replacing only half of the layers in the encoder, the Deformer improves +5.6% relative WER without a LM and +6.4% relative WER with a LM over the Conformer baseline on the WSJ eval92 set.

</details>

### [CPrune: Compiler-Informed Model Pruning for Efficient Target-Aware DNN Execution](2207.01260.md)
**Taeho Kim, Yongin Kwon, Jemin Lee, Taeho Kim et al.** · 2022-07-04

<details>
<summary>Abstract</summary>

Mobile devices run deep learning models for various purposes, such as image classification and speech recognition. Due to the resource constraints of mobile devices, researchers have focused on either making a lightweight deep neural network (DNN) model using model pruning or generating an efficient code using compiler optimization. Surprisingly, we found that the straightforward integration between model compression and compiler auto-tuning often does not produce the most efficient model for a target device. We propose CPrune, a compiler-informed model pruning for efficient target-aware DNN execution to support an application with a required target accuracy. CPrune makes a lightweight DNN model through informed pruning based on the structural information of subgraphs built during the compiler tuning process. Our experimental results show that CPrune increases the DNN execution speed up to 2.73x compared to the state-of-the-art TVM auto-tune while satisfying the accuracy requirement.

</details>

### [Generating gender-ambiguous voices for privacy-preserving speech recognition](2207.01052.md)
**Dimitrios Stoidis, Andrea Cavallaro** · 2022-07-03

<details>
<summary>Abstract</summary>

Our voice encodes a uniquely identifiable pattern which can be used to infer private attributes, such as gender or identity, that an individual might wish not to reveal when using a speech recognition service. To prevent attribute inference attacks alongside speech recognition tasks, we present a generative adversarial network, GenGAN, that synthesises voices that conceal the gender or identity of a speaker. The proposed network includes a generator with a U-Net architecture that learns to fool a discriminator. We condition the generator only on gender information and use an adversarial loss between signal distortion and privacy preservation. We show that GenGAN improves the trade-off between privacy and utility compared to privacy-preserving representation learning methods that consider gender information as a sensitive attribute to protect.

</details>

### [Leveraging Acoustic Contextual Representation by Audio-textual Cross-modal Learning for Conversational ASR](2207.01039.md)
**Kun Wei, Yike Zhang, Sining Sun, Lei Xie et al.** · 2022-07-03

<details>
<summary>Abstract</summary>

Leveraging context information is an intuitive idea to improve performance on conversational automatic speech recognition(ASR). Previous works usually adopt recognized hypotheses of historical utterances as preceding context, which may bias the current recognized hypothesis due to the inevitable historicalrecognition errors. To avoid this problem, we propose an audio-textual cross-modal representation extractor to learn contextual representations directly from preceding speech. Specifically, it consists of two modal-related encoders, extracting high-level latent features from speech and the corresponding text, and a cross-modal encoder, which aims to learn the correlation between speech and text. We randomly mask some input tokens and input sequences of each modality. Then a token-missing or modal-missing prediction with a modal-level CTC loss on the cross-modal encoder is performed. Thus, the model captures not only the bi-directional context dependencies in a specific modality but also relationships between different modalities. Then, during the training of the conversational ASR system, the extractor will be frozen to extract the textual representation of preceding speech, while such representation is used as context fed to the ASR decoder through attention mechanism. The effectiveness of the proposed approach is validated on several Mandarin conversation corpora and the highest character error rate (CER) reduction up to 16% is achieved on the MagicData dataset.

</details>

### [M-Adapter: Modality Adaptation for End-to-End Speech-to-Text Translation](2207.00952.md)
**Jinming Zhao, Hao Yang, Ehsan Shareghi, Gholamreza Haffari** · 2022-07-03

<details>
<summary>Abstract</summary>

End-to-end speech-to-text translation models are often initialized with pre-trained speech encoder and pre-trained text decoder. This leads to a significant training gap between pre-training and fine-tuning, largely due to the modality differences between speech outputs from the encoder and text inputs to the decoder. In this work, we aim to bridge the modality gap between speech and text to improve translation quality. We propose M-Adapter, a novel Transformer-based module, to adapt speech representations to text. While shrinking the speech sequence, M-Adapter produces features desired for speech-to-text translation via modelling global and local dependencies of a speech sequence. Our experimental results show that our model outperforms a strong baseline by up to 1 BLEU score on the Must-C En$\rightarrow$DE dataset.\footnote{Our code is available at https://github.com/mingzi151/w2v2-st.}

</details>

### [Continuous Sign Language Recognition via Temporal Super-Resolution Network](2207.00928.md)
**Qidan Zhu, Jing Li, Fei Yuan, Quan Gan** · 2022-07-03

<details>
<summary>Abstract</summary>

Aiming at the problem that the spatial-temporal hierarchical continuous sign language recognition model based on deep learning has a large amount of computation, which limits the real-time application of the model, this paper proposes a temporal super-resolution network(TSRNet). The data is reconstructed into a dense feature sequence to reduce the overall model computation while keeping the final recognition accuracy loss to a minimum. The continuous sign language recognition model(CSLR) via TSRNet mainly consists of three parts: frame-level feature extraction, time series feature extraction and TSRNet, where TSRNet is located between frame-level feature extraction and time-series feature extraction, which mainly includes two branches: detail descriptor and rough descriptor. The sparse frame-level features are fused through the features obtained by the two designed branches as the reconstructed dense frame-level feature sequence, and the connectionist temporal classification(CTC) loss is used for training and optimization after the time-series feature extraction part. To better recover semantic-level information, the overall model is trained with the self-generating adversarial training method proposed in this paper to reduce the model error rate. The training method regards the TSRNet as the generator, and the frame-level processing part and the temporal processing part as the discriminator. In addition, in order to unify the evaluation criteria of model accuracy loss under different benchmarks, this paper proposes word error rate deviation(WERD), which takes the error rate between the estimated word error rate (WER) and the reference WER obtained by the reconstructed frame-level feature sequence and the complete original frame-level feature sequence as the WERD. Experiments on two large-scale sign language datasets demonstrate the effectiveness of the proposed model.

</details>

### [Improving Transformer-based Conversational ASR by Inter-Sentential Attention Mechanism](2207.00883.md)
**Kun Wei, Pengcheng Guo, Ning Jiang** · 2022-07-02

<details>
<summary>Abstract</summary>

Transformer-based models have demonstrated their effectiveness in automatic speech recognition (ASR) tasks and even shown superior performance over the conventional hybrid framework. The main idea of Transformers is to capture the long-range global context within an utterance by self-attention layers. However, for scenarios like conversational speech, such utterance-level modeling will neglect contextual dependencies that span across utterances. In this paper, we propose to explicitly model the inter-sentential information in a Transformer based end-to-end architecture for conversational speech recognition. Specifically, for the encoder network, we capture the contexts of previous speech and incorporate such historic information into current input by a context-aware residual attention mechanism. For the decoder, the prediction of current utterance is also conditioned on the historic linguistic information through a conditional decoder framework. We show the effectiveness of our proposed method on several open-source dialogue corpora and the proposed method consistently improved the performance from the utterance-level Transformer-based ASR models.

</details>

### [Tree-constrained Pointer Generator with Graph Neural Network Encodings for Contextual Speech Recognition](2207.00857.md)
**Guangzhi Sun, Chao Zhang, Philip C. Woodland** · 2022-07-02

<details>
<summary>Abstract</summary>

Incorporating biasing words obtained as contextual knowledge is critical for many automatic speech recognition (ASR) applications. This paper proposes the use of graph neural network (GNN) encodings in a tree-constrained pointer generator (TCPGen) component for end-to-end contextual ASR. By encoding the biasing words in the prefix-tree with a tree-based GNN, lookahead for future wordpieces in end-to-end ASR decoding is achieved at each tree node by incorporating information about all wordpieces on the tree branches rooted from it, which allows a more accurate prediction of the generation probability of the biasing words. Systems were evaluated on the Librispeech corpus using simulated biasing tasks, and on the AMI corpus by proposing a novel visual-grounded contextual ASR pipeline that extracts biasing words from slides alongside each meeting. Results showed that TCPGen with GNN encodings achieved about a further 15% relative WER reduction on the biasing words compared to the original TCPGen, with a negligible increase in the computation cost for decoding.

</details>

### [UserLibri: A Dataset for ASR Personalization Using Only Text](2207.00706.md)
**Theresa Breiner, Swaroop Ramaswamy, Ehsan Variani, Shefali Garg et al.** · 2022-07-02

<details>
<summary>Abstract</summary>

Personalization of speech models on mobile devices (on-device personalization) is an active area of research, but more often than not, mobile devices have more text-only data than paired audio-text data. We explore training a personalized language model on text-only data, used during inference to improve speech recognition performance for that user. We experiment on a user-clustered LibriSpeech corpus, supplemented with personalized text-only data for each user from Project Gutenberg. We release this User-Specific LibriSpeech (UserLibri) dataset to aid future personalization research. LibriSpeech audio-transcript pairs are grouped into 55 users from the test-clean dataset and 52 users from test-other. We are able to lower the average word error rate per user across both sets in streaming and nonstreaming models, including an improvement of 2.5 for the harder set of test-other users when streaming.

</details>

### [Improving Low-Resource Speech Recognition with Pretrained Speech Models: Continued Pretraining vs. Semi-Supervised Training](2207.00659.md)
**Mitchell DeHaven, Jayadev Billa** · 2022-07-01

<details>
<summary>Abstract</summary>

Self-supervised Transformer based models, such as wav2vec 2.0 and HuBERT, have produced significant improvements over existing approaches to automatic speech recognition (ASR). This is evident in the performance of the wav2vec 2.0 based pretrained XLSR-53 model across many languages when fine-tuned with available labeled data. However, the performance from finetuning these models can be dependent on the amount of in-language or similar-to-in-language data included in the pretraining dataset. In this paper we investigate continued pretraining (CoPT) with unlabeled in-language audio data on the XLSR-53 pretrained model in several low-resource languages. CoPT is more computationally efficient than semi-supervised training (SST), the standard approach of utilizing unlabeled data in ASR, since it omits the need for pseudo-labeling of the unlabeled data. We show CoPT results in word error rates (WERs), equal to or slightly better than using SST. In addition, we show that using the CoPT model for pseudo-labeling, and using these labels in SST, results in further improvements in WER.

</details>

### [Updating Only Encoders Prevents Catastrophic Forgetting of End-to-End ASR Models](2207.00216.md)
**Yuki Takashima, Shota Horiguchi, Shinji Watanabe, Paola García et al.** · 2022-07-01

<details>
<summary>Abstract</summary>

In this paper, we present an incremental domain adaptation technique to prevent catastrophic forgetting for an end-to-end automatic speech recognition (ASR) model. Conventional approaches require extra parameters of the same size as the model for optimization, and it is difficult to apply these approaches to end-to-end ASR models because they have a huge amount of parameters. To solve this problem, we first investigate which parts of end-to-end ASR models contribute to high accuracy in the target domain while preventing catastrophic forgetting. We conduct experiments on incremental domain adaptation from the LibriSpeech dataset to the AMI meeting corpus with two popular end-to-end ASR models and found that adapting only the linear layers of their encoders can prevent catastrophic forgetting. Then, on the basis of this finding, we develop an element-wise parameter selection focused on specific layers to further reduce the number of fine-tuning parameters. Experimental results show that our approach consistently prevents catastrophic forgetting compared to parameter selection from the whole model.

</details>

### [FitHuBERT: Going Thinner and Deeper for Knowledge Distillation of Speech Self-Supervised Learning](2207.00555.md)
**Yeonghyeon Lee, Kangwook Jang, Jahyun Goo, Youngmoon Jung et al.** · 2022-07-01

<details>
<summary>Abstract</summary>

Large-scale speech self-supervised learning (SSL) has emerged to the main field of speech processing, however, the problem of computational cost arising from its vast size makes a high entry barrier to academia. In addition, existing distillation techniques of speech SSL models compress the model by reducing layers, which induces performance degradation in linguistic pattern recognition tasks such as phoneme recognition (PR). In this paper, we propose FitHuBERT, which makes thinner in dimension throughout almost all model components and deeper in layer compared to prior speech SSL distillation works. Moreover, we employ a time-reduction layer to speed up inference time and propose a method of hint-based distillation for less performance degradation. Our method reduces the model to 23.8% in size and 35.9% in inference time compared to HuBERT. Also, we achieve 12.1% word error rate and 13.3% phoneme error rate on the SUPERB benchmark which is superior than prior work.

</details>

### [Sub-8-Bit Quantization Aware Training for 8-Bit Neural Network Accelerator with On-Device Speech Recognition](2206.15408.md)
**Kai Zhen, Hieu Duy Nguyen, Raviteja Chinta, Nathan Susanj et al.** · 2022-06-30

<details>
<summary>Abstract</summary>

We present a novel sub-8-bit quantization-aware training (S8BQAT) scheme for 8-bit neural network accelerators. Our method is inspired from Lloyd-Max compression theory with practical adaptations for a feasible computational overhead during training. With the quantization centroids derived from a 32-bit baseline, we augment training loss with a Multi-Regional Absolute Cosine (MRACos) regularizer that aggregates weights towards their nearest centroid, effectively acting as a pseudo compressor. Additionally, a periodically invoked hard compressor is introduced to improve the convergence rate by emulating runtime model weight quantization. We apply S8BQAT on speech recognition tasks using Recurrent Neural NetworkTransducer (RNN-T) architecture. With S8BQAT, we are able to increase the model parameter size to reduce the word error rate by 4-16% relatively, while still improving latency by 5%.

</details>

### [FeaRLESS: Feature Refinement Loss for Ensembling Self-Supervised Learning Features in Robust End-to-end Speech Recognition](2206.15056.md)
**Szu-Jui Chen, Jiamin Xie, John H. L. Hansen** · 2022-06-30

<details>
<summary>Abstract</summary>

Self-supervised learning representations (SSLR) have resulted in robust features for downstream tasks in many fields. Recently, several SSLRs have shown promising results on automatic speech recognition (ASR) benchmark corpora. However, previous studies have only shown performance for solitary SSLRs as an input feature for ASR models. In this study, we propose to investigate the effectiveness of diverse SSLR combinations using various fusion methods within end-to-end (E2E) ASR models. In addition, we will show there are correlations between these extracted SSLRs. As such, we further propose a feature refinement loss for decorrelation to efficiently combine the set of input features. For evaluation, we show that the proposed 'FeaRLESS learning features' perform better than systems without the proposed feature refinement loss for both the WSJ and Fearless Steps Challenge (FSC) corpora.

</details>

### [Nextformer: A ConvNeXt Augmented Conformer For End-To-End Speech Recognition](2206.14747.md)
**Yongjun Jiang, Jian Yu, Wenwen Yang, Bihong Zhang et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

Conformer models have achieved state-of-the-art(SOTA) results in end-to-end speech recognition. However Conformer mainly focuses on temporal modeling while pays less attention on time-frequency property of speech feature. In this paper we augment Conformer with ConvNeXt and propose Nextformer structure. We use stacks of ConvNeXt block to replace the commonly used subsampling module in Conformer for utilizing the information contained in time-frequency speech feature. Besides, we insert an additional downsampling module in middle of Conformer layers to make our model more efficient and accurate. We conduct experiments on two opening datasets, AISHELL-1 and WenetSpeech. On AISHELL-1, compared to Conformer baselines, Nextformer obtains 7.3% and 6.3% relative CER reduction in non-streaming and streaming mode respectively, and on a much larger WenetSpeech dataset, Nextformer gives 5.0%~6.5% and 7.5%~14.6% relative CER reduction in non-streaming and streaming mode, while keep the computational cost FLOPs comparable to Conformer. To the best of our knowledge, the proposed Nextformer model achieves SOTA results on AISHELL-1(CER 4.06%) and WenetSpeech(CER 7.56%/11.29%).

</details>

### [The THUEE System Description for the IARPA OpenASR21 Challenge](2206.14660.md)
**Jing Zhao, Haoyu Wang, Jinpeng Li, Shuzhou Chai et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

This paper describes the THUEE team's speech recognition system for the IARPA Open Automatic Speech Recognition Challenge (OpenASR21), with further experiment explorations. We achieve outstanding results under both the Constrained and Constrained-plus training conditions. For the Constrained training condition, we construct our basic ASR system based on the standard hybrid architecture. To alleviate the Out-Of-Vocabulary (OOV) problem, we extend the pronunciation lexicon using Grapheme-to-Phoneme (G2P) techniques for both OOV and potential new words. Standard acoustic model structures such as CNN-TDNN-F and CNN-TDNN-F-A are adopted. In addition, multiple data augmentation techniques are applied. For the Constrained-plus training condition, we use the self-supervised learning framework wav2vec2.0. We experiment with various fine-tuning techniques with the Connectionist Temporal Classification (CTC) criterion on top of the publicly available pre-trained model XLSR-53. We find that the frontend feature extractor plays an important role when applying the wav2vec2.0 pre-trained model to the encoder-decoder based CTC/Attention ASR architecture. Extra improvements can be achieved by using the CTC model finetuned in the target language as the frontend feature extractor.

</details>

### [Language-specific Characteristic Assistance for Code-switching Speech Recognition](2206.14580.md)
**Tongtong Song, Qiang Xu, Meng Ge, Longbiao Wang et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

Dual-encoder structure successfully utilizes two language-specific encoders (LSEs) for code-switching speech recognition. Because LSEs are initialized by two pre-trained language-specific models (LSMs), the dual-encoder structure can exploit sufficient monolingual data and capture the individual language attributes. However, most existing methods have no language constraints on LSEs and underutilize language-specific knowledge of LSMs. In this paper, we propose a language-specific characteristic assistance (LSCA) method to mitigate the above problems. Specifically, during training, we introduce two language-specific losses as language constraints and generate corresponding language-specific targets for them. During decoding, we take the decoding abilities of LSMs into account by combining the output probabilities of two LSMs and the mixture model to obtain the final predictions. Experiments show that either the training or decoding method of LSCA can improve the model's performance. Furthermore, the best result can obtain up to 15.4% relative error reduction on the code-switching test set by combining the training and decoding methods of LSCA. Moreover, the system can process code-switching speech recognition tasks well without extra shared parameters or even retraining based on two pre-trained LSMs by using our method.

</details>

### [STOP: A dataset for Spoken Task Oriented Semantic Parsing](2207.10643.md)
**Paden Tomasello, Akshat Shrivastava, Daniel Lazar, Po-Chun Hsu et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

End-to-end spoken language understanding (SLU) predicts intent directly from audio using a single model. It promises to improve the performance of assistant systems by leveraging acoustic information lost in the intermediate textual representation and preventing cascading errors from Automatic Speech Recognition (ASR). Further, having one unified model has efficiency advantages when deploying assistant systems on-device. However, the limited number of public audio datasets with semantic parse labels hinders the research progress in this area. In this paper, we release the Spoken Task-Oriented semantic Parsing (STOP) dataset, the largest and most complex SLU dataset to be publicly available. Additionally, we define low-resource splits to establish a benchmark for improving SLU when limited labeled data is available. Furthermore, in addition to the human-recorded audio, we are releasing a TTS-generated version to benchmark the performance for low-resource domain adaptation of end-to-end SLU systems. Initial experimentation show end-to-end SLU models performing slightly worse than their cascaded counterparts, which we hope encourages future work in this direction.

</details>

### [On the Prediction Network Architecture in RNN-T for ASR](2206.14618.md)
**Dario Albesano, Jesús Andrés-Ferrer, Nicola Ferri, Puming Zhan** · 2022-06-29

<details>
<summary>Abstract</summary>

RNN-T models have gained popularity in the literature and in commercial systems because of their competitiveness and capability of operating in online streaming mode. In this work, we conduct an extensive study comparing several prediction network architectures for both monotonic and original RNN-T models. We compare 4 types of prediction networks based on a common state-of-the-art Conformer encoder and report results obtained on Librispeech and an internal medical conversation data set. Our study covers both offline batch-mode and online streaming scenarios. In contrast to some previous works, our results show that Transformer does not always outperform LSTM when used as prediction network along with Conformer encoder. Inspired by our scoreboard, we propose a new simple prediction network architecture, N-Concat, that outperforms the others in our on-line streaming benchmark. Transformer and n-gram reduced architectures perform very similarly yet with some important distinct behaviour in terms of previous context. Overall we obtained up to 4.1 % relative WER improvement compared to our LSTM baseline, while reducing prediction network parameters by nearly an order of magnitude (8.4 times).

</details>

### [Self-Adaptive Multilingual ASR Rescoring with Language Identification and Unified Language Model](s2:dd8b6d162afb475bd44fbad52772f597d42699fd.md)
**Zhuo Gong, D. Saito, Longfei Yang, T. Shinozaki et al.** · 2022-06-28

<details>
<summary>Abstract</summary>

Language Models (LM) can be used in automatic speech recognition (ASR) rescoring to select the hypothesis with the fewest errors. While in multilingual ASR, multiple LMs might be used based on language identification (LID) given by the multilingual ASR outputs. However, in the traditional shallow fusion method, a static LM weight is determined by a development set. This static weight might not fulfill the situations of all languages in test data. And for multiple LMs, different weight needs to be searched for each LM. Instead, A unified multilingual LM will receive a LID token at the beginning of its auto-regressive predicting to decide which language to decode, so that merely one weight is necessary for LM rescoring. Then, we propose a multilingual ASR rescoring method which dynamically tunes the LM weight during decoding to optimize the balance between the end-to-end (E2E) multilingual ASR model and the LM according to the LM’s entropy and logits score as model confidence metrics. With this method, resources for search the best hyperparameter LM weight can also be saved. The experiments are mainly conducted on Common voice and Voxforge corpora. The results show that this method can reach the performance of the best static LM weight and even defeat it in several languages with no hyperparameter to be tuned and nearly zero overhead.

</details>

### [Challenges and Opportunities in Multi-device Speech Processing](2206.15432.md)
**Gregory Ciccarelli, Jarred Barber, Arun Nair, Israel Cohen et al.** · 2022-06-27

<details>
<summary>Abstract</summary>

We review current solutions and technical challenges for automatic speech recognition, keyword spotting, device arbitration, speech enhancement, and source localization in multidevice home environments to provide context for the INTERSPEECH 2022 special session, "Challenges and opportunities for signal processing and machine learning for multiple smart devices". We also identify the datasets needed to support these research areas. Based on the review and our research experience in the multi-device domain, we conclude with an outlook on the future evolution

</details>

### [Wav2Vec-Aug: Improved self-supervised training with limited data](2206.13654.md)
**Anuroop Sriram, Michael Auli, Alexei Baevski** · 2022-06-27

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) of speech representations has received much attention over the last few years but most work has focused on languages and domains with an abundance of unlabeled data. However, for many languages there is a shortage even in the unlabeled data which limits the effectiveness of SSL. In this work, we focus on the problem of applying SSL to domains with limited available data by leveraging data augmentation for Wav2Vec 2.0 pretraining. Further, we propose improvements to each component of the model which result in a combined relative word error rate (WER) improvement of up to 13% compared to Wav2Vec 2.0 on Librispeech test-clean / other.

</details>

### [Improving the Training Recipe for a Robust Conformer-based Hybrid Model](2206.12955.md)
**Mohammad Zeineldeen, Jingjing Xu, Christoph Lüscher, Ralf Schlüter et al.** · 2022-06-26

<details>
<summary>Abstract</summary>

Speaker adaptation is important to build robust automatic speech recognition (ASR) systems. In this work, we investigate various methods for speaker adaptive training (SAT) based on feature-space approaches for a conformer-based acoustic model (AM) on the Switchboard 300h dataset. We propose a method, called Weighted-Simple-Add, which adds weighted speaker information vectors to the input of the multi-head self-attention module of the conformer AM. Using this method for SAT, we achieve 3.5% and 4.5% relative improvement in terms of WER on the CallHome part of Hub5'00 and Hub5'01 respectively. Moreover, we build on top of our previous work where we proposed a novel and competitive training recipe for a conformer-based hybrid AM. We extend and improve this recipe where we achieve 11% relative improvement in terms of word-error-rate (WER) on Switchboard 300h Hub5'00 dataset. We also make this recipe efficient by reducing the total number of parameters by 34% relative.

</details>

### [On Comparison of Encoders for Attention based End to End Speech Recognition in Standalone and Rescoring Mode](2206.12829.md)
**Raviraj Joshi, Subodh Kumar** · 2022-06-26

<details>
<summary>Abstract</summary>

The streaming automatic speech recognition (ASR) models are more popular and suitable for voice-based applications. However, non-streaming models provide better performance as they look at the entire audio context. To leverage the benefits of the non-streaming model in streaming applications like voice search, it is commonly used in second pass re-scoring mode. The candidate hypothesis generated using steaming models is re-scored using a non-streaming model. In this work, we evaluate the non-streaming attention-based end-to-end ASR models on the Flipkart voice search task in both standalone and re-scoring modes. These models are based on Listen-Attend-Spell (LAS) encoder-decoder architecture. We experiment with different encoder variations based on LSTM, Transformer, and Conformer. We compare the latency requirements of these models along with their performance. Overall we show that the Transformer model offers acceptable WER with the lowest latency requirements. We report a relative WER improvement of around 16% with the second pass LAS re-scoring with latency overhead under 5ms. We also highlight the importance of CNN front-end with Transformer architecture to achieve comparable word error rates (WER). Moreover, we observe that in the second pass re-scoring mode all the encoders provide similar benefits whereas the difference in performance is prominent in standalone text generation mode.

</details>

### [Low-resource Accent Classification in Geographically-proximate Settings: A Forensic and Sociophonetics Perspective](2206.12759.md)
**Qingcheng Zeng, Dading Chong, Peilin Zhou, Jie Yang** · 2022-06-26

<details>
<summary>Abstract</summary>

Accented speech recognition and accent classification are relatively under-explored research areas in speech technology. Recently, deep learning-based methods and Transformer-based pretrained models have achieved superb performances in both areas. However, most accent classification tasks focused on classifying different kinds of English accents and little attention was paid to geographically-proximate accent classification, especially under a low-resource setting where forensic speech science tasks usually encounter. In this paper, we explored three main accent modelling methods combined with two different classifiers based on 105 speaker recordings retrieved from five urban varieties in Northern England. Although speech representations generated from pretrained models generally have better performances in downstream classification, traditional methods like Mel Frequency Cepstral Coefficients (MFCCs) and formant measurements are equipped with specific strengths. These results suggest that in forensic phonetics scenario where data are relatively scarce, a simple modelling method and classifier could be competitive with state-of-the-art pretrained speech models as feature extractors, which could enhance a sooner estimation for the accent information in practices. Besides, our findings also cross-validated a new methodology in quantifying sociophonetic changes.

</details>

### [TEVR: Improving Speech Recognition by Token Entropy Variance Reduction](2206.12693.md)
**Hajo Nils Krabbenhöft, Erhardt Barth** · 2022-06-25

<details>
<summary>Abstract</summary>

This paper presents TEVR, a speech recognition model designed to minimize the variation in token entropy w.r.t. to the language model. This takes advantage of the fact that if the language model will reliably and accurately predict a token anyway, then the acoustic model doesn't need to be accurate in recognizing it. We train German ASR models with 900 million parameters and show that on CommonVoice German, TEVR scores a very competitive 3.64% word error rate, which outperforms the best reported results by a relative 16.89% reduction in word error rate. We hope that releasing our fully trained speech recognition pipeline to the community will lead to privacy-preserving offline virtual assistants in the future.

</details>

### [Distilling a Pretrained Language Model to a Multilingual ASR Model](2206.12638.md)
**Kwanghee Choi, Hyung-Min Park** · 2022-06-25

<details>
<summary>Abstract</summary>

Multilingual speech data often suffer from long-tailed language distribution, resulting in performance degradation. However, multilingual text data is much easier to obtain, yielding a more useful general language model. Hence, we are motivated to distill the rich knowledge embedded inside a well-trained teacher text model to the student speech model. We propose a novel method called the Distilling a Language model to a Speech model (Distill-L2S), which aligns the latent representations of two different modalities. The subtle differences are handled by the shrinking mechanism, nearest-neighbor interpolation, and a learnable linear projection layer. We demonstrate the effectiveness of our distillation method by applying it to the multilingual automatic speech recognition (ASR) task. We distill the transformer-based cross-lingual language model (InfoXLM) while fine-tuning the large-scale multilingual ASR model (XLSR-wav2vec 2.0) for each language. We show the superiority of our method on 20 low-resource languages of the CommonVoice dataset with less than 100 hours of speech data.

</details>

### [PoCaP Corpus: A Multimodal Dataset for Smart Operating Room Speech Assistant using Interventional Radiology Workflow Analysis](2206.12320.md)
**Kubilay Can Demir, Matthias May, Axel Schmid, Michael Uder et al.** · 2022-06-24

<details>
<summary>Abstract</summary>

This paper presents a new multimodal interventional radiology dataset, called PoCaP (Port Catheter Placement) Corpus. This corpus consists of speech and audio signals in German, X-ray images, and system commands collected from 31 PoCaP interventions by six surgeons with average duration of 81.4 $\pm$ 41.0 minutes. The corpus aims to provide a resource for developing a smart speech assistant in operating rooms. In particular, it may be used to develop a speech controlled system that enables surgeons to control the operation parameters such as C-arm movements and table positions. In order to record the dataset, we acquired consent by the institutional review board and workers council in the University Hospital Erlangen and by the patients for data privacy. We describe the recording set-up, data structure, workflow and preprocessing steps, and report the first PoCaP Corpus speech recognition analysis results with 11.52 $\%$ word error rate using pretrained models. The findings suggest that the data has the potential to build a robust command recognition system and will allow the development of a novel intervention support systems using speech and image processing in the medical domain.

</details>

### [Confidence Score Based Conformer Speaker Adaptation for Speech Recognition](2206.12045.md)
**Jiajun Deng, Xurong Xie, Tianzi Wang, Mingyu Cui et al.** · 2022-06-24

<details>
<summary>Abstract</summary>

A key challenge for automatic speech recognition (ASR) systems is to model the speaker level variability. In this paper, compact speaker dependent learning hidden unit contributions (LHUC) are used to facilitate both speaker adaptive training (SAT) and test time unsupervised speaker adaptation for state-of-the-art Conformer based end-to-end ASR systems. The sensitivity during adaptation to supervision error rate is reduced using confidence score based selection of the more "trustworthy" subset of speaker specific data. A confidence estimation module is used to smooth the over-confident Conformer decoder output probabilities before serving as confidence scores. The increased data sparsity due to speaker level data selection is addressed using Bayesian estimation of LHUC parameters. Experiments on the 300-hour Switchboard corpus suggest that the proposed LHUC-SAT Conformer with confidence score based test time unsupervised adaptation outperformed the baseline speaker independent and i-vector adapted Conformer systems by up to 1.0%, 1.0%, and 1.2% absolute (9.0%, 7.9%, and 8.9% relative) word error rate (WER) reductions on the NIST Hub5'00, RT02, and RT03 evaluation sets respectively. Consistent performance improvements were retained after external Transformer and LSTM language models were used for rescoring.

</details>

### [Predicting within and across language phoneme recognition performance of self-supervised learning speech pre-trained models](2206.12489.md)
**Hang Ji, Tanvina Patel, Odette Scharenborg** · 2022-06-24

<details>
<summary>Abstract</summary>

In this work, we analyzed and compared speech representations extracted from different frozen self-supervised learning (SSL) speech pre-trained models on their ability to capture articulatory features (AF) information and their subsequent prediction of phone recognition performance for within and across language scenarios. Specifically, we compared CPC, wav2vec 2.0, and HuBert. First, frame-level AF probing tasks were implemented. Subsequently, phone-level end-to-end ASR systems for phoneme recognition tasks were implemented, and the performance on the frame-level AF probing task and the phone accuracy were correlated. Compared to the conventional speech representation MFCC, all SSL pre-trained speech representations captured more AF information, and achieved better phoneme recognition performance within and across languages, with HuBert performing best. The frame-level AF probing task is a good predictor of phoneme recognition performance, showing the importance of capturing AF information in the speech representations. Compared with MFCC, in the within-language scenario, the performance of these SSL speech pre-trained models on AF probing tasks achieved a maximum relative increase of 34.4%, and it resulted in the lowest PER of 10.2%. In the cross-language scenario, the maximum relative increase of 26.7% also resulted in the lowest PER of 23.0%.

</details>

### [Pruned RNN-T for fast, memory-efficient ASR training](2206.13236.md)
**Fangjun Kuang, Liyong Guo, Wei Kang, Long Lin et al.** · 2022-06-23

<details>
<summary>Abstract</summary>

The RNN-Transducer (RNN-T) framework for speech recognition has been growing in popularity, particularly for deployed real-time ASR systems, because it combines high accuracy with naturally streaming recognition. One of the drawbacks of RNN-T is that its loss function is relatively slow to compute, and can use a lot of memory. Excessive GPU memory usage can make it impractical to use RNN-T loss in cases where the vocabulary size is large: for example, for Chinese character-based ASR. We introduce a method for faster and more memory-efficient RNN-T loss computation. We first obtain pruning bounds for the RNN-T recursion using a simple joiner network that is linear in the encoder and decoder embeddings; we can evaluate this without using much memory. We then use those pruning bounds to evaluate the full, non-linear joiner network.

</details>

### [Towards Green ASR: Lossless 4-bit Quantization of a Hybrid TDNN System on the 300-hr Switchboard Corpus](2206.11643.md)
**Junhao Xu, Shoukang Hu, Xunying Liu, Helen Meng** · 2022-06-23

<details>
<summary>Abstract</summary>

State of the art time automatic speech recognition (ASR) systems are becoming increasingly complex and expensive for practical applications. This paper presents the development of a high performance and low-footprint 4-bit quantized LF-MMI trained factored time delay neural networks (TDNNs) based ASR system on the 300-hr Switchboard corpus. A key feature of the overall system design is to account for the fine-grained, varying performance sensitivity at different model components to quantization errors. To this end, a set of neural architectural compression and mixed precision quantization approaches were used to facilitate hidden layer level auto-configuration of optimal factored TDNN weight matrix subspace dimensionality and quantization bit-widths. The proposed techniques were also used to produce 2-bit mixed precision quantized Transformer language models. Experiments conducted on the Switchboard data suggest that the proposed neural architectural compression and mixed precision quantization techniques consistently outperform the uniform precision quantised baseline systems of comparable bit-widths in terms of word error rate (WER). An overall "lossless" compression ratio of 13.6 was obtained over the baseline full precision system including both the TDNN and Transformer components while incurring no statistically significant WER increase.

</details>

### [Two-pass Decoding and Cross-adaptation Based System Combination of End-to-end Conformer and Hybrid TDNN ASR Systems](2206.11596.md)
**Mingyu Cui, Jiajun Deng, Shoukang Hu, Xurong Xie et al.** · 2022-06-23

<details>
<summary>Abstract</summary>

Fundamental modelling differences between hybrid and end-to-end (E2E) automatic speech recognition (ASR) systems create large diversity and complementarity among them. This paper investigates multi-pass rescoring and cross adaptation based system combination approaches for hybrid TDNN and Conformer E2E ASR systems. In multi-pass rescoring, state-of-the-art hybrid LF-MMI trained CNN-TDNN system featuring speed perturbation, SpecAugment and Bayesian learning hidden unit contributions (LHUC) speaker adaptation was used to produce initial N-best outputs before being rescored by the speaker adapted Conformer system using a 2-way cross system score interpolation. In cross adaptation, the hybrid CNN-TDNN system was adapted to the 1-best output of the Conformer system or vice versa. Experiments on the 300-hour Switchboard corpus suggest that the combined systems derived using either of the two system combination approaches outperformed the individual systems. The best combined system obtained using multi-pass rescoring produced statistically significant word error rate (WER) reductions of 2.5% to 3.9% absolute (22.5% to 28.9% relative) over the stand alone Conformer system on the NIST Hub5'00, Rt03 and Rt02 evaluation data.

</details>

### [Answer Fast: Accelerating BERT on the Tensor Streaming Processor](2206.11062.md)
**Ibrahim Ahmed, Sahil Parmar, Matthew Boyd, Michael Beidler et al.** · 2022-06-22

<details>
<summary>Abstract</summary>

Transformers have become a predominant machine learning workload, they are not only the de-facto standard for natural language processing tasks, but they are also being deployed in other domains such as vision and speech recognition. Many of the transformer-based applications are real-time systems such as machine translation and web search. These real time systems often come with strict end-to-end inference latency requirements. Unfortunately, while the majority of the transformer computation comes from matrix multiplications, transformers also include several non-linear components that tend to become the bottleneck during an inference. In this work, we accelerate the inference of BERT models on the tensor streaming processor. By carefully fusing all the nonlinear components with the matrix multiplication components, we are able to efficiently utilize the on-chip matrix multiplication units resulting in a deterministic tail latency of 130 $μ$s for a batch-1 inference through BERT-base, which is 6X faster than the current state-of-the-art.

</details>

### [A Systematic Comparison of Phonetic Aware Techniques for Speech Enhancement](2206.11000.md)
**Or Tal, Moshe Mandel, Felix Kreuk, Yossi Adi** · 2022-06-22

<details>
<summary>Abstract</summary>

Speech enhancement has seen great improvement in recent years using end-to-end neural networks. However, most models are agnostic to the spoken phonetic content. Recently, several studies suggested phonetic-aware speech enhancement, mostly using perceptual supervision. Yet, injecting phonetic features during model optimization can take additional forms (e.g., model conditioning). In this paper, we conduct a systematic comparison between different methods of incorporating phonetic information in a speech enhancement model. By conducting a series of controlled experiments, we observe the influence of different phonetic content models as well as various feature-injection techniques on enhancement performance, considering both causal and non-causal models. Specifically, we evaluate three settings for injecting phonetic information, namely: i) feature conditioning; ii) perceptual supervision; and iii) regularization. Phonetic features are obtained using an intermediate layer of either a supervised pre-trained Automatic Speech Recognition (ASR) model or by using a pre-trained Self-Supervised Learning (SSL) model. We further observe the effect of choosing different embedding layers on performance, considering both manual and learned configurations. Results suggest that using a SSL model as phonetic features outperforms the ASR one in most cases. Interestingly, the conditioning setting performs best among the evaluated configurations.

</details>

### [Supervision-Guided Codebooks for Masked Prediction in Speech Pre-training](2206.10125.md)
**Chengyi Wang, Yiming Wang, Yu Wu, Sanyuan Chen et al.** · 2022-06-21

<details>
<summary>Abstract</summary>

Recently, masked prediction pre-training has seen remarkable progress in self-supervised learning (SSL) for speech recognition. It usually requires a codebook obtained in an unsupervised way, making it less accurate and difficult to interpret. We propose two supervision-guided codebook generation approaches to improve automatic speech recognition (ASR) performance and also the pre-training efficiency, either through decoding with a hybrid ASR system to generate phoneme-level alignments (named PBERT), or performing clustering on the supervised speech features extracted from an end-to-end CTC model (named CTC clustering). Both the hybrid and CTC models are trained on the same small amount of labeled speech as used in fine-tuning. Experiments demonstrate significant superiority of our methods to various SSL and self-training baselines, with up to 17.0% relative WER reduction. Our pre-trained models also show good transferability in a non-ASR speech task.

</details>

### [Boosting Cross-Domain Speech Recognition with Self-Supervision](2206.09783.md)
**Han Zhu, Gaofeng Cheng, Jindong Wang, Wenxin Hou et al.** · 2022-06-20

<details>
<summary>Abstract</summary>

The cross-domain performance of automatic speech recognition (ASR) could be severely hampered due to the mismatch between training and testing distributions. Since the target domain usually lacks labeled data, and domain shifts exist at acoustic and linguistic levels, it is challenging to perform unsupervised domain adaptation (UDA) for ASR. Previous work has shown that self-supervised learning (SSL) or pseudo-labeling (PL) is effective in UDA by exploiting the self-supervisions of unlabeled data. However, these self-supervisions also face performance degradation in mismatched domain distributions, which previous work fails to address. This work presents a systematic UDA framework to fully utilize the unlabeled data with self-supervision in the pre-training and fine-tuning paradigm. On the one hand, we apply continued pre-training and data replay techniques to mitigate the domain mismatch of the SSL pre-trained model. On the other hand, we propose a domain-adaptive fine-tuning approach based on the PL technique with three unique modifications: Firstly, we design a dual-branch PL method to decrease the sensitivity to the erroneous pseudo-labels; Secondly, we devise an uncertainty-aware confidence filtering strategy to improve pseudo-label correctness; Thirdly, we introduce a two-step PL approach to incorporate target domain linguistic knowledge, thus generating more accurate target domain pseudo-labels. Experimental results on various cross-domain scenarios demonstrate that the proposed approach effectively boosts the cross-domain performance and significantly outperforms previous approaches.

</details>

### [Transfer Learning for Robust Low-Resource Children's Speech ASR with Transformers and Source-Filter Warping](2206.09396.md)
**Jenthe Thienpondt, Kris Demuynck** · 2022-06-19

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems are known to exhibit difficulties when transcribing children's speech. This can mainly be attributed to the absence of large children's speech corpora to train robust ASR models and the resulting domain mismatch when decoding children's speech with systems trained on adult data. In this paper, we propose multiple enhancements to alleviate these issues. First, we propose a data augmentation technique based on the source-filter model of speech to close the domain gap between adult and children's speech. This enables us to leverage the data availability of adult speech corpora by making these samples perceptually similar to children's speech. Second, using this augmentation strategy, we apply transfer learning on a Transformer model pre-trained on adult data. This model follows the recently introduced XLS-R architecture, a wav2vec 2.0 model pre-trained on several cross-lingual adult speech corpora to learn general and robust acoustic frame-level representations. Adopting this model for the ASR task using adult data augmented with the proposed source-filter warping strategy and a limited amount of in-domain children's speech significantly outperforms previous state-of-the-art results on the PF-STAR British English Children's Speech corpus with a 4.86% WER on the official test set.

</details>

### [Developing a Speech Recognition System for Recognizing Tonal Speech Signals Using a Convolutional Neural Network](s2:3f083ec3128c2ddfcfe7ec609c104d27c3847d33.md)
**Sakshi Dua, Sethuraman Sambath Kumar, Y. Albagory, Rajakumar Ramalingam et al.** · 2022-06-19

<details>
<summary>Abstract</summary>

Deep learning-based machine learning models have shown significant results in speech recognition and numerous vision-related tasks. The performance of the present speech-to-text model relies upon the hyperparameters used in this research work. In this research work, it is shown that convolutional neural networks (CNNs) can model raw and tonal speech signals. Their performance is on par with existing recognition systems. This study extends the role of the CNN-based approach to robust and uncommon speech signals (tonal) using its own designed database for target research. The main objective of this research work was to develop a speech-to-text recognition system to recognize the tonal speech signals of Gurbani hymns using a CNN. Further, the CNN model, with six layers of 2DConv, 2DMax Pooling, and 256 dense layer units (Google’s TensorFlow service) was also used in this work, as well as Praat for speech segmentation. Feature extraction was enforced using the MFCC feature extraction technique, which extracts standard speech features and features of background music as well. Our study reveals that the CNN-based method for identifying tonal speech sentences and adding instrumental knowledge performs better than the existing and conventional approaches. The experimental results demonstrate the significant performance of the present CNN architecture by providing an 89.15% accuracy rate and a 10.56% WER for continuous and extensive vocabulary sentences of speech signals with different tones.

</details>

### [Detecting Adversarial Examples in Batches -- a geometrical approach](2206.08738.md)
**Danush Kumar Venkatesh, Peter Steinbach** · 2022-06-17

<details>
<summary>Abstract</summary>

Many deep learning methods have successfully solved complex tasks in computer vision and speech recognition applications. Nonetheless, the robustness of these models has been found to be vulnerable to perturbed inputs or adversarial examples, which are imperceptible to the human eye, but lead the model to erroneous output decisions. In this study, we adapt and introduce two geometric metrics, density and coverage, and evaluate their use in detecting adversarial samples in batches of unseen data. We empirically study these metrics using MNIST and two real-world biomedical datasets from MedMNIST, subjected to two different adversarial attacks. Our experiments show promising results for both metrics to detect adversarial examples. We believe that his work can lay the ground for further study on these metrics' use in deployed machine learning systems to monitor for possible attacks by adversarial examples or related pathologies such as dataset shift.

</details>

### [Paraformer: Fast and Accurate Parallel Transformer for Non-autoregressive End-to-End Speech Recognition](2206.08317.md)
**Zhifu Gao, Shiliang Zhang, Ian McLoughlin, Zhijie Yan** · 2022-06-16

<details>
<summary>Abstract</summary>

Transformers have recently dominated the ASR field. Although able to yield good performance, they involve an autoregressive (AR) decoder to generate tokens one by one, which is computationally inefficient. To speed up inference, non-autoregressive (NAR) methods, e.g. single-step NAR, were designed, to enable parallel generation. However, due to an independence assumption within the output tokens, performance of single-step NAR is inferior to that of AR models, especially with a large-scale corpus. There are two challenges to improving single-step NAR: Firstly to accurately predict the number of output tokens and extract hidden variables; secondly, to enhance modeling of interdependence between output tokens. To tackle both challenges, we propose a fast and accurate parallel transformer, termed Paraformer. This utilizes a continuous integrate-and-fire based predictor to predict the number of tokens and generate hidden variables. A glancing language model (GLM) sampler then generates semantic embeddings to enhance the NAR decoder's ability to model context interdependence. Finally, we design a strategy to generate negative samples for minimum word error rate training to further improve performance. Experiments using the public AISHELL-1, AISHELL-2 benchmark, and an industrial-level 20,000 hour task demonstrate that the proposed Paraformer can attain comparable performance to the state-of-the-art AR transformer, with more than 10x speedup.

</details>

### [Censer: Curriculum Semi-supervised Learning for Speech Recognition Based on Self-supervised Pre-training](2206.08189.md)
**Bowen Zhang, Songjun Cao, Xiaoming Zhang, Yike Zhang et al.** · 2022-06-16

<details>
<summary>Abstract</summary>

Recent studies have shown that the benefits provided by self-supervised pre-training and self-training (pseudo-labeling) are complementary. Semi-supervised fine-tuning strategies under the pre-training framework, however, remain insufficiently studied. Besides, modern semi-supervised speech recognition algorithms either treat unlabeled data indiscriminately or filter out noisy samples with a confidence threshold. The dissimilarities among different unlabeled data are often ignored. In this paper, we propose Censer, a semi-supervised speech recognition algorithm based on self-supervised pre-training to maximize the utilization of unlabeled data. The pre-training stage of Censer adopts wav2vec2.0 and the fine-tuning stage employs an improved semi-supervised learning algorithm from slimIPL, which leverages unlabeled data progressively according to their pseudo labels' qualities. We also incorporate a temporal pseudo label pool and an exponential moving average to control the pseudo labels' update frequency and to avoid model divergence. Experimental results on Libri-Light and LibriSpeech datasets manifest our proposed method achieves better performance compared to existing approaches while being more unified.

</details>

### [A CTC Triggered Siamese Network with Spatial-Temporal Dropout for Speech Recognition](2206.08031.md)
**Yingying Gao, Junlan Feng, Tianrui Wang, Chao Deng et al.** · 2022-06-16

<details>
<summary>Abstract</summary>

Siamese networks have shown effective results in unsupervised visual representation learning. These models are designed to learn an invariant representation of two augmentations for one input by maximizing their similarity. In this paper, we propose an effective Siamese network to improve the robustness of End-to-End automatic speech recognition (ASR). We introduce spatial-temporal dropout to support a more violent disturbance for Siamese-ASR framework. Besides, we also relax the similarity regularization to maximize the similarities of distributions on the frames that connectionist temporal classification (CTC) spikes occur rather than on all of them. The efficiency of the proposed architecture is evaluated on two benchmarks, AISHELL-1 and Librispeech, resulting in 7.13% and 6.59% relative character error rate (CER) and word error rate (WER) reductions respectively. Analysis shows that our proposed approach brings a better uniformity for the trained model and enlarges the CTC spikes obviously.

</details>

### [DRAFT: A Novel Framework to Reduce Domain Shifting in Self-supervised Learning and Its Application to Children's ASR](2206.07931.md)
**Ruchao Fan, Abeer Alwan** · 2022-06-16

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) in the pretraining stage using un-annotated speech data has been successful in low-resource automatic speech recognition (ASR) tasks. However, models trained through SSL are biased to the pretraining data which is usually different from the data used in finetuning tasks, causing a domain shifting problem, and thus resulting in limited knowledge transfer. We propose a novel framework, domain responsible adaptation and finetuning (DRAFT), to reduce domain shifting in pretrained speech models through an additional adaptation stage. In DRAFT, residual adapters (RAs) are inserted in the pretrained model to learn domain-related information with the same SSL loss as the pretraining stage. Only RA parameters are updated during the adaptation stage. DRAFT is agnostic to the type of SSL method used and is evaluated with three widely used approaches: APC, Wav2vec2.0, and HuBERT. On two child ASR tasks (OGI and MyST databases), using SSL models trained with un-annotated adult speech data (Librispeech), relative WER improvements of up to 19.7% are observed when compared to the pretrained models without adaptation. Additional experiments examined the potential of cross knowledge transfer between the two datasets and the results are promising, showing a broader usage of the proposed DRAFT framework.

</details>

### [Adversarial Privacy Protection on Speech Enhancement](2206.08170.md)
**Mingyu Dong, Diqun Yan, Rangding Wang** · 2022-06-16

<details>
<summary>Abstract</summary>

Speech is easily leaked imperceptibly, such as being recorded by mobile phones in different situations. Private content in speech may be maliciously extracted through speech enhancement technology. Speech enhancement technology has developed rapidly along with deep neural networks (DNNs), but adversarial examples can cause DNNs to fail. In this work, we propose an adversarial method to degrade speech enhancement systems. Experimental results show that generated adversarial examples can erase most content information in original examples or replace it with target speech content through speech enhancement. The word error rate (WER) between an enhanced original example and enhanced adversarial example recognition result can reach 89.0%. WER of target attack between enhanced adversarial example and target example is low to 33.75% . Adversarial perturbation can bring the rate of change to the original example to more than 1.4430. This work can prevent the malicious extraction of speech.

</details>

### [AVATAR: Unconstrained Audiovisual Speech Recognition](2206.07684.md)
**Valentin Gabeur, Paul Hongsuck Seo, Arsha Nagrani, Chen Sun et al.** · 2022-06-15

<details>
<summary>Abstract</summary>

Audio-visual automatic speech recognition (AV-ASR) is an extension of ASR that incorporates visual cues, often from the movements of a speaker's mouth. Unlike works that simply focus on the lip motion, we investigate the contribution of entire visual frames (visual actions, objects, background etc.). This is particularly useful for unconstrained videos, where the speaker is not necessarily visible. To solve this task, we propose a new sequence-to-sequence AudioVisual ASR TrAnsformeR (AVATAR) which is trained end-to-end from spectrograms and full-frame RGB. To prevent the audio stream from dominating training, we propose different word-masking strategies, thereby encouraging our model to pay attention to the visual stream. We demonstrate the contribution of the visual modality on the How2 AV-ASR benchmark, especially in the presence of simulated noise, and show that our model outperforms all other prior work by a large margin. Finally, we also create a new, real-world test bed for AV-ASR called VisSpeech, which demonstrates the contribution of the visual modality under challenging audio conditions.

</details>

### [Transformer-based Automatic Speech Recognition of Formal and Colloquial Czech in MALACH Project](2206.07666.md)
**Jan Lehečka, Josef V. Psutka, Josef Psutka** · 2022-06-15

<details>
<summary>Abstract</summary>

Czech is a very specific language due to its large differences between the formal and the colloquial form of speech. While the formal (written) form is used mainly in official documents, literature, and public speeches, the colloquial (spoken) form is used widely among people in casual speeches. This gap introduces serious problems for ASR systems, especially when training or evaluating ASR models on datasets containing a lot of colloquial speech, such as the MALACH project. In this paper, we are addressing this problem in the light of a new paradigm in end-to-end ASR systems -- recently introduced self-supervised audio Transformers. Specifically, we are investigating the influence of colloquial speech on the performance of Wav2Vec 2.0 models and their ability to transcribe colloquial speech directly into formal transcripts. We are presenting results with both formal and colloquial forms in the training transcripts, language models, and evaluation transcripts.

</details>

### [Exploring Capabilities of Monolingual Audio Transformers using Large Datasets in Automatic Speech Recognition of Czech](2206.07627.md)
**Jan Lehečka, Jan Švec, Aleš Pražák, Josef V. Psutka** · 2022-06-15

<details>
<summary>Abstract</summary>

In this paper, we present our progress in pretraining Czech monolingual audio transformers from a large dataset containing more than 80 thousand hours of unlabeled speech, and subsequently fine-tuning the model on automatic speech recognition tasks using a combination of in-domain data and almost 6 thousand hours of out-of-domain transcribed speech. We are presenting a large palette of experiments with various fine-tuning setups evaluated on two public datasets (CommonVoice and VoxPopuli) and one extremely challenging dataset from the MALACH project. Our results show that monolingual Wav2Vec 2.0 models are robust ASR systems, which can take advantage of large labeled and unlabeled datasets and successfully compete with state-of-the-art LVCSR systems. Moreover, Wav2Vec models proved to be good zero-shot learners when no training data are available for the target ASR task.

</details>

### [The ZevoMOS entry to VoiceMOS Challenge 2022](2206.07448.md)
**Adriana Stan** · 2022-06-15

<details>
<summary>Abstract</summary>

This paper introduces the ZevoMOS entry to the main track of the VoiceMOS Challenge 2022. The ZevoMOS submission is based on a two-step finetuning of pretrained self-supervised learning (SSL) speech models. The first step uses a task of classifying natural versus synthetic speech, while the second step's task is to predict the MOS scores associated with each training sample. The results of the finetuning process are then combined with the confidence scores extracted from an automatic speech recognition model, as well as the raw embeddings of the training samples obtained from a wav2vec SSL speech model. The team id assigned to the ZevoMOS system within the VoiceMOS Challenge is T01. The submission was placed on the 14th place with respect to the system-level SRCC, and on the 9th place with respect to the utterance-level MSE. The paper also introduces additional evaluations of the intermediate results.

</details>

### [Residual Language Model for End-to-end Speech Recognition](2206.07430.md)
**Emiru Tsunoo, Yosuke Kashiwagi, Chaitanya Narisetty, Shinji Watanabe** · 2022-06-15

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition suffers from adaptation to unknown target domain speech despite being trained with a large amount of paired audio--text data. Recent studies estimate a linguistic bias of the model as the internal language model (LM). To effectively adapt to the target domain, the internal LM is subtracted from the posterior during inference and fused with an external target-domain LM. However, this fusion complicates the inference and the estimation of the internal LM may not always be accurate. In this paper, we propose a simple external LM fusion method for domain adaptation, which considers the internal LM estimation in its training. We directly model the residual factor of the external and internal LMs, namely the residual LM. To stably train the residual LM, we propose smoothing the estimated internal LM and optimizing it with a combination of cross-entropy and mean-squared-error losses, which consider the statistical behaviors of the internal LM in the target domain data. We experimentally confirmed that the proposed residual LM performs better than the internal LM estimation in most of the cross-domain and intra-domain scenarios.

</details>

### [Learning-Based Data Storage [Vision] (Technical Report)](2206.05778.md)
**Xiang Lian, Xiaofei Zhang** · 2022-06-12

<details>
<summary>Abstract</summary>

Deep neural network (DNN) and its variants have been extensively used for a wide spectrum of real applications such as image classification, face/speech recognition, fraud detection, and so on. In addition to many important machine learning tasks, as artificial networks emulating the way brain cells function, DNNs also show the capability of storing non-linear relationships between input and output data, which exhibits the potential of storing data via DNNs. We envision a new paradigm of data storage, "DNN-as-a-Database", where data are encoded in well-trained machine learning models. Compared with conventional data storage that directly records data in raw formats, learning-based structures (e.g., DNN) can implicitly encode data pairs of inputs and outputs and compute/materialize actual output data of different resolutions only if input data are provided. This new paradigm can greatly enhance the data security by allowing flexible data privacy settings on different levels, achieve low space consumption and fast computation with the acceleration of new hardware (e.g., Diffractive Neural Network and AI chips), and can be generalized to distributed DNN-based storage/computing. In this paper, we propose this novel concept of learning-based data storage, which utilizes a learning structure called learning-based memory unit (LMU), to store, organize, and retrieve data. As a case study, we use DNNs as the engine in the LMU, and study the data capacity and accuracy of the DNN-based data storage. Our preliminary experimental results show the feasibility of the learning-based data storage by achieving high (100%) accuracy of the DNN storage. We explore and design effective solutions to utilize the DNN-based data storage to manage and query relational tables. We discuss how to generalize our solutions to other data types (e.g., graphs) and environments such as distributed DNN storage/computing.

</details>

### [Investigation of Ensemble features of Self-Supervised Pretrained Models for Automatic Speech Recognition](2206.05518.md)
**A Arunkumar, Vrunda N Sukhadia, S. Umesh** · 2022-06-11

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) based models have been shown to generate powerful representations that can be used to improve the performance of downstream speech tasks. Several state-of-the-art SSL models are available, and each of these models optimizes a different loss which gives rise to the possibility of their features being complementary. This paper proposes using an ensemble of such SSL representations and models, which exploits the complementary nature of the features extracted by the various pretrained models. We hypothesize that this results in a richer feature representation and shows results for the ASR downstream task. To this end, we use three SSL models that have shown excellent results on ASR tasks, namely HuBERT, Wav2vec2.0, and WaveLM. We explore the ensemble of models fine-tuned for the ASR task and the ensemble of features using the embeddings obtained from the pre-trained models for a downstream ASR task. We get improved performance over individual models and pre-trained features using Librispeech(100h) and WSJ dataset for the downstream tasks.

</details>

### [Training Neural Networks using SAT solvers](2206.04833.md)
**Subham S. Sahoo** · 2022-06-10

<details>
<summary>Abstract</summary>

We propose an algorithm to explore the global optimization method, using SAT solvers, for training a neural net. Deep Neural Networks have achieved great feats in tasks like-image recognition, speech recognition, etc. Much of their success can be attributed to the gradient-based optimisation methods, which scale well to huge datasets while still giving solutions, better than any other existing methods. However, there exist learning problems like the parity function and the Fast Fourier Transform, where a neural network using gradient-based optimisation algorithm can not capture the underlying structure of the learning task properly. Thus, exploring global optimisation methods is of utmost interest as the gradient-based methods get stuck in local optima. In the experiments, we demonstrate the effectiveness of our algorithm against the ADAM optimiser in certain tasks like parity learning. However, in the case of image classification on the MNIST Dataset, the performance of our algorithm was less than satisfactory. We further discuss the role of the size of the training dataset and the hyper-parameter settings in keeping things scalable for a SAT solver.

</details>

### [Revisiting End-to-End Speech-to-Text Translation From Scratch](2206.04571.md)
**Biao Zhang, Barry Haddow, Rico Sennrich** · 2022-06-09

<details>
<summary>Abstract</summary>

End-to-end (E2E) speech-to-text translation (ST) often depends on pretraining its encoder and/or decoder using source transcripts via speech recognition or text translation tasks, without which translation performance drops substantially. However, transcripts are not always available, and how significant such pretraining is for E2E ST has rarely been studied in the literature. In this paper, we revisit this question and explore the extent to which the quality of E2E ST trained on speech-translation pairs alone can be improved. We reexamine several techniques proven beneficial to ST previously, and offer a set of best practices that biases a Transformer-based E2E ST system toward training from scratch. Besides, we propose parameterized distance penalty to facilitate the modeling of locality in the self-attention model for speech. On four benchmarks covering 23 languages, our experiments show that, without using any transcripts or pretraining, the proposed system reaches and even outperforms previous studies adopting pretraining, although the gap remains in (extremely) low-resource settings. Finally, we discuss neural acoustic feature modeling, where a neural model is designed to extract acoustic features from raw speech signals directly, with the goal to simplify inductive biases and add freedom to the model in describing speech. For the first time, we demonstrate its feasibility and show encouraging results on ST tasks.

</details>

### [Joint Encoder-Decoder Self-Supervised Pre-training for ASR](2206.04465.md)
**Arunkumar A, Umesh S** · 2022-06-09

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has shown tremendous success in various speech-related downstream tasks, including Automatic Speech Recognition (ASR). The output embeddings of the SSL model are treated as powerful short-time representations of the speech signal. However, in the ASR task, the main objective is to get the correct sequence of acoustic units, characters, or byte-pair encodings (BPEs). Usually, encoder-decoder architecture works exceptionally well for a sequence-to-sequence task like ASR. Therefore, in this paper, we propose a new paradigm that exploits the power of a decoder during self-supervised learning. We use Hidden Unit BERT (HuBERT) SSL framework to compute the conventional masked prediction loss for the encoder. In addition, we have introduced a decoder in the SSL framework and proposed a target preparation strategy for the decoder. Finally, we use a multitask SSL setup wherein we jointly optimize both the encoder and decoder losses. We hypothesize that the presence of a decoder in the SSL model helps it learn an acoustic unit-based language model, which might improve the performance of an ASR downstream task. We compare our proposed SSL model with HuBERT and show up to 25% relative improvement in performance on ASR by finetuning on various LibriSpeech subsets.

</details>

### [Context-based out-of-vocabulary word recovery for ASR systems in Indian languages](2206.04305.md)
**Arun Baby, Saranya Vinnaitherthan, Akhil Kerhalkar, Pranav Jawale et al.** · 2022-06-09

<details>
<summary>Abstract</summary>

Detecting and recovering out-of-vocabulary (OOV) words is always challenging for Automatic Speech Recognition (ASR) systems. Many existing methods focus on modeling OOV words by modifying acoustic and language models and integrating context words cleverly into models. To train such complex models, we need a large amount of data with context words, additional training time, and increased model size. However, after getting the ASR transcription to recover context-based OOV words, the post-processing method has not been explored much. In this work, we propose a post-processing technique to improve the performance of context-based OOV recovery. We created an acoustically boosted language model with a sub-graph made at phone level with an OOV words list. We proposed two methods to determine a suitable cost function to retrieve the OOV words based on the context. The cost function is defined based on phonetic and acoustic knowledge for matching and recovering the correct context words in the decode. The effectiveness of the proposed cost function is evaluated at both word-level and sentence-level. The evaluation results show that this approach can recover an average of 50% context-based OOV words across multiple categories.

</details>

### [LegoNN: Building Modular Encoder-Decoder Models](2206.03318.md)
**Siddharth Dalmia, Dmytro Okhonko, Mike Lewis, Sergey Edunov et al.** · 2022-06-07

<details>
<summary>Abstract</summary>

State-of-the-art encoder-decoder models (e.g. for machine translation (MT) or automatic speech recognition (ASR)) are constructed and trained end-to-end as an atomic unit. No component of the model can be (re-)used without the others, making it impossible to share parts, e.g. a high resourced decoder, across tasks. We describe LegoNN, a procedure for building encoder-decoder architectures in a way so that its parts can be applied to other tasks without the need for any fine-tuning. To achieve this reusability, the interface between encoder and decoder modules is grounded to a sequence of marginal distributions over a pre-defined discrete vocabulary. We present two approaches for ingesting these marginals; one is differentiable, allowing the flow of gradients across the entire network, and the other is gradient-isolating. To enable the portability of decoder modules between MT tasks for different source languages and across other tasks like ASR, we introduce a modality agnostic encoder which consists of a length control mechanism to dynamically adapt encoders' output lengths in order to match the expected input length range of pre-trained decoders. We present several experiments to demonstrate the effectiveness of LegoNN models: a trained language generation LegoNN decoder module from German-English (De-En) MT task can be reused without any fine-tuning for the Europarl English ASR and the Romanian-English (Ro-En) MT tasks, matching or beating the performance of baseline. After fine-tuning, LegoNN models improve the Ro-En MT task by 1.5 BLEU points and achieve 12.5% relative WER reduction on the Europarl ASR task. To show how the approach generalizes, we compose a LegoNN ASR model from three modules -- each has been learned within different end-to-end trained models on three different datasets -- achieving an overall WER reduction of 19.5%.

</details>

### [FedNST: Federated Noisy Student Training for Automatic Speech Recognition](2206.02797.md)
**Haaris Mehmood, Agnieszka Dobrowolska, Karthikeyan Saravanan, Mete Ozay** · 2022-06-06

<details>
<summary>Abstract</summary>

Federated Learning (FL) enables training state-of-the-art Automatic Speech Recognition (ASR) models on user devices (clients) in distributed systems, hence preventing transmission of raw user data to a central server. A key challenge facing practical adoption of FL for ASR is obtaining ground-truth labels on the clients. Existing approaches rely on clients to manually transcribe their speech, which is impractical for obtaining large training corpora. A promising alternative is using semi-/self-supervised learning approaches to leverage unlabelled user data. To this end, we propose FedNST, a novel method for training distributed ASR models using private and unlabelled user data. We explore various facets of FedNST, such as training models with different proportions of labelled and unlabelled data, and evaluate the proposed approach on 1173 simulated clients. Evaluating FedNST on LibriSpeech, where 960 hours of speech data is split equally into server (labelled) and client (unlabelled) data, showed a 22.5% relative word error rate reduction} (WERR) over a supervised baseline trained only on server data.

</details>

### [Variable-rate hierarchical CPC leads to acoustic unit discovery in speech](2206.02211.md)
**Santiago Cuervo, Adrian Łańcucki, Ricard Marxer, Paweł Rychlikowski et al.** · 2022-06-05

<details>
<summary>Abstract</summary>

The success of deep learning comes from its ability to capture the hierarchical structure of data by learning high-level representations defined in terms of low-level ones. In this paper we explore self-supervised learning of hierarchical representations of speech by applying multiple levels of Contrastive Predictive Coding (CPC). We observe that simply stacking two CPC models does not yield significant improvements over single-level architectures. Inspired by the fact that speech is often described as a sequence of discrete units unevenly distributed in time, we propose a model in which the output of a low-level CPC module is non-uniformly downsampled to directly minimize the loss of a high-level CPC module. The latter is designed to also enforce a prior of separability and discreteness in its representations by enforcing dissimilarity of successive high-level representations through focused negative sampling, and by quantization of the prediction targets. Accounting for the structure of the speech signal improves upon single-level CPC features and enhances the disentanglement of the learned representations, as measured by downstream speech recognition tasks, while resulting in a meaningful segmentation of the signal that closely resembles phone boundaries.

</details>

### [Lip-Listening: Mixing Senses to Understand Lips using Cross Modality Knowledge Distillation for Word-Based Models](2207.05692.md)
**Hadeel Mabrouk, Omar Abugabal, Nourhan Sakr, Hesham M. Eraqi** · 2022-06-05

<details>
<summary>Abstract</summary>

In this work, we propose a technique to transfer speech recognition capabilities from audio speech recognition systems to visual speech recognizers, where our goal is to utilize audio data during lipreading model training. Impressive progress in the domain of speech recognition has been exhibited by audio and audio-visual systems. Nevertheless, there is still much to be explored with regards to visual speech recognition systems due to the visual ambiguity of some phonemes. To this end, the development of visual speech recognition models is crucial given the instability of audio models. The main contributions of this work are i) building on recent state-of-the-art word-based lipreading models by integrating sequence-level and frame-level Knowledge Distillation (KD) to their systems; ii) leveraging audio data during training visual models, a feat which has not been utilized in prior word-based work; iii) proposing the Gaussian-shaped averaging in frame-level KD, as an efficient technique that aids the model in distilling knowledge at the sequence model encoder. This work proposes a novel and competitive architecture for lip-reading, as we demonstrate a noticeable improvement in performance, setting a new benchmark equals to 88.64% on the LRW dataset.

</details>

### [LAE: Language-Aware Encoder for Monolingual and Multilingual ASR](2206.02093.md)
**Jinchuan Tian, Jianwei Yu, Chunlei Zhang, Chao Weng et al.** · 2022-06-05

<details>
<summary>Abstract</summary>

Despite the rapid progress in automatic speech recognition (ASR) research, recognizing multilingual speech using a unified ASR system remains highly challenging. Previous works on multilingual speech recognition mainly focus on two directions: recognizing multiple monolingual speech or recognizing code-switched speech that uses different languages interchangeably within a single utterance. However, a pragmatic multilingual recognizer is expected to be compatible with both directions. In this work, a novel language-aware encoder (LAE) architecture is proposed to handle both situations by disentangling language-specific information and generating frame-level language-aware representations during encoding. In the LAE, the primary encoding is implemented by the shared block while the language-specific blocks are used to extract specific representations for each language. To learn language-specific information discriminatively, a language-aware training method is proposed to optimize the language-specific blocks in LAE. Experiments conducted on Mandarin-English code-switched speech suggest that the proposed LAE is capable of discriminating different languages in frame-level and shows superior performance on both monolingual and multilingual ASR tasks. With either a real-recorded or simulated code-switched dataset, the proposed LAE achieves statistically significant improvements on both CTC and neural transducer systems. Code is released

</details>

### [Pronunciation Dictionary-Free Multilingual Speech Synthesis by Combining Unsupervised and Supervised Phonetic Representations](2206.00951.md)
**Chang Liu, Zhen-Hua Ling, Ling-Hui Chen** · 2022-06-02

<details>
<summary>Abstract</summary>

This paper proposes a multilingual speech synthesis method which combines unsupervised phonetic representations (UPR) and supervised phonetic representations (SPR) to avoid reliance on the pronunciation dictionaries of target languages. In this method, a pretrained wav2vec 2.0 model is adopted to extract UPRs and a language-independent automatic speech recognition (LI-ASR) model is built with a connectionist temporal classification (CTC) loss to extract segment-level SPRs from the audio data of target languages. Then, an acoustic model is designed, which first predicts UPRs and SPRs from texts separately and then combines the predicted UPRs and SPRs to generate mel-spectrograms. The results of our experiments on six languages show that the proposed method outperformed the methods that directly predicted mel-spectrograms from character or phoneme sequences and the ablated models that utilized only UPRs or SPRs.

</details>

### [Squeezeformer: An Efficient Transformer for Automatic Speech Recognition](2206.00888.md)
**Sehoon Kim, Amir Gholami, Albert Shaw, Nicholas Lee et al.** · 2022-06-02

<details>
<summary>Abstract</summary>

The recently proposed Conformer model has become the de facto backbone model for various downstream speech tasks based on its hybrid attention-convolution architecture that captures both local and global features. However, through a series of systematic studies, we find that the Conformer architecture's design choices are not optimal. After re-examining the design choices for both the macro and micro-architecture of Conformer, we propose Squeezeformer which consistently outperforms the state-of-the-art ASR models under the same training schemes. In particular, for the macro-architecture, Squeezeformer incorporates (i) the Temporal U-Net structure which reduces the cost of the multi-head attention modules on long sequences, and (ii) a simpler block structure of multi-head attention or convolution modules followed up by feed-forward module instead of the Macaron structure proposed in Conformer. Furthermore, for the micro-architecture, Squeezeformer (i) simplifies the activations in the convolutional block, (ii) removes redundant Layer Normalization operations, and (iii) incorporates an efficient depthwise down-sampling layer to efficiently sub-sample the input signal. Squeezeformer achieves state-of-the-art results of 7.5%, 6.5%, and 6.0% word-error-rate (WER) on LibriSpeech test-other without external language models, which are 3.1%, 1.4%, and 0.6% better than Conformer-CTC with the same number of FLOPs. Our code is open-sourced and available online.

</details>

### [Adversarial synthesis based data-augmentation for code-switched spoken language identification](2205.15747.md)
**Parth Shastri, Chirag Patil, Poorval Wanere, Shrinivas Mahajan et al.** · 2022-05-30

<details>
<summary>Abstract</summary>

Spoken Language Identification (LID) is an important sub-task of Automatic Speech Recognition(ASR) that is used to classify the language(s) in an audio segment. Automatic LID plays an useful role in multilingual countries. In various countries, identifying a language becomes hard, due to the multilingual scenario where two or more than two languages are mixed together during conversation. Such phenomenon of speech is called as code-mixing or code-switching. This nature is followed not only in India but also in many Asian countries. Such code-mixed data is hard to find, which further reduces the capabilities of the spoken LID. Hence, this work primarily addresses this problem using data augmentation as a solution on the on the data scarcity of the code-switched class. This study focuses on Indic language code-mixed with English. Spoken LID is performed on Hindi, code-mixed with English. This research proposes Generative Adversarial Network (GAN) based data augmentation technique performed using Mel spectrograms for audio data. GANs have already been proven to be accurate in representing the real data distribution in the image domain. Proposed research exploits these capabilities of GANs in speech domains such as speech classification, automatic speech recognition, etc. GANs are trained to generate Mel spectrograms of the minority code-mixed class which are then used to augment data for the classifier. Utilizing GANs give an overall improvement on Unweighted Average Recall by an amount of 3.5% as compared to a Convolutional Recurrent Neural Network (CRNN) classifier used as the baseline reference.

</details>

### [Adaptive Activation Network For Low Resource Multilingual Speech Recognition](2205.14326.md)
**Jian Luo, Jianzong Wang, Ning Cheng, Zhenpeng Zheng et al.** · 2022-05-28

<details>
<summary>Abstract</summary>

Low resource automatic speech recognition (ASR) is a useful but thorny task, since deep learning ASR models usually need huge amounts of training data. The existing models mostly established a bottleneck (BN) layer by pre-training on a large source language, and transferring to the low resource target language. In this work, we introduced an adaptive activation network to the upper layers of ASR model, and applied different activation functions to different languages. We also proposed two approaches to train the model: (1) cross-lingual learning, replacing the activation function from source language to target language, (2) multilingual learning, jointly training the Connectionist Temporal Classification (CTC) loss of each language and the relevance of different languages. Our experiments on IARPA Babel datasets demonstrated that our approaches outperform the from-scratch training and traditional bottleneck feature based methods. In addition, combining the cross-lingual learning and multilingual learning together could further improve the performance of multilingual speech recognition.

</details>

### [Is Lip Region-of-Interest Sufficient for Lipreading?](2205.14295.md)
**Jing-Xuan Zhang, Gen-Shun Wan, Jia Pan** · 2022-05-28

<details>
<summary>Abstract</summary>

Lip region-of-interest (ROI) is conventionally used for visual input in the lipreading task. Few works have adopted the entire face as visual input because lip-excluded parts of the face are usually considered to be redundant and irrelevant to visual speech recognition. However, faces contain much more detailed information than lips, such as speakers' head pose, emotion, identity etc. We argue that such information might benefit visual speech recognition if a powerful feature extractor employing the entire face is trained. In this work, we propose to adopt the entire face for lipreading with self-supervised learning. AV-HuBERT, an audio-visual multi-modal self-supervised learning framework, was adopted in our experiments. Our experimental results showed that adopting the entire face achieved 16% relative word error rate (WER) reduction on the lipreading task, compared with the baseline method using lip as visual input. Without self-supervised pretraining, the model with face input achieved a higher WER than that using lip input in the case of limited training data (30 hours), while a slightly lower WER when using large amount of training data (433 hours).

</details>

### [Contrastive Siamese Network for Semi-supervised Speech Recognition](2205.14054.md)
**Soheil Khorram, Jaeyoung Kim, Anshuman Tripathi, Han Lu et al.** · 2022-05-27

<details>
<summary>Abstract</summary>

This paper introduces contrastive siamese (c-siam) network, an architecture for leveraging unlabeled acoustic data in speech recognition. c-siam is the first network that extracts high-level linguistic information from speech by matching outputs of two identical transformer encoders. It contains augmented and target branches which are trained by: (1) masking inputs and matching outputs with a contrastive loss, (2) incorporating a stop gradient operation on the target branch, (3) using an extra learnable transformation on the augmented branch, (4) introducing new temporal augment functions to prevent the shortcut learning problem. We use the Libri-light 60k unsupervised data and the LibriSpeech 100hrs/960hrs supervised data to compare c-siam and other best-performing systems. Our experiments show that c-siam provides 20% relative word error rate improvement over wav2vec baselines. A c-siam network with 450M parameters achieves competitive results compared to the state-of-the-art networks with 600M parameters.

</details>

### [Punctuation Restoration in Spanish Customer Support Transcripts using Transfer Learning](2205.13961.md)
**Xiliang Zhu, Shayna Gardiner, David Rossouw, Tere Roldán et al.** · 2022-05-27

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems typically produce unpunctuated transcripts that have poor readability. In addition, building a punctuation restoration system is challenging for low-resource languages, especially for domain-specific applications. In this paper, we propose a Spanish punctuation restoration system designed for a real-time customer support transcription service. To address the data sparsity of Spanish transcripts in the customer support domain, we introduce two transfer-learning-based strategies: 1) domain adaptation using out-of-domain Spanish text data; 2) cross-lingual transfer learning leveraging in-domain English transcript data. Our experiment results show that these strategies improve the accuracy of the Spanish punctuation restoration system.

</details>

### [Global Normalization for Streaming Speech Recognition in a Modular Framework](2205.13674.md)
**Ehsan Variani, Ke Wu, Michael Riley, David Rybach et al.** · 2022-05-26

<details>
<summary>Abstract</summary>

We introduce the Globally Normalized Autoregressive Transducer (GNAT) for addressing the label bias problem in streaming speech recognition. Our solution admits a tractable exact computation of the denominator for the sequence-level normalization. Through theoretical and empirical results, we demonstrate that by switching to a globally normalized model, the word error rate gap between streaming and non-streaming speech-recognition models can be greatly reduced (by more than 50\% on the Librispeech dataset). This model is developed in a modular framework which encompasses all the common neural speech recognition models. The modularity of this framework enables controlled comparison of modelling choices and creation of new models.

</details>

### [Contextual Adapters for Personalized Speech Recognition in Neural Transducers](2205.13660.md)
**Kanthashree Mysore Sathyendra, Thejaswi Muniyappa, Feng-Ju Chang, Jing Liu et al.** · 2022-05-26

<details>
<summary>Abstract</summary>

Personal rare word recognition in end-to-end Automatic Speech Recognition (E2E ASR) models is a challenge due to the lack of training data. A standard way to address this issue is with shallow fusion methods at inference time. However, due to their dependence on external language models and the deterministic approach to weight boosting, their performance is limited. In this paper, we propose training neural contextual adapters for personalization in neural transducer based ASR models. Our approach can not only bias towards user-defined words, but also has the flexibility to work with pretrained ASR models. Using an in-house dataset, we demonstrate that contextual adapters can be applied to any general purpose pretrained ASR model to improve personalization. Our method outperforms shallow fusion, while retaining functionality of the pretrained models by not altering any of the model weights. We further show that the adapter style training is superior to full-fine-tuning of the ASR models on datasets with user-defined content.

</details>

### [Joint Training of Speech Enhancement and Self-supervised Model for Noise-robust ASR](2205.13293.md)
**Qiu-Shi Zhu, Jie Zhang, Zi-Qiang Zhang, Li-Rong Dai** · 2022-05-26

<details>
<summary>Abstract</summary>

Speech enhancement (SE) is usually required as a front end to improve the speech quality in noisy environments, while the enhanced speech might not be optimal for automatic speech recognition (ASR) systems due to speech distortion. On the other hand, it was shown that self-supervised pre-training enables the utilization of a large amount of unlabeled noisy data, which is rather beneficial for the noise robustness of ASR. However, the potential of the (optimal) integration of SE and self-supervised pre-training still remains unclear. In order to find an appropriate combination and reduce the impact of speech distortion caused by SE, in this paper we therefore propose a joint pre-training approach for the SE module and the self-supervised model. First, in the pre-training phase the original noisy waveform or the waveform obtained by SE is fed into the self-supervised model to learn the contextual representation, where the quantified clean speech acts as the target. Second, we propose a dual-attention fusion method to fuse the features of noisy and enhanced speeches, which can compensate the information loss caused by separately using individual modules. Due to the flexible exploitation of clean/noisy/enhanced branches, the proposed method turns out to be a generalization of some existing noise-robust ASR models, e.g., enhanced wav2vec2.0. Finally, experimental results on both synthetic and real noisy datasets show that the proposed joint training approach can improve the ASR performance under various noisy settings, leading to a stronger noise robustness.

</details>

### [Semantic-preserved Communication System for Highly Efficient Speech Transmission](2205.12727.md)
**Tianxiao Han, Qianqian Yang, Zhiguo Shi, Shibo He et al.** · 2022-05-25

<details>
<summary>Abstract</summary>

Deep learning (DL) based semantic communication methods have been explored for the efficient transmission of images, text, and speech in recent years. In contrast to traditional wireless communication methods that focus on the transmission of abstract symbols, semantic communication approaches attempt to achieve better transmission efficiency by only sending the semantic-related information of the source data. In this paper, we consider semantic-oriented speech transmission which transmits only the semantic-relevant information over the channel for the speech recognition task, and a compact additional set of semantic-irrelevant information for the speech reconstruction task. We propose a novel end-to-end DL-based transceiver which extracts and encodes the semantic information from the input speech spectrums at the transmitter and outputs the corresponding transcriptions from the decoded semantic information at the receiver. For the speech to speech transmission, we further include a CTC alignment module that extracts a small number of additional semantic-irrelevant but speech-related information for the better reconstruction of the original speech signals at the receiver. The simulation results confirm that our proposed method outperforms current methods in terms of the accuracy of the predicted text for the speech to text transmission and the quality of the recovered speech signals for the speech to speech transmission, and significantly improves transmission efficiency. More specifically, the proposed method only sends 16% of the amount of the transmitted symbols required by the existing methods while achieving about 10% reduction in WER for the speech to text transmission. For the speech to speech transmission, it results in an even more remarkable improvement in terms of transmission efficiency with only 0.2% of the amount of the transmitted symbols required by the existing method.

</details>

### [Investigating Lexical Replacements for Arabic-English Code-Switched Data Augmentation](2205.12649.md)
**Injy Hamed, Nizar Habash, Slim Abdennadher, Ngoc Thang Vu** · 2022-05-25

<details>
<summary>Abstract</summary>

Data sparsity is a main problem hindering the development of code-switching (CS) NLP systems. In this paper, we investigate data augmentation techniques for synthesizing dialectal Arabic-English CS text. We perform lexical replacements using word-aligned parallel corpora where CS points are either randomly chosen or learnt using a sequence-to-sequence model. We compare these approaches against dictionary-based replacements. We assess the quality of the generated sentences through human evaluation and evaluate the effectiveness of data augmentation on machine translation (MT), automatic speech recognition (ASR), and speech translation (ST) tasks. Results show that using a predictive model results in more natural CS sentences compared to the random approach, as reported in human judgements. In the downstream tasks, despite the random approach generating more data, both approaches perform equally (outperforming dictionary-based replacements). Overall, data augmentation achieves 34% improvement in perplexity, 5.2% relative improvement on WER for ASR task, +4.0-5.1 BLEU points on MT task, and +2.1-2.2 BLEU points on ST over a baseline trained on available data without augmentation.

</details>

### [Heterogeneous Reservoir Computing Models for Persian Speech Recognition](2205.12594.md)
**Zohreh Ansari, Farzin Pourhoseini, Fatemeh Hadaeghi** · 2022-05-25

<details>
<summary>Abstract</summary>

Over the last decade, deep-learning methods have been gradually incorporated into conventional automatic speech recognition (ASR) frameworks to create acoustic, pronunciation, and language models. Although it led to significant improvements in ASRs' recognition accuracy, due to their hard constraints related to hardware requirements (e.g., computing power and memory usage), it is unclear if such approaches are the most computationally- and energy-efficient options for embedded ASR applications. Reservoir computing (RC) models (e.g., echo state networks (ESNs) and liquid state machines (LSMs)), on the other hand, have been proven inexpensive to train, have vastly fewer parameters, and are compatible with emergent hardware technologies. However, their performance in speech processing tasks is relatively inferior to that of the deep-learning-based models. To enhance the accuracy of the RC in ASR applications, we propose heterogeneous single and multi-layer ESNs to create non-linear transformations of the inputs that capture temporal context at different scales. To test our models, we performed a speech recognition task on the Farsdat Persian dataset. Since, to the best of our knowledge, standard RC has not yet been employed to conduct any Persian ASR tasks, we also trained conventional single-layer and deep ESNs to provide baselines for comparison. Besides, we compared the RC performance with a standard long-short-term memory (LSTM) model. Heterogeneous RC models (1) show improved performance to the standard RC models; (2) perform on par in terms of recognition accuracy with the LSTM, and (3) reduce the training time considerably.

</details>

### [An Investigation on Applying Acoustic Feature Conversion to ASR of Adult and Child Speech](2205.12477.md)
**Wei Liu, Jingyu Li, Tan Lee** · 2022-05-25

<details>
<summary>Abstract</summary>

The performance of child speech recognition is generally less satisfactory compared to adult speech due to limited amount of training data. Significant performance degradation is expected when applying an automatic speech recognition (ASR) system trained on adult speech to child speech directly, as a result of domain mismatch. The present study is focused on adult-to-child acoustic feature conversion to alleviate this mismatch. Different acoustic feature conversion approaches, including deep neural network based and signal processing based, are investigated and compared under a fair experimental setting, in which converted acoustic features from the same amount of labeled adult speech are used to train the ASR models from scratch. Experimental results reveal that not all of the conversion methods lead to ASR performance gain. Specifically, as a classic unsupervised domain adaptation method, the statistic matching does not show an effectiveness. A disentanglement-based auto-encoder (DAE) conversion framework is found to be useful and the approach of F0 normalization achieves the best performance. It is noted that the F0 distribution of converted features is an important attribute to reflect the conversion quality, while utilizing an adult-child deep classification model to make judgment is shown to be inappropriate.

</details>

### [Improving CTC-based ASR Models with Gated Interlayer Collaboration](2205.12462.md)
**Yuting Yang, Yuke Li, Binbin Du** · 2022-05-25

<details>
<summary>Abstract</summary>

The CTC-based automatic speech recognition (ASR) models without the external language model usually lack the capacity to model conditional dependencies and textual interactions. In this paper, we present a Gated Interlayer Collaboration (GIC) mechanism to improve the performance of CTC-based models, which introduces textual information into the model and thus relaxes the conditional independence assumption of CTC-based models. Specifically, we consider the weighted sum of token embeddings as the textual representation for each position, where the position-specific weights are the softmax probability distribution constructed via inter-layer auxiliary CTC losses. The textual representations are then fused with acoustic features by developing a gate unit. Experiments on AISHELL-1, TEDLIUM2, and AIDATATANG corpora show that the proposed method outperforms several strong baselines.

</details>

### [Adaptive multilingual speech recognition with pretrained models](2205.12304.md)
**Ngoc-Quan Pham, Alex Waibel, Jan Niehues** · 2022-05-24

<details>
<summary>Abstract</summary>

Multilingual speech recognition with supervised learning has achieved great results as reflected in recent research. With the development of pretraining methods on audio and text data, it is imperative to transfer the knowledge from unsupervised multilingual models to facilitate recognition, especially in many languages with limited data. Our work investigated the effectiveness of using two pretrained models for two modalities: wav2vec 2.0 for audio and MBART50 for text, together with the adaptive weight techniques to massively improve the recognition quality on the public datasets containing CommonVoice and Europarl. Overall, we noticed an 44% improvement over purely supervised learning, and more importantly, each technique provides a different reinforcement in different languages. We also explore other possibilities to potentially obtain the best model by slightly adding either depth or relative attention to the architecture.

</details>

### [DNNAbacus: Toward Accurate Computational Cost Prediction for Deep Neural Networks](2205.12095.md)
**Lu Bai, Weixing Ji, Qinyuan Li, Xilai Yao et al.** · 2022-05-24

<details>
<summary>Abstract</summary>

Deep learning is attracting interest across a variety of domains, including natural language processing, speech recognition, and computer vision. However, model training is time-consuming and requires huge computational resources. Existing works on the performance prediction of deep neural networks, which mostly focus on the training time prediction of a few models, rely on analytical models and result in high relative errors. %Optimizing task scheduling and reducing job failures in data centers are essential to improve resource utilization and reduce carbon emissions. This paper investigates the computational resource demands of 29 classical deep neural networks and builds accurate models for predicting computational costs. We first analyze the profiling results of typical networks and demonstrate that the computational resource demands of models with different inputs and hyperparameters are not obvious and intuitive. We then propose a lightweight prediction approach DNNAbacus with a novel network structural matrix for network representation. DNNAbacus can accurately predict both memory and time cost for PyTorch and TensorFlow models, which is also generalized to different hardware architectures and can have zero-shot capability for unseen networks. Our experimental results show that the mean relative error (MRE) is 0.9% with respect to time and 2.8% with respect to memory for 29 classic models, which is much lower than the state-of-the-art works.

</details>

### [Multi-Level Modeling Units for End-to-End Mandarin Speech Recognition](2205.11998.md)
**Yuting Yang, Binbin Du, Yuke Li** · 2022-05-24

<details>
<summary>Abstract</summary>

The choice of modeling units is crucial for automatic speech recognition (ASR) tasks. In mandarin scenarios, the Chinese characters represent meaning but are not directly related to the pronunciation. Thus only considering the writing of Chinese characters as modeling units is insufficient to capture speech features. In this paper, we present a novel method involves with multi-level modeling units, which integrates multi-level information for mandarin speech recognition. Specifically, the encoder block considers syllables as modeling units and the decoder block deals with character-level modeling units. To facilitate the incremental conversion from syllable features to character features, we design an auxiliary task that applies cross-entropy (CE) loss to intermediate decoder layers. During inference, the input feature sequences are converted into syllable sequences by the encoder block and then converted into Chinese characters by the decoder block. Experiments on the widely used AISHELL-1 corpus demonstrate that our method achieves promising results with CER of 4.1%/4.6% and 4.6%/5.2%, using the Conformer and the Transformer backbones respectively.

</details>

### [Training Efficient CNNS: Tweaking the Nuts and Bolts of Neural Networks for Lighter, Faster and Robust Models](2205.12050.md)
**Sabeesh Ethiraj, Bharath Kumar Bolla** · 2022-05-23

<details>
<summary>Abstract</summary>

Deep Learning has revolutionized the fields of computer vision, natural language understanding, speech recognition, information retrieval and more. Many techniques have evolved over the past decade that made models lighter, faster, and robust with better generalization. However, many deep learning practitioners persist with pre-trained models and architectures trained mostly on standard datasets such as Imagenet, MS-COCO, IMDB-Wiki Dataset, and Kinetics-700 and are either hesitant or unaware of redesigning the architecture from scratch that will lead to better performance. This scenario leads to inefficient models that are not suitable on various devices such as mobile, edge, and fog. In addition, these conventional training methods are of concern as they consume a lot of computing power. In this paper, we revisit various SOTA techniques that deal with architecture efficiency (Global Average Pooling, depth-wise convolutions & squeeze and excitation, Blurpool), learning rate (Cyclical Learning Rate), data augmentation (Mixup, Cutout), label manipulation (label smoothing), weight space manipulation (stochastic weight averaging), and optimizer (sharpness aware minimization). We demonstrate how an efficient deep convolution network can be built in a phased manner by sequentially reducing the number of training parameters and using the techniques mentioned above. We achieved a SOTA accuracy of 99.2% on MNIST data with just 1500 parameters and an accuracy of 86.01% with just over 140K parameters on the CIFAR-10 dataset.

</details>

### [Calibrate and Refine! A Novel and Agile Framework for ASR-error Robust Intent Detection](2205.11008.md)
**Peilin Zhou, Dading Chong, Helin Wang, Qingcheng Zeng** · 2022-05-23

<details>
<summary>Abstract</summary>

The past ten years have witnessed the rapid development of text-based intent detection, whose benchmark performances have already been taken to a remarkable level by deep learning techniques. However, automatic speech recognition (ASR) errors are inevitable in real-world applications due to the environment noise, unique speech patterns and etc, leading to sharp performance drop in state-of-the-art text-based intent detection models. Essentially, this phenomenon is caused by the semantic drift brought by ASR errors and most existing works tend to focus on designing new model structures to reduce its impact, which is at the expense of versatility and flexibility. Different from previous one-piece model, in this paper, we propose a novel and agile framework called CR-ID for ASR error robust intent detection with two plug-and-play modules, namely semantic drift calibration module (SDCM) and phonemic refinement module (PRM), which are both model-agnostic and thus could be easily integrated to any existing intent detection models without modifying their structures. Experimental results on SNIPS dataset show that, our proposed CR-ID framework achieves competitive performance and outperform all the baseline methods on ASR outputs, which verifies that CR-ID can effectively alleviate the semantic drift caused by ASR errors.

</details>

### [A Comprehensive Handwritten Paragraph Text Recognition System: LexiconNet](2205.11018.md)
**Lalita Kumari, Sukhdeep Singh, Vaibhav Varish Singh Rathore, Anuj Sharma** · 2022-05-23

<details>
<summary>Abstract</summary>

In this study, we have presented an efficient procedure using two state-of-the-art approaches from the literature of handwritten text recognition as Vertical Attention Network and Word Beam Search. The attention module is responsible for internal line segmentation that consequently processes a page in a line-by-line manner. At the decoding step, we have added a connectionist temporal classification-based word beam search decoder as a post-processing step. In this study, an end-to-end paragraph recognition system is presented with a lexicon decoder as a post-processing step. Our procedure reports state-of-the-art results on standard datasets. The reported character error rate is 3.24% on the IAM dataset with 27.19% improvement, 1.13% on RIMES with 40.83% improvement and 2.43% on the READ-16 dataset with 32.31% improvement from existing literature and the word error rate is 8.29% on IAM dataset with 43.02% improvement, 2.94% on RIMES dataset with 56.25% improvement and 7.35% on READ-2016 dataset with 47.27% improvement from the existing results. The character error rate and word error rate reported in this work surpass the results reported in the literature.

</details>

### [Hybrid RNN-T/Attention-Based Streaming ASR with Triggered Chunkwise Attention and Dual Internal Language Model Integration](s2:f8ae264ceca2cf737de71b1ba59083b9a31e9efc.md)
**Takafumi Moriya, Takanori Ashihara, Atsushi Ando, Hiroshi Sato et al.** · 2022-05-23

<details>
<summary>Abstract</summary>

In this paper we propose improvements to our recently proposed hybrid RNN-T/Attention architecture that includes a shared encoder followed by recurrent neural network-transducer (RNN-T) and triggered attention-based decoders (TAD). The use of triggered attention enables the attention-based decoder (AD) to operate in a streaming manner. When a trigger point is detected by RNN-T, TAD uses the context from the start-of-speech up to that trigger point to compute the attention weights. Consequently, the computation costs and the memory consumptions are quadratically increased with the duration of the utterances because all input features must be stored and used to re-compute the attention weights. In this paper, we use a short context from a few frames prior to each trigger point for attention weight computation resulting in reduced computation and memory costs. We call the proposed framework triggered chunkwise AD (TCAD). We also investigate the effectiveness of internal language model (ILM) estimation approach using both ILMs of RNN-T and TCAD heads for improving RNN-T performance. We confirm in experiments with public and private datasets covering various scenarios that TCAD achieves superior recognition performance while reducing computation costs compared to TAD.

</details>

### [DP-DWA: Dual-Path Dynamic Weight Attention Network With Streaming Dfsmn-San For Automatic Speech Recognition](s2:46fc4d6c21b16b897f6ce1c8188862dfb91d0a3f.md)
**Dongpeng Ma, Yiwen Wang, Liqiang He, Mingjie Jin et al.** · 2022-05-23

<details>
<summary>Abstract</summary>

In multi-channel far-field automatic speech recognition (ASR) scenarios, distortion is introduced when the speech signal is processed by the front end, which damages the recognition performance for the ASR tasks. In this paper, we propose a dual-path network for the far-field acoustic model, which uses voice processing (VP) signal and acoustic echo cancellation (AEC) signal as input. Specifically, we design a dynamic weight attention (DWA) module for combining two signals. Besides, we streamline our best deep feed-forward sequential memory network with self-attention (DFSMN-SAN) acoustic model for real-time requirements. Joint-training strategy is adopted to optimize the proposed approach. We find that with dual-path network, we can achieve a 54.5% relative improvement in character error rate (CER) on a 10,000-hour online conference task. In addition, our proposed method is not affected by the arrangement of different microphone arrays. We achieve a 23.56% relative improvement on a vehicle task, which has an array with two microphones.

</details>

### [Deep Learning for Visual Speech Analysis: A Survey](2205.10839.md)
**Changchong Sheng, Gangyao Kuang, Liang Bai, Chenping Hou et al.** · 2022-05-22

<details>
<summary>Abstract</summary>

Visual speech, referring to the visual domain of speech, has attracted increasing attention due to its wide applications, such as public security, medical treatment, military defense, and film entertainment. As a powerful AI strategy, deep learning techniques have extensively promoted the development of visual speech learning. Over the past five years, numerous deep learning based methods have been proposed to address various problems in this area, especially automatic visual speech recognition and generation. To push forward future research on visual speech, this paper aims to present a comprehensive review of recent progress in deep learning methods on visual speech analysis. We cover different aspects of visual speech, including fundamental problems, challenges, benchmark datasets, a taxonomy of existing methods, and state-of-the-art performance. Besides, we also identify gaps in current research and discuss inspiring future research directions.

</details>

### [Language Models with Image Descriptors are Strong Few-Shot Video-Language Learners](2205.10747.md)
**Zhenhailong Wang, Manling Li, Ruochen Xu, Luowei Zhou et al.** · 2022-05-22

<details>
<summary>Abstract</summary>

The goal of this work is to build flexible video-language models that can generalize to various video-to-text tasks from few examples, such as domain-specific captioning, question answering, and future event prediction. Existing few-shot video-language learners focus exclusively on the encoder, resulting in the absence of a video-to-text decoder to handle generative tasks. Video captioners have been pretrained on large-scale video-language datasets, but they rely heavily on finetuning and lack the ability to generate text for unseen tasks in a few-shot setting. We propose VidIL, a few-shot Video-language Learner via Image and Language models, which demonstrates strong performance on few-shot video-to-text tasks without the necessity of pretraining or finetuning on any video datasets. We use the image-language models to translate the video content into frame captions, object, attribute, and event phrases, and compose them into a temporal structure template. We then instruct a language model, with a prompt containing a few in-context examples, to generate a target output from the composed content. The flexibility of prompting allows the model to capture any form of text input, such as automatic speech recognition (ASR) transcripts. Our experiments demonstrate the power of language models in understanding videos on a wide variety of video-language tasks, including video captioning, video question answering, video caption retrieval, and video future event prediction. Especially, on video future event prediction, our few-shot model significantly outperforms state-of-the-art supervised models trained on large-scale video datasets. Code and resources are publicly available for research purposes at https://github.com/MikeWangWZHL/VidIL .

</details>

### [Self-Supervised Speech Representation Learning: A Review](2205.10643.md)
**Abdelrahman Mohamed, Hung-yi Lee, Lasse Borgholt, Jakob D. Havtorn et al.** · 2022-05-21

<details>
<summary>Abstract</summary>

Although supervised deep learning has revolutionized speech and audio processing, it has necessitated the building of specialist models for individual tasks and application scenarios. It is likewise difficult to apply this to dialects and languages for which only limited labeled data is available. Self-supervised representation learning methods promise a single universal model that would benefit a wide variety of tasks and domains. Such methods have shown success in natural language processing and computer vision domains, achieving new levels of performance while reducing the number of labels required for many downstream scenarios. Speech representation learning is experiencing similar progress in three main categories: generative, contrastive, and predictive methods. Other approaches rely on multi-modal data for pre-training, mixing text or visual data streams with speech. Although self-supervised speech representation is still a nascent research area, it is closely related to acoustic word embedding and learning with zero lexical resources, both of which have seen active research for many years. This review presents approaches for self-supervised speech representation learning and their connection to other research areas. Since many current methods focus solely on automatic speech recognition as a downstream task, we review recent efforts on benchmarking learned representations to extend the application beyond speech recognition.

</details>

### [NeuralEcho: A Self-Attentive Recurrent Neural Network For Unified Acoustic Echo Suppression And Speech Enhancement](2205.10401.md)
**Meng Yu, Yong Xu, Chunlei Zhang, Shi-Xiong Zhang et al.** · 2022-05-20

<details>
<summary>Abstract</summary>

Acoustic echo cancellation (AEC) plays an important role in the full-duplex speech communication as well as the front-end speech enhancement for recognition in the conditions when the loudspeaker plays back. In this paper, we present an all-deep-learning framework that implicitly estimates the second order statistics of echo/noise and target speech, and jointly solves echo and noise suppression through an attention based recurrent neural network. The proposed model outperforms the state-of-the-art joint echo cancellation and speech enhancement method F-T-LSTM in terms of objective speech quality metrics, speech recognition accuracy and model complexity. We show that this model can work with speaker embedding for better target speech enhancement and furthermore develop a branch for automatic gain control (AGC) task to form an all-in-one front-end speech enhancement system.

</details>

### [Set-based Meta-Interpolation for Few-Task Meta-Learning](2205.09990.md)
**Seanie Lee, Bruno Andreis, Kenji Kawaguchi, Juho Lee et al.** · 2022-05-20

<details>
<summary>Abstract</summary>

Meta-learning approaches enable machine learning systems to adapt to new tasks given few examples by leveraging knowledge from related tasks. However, a large number of meta-training tasks are still required for generalization to unseen tasks during meta-testing, which introduces a critical bottleneck for real-world problems that come with only few tasks, due to various reasons including the difficulty and cost of constructing tasks. Recently, several task augmentation methods have been proposed to tackle this issue using domain-specific knowledge to design augmentation techniques to densify the meta-training task distribution. However, such reliance on domain-specific knowledge renders these methods inapplicable to other domains. While Manifold Mixup based task augmentation methods are domain-agnostic, we empirically find them ineffective on non-image domains. To tackle these limitations, we propose a novel domain-agnostic task augmentation method, Meta-Interpolation, which utilizes expressive neural set functions to densify the meta-training task distribution using bilevel optimization. We empirically validate the efficacy of Meta-Interpolation on eight datasets spanning across various domains such as image classification, molecule property prediction, text classification and speech recognition. Experimentally, we show that Meta-Interpolation consistently outperforms all the relevant baselines. Theoretically, we prove that task interpolation with the set function regularizes the meta-learner to improve generalization.

</details>

### [Content-Context Factorized Representations for Automated Speech Recognition](2205.09872.md)
**David M. Chan, Shalini Ghosh** · 2022-05-19

<details>
<summary>Abstract</summary>

Deep neural networks have largely demonstrated their ability to perform automated speech recognition (ASR) by extracting meaningful features from input audio frames. Such features, however, may consist not only of information about the spoken language content, but also may contain information about unnecessary contexts such as background noise and sounds or speaker identity, accent, or protected attributes. Such information can directly harm generalization performance, by introducing spurious correlations between the spoken words and the context in which such words were spoken. In this work, we introduce an unsupervised, encoder-agnostic method for factoring speech-encoder representations into explicit content-encoding representations and spurious context-encoding representations. By doing so, we demonstrate improved performance on standard ASR benchmarks, as well as improved performance in both real-world and artificially noisy ASR scenarios.

</details>

### [Automatic Spoken Language Identification using a Time-Delay Neural Network](2205.09564.md)
**Benjamin Kepecs, Homayoon Beigi** · 2022-05-19

<details>
<summary>Abstract</summary>

Closed-set spoken language identification is the task of recognizing the language being spoken in a recorded audio clip from a set of known languages. In this study, a language identification system was built and trained to distinguish between Arabic, Spanish, French, and Turkish based on nothing more than recorded speech. A pre-existing multilingual dataset was used to train a series of acoustic models based on the Tedlium TDNN model to perform automatic speech recognition. The system was provided with a custom multilingual language model and a specialized pronunciation lexicon with language names prepended to phones. The trained model was used to generate phone alignments to test data from all four languages, and languages were predicted based on a voting scheme choosing the most common language prepend in an utterance. Accuracy was measured by comparing predicted languages to known languages, and was determined to be very high in identifying Spanish and Arabic, and somewhat lower in identifying Turkish and French.

</details>

### [Insights on Neural Representations for End-to-End Speech Recognition](2205.09456.md)
**Anna Ollerenshaw, Md Asif Jalal, Thomas Hain** · 2022-05-19

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) models aim to learn a generalised speech representation. However, there are limited tools available to understand the internal functions and the effect of hierarchical dependencies within the model architecture. It is crucial to understand the correlations between the layer-wise representations, to derive insights on the relationship between neural representations and performance. Previous investigations of network similarities using correlation analysis techniques have not been explored for End-to-End ASR models. This paper analyses and explores the internal dynamics between layers during training with CNN, LSTM and Transformer based approaches using Canonical correlation analysis (CCA) and centered kernel alignment (CKA) for the experiments. It was found that neural representations within CNN layers exhibit hierarchical correlation dependencies as layer depth increases but this is mostly limited to cases where neural representation correlates more closely. This behaviour is not observed in LSTM architecture, however there is a bottom-up pattern observed across the training process, while Transformer encoder layers exhibit irregular coefficiency correlation as neural depth increases. Altogether, these results provide new insights into the role that neural architectures have upon speech recognition performance. More specifically, these techniques can be used as indicators to build better performing speech recognition models.

</details>

### [Minimising Biasing Word Errors for Contextual ASR with the Tree-Constrained Pointer Generator](2205.09058.md)
**Guangzhi Sun, Chao Zhang, Philip C Woodland** · 2022-05-18

<details>
<summary>Abstract</summary>

Contextual knowledge is essential for reducing speech recognition errors on high-valued long-tail words. This paper proposes a novel tree-constrained pointer generator (TCPGen) component that enables end-to-end ASR models to bias towards a list of long-tail words obtained using external contextual information. With only a small overhead in memory use and computation cost, TCPGen can structure thousands of biasing words efficiently into a symbolic prefix-tree and creates a neural shortcut between the tree and the final ASR output to facilitate the recognition of the biasing words. To enhance TCPGen, we further propose a novel minimum biasing word error (MBWE) loss that directly optimises biasing word errors during training, along with a biasing-word-driven language model discounting (BLMD) method during the test. All contextual ASR systems were evaluated on the public Librispeech audiobook corpus and the data from the dialogue state tracking challenges (DSTC) with the biasing lists extracted from the dialogue-system ontology. Consistent word error rate (WER) reductions were achieved with TCPGen, which were particularly significant on the biasing words with around 40\% relative reductions in the recognition error rates. MBWE and BLMD further improved the effectiveness of TCPGen and achieved more significant WER reductions on the biasing words. TCPGen also achieved zero-shot learning of words not in the audio training set with large WER reductions on the out-of-vocabulary words in the biasing list.

</details>

### [Deploying self-supervised learning in the wild for hybrid automatic speech recognition](2205.08598.md)
**Mostafa Karimi, Changliang Liu, Kenichi Kumatani, Yao Qian et al.** · 2022-05-17

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) methods have proven to be very successful in automatic speech recognition (ASR). These great improvements have been reported mostly based on highly curated datasets such as LibriSpeech for non-streaming End-to-End ASR models. However, the pivotal characteristics of SSL is to be utilized for any untranscribed audio data. In this paper, we provide a full exploration on how to utilize uncurated audio data in SSL from data pre-processing to deploying an streaming hybrid ASR model. More specifically, we present (1) the effect of Audio Event Detection (AED) model in data pre-processing pipeline (2) analysis on choosing optimizer and learning rate scheduling (3) comparison of recently developed contrastive losses, (4) comparison of various pre-training strategies such as utilization of in-domain versus out-domain pre-training data, monolingual versus multilingual pre-training data, multi-head multilingual SSL versus single-head multilingual SSL and supervised pre-training versus SSL. The experimental results show that SSL pre-training with in-domain uncurated data can achieve better performance in comparison to all the alternative out-domain pre-training strategies.

</details>

### [SAMU-XLSR: Semantically-Aligned Multimodal Utterance-level Cross-Lingual Speech Representation](2205.08180.md)
**Sameer Khurana, Antoine Laurent, James Glass** · 2022-05-17

<details>
<summary>Abstract</summary>

We propose the SAMU-XLSR: Semantically-Aligned Multimodal Utterance-level Cross-Lingual Speech Representation learning framework. Unlike previous works on speech representation learning, which learns multilingual contextual speech embedding at the resolution of an acoustic frame (10-20ms), this work focuses on learning multimodal (speech-text) multilingual speech embedding at the resolution of a sentence (5-10s) such that the embedding vector space is semantically aligned across different languages. We combine state-of-the-art multilingual acoustic frame-level speech representation learning model XLS-R with the Language Agnostic BERT Sentence Embedding (LaBSE) model to create an utterance-level multimodal multilingual speech encoder SAMU-XLSR. Although we train SAMU-XLSR with only multilingual transcribed speech data, cross-lingual speech-text and speech-speech associations emerge in its learned representation space. To substantiate our claims, we use SAMU-XLSR speech encoder in combination with a pre-trained LaBSE text sentence encoder for cross-lingual speech-to-text translation retrieval, and SAMU-XLSR alone for cross-lingual speech-to-speech translation retrieval. We highlight these applications by performing several cross-lingual text and speech translation retrieval tasks across several datasets.

</details>

### [Pretraining Approaches for Spoken Language Recognition: TalTech Submission to the OLR 2021 Challenge](2205.07083.md)
**Tanel Alumäe, Kunnar Kukk** · 2022-05-14

<details>
<summary>Abstract</summary>

This paper investigates different pretraining approaches to spoken language identification. The paper is based on our submission to the Oriental Language Recognition 2021 Challenge. We participated in two tracks of the challenge: constrained and unconstrained language recognition. For the constrained track, we first trained a Conformer-based encoder-decoder model for multilingual automatic speech recognition (ASR), using the provided training data that had transcripts available. The shared encoder of the multilingual ASR model was then finetuned for the language identification task. For the unconstrained task, we relied on both externally available pretrained models as well as external data: the multilingual XLSR-53 wav2vec2.0 model was finetuned on the VoxLingua107 corpus for the language recognition task, and finally finetuned on the provided target language training data, augmented with CommonVoice data. Our primary metric $C_{\rm avg}$ values on the Test set are 0.0079 for the constrained task and 0.0119 for the unconstrained task which resulted in the second place in both rankings. In post-evaluation experiments, we study the amount of target language data needed for training an accurate backend model, the importance of multilingual pretraining data, and compare different models as finetuning starting points.

</details>

### [Improved Consistency Training for Semi-Supervised Sequence-to-Sequence ASR via Speech Chain Reconstruction and Self-Transcribing](2205.06963.md)
**Heli Qi, Sashi Novitasari, Sakriani Sakti, Satoshi Nakamura** · 2022-05-14

<details>
<summary>Abstract</summary>

Consistency regularization has recently been applied to semi-supervised sequence-to-sequence (S2S) automatic speech recognition (ASR). This principle encourages an ASR model to output similar predictions for the same input speech with different perturbations. The existing paradigm of semi-supervised S2S ASR utilizes SpecAugment as data augmentation and requires a static teacher model to produce pseudo transcripts for untranscribed speech. However, this paradigm fails to take full advantage of consistency regularization. First, the masking operations of SpecAugment may damage the linguistic contents of the speech, thus influencing the quality of pseudo labels. Second, S2S ASR requires both input speech and prefix tokens to make the next prediction. The static prefix tokens made by the offline teacher model cannot match dynamic pseudo labels during consistency training. In this work, we propose an improved consistency training paradigm of semi-supervised S2S ASR. We utilize speech chain reconstruction as the weak augmentation to generate high-quality pseudo labels. Moreover, we demonstrate that dynamic pseudo transcripts produced by the student ASR model benefit the consistency training. Experiments on LJSpeech and LibriSpeech corpora show that compared to supervised baselines, our improved paradigm achieves a 12.2% CER improvement in the single-speaker setting and 38.6% in the multi-speaker setting.

</details>

### [Personalized Adversarial Data Augmentation for Dysarthric and Elderly Speech Recognition](2205.06445.md)
**Zengrui Jin, Mengzhe Geng, Jiajun Deng, Tianzi Wang et al.** · 2022-05-13

<details>
<summary>Abstract</summary>

Despite the rapid progress of automatic speech recognition (ASR) technologies targeting normal speech, accurate recognition of dysarthric and elderly speech remains highly challenging tasks to date. It is difficult to collect large quantities of such data for ASR system development due to the mobility issues often found among these users. To this end, data augmentation techniques play a vital role. In contrast to existing data augmentation techniques only modifying the speaking rate or overall shape of spectral contour, fine-grained spectro-temporal differences between dysarthric, elderly and normal speech are modelled using a novel set of speaker dependent (SD) generative adversarial networks (GAN) based data augmentation approaches in this paper. These flexibly allow both: a) temporal or speed perturbed normal speech spectra to be modified and closer to those of an impaired speaker when parallel speech data is available; and b) for non-parallel data, the SVD decomposed normal speech spectral basis features to be transformed into those of a target elderly speaker before being re-composed with the temporal bases to produce the augmented data for state-of-the-art TDNN and Conformer ASR system training. Experiments are conducted on four tasks: the English UASpeech and TORGO dysarthric speech corpora; the English DementiaBank Pitt and Cantonese JCCOCC MoCA elderly speech datasets. The proposed GAN based data augmentation approaches consistently outperform the baseline speed perturbation method by up to 0.91% and 3.0% absolute (9.61% and 6.4% relative) WER reduction on the TORGO and DementiaBank data respectively. Consistent performance improvements are retained after applying LHUC based speaker adaptation.

</details>

### [End-to-End Multi-Person Audio/Visual Automatic Speech Recognition](2205.05586.md)
**Otavio Braga, Takaki Makino, Olivier Siohan, Hank Liao** · 2022-05-11

<details>
<summary>Abstract</summary>

Traditionally, audio-visual automatic speech recognition has been studied under the assumption that the speaking face on the visual signal is the face matching the audio. However, in a more realistic setting, when multiple faces are potentially on screen one needs to decide which face to feed to the A/V ASR system. The present work takes the recent progress of A/V ASR one step further and considers the scenario where multiple people are simultaneously on screen (multi-person A/V ASR). We propose a fully differentiable A/V ASR model that is able to handle multiple face tracks in a video. Instead of relying on two separate models for speaker face selection and audio-visual ASR on a single face track, we introduce an attention layer to the ASR encoder that is able to soft-select the appropriate face video track. Experiments carried out on an A/V system trained on over 30k hours of YouTube videos illustrate that the proposed approach can automatically select the proper face tracks with minor WER degradation compared to an oracle selection of the speaking face while still showing benefits of employing the visual signal instead of the audio alone.

</details>

### [A Closer Look at Audio-Visual Multi-Person Speech Recognition and Active Speaker Selection](2205.05684.md)
**Otavio Braga, Olivier Siohan** · 2022-05-11

<details>
<summary>Abstract</summary>

Audio-visual automatic speech recognition is a promising approach to robust ASR under noisy conditions. However, up until recently it had been traditionally studied in isolation assuming the video of a single speaking face matches the audio, and selecting the active speaker at inference time when multiple people are on screen was put aside as a separate problem. As an alternative, recent work has proposed to address the two problems simultaneously with an attention mechanism, baking the speaker selection problem directly into a fully differentiable model. One interesting finding was that the attention indirectly learns the association between the audio and the speaking face even though this correspondence is never explicitly provided at training time. In the present work we further investigate this connection and examine the interplay between the two problems. With experiments involving over 50 thousand hours of public YouTube videos as training data, we first evaluate the accuracy of the attention layer on an active speaker selection task. Secondly, we show under closer scrutiny that an end-to-end model performs at least as well as a considerably larger two-step system that utilizes a hard decision boundary under various noise conditions and number of parallel face tracks.

</details>

### [Best of Both Worlds: Multi-task Audio-Visual Automatic Speech Recognition and Active Speaker Detection](2205.05206.md)
**Otavio Braga, Olivier Siohan** · 2022-05-10

<details>
<summary>Abstract</summary>

Under noisy conditions, automatic speech recognition (ASR) can greatly benefit from the addition of visual signals coming from a video of the speaker's face. However, when multiple candidate speakers are visible this traditionally requires solving a separate problem, namely active speaker detection (ASD), which entails selecting at each moment in time which of the visible faces corresponds to the audio. Recent work has shown that we can solve both problems simultaneously by employing an attention mechanism over the competing video tracks of the speakers' faces, at the cost of sacrificing some accuracy on active speaker detection. This work closes this gap in active speaker detection accuracy by presenting a single model that can be jointly trained with a multi-task loss. By combining the two tasks during training we reduce the ASD classification accuracy by approximately 25%, while simultaneously improving the ASR performance when compared to the multi-person baseline trained exclusively for ASR.

</details>

### [Separator-Transducer-Segmenter: Streaming Recognition and Segmentation of Multi-party Speech](2205.05199.md)
**Ilya Sklyar, Anna Piunova, Christian Osendorfer** · 2022-05-10

<details>
<summary>Abstract</summary>

Streaming recognition and segmentation of multi-party conversations with overlapping speech is crucial for the next generation of voice assistant applications. In this work we address its challenges discovered in the previous work on multi-turn recurrent neural network transducer (MT-RNN-T) with a novel approach, separator-transducer-segmenter (STS), that enables tighter integration of speech separation, recognition and segmentation in a single model. First, we propose a new segmentation modeling strategy through start-of-turn and end-of-turn tokens that improves segmentation without recognition accuracy degradation. Second, we further improve both speech recognition and segmentation accuracy through an emission regularization method, FastEmit, and multi-task training with speech activity information as an additional training signal. Third, we experiment with end-of-turn emission latency penalty to improve end-point detection for each speaker turn. Finally, we establish a novel framework for segmentation analysis of multi-party conversations through emission latency metrics. With our best model, we report 4.6% abs. turn counting accuracy improvement and 17% rel. word error rate (WER) improvement on LibriCSS dataset compared to the previously published work.

</details>

### [Deep Learning Enabled Semantic Communications with Speech Recognition and Synthesis](2205.04603.md)
**Zhenzi Weng, Zhijin Qin, Xiaoming Tao, Chengkang Pan et al.** · 2022-05-09

<details>
<summary>Abstract</summary>

In this paper, we develop a deep learning based semantic communication system for speech transmission, named DeepSC-ST. We take the speech recognition and speech synthesis as the transmission tasks of the communication system, respectively. First, the speech recognition-related semantic features are extracted for transmission by a joint semantic-channel encoder and the text is recovered at the receiver based on the received semantic features, which significantly reduces the required amount of data transmission without performance degradation. Then, we perform speech synthesis at the receiver, which dedicates to re-generate the speech signals by feeding the recognized text and the speaker information into a neural network module. To enable the DeepSC-ST adaptive to dynamic channel environments, we identify a robust model to cope with different channel conditions. According to the simulation results, the proposed DeepSC-ST significantly outperforms conventional communication systems and existing DL-enabled communication systems, especially in the low signal-to-noise ratio (SNR) regime. A software demonstration is further developed as a proof-of-concept of the DeepSC-ST.

</details>

### [Speaker Reinforcement Using Target Source Extraction for Robust Automatic Speech Recognition](2205.04433.md)
**Catalin Zorila, Rama Doddipatla** · 2022-05-09

<details>
<summary>Abstract</summary>

Improving the accuracy of single-channel automatic speech recognition (ASR) in noisy conditions is challenging. Strong speech enhancement front-ends are available, however, they typically require that the ASR model is retrained to cope with the processing artifacts. In this paper we explore a speaker reinforcement strategy for improving recognition performance without retraining the acoustic model (AM). This is achieved by remixing the enhanced signal with the unprocessed input to alleviate the processing artifacts. We evaluate the proposed approach using a DNN speaker extraction based speech denoiser trained with a perceptually motivated loss function. Results show that (without AM retraining) our method yields about 23% and 25% relative accuracy gains compared with the unprocessed for the monoaural simulated and real CHiME-4 evaluation sets, respectively, and outperforms a state-of-the-art reference method.

</details>

### [Online Model Compression for Federated Learning with Large Models](2205.03494.md)
**Tien-Ju Yang, Yonghui Xiao, Giovanni Motta, Françoise Beaufays et al.** · 2022-05-06

<details>
<summary>Abstract</summary>

This paper addresses the challenges of training large neural network models under federated learning settings: high on-device memory usage and communication cost. The proposed Online Model Compression (OMC) provides a framework that stores model parameters in a compressed format and decompresses them only when needed. We use quantization as the compression method in this paper and propose three methods, (1) using per-variable transformation, (2) weight matrices only quantization, and (3) partial parameter quantization, to minimize the impact on model accuracy. According to our experiments on two recent neural networks for speech recognition and two different datasets, OMC can reduce memory usage and communication cost of model parameters by up to 59% while attaining comparable accuracy and training speed when compared with full-precision training.

</details>

### [A Conformer-based Waveform-domain Neural Acoustic Echo Canceller Optimized for ASR Accuracy](2205.03481.md)
**Sankaran Panchapagesan, Arun Narayanan, Turaj Zakizadeh Shabestary, Shuai Shao et al.** · 2022-05-06

<details>
<summary>Abstract</summary>

Acoustic Echo Cancellation (AEC) is essential for accurate recognition of queries spoken to a smart speaker that is playing out audio. Previous work has shown that a neural AEC model operating on log-mel spectral features (denoted "logmel" hereafter) can greatly improve Automatic Speech Recognition (ASR) accuracy when optimized with an auxiliary loss utilizing a pre-trained ASR model encoder. In this paper, we develop a conformer-based waveform-domain neural AEC model inspired by the "TasNet" architecture. The model is trained by jointly optimizing Negative Scale-Invariant SNR (SISNR) and ASR losses on a large speech dataset. On a realistic rerecorded test set, we find that cascading a linear adaptive AEC and a waveform-domain neural AEC is very effective, giving 56-59% word error rate (WER) reduction over the linear AEC alone. On this test set, the 1.6M parameter waveform-domain neural AEC also improves over a larger 6.5M parameter logmel-domain neural AEC model by 20-29% in easy to moderate conditions. By operating on smaller frames, the waveform neural model is able to perform better at smaller sizes and is better suited for applications where memory is limited.

</details>

### [Transformer-Based Multi-Aspect Multi-Granularity Non-Native English Speaker Pronunciation Assessment](2205.03432.md)
**Yuan Gong, Ziyi Chen, Iek-Heng Chu, Peng Chang et al.** · 2022-05-06

<details>
<summary>Abstract</summary>

Automatic pronunciation assessment is an important technology to help self-directed language learners. While pronunciation quality has multiple aspects including accuracy, fluency, completeness, and prosody, previous efforts typically only model one aspect (e.g., accuracy) at one granularity (e.g., at the phoneme-level). In this work, we explore modeling multi-aspect pronunciation assessment at multiple granularities. Specifically, we train a Goodness Of Pronunciation feature-based Transformer (GOPT) with multi-task learning. Experiments show that GOPT achieves the best results on speechocean762 with a public automatic speech recognition (ASR) acoustic model trained on Librispeech.

</details>

### [A Highly Adaptive Acoustic Model for Accurate Multi-Dialect Speech Recognition](2205.03027.md)
**Sanghyun Yoo, Inchul Song, Yoshua Bengio** · 2022-05-06

<details>
<summary>Abstract</summary>

Despite the success of deep learning in speech recognition, multi-dialect speech recognition remains a difficult problem. Although dialect-specific acoustic models are known to perform well in general, they are not easy to maintain when dialect-specific data is scarce and the number of dialects for each language is large. Therefore, a single unified acoustic model (AM) that generalizes well for many dialects has been in demand. In this paper, we propose a novel acoustic modeling technique for accurate multi-dialect speech recognition with a single AM. Our proposed AM is dynamically adapted based on both dialect information and its internal representation, which results in a highly adaptive AM for handling multiple dialects simultaneously. We also propose a simple but effective training method to deal with unseen dialects. The experimental results on large scale speech datasets show that the proposed AM outperforms all the previous ones, reducing word error rates (WERs) by 8.11% relative compared to a single all-dialects AM and by 7.31% relative compared to dialect-specific AMs.

</details>

### [Hearing voices at the National Library -- a speech corpus and acoustic model for the Swedish language](2205.03026.md)
**Martin Malmsten, Chris Haffenden, Love Börjeson** · 2022-05-06

<details>
<summary>Abstract</summary>

This paper explains our work in developing new acoustic models for automated speech recognition (ASR) at KBLab, the infrastructure for data-driven research at the National Library of Sweden (KB). We evaluate different approaches for a viable speech-to-text pipeline for audiovisual resources in Swedish, using the wav2vec 2.0 architecture in combination with speech corpuses created from KB's collections. These approaches include pretraining an acoustic model for Swedish from the ground up, and fine-tuning existing monolingual and multilingual models. The collections-based corpuses we use have been sampled from millions of hours of speech, with a conscious attempt to balance regional dialects to produce a more representative, and thus more democratic, model. The acoustic model this enabled, "VoxRex", outperforms existing models for Swedish ASR. We also evaluate combining this model with various pretrained language models, which further enhanced performance. We conclude by highlighting the potential of such technology for cultural heritage institutions with vast collections of previously unlabelled audiovisual data. Our models are released for further exploration and research here: https://huggingface.co/KBLab.

</details>

### [Cross-modal Contrastive Learning for Speech Translation](2205.02444.md)
**Rong Ye, Mingxuan Wang, Lei Li** · 2022-05-05

<details>
<summary>Abstract</summary>

How can we learn unified representations for spoken utterances and their written text? Learning similar representations for semantically similar speech and text is important for speech translation. To this end, we propose ConST, a cross-modal contrastive learning method for end-to-end speech-to-text translation. We evaluate ConST and a variety of previous baselines on a popular benchmark MuST-C. Experiments show that the proposed ConST consistently outperforms the previous methods on, and achieves an average BLEU of 29.4. The analysis further verifies that ConST indeed closes the representation gap of different modalities -- its learned representation improves the accuracy of cross-modal speech-text retrieval from 4% to 88%. Code and models are available at https://github.com/ReneeYe/ConST.

</details>

### [ON-TRAC Consortium Systems for the IWSLT 2022 Dialect and Low-resource Speech Translation Tasks](2205.01987.md)
**Marcely Zanon Boito, John Ortega, Hugo Riguidel, Antoine Laurent et al.** · 2022-05-04

<details>
<summary>Abstract</summary>

This paper describes the ON-TRAC Consortium translation systems developed for two challenge tracks featured in the Evaluation Campaign of IWSLT 2022: low-resource and dialect speech translation. For the Tunisian Arabic-English dataset (low-resource and dialect tracks), we build an end-to-end model as our joint primary submission, and compare it against cascaded models that leverage a large fine-tuned wav2vec 2.0 model for ASR. Our results show that in our settings pipeline approaches are still very competitive, and that with the use of transfer learning, they can outperform end-to-end models for speech translation (ST). For the Tamasheq-French dataset (low-resource track) our primary submission leverages intermediate representations from a wav2vec 2.0 model trained on 234 hours of Tamasheq audio, while our contrastive model uses a French phonetic transcription of the Tamasheq audio as input in a Conformer speech translation architecture jointly trained on automatic speech recognition, ST and machine translation losses. Our results highlight that self-supervised models trained on smaller sets of target data are more effective to low-resource end-to-end ST fine-tuning, compared to large off-the-shelf models. Results also illustrate that even approximate phonetic transcriptions can improve ST scores.

</details>

### [On monoaural speech enhancement for automatic recognition of real noisy speech using mixture invariant training](2205.01751.md)
**Jisi Zhang, Catalin Zorila, Rama Doddipatla, Jon Barker** · 2022-05-03

<details>
<summary>Abstract</summary>

In this paper, we explore an improved framework to train a monoaural neural enhancement model for robust speech recognition. The designed training framework extends the existing mixture invariant training criterion to exploit both unpaired clean speech and real noisy data. It is found that the unpaired clean speech is crucial to improve quality of separated speech from real noisy speech. The proposed method also performs remixing of processed and unprocessed signals to alleviate the processing artifacts. Experiments on the single-channel CHiME-3 real test sets show that the proposed method improves significantly in terms of speech recognition performance over the enhancement system trained either on the mismatched simulated data in a supervised fashion or on the matched real data in an unsupervised fashion. Between 16% and 39% relative WER reduction has been achieved by the proposed system compared to the unprocessed signal using end-to-end and hybrid acoustic models without retraining on distorted data.

</details>

### [Wav2Seq: Pre-training Speech-to-Text Encoder-Decoder Models Using Pseudo Languages](2205.01086.md)
**Felix Wu, Kwangyoun Kim, Shinji Watanabe, Kyu Han et al.** · 2022-05-02

<details>
<summary>Abstract</summary>

We introduce Wav2Seq, the first self-supervised approach to pre-train both parts of encoder-decoder models for speech data. We induce a pseudo language as a compact discrete representation, and formulate a self-supervised pseudo speech recognition task -- transcribing audio inputs into pseudo subword sequences. This process stands on its own, or can be applied as low-cost second-stage pre-training. We experiment with automatic speech recognition (ASR), spoken named entity recognition, and speech-to-text translation. We set new state-of-the-art results for end-to-end spoken named entity recognition, and show consistent improvements on 20 language pairs for speech-to-text translation, even when competing methods use additional text data for training. Finally, on ASR, our approach enables encoder-decoder methods to benefit from pre-training for all parts of the network, and shows comparable performance to highly optimized recent methods.

</details>

### [Bilingual End-to-End ASR with Byte-Level Subwords](2205.00485.md)
**Liuhui Deng, Roger Hsiao, Arnab Ghoshal** · 2022-05-01

<details>
<summary>Abstract</summary>

In this paper, we investigate how the output representation of an end-to-end neural network affects multilingual automatic speech recognition (ASR). We study different representations including character-level, byte-level, byte pair encoding (BPE), and byte-level byte pair encoding (BBPE) representations, and analyze their strengths and weaknesses. We focus on developing a single end-to-end model to support utterance-based bilingual ASR, where speakers do not alternate between two languages in a single utterance but may change languages across utterances. We conduct our experiments on English and Mandarin dictation tasks, and we find that BBPE with penalty schemes can improve utterance-based bilingual ASR performance by 2% to 5% relative even with smaller number of outputs and fewer parameters. We conclude with analysis that indicates directions for further improving multilingual ASR.

</details>

### [Improving Multimodal Speech Recognition by Data Augmentation and Speech Representations](2204.13206.md)
**Dan Oneata, Horia Cucu** · 2022-04-27

<details>
<summary>Abstract</summary>

Multimodal speech recognition aims to improve the performance of automatic speech recognition (ASR) systems by leveraging additional visual information that is usually associated to the audio input. While previous approaches make crucial use of strong visual representations, e.g. by finetuning pretrained image recognition networks, significantly less attention has been paid to its counterpart: the speech component. In this work, we investigate ways of improving the base speech recognition system by following similar techniques to the ones used for the visual encoder, namely, transferring representations and data augmentation. First, we show that starting from a pretrained ASR significantly improves the state-of-the-art performance; remarkably, even when building upon a strong unimodal system, we still find gains by including the visual modality. Second, we employ speech data augmentation techniques to encourage the multimodal system to attend to the visual stimuli. This technique replaces previously used word masking and comes with the benefits of being conceptually simpler and yielding consistent improvements in the multimodal setting. We provide empirical results on three multimodal datasets, including the newly introduced Localized Narratives.

</details>

### [Ultra Fast Speech Separation Model with Teacher Student Learning](2204.12777.md)
**Sanyuan Chen, Yu Wu, Zhuo Chen, Jian Wu et al.** · 2022-04-27

<details>
<summary>Abstract</summary>

Transformer has been successfully applied to speech separation recently with its strong long-dependency modeling capacity using a self-attention mechanism. However, Transformer tends to have heavy run-time costs due to the deep encoder layers, which hinders its deployment on edge devices. A small Transformer model with fewer encoder layers is preferred for computational efficiency, but it is prone to performance degradation. In this paper, an ultra fast speech separation Transformer model is proposed to achieve both better performance and efficiency with teacher student learning (T-S learning). We introduce layer-wise T-S learning and objective shifting mechanisms to guide the small student model to learn intermediate representations from the large teacher model. Compared with the small Transformer model trained from scratch, the proposed T-S learning method reduces the word error rate (WER) by more than 5% for both multi-channel and single-channel speech separation on LibriCSS dataset. Utilizing more unlabeled speech data, our ultra fast speech separation models achieve more than 10% relative WER reduction.

</details>

### [Automatic Speech Recognition (ASR) Systems for Children: A Systematic Literature Review](s2:4518b0e5e4aa52857d05724c63543583941aac7c.md)
**V. Bhardwaj, Mohamed Tahar, Ben Othman, Vinay Kukreja et al.** · 2022-04-27

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is one of the ways used to transform acoustic speech signals into text. Over the last few decades, an enormous amount of research work has been done in the research area of speech recognition (SR). However, most studies have focused on building ASR systems based on adult speech. The recognition of children’s speech was neglected for some time, which means that the field of children’s SR research is wide open. Children’s SR is a challenging task due to the large variations in children’s articulatory, acoustic, physical, and linguistic characteristics compared to adult speech. Thus, the field became a very attractive area of research and it is important to understand where the main center of attention is, and what are the most widely used methods for extracting acoustic features, various acoustic models, speech datasets, the SR toolkits used during the recognition process, and so on. ASR systems or interfaces are extensively used and integrated into various real-life applications, such as search engines, the healthcare industry, biometric analysis, car systems, the military, aids for people with disabilities, and mobile devices. A systematic literature review (SLR) is presented in this work by extracting the relevant information from 76 research papers published from 2009 to 2020 in the field of ASR for children. The objective of this review is to throw light on the trends of research in children’s speech recognition and analyze the potential of trending techniques to recognize children’s speech.

</details>

### [Mask scalar prediction for improving robust automatic speech recognition](2204.12092.md)
**Arun Narayanan, James Walker, Sankaran Panchapagesan, Nathan Howard et al.** · 2022-04-26

<details>
<summary>Abstract</summary>

Using neural network based acoustic frontends for improving robustness of streaming automatic speech recognition (ASR) systems is challenging because of the causality constraints and the resulting distortion that the frontend processing introduces in speech. Time-frequency masking based approaches have been shown to work well, but they need additional hyper-parameters to scale the mask to limit speech distortion. Such mask scalars are typically hand-tuned and chosen conservatively. In this work, we present a technique to predict mask scalars using an ASR-based loss in an end-to-end fashion, with minimal increase in the overall model size and complexity. We evaluate the approach on two robust ASR tasks: multichannel enhancement in the presence of speech and non-speech noise, and acoustic echo cancellation (AEC). Results show that the presented algorithm consistently improves word error rate (WER) without the need for any additional tuning over strong baselines that use hand-tuned hyper-parameters: up to 16% for multichannel enhancement in noisy conditions, and up to 7% for AEC.

</details>

### [Cleanformer: A multichannel array configuration-invariant neural enhancement frontend for ASR in smart speakers](2204.11933.md)
**Joseph Caroselli, Arun Narayanan, Nathan Howard, Tom O'Malley** · 2022-04-25

<details>
<summary>Abstract</summary>

This work introduces the Cleanformer, a streaming multichannel neural based enhancement frontend for automatic speech recognition (ASR). This model has a conformer-based architecture which takes as inputs a single channel each of raw and enhanced signals, and uses self-attention to derive a time-frequency mask. The enhanced input is generated by a multichannel adaptive noise cancellation algorithm known as Speech Cleaner, which makes use of noise context to derive its filter taps. The time-frequency mask is applied to the noisy input to produce enhanced output features for ASR. Detailed evaluations are presented with simulated and re-recorded datasets in speech-based and non-speech-based noise that show significant reduction in word error rate (WER) when using a large-scale state-of-the-art ASR model. It also will be shown to significantly outperform enhancement using a beamformer with ideal steering. The enhancement model is agnostic of the number of microphones and array configuration and, therefore, can be used with different microphone arrays without the need for retraining. It is demonstrated that performance improves with more microphones, up to 4, with each additional microphone providing a smaller marginal benefit. Specifically, for an SNR of -6dB, relative WER improvements of about 80\% are shown in both noise conditions.

</details>

### [Enable Deep Learning on Mobile Devices: Methods, Systems, and Applications](2204.11786.md)
**Han Cai, Ji Lin, Yujun Lin, Zhijian Liu et al.** · 2022-04-25

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have achieved unprecedented success in the field of artificial intelligence (AI), including computer vision, natural language processing and speech recognition. However, their superior performance comes at the considerable cost of computational complexity, which greatly hinders their applications in many resource-constrained devices, such as mobile phones and Internet of Things (IoT) devices. Therefore, methods and techniques that are able to lift the efficiency bottleneck while preserving the high accuracy of DNNs are in great demand in order to enable numerous edge AI applications. This paper provides an overview of efficient deep learning methods, systems and applications. We start from introducing popular model compression methods, including pruning, factorization, quantization as well as compact model design. To reduce the large design cost of these manual solutions, we discuss the AutoML framework for each of them, such as neural architecture search (NAS) and automated pruning and quantization. We then cover efficient on-device training to enable user customization based on the local data on mobile devices. Apart from general acceleration techniques, we also showcase several task-specific accelerations for point cloud, video and natural language processing by exploiting their spatial sparsity and temporal/token redundancy. Finally, to support all these algorithmic advancements, we introduce the efficient deep learning system design from both software and hardware perspectives.

</details>

### [Supervised Attention in Sequence-to-Sequence Models for Speech Recognition](2204.12308.md)
**Gene-Ping Yang, Hao Tang** · 2022-04-25

<details>
<summary>Abstract</summary>

Attention mechanism in sequence-to-sequence models is designed to model the alignments between acoustic features and output tokens in speech recognition. However, attention weights produced by models trained end to end do not always correspond well with actual alignments, and several studies have further argued that attention weights might not even correspond well with the relevance attribution of frames. Regardless, visual similarity between attention weights and alignments is widely used during training as an indicator of the models quality. In this paper, we treat the correspondence between attention weights and alignments as a learning problem by imposing a supervised attention loss. Experiments have shown significant improved performance, suggesting that learning the alignments well during training critically determines the performance of sequence-to-sequence models.

</details>

### [Understanding Audio Features via Trainable Basis Functions](2204.11437.md)
**Kwan Yee Heung, Kin Wai Cheuk, Dorien Herremans** · 2022-04-25

<details>
<summary>Abstract</summary>

In this paper we explore the possibility of maximizing the information represented in spectrograms by making the spectrogram basis functions trainable. We experiment with two different tasks, namely keyword spotting (KWS) and automatic speech recognition (ASR). For most neural network models, the architecture and hyperparameters are typically fine-tuned and optimized in experiments. Input features, however, are often treated as fixed. In the case of audio, signals can be mainly expressed in two main ways: raw waveforms (time-domain) or spectrograms (time-frequency-domain). In addition, different spectrogram types are often used and tailored to fit different applications. In our experiments, we allow for this tailoring directly as part of the network. Our experimental results show that using trainable basis functions can boost the accuracy of Keyword Spotting (KWS) by 14.2 percentage points, and lower the Phone Error Rate (PER) by 9.5 percentage points. Although models using trainable basis functions become less effective as the model complexity increases, the trained filter shapes could still provide us with insights on which frequency bins are important for that specific task. From our experiments, we can conclude that trainable basis functions are a useful tool to boost the performance when the model complexity is limited.

</details>

### [On-demand compute reduction with stochastic wav2vec 2.0](2204.11934.md)
**Apoorv Vyas, Wei-Ning Hsu, Michael Auli, Alexei Baevski** · 2022-04-25

<details>
<summary>Abstract</summary>

Squeeze and Efficient Wav2vec (SEW) is a recently proposed architecture that squeezes the input to the transformer encoder for compute efficient pre-training and inference with wav2vec 2.0 (W2V2) models. In this work, we propose stochastic compression for on-demand compute reduction for W2V2 models. As opposed to using a fixed squeeze factor, we sample it uniformly during training. We further introduce query and key-value pooling mechanisms that can be applied to each transformer layer for further compression. Our results for models pre-trained on 960h Librispeech dataset and fine-tuned on 10h of transcribed data show that using the same stochastic model, we get a smooth trade-off between word error rate (WER) and inference time with only marginal WER degradation compared to the W2V2 and SEW models trained for a specific setting. We further show that we can fine-tune the same stochastically pre-trained model to a specific configuration to recover the WER difference resulting in significant computational savings on pre-training models from scratch.

</details>

### [Improved far-field speech recognition using Joint Variational Autoencoder](2204.11286.md)
**Shashi Kumar, Shakti P. Rath, Abhishek Pandey** · 2022-04-24

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems suffer considerably when source speech is corrupted with noise or room impulse responses (RIR). Typically, speech enhancement is applied in both mismatched and matched scenario training and testing. In matched setting, acoustic model (AM) is trained on dereverberated far-field features while in mismatched setting, AM is fixed. In recent past, mapping speech features from far-field to close-talk using denoising autoencoder (DA) has been explored. In this paper, we focus on matched scenario training and show that the proposed joint VAE based mapping achieves a significant improvement over DA. Specifically, we observe an absolute improvement of 2.5% in word error rate (WER) compared to DA based enhancement and 3.96% compared to AM trained directly on far-field filterbank features.

</details>

### [E2E Segmenter: Joint Segmenting and Decoding for Long-Form ASR](2204.10749.md)
**W. Ronny Huang, Shuo-yiin Chang, David Rybach, Rohit Prabhavalkar et al.** · 2022-04-22

<details>
<summary>Abstract</summary>

Improving the performance of end-to-end ASR models on long utterances ranging from minutes to hours in length is an ongoing challenge in speech recognition. A common solution is to segment the audio in advance using a separate voice activity detector (VAD) that decides segment boundary locations based purely on acoustic speech/non-speech information. VAD segmenters, however, may be sub-optimal for real-world speech where, e.g., a complete sentence that should be taken as a whole may contain hesitations in the middle ("set an alarm for... 5 o'clock"). We propose to replace the VAD with an end-to-end ASR model capable of predicting segment boundaries in a streaming fashion, allowing the segmentation decision to be conditioned not only on better acoustic features but also on semantic features from the decoded text with negligible extra computation. In experiments on real world long-form audio (YouTube) with lengths of up to 30 minutes, we demonstrate 8.5% relative WER improvement and 250 ms reduction in median end-of-segment latency compared to the VAD segmenter baseline on a state-of-the-art Conformer RNN-T model.

</details>

### [Efficient Training of Neural Transducer for Speech Recognition](2204.10586.md)
**Wei Zhou, Wilfried Michel, Ralf Schlüter, Hermann Ney** · 2022-04-22

<details>
<summary>Abstract</summary>

As one of the most popular sequence-to-sequence modeling approaches for speech recognition, the RNN-Transducer has achieved evolving performance with more and more sophisticated neural network models of growing size and increasing training epochs. While strong computation resources seem to be the prerequisite of training superior models, we try to overcome it by carefully designing a more efficient training pipeline. In this work, we propose an efficient 3-stage progressive training pipeline to build highly-performing neural transducer models from scratch with very limited computation resources in a reasonable short time period. The effectiveness of each stage is experimentally verified on both Librispeech and Switchboard corpora. The proposed pipeline is able to train transducer models approaching state-of-the-art performance with a single GPU in just 2-3 weeks. Our best conformer transducer achieves 4.1% WER on Librispeech test-other with only 35 epochs of training.

</details>

### [Layer-wise Fast Adaptation for End-to-End Multi-Accent Speech Recognition](2204.09883.md)
**Xun Gong, Yizhou Lu, Zhikai Zhou, Yanmin Qian** · 2022-04-21

<details>
<summary>Abstract</summary>

Accent variability has posed a huge challenge to automatic speech recognition~(ASR) modeling. Although one-hot accent vector based adaptation systems are commonly used, they require prior knowledge about the target accent and cannot handle unseen accents. Furthermore, simply concatenating accent embeddings does not make good use of accent knowledge, which has limited improvements. In this work, we aim to tackle these problems with a novel layer-wise adaptation structure injected into the E2E ASR model encoder. The adapter layer encodes an arbitrary accent in the accent space and assists the ASR model in recognizing accented speech. Given an utterance, the adaptation structure extracts the corresponding accent information and transforms the input acoustic feature into an accent-related feature through the linear combination of all accent bases. We further explore the injection position of the adaptation layer, the number of accent bases, and different types of accent bases to achieve better accent adaptation. Experimental results show that the proposed adaptation structure brings 12\% and 10\% relative word error rate~(WER) reduction on the AESRC2020 accent dataset and the Librispeech dataset, respectively, compared to the baseline.

</details>

### [A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond](2204.09269.md)
**Yisheng Xiao, Lijun Wu, Junliang Guo, Juntao Li et al.** · 2022-04-20

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) generation, which is first proposed in neural machine translation (NMT) to speed up inference, has attracted much attention in both machine learning and natural language processing communities. While NAR generation can significantly accelerate inference speed for machine translation, the speedup comes at the cost of sacrificed translation accuracy compared to its counterpart, autoregressive (AR) generation. In recent years, many new models and algorithms have been designed/proposed to bridge the accuracy gap between NAR generation and AR generation. In this paper, we conduct a systematic survey with comparisons and discussions of various non-autoregressive translation (NAT) models from different aspects. Specifically, we categorize the efforts of NAT into several groups, including data manipulation, modeling methods, training criterion, decoding algorithms, and the benefit from pre-trained models. Furthermore, we briefly review other applications of NAR models beyond machine translation, such as grammatical error correction, text summarization, text style transfer, dialogue, semantic parsing, automatic speech recognition, and so on. In addition, we also discuss potential directions for future exploration, including releasing the dependency of KD, reasonable training objectives, pre-training for NAR, and wider applications, etc. We hope this survey can help researchers capture the latest progress in NAR generation, inspire the design of advanced NAR models and algorithms, and enable industry practitioners to choose appropriate solutions for their applications. The web page of this survey is at \url{https://github.com/LitterBrother-Xiao/Overview-of-Non-autoregressive-Applications}.

</details>

### [Robustness Testing of Data and Knowledge Driven Anomaly Detection in Cyber-Physical Systems](2204.09183.md)
**Xugui Zhou, Maxfield Kouzel, Homa Alemzadeh** · 2022-04-20

<details>
<summary>Abstract</summary>

The growing complexity of Cyber-Physical Systems (CPS) and challenges in ensuring safety and security have led to the increasing use of deep learning methods for accurate and scalable anomaly detection. However, machine learning (ML) models often suffer from low performance in predicting unexpected data and are vulnerable to accidental or malicious perturbations. Although robustness testing of deep learning models has been extensively explored in applications such as image classification and speech recognition, less attention has been paid to ML-driven safety monitoring in CPS. This paper presents the preliminary results on evaluating the robustness of ML-based anomaly detection methods in safety-critical CPS against two types of accidental and malicious input perturbations, generated using a Gaussian-based noise model and the Fast Gradient Sign Method (FGSM). We test the hypothesis of whether integrating the domain knowledge (e.g., on unsafe system behavior) with the ML models can improve the robustness of anomaly detection without sacrificing accuracy and transparency. Experimental results with two case studies of Artificial Pancreas Systems (APS) for diabetes management show that ML-based safety monitors trained with domain knowledge can reduce on average up to 54.2% of robustness error and keep the average F1 scores high while improving transparency.

</details>

### [Disappeared Command: Spoofing Attack On Automatic Speech Recognition Systems with Sound Masking](2204.08977.md)
**Jinghui Xu, Jifeng Zhu, Yong Yang** · 2022-04-19

<details>
<summary>Abstract</summary>

The development of deep learning technology has greatly promoted the performance improvement of automatic speech recognition (ASR) technology, which has demonstrated an ability comparable to human hearing in many tasks. Voice interfaces are becoming more and more widely used as input for many applications and smart devices. However, existing research has shown that DNN is easily disturbed by slight disturbances and makes false recognition, which is extremely dangerous for intelligent voice applications controlled by voice.

</details>

### [Blockwise Streaming Transformer for Spoken Language Understanding and Simultaneous Speech Translation](2204.08920.md)
**Keqi Deng, Shinji Watanabe, Jiatong Shi, Siddhant Arora** · 2022-04-19

<details>
<summary>Abstract</summary>

Although Transformers have gained success in several speech processing tasks like spoken language understanding (SLU) and speech translation (ST), achieving online processing while keeping competitive performance is still essential for real-world interaction. In this paper, we take the first step on streaming SLU and simultaneous ST using a blockwise streaming Transformer, which is based on contextual block processing and blockwise synchronous beam search. Furthermore, we design an automatic speech recognition (ASR)-based intermediate loss regularization for the streaming SLU task to improve the classification performance further. As for the simultaneous ST task, we propose a cross-lingual encoding method, which employs a CTC branch optimized with target language translations. In addition, the CTC translation output is also used to refine the search space with CTC prefix score, achieving joint CTC/attention simultaneous translation for the first time. Experiments for SLU are conducted on FSC and SLURP corpora, while the ST task is evaluated on Fisher-CallHome Spanish and MuST-C En-De corpora. Experimental results show that the blockwise streaming Transformer achieves competitive results compared to offline models, especially with our proposed methods that further yield a 2.4% accuracy gain on the SLU task and a 4.3 BLEU gain on the ST task over streaming baselines.

</details>

### [An Investigation of Monotonic Transducers for Large-Scale Automatic Speech Recognition](2204.08858.md)
**Niko Moritz, Frank Seide, Duc Le, Jay Mahadeokar et al.** · 2022-04-19

<details>
<summary>Abstract</summary>

The two most popular loss functions for streaming end-to-end automatic speech recognition (ASR) are RNN-Transducer (RNN-T) and connectionist temporal classification (CTC). Between these two loss types we can classify the monotonic RNN-T (MonoRNN-T) and the recently proposed CTC-like Transducer (CTC-T). Monotonic transducers have a few advantages. First, RNN-T can suffer from runaway hallucination, where a model keeps emitting non-blank symbols without advancing in time. Secondly, monotonic transducers consume exactly one model score per time step and are therefore more compatible with traditional FST-based ASR decoders. However, the MonoRNN-T so far has been found to have worse accuracy than RNN-T. It does not have to be that way: By regularizing the training via joint LAS training or parameter initialization from RNN-T, both MonoRNN-T and CTC-T perform as well or better than RNN-T. This is demonstrated for LibriSpeech and for a large-scale in-house data set.

</details>

### [Councils in Action: Automating the Curation of Municipal Governance Data for Research](2204.09110.md)
**Eva Maxfield Brown, Nicholas Weber** · 2022-04-19

<details>
<summary>Abstract</summary>

Large scale comparative research into municipal governance is often prohibitively difficult due to a lack of high-quality data. But, recent advances in speech-to-text algorithms and natural language processing has made it possible to more easily collect and analyze data about municipal governments. In this paper, we introduce an open-source platform, the Council Data Project (CDP), to curate novel datasets for research into municipal governance. The contribution of this work is two-fold: 1. We demonstrate that CDP, as an infrastructure, can be used to assemble reliable comparative data on municipal governance; 2. We provide exploratory analysis of three municipalities to show how CDP data can be used to gain insight into how municipal governments perform over time. We conclude by describing future directions for research on and with CDP such as the development of machine learning models for speaker annotation, outline generation, and named entity recognition for improved linked data.

</details>

### [Multi-View Spatial-Temporal Network for Continuous Sign Language Recognition](2204.08747.md)
**Ronghui Li, Lu Meng** · 2022-04-19

<details>
<summary>Abstract</summary>

Sign language is a beautiful visual language and is also the primary language used by speaking and hearing-impaired people. However, sign language has many complex expressions, which are difficult for the public to understand and master. Sign language recognition algorithms will significantly facilitate communication between hearing-impaired people and normal people. Traditional continuous sign language recognition often uses a sequence learning method based on Convolutional Neural Network (CNN) and Long Short-Term Memory Network (LSTM). These methods can only learn spatial and temporal features separately, which cannot learn the complex spatial-temporal features of sign language. LSTM is also difficult to learn long-term dependencies. To alleviate these problems, this paper proposes a multi-view spatial-temporal continuous sign language recognition network. The network consists of three parts. The first part is a Multi-View Spatial-Temporal Feature Extractor Network (MSTN), which can directly extract the spatial-temporal features of RGB and skeleton data; the second is a sign language encoder network based on Transformer, which can learn long-term dependencies; the third is a Connectionist Temporal Classification (CTC) decoder network, which is used to predict the whole meaning of the continuous sign language. Our algorithm is tested on two public sign language datasets SLR-100 and PHOENIX-Weather 2014T (RWTH). As a result, our method achieves excellent performance on both datasets. The word error rate on the SLR-100 dataset is 1.9%, and the word error rate on the RWTHPHOENIX-Weather dataset is 22.8%.

</details>

### [Streaming Align-Refine for Non-autoregressive Deliberation](2204.07556.md)
**Weiran Wang, Ke Hu, Tara N. Sainath** · 2022-04-15

<details>
<summary>Abstract</summary>

We propose a streaming non-autoregressive (non-AR) decoding algorithm to deliberate the hypothesis alignment of a streaming RNN-T model. Our algorithm facilitates a simple greedy decoding procedure, and at the same time is capable of producing the decoding result at each frame with limited right context, thus enjoying both high efficiency and low latency. These advantages are achieved by converting the offline Align-Refine algorithm to be streaming-compatible, with a novel transformer decoder architecture that performs local self-attentions for both text and audio, and a time-aligned cross-attention at each layer. Furthermore, we perform discriminative training of our model with the minimum word error rate (MWER) criterion, which has not been done in the non-AR decoding literature. Experiments on voice search datasets and Librispeech show that with reasonable right context, our streaming model performs as well as the offline counterpart, and discriminative training leads to further WER gain when the first-pass model has small capacity.

</details>

### [HuBERT-EE: Early Exiting HuBERT for Efficient Speech Recognition](2204.06328.md)
**Ji Won Yoon, Beom Jun Woo, Nam Soo Kim** · 2022-04-13

<details>
<summary>Abstract</summary>

Pre-training with self-supervised models, such as Hidden-unit BERT (HuBERT) and wav2vec 2.0, has brought significant improvements in automatic speech recognition (ASR). However, these models usually require an expensive computational cost to achieve outstanding performance, slowing down the inference speed. To improve the model efficiency, we introduce an early exit scheme for ASR, namely HuBERT-EE, that allows the model to stop the inference dynamically. In HuBERT-EE, multiple early exit branches are added at the intermediate layers. When the intermediate prediction of the early exit branch is confident, the model stops the inference, and the corresponding result can be returned early. We investigate the proper early exiting criterion and fine-tuning strategy to effectively perform early exiting. Experimental results on the LibriSpeech show that HuBERT-EE can accelerate the inference of the HuBERT while simultaneously balancing the trade-off between the performance and the latency.

</details>

### [Self-critical Sequence Training for Automatic Speech Recognition](2204.06260.md)
**Chen Chen, Yuchen Hu, Nana Hou, Xiaofeng Qi et al.** · 2022-04-13

<details>
<summary>Abstract</summary>

Although automatic speech recognition (ASR) task has gained remarkable success by sequence-to-sequence models, there are two main mismatches between its training and testing that might lead to performance degradation: 1) The typically used cross-entropy criterion aims to maximize log-likelihood of the training data, while the performance is evaluated by word error rate (WER), not log-likelihood; 2) The teacher-forcing method leads to the dependence on ground truth during training, which means that model has never been exposed to its own prediction before testing. In this paper, we propose an optimization method called self-critical sequence training (SCST) to make the training procedure much closer to the testing phase. As a reinforcement learning (RL) based method, SCST utilizes a customized reward function to associate the training criterion and WER. Furthermore, it removes the reliance on teacher-forcing and harmonizes the model with respect to its inference procedure. We conducted experiments on both clean and noisy speech datasets, and the results show that the proposed SCST respectively achieves 8.7% and 7.8% relative improvements over the baseline in terms of WER.

</details>

### [A Unified Cascaded Encoder ASR Model for Dynamic Model Sizes](2204.06164.md)
**Shaojin Ding, Weiran Wang, Ding Zhao, Tara N. Sainath et al.** · 2022-04-13

<details>
<summary>Abstract</summary>

In this paper, we propose a dynamic cascaded encoder Automatic Speech Recognition (ASR) model, which unifies models for different deployment scenarios. Moreover, the model can significantly reduce model size and power consumption without loss of quality. Namely, with the dynamic cascaded encoder model, we explore three techniques to maximally boost the performance of each model size: 1) Use separate decoders for each sub-model while sharing the encoders; 2) Use funnel-pooling to improve the encoder efficiency; 3) Balance the size of causal and non-causal encoders to improve quality and fit deployment constraints. Overall, the proposed large-medium model has 30% smaller size and reduces power consumption by 33%, compared to the baseline cascaded encoder model. The triple-size model that unifies the large, medium, and small models achieves 37% total size reduction with minimal quality loss, while substantially reducing the engineering efforts of having separate models.

</details>

### [ASR in German: A Detailed Error Analysis](2204.05617.md)
**Johannes Wirth, Rene Peinl** · 2022-04-12

<details>
<summary>Abstract</summary>

The amount of freely available systems for automatic speech recognition (ASR) based on neural networks is growing steadily, with equally increasingly reliable predictions. However, the evaluation of trained models is typically exclusively based on statistical metrics such as WER or CER, which do not provide any insight into the nature or impact of the errors produced when predicting transcripts from speech input. This work presents a selection of ASR model architectures that are pretrained on the German language and evaluates them on a benchmark of diverse test datasets. It identifies cross-architectural prediction errors, classifies those into categories and traces the sources of errors per category back into training data as well as other sources. Finally, it discusses solutions in order to create qualitatively better training datasets and more robust ASR systems.

</details>

### [Multimodal Sparse Transformer Network for Audio-Visual Speech Recognition](s2:08f9b6c9c305aa13e92805ab1f0171e10aa786c6.md)
**Qiya Song, Bin Sun, Shutao Li** · 2022-04-12

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is the major human–machine interface in many intelligent systems, such as intelligent homes, autonomous driving, and servant robots. However, its performance usually significantly deteriorates in the presence of external noise, leading to limitations of its application scenes. The audio-visual speech recognition (AVSR) takes visual information as a complementary modality to enhance the performance of audio speech recognition effectively, particularly in noisy conditions. Recently, the transformer-based architectures have been used to model the audio and video sequences for the AVSR, which achieves a superior performance. However, its performance may be degraded in these architectures due to extracting irrelevant information while modeling long-term dependences. In addition, the motion feature is essential for capturing the spatio-temporal information within the lip region to best utilize visual sequences but has not been considered in the AVSR tasks. Therefore, we propose a multimodal sparse transformer network (MMST) in this article. The sparse self-attention mechanism can improve the concentration of attention on global information by selecting the most relevant parts wisely. Moreover, the motion features are seamlessly introduced into the MMST model. We subtly allow motion-modality information to flow into visual modality through the cross-modal attention module to enhance visual features, thereby further improving recognition performance. Extensive experiments conducted on different datasets validate that our proposed method outperforms several state-of-the-art methods in terms of the word error rate (WER).

</details>

### [Unified Speech-Text Pre-training for Speech Translation and Recognition](2204.05409.md)
**Yun Tang, Hongyu Gong, Ning Dong, Changhan Wang et al.** · 2022-04-11

<details>
<summary>Abstract</summary>

We describe a method to jointly pre-train speech and text in an encoder-decoder modeling framework for speech translation and recognition. The proposed method incorporates four self-supervised and supervised subtasks for cross modality learning. A self-supervised speech subtask leverages unlabelled speech data, and a (self-)supervised text to text subtask makes use of abundant text training data. Two auxiliary supervised speech tasks are included to unify speech and text modeling space. Our contribution lies in integrating linguistic information from the text corpus into the speech pre-training. Detailed analysis reveals learning interference among subtasks. Two pre-training configurations for speech translation and recognition, respectively, are presented to alleviate subtask interference. Our experiments show the proposed method can effectively fuse speech and text information into one model. It achieves between 1.7 and 2.3 BLEU improvement above the state of the art on the MuST-C speech translation dataset and comparable WERs to wav2vec 2.0 on the Librispeech speech recognition task.

</details>

### [Large-Scale Streaming End-to-End Speech Translation with Neural Transducers](2204.05352.md)
**Jian Xue, Peidong Wang, Jinyu Li, Matt Post et al.** · 2022-04-11

<details>
<summary>Abstract</summary>

Neural transducers have been widely used in automatic speech recognition (ASR). In this paper, we introduce it to streaming end-to-end speech translation (ST), which aims to convert audio signals to texts in other languages directly. Compared with cascaded ST that performs ASR followed by text-based machine translation (MT), the proposed Transformer transducer (TT)-based ST model drastically reduces inference latency, exploits speech information, and avoids error propagation from ASR to MT. To improve the modeling capacity, we propose attention pooling for the joint network in TT. In addition, we extend TT-based ST to multilingual ST, which generates texts of multiple languages at the same time. Experimental results on a large-scale 50 thousand (K) hours pseudo-labeled training set show that TT-based ST not only significantly reduces inference time but also outperforms non-streaming cascaded ST for English-German translation.

</details>

### [Deep Embeddings for Robust User-Based Amateur Vocal Percussion Classification](2204.04646.md)
**Alejandro Delgado, Emir Demirel, Vinod Subramanian, Charalampos Saitis et al.** · 2022-04-10

<details>
<summary>Abstract</summary>

Vocal Percussion Transcription (VPT) is concerned with the automatic detection and classification of vocal percussion sound events, allowing music creators and producers to sketch drum lines on the fly. Classifier algorithms in VPT systems learn best from small user-specific datasets, which usually restrict modelling to small input feature sets to avoid data overfitting. This study explores several deep supervised learning strategies to obtain informative feature sets for amateur vocal percussion classification. We evaluated the performance of these sets on regular vocal percussion classification tasks and compared them with several baseline approaches including feature selection methods and a speech recognition engine. These proposed learning models were supervised with several label sets containing information from four different levels of abstraction: instrument-level, syllable-level, phoneme-level, and boxeme-level. Results suggest that convolutional neural networks supervised with syllable-level annotations produced the most informative embeddings for classification, which can be used as input representations to fit classifiers with. Finally, we used back-propagation-based saliency maps to investigate the importance of different spectrogram regions for feature learning.

</details>

### [Unsupervised Uncertainty Measures of Automatic Speech Recognition for Non-intrusive Speech Intelligibility Prediction](2204.04288.md)
**Zehai Tu, Ning Ma, Jon Barker** · 2022-04-08

<details>
<summary>Abstract</summary>

Non-intrusive intelligibility prediction is important for its application in realistic scenarios, where a clean reference signal is difficult to access. The construction of many non-intrusive predictors require either ground truth intelligibility labels or clean reference signals for supervised learning. In this work, we leverage an unsupervised uncertainty estimation method for predicting speech intelligibility, which does not require intelligibility labels or reference signals to train the predictor. Our experiments demonstrate that the uncertainty from state-of-the-art end-to-end automatic speech recognition (ASR) models is highly correlated with speech intelligibility. The proposed method is evaluated on two databases and the results show that the unsupervised uncertainty measures of ASR models are more correlated with speech intelligibility from listening results than the predictions made by widely used intrusive methods.

</details>

### [Auditory-Based Data Augmentation for End-to-End Automatic Speech Recognition](2204.04284.md)
**Zehai Tu, Jack Deadman, Ning Ma, Jon Barker** · 2022-04-08

<details>
<summary>Abstract</summary>

End-to-end models have achieved significant improvement on automatic speech recognition. One common method to improve performance of these models is expanding the data-space through data augmentation. Meanwhile, human auditory inspired front-ends have also demonstrated improvement for automatic speech recognisers. In this work, a well-verified auditory-based model, which can simulate various hearing abilities, is investigated for the purpose of data augmentation for end-to-end speech recognition. By introducing the auditory model into the data augmentation process, end-to-end systems are encouraged to ignore variation from the signal that cannot be heard and thereby focus on robust features for speech recognition. Two mechanisms in the auditory model, spectral smearing and loudness recruitment, are studied on the LibriSpeech dataset with a transformer-based end-to-end model. The results show that the proposed augmentation methods can bring statistically significant improvement on the performance of the state-of-the-art SpecAugment.

</details>

### [Adding Connectionist Temporal Summarization into Conformer to Improve Its Decoder Efficiency For Speech Recognition](2204.03889.md)
**Nick J. C. Wang, Zongfeng Quan, Shaojun Wang, Jing Xiao** · 2022-04-08

<details>
<summary>Abstract</summary>

The Conformer model is an excellent architecture for speech recognition modeling that effectively utilizes the hybrid losses of connectionist temporal classification (CTC) and attention to train model parameters. To improve the decoding efficiency of Conformer, we propose a novel connectionist temporal summarization (CTS) method that reduces the number of frames required for the attention decoder fed from the acoustic sequences generated by the encoder, thus reducing operations. However, to achieve such decoding improvements, we must fine-tune model parameters, as cross-attention observations are changed and thus require corresponding refinements. Our final experiments show that, with a beamwidth of 4, the LibriSpeech's decoding budget can be reduced by up to 20% and for FluentSpeech data it can be reduced by 11%, without losing ASR accuracy. An improvement in accuracy is even found for the LibriSpeech "test-other" set. The word error rate (WER) is reduced by 6\% relative at the beam width of 1 and by 3% relative at the beam width of 4.

</details>

### [Hierarchical Softmax for End-to-End Low-resource Multilingual Speech Recognition](2204.03855.md)
**Qianying Liu, Zhuo Gong, Zhengdong Yang, Yuhang Yang et al.** · 2022-04-08

<details>
<summary>Abstract</summary>

Low-resource speech recognition has been long-suffering from insufficient training data. In this paper, we propose an approach that leverages neighboring languages to improve low-resource scenario performance, founded on the hypothesis that similar linguistic units in neighboring languages exhibit comparable term frequency distributions, which enables us to construct a Huffman tree for performing multilingual hierarchical Softmax decoding. This hierarchical structure enables cross-lingual knowledge sharing among similar tokens, thereby enhancing low-resource training outcomes. Empirical analyses demonstrate that our method is effective in improving the accuracy and efficiency of low-resource speech recognition.

</details>

### [Defense against Adversarial Attacks on Hybrid Speech Recognition using Joint Adversarial Fine-tuning with Denoiser](2204.03851.md)
**Sonal Joshi, Saurabh Kataria, Yiwen Shao, Piotr Zelasko et al.** · 2022-04-08

<details>
<summary>Abstract</summary>

Adversarial attacks are a threat to automatic speech recognition (ASR) systems, and it becomes imperative to propose defenses to protect them. In this paper, we perform experiments to show that K2 conformer hybrid ASR is strongly affected by white-box adversarial attacks. We propose three defenses--denoiser pre-processor, adversarially fine-tuning ASR model, and adversarially fine-tuning joint model of ASR and denoiser. Our evaluation shows denoiser pre-processor (trained on offline adversarial examples) fails to defend against adaptive white-box attacks. However, adversarially fine-tuning the denoiser using a tandem model of denoiser and ASR offers more robustness. We evaluate two variants of this defense--one updating parameters of both models and the second keeping ASR frozen. The joint model offers a mean absolute decrease of 19.3\% ground truth (GT) WER with reference to baseline against fast gradient sign method (FGSM) attacks with different $L_\infty$ norms. The joint model with frozen ASR parameters gives the best defense against projected gradient descent (PGD) with 7 iterations, yielding a mean absolute increase of 22.3\% GT WER with reference to baseline; and against PGD with 500 iterations, yielding a mean absolute decrease of 45.08\% GT WER and an increase of 68.05\% adversarial target WER.

</details>

### [MAESTRO: Matched Speech Text Representations through Modality Matching](2204.03409.md)
**Zhehuai Chen, Yu Zhang, Andrew Rosenberg, Bhuvana Ramabhadran et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

We present Maestro, a self-supervised training method to unify representations learnt from speech and text modalities. Self-supervised learning from speech signals aims to learn the latent structure inherent in the signal, while self-supervised learning from text attempts to capture lexical information. Learning aligned representations from unpaired speech and text sequences is a challenging task. Previous work either implicitly enforced the representations learnt from these two modalities to be aligned in the latent space through multitasking and parameter sharing or explicitly through conversion of modalities via speech synthesis. While the former suffers from interference between the two modalities, the latter introduces additional complexity. In this paper, we propose Maestro, a novel algorithm to learn unified representations from both these modalities simultaneously that can transfer to diverse downstream tasks such as Automated Speech Recognition (ASR) and Speech Translation (ST). Maestro learns unified representations through sequence alignment, duration prediction and matching embeddings in the learned space through an aligned masked-language model loss. We establish a new state-of-the-art (SOTA) on VoxPopuli multilingual ASR with a 8% relative reduction in Word Error Rate (WER), multidomain SpeechStew ASR (3.7% relative) and 21 languages to English multilingual ST on CoVoST 2 with an improvement of 2.8 BLEU averaged over 21 languages.

</details>

### [Enabling All In-Edge Deep Learning: A Literature Review](2204.03326.md)
**Praveen Joshi, Mohammed Hasanuzzaman, Chandra Thapa, Haithem Afli et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

In recent years, deep learning (DL) models have demonstrated remarkable achievements on non-trivial tasks such as speech recognition and natural language understanding. One of the significant contributors to its success is the proliferation of end devices that acted as a catalyst to provide data for data-hungry DL models. However, computing DL training and inference is the main challenge. Usually, central cloud servers are used for the computation, but it opens up other significant challenges, such as high latency, increased communication costs, and privacy concerns. To mitigate these drawbacks, considerable efforts have been made to push the processing of DL models to edge servers. Moreover, the confluence point of DL and edge has given rise to edge intelligence (EI). This survey paper focuses primarily on the fifth level of EI, called all in-edge level, where DL training and inference (deployment) are performed solely by edge servers. All in-edge is suitable when the end devices have low computing resources, e.g., Internet-of-Things, and other requirements such as latency and communication cost are important in mission-critical applications, e.g., health care. Firstly, this paper presents all in-edge computing architectures, including centralized, decentralized, and distributed. Secondly, this paper presents enabling technologies, such as model parallelism and split learning, which facilitate DL training and deployment at edge servers. Thirdly, model adaptation techniques based on model compression and conditional computation are described because the standard cloud-based DL deployment cannot be directly applied to all in-edge due to its limited computational resources. Fourthly, this paper discusses eleven key performance metrics to evaluate the performance of DL at all in-edge efficiently. Finally, several open research challenges in the area of all in-edge are presented.

</details>

### [Three-Module Modeling For End-to-End Spoken Language Understanding Using Pre-trained DNN-HMM-Based Acoustic-Phonetic Model](2204.03315.md)
**Nick J. C. Wang, Lu Wang, Yandan Sun, Haimei Kang et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

In spoken language understanding (SLU), what the user says is converted to his/her intent. Recent work on end-to-end SLU has shown that accuracy can be improved via pre-training approaches. We revisit ideas presented by Lugosch et al. using speech pre-training and three-module modeling; however, to ease construction of the end-to-end SLU model, we use as our phoneme module an open-source acoustic-phonetic model from a DNN-HMM hybrid automatic speech recognition (ASR) system instead of training one from scratch. Hence we fine-tune on speech only for the word module, and we apply multi-target learning (MTL) on the word and intent modules to jointly optimize SLU performance. MTL yields a relative reduction of 40% in intent-classification error rates (from 1.0% to 0.6%). Note that our three-module model is a streaming method. The final outcome of the proposed three-module modeling approach yields an intent accuracy of 99.4% on FluentSpeech, an intent error rate reduction of 50% compared to that of Lugosch et al. Although we focus on real-time streaming methods, we also list non-streaming methods for comparison.

</details>

### [Speech Pre-training with Acoustic Piece](2204.03240.md)
**Shuo Ren, Shujie Liu, Yu Wu, Long Zhou et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

Previous speech pre-training methods, such as wav2vec2.0 and HuBERT, pre-train a Transformer encoder to learn deep representations from audio data, with objectives predicting either elements from latent vector quantized space or pre-generated labels (known as target codes) with offline clustering. However, those training signals (quantized elements or codes) are independent across different tokens without considering their relations. According to our observation and analysis, the target codes share obvious patterns aligned with phonemized text data. Based on that, we propose to leverage those patterns to better pre-train the model considering the relations among the codes. The patterns we extracted, called "acoustic piece"s, are from the sentence piece result of HuBERT codes. With the acoustic piece as the training signal, we can implicitly bridge the input audio and natural language, which benefits audio-to-text tasks, such as automatic speech recognition (ASR). Simple but effective, our method "HuBERT-AP" significantly outperforms strong baselines on the LibriSpeech ASR task.

</details>

### [3M: Multi-loss, Multi-path and Multi-level Neural Networks for speech recognition](2204.03178.md)
**Zhao You, Shulin Feng, Dan Su, Dong Yu** · 2022-04-07

<details>
<summary>Abstract</summary>

Recently, Conformer based CTC/AED model has become a mainstream architecture for ASR. In this paper, based on our prior work, we identify and integrate several approaches to achieve further improvements for ASR tasks, which we denote as multi-loss, multi-path and multi-level, summarized as "3M" model. Specifically, multi-loss refers to the joint CTC/AED loss and multi-path denotes the Mixture-of-Experts(MoE) architecture which can effectively increase the model capacity without remarkably increasing computation cost. Multi-level means that we introduce auxiliary loss at multiple level of a deep model to help training. We evaluate our proposed method on the public WenetSpeech dataset and experimental results show that the proposed method provides 12.2%-17.6% relative CER improvement over the baseline model trained by Wenet toolkit. On our large scale dataset of 150k hours corpus, the 3M model has also shown obvious superiority over the baseline Conformer model. Code is publicly available at https://github.com/tencent-ailab/3m-asr.

</details>

### [MTI-Net: A Multi-Target Speech Intelligibility Prediction Model](2204.03310.md)
**Ryandhimas E. Zezario, Szu-wei Fu, Fei Chen, Chiou-Shann Fuh et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

Recently, deep learning (DL)-based non-intrusive speech assessment models have attracted great attention. Many studies report that these DL-based models yield satisfactory assessment performance and good flexibility, but their performance in unseen environments remains a challenge. Furthermore, compared to quality scores, fewer studies elaborate deep learning models to estimate intelligibility scores. This study proposes a multi-task speech intelligibility prediction model, called MTI-Net, for simultaneously predicting human and machine intelligibility measures. Specifically, given a speech utterance, MTI-Net is designed to predict human subjective listening test results and word error rate (WER) scores. We also investigate several methods that can improve the prediction performance of MTI-Net. First, we compare different features (including low-level features and embeddings from self-supervised learning (SSL) models) and prediction targets of MTI-Net. Second, we explore the effect of transfer learning and multi-tasking learning on training MTI-Net. Finally, we examine the potential advantages of fine-tuning SSL embeddings. Experimental results demonstrate the effectiveness of using cross-domain features, multi-task learning, and fine-tuning SSL embeddings. Furthermore, it is confirmed that the intelligibility and WER scores predicted by MTI-Net are highly correlated with the ground-truth scores.

</details>

### [Enhanced Direct Speech-to-Speech Translation Using Self-supervised Pre-training and Data Augmentation](2204.02967.md)
**Sravya Popuri, Peng-Jen Chen, Changhan Wang, Juan Pino et al.** · 2022-04-06

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation (S2ST) models suffer from data scarcity issues as there exists little parallel S2ST data, compared to the amount of data available for conventional cascaded systems that consist of automatic speech recognition (ASR), machine translation (MT), and text-to-speech (TTS) synthesis. In this work, we explore self-supervised pre-training with unlabeled speech data and data augmentation to tackle this issue. We take advantage of a recently proposed speech-to-unit translation (S2UT) framework that encodes target speech into discrete representations, and transfer pre-training and efficient partial finetuning techniques that work well for speech-to-text translation (S2T) to the S2UT domain by studying both speech encoder and discrete unit decoder pre-training. Our experiments on Spanish-English translation show that self-supervised pre-training consistently improves model performance compared with multitask learning with an average 6.6-12.1 BLEU gain, and it can be further combined with data augmentation techniques that apply MT to create weakly supervised training data. Audio samples are available at: https://facebookresearch.github.io/speech_translation/enhanced_direct_s2st_units/index.html .

</details>

### [A survey on recently proposed activation functions for Deep Learning](2204.02921.md)
**Murilo Gustineli** · 2022-04-06

<details>
<summary>Abstract</summary>

Artificial neural networks (ANN), typically referred to as neural networks, are a class of Machine Learning algorithms and have achieved widespread success, having been inspired by the biological structure of the human brain. Neural networks are inherently powerful due to their ability to learn complex function approximations from data. This generalization ability has been able to impact multidisciplinary areas involving image recognition, speech recognition, natural language processing, and others. Activation functions are a crucial sub-component of neural networks. They define the output of a node in the network given a set of inputs. This survey discusses the main concepts of activation functions in neural networks, including; a brief introduction to deep neural networks, a summary of what are activation functions and how they are used in neural networks, their most common properties, the different types of activation functions, some of the challenges, limitations, and alternative solutions faced by activation functions, concluding with the final remarks.

</details>

### [A Wav2vec2-Based Experimental Study on Self-Supervised Learning Methods to Improve Child Speech Recognition](2204.05419.md)
**Rishabh Jain, Andrei Barcovschi, Mariam Yiwere, Dan Bigioi et al.** · 2022-04-06

<details>
<summary>Abstract</summary>

Despite recent advancements in deep learning technologies, Child Speech Recognition remains a challenging task. Current Automatic Speech Recognition (ASR) models require substantial amounts of annotated data for training, which is scarce. In this work, we explore using the ASR model, wav2vec2, with different pretraining and finetuning configurations for self-supervised learning (SSL) toward improving automatic child speech recognition. The pretrained wav2vec2 models were finetuned using different amounts of child speech training data, adult speech data, and a combination of both, to discover the optimum amount of data required to finetune the model for the task of child ASR. Our trained model achieves the best Word Error Rate (WER) of 7.42 on the MyST child speech dataset, 2.99 on the PFSTAR dataset and 12.47 on the CMU KIDS dataset as compared to any other previous methods. Our models outperformed the wav2vec2 BASE 960 on child speech which is considered a state-of-the-art ASR model on adult speech by just using 10 hours of child speech data in finetuning. The analysis of different types of training data and their effect on inference is also provided by using a combination of datasets in pretraining, finetuning and inference.

</details>

### [Emotional Speech Recognition with Pre-trained Deep Visual Models](2204.03561.md)
**Waleed Ragheb, Mehdi Mirzapour, Ali Delfardi, Hélène Jacquenet et al.** · 2022-04-06

<details>
<summary>Abstract</summary>

In this paper, we propose a new methodology for emotional speech recognition using visual deep neural network models. We employ the transfer learning capabilities of the pre-trained computer vision deep models to have a mandate for the emotion recognition in speech task. In order to achieve that, we propose to use a composite set of acoustic features and a procedure to convert them into images. Besides, we present a training paradigm for these models taking into consideration the different characteristics between acoustic-based images and regular ones. In our experiments, we use the pre-trained VGG-16 model and test the overall methodology on the Berlin EMO-DB dataset for speaker-independent emotion recognition. We evaluate the proposed model on the full list of the seven emotions and the results set a new state-of-the-art.

</details>

### [Successes and critical failures of neural networks in capturing human-like speech recognition](2204.03740.md)
**Federico Adolfi, Jeffrey S. Bowers, David Poeppel** · 2022-04-06

<details>
<summary>Abstract</summary>

Natural and artificial audition can in principle acquire different solutions to a given problem. The constraints of the task, however, can nudge the cognitive science and engineering of audition to qualitatively converge, suggesting that a closer mutual examination would potentially enrich artificial hearing systems and process models of the mind and brain. Speech recognition - an area ripe for such exploration - is inherently robust in humans to a number transformations at various spectrotemporal granularities. To what extent are these robustness profiles accounted for by high-performing neural network systems? We bring together experiments in speech recognition under a single synthesis framework to evaluate state-of-the-art neural networks as stimulus-computable, optimized observers. In a series of experiments, we (1) clarify how influential speech manipulations in the literature relate to each other and to natural speech, (2) show the granularities at which machines exhibit out-of-distribution robustness, reproducing classical perceptual phenomena in humans, (3) identify the specific conditions where model predictions of human performance differ, and (4) demonstrate a crucial failure of all artificial systems to perceptually recover where humans do, suggesting alternative directions for theory and model building. These findings encourage a tighter synergy between the cognitive science and engineering of audition.

</details>

### [Simple and Effective Unsupervised Speech Synthesis](2204.02524.md)
**Alexander H. Liu, Cheng-I Jeff Lai, Wei-Ning Hsu, Michael Auli et al.** · 2022-04-06

<details>
<summary>Abstract</summary>

We introduce the first unsupervised speech synthesis system based on a simple, yet effective recipe. The framework leverages recent work in unsupervised speech recognition as well as existing neural-based speech synthesis. Using only unlabeled speech audio and unlabeled text as well as a lexicon, our method enables speech synthesis without the need for a human-labeled corpus. Experiments demonstrate the unsupervised system can synthesize speech similar to a supervised counterpart in terms of naturalness and intelligibility measured by human evaluation.

</details>

### [Towards End-to-end Unsupervised Speech Recognition](2204.02492.md)
**Alexander H. Liu, Wei-Ning Hsu, Michael Auli, Alexei Baevski** · 2022-04-05

<details>
<summary>Abstract</summary>

Unsupervised speech recognition has shown great potential to make Automatic Speech Recognition (ASR) systems accessible to every language. However, existing methods still heavily rely on hand-crafted pre-processing. Similar to the trend of making supervised speech recognition end-to-end, we introduce wav2vec-U 2.0 which does away with all audio-side pre-processing and improves accuracy through better architecture. In addition, we introduce an auxiliary self-supervised objective that ties model predictions back to the input. Experiments show that wav2vec-U 2.0 improves unsupervised recognition results across different languages while being conceptually simpler.

</details>

### [Combining Spectral and Self-Supervised Features for Low Resource Speech Recognition and Translation](2204.02470.md)
**Dan Berrebbi, Jiatong Shi, Brian Yan, Osbel Lopez-Francisco et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) models have been successfully applied in various deep learning-based speech tasks, particularly those with a limited amount of data. However, the quality of SSL representations depends highly on the relatedness between the SSL training domain(s) and the target data domain. On the contrary, spectral feature (SF) extractors such as log Mel-filterbanks are hand-crafted non-learnable components, and could be more robust to domain shifts. The present work examines the assumption that combining non-learnable SF extractors to SSL models is an effective approach to low resource speech tasks. We propose a learnable and interpretable framework to combine SF and SSL representations. The proposed framework outperforms significantly both baseline and SSL models on Automatic Speech Recognition (ASR) and Speech Translation (ST) tasks on three low resource datasets. We additionally design a mixture of experts based combination model. This last model reveals that the relative contribution of SSL models over conventional SF extractors is very small in case of domain mismatch between SSL training set and the target language data.

</details>

### [Hear No Evil: Towards Adversarial Robustness of Automatic Speech Recognition via Multi-Task Learning](2204.02381.md)
**Nilaksh Das, Duen Horng Chau** · 2022-04-05

<details>
<summary>Abstract</summary>

As automatic speech recognition (ASR) systems are now being widely deployed in the wild, the increasing threat of adversarial attacks raises serious questions about the security and reliability of using such systems. On the other hand, multi-task learning (MTL) has shown success in training models that can resist adversarial attacks in the computer vision domain. In this work, we investigate the impact of performing such multi-task learning on the adversarial robustness of ASR models in the speech domain. We conduct extensive MTL experimentation by combining semantically diverse tasks such as accent classification and ASR, and evaluate a wide range of adversarial settings. Our thorough analysis reveals that performing MTL with semantically diverse tasks consistently makes it harder for an adversarial attack to succeed. We also discuss in detail the serious pitfalls and their related remedies that have a significant impact on the robustness of MTL models. Our proposed MTL approach shows considerable absolute improvements in adversarially targeted WER ranging from 17.25 up to 59.90 compared to single-task learning baselines (attention decoder and CTC respectively). Ours is the first in-depth study that uncovers adversarial robustness gains from multi-task learning for ASR.

</details>

### [Low-Latency Speech Separation Guided Diarization for Telephone Conversations](2204.02306.md)
**Giovanni Morrone, Samuele Cornell, Desh Raj, Luca Serafini et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

In this paper, we carry out an analysis on the use of speech separation guided diarization (SSGD) in telephone conversations. SSGD performs diarization by separating the speakers signals and then applying voice activity detection on each estimated speaker signal. In particular, we compare two low-latency speech separation models. Moreover, we show a post-processing algorithm that significantly reduces the false alarm errors of a SSGD pipeline. We perform our experiments on two datasets: Fisher Corpus Part 1 and CALLHOME, evaluating both separation and diarization metrics. Notably, our SSGD DPRNN-based online model achieves 11.1% DER on CALLHOME, comparable with most state-of-the-art end-to-end neural diarization models despite being trained on an order of magnitude less data and having considerably lower latency, i.e., 0.1 vs. 10 seconds. We also show that the separated signals can be readily fed to a speech recognition back-end with performance close to the oracle source signals.

</details>

### [A Complementary Joint Training Approach Using Unpaired Speech and Text for Low-Resource Automatic Speech Recognition](2204.02023.md)
**Ye-Qian Du, Jie Zhang, Qiu-Shi Zhu, Li-Rong Dai et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

Unpaired data has shown to be beneficial for low-resource automatic speech recognition~(ASR), which can be involved in the design of hybrid models with multi-task training or language model dependent pre-training. In this work, we leverage unpaired data to train a general sequence-to-sequence model. Unpaired speech and text are used in the form of data pairs by generating the corresponding missing parts in prior to model training. Inspired by the complementarity of speech-PseudoLabel pair and SynthesizedAudio-text pair in both acoustic features and linguistic features, we propose a complementary joint training~(CJT) method that trains a model alternatively with two data pairs. Furthermore, label masking for pseudo-labels and gradient restriction for synthesized audio are proposed to further cope with the deviations from real data, termed as CJT++. Experimental results show that compared to speech-only training, the proposed basic CJT achieves great performance improvements on clean/other test sets, and the CJT++ re-training yields further performance enhancements. It is also apparent that the proposed method outperforms the wav2vec2.0 model with the same model size and beam size, particularly in extreme low-resource cases.

</details>

### [Unsupervised Data Selection via Discrete Speech Representation for ASR](2204.01981.md)
**Zhiyun Lu, Yongqiang Wang, Yu Zhang, Wei Han et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

Self-supervised learning of speech representations has achieved impressive results in improving automatic speech recognition (ASR). In this paper, we show that data selection is important for self-supervised learning. We propose a simple and effective unsupervised data selection method which selects acoustically similar speech to a target domain. It takes the discrete speech representation available in common self-supervised learning frameworks as input, and applies a contrastive data selection method on the discrete tokens. Through extensive empirical studies we show that our proposed method reduces the amount of required pre-training data and improves the downstream ASR performance. Pre-training on a selected subset of 6% of the general data pool results in 11.8% relative improvements in LibriSpeech test-other compared to pre-training on the full set. On Multilingual LibriSpeech French, German, and Spanish test sets, selecting 6% data for pre-training reduces word error rate by more than 15% relatively compared to the full set, and achieves competitive results compared to current state-of-the-art performances.

</details>

### [Audio-visual multi-channel speech separation, dereverberation and recognition](2204.01977.md)
**Guinan Li, Jianwei Yu, Jiajun Deng, Xunying Liu et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

Despite the rapid advance of automatic speech recognition (ASR) technologies, accurate recognition of cocktail party speech characterised by the interference from overlapping speakers, background noise and room reverberation remains a highly challenging task to date. Motivated by the invariance of visual modality to acoustic signal corruption, audio-visual speech enhancement techniques have been developed, although predominantly targeting overlapping speech separation and recognition tasks. In this paper, an audio-visual multi-channel speech separation, dereverberation and recognition approach featuring a full incorporation of visual information into all three stages of the system is proposed. The advantage of the additional visual modality over using audio only is demonstrated on two neural dereverberation approaches based on DNN-WPE and spectral mapping respectively. The learning cost function mismatch between the separation and dereverberation models and their integration with the back-end recognition system is minimised using fine-tuning on the MSE and LF-MMI criteria. Experiments conducted on the LRS2 dataset suggest that the proposed audio-visual multi-channel speech separation, dereverberation and recognition system outperforms the baseline audio-visual multi-channel speech separation and recognition system containing no dereverberation module by a statistically significant word error rate (WER) reduction of 2.06% absolute (8.77% relative).

</details>

### [Deliberation Model for On-Device Spoken Language Understanding](2204.01893.md)
**Duc Le, Akshat Shrivastava, Paden Tomasello, Suyoun Kim et al.** · 2022-04-04

<details>
<summary>Abstract</summary>

We propose a novel deliberation-based approach to end-to-end (E2E) spoken language understanding (SLU), where a streaming automatic speech recognition (ASR) model produces the first-pass hypothesis and a second-pass natural language understanding (NLU) component generates the semantic parse by conditioning on both ASR's text and audio embeddings. By formulating E2E SLU as a generalized decoder, our system is able to support complex compositional semantic structures. Furthermore, the sharing of parameters between ASR and NLU makes the system especially suitable for resource-constrained (on-device) environments; our proposed approach consistently outperforms strong pipeline NLU baselines by 0.60% to 0.65% on the spoken version of the TOPv2 dataset (STOP). We demonstrate that the fusion of text and audio features, coupled with the system's ability to rewrite the first-pass hypothesis, makes our approach more robust to ASR errors. Finally, we show that our approach can significantly reduce the degradation when moving from natural speech to synthetic speech training, but more work is required to make text-to-speech (TTS) a viable solution for scaling up E2E SLU.

</details>

### [GWA: A Large High-Quality Acoustic Dataset for Audio Processing](2204.01787.md)
**Zhenyu Tang, Rohith Aralikatti, Anton Ratnarajah, Dinesh Manocha** · 2022-04-04

<details>
<summary>Abstract</summary>

We present the Geometric-Wave Acoustic (GWA) dataset, a large-scale audio dataset of about 2 million synthetic room impulse responses (IRs) and their corresponding detailed geometric and simulation configurations. Our dataset samples acoustic environments from over 6.8K high-quality diverse and professionally designed houses represented as semantically labeled 3D meshes. We also present a novel real-world acoustic materials assignment scheme based on semantic matching that uses a sentence transformer model. We compute high-quality impulse responses corresponding to accurate low-frequency and high-frequency wave effects by automatically calibrating geometric acoustic ray-tracing with a finite-difference time-domain wave solver. We demonstrate the higher accuracy of our IRs by comparing with recorded IRs from complex real-world environments. Moreover, we highlight the benefits of GWA on audio deep learning tasks such as automated speech recognition, speech enhancement, and speech separation. This dataset is the first data with accurate wave acoustic simulations in complex scenes. Codes and data are available at https://gamma.umd.edu/pro/sound/gwa.

</details>

### [Cross-lingual Self-Supervised Speech Representations for Improved Dysarthric Speech Recognition](2204.01670.md)
**Abner Hernandez, Paula Andrea Pérez-Toro, Elmar Nöth, Juan Rafael Orozco-Arroyave et al.** · 2022-04-04

<details>
<summary>Abstract</summary>

State-of-the-art automatic speech recognition (ASR) systems perform well on healthy speech. However, the performance on impaired speech still remains an issue. The current study explores the usefulness of using Wav2Vec self-supervised speech representations as features for training an ASR system for dysarthric speech. Dysarthric speech recognition is particularly difficult as several aspects of speech such as articulation, prosody and phonation can be impaired. Specifically, we train an acoustic model with features extracted from Wav2Vec, Hubert, and the cross-lingual XLSR model. Results suggest that speech representations pretrained on large unlabelled data can improve word error rate (WER) performance. In particular, features from the multilingual model led to lower WERs than filterbanks (Fbank) or models trained on a single language. Improvements were observed in English speakers with cerebral palsy caused dysarthria (UASpeech corpus), Spanish speakers with Parkinsonian dysarthria (PC-GITA corpus) and Italian speakers with paralysis-based dysarthria (EasyCall corpus). Compared to using Fbank features, XLSR-based features reduced WERs by 6.8%, 22.0%, and 7.0% for the UASpeech, PC-GITA, and EasyCall corpus, respectively.

</details>

### [A Study of Gender Impact in Self-supervised Models for Speech-to-Text Systems](2204.01397.md)
**Marcely Zanon Boito, Laurent Besacier, Natalia Tomashenko, Yannick Estève** · 2022-04-04

<details>
<summary>Abstract</summary>

Self-supervised models for speech processing emerged recently as popular foundation blocks in speech processing pipelines. These models are pre-trained on unlabeled audio data and then used in speech processing downstream tasks such as automatic speech recognition (ASR) or speech translation (ST). Since these models are now used in research and industrial systems alike, it becomes necessary to understand the impact caused by some features such as gender distribution within pre-training data. Using French as our investigation language, we train and compare gender-specific wav2vec 2.0 models against models containing different degrees of gender balance in their pre-training data. The comparison is performed by applying these models to two speech-to-text downstream tasks: ASR and ST. Results show the type of downstream integration matters. We observe lower overall performance using gender-specific pre-training before fine-tuning an end-to-end ASR system. However, when self-supervised models are used as feature extractors, the overall ASR and ST results follow more complex patterns in which the balanced pre-trained model does not necessarily lead to the best results. Lastly, our crude 'fairness' metric, the relative performance difference measured between female and male test sets, does not display a strong variation from balanced to gender-specific pre-trained wav2vec 2.0 models.

</details>

### [An Analysis of Semantically-Aligned Speech-Text Embeddings](2204.01235.md)
**Muhammad Huzaifah, Ivan Kukanov** · 2022-04-04

<details>
<summary>Abstract</summary>

Embeddings play an important role in end-to-end solutions for multi-modal language processing problems. Although there has been some effort to understand the properties of single-modality embedding spaces, particularly that of text, their cross-modal counterparts are less understood. In this work, we study some intrinsic properties of a joint speech-text embedding space, constructed by minimizing the distance between paired utterance and transcription inputs in a teacher-student model setup, that are informative for several prominent use cases. We found that incorporating automatic speech recognition through both pretraining and multitask scenarios aid semantic alignment significantly, resulting in more tightly coupled embeddings. To analyse cross-modal embeddings we utilise a quantitative retrieval accuracy metric for semantic alignment, zero-shot classification for generalisability, and probing of the encoders to observe the extent of knowledge transfer from one modality to another.

</details>

### [Deep Speech Based End-to-End Automated Speech Recognition (ASR) for Indian-English Accents](2204.00977.md)
**Priyank Dubey, Bilal Shah** · 2022-04-03

<details>
<summary>Abstract</summary>

Automated Speech Recognition (ASR) is an interdisciplinary application of computer science and linguistics that enable us to derive the transcription from the uttered speech waveform. It finds several applications in Military like High-performance fighter aircraft, helicopters, air-traffic controller. Other than military speech recognition is used in healthcare, persons with disabilities and many more. ASR has been an active research area. Several models and algorithms for speech to text (STT) have been proposed. One of the most recent is Mozilla Deep Speech, it is based on the Deep Speech research paper by Baidu. Deep Speech is a state-of-art speech recognition system is developed using end-to-end deep learning, it is trained using well-optimized Recurrent Neural Network (RNN) training system utilizing multiple Graphical Processing Units (GPUs). This training is mostly done using American-English accent datasets, which results in poor generalizability to other English accents. India is a land of vast diversity. This can even be seen in the speech, there are several English accents which vary from state to state. In this work, we have used transfer learning approach using most recent Deep Speech model i.e., deepspeech-0.9.3 to develop an end-to-end speech recognition system for Indian-English accents. This work utilizes fine-tuning and data argumentation to further optimize and improve the Deep Speech ASR system. Indic TTS data of Indian-English accents is used for transfer learning and fine-tuning the pre-trained Deep Speech model. A general comparison is made among the untrained model, our trained model and other available speech recognition services for Indian-English Accents.

</details>

### [Leveraging Phone Mask Training for Phonetic-Reduction-Robust E2E Uyghur Speech Recognition](2204.00819.md)
**Guodong Ma, Pengfei Hu, Jian Kang, Shen Huang et al.** · 2022-04-02

<details>
<summary>Abstract</summary>

In Uyghur speech, consonant and vowel reduction are often encountered, especially in spontaneous speech with high speech rate, which will cause a degradation of speech recognition performance. To solve this problem, we propose an effective phone mask training method for Conformer-based Uyghur end-to-end (E2E) speech recognition. The idea is to randomly mask off a certain percentage features of phones during model training, which simulates the above verbal phenomena and facilitates E2E model to learn more contextual information. According to experiments, the above issues can be greatly alleviated. In addition, deep investigations are carried out into different units in masking, which shows the effectiveness of our proposed masking unit. We also further study the masking method and optimize filling strategy of phone mask. Finally, compared with Conformer-based E2E baseline without mask training, our model demonstrates about 5.51% relative Word Error Rate (WER) reduction on reading speech and 12.92% on spontaneous speech, respectively. The above approach has also been verified on test-set of open-source data THUYG-20, which shows 20% relative improvements.

</details>

### [End-to-end model for named entity recognition from speech without paired training data](2204.00803.md)
**Salima Mdhaffar, Jarod Duret, Titouan Parcollet, Yannick Estève** · 2022-04-02

<details>
<summary>Abstract</summary>

Recent works showed that end-to-end neural approaches tend to become very popular for spoken language understanding (SLU). Through the term end-to-end, one considers the use of a single model optimized to extract semantic information directly from the speech signal. A major issue for such models is the lack of paired audio and textual data with semantic annotation. In this paper, we propose an approach to build an end-to-end neural model to extract semantic information in a scenario in which zero paired audio data is available. Our approach is based on the use of an external model trained to generate a sequence of vectorial representations from text. These representations mimic the hidden representations that could be generated inside an end-to-end automatic speech recognition (ASR) model by processing a speech signal. An SLU neural module is then trained using these representations as input and the annotated text as output. Last, the SLU module replaces the top layers of the ASR model to achieve the construction of the end-to-end model. Our experiments on named entity recognition, carried out on the QUAERO corpus, show that this approach is very promising, getting better results than a comparable cascade approach or than the use of synthetic voices.

</details>

### [Fast Real-time Personalized Speech Enhancement: End-to-End Enhancement Network (E3Net) and Knowledge Distillation](2204.00771.md)
**Manthan Thakker, Sefik Emre Eskimez, Takuya Yoshioka, Huaming Wang** · 2022-04-02

<details>
<summary>Abstract</summary>

This paper investigates how to improve the runtime speed of personalized speech enhancement (PSE) networks while maintaining the model quality. Our approach includes two aspects: architecture and knowledge distillation (KD). We propose an end-to-end enhancement (E3Net) model architecture, which is $3\times$ faster than a baseline STFT-based model. Besides, we use KD techniques to develop compressed student models without significantly degrading quality. In addition, we investigate using noisy data without reference clean signals for training the student models, where we combine KD with multi-task learning (MTL) using automatic speech recognition (ASR) loss. Our results show that E3Net provides better speech and transcription quality with a lower target speaker over-suppression (TSOS) rate than the baseline model. Furthermore, we show that the KD methods can yield student models that are $2-4\times$ faster than the teacher and provides reasonable quality. Combining KD and MTL improves the ASR and TSOS metrics without degrading the speech quality.

</details>

### [Speaker adaptation for Wav2vec2 based dysarthric ASR](2204.00770.md)
**Murali Karthick Baskar, Tim Herzig, Diana Nguyen, Mireia Diez et al.** · 2022-04-02

<details>
<summary>Abstract</summary>

Dysarthric speech recognition has posed major challenges due to lack of training data and heavy mismatch in speaker characteristics. Recent ASR systems have benefited from readily available pretrained models such as wav2vec2 to improve the recognition performance. Speaker adaptation using fMLLR and xvectors have provided major gains for dysarthric speech with very little adaptation data. However, integration of wav2vec2 with fMLLR features or xvectors during wav2vec2 finetuning is yet to be explored. In this work, we propose a simple adaptation network for fine-tuning wav2vec2 using fMLLR features. The adaptation network is also flexible to handle other speaker adaptive features such as xvectors. Experimental analysis show steady improvements using our proposed approach across all impairment severity levels and attains 57.72\% WER for high severity in UASpeech dataset. We also performed experiments on German dataset to substantiate the consistency of our proposed approach across diverse domains.

</details>

### [End-to-end multi-talker audio-visual ASR using an active speaker attention module](2204.00652.md)
**Richard Rose, Olivier Siohan** · 2022-04-01

<details>
<summary>Abstract</summary>

This paper presents a new approach for end-to-end audio-visual multi-talker speech recognition. The approach, referred to here as the visual context attention model (VCAM), is important because it uses the available video information to assign decoded text to one of multiple visible faces. This essentially resolves the label ambiguity issue associated with most multi-talker modeling approaches which can decode multiple label strings but cannot assign the label strings to the correct speakers. This is implemented as a transformer-transducer based end-to-end model and evaluated using a two speaker audio-visual overlapping speech dataset created from YouTube videos. It is shown in the paper that the VCAM model improves performance with respect to previously reported audio-only and audio-visual multi-talker ASR systems.

</details>

### [Multi-task RNN-T with Semantic Decoder for Streamable Spoken Language Understanding](2204.00558.md)
**Xuandi Fu, Feng-Ju Chang, Martin Radfar, Kai Wei et al.** · 2022-04-01

<details>
<summary>Abstract</summary>

End-to-end Spoken Language Understanding (E2E SLU) has attracted increasing interest due to its advantages of joint optimization and low latency when compared to traditionally cascaded pipelines. Existing E2E SLU models usually follow a two-stage configuration where an Automatic Speech Recognition (ASR) network first predicts a transcript which is then passed to a Natural Language Understanding (NLU) module through an interface to infer semantic labels, such as intent and slot tags. This design, however, does not consider the NLU posterior while making transcript predictions, nor correct the NLU prediction error immediately by considering the previously predicted word-pieces. In addition, the NLU model in the two-stage system is not streamable, as it must wait for the audio segments to complete processing, which ultimately impacts the latency of the SLU system. In this work, we propose a streamable multi-task semantic transducer model to address these considerations. Our proposed architecture predicts ASR and NLU labels auto-regressively and uses a semantic decoder to ingest both previously predicted word-pieces and slot tags while aggregating them through a fusion network. Using an industry scale SLU and a public FSC dataset, we show the proposed model outperforms the two-stage E2E SLU model for both ASR and NLU metrics.

</details>

### [End-to-End Integration of Speech Recognition, Speech Enhancement, and Self-Supervised Learning Representation](2204.00540.md)
**Xuankai Chang, Takashi Maekaku, Yuya Fujita, Shinji Watanabe** · 2022-04-01

<details>
<summary>Abstract</summary>

This work presents our end-to-end (E2E) automatic speech recognition (ASR) model targetting at robust speech recognition, called Integraded speech Recognition with enhanced speech Input for Self-supervised learning representation (IRIS). Compared with conventional E2E ASR models, the proposed E2E model integrates two important modules including a speech enhancement (SE) module and a self-supervised learning representation (SSLR) module. The SE module enhances the noisy speech. Then the SSLR module extracts features from enhanced speech to be used for speech recognition (ASR). To train the proposed model, we establish an efficient learning scheme. Evaluation results on the monaural CHiME-4 task show that the IRIS model achieves the best performance reported in the literature for the single-channel CHiME-4 benchmark (2.0% for the real development and 3.9% for the real test) thanks to the powerful pre-trained SSLR module and the fine-tuned SE module.

</details>

### [Zero-Shot Cross-lingual Aphasia Detection using Automatic Speech Recognition](2204.00448.md)
**Gerasimos Chatzoudis, Manos Plitsis, Spyridoula Stamouli, Athanasia-Lida Dimou et al.** · 2022-04-01

<details>
<summary>Abstract</summary>

Aphasia is a common speech and language disorder, typically caused by a brain injury or a stroke, that affects millions of people worldwide. Detecting and assessing Aphasia in patients is a difficult, time-consuming process, and numerous attempts to automate it have been made, the most successful using machine learning models trained on aphasic speech data. Like in many medical applications, aphasic speech data is scarce and the problem is exacerbated in so-called "low resource" languages, which are, for this task, most languages excluding English. We attempt to leverage available data in English and achieve zero-shot aphasia detection in low-resource languages such as Greek and French, by using language-agnostic linguistic features. Current cross-lingual aphasia detection approaches rely on manually extracted transcripts. We propose an end-to-end pipeline using pre-trained Automatic Speech Recognition (ASR) models that share cross-lingual speech representations and are fine-tuned for our desired low-resource languages. To further boost our ASR model's performance, we also combine it with a language model. We show that our ASR-based end-to-end pipeline offers comparable results to previous setups using human-annotated transcripts.

</details>

### [Text-To-Speech Data Augmentation for Low Resource Speech Recognition](2204.00291.md)
**Rodolfo Zevallos** · 2022-04-01

<details>
<summary>Abstract</summary>

Nowadays, the main problem of deep learning techniques used in the development of automatic speech recognition (ASR) models is the lack of transcribed data. The goal of this research is to propose a new data augmentation method to improve ASR models for agglutinative and low-resource languages. This novel data augmentation method generates both synthetic text and synthetic audio. Some experiments were conducted using the corpus of the Quechua language, which is an agglutinative and low-resource language. In this study, a sequence-to-sequence (seq2seq) model was applied to generate synthetic text, in addition to generating synthetic speech using a text-to-speech (TTS) model for Quechua. The results show that the new data augmentation method works well to improve the ASR model for Quechua. In this research, an 8.73% improvement in the word-error-rate (WER) of the ASR model is obtained using a combination of synthetic text and synthetic speech.

</details>

### [End-to-End Multi-speaker ASR with Independent Vector Analysis](2204.00218.md)
**Robin Scheibler, Wangyou Zhang, Xuankai Chang, Shinji Watanabe et al.** · 2022-04-01

<details>
<summary>Abstract</summary>

We develop an end-to-end system for multi-channel, multi-speaker automatic speech recognition. We propose a frontend for joint source separation and dereverberation based on the independent vector analysis (IVA) paradigm. It uses the fast and stable iterative source steering algorithm together with a neural source model. The parameters from the ASR module and the neural source model are optimized jointly from the ASR loss itself. We demonstrate competitive performance with previous systems using neural beamforming frontends. First, we explore the trade-offs when using various number of channels for training and testing. Second, we demonstrate that the proposed IVA frontend performs well on noisy data, even when trained on clean mixtures only. Furthermore, it extends without retraining to the separation of more speakers, which is demonstrated on mixtures of three and four speakers.

</details>

### [Alternate Intermediate Conditioning with Syllable-level and Character-level Targets for Japanese ASR](2204.00175.md)
**Yusuke Fujita, Tatsuya Komatsu, Yusuke Kida** · 2022-04-01

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition directly maps input speech to characters. However, the mapping can be problematic when several different pronunciations should be mapped into one character or when one pronunciation is shared among many different characters. Japanese ASR suffers the most from such many-to-one and one-to-many mapping problems due to Japanese kanji characters. To alleviate the problems, we introduce explicit interaction between characters and syllables using Self-conditioned connectionist temporal classification (CTC), in which the upper layers are ``self-conditioned'' on the intermediate predictions from the lower layers. The proposed method utilizes character-level and syllable-level intermediate predictions as conditioning features to deal with mutual dependency between characters and syllables. Experimental results on Corpus of Spontaneous Japanese show that the proposed method outperformed the conventional multi-task and Self-conditioned CTC methods.

</details>

### [InterAug: Augmenting Noisy Intermediate Predictions for CTC-based ASR](2204.00174.md)
**Yu Nakagome, Tatsuya Komatsu, Yusuke Fujita, Shuta Ichimura et al.** · 2022-04-01

<details>
<summary>Abstract</summary>

This paper proposes InterAug: a novel training method for CTC-based ASR using augmented intermediate representations for conditioning. The proposed method exploits the conditioning framework of self-conditioned CTC to train robust models by conditioning with "noisy" intermediate predictions. During the training, intermediate predictions are changed to incorrect intermediate predictions, and fed into the next layer for conditioning. The subsequent layers are trained to correct the incorrect intermediate predictions with the intermediate losses. By repeating the augmentation and the correction, iterative refinements, which generally require a special decoder, can be realized only with the audio encoder. To produce noisy intermediate predictions, we also introduce new augmentation: intermediate feature space augmentation and intermediate token space augmentation that are designed to simulate typical errors. The combination of the proposed InterAug framework with new augmentation allows explicit training of the robust audio encoders. In experiments using augmentations simulating deletion, insertion, and substitution error, we confirmed that the trained model acquires robustness to each error, boosting the speech recognition performance of the strong self-conditioned CTC baseline.

</details>

### [Filter-based Discriminative Autoencoders for Children Speech Recognition](2204.00164.md)
**Chiang-Lin Tai, Hung-Shin Lee, Yu Tsao, Hsin-Min Wang** · 2022-04-01

<details>
<summary>Abstract</summary>

Children speech recognition is indispensable but challenging due to the diversity of children's speech. In this paper, we propose a filter-based discriminative autoencoder for acoustic modeling. To filter out the influence of various speaker types and pitches, auxiliary information of the speaker and pitch features is input into the encoder together with the acoustic features to generate phonetic embeddings. In the training phase, the decoder uses the auxiliary information and the phonetic embedding extracted by the encoder to reconstruct the input acoustic features. The autoencoder is trained by simultaneously minimizing the ASR loss and feature reconstruction error. The framework can make the phonetic embedding purer, resulting in more accurate senone (triphone-state) scores. Evaluated on the test set of the CMU Kids corpus, our system achieves a 7.8% relative WER reduction compared to the baseline system. In the domain adaptation experiment, our system also outperforms the baseline system on the British-accent PF-STAR task.

</details>

### [WavFT: Acoustic model finetuning with labelled and unlabelled data](2204.00348.md)
**Utkarsh Chauhan, Vikas Joshi, Rupesh R. Mehta** · 2022-04-01

<details>
<summary>Abstract</summary>

Unsupervised and self-supervised learning methods have leveraged unlabelled data to improve the pretrained models. However, these methods need significantly large amount of unlabelled data and the computational cost of training models with such large amount of data can be prohibitively high. We address this issue by using unlabelled data during finetuning, instead of pretraining. We propose acoustic model finetuning (FT) using labelled and unlabelled data. The model is jointly trained to learn representations to classify senones, as well as learn contextual acoustic representations. Our training objective is a combination of cross entropy loss, suitable for classification task, and contrastive loss, suitable to learn acoustic representations. The proposed approach outperforms conventional finetuning with 11.2% and 9.19% word error rate relative (WERR) reduction on Gujarati and Bengali languages respectively.

</details>

### [Spatial Loss for Unsupervised Multi-channel Source Separation](2204.00210.md)
**Kohei Saijo, Robin Scheibler** · 2022-04-01

<details>
<summary>Abstract</summary>

We propose a spatial loss for unsupervised multi-channel source separation. The proposed loss exploits the duality of direction of arrival (DOA) and beamforming: the steering and beamforming vectors should be aligned for the target source, but orthogonal for interfering ones. The spatial loss encourages consistency between the mixing and demixing systems from a classic DOA estimator and a neural separator, respectively. With the proposed loss, we train the neural separators based on minimum variance distortionless response (MVDR) beamforming and independent vector analysis (IVA). We also investigate the effectiveness of combining our spatial loss and a signal loss, which uses the outputs of blind source separation as the reference. We evaluate our proposed method on synthetic and recorded (LibriCSS) mixtures. We find that the spatial loss is most effective to train IVA-based separators. For the neural MVDR beamformer, it performs best when combined with a signal loss. On synthetic mixtures, the proposed unsupervised loss leads to the same performance as a supervised loss in terms of word error rate. On LibriCSS, we obtain close to state-of-the-art performance without any labeled training data.

</details>

### [Perceptive, non-linear Speech Processing and Spiking Neural Networks](2204.00094.md)
**Jean Rouat, Ramin Pichevar, Stéphane Loiselle** · 2022-03-31

<details>
<summary>Abstract</summary>

Source separation and speech recognition are very difficult in the context of noisy and corrupted speech. Most conventional techniques need huge databases to estimate speech (or noise) density probabilities to perform separation or recognition. We discuss the potential of perceptive speech analysis and processing in combination with biologically plausible neural network processors. We illustrate the potential of such non-linear processing of speech on a source separation system inspired by an Auditory Scene Analysis paradigm. We also discuss a potential application in speech recognition.

</details>

### [Importance of Different Temporal Modulations of Speech: A Tale of Two Perspectives](2204.00065.md)
**Samik Sadhu, Hynek Hermansky** · 2022-03-31

<details>
<summary>Abstract</summary>

How important are different temporal speech modulations for speech recognition? We answer this question from two complementary perspectives. Firstly, we quantify the amount of phonetic \textit{information} in the modulation spectrum of speech by computing the mutual information between temporal modulations with frame-wise phoneme labels. Looking from another perspective, we ask - which speech modulations an Automatic Speech Recognition (ASR) system prefers for its operation. Data-driven weights are learned over the modulation spectrum and optimized for an end-to-end ASR task. Both methods unanimously agree that speech information is mostly contained in slow modulation. Maximum mutual information occurs around 3-6 Hz which also happens to be the range of modulations most preferred by the ASR. In addition, we show that the incorporation of this knowledge into ASRs significantly reduces their dependency on the amount of training data.

</details>

### [Pre-Training Transformer Decoder for End-to-End ASR Model with Unpaired Speech Data](2203.17113.md)
**Junyi Ao, Ziqiang Zhang, Long Zhou, Shujie Liu et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

This paper studies a novel pre-training technique with unpaired speech data, Speech2C, for encoder-decoder based automatic speech recognition (ASR). Within a multi-task learning framework, we introduce two pre-training tasks for the encoder-decoder network using acoustic units, i.e., pseudo codes, derived from an offline clustering model. One is to predict the pseudo codes via masked language modeling in encoder output, like HuBERT model, while the other lets the decoder learn to reconstruct pseudo codes autoregressively instead of generating textual scripts. In this way, the decoder learns to reconstruct original speech information with codes before learning to generate correct text. Comprehensive experiments on the LibriSpeech corpus show that the proposed Speech2C can relatively reduce the word error rate (WER) by 19.2% over the method without decoder pre-training, and also outperforms significantly the state-of-the-art wav2vec 2.0 and HuBERT on fine-tuning subsets of 10h and 100h. We release our code and model at https://github.com/microsoft/SpeechT5/tree/main/Speech2C.

</details>

### [Analyzing the factors affecting usefulness of Self-Supervised Pre-trained Representations for Speech Recognition](2203.16973.md)
**Ashish Seth, Lodagala V S V Durga Prasad, Sreyan Ghosh, S. Umesh** · 2022-03-31

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) to learn high-level speech representations has been a popular approach to building Automatic Speech Recognition (ASR) systems in low-resource settings. However, the common assumption made in literature is that a considerable amount of unlabeled data is available for the same domain or language that can be leveraged for SSL pre-training, which we acknowledge is not feasible in a real-world setting. In this paper, as part of the Interspeech Gram Vaani ASR challenge, we try to study the effect of domain, language, dataset size, and other aspects of our upstream pre-training SSL data on the final performance low-resource downstream ASR task. We also build on the continued pre-training paradigm to study the effect of prior knowledge possessed by models trained using SSL. Extensive experiments and studies reveal that the performance of ASR systems is susceptible to the data used for SSL pre-training. Their performance improves with an increase in similarity and volume of pre-training data. We believe our work will be helpful to the speech community in building better ASR systems in low-resource settings and steer research towards improving generalization in SSL-based pre-training for speech systems.

</details>

### [Memory-Efficient Training of RNN-Transducer with Sampled Softmax](2203.16868.md)
**Jaesong Lee, Lukas Lee, Shinji Watanabe** · 2022-03-31

<details>
<summary>Abstract</summary>

RNN-Transducer has been one of promising architectures for end-to-end automatic speech recognition. Although RNN-Transducer has many advantages including its strong accuracy and streaming-friendly property, its high memory consumption during training has been a critical problem for development. In this work, we propose to apply sampled softmax to RNN-Transducer, which requires only a small subset of vocabulary during training thus saves its memory consumption. We further extend sampled softmax to optimize memory consumption for a minibatch, and employ distributions of auxiliary CTC losses for sampling vocabulary to improve model accuracy. We present experimental results on LibriSpeech, AISHELL-1, and CSJ-APS, where sampled softmax greatly reduces memory consumption and still maintains the accuracy of the baseline model.

</details>

### [NeuFA: Neural Network Based End-to-End Forced Alignment with Bidirectional Attention Mechanism](2203.16838.md)
**Jingbei Li, Yi Meng, Zhiyong Wu, Helen Meng et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

Although deep learning and end-to-end models have been widely used and shown superiority in automatic speech recognition (ASR) and text-to-speech (TTS) synthesis, state-of-the-art forced alignment (FA) models are still based on hidden Markov model (HMM). HMM has limited view of contextual information and is developed with long pipelines, leading to error accumulation and unsatisfactory performance. Inspired by the capability of attention mechanism in capturing long term contextual information and learning alignments in ASR and TTS, we propose a neural network based end-to-end forced aligner called NeuFA, in which a novel bidirectional attention mechanism plays an essential role. NeuFA integrates the alignment learning of both ASR and TTS tasks in a unified framework by learning bidirectional alignment information from a shared attention matrix in the proposed bidirectional attention mechanism. Alignments are extracted from the learnt attention weights and optimized by the ASR, TTS and FA tasks in a multi-task learning manner. Experimental results demonstrate the effectiveness of our proposed model, with mean absolute error on test set drops from 25.8 ms to 23.7 ms at word level, and from 17.0 ms to 15.7 ms at phoneme level compared with state-of-the-art HMM based model.

</details>

### [A Comparative Study on Speaker-attributed Automatic Speech Recognition in Multi-party Meetings](2203.16834.md)
**Fan Yu, Zhihao Du, Shiliang Zhang, Yuxiao Lin et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

In this paper, we conduct a comparative study on speaker-attributed automatic speech recognition (SA-ASR) in the multi-party meeting scenario, a topic with increasing attention in meeting rich transcription. Specifically, three approaches are evaluated in this study. The first approach, FD-SOT, consists of a frame-level diarization model to identify speakers and a multi-talker ASR to recognize utterances. The speaker-attributed transcriptions are obtained by aligning the diarization results and recognized hypotheses. However, such an alignment strategy may suffer from erroneous timestamps due to the modular independence, severely hindering the model performance. Therefore, we propose the second approach, WD-SOT, to address alignment errors by introducing a word-level diarization model, which can get rid of such timestamp alignment dependency. To further mitigate the alignment issues, we propose the third approach, TS-ASR, which trains a target-speaker separation module and an ASR module jointly. By comparing various strategies for each SA-ASR approach, experimental results on a real meeting scenario corpus, AliMeeting, reveal that the WD-SOT approach achieves 10.7% relative reduction on averaged speaker-dependent character error rate (SD-CER), compared with the FD-SOT approach. In addition, the TS-ASR approach also outperforms the FD-SOT approach and brings 16.5% relative average SD-CER reduction.

</details>

### [Effectiveness of text to speech pseudo labels for forced alignment and cross lingual pretrained models for low resource speech recognition](2203.16823.md)
**Anirudh Gupta, Rishabh Gaur, Ankur Dhuriya, Harveen Singh Chadha et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

In the recent years end to end (E2E) automatic speech recognition (ASR) systems have achieved promising results given sufficient resources. Even for languages where not a lot of labelled data is available, state of the art E2E ASR systems can be developed by pretraining on huge amounts of high resource languages and finetune on low resource languages. For a lot of low resource languages the current approaches are still challenging, since in many cases labelled data is not available in open domain. In this paper we present an approach to create labelled data for Maithili, Bhojpuri and Dogri by utilising pseudo labels from text to speech for forced alignment. The created data was inspected for quality and then further used to train a transformer based wav2vec 2.0 ASR model. All data and models are available in open domain.

</details>

### [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](2203.16822.md)
**Juan Zuluaga-Gomez, Amrutha Prasad, Iuliia Nigmatulina, Saeed Sarfjoo et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

Recent work on self-supervised pre-training focus on leveraging large-scale unlabeled speech data to build robust end-to-end (E2E) acoustic models (AM) that can be later fine-tuned on downstream tasks e.g., automatic speech recognition (ASR). Yet, few works investigated the impact on performance when the data properties substantially differ between the pre-training and fine-tuning phases, termed domain shift. We target this scenario by analyzing the robustness of Wav2Vec 2.0 and XLS-R models on downstream ASR for a completely unseen domain, air traffic control (ATC) communications. We benchmark these two models on several open-source and challenging ATC databases with signal-to-noise ratio between 5 and 20 dB. Relative word error rate (WER) reductions between 20% to 40% are obtained in comparison to hybrid-based ASR baselines by only fine-tuning E2E acoustic models with a smaller fraction of labeled data. We analyze WERs on the low-resource scenario and gender bias carried by one ATC dataset.

</details>

### [An Empirical Study of Language Model Integration for Transducer based Speech Recognition](2203.16776.md)
**Huahuan Zheng, Keyu An, Zhijian Ou, Chen Huang et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

Utilizing text-only data with an external language model (ELM) in end-to-end RNN-Transducer (RNN-T) for speech recognition is challenging. Recently, a class of methods such as density ratio (DR) and internal language model estimation (ILME) have been developed, outperforming the classic shallow fusion (SF) method. The basic idea behind these methods is that RNN-T posterior should first subtract the implicitly learned internal language model (ILM) prior, in order to integrate the ELM. While recent studies suggest that RNN-T only learns some low-order language model information, the DR method uses a well-trained neural language model with full context, which may be inappropriate for the estimation of ILM and deteriorate the integration performance. Based on the DR method, we propose a low-order density ratio method (LODR) by replacing the estimation with a low-order weak language model. Extensive empirical experiments are conducted on both in-domain and cross-domain scenarios on English LibriSpeech & Tedlium-2 and Chinese WenetSpeech & AISHELL-1 datasets. It is shown that LODR consistently outperforms SF in all tasks, while performing generally close to ILME and better than DR in most tests.

</details>

### [CUSIDE: Chunking, Simulating Future Context and Decoding for Streaming ASR](2203.16758.md)
**Keyu An, Huahuan Zheng, Zhijian Ou, Hongyu Xiang et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

History and future contextual information are known to be important for accurate acoustic modeling. However, acquiring future context brings latency for streaming ASR. In this paper, we propose a new framework - Chunking, Simulating Future Context and Decoding (CUSIDE) for streaming speech recognition. A new simulation module is introduced to recursively simulate the future contextual frames, without waiting for future context. The simulation module is jointly trained with the ASR model using a self-supervised loss; the ASR model is optimized with the usual ASR loss, e.g., CTC-CRF as used in our experiments. Experiments show that, compared to using real future frames as right context, using simulated future context can drastically reduce latency while maintaining recognition accuracy. With CUSIDE, we obtain new state-of-the-art streaming ASR results on the AISHELL-1 dataset.

</details>

### [Exploiting Single-Channel Speech for Multi-Channel End-to-End Speech Recognition: A Comparative Study](2203.16757.md)
**Keyu An, Ji Xiao, Zhijian Ou** · 2022-03-31

<details>
<summary>Abstract</summary>

Recently, the end-to-end training approach for multi-channel ASR has shown its effectiveness, which usually consists of a beamforming front-end and a recognition back-end. However, the end-to-end training becomes more difficult due to the integration of multiple modules, particularly considering that multi-channel speech data recorded in real environments are limited in size. This raises the demand to exploit the single-channel data for multi-channel end-to-end ASR. In this paper, we systematically compare the performance of three schemes to exploit external single-channel data for multi-channel end-to-end ASR, namely back-end pre-training, data scheduling, and data simulation, under different settings such as the sizes of the single-channel data and the choices of the front-end. Extensive experiments on CHiME-4 and AISHELL-4 datasets demonstrate that while all three methods improve the multi-channel end-to-end speech recognition performance, data simulation outperforms the other two, at the cost of longer training time. Data scheduling outperforms back-end pre-training marginally but nearly consistently, presumably because that in the pre-training stage, the back-end tends to overfit on the single-channel data, especially when the single-channel data size is small.

</details>

### [Improving Speech Recognition for Indic Languages using Language Model](2203.16595.md)
**Ankur Dhuriya, Harveen Singh Chadha, Anirudh Gupta, Priyanshi Shah et al.** · 2022-03-30

<details>
<summary>Abstract</summary>

We study the effect of applying a language model (LM) on the output of Automatic Speech Recognition (ASR) systems for Indic languages. We fine-tune wav2vec $2.0$ models for $18$ Indic languages and adjust the results with language models trained on text derived from a variety of sources. Our findings demonstrate that the average Character Error Rate (CER) decreases by over $28$ \% and the average Word Error Rate (WER) decreases by about $36$ \% after decoding with LM. We show that a large LM may not provide a substantial improvement as compared to a diverse one. We also demonstrate that high quality transcriptions can be obtained on domain-specific data without retraining the ASR model and show results on biomedical domain.

</details>

### [Code Switched and Code Mixed Speech Recognition for Indic languages](2203.16578.md)
**Harveen Singh Chadha, Priyanshi Shah, Ankur Dhuriya, Neeraj Chhimwal et al.** · 2022-03-30

<details>
<summary>Abstract</summary>

Training multilingual automatic speech recognition (ASR) systems is challenging because acoustic and lexical information is typically language specific. Training multilingual system for Indic languages is even more tougher due to lack of open source datasets and results on different approaches. We compare the performance of end to end multilingual speech recognition system to the performance of monolingual models conditioned on language identification (LID). The decoding information from a multilingual model is used for language identification and then combined with monolingual models to get an improvement of 50% WER across languages. We also propose a similar technique to solve the Code Switched problem and achieve a WER of 21.77 and 28.27 over Hindi-English and Bengali-English respectively. Our work talks on how transformer based ASR especially wav2vec 2.0 can be applied in developing multilingual ASR and code switched ASR for Indic languages.

</details>

### [Using Adapters to Overcome Catastrophic Forgetting in End-to-End Automatic Speech Recognition](2203.16082.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2022-03-30

<details>
<summary>Abstract</summary>

Learning a set of tasks in sequence remains a challenge for artificial neural networks, which, in such scenarios, tend to suffer from Catastrophic Forgetting (CF). The same applies to End-to-End (E2E) Automatic Speech Recognition (ASR) models, even for monolingual tasks. In this paper, we aim to overcome CF for E2E ASR by inserting adapters, small architectures of few parameters which allow a general model to be fine-tuned to a specific task, into our model. We make these adapters task-specific, while regularizing the parameters of the model shared by all tasks, thus stimulating the model to fully exploit the adapters while keeping the shared parameters to work well for all tasks. Our method outperforms all baselines on two monolingual experiments while being more storage efficient and without requiring the storage of data from previous tasks.

</details>

### [4-bit Conformer with Native Quantization Aware Training for Speech Recognition](2203.15952.md)
**Shaojin Ding, Phoenix Meadowlark, Yanzhang He, Lukasz Lew et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Reducing the latency and model size has always been a significant research problem for live Automatic Speech Recognition (ASR) application scenarios. Along this direction, model quantization has become an increasingly popular approach to compress neural networks and reduce computation cost. Most of the existing practical ASR systems apply post-training 8-bit quantization. To achieve a higher compression rate without introducing additional performance regression, in this study, we propose to develop 4-bit ASR models with native quantization aware training, which leverages native integer operations to effectively optimize both training and inference. We conducted two experiments on state-of-the-art Conformer-based ASR models to evaluate our proposed quantization technique. First, we explored the impact of different precisions for both weight and activation quantization on the LibriSpeech dataset, and obtained a lossless 4-bit Conformer model with 5.8x size reduction compared to the float32 model. Following this, we for the first time investigated and revealed the viability of 4-bit quantization on a practical ASR system that is trained with large-scale datasets, and produced a lossless Conformer ASR model with mixed 4-bit and 8-bit weights that has 5x size reduction compared to the float32 model.

</details>

### [Recent improvements of ASR models in the face of adversarial attacks](2203.16536.md)
**Raphael Olivier, Bhiksha Raj** · 2022-03-29

<details>
<summary>Abstract</summary>

Like many other tasks involving neural networks, Speech Recognition models are vulnerable to adversarial attacks. However recent research has pointed out differences between attacks and defenses on ASR models compared to image models. Improving the robustness of ASR models requires a paradigm shift from evaluating attacks on one or a few models to a systemic approach in evaluation. We lay the ground for such research by evaluating on various architectures a representative set of adversarial attacks: targeted and untargeted, optimization and speech processing-based, white-box, black-box and targeted attacks. Our results show that the relative strengths of different attack algorithms vary considerably when changing the model architecture, and that the results of some attacks are not to be blindly trusted. They also indicate that training choices such as self-supervised pretraining can significantly impact robustness by enabling transferable perturbations. We release our source code as a package that should help future research in evaluating their attacks and defenses.

</details>

### [Shallow Fusion of Weighted Finite-State Transducer and Language Model for Text Normalization](2203.15917.md)
**Evelina Bakhturina, Yang Zhang, Boris Ginsburg** · 2022-03-29

<details>
<summary>Abstract</summary>

Text normalization (TN) systems in production are largely rule-based using weighted finite-state transducers (WFST). However, WFST-based systems struggle with ambiguous input when the normalized form is context-dependent. On the other hand, neural text normalization systems can take context into account but they suffer from unrecoverable errors and require labeled normalization datasets, which are hard to collect. We propose a new hybrid approach that combines the benefits of rule-based and neural systems. First, a non-deterministic WFST outputs all normalization candidates, and then a neural language model picks the best one -- similar to shallow fusion for automatic speech recognition. While the WFST prevents unrecoverable errors, the language model resolves contextual ambiguity. The approach is easy to extend and we show it is effective. It achieves comparable or better results than existing state-of-the-art TN models.

</details>

### [Streaming parallel transducer beam search with fast-slow cascaded encoders](2203.15773.md)
**Jay Mahadeokar, Yangyang Shi, Ke Li, Duc Le et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Streaming ASR with strict latency constraints is required in many speech recognition applications. In order to achieve the required latency, streaming ASR models sacrifice accuracy compared to non-streaming ASR models due to lack of future input context. Previous research has shown that streaming and non-streaming ASR for RNN Transducers can be unified by cascading causal and non-causal encoders. This work improves upon this cascaded encoders framework by leveraging two streaming non-causal encoders with variable input context sizes that can produce outputs at different audio intervals (e.g. fast and slow). We propose a novel parallel time-synchronous beam search algorithm for transducers that decodes from fast-slow encoders, where the slow encoder corrects the mistakes generated from the fast encoder. The proposed algorithm, achieves up to 20% WER reduction with a slight increase in token emission delays on the public Librispeech dataset and in-house datasets. We also explore techniques to reduce the computation by distributing processing between the fast and slow encoders. Lastly, we explore sharing the parameters in the fast encoder to reduce the memory footprint. This enables low latency processing on edge devices with low computation cost and a low memory footprint.

</details>

### [Integrating Lattice-Free MMI into End-to-End Speech Recognition](2203.15614.md)
**Jinchuan Tian, Jianwei Yu, Chao Weng, Yuexian Zou et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR) research, discriminative criteria have achieved superior performance in DNN-HMM systems. Given this success, the adoption of discriminative criteria is promising to boost the performance of end-to-end (E2E) ASR systems. With this motivation, previous works have introduced the minimum Bayesian risk (MBR, one of the discriminative criteria) into E2E ASR systems. However, the effectiveness and efficiency of the MBR-based methods are compromised: the MBR criterion is only used in system training, which creates a mismatch between training and decoding; the on-the-fly decoding process in MBR-based methods results in the need for pre-trained models and slow training speeds. To this end, novel algorithms are proposed in this work to integrate another widely used discriminative criterion, lattice-free maximum mutual information (LF-MMI), into E2E ASR systems not only in the training stage but also in the decoding process. The proposed LF-MMI training and decoding methods show their effectiveness on two widely used E2E frameworks: Attention-Based Encoder-Decoders (AEDs) and Neural Transducers (NTs). Compared with MBR-based methods, the proposed LF-MMI method: maintains the consistency between training and decoding; eschews the on-the-fly decoding process; trains from randomly initialized models with superior training efficiency. Experiments suggest that the LF-MMI method outperforms its MBR counterparts and consistently leads to statistically significant performance improvements on various frameworks and datasets from 30 hours to 14.3k hours. The proposed method achieves state-of-the-art (SOTA) results on Aishell-1 (CER 4.10%) and Aishell-2 (CER 5.02%) datasets. Code is released.

</details>

### [Dynamic Latency for CTC-Based Streaming Automatic Speech Recognition With Emformer](2203.15613.md)
**Jingyu Sun, Guiping Zhong, Dinghao Zhou, Baoxiang Li** · 2022-03-29

<details>
<summary>Abstract</summary>

An inferior performance of the streaming automatic speech recognition models versus non-streaming model is frequently seen due to the absence of future context. In order to improve the performance of the streaming model and reduce the computational complexity, a frame-level model using efficient augment memory transformer block and dynamic latency training method is employed for streaming automatic speech recognition in this paper. The long-range history context is stored into the augment memory bank as a complement to the limited history context used in the encoder. Key and value are cached by a cache mechanism and reused for next chunk to reduce computation. Afterwards, a dynamic latency training method is proposed to obtain better performance and support low and high latency inference simultaneously. Our experiments are conducted on benchmark 960h LibriSpeech data set. With an average latency of 640ms, our model achieves a relative WER reduction of 6.0% on test-clean and 3.0% on test-other versus the truncate chunk-wise Transformer.

</details>

### [Locality Matters: A Locality-Biased Linear Attention for Automatic Speech Recognition](2203.15609.md)
**Jingyu Sun, Guiping Zhong, Dinghao Zhou, Baoxiang Li et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Conformer has shown a great success in automatic speech recognition (ASR) on many public benchmarks. One of its crucial drawbacks is the quadratic time-space complexity with respect to the input sequence length, which prohibits the model to scale-up as well as process longer input audio sequences. To solve this issue, numerous linear attention methods have been proposed. However, these methods often have limited performance on ASR as they treat tokens equally in modeling, neglecting the fact that the neighbouring tokens are often more connected than the distanced tokens. In this paper, we take this fact into account and propose a new locality-biased linear attention for Conformer. It not only achieves higher accuracy than the vanilla Conformer, but also enjoys linear space-time computational complexity. To be specific, we replace the softmax attention with a locality-biased linear attention (LBLA) mechanism in Conformer blocks. The LBLA contains a kernel function to ensure the linear complexities and a cosine reweighing matrix to impose more weights on neighbouring tokens. Extensive experiments on the LibriSpeech corpus show that by introducing this locality bias to the Conformer, our method achieves a lower word error rate with more than 22% inference speed.

</details>

### [Frequency-Directional Attention Model for Multilingual Automatic Speech Recognition](2203.15473.md)
**Akihiro Dobashi, Chee Siang Leow, Hiromitsu Nishizaki** · 2022-03-29

<details>
<summary>Abstract</summary>

This paper proposes a model for transforming speech features using the frequency-directional attention model for End-to-End (E2E) automatic speech recognition. The idea is based on the hypothesis that in the phoneme system of each language, the characteristics of the frequency bands of speech when uttering them are different. By transforming the input Mel filter bank features with an attention model that characterizes the frequency direction, a feature transformation suitable for ASR in each language can be expected. This paper introduces a Transformer-encoder as a frequency-directional attention model. We evaluated the proposed method on a multilingual E2E ASR system for six different languages and found that the proposed method could achieve, on average, 5.3 points higher accuracy than the ASR model for each language by introducing the frequency-directional attention mechanism. Furthermore, visualization of the attention weights based on the proposed method suggested that it is possible to transform acoustic features considering the frequency characteristics of each language.

</details>

### [WeNet 2.0: More Productive End-to-End Speech Recognition Toolkit](2203.15455.md)
**Binbin Zhang, Di Wu, Zhendong Peng, Xingchen Song et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Recently, we made available WeNet, a production-oriented end-to-end speech recognition toolkit, which introduces a unified two-pass (U2) framework and a built-in runtime to address the streaming and non-streaming decoding modes in a single model. To further improve ASR performance and facilitate various production requirements, in this paper, we present WeNet 2.0 with four important updates. (1) We propose U2++, a unified two-pass framework with bidirectional attention decoders, which includes the future contextual information by a right-to-left attention decoder to improve the representative ability of the shared encoder and the performance during the rescoring stage. (2) We introduce an n-gram based language model and a WFST-based decoder into WeNet 2.0, promoting the use of rich text data in production scenarios. (3) We design a unified contextual biasing framework, which leverages user-specific context (e.g., contact lists) to provide rapid adaptation ability for production and improves ASR accuracy in both with-LM and without-LM scenarios. (4) We design a unified IO to support large-scale data for effective model training. In summary, the brand-new WeNet 2.0 achieves up to 10\% relative recognition performance improvement over the original WeNet on various corpora and makes available several important production-oriented features.

</details>

### [Investigating Self-supervised Pretraining Frameworks for Pathological Speech Recognition](2203.15431.md)
**Lester Phillip Violeta, Wen-Chin Huang, Tomoki Toda** · 2022-03-29

<details>
<summary>Abstract</summary>

We investigate the performance of self-supervised pretraining frameworks on pathological speech datasets used for automatic speech recognition (ASR). Modern end-to-end models require thousands of hours of data to train well, but only a small number of pathological speech datasets are publicly available. A proven solution to this problem is by first pretraining the model on a huge number of healthy speech datasets and then fine-tuning it on the pathological speech datasets. One new pretraining framework called self-supervised learning (SSL) trains a network using only speech data, providing more flexibility in training data requirements and allowing more speech data to be used in pretraining. We investigate SSL frameworks such as the wav2vec 2.0 and WavLM models using different setups and compare their performance with different supervised pretraining setups, using two types of pathological speech, namely, Japanese electrolaryngeal and English dysarthric. Our results show that although SSL has shown success with minimally resourced healthy speech, we do not find this to be the case with pathological speech. The best supervised setup outperforms the best SSL setup by 13.9% character error rate in electrolaryngeal speech and 16.8% word error rate in dysarthric speech.

</details>

### [Short-Term Word-Learning in a Dynamically Changing Environment](2203.15404.md)
**Christian Huber, Rishu Kumar, Ondřej Bojar, Alexander Waibel** · 2022-03-29

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence automatic speech recognition (ASR) systems are in principle open vocabulary systems, when using appropriate modeling units. In practice, however, they often fail to recognize words not seen during training, e.g., named entities, numbers or technical terms. To alleviate this problem, Huber et al. proposed to supplement an end-to-end ASR system with a word/phrase memory and a mechanism to access this memory to recognize the words and phrases correctly. In this paper we study, a) methods to acquire important words for this memory dynamically and, b) the trade-off between improvement in recognition accuracy of new words and the potential danger of false alarms for those added words. We demonstrate significant improvements in the detection rate of new words with only a minor increase in false alarms (F1 score 0.30 $\rightarrow$ 0.80), when using an appropriate number of new words. In addition, we show that important keywords can be extracted from supporting documents and used effectively.

</details>

### [Noise-robust Speech Recognition with 10 Minutes Unparalleled In-domain Data](2203.15321.md)
**Chen Chen, Nana Hou, Yuchen Hu, Shashank Shirol et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Noise-robust speech recognition systems require large amounts of training data including noisy speech data and corresponding transcripts to achieve state-of-the-art performances in face of various practical environments. However, such plenty of in-domain data is not always available in the real-life world. In this paper, we propose a generative adversarial network to simulate noisy spectrum from the clean spectrum (Simu-GAN), where only 10 minutes of unparalleled in-domain noisy speech data is required as labels. Furthermore, we also propose a dual-path speech recognition system to improve the robustness of the system under noisy conditions. Experimental results show that the proposed speech recognition system achieves 7.3% absolute improvement with simulated noisy data by Simu-GAN over the best baseline in terms of word error rate (WER).

</details>

### [Mel Frequency Spectral Domain Defenses against Adversarial Attacks on Speech Recognition Systems](2203.15283.md)
**Nicholas Mehlman, Anirudh Sreeram, Raghuveer Peri, Shrikanth Narayanan** · 2022-03-29

<details>
<summary>Abstract</summary>

A variety of recent works have looked into defenses for deep neural networks against adversarial attacks particularly within the image processing domain. Speech processing applications such as automatic speech recognition (ASR) are increasingly relying on deep learning models, and so are also prone to adversarial attacks. However, many of the defenses explored for ASR simply adapt the image-domain defenses, which may not provide optimal robustness. This paper explores speech specific defenses using the mel spectral domain, and introduces a novel defense method called 'mel domain noise flooding' (MDNF). MDNF applies additive noise to the mel spectrogram of a speech utterance prior to re-synthesising the audio signal. We test the defenses against strong white-box adversarial attacks such as projected gradient descent (PGD) and Carlini-Wagner (CW) attacks, and show better robustness compared to a randomized smoothing baseline across strong threat models.

</details>

### [Shifted Chunk Encoder for Transformer Based Streaming End-to-End ASR](2203.15206.md)
**Fangyuan Wang, Bo Xu** · 2022-03-29

<details>
<summary>Abstract</summary>

Currently, there are mainly three kinds of Transformer encoder based streaming End to End (E2E) Automatic Speech Recognition (ASR) approaches, namely time-restricted methods, chunk-wise methods, and memory-based methods. Generally, all of them have limitations in aspects of linear computational complexity, global context modeling, and parallel training. In this work, we aim to build a model to take all these three advantages for streaming Transformer ASR. Particularly, we propose a shifted chunk mechanism for the chunk-wise Transformer which provides cross-chunk connections between chunks. Therefore, the global context modeling ability of chunk-wise models can be significantly enhanced while all the original merits inherited. We integrate this scheme with the chunk-wise Transformer and Conformer, and identify them as SChunk-Transformer and SChunk-Conformer, respectively. Experiments on AISHELL-1 show that the SChunk-Transformer and SChunk-Conformer can respectively achieve CER 6.43% and 5.77%. And the linear complexity makes them possible to train with large batches and infer more efficiently. Our models can significantly outperform their conventional chunk-wise counterparts, while being competitive, with only 0.22 absolute CER drop, when compared with U2 which has quadratic complexity. A better CER can be achieved if compared with existing chunk-wise or memory-based methods, such as HS-DACS and MMA. Code is released.

</details>

### [Improving Generalization of Deep Neural Network Acoustic Models with Length Perturbation and N-best Based Label Smoothing](2203.15176.md)
**Xiaodong Cui, George Saon, Tohru Nagano, Masayuki Suzuki et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

We introduce two techniques, length perturbation and n-best based label smoothing, to improve generalization of deep neural network (DNN) acoustic models for automatic speech recognition (ASR). Length perturbation is a data augmentation algorithm that randomly drops and inserts frames of an utterance to alter the length of the speech feature sequence. N-best based label smoothing randomly injects noise to ground truth labels during training in order to avoid overfitting, where the noisy labels are generated from n-best hypotheses. We evaluate these two techniques extensively on the 300-hour Switchboard (SWB300) dataset and an in-house 500-hour Japanese (JPN500) dataset using recurrent neural network transducer (RNNT) acoustic models for ASR. We show that both techniques improve the generalization of RNNT models individually and they can also be complementary. In particular, they yield good improvements over a strong SWB300 baseline and give state-of-art performance on SWB300 using RNNT models.

</details>

### [CMGAN: Conformer-based Metric GAN for Speech Enhancement](2203.15149.md)
**Ruizhe Cao, Sherif Abdulatif, Bin Yang** · 2022-03-28

<details>
<summary>Abstract</summary>

Recently, convolution-augmented transformer (Conformer) has achieved promising performance in automatic speech recognition (ASR) and time-domain speech enhancement (SE), as it can capture both local and global dependencies in the speech signal. In this paper, we propose a conformer-based metric generative adversarial network (CMGAN) for SE in the time-frequency (TF) domain. In the generator, we utilize two-stage conformer blocks to aggregate all magnitude and complex spectrogram information by modeling both time and frequency dependencies. The estimation of magnitude and complex spectrogram is decoupled in the decoder stage and then jointly incorporated to reconstruct the enhanced speech. In addition, a metric discriminator is employed to further improve the quality of the enhanced estimated speech by optimizing the generator with respect to a corresponding evaluation score. Quantitative analysis on Voice Bank+DEMAND dataset indicates the capability of CMGAN in outperforming various previous models with a margin, i.e., PESQ of 3.41 and SSNR of 11.10 dB.

</details>

### [Finnish Parliament ASR corpus - Analysis, benchmarks and statistics](2203.14876.md)
**Anja Virkkunen, Aku Rouhe, Nhan Phan, Mikko Kurimo** · 2022-03-28

<details>
<summary>Abstract</summary>

Public sources like parliament meeting recordings and transcripts provide ever-growing material for the training and evaluation of automatic speech recognition (ASR) systems. In this paper, we publish and analyse the Finnish parliament ASR corpus, the largest publicly available collection of manually transcribed speech data for Finnish with over 3000 hours of speech and 449 speakers for which it provides rich demographic metadata. This corpus builds on earlier initial work, and as a result the corpus has a natural split into two training subsets from two periods of time. Similarly, there are two official, corrected test sets covering different times, setting an ASR task with longitudinal distribution-shift characteristics. An official development set is also provided. We develop a complete Kaldi-based data preparation pipeline, and hidden Markov model (HMM), hybrid deep neural network (HMM-DNN) and attention-based encoder-decoder (AED) ASR recipes. We set benchmarks on the official test sets, as well as multiple other recently used test sets. Both temporal corpus subsets are already large, and we observe that beyond their scale, ASR performance on the official test sets plateaus, whereas other domains benefit from added data. The HMM-DNN and AED approaches are compared in a carefully matched equal data setting, with the HMM-DNN system consistently performing better. Finally, the variation of the ASR accuracy is compared between the speaker categories available in the parliament metadata to detect potential biases based on factors such as gender, age, and education.

</details>

### [Dual-Path Style Learning for End-to-End Noise-Robust Speech Recognition](2203.14838.md)
**Yuchen Hu, Nana Hou, Chen Chen, Eng Siong Chng** · 2022-03-28

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems degrade significantly under noisy conditions. Recently, speech enhancement (SE) is introduced as front-end to reduce noise for ASR, but it also suppresses some important speech information, i.e., over-suppression. To alleviate this, we propose a dual-path style learning approach for end-to-end noise-robust speech recognition (DPSL-ASR). Specifically, we first introduce clean speech feature along with the fused feature from IFF-Net as dual-path inputs to recover the suppressed information. Then, we propose style learning to map the fused feature close to clean feature, in order to learn latent speech information from the latter, i.e., clean "speech style". Furthermore, we also minimize the distance of final ASR outputs in two paths to improve noise-robustness. Experiments show that the proposed approach achieves relative word error rate (WER) reductions of 10.6% and 8.6% over the best IFF-Net baseline, on RATS and CHiME-4 datasets respectively.

</details>

### [The MIT Voice Name System](2204.09657.md)
**Brian Subirana, Harry Levinson, Ferran Hueto, Prithvi Rajasekaran et al.** · 2022-03-28

<details>
<summary>Abstract</summary>

This RFC white Paper summarizes our progress on the MIT Voice Name System (VNS) and Huey. The VNS, similar in name and function to the DNS, is a system to reserve and use "wake words" to activate Artificial Intelligence (AI) devices. Just like you can say "Hey Siri" to activate Apple's personal assistant, we propose using the VNS in smart speakers and other devices to route wake requests based on commands such as "turn off", "open grocery shopping list" or "271, start flash card review of my computer vision class". We also introduce Huey, an unambiguous Natural Language to interact with AI devices. We aim to standardize voice interactions to a universal reach similar to that of other systems such as phone numbering, with an agreed world-wide approach to assign and use numbers, or the Internet's DNS, with a standard naming system, that has helped flourish popular services including the World-Wide-Web, FTP, and email. Just like these standards are "neutral", we also aim to endow the VNS with "wake neutrality" so that each participant can develop its own digital voice. We focus on voice as a starting point to talk to any IoT object and explain briefly how the VNS may be expanded to other AI technologies enabling person-to-machine conversations (really machine-to-machine), including computer vision or neural interfaces. We also describe briefly considerations for a broader set of standards, MIT Open AI (MOA), including a reference architecture to serve as a starting point for the development of a general conversational commerce infrastructure that has standard "Wake Words", NLP commands such as "Shopping Lists" or "Flash Card Reviews", and personalities such as Pi or 271. Privacy and security are key elements considered because of speech-to-text errors and the amount of personal information contained in a voice sample.

</details>

### [Listen, Adapt, Better WER: Source-free Single-utterance Test-time Adaptation for Automatic Speech Recognition](2203.14222.md)
**Guan-Ting Lin, Shang-Wen Li, Hung-yi Lee** · 2022-03-27

<details>
<summary>Abstract</summary>

Although deep learning-based end-to-end Automatic Speech Recognition (ASR) has shown remarkable performance in recent years, it suffers severe performance regression on test samples drawn from different data distributions. Test-time Adaptation (TTA), previously explored in the computer vision area, aims to adapt the model trained on source domains to yield better predictions for test samples, often out-of-domain, without accessing the source data. Here, we propose the Single-Utterance Test-time Adaptation (SUTA) framework for ASR, which is the first TTA study on ASR to our best knowledge. The single-utterance TTA is a more realistic setting that does not assume test data are sampled from identical distribution and does not delay on-demand inference due to pre-collection for the batch of adaptation data. SUTA consists of unsupervised objectives with an efficient adaptation strategy. Empirical results demonstrate that SUTA effectively improves the performance of the source ASR model evaluated on multiple out-of-domain target corpora and in-domain test samples.

</details>

### [Speech-enhanced and Noise-aware Networks for Robust Speech Recognition](2203.13696.md)
**Hung-Shin Lee, Pin-Yuan Chen, Yao-Fei Cheng, Yu Tsao et al.** · 2022-03-25

<details>
<summary>Abstract</summary>

Compensation for channel mismatch and noise interference is essential for robust automatic speech recognition. Enhanced speech has been introduced into the multi-condition training of acoustic models to improve their generalization ability. In this paper, a noise-aware training framework based on two cascaded neural structures is proposed to jointly optimize speech enhancement and speech recognition. The feature enhancement module is composed of a multi-task autoencoder, where noisy speech is decomposed into clean speech and noise. By concatenating its enhanced, noise-aware, and noisy features for each frame, the acoustic-modeling module maps each feature-augmented frame into a triphone state by optimizing the lattice-free maximum mutual information and cross entropy between the predicted and actual state sequences. On top of the factorized time delay neural network (TDNN-F) and its convolutional variant (CNN-TDNNF), both with SpecAug, the two proposed systems achieve word error rate (WER) of 3.90% and 3.55%, respectively, on the Aurora-4 task. Compared with the best existing systems that use bigram and trigram language models for decoding, the proposed CNN-TDNNF-based system achieves a relative WER reduction of 15.20% and 33.53%, respectively. In addition, the proposed CNN-TDNNF-based system also outperforms the baseline CNN-TDNNF system on the AMI task.

</details>

### [Chain-based Discriminative Autoencoders for Speech Recognition](2203.13687.md)
**Hung-Shin Lee, Pin-Tuan Huang, Yao-Fei Cheng, Hsin-Min Wang** · 2022-03-25

<details>
<summary>Abstract</summary>

In our previous work, we proposed a discriminative autoencoder (DcAE) for speech recognition. DcAE combines two training schemes into one. First, since DcAE aims to learn encoder-decoder mappings, the squared error between the reconstructed speech and the input speech is minimized. Second, in the code layer, frame-based phonetic embeddings are obtained by minimizing the categorical cross-entropy between ground truth labels and predicted triphone-state scores. DcAE is developed based on the Kaldi toolkit by treating various TDNN models as encoders. In this paper, we further propose three new versions of DcAE. First, a new objective function that considers both categorical cross-entropy and mutual information between ground truth and predicted triphone-state sequences is used. The resulting DcAE is called a chain-based DcAE (c-DcAE). For application to robust speech recognition, we further extend c-DcAE to hierarchical and parallel structures, resulting in hc-DcAE and pc-DcAE. In these two models, both the error between the reconstructed noisy speech and the input noisy speech and the error between the enhanced speech and the reference clean speech are taken into the objective function. Experimental results on the WSJ and Aurora-4 corpora show that our DcAE models outperform baseline systems.

</details>

### [Impact of Dataset on Acoustic Models for Automatic Speech Recognition](2203.13590.md)
**Siddhesh Singh** · 2022-03-25

<details>
<summary>Abstract</summary>

In Automatic Speech Recognition, GMM-HMM had been widely used for acoustic modelling. With the current advancement of deep learning, the Gaussian Mixture Model (GMM) from acoustic models has been replaced with Deep Neural Network, namely DNN-HMM Acoustic Models. The GMM models are widely used to create the alignments of the training data for the hybrid deep neural network model, thus making it an important task to create accurate alignments. Many factors such as training dataset size, training data augmentation, model hyperparameters, etc., affect the model learning. Traditionally in machine learning, larger datasets tend to have better performance, while smaller datasets tend to trigger over-fitting. The collection of speech data and their accurate transcriptions is a significant challenge that varies over different languages, and in most cases, it might be limited to big organizations. Moreover, in the case of available large datasets, training a model using such data requires additional time and computing resources, which may not be available. While the data about the accuracy of state-of-the-art ASR models on open-source datasets are published, the study about the impact of the size of a dataset on acoustic models is not readily available. This work aims to investigate the impact of dataset size variations on the performance of various GMM-HMM Acoustic Models and their respective computational costs.

</details>

### [Building Robust Spoken Language Understanding by Cross Attention between Phoneme Sequence and ASR Hypothesis](2203.12067.md)
**Zexun Wang, Yuquan Le, Yi Zhu, Yuming Zhao et al.** · 2022-03-22

<details>
<summary>Abstract</summary>

Building Spoken Language Understanding (SLU) robust to Automatic Speech Recognition (ASR) errors is an essential issue for various voice-enabled virtual assistants. Considering that most ASR errors are caused by phonetic confusion between similar-sounding expressions, intuitively, leveraging the phoneme sequence of speech can complement ASR hypothesis and enhance the robustness of SLU. This paper proposes a novel model with Cross Attention for SLU (denoted as CASLU). The cross attention block is devised to catch the fine-grained interactions between phoneme and word embeddings in order to make the joint representations catch the phonetic and semantic features of input simultaneously and for overcoming the ASR errors in downstream natural language understanding (NLU) tasks. Extensive experiments are conducted on three datasets, showing the effectiveness and competitiveness of our approach. Additionally, We also validate the universality of CASLU and prove its complementarity when combining with other robust SLU techniques.

</details>

### [A Text-to-Speech Pipeline, Evaluation Methodology, and Initial Fine-Tuning Results for Child Speech Synthesis](2203.11562.md)
**Rishabh Jain, Mariam Yiwere, Dan Bigioi, Peter Corcoran et al.** · 2022-03-22

<details>
<summary>Abstract</summary>

Speech synthesis has come a long way as current text-to-speech (TTS) models can now generate natural human-sounding speech. However, most of the TTS research focuses on using adult speech data and there has been very limited work done on child speech synthesis. This study developed and validated a training pipeline for fine-tuning state-of-the-art (SOTA) neural TTS models using child speech datasets. This approach adopts a multi-speaker TTS retuning workflow to provide a transfer-learning pipeline. A publicly available child speech dataset was cleaned to provide a smaller subset of approximately 19 hours, which formed the basis of our fine-tuning experiments. Both subjective and objective evaluations were performed using a pretrained MOSNet for objective evaluation and a novel subjective framework for mean opinion score (MOS) evaluations. Subjective evaluations achieved the MOS of 3.95 for speech intelligibility, 3.89 for voice naturalness, and 3.96 for voice consistency. Objective evaluation using a pretrained MOSNet showed a strong correlation between real and synthetic child voices. Speaker similarity was also verified by calculating the cosine similarity between the embeddings of utterances. An automatic speech recognition (ASR) model is also used to provide a word error rate (WER) comparison between the real and synthetic child voices. The final trained TTS model was able to synthesize child-like speech from reference audio samples as short as 5 seconds.

</details>

### [Modeling speech recognition and synthesis simultaneously: Encoding and decoding lexical and sublexical semantic information into speech with no direct access to speech data](2203.11476.md)
**Gašper Beguš, Alan Zhou** · 2022-03-22

<details>
<summary>Abstract</summary>

Human speakers encode information into raw speech which is then decoded by the listeners. This complex relationship between encoding (production) and decoding (perception) is often modeled separately. Here, we test how encoding and decoding of lexical semantic information can emerge automatically from raw speech in unsupervised generative deep convolutional networks that combine the production and perception principles of speech. We introduce, to our knowledge, the most challenging objective in unsupervised lexical learning: a network that must learn unique representations for lexical items with no direct access to training data. We train several models (ciwGAN and fiwGAN arXiv:2006.02951) and test how the networks classify acoustic lexical items in unobserved test data. Strong evidence in favor of lexical learning and a causal relationship between latent codes and meaningful sublexical units emerge. The architecture that combines the production and perception principles is thus able to learn to decode unique information from raw acoustic data without accessing real training data directly. We propose a technique to explore lexical (holistic) and sublexical (featural) learned representations in the classifier network. The results bear implications for unsupervised speech technology, as well as for unsupervised semantic modeling as language models increasingly bypass text and operate from raw acoustics.

</details>

### [Pseudo Label Is Better Than Human Label](2203.12668.md)
**Dongseong Hwang, Khe Chai Sim, Zhouyuan Huo, Trevor Strohman** · 2022-03-22

<details>
<summary>Abstract</summary>

State-of-the-art automatic speech recognition (ASR) systems are trained with tens of thousands of hours of labeled speech data. Human transcription is expensive and time consuming. Factors such as the quality and consistency of the transcription can greatly affect the performance of the ASR models trained with these data. In this paper, we show that we can train a strong teacher model to produce high quality pseudo labels by utilizing recent self-supervised and semi-supervised learning techniques. Specifically, we use JUST (Joint Unsupervised/Supervised Training) and iterative noisy student teacher training to train a 600 million parameter bi-directional teacher model. This model achieved 4.0% word error rate (WER) on a voice search task, 11.1% relatively better than a baseline. We further show that by using this strong teacher model to generate high-quality pseudo labels for training, we can achieve 13.6% relative WER reduction (5.9% to 5.1%) for a streaming model compared to using human labels.

</details>

### [Enhancing Speech Recognition Decoding via Layer Aggregation](2203.11325.md)
**Tomer Wullach, Shlomo E. Chazan** · 2022-03-21

<details>
<summary>Abstract</summary>

Recently proposed speech recognition systems are designed to predict using representations generated by their top layers, employing greedy decoding which isolates each timestep from the rest of the sequence. Aiming for improved performance, a beam search algorithm is frequently utilized and a language model is incorporated to assist with ranking the top candidates. In this work, we experiment with several speech recognition models and find that logits predicted using the top layers may hamper beam search from achieving optimal results. Specifically, we show that fined-tuned Wav2Vec 2.0 and HuBERT yield highly confident predictions, and hypothesize that the predictions are based on local information and may not take full advantage of the information encoded in intermediate layers. To this end, we perform a layer analysis to reveal and visualize how predictions evolve throughout the inference flow. We then propose a prediction method that aggregates the top M layers, potentially leveraging useful information encoded in intermediate layers and relaxing model confidence. We showcase the effectiveness of our approach via beam search decoding, conducting our experiments on Librispeech test and dev sets and achieving WER, and CER reduction of up to 10% and 22%, respectively.

</details>

### [XTREME-S: Evaluating Cross-lingual Speech Representations](2203.10752.md)
**Alexis Conneau, Ankur Bapna, Yu Zhang, Min Ma et al.** · 2022-03-21

<details>
<summary>Abstract</summary>

We introduce XTREME-S, a new benchmark to evaluate universal cross-lingual speech representations in many languages. XTREME-S covers four task families: speech recognition, classification, speech-to-text translation and retrieval. Covering 102 languages from 10+ language families, 3 different domains and 4 task families, XTREME-S aims to simplify multilingual speech representation evaluation, as well as catalyze research in "universal" speech representation learning. This paper describes the new benchmark and establishes the first speech-only and speech-text baselines using XLS-R and mSLAM on all downstream tasks. We motivate the design choices and detail how to use the benchmark. Datasets and fine-tuning scripts are made easily accessible at https://hf.co/datasets/google/xtreme_s.

</details>

### [STEMM: Self-learning with Speech-text Manifold Mixup for Speech Translation](2203.10426.md)
**Qingkai Fang, Rong Ye, Lei Li, Yang Feng et al.** · 2022-03-20

<details>
<summary>Abstract</summary>

How to learn a better speech representation for end-to-end speech-to-text translation (ST) with limited labeled data? Existing techniques often attempt to transfer powerful machine translation (MT) capabilities to ST, but neglect the representation discrepancy across modalities. In this paper, we propose the Speech-TExt Manifold Mixup (STEMM) method to calibrate such discrepancy. Specifically, we mix up the representation sequences of different modalities, and take both unimodal speech sequences and multimodal mixed sequences as input to the translation model in parallel, and regularize their output predictions with a self-learning framework. Experiments on MuST-C speech translation benchmark and further analysis show that our method effectively alleviates the cross-modal representation discrepancy, and achieves significant improvements over a strong baseline on eight translation directions.

</details>

### [Exploiting Cross Domain Acoustic-to-articulatory Inverted Features For Disordered Speech Recognition](2203.10274.md)
**Shujie Hu, Shansong Liu, Xurong Xie, Mengzhe Geng et al.** · 2022-03-19

<details>
<summary>Abstract</summary>

Articulatory features are inherently invariant to acoustic signal distortion and have been successfully incorporated into automatic speech recognition (ASR) systems for normal speech. Their practical application to disordered speech recognition is often limited by the difficulty in collecting such specialist data from impaired speakers. This paper presents a cross-domain acoustic-to-articulatory (A2A) inversion approach that utilizes the parallel acoustic-articulatory data of the 15-hour TORGO corpus in model training before being cross-domain adapted to the 102.7-hour UASpeech corpus and to produce articulatory features. Mixture density networks based neural A2A inversion models were used. A cross-domain feature adaptation network was also used to reduce the acoustic mismatch between the TORGO and UASpeech data. On both tasks, incorporating the A2A generated articulatory features consistently outperformed the baseline hybrid DNN/TDNN, CTC and Conformer based end-to-end systems constructed using acoustic features only. The best multi-modal system incorporating video modality and the cross-domain articulatory features as well as data augmentation and learning hidden unit contributions (LHUC) speaker adaptation produced the lowest published word error rate (WER) of 24.82% on the 16 dysarthric speakers of the benchmark UASpeech task.

</details>

### [Similarity and Content-based Phonetic Self Attention for Speech Recognition](2203.10252.md)
**Kyuhong Shim, Wonyong Sung** · 2022-03-19

<details>
<summary>Abstract</summary>

Transformer-based speech recognition models have achieved great success due to the self-attention (SA) mechanism that utilizes every frame in the feature extraction process. Especially, SA heads in lower layers capture various phonetic characteristics by the query-key dot product, which is designed to compute the pairwise relationship between frames. In this paper, we propose a variant of SA to extract more representative phonetic features. The proposed phonetic self-attention (phSA) is composed of two different types of phonetic attention; one is similarity-based and the other is content-based. In short, similarity-based attention captures the correlation between frames while content-based attention only considers each frame without being affected by other frames. We identify which parts of the original dot product equation are related to two different attention patterns and improve each part with simple modifications. Our experiments on phoneme classification and speech recognition show that replacing SA with phSA for lower layers improves the recognition performance without increasing the latency and the parameter size.

</details>

### [Neural Predictor for Black-Box Adversarial Attacks on Speech Recognition](2203.09849.md)
**Marie Biolková, Bac Nguyen** · 2022-03-18

<details>
<summary>Abstract</summary>

Recent works have revealed the vulnerability of automatic speech recognition (ASR) models to adversarial examples (AEs), i.e., small perturbations that cause an error in the transcription of the audio signal. Studying audio adversarial attacks is therefore the first step towards robust ASR. Despite the significant progress made in attacking audio examples, the black-box attack remains challenging because only the hard-label information of transcriptions is provided. Due to this limited information, existing black-box methods often require an excessive number of queries to attack a single audio example. In this paper, we introduce NP-Attack, a neural predictor-based method, which progressively evolves the search towards a small adversarial perturbation. Given a perturbation direction, our neural predictor directly estimates the smallest perturbation that causes a mistranscription. In particular, it enables NP-Attack to accurately learn promising perturbation directions via gradient-based optimization. Experimental results show that NP-Attack achieves competitive results with other state-of-the-art black-box adversarial attacks while requiring a significantly smaller number of queries. The code of NP-Attack is available online.

</details>

### [Representative Subset Selection for Efficient Fine-Tuning in Self-Supervised Speech Recognition](2203.09829.md)
**Abdul Hameed Azeemi, Ihsan Ayyub Qazi, Agha Ali Raza** · 2022-03-18

<details>
<summary>Abstract</summary>

Self-supervised speech recognition models require considerable labeled training data for learning high-fidelity representations for Automatic Speech Recognition (ASR) which is computationally demanding and time-consuming. We consider the task of identifying an optimal subset of data for efficient fine-tuning in self-supervised speech models for ASR. We discover that the dataset pruning strategies used in vision tasks for sampling the most informative examples do not perform better than random subset selection on fine-tuning self-supervised ASR. We then present the COWERAGE algorithm for representative subset selection in self-supervised ASR. COWERAGE is based on our finding that ensuring the coverage of examples based on training Word Error Rate (WER) in the early training epochs leads to better generalization performance. Extensive experiments with the wav2vec 2.0 and HuBERT model on TIMIT, Librispeech, and LJSpeech datasets show the effectiveness of COWERAGE and its transferability across models, with up to 17% relative WER improvement over existing dataset pruning methods and random sampling. We also demonstrate that the coverage of training instances in terms of WER values ensures the inclusion of phonemically diverse examples, leading to better test accuracy in self-supervised speech recognition models.

</details>

### [Whither the Priors for (Vocal) Interactivity?](2203.08578.md)
**Roger K. Moore** · 2022-03-16

<details>
<summary>Abstract</summary>

Voice-based communication is often cited as one of the most `natural' ways in which humans and robots might interact, and the recent availability of accurate automatic speech recognition and intelligible speech synthesis has enabled researchers to integrate advanced off-the-shelf spoken language technology components into their robot platforms. Despite this, the resulting interactions are anything but `natural'. It transpires that simply giving a robot a voice doesn't mean that a user will know how (or when) to talk to it, and the resulting `conversations' tend to be stilted, one-sided and short. On the surface, these difficulties might appear to be fairly trivial consequences of users' unfamiliarity with robots (and \emph{vice versa}), and that any problems would be mitigated by long-term use by the human, coupled with `deep learning' by the robot. However, it is argued here that such communication failures are indicative of a deeper malaise: a fundamental lack of basic principles -- \emph{priors} -- underpinning not only speech-based interaction in particular, but (vocal) interactivity in general. This is evidenced not only by the fact that contemporary spoken language systems already require training data sets that are orders-of-magnitude greater than that experienced by a young child, but also by the lack of design principles for creating effective communicative human-robot interaction. This short position paper identifies some of the key areas where theoretical insights might help overcome these shortfalls.

</details>

### [RED-ACE: Robust Error Detection for ASR using Confidence Embeddings](2203.07172.md)
**Zorik Gekhman, Dina Zverinski, Jonathan Mallinson, Genady Beryozkin** · 2022-03-14

<details>
<summary>Abstract</summary>

ASR Error Detection (AED) models aim to post-process the output of Automatic Speech Recognition (ASR) systems, in order to detect transcription errors. Modern approaches usually use text-based input, comprised solely of the ASR transcription hypothesis, disregarding additional signals from the ASR model. Instead, we propose to utilize the ASR system's word-level confidence scores for improving AED performance. Specifically, we add an ASR Confidence Embedding (ACE) layer to the AED model's encoder, allowing us to jointly encode the confidence scores and the transcribed text into a contextualized representation. Our experiments show the benefits of ASR confidence scores for AED, their complementary effect over the textual signal, as well as the effectiveness and robustness of ACE for combining these signals. To foster further research, we publish a novel AED dataset consisting of ASR outputs on the LibriSpeech corpus with annotated transcription errors.

</details>

### [Spectral Modification Based Data Augmentation For Improving End-to-End ASR For Children's Speech](2203.06600.md)
**Vishwanath Pratap Singh, Hardik Sailor, Supratik Bhattacharya, Abhishek Pandey** · 2022-03-13

<details>
<summary>Abstract</summary>

Training a robust Automatic Speech Recognition (ASR) system for children's speech recognition is a challenging task due to inherent differences in acoustic attributes of adult and child speech and scarcity of publicly available children's speech dataset. In this paper, a novel segmental spectrum warping and perturbations in formant energy are introduced, to generate a children-like speech spectrum from that of an adult's speech spectrum. Then, this modified adult spectrum is used as augmented data to improve end-to-end ASR systems for children's speech recognition. The proposed data augmentation methods give 6.5% and 6.1% relative reduction in WER on children dev and test sets respectively, compared to the vocal tract length perturbation (VTLP) baseline system trained on Librispeech 100 hours adult speech dataset. When children's speech data is added in training with Librispeech set, it gives a 3.7 % and 5.1% relative reduction in WER, compared to the VTLP baseline system.

</details>

### [A combined approach to the analysis of speech conversations in a contact center domain](2203.06396.md)
**Andrea Brunello, Enrico Marzano, Angelo Montanari, Guido Sciavicco** · 2022-03-12

<details>
<summary>Abstract</summary>

The ever more accurate search for deep analysis in customer data is a really strong technological trend nowadays, quite appealing to both private and public companies. This is particularly true in the contact center domain, where speech analytics is an extremely powerful methodology for gaining insights from unstructured data, coming from customer and human agent conversations. In this work, we describe an experimentation with a speech analytics process for an Italian contact center, that deals with call recordings extracted from inbound or outbound flows. First, we illustrate in detail the development of an in-house speech-to-text solution, based on Kaldi framework, and evaluate its performance (and compare it to Google Cloud Speech API). Then, we evaluate and compare different approaches to the semantic tagging of call transcripts, ranging from classic regular expressions to machine learning models based on ngrams and logistic regression, and propose a combination of them, which is shown to provide a consistent benefit. Finally, a decision tree inducer, called J48S, is applied to the problem of tagging. Such an algorithm is natively capable of exploiting sequential data, such as texts, for classification purposes. The solution is compared with the other approaches and is shown to provide competitive classification performances, while generating highly interpretable models and reducing the complexity of the data preparation phase. The potential operational impact of the whole process is thoroughly examined.

</details>

### [Transformer-based Streaming ASR with Cumulative Attention](2203.05736.md)
**Mohan Li, Shucong Zhang, Catalin Zorila, Rama Doddipatla** · 2022-03-11

<details>
<summary>Abstract</summary>

In this paper, we propose an online attention mechanism, known as cumulative attention (CA), for streaming Transformer-based automatic speech recognition (ASR). Inspired by monotonic chunkwise attention (MoChA) and head-synchronous decoder-end adaptive computation steps (HS-DACS) algorithms, CA triggers the ASR outputs based on the acoustic information accumulated at each encoding timestep, where the decisions are made using a trainable device, referred to as halting selector. In CA, all the attention heads of the same decoder layer are synchronised to have a unified halting position. This feature effectively alleviates the problem caused by the distinct behaviour of individual heads, which may otherwise give rise to severe latency issues as encountered by MoChA. The ASR experiments conducted on AIShell-1 and Librispeech datasets demonstrate that the proposed CA-based Transformer system can achieve on par or better performance with significant reduction in latency during inference, when compared to other streaming Transformer systems in literature.

</details>

### [Sentence-Select: Large-Scale Language Model Data Selection for Rare-Word Speech Recognition](2203.05008.md)
**W. Ronny Huang, Cal Peyser, Tara N. Sainath, Ruoming Pang et al.** · 2022-03-09

<details>
<summary>Abstract</summary>

Language model fusion helps smart assistants recognize words which are rare in acoustic data but abundant in text-only corpora (typed search logs). However, such corpora have properties that hinder downstream performance, including being (1) too large, (2) beset with domain-mismatched content, and (3) heavy-headed rather than heavy-tailed (excessively many duplicate search queries such as "weather"). We show that three simple strategies for selecting language modeling data can dramatically improve rare-word recognition without harming overall performance. First, to address the heavy-headedness, we downsample the data according to a soft log function, which tunably reduces high frequency (head) sentences. Second, to encourage rare-word exposure, we explicitly filter for words rare in the acoustic data. Finally, we tackle domain-mismatch via perplexity-based contrastive selection, filtering for examples matched to the target domain. We down-select a large corpus of web search queries by a factor of 53x and achieve better LM perplexities than without down-selection. When shallow-fused with a state-of-the-art, production speech engine, our LM achieves WER reductions of up to 24% relative on rare-word sentences (without changing overall WER) compared to a baseline LM trained on the raw corpus. These gains are further validated through favorable side-by-side evaluations on live voice search traffic.

</details>

### [A practical framework for multi-domain speech recognition and an instance sampling method to neural language modeling](2203.04767.md)
**Yike Zhang, Xiaobing Feng, Yi Liu, Songjun Cao et al.** · 2022-03-09

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems used on smart phones or vehicles are usually required to process speech queries from very different domains. In such situations, a vanilla ASR system usually fails to perform well on every domain. This paper proposes a multi-domain ASR framework for Tencent Map, a navigation app used on smart phones and in-vehicle infotainment systems. The proposed framework consists of three core parts: a basic ASR module to generate n-best lists of a speech query, a text classification module to determine which domain the speech query belongs to, and a reranking module to rescore n-best lists using domain-specific language models. In addition, an instance sampling based method to training neural network language models (NNLMs) is proposed to address the data imbalance problem in multi-domain ASR. In experiments, the proposed framework was evaluated on navigation domain and music domain, since navigating and playing music are two main features of Tencent Map. Compared to a general ASR system, the proposed framework achieves a relative 13% $\sim$ 22% character error rate reduction on several test sets collected from Tencent Map and our in-car voice assistant.

</details>

### [Towards Contextual Spelling Correction for Customization of End-to-end Speech Recognition Systems](2203.00888.md)
**Xiaoqiang Wang, Yanqing Liu, Jinyu Li, Veljko Miljanic et al.** · 2022-03-02

<details>
<summary>Abstract</summary>

Contextual biasing is an important and challenging task for end-to-end automatic speech recognition (ASR) systems, which aims to achieve better recognition performance by biasing the ASR system to particular context phrases such as person names, music list, proper nouns, etc. Existing methods mainly include contextual LM biasing and adding bias encoder into end-to-end ASR models. In this work, we introduce a novel approach to do contextual biasing by adding a contextual spelling correction model on top of the end-to-end ASR system. We incorporate contextual information into a sequence-to-sequence spelling correction model with a shared context encoder. Our proposed model includes two different mechanisms: autoregressive (AR) and non-autoregressive (NAR). We propose filtering algorithms to handle large-size context lists, and performance balancing mechanisms to control the biasing degree of the model. We demonstrate the proposed model is a general biasing solution which is domain-insensitive and can be adopted in different scenarios. Experiments show that the proposed method achieves as much as 51% relative word error rate (WER) reduction over ASR system and outperforms traditional biasing methods. Compared to the AR solution, the proposed NAR model reduces model size by 43.2% and speeds up inference by 2.1 times.

</details>

### [A Conformer Based Acoustic Model for Robust Automatic Speech Recognition](2203.00725.md)
**Yufeng Yang, Peidong Wang, DeLiang Wang** · 2022-03-01

<details>
<summary>Abstract</summary>

This study addresses robust automatic speech recognition (ASR) by introducing a Conformer-based acoustic model. The proposed model builds on the wide residual bi-directional long short-term memory network (WRBN) with utterance-wise dropout and iterative speaker adaptation, but employs a Conformer encoder instead of the recurrent network. The Conformer encoder uses a convolution-augmented attention mechanism for acoustic modeling. The proposed system is evaluated on the monaural ASR task of the CHiME-4 corpus. Coupled with utterance-wise normalization and speaker adaptation, our model achieves $6.25\%$ word error rate, which outperforms WRBN by $8.4\%$ relatively. In addition, the proposed Conformer-based model is $18.3\%$ smaller in model size and reduces total training time by $79.6\%$.

</details>

### [Measuring the Impact of Individual Domain Factors in Self-Supervised Pre-Training](2203.00648.md)
**Ramon Sanabria, Wei-Ning Hsu, Alexei Baevski, Michael Auli** · 2022-03-01

<details>
<summary>Abstract</summary>

Human speech data comprises a rich set of domain factors such as accent, syntactic and semantic variety, or acoustic environment. Previous work explores the effect of domain mismatch in automatic speech recognition between pre-training and fine-tuning as a whole but does not dissect the contribution of individual factors. In this paper, we present a controlled study to better understand the effect of such factors on the performance of pre-trained representations on automatic speech recognition. To do so, we pre-train models either on modified natural speech or synthesized audio, with a single domain factor modified, and then measure performance after fine-tuning. Results show that phonetic domain factors play an important role during pre-training while grammatical and syntactic factors are far less important. To our knowledge, this is the first study to better understand the domain characteristics of pre-trained sets in self-supervised pre-training for speech.

</details>

### [Sentiment Word Aware Multimodal Refinement for Multimodal Sentiment Analysis with ASR Errors](2203.00257.md)
**Yang Wu, Yanyan Zhao, Hao Yang, Song Chen et al.** · 2022-03-01

<details>
<summary>Abstract</summary>

Multimodal sentiment analysis has attracted increasing attention and lots of models have been proposed. However, the performance of the state-of-the-art models decreases sharply when they are deployed in the real world. We find that the main reason is that real-world applications can only access the text outputs by the automatic speech recognition (ASR) models, which may be with errors because of the limitation of model capacity. Through further analysis of the ASR outputs, we find that in some cases the sentiment words, the key sentiment elements in the textual modality, are recognized as other words, which makes the sentiment of the text change and hurts the performance of multimodal sentiment models directly. To address this problem, we propose the sentiment word aware multimodal refinement model (SWRM), which can dynamically refine the erroneous sentiment words by leveraging multimodal sentiment clues. Specifically, we first use the sentiment word position detection module to obtain the most possible position of the sentiment word in the text and then utilize the multimodal sentiment word refinement module to dynamically refine the sentiment word embeddings. The refined embeddings are taken as the textual inputs of the multimodal feature fusion module to predict the sentiment labels. We conduct extensive experiments on the real-world datasets including MOSI-Speechbrain, MOSI-IBM, and MOSI-iFlytek and the results demonstrate the effectiveness of our model, which surpasses the current state-of-the-art models on three datasets. Furthermore, our approach can be adapted for other multimodal feature fusion models easily. Data and code are available at https://github.com/albertwy/SWRM.

</details>

### [Extended Graph Temporal Classification for Multi-Speaker End-to-End ASR](2203.00232.md)
**Xuankai Chang, Niko Moritz, Takaaki Hori, Shinji Watanabe et al.** · 2022-03-01

<details>
<summary>Abstract</summary>

Graph-based temporal classification (GTC), a generalized form of the connectionist temporal classification loss, was recently proposed to improve automatic speech recognition (ASR) systems using graph-based supervision. For example, GTC was first used to encode an N-best list of pseudo-label sequences into a graph for semi-supervised learning. In this paper, we propose an extension of GTC to model the posteriors of both labels and label transitions by a neural network, which can be applied to a wider range of tasks. As an example application, we use the extended GTC (GTC-e) for the multi-speaker speech recognition task. The transcriptions and speaker information of multi-speaker speech are represented by a graph, where the speaker information is associated with the transitions and ASR outputs with the nodes. Using GTC-e, multi-speaker ASR modelling becomes very similar to single-speaker ASR modeling, in that tokens by multiple speakers are recognized as a single merged sequence in chronological order. For evaluation, we perform experiments on a simulated multi-speaker speech dataset derived from LibriSpeech, obtaining promising results with performance close to classical benchmarks for the task.

</details>

### [Integrating Text Inputs For Training and Adapting RNN Transducer ASR Models](2202.13155.md)
**Samuel Thomas, Brian Kingsbury, George Saon, Hong-Kwang J. Kuo** · 2022-02-26

<details>
<summary>Abstract</summary>

Compared to hybrid automatic speech recognition (ASR) systems that use a modular architecture in which each component can be independently adapted to a new domain, recent end-to-end (E2E) ASR system are harder to customize due to their all-neural monolithic construction. In this paper, we propose a novel text representation and training framework for E2E ASR models. With this approach, we show that a trained RNN Transducer (RNN-T) model's internal LM component can be effectively adapted with text-only data. An RNN-T model trained using both speech and text inputs improves over a baseline model trained on just speech with close to 13% word error rate (WER) reduction on the Switchboard and CallHome test sets of the NIST Hub5 2000 evaluation. The usefulness of the proposed approach is further demonstrated by customizing this general purpose RNN-T model to three separate datasets. We observe 20-45% relative word error rate (WER) reduction in these settings with this novel LM style customization technique using only unpaired text data from the new domains.

</details>

### [Language-Independent Speaker Anonymization Approach using Self-Supervised Pre-Trained Models](2202.13097.md)
**Xiaoxiao Miao, Xin Wang, Erica Cooper, Junichi Yamagishi et al.** · 2022-02-26

<details>
<summary>Abstract</summary>

Speaker anonymization aims to protect the privacy of speakers while preserving spoken linguistic information from speech. Current mainstream neural network speaker anonymization systems are complicated, containing an F0 extractor, speaker encoder, automatic speech recognition acoustic model (ASR AM), speech synthesis acoustic model and speech waveform generation model. Moreover, as an ASR AM is language-dependent, trained on English data, it is hard to adapt it into another language. In this paper, we propose a simpler self-supervised learning (SSL)-based method for language-independent speaker anonymization without any explicit language-dependent model, which can be easily used for other languages. Extensive experiments were conducted on the VoicePrivacy Challenge 2020 datasets in English and AISHELL-3 datasets in Mandarin to demonstrate the effectiveness of our proposed SSL-based language-independent speaker anonymization method.

</details>

### [Visual Speech Recognition for Multiple Languages in the Wild](2202.13084.md)
**Pingchuan Ma, Stavros Petridis, Maja Pantic** · 2022-02-26

<details>
<summary>Abstract</summary>

Visual speech recognition (VSR) aims to recognize the content of speech based on lip movements, without relying on the audio stream. Advances in deep learning and the availability of large audio-visual datasets have led to the development of much more accurate and robust VSR models than ever before. However, these advances are usually due to the larger training sets rather than the model design. Here we demonstrate that designing better models is equally as important as using larger training sets. We propose the addition of prediction-based auxiliary tasks to a VSR model, and highlight the importance of hyperparameter optimization and appropriate data augmentations. We show that such a model works for different languages and outperforms all previous methods trained on publicly available datasets by a large margin. It even outperforms models that were trained on non-publicly available datasets containing up to to 21 times more data. We show, furthermore, that using additional training data, even in other languages or with automatically generated transcriptions, results in further improvement.

</details>

### [Ask2Mask: Guided Data Selection for Masked Speech Modeling](2202.12719.md)
**Murali Karthick Baskar, Andrew Rosenberg, Bhuvana Ramabhadran, Yu Zhang et al.** · 2022-02-24

<details>
<summary>Abstract</summary>

Masked speech modeling (MSM) methods such as wav2vec2 or w2v-BERT learn representations over speech frames which are randomly masked within an utterance. While these methods improve performance of Automatic Speech Recognition (ASR) systems, they have one major limitation. They treat all unsupervised speech samples with equal weight, which hinders learning as not all samples have relevant information to learn meaningful representations. In this work, we address this limitation. We propose ask2mask (ATM), a novel approach to focus on specific samples during MSM pre-training. ATM employs an external ASR model or \textit{scorer} to weight unsupervised input samples in two different ways: 1) A fine-grained data selection is performed by masking over the highly confident input frames as chosen by the scorer. This allows the model to learn meaningful representations. 2) ATM is further extended to focus at utterance-level by weighting the final MSM loss with the utterance-level confidence score. We conduct fine-tuning experiments on two well-benchmarked corpora: LibriSpeech (matching the pre-training data) and Commonvoice, TED-LIUM, AMI and CHiME-6 (not matching the pre-training data). The results substantiate the efficacy of ATM on significantly improving the recognition performance under mismatched conditions (up to 11.6\% relative over published results and upto 4.46\% relative over our internal baseline) while still yielding modest improvements under matched conditions.

</details>

### [Leveraging Unimodal Self-Supervised Learning for Multimodal Audio-Visual Speech Recognition](2203.07996.md)
**Xichen Pan, Peiyu Chen, Yichen Gong, Helong Zhou et al.** · 2022-02-24

<details>
<summary>Abstract</summary>

Training Transformer-based models demands a large amount of data, while obtaining aligned and labelled data in multimodality is rather cost-demanding, especially for audio-visual speech recognition (AVSR). Thus it makes a lot of sense to make use of unlabelled unimodal data. On the other side, although the effectiveness of large-scale self-supervised learning is well established in both audio and visual modalities, how to integrate those pre-trained models into a multimodal scenario remains underexplored. In this work, we successfully leverage unimodal self-supervised learning to promote the multimodal AVSR. In particular, audio and visual front-ends are trained on large-scale unimodal datasets, then we integrate components of both front-ends into a larger multimodal framework which learns to recognize parallel audio-visual data into characters through a combination of CTC and seq2seq decoding. We show that both components inherited from unimodal self-supervised learning cooperate well, resulting in that the multimodal framework yields competitive results through fine-tuning. Our model is experimentally validated on both word-level and sentence-level tasks. Especially, even without an external language model, our proposed model raises the state-of-the-art performances on the widely accepted Lip Reading Sentences 2 (LRS2) dataset by a large margin, with a relative improvement of 30%.

</details>

### [FlowSense: Monitoring Airflow in Building Ventilation Systems Using Audio Sensing](2202.11136.md)
**Bhawana Chhaglani, Camellia Zakaria, Adam Lechowicz, Prashant Shenoy et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

Proper indoor ventilation through buildings' heating, ventilation, and air conditioning (HVAC) systems has become an increasing public health concern that significantly impacts individuals' health and safety at home, work, and school. While much work has progressed in providing energy-efficient and user comfort for HVAC systems through IoT devices and mobile-sensing approaches, ventilation is an aspect that has received lesser attention despite its importance. With a motivation to monitor airflow from building ventilation systems through commodity sensing devices, we present FlowSense, a machine learning-based algorithm to predict airflow rate from sensed audio data in indoor spaces. Our ML technique can predict the state of an air vent-whether it is on or off-as well as the rate of air flowing through active vents. By exploiting a low-pass filter to obtain low-frequency audio signals, we put together a privacy-preserving pipeline that leverages a silence detection algorithm to only sense for sounds of air from HVAC air vent when no human speech is detected. We also propose the Minimum Persistent Sensing (MPS) as a post-processing algorithm to reduce interference from ambient noise, including ongoing human conversation, office machines, and traffic noises. Together, these techniques ensure user privacy and improve the robustness of FlowSense. We validate our approach yielding over 90% accuracy in predicting vent status and 0.96 MSE in predicting airflow rate when the device is placed within 2.25 meters away from an air vent. Additionally, we demonstrate how our approach as a mobile audio-sensing platform is robust to smartphone models, distance, and orientation. Finally, we evaluate FlowSense privacy-preserving pipeline through a user study and a Google Speech Recognition service, confirming that the audio signals we used as input data are inaudible and inconstructible.

</details>

### [Improving CTC-based speech recognition via knowledge transferring from pre-trained language models](2203.03582.md)
**Keqi Deng, Songjun Cao, Yike Zhang, Long Ma et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

Recently, end-to-end automatic speech recognition models based on connectionist temporal classification (CTC) have achieved impressive results, especially when fine-tuned from wav2vec2.0 models. Due to the conditional independence assumption, CTC-based models are always weaker than attention-based encoder-decoder models and require the assistance of external language models (LMs). To solve this issue, we propose two knowledge transferring methods that leverage pre-trained LMs, such as BERT and GPT2, to improve CTC-based models. The first method is based on representation learning, in which the CTC-based models use the representation produced by BERT as an auxiliary learning target. The second method is based on joint classification learning, which combines GPT2 for text modeling with a hybrid CTC/attention architecture. Experiment on AISHELL-1 corpus yields a character error rate (CER) of 4.2% on the test set. When compared to the vanilla CTC-based models fine-tuned from the wav2vec2.0 models, our knowledge transferring method reduces CER by 16.1% relatively without external LMs.

</details>

### [Korean Tokenization for Beam Search Rescoring in Speech Recognition](2203.03583.md)
**Kyuhong Shim, Hyewon Bae, Wonyong Sung** · 2022-02-22

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition (ASR) models can be greatly improved by proper beam-search decoding with external language model (LM). There has been an increasing interest in Korean speech recognition, but not many studies have been focused on the decoding procedure. In this paper, we propose a Korean tokenization method for neural network-based LM used for Korean ASR. Although the common approach is to use the same tokenization method for external LM as the ASR model, we show that it may not be the best choice for Korean. We propose a new tokenization method that inserts a special token, SkipTC, when there is no trailing consonant in a Korean syllable. By utilizing the proposed SkipTC token, the input sequence for LM becomes very regularly patterned so that the LM can better learn the linguistic characteristics. Our experiments show that the proposed approach achieves a lower word error rate compared to the same LM model without SkipTC. In addition, we are the first to report the ASR performance for the recently introduced large-scale 7,600h Korean speech dataset.

</details>

### [Adversarial Attacks on Speech Recognition Systems for Mission-Critical Applications: A Survey](2202.10594.md)
**Ngoc Dung Huynh, Mohamed Reda Bouadjenek, Imran Razzak, Kevin Lee et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

A Machine-Critical Application is a system that is fundamentally necessary to the success of specific and sensitive operations such as search and recovery, rescue, military, and emergency management actions. Recent advances in Machine Learning, Natural Language Processing, voice recognition, and speech processing technologies have naturally allowed the development and deployment of speech-based conversational interfaces to interact with various machine-critical applications. While these conversational interfaces have allowed users to give voice commands to carry out strategic and critical activities, their robustness to adversarial attacks remains uncertain and unclear. Indeed, Adversarial Artificial Intelligence (AI) which refers to a set of techniques that attempt to fool machine learning models with deceptive data, is a growing threat in the AI and machine learning research community, in particular for machine-critical applications. The most common reason of adversarial attacks is to cause a malfunction in a machine learning model. An adversarial attack might entail presenting a model with inaccurate or fabricated samples as it's training data, or introducing maliciously designed data to deceive an already trained model. While focusing on speech recognition for machine-critical applications, in this paper, we first review existing speech recognition techniques, then, we investigate the effectiveness of adversarial attacks and defenses against these systems, before outlining research challenges, defense recommendations, and future work. This paper is expected to serve researchers and practitioners as a reference to help them in understanding the challenges, position themselves and, ultimately, help them to improve existing models of speech recognition for mission-critical applications. Keywords: Mission-Critical Applications, Adversarial AI, Speech Recognition Systems.

</details>

### [VADOI:Voice-Activity-Detection Overlapping Inference For End-to-end Long-form Speech Recognition](2202.10593.md)
**Jinhan Wang, Xiaosu Tong, Jinxi Guo, Di He et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

While end-to-end models have shown great success on the Automatic Speech Recognition task, performance degrades severely when target sentences are long-form. The previous proposed methods, (partial) overlapping inference are shown to be effective on long-form decoding. For both methods, word error rate (WER) decreases monotonically when overlapping percentage decreases. Setting aside computational cost, the setup with 50% overlapping during inference can achieve the best performance. However, a lower overlapping percentage has an advantage of fast inference speed. In this paper, we first conduct comprehensive experiments comparing overlapping inference and partial overlapping inference with various configurations. We then propose Voice-Activity-Detection Overlapping Inference to provide a trade-off between WER and computation cost. Results show that the proposed method can achieve a 20% relative computation cost reduction on Librispeech and Microsoft Speech Language Translation long-form corpus while maintaining the WER performance when comparing to the best performing overlapping inference algorithm. We also propose Soft-Match to compensate for similar words mis-aligned problem.

</details>

### [Spanish and English Phoneme Recognition by Training on Simulated Classroom Audio Recordings of Collaborative Learning Environments](2202.10536.md)
**Mario Esparza** · 2022-02-21

<details>
<summary>Abstract</summary>

Audio recordings of collaborative learning environments contain a constant presence of cross-talk and background noise. Dynamic speech recognition between Spanish and English is required in these environments. To eliminate the standard requirement of large-scale ground truth, the thesis develops a simulated dataset by transforming audio transcriptions into phonemes and using 3D speaker geometry and data augmentation to generate an acoustic simulation of Spanish and English speech. The thesis develops a low-complexity neural network for recognizing Spanish and English phonemes (available at github.com/muelitas/keywordRec). When trained on 41 English phonemes, 0.099 PER is achieved on Speech Commands. When trained on 36 Spanish phonemes and tested on real recordings of collaborative learning environments, a 0.7208 LER is achieved. Slightly better than Google's Speech-to-text 0.7272 LER, which used anywhere from 15 to 1,635 times more parameters and trained on 300 to 27,500 hours of real data as opposed to 13 hours of simulated audios.

</details>

### [Speaker Adaptation Using Spectro-Temporal Deep Features for Dysarthric and Elderly Speech Recognition](2202.10290.md)
**Mengzhe Geng, Xurong Xie, Zi Ye, Tianzi Wang et al.** · 2022-02-21

<details>
<summary>Abstract</summary>

Despite the rapid progress of automatic speech recognition (ASR) technologies targeting normal speech in recent decades, accurate recognition of dysarthric and elderly speech remains highly challenging tasks to date. Sources of heterogeneity commonly found in normal speech including accent or gender, when further compounded with the variability over age and speech pathology severity level, create large diversity among speakers. To this end, speaker adaptation techniques play a key role in personalization of ASR systems for such users. Motivated by the spectro-temporal level differences between dysarthric, elderly and normal speech that systematically manifest in articulatory imprecision, decreased volume and clarity, slower speaking rates and increased dysfluencies, novel spectrotemporal subspace basis deep embedding features derived using SVD speech spectrum decomposition are proposed in this paper to facilitate auxiliary feature based speaker adaptation of state-of-the-art hybrid DNN/TDNN and end-to-end Conformer speech recognition systems. Experiments were conducted on four tasks: the English UASpeech and TORGO dysarthric speech corpora; the English DementiaBank Pitt and Cantonese JCCOCC MoCA elderly speech datasets. The proposed spectro-temporal deep feature adapted systems outperformed baseline i-Vector and xVector adaptation by up to 2.63% absolute (8.63% relative) reduction in word error rate (WER). Consistent performance improvements were retained after model based speaker adaptation using learning hidden unit contributions (LHUC) was further applied. The best speaker adapted system using the proposed spectral basis embedding features produced the lowest published WER of 25.05% on the UASpeech test set of 16 dysarthric speakers.

</details>

### [r-G2P: Evaluating and Enhancing Robustness of Grapheme to Phoneme Conversion by Controlled noise introducing and Contextual information incorporation](2202.11194.md)
**Chendong Zhao, Jianzong Wang, Xiaoyang Qu, Haoqian Wang et al.** · 2022-02-21

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is the process of converting the written form of words to their pronunciations. It has an important role for text-to-speech (TTS) synthesis and automatic speech recognition (ASR) systems. In this paper, we aim to evaluate and enhance the robustness of G2P models. We show that neural G2P models are extremely sensitive to orthographical variations in graphemes like spelling mistakes. To solve this problem, we propose three controlled noise introducing methods to synthesize noisy training data. Moreover, we incorporate the contextual information with the baseline and propose a robust training strategy to stabilize the training process. The experimental results demonstrate that our proposed robust G2P model (r-G2P) outperforms the baseline significantly (-2.73\% WER on Dict-based benchmarks and -9.09\% WER on Real-world sources).

</details>

### [Adaptive Discounting of Implicit Language Models in RNN-Transducers](2203.02317.md)
**Vinit Unni, Shreya Khare, Ashish Mittal, Preethi Jyothi et al.** · 2022-02-21

<details>
<summary>Abstract</summary>

RNN-Transducer (RNN-T) models have become synonymous with streaming end-to-end ASR systems. While they perform competitively on a number of evaluation categories, rare words pose a serious challenge to RNN-T models. One main reason for the degradation in performance on rare words is that the language model (LM) internal to RNN-Ts can become overconfident and lead to hallucinated predictions that are acoustically inconsistent with the underlying speech. To address this issue, we propose a lightweight adaptive LM discounting technique AdaptLMD, that can be used with any RNN-T architecture without requiring any external resources or additional parameters. AdaptLMD uses a two-pronged approach: 1) Randomly mask the prediction network output to encourage the RNN-T to not be overly reliant on it's outputs. 2) Dynamically choose when to discount the implicit LM (ILM) based on rarity of recently predicted tokens and divergence between ILM and implicit acoustic model (IAM) scores. Comparing AdaptLMD to a competitive RNN-T baseline, we obtain up to 4% and 14% relative reductions in overall WER and rare word PER, respectively, on a conversational, code-mixed Hindi-English ASR task.

</details>

### [Domain Adaptation of low-resource Target-Domain models using well-trained ASR Conformer Models](2202.09167.md)
**Vrunda N. Sukhadia, S. Umesh** · 2022-02-18

<details>
<summary>Abstract</summary>

In this paper, we investigate domain adaptation for low-resource Automatic Speech Recognition (ASR) of target-domain data, when a well-trained ASR model trained with a large dataset is available. We argue that in the encoder-decoder framework, the decoder of the well-trained ASR model is largely tuned towards the source-domain, hurting the performance of target-domain models in vanilla transfer-learning. On the other hand, the encoder layers of the well-trained ASR model mostly capture the acoustic characteristics. We, therefore, propose to use the embeddings tapped from these encoder layers as features for a downstream Conformer target-domain model and show that they provide significant improvements. We do ablation studies on which encoder layer is optimal to tap the embeddings, as well as the effect of freezing or updating the well-trained ASR model's encoder layers. We further show that applying Spectral Augmentation (SpecAug) on the proposed features (this is in addition to default SpecAug on input spectral features) provides a further improvement on the target-domain performance. For the LibriSpeech-100-clean data as target-domain and SPGI-5000 as a well-trained model, we get 30% relative improvement over baseline. Similarly, with WSJ data as target-domain and LibriSpeech-960 as a well-trained model, we get 50% relative improvement over baseline.

</details>

### [End-to-end contextual asr based on posterior distribution adaptation for hybrid ctc/attention system](2202.09003.md)
**Zhengyi Zhang, Pan Zhou** · 2022-02-18

<details>
<summary>Abstract</summary>

End-to-end (E2E) speech recognition architectures assemble all components of traditional speech recognition system into a single model. Although it simplifies ASR system, it introduces contextual ASR drawback: the E2E model has worse performance on utterances containing infrequent proper nouns. In this work, we propose to add a contextual bias attention (CBA) module to attention based encoder decoder (AED) model to improve its ability of recognizing the contextual phrases. Specifically, CBA utilizes the context vector of source attention in decoder to attend to a specific bias embedding. Jointly learned with the basic AED parameters, CBA can tell the model when and where to bias its output probability distribution. At inference stage, a list of bias phrases is preloaded and we adapt the posterior distributions of both CTC and attention decoder according to the attended bias phrase of CBA. We evaluate the proposed method on GigaSpeech and achieve a consistent relative improvement on recall rate of bias phrases ranging from 15% to 28% compared to the baseline model. Meanwhile, our method shows a strong anti-bias ability as the performance on general tests only degrades 1.7% even 2,000 bias phrases are present.

</details>

### [Curriculum optimization for low-resource speech recognition](2202.08883.md)
**Anastasia Kuznetsova, Anurag Kumar, Jennifer Drexler Fox, Francis Tyers** · 2022-02-17

<details>
<summary>Abstract</summary>

Modern end-to-end speech recognition models show astonishing results in transcribing audio signals into written text. However, conventional data feeding pipelines may be sub-optimal for low-resource speech recognition, which still remains a challenging task. We propose an automated curriculum learning approach to optimize the sequence of training examples based on both the progress of the model while training and prior knowledge about the difficulty of the training examples. We introduce a new difficulty measure called compression ratio that can be used as a scoring function for raw audio in various noise conditions. The proposed method improves speech recognition Word Error Rate performance by up to 33% relative over the baseline system

</details>

### [AISHELL-NER: Named Entity Recognition from Chinese Speech](2202.08533.md)
**Boli Chen, Guangwei Xu, Xiaobin Wang, Pengjun Xie et al.** · 2022-02-17

<details>
<summary>Abstract</summary>

Named Entity Recognition (NER) from speech is among Spoken Language Understanding (SLU) tasks, aiming to extract semantic information from the speech signal. NER from speech is usually made through a two-step pipeline that consists of (1) processing the audio using an Automatic Speech Recognition (ASR) system and (2) applying an NER tagger to the ASR outputs. Recent works have shown the capability of the End-to-End (E2E) approach for NER from English and French speech, which is essentially entity-aware ASR. However, due to the many homophones and polyphones that exist in Chinese, NER from Chinese speech is effectively a more challenging task. In this paper, we introduce a new dataset AISEHLL-NER for NER from Chinese speech. Extensive experiments are conducted to explore the performance of several state-of-the-art methods. The results demonstrate that the performance could be improved by combining entity-aware ASR and pretrained NER tagger, which can be easily applied to the modern SLU pipeline. The dataset is publicly available at github.com/Alibaba-NLP/AISHELL-NER.

</details>

### [Mitigating Closed-model Adversarial Examples with Bayesian Neural Modeling for Enhanced End-to-End Speech Recognition](2202.08532.md)
**Chao-Han Huck Yang, Zeeshan Ahmed, Yile Gu, Joseph Szurley et al.** · 2022-02-17

<details>
<summary>Abstract</summary>

In this work, we aim to enhance the system robustness of end-to-end automatic speech recognition (ASR) against adversarially-noisy speech examples. We focus on a rigorous and empirical "closed-model adversarial robustness" setting (e.g., on-device or cloud applications). The adversarial noise is only generated by closed-model optimization (e.g., evolutionary and zeroth-order estimation) without accessing gradient information of a targeted ASR model directly. We propose an advanced Bayesian neural network (BNN) based adversarial detector, which could model latent distributions against adaptive adversarial perturbation with divergence measurement. We further simulate deployment scenarios of RNN Transducer, Conformer, and wav2vec-2.0 based ASR systems with the proposed adversarial detection system. Leveraging the proposed BNN based detection system, we improve detection rate by +2.77 to +5.42% (relative +3.03 to +6.26%) and reduce the word error rate by 5.02 to 7.47% on LibriSpeech datasets compared to the current model enhancement methods against the adversarial speech examples.

</details>

### [MLP-ASR: Sequence-length agnostic all-MLP architectures for speech recognition](2202.08456.md)
**Jin Sakuma, Tatsuya Komatsu, Robin Scheibler** · 2022-02-17

<details>
<summary>Abstract</summary>

We propose multi-layer perceptron (MLP)-based architectures suitable for variable length input. MLP-based architectures, recently proposed for image classification, can only be used for inputs of a fixed, pre-defined size. However, many types of data are naturally variable in length, for example, acoustic signals. We propose three approaches to extend MLP-based architectures for use with sequences of arbitrary length. The first one uses a circular convolution applied in the Fourier domain, the second applies a depthwise convolution, and the final relies on a shift operation. We evaluate the proposed architectures on an automatic speech recognition task with the Librispeech and Tedlium2 corpora. The best proposed MLP-based architectures improves WER by 1.0 / 0.9%, 0.9 / 0.5% on Librispeech dev-clean/dev-other, test-clean/test-other set, and 0.8 / 1.1% on Tedlium2 dev/test set using 86.4% the size of self-attention-based architecture.

</details>

### [Knowledge Transfer from Large-scale Pretrained Language Models to End-to-end Speech Recognizers](2202.07894.md)
**Yotaro Kubo, Shigeki Karita, Michiel Bacchiani** · 2022-02-16

<details>
<summary>Abstract</summary>

End-to-end speech recognition is a promising technology for enabling compact automatic speech recognition (ASR) systems since it can unify the acoustic and language model into a single neural network. However, as a drawback, training of end-to-end speech recognizers always requires transcribed utterances. Since end-to-end models are also known to be severely data hungry, this constraint is crucial especially because obtaining transcribed utterances is costly and can possibly be impractical or impossible. This paper proposes a method for alleviating this issue by transferring knowledge from a language model neural network that can be pretrained with text-only data. Specifically, this paper attempts to transfer semantic knowledge acquired in embedding vectors of large-scale language models. Since embedding vectors can be assumed as implicit representations of linguistic information such as part-of-speech, intent, and so on, those are also expected to be useful modeling cues for ASR decoders. This paper extends two types of ASR decoders, attention-based decoders and neural transducers, by modifying training loss functions to include embedding prediction terms. The proposed systems were shown to be effective for error rate reduction without incurring extra computational costs in the decoding phase.

</details>

### [Conversational Speech Recognition By Learning Conversation-level Characteristics](2202.07855.md)
**Kun Wei, Yike Zhang, Sining Sun, Lei Xie et al.** · 2022-02-16

<details>
<summary>Abstract</summary>

Conversational automatic speech recognition (ASR) is a task to recognize conversational speech including multiple speakers. Unlike sentence-level ASR, conversational ASR can naturally take advantages from specific characteristics of conversation, such as role preference and topical coherence. This paper proposes a conversational ASR model which explicitly learns conversation-level characteristics under the prevalent end-to-end neural framework. The highlights of the proposed model are twofold. First, a latent variational module (LVM) is attached to a conformer-based encoder-decoder ASR backbone to learn role preference and topical coherence. Second, a topic model is specifically adopted to bias the outputs of the decoder to words in the predicted topics. Experiments on two Mandarin conversational ASR tasks show that the proposed model achieves a maximum 12% relative character error rate (CER) reduction.

</details>

### [Capitalization Normalization for Language Modeling with an Accurate and Efficient Hierarchical RNN Model](2202.08171.md)
**Hao Zhang, You-Chi Cheng, Shankar Kumar, W. Ronny Huang et al.** · 2022-02-16

<details>
<summary>Abstract</summary>

Capitalization normalization (truecasing) is the task of restoring the correct case (uppercase or lowercase) of noisy text. We propose a fast, accurate and compact two-level hierarchical word-and-character-based recurrent neural network model. We use the truecaser to normalize user-generated text in a Federated Learning framework for language modeling. A case-aware language model trained on this normalized text achieves the same perplexity as a model trained on text with gold capitalization. In a real user A/B experiment, we demonstrate that the improvement translates to reduced prediction error rates in a virtual keyboard application. Similarly, in an ASR language model fusion experiment, we show reduction in uppercase character error rate and word error rate.

</details>

### [Learning Contextually Fused Audio-visual Representations for Audio-visual Speech Recognition](2202.07428.md)
**Zi-Qiang Zhang, Jie Zhang, Jian-Shu Zhang, Ming-Hui Wu et al.** · 2022-02-15

<details>
<summary>Abstract</summary>

With the advance in self-supervised learning for audio and visual modalities, it has become possible to learn a robust audio-visual speech representation. This would be beneficial for improving the audio-visual speech recognition (AVSR) performance, as the multi-modal inputs contain more fruitful information in principle. In this paper, based on existing self-supervised representation learning methods for audio modality, we therefore propose an audio-visual representation learning approach. The proposed approach explores both the complementarity of audio-visual modalities and long-term context dependency using a transformer-based fusion module and a flexible masking strategy. After pre-training, the model is able to extract fused representations required by AVSR. Without loss of generality, it can be applied to single-modal tasks, e.g. audio/visual speech recognition by simply masking out one modality in the fusion module. The proposed pre-trained model is evaluated on speech recognition and lipreading tasks using one or two modalities, where the superiority is revealed.

</details>

### [Multi-style Training for South African Call Centre Audio](2202.07219.md)
**Walter Heymans, Marelie H. Davel, Charl van Heerden** · 2022-02-15

<details>
<summary>Abstract</summary>

Mismatched data is a challenging problem for automatic speech recognition (ASR) systems. One of the most common techniques used to address mismatched data is multi-style training (MTR), a form of data augmentation that attempts to transform the training data to be more representative of the testing data; and to learn robust representations applicable to different conditions. This task can be very challenging if the test conditions are unknown. We explore the impact of different MTR styles on system performance when testing conditions are different from training conditions in the context of deep neural network hidden Markov model (DNN-HMM) ASR systems. A controlled environment is created using the LibriSpeech corpus, where we isolate the effect of different MTR styles on final system performance. We evaluate our findings on a South African call centre dataset that contains noisy, WAV49-encoded audio.

</details>

### [Vau da muntanialas: Energy-efficient multi-die scalable acceleration of RNN inference](2202.07462.md)
**Gianna Paulin, Francesco Conti, Lukas Cavigelli, Luca Benini** · 2022-02-14

<details>
<summary>Abstract</summary>

Recurrent neural networks such as Long Short-Term Memories (LSTMs) learn temporal dependencies by keeping an internal state, making them ideal for time-series problems such as speech recognition. However, the output-to-input feedback creates distinctive memory bandwidth and scalability challenges in designing accelerators for RNNs. We present Muntaniala, an RNN accelerator architecture for LSTM inference with a silicon-measured energy-efficiency of 3.25$TOP/s/W$ and performance of 30.53$GOP/s$ in UMC 65 $nm$ technology. The scalable design of Muntaniala allows running large RNN models by combining multiple tiles in a systolic array. We keep all parameters stationary on every die in the array, drastically reducing the I/O communication to only loading new features and sharing partial results with other dies. For quantifying the overall system power, including I/O power, we built Vau da Muntanialas, to the best of our knowledge, the first demonstration of a systolic multi-chip-on-PCB array of RNN accelerator. Our multi-die prototype performs LSTM inference with 192 hidden states in 330$μs$ with a total system power of 9.0$mW$ at 10$MHz$ consuming 2.95$μJ$. Targeting the 8/16-bit quantization implemented in Muntaniala, we show a phoneme error rate (PER) drop of approximately 3% with respect to floating-point (FP) on a 3L-384NH-123NI LSTM network on the TIMIT dataset.

</details>

### [Saving RNN Computations with a Neuron-Level Fuzzy Memoization Scheme](2202.06563.md)
**Franyell Silfa, Jose-Maria Arnau, Antonio González** · 2022-02-14

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are a key technology for applications such as automatic speech recognition or machine translation. Unlike conventional feed-forward DNNs, RNNs remember past information to improve the accuracy of future predictions and, therefore, they are very effective for sequence processing problems. For each application run, recurrent layers are executed many times for processing a potentially large sequence of inputs (words, images, audio frames, etc.). In this paper, we observe that the output of a neuron exhibits small changes in consecutive invocations.~We exploit this property to build a neuron-level fuzzy memoization scheme, which dynamically caches each neuron's output and reuses it whenever it is predicted that the current output will be similar to a previously computed result, avoiding in this way the output computations. The main challenge in this scheme is determining whether the new neuron's output for the current input in the sequence will be similar to a recently computed result. To this end, we extend the recurrent layer with a much simpler Bitwise Neural Network (BNN), and show that the BNN and RNN outputs are highly correlated: if two BNN outputs are very similar, the corresponding outputs in the original RNN layer are likely to exhibit negligible changes. The BNN provides a low-cost and effective mechanism for deciding when fuzzy memoization can be applied with a small impact on accuracy. We evaluate our memoization scheme on top of a state-of-the-art accelerator for RNNs, for a variety of different neural networks from multiple application domains. We show that our technique avoids more than 26.7\% of computations, resulting in 21\% energy savings and 1.4x speedup on average.

</details>

### [Punctuation restoration in Swedish through fine-tuned KB-BERT](2202.06769.md)
**John Björkman Nilsson** · 2022-02-14

<details>
<summary>Abstract</summary>

Presented here is a method for automatic punctuation restoration in Swedish using a BERT model. The method is based on KB-BERT, a publicly available, neural network language model pre-trained on a Swedish corpus by National Library of Sweden. This model has then been fine-tuned for this specific task using a corpus of government texts. With a lower-case and unpunctuated Swedish text as input, the model is supposed to return a grammatically correct punctuated copy of the text as output. A successful solution to this problem brings benefits for an array of NLP domains, such as speech-to-text and automated text. Only the punctuation marks period, comma and question marks were considered for the project, due to a lack of data for more rare marks such as semicolon. Additionally, some marks are somewhat interchangeable with the more common, such as exclamation points and periods. Thus, the data set had all exclamation points replaced with periods. The fine-tuned Swedish BERT model, dubbed prestoBERT, achieved an overall F1-score of 78.9. The proposed model scored similarly to international counterparts, with Hungarian and Chinese models obtaining F1-scores of 82.2 and 75.6 respectively. As further comparison, a human evaluation case study was carried out. The human test group achieved an overall F1-score of 81.7, but scored substantially worse than prestoBERT on both period and comma. Inspecting output sentences from the model and humans show satisfactory results, despite the difference in F1-score. The disconnect seems to stem from an unnecessary focus on replicating the exact same punctuation used in the test set, rather than providing any of the number of correct interpretations. If the loss function could be rewritten to reward all grammatically correct outputs, rather than only the one original example, the performance could improve significantly for both prestoBERT and the human group.

</details>

### [Multimodal Depression Classification Using Articulatory Coordination Features And Hierarchical Attention Based Text Embeddings](2202.06238.md)
**Nadee Seneviratne, Carol Espy-Wilson** · 2022-02-13

<details>
<summary>Abstract</summary>

Multimodal depression classification has gained immense popularity over the recent years. We develop a multimodal depression classification system using articulatory coordination features extracted from vocal tract variables and text transcriptions obtained from an automatic speech recognition tool that yields improvements of area under the receiver operating characteristics curve compared to uni-modal classifiers (7.5% and 13.7% for audio and text respectively). We show that in the case of limited training data, a segment-level classifier can first be trained to then obtain a session-wise prediction without hindering the performance, using a multi-stage convolutional recurrent neural network. A text model is trained using a Hierarchical Attention Network (HAN). The multimodal system is developed by combining embeddings from the session-level audio model and the HAN text model

</details>

### [USTED: Improving ASR with a Unified Speech and Text Encoder-Decoder](2202.06045.md)
**Bolaji Yusuf, Ankur Gandhe, Alex Sokolov** · 2022-02-12

<details>
<summary>Abstract</summary>

Improving end-to-end speech recognition by incorporating external text data has been a longstanding research topic. There has been a recent focus on training E2E ASR models that get the performance benefits of external text data without incurring the extra cost of evaluating an external language model at inference time. In this work, we propose training ASR model jointly with a set of text-to-text auxiliary tasks with which it shares a decoder and parts of the encoder. When we jointly train ASR and masked language model with the 960-hour Librispeech and Opensubtitles data respectively, we observe WER reductions of 16% and 20% on test-other and test-clean respectively over an ASR-only baseline without any extra cost at inference time, and reductions of 6% and 8% compared to a stronger MUTE-L baseline which trains the decoder with the same text data as our model. We achieve further improvements when we train masked language model on Librispeech data or when we use machine translation as the auxiliary task, without significantly sacrificing performance on the task itself.

</details>

### [Wav2Vec2.0 on the Edge: Performance Evaluation](2202.05993.md)
**Santosh Gondi** · 2022-02-12

<details>
<summary>Abstract</summary>

Wav2Vec2.0 is a state-of-the-art model which learns speech representations through unlabeled speech data, aka, self supervised learning. The pretrained model is then fine tuned on small amounts of labeled data to use it for speech-to-text and machine translation tasks. Wav2Vec 2.0 is a transformative solution for low resource languages as it is mainly developed using unlabeled audio data. Getting large amounts of labeled data is resource intensive and especially challenging to do for low resource languages such as Swahilli, Tatar, etc. Furthermore, Wav2Vec2.0 word-error-rate(WER) matches or surpasses the very recent supervised learning algorithms while using 100x less labeled data. Given its importance and enormous potential in enabling speech based tasks on world's 7000 languages, it is key to evaluate the accuracy, latency and efficiency of this model on low resource and low power edge devices and investigate the feasibility of using it in such devices for private, secure and reliable speech based tasks. On-device speech tasks preclude sending audio data to the server hence inherently providing privacy, reduced latency and enhanced reliability. In this paper, Wav2Vec2.0 model's accuracy and latency has been evaluated on Raspberry Pi along with the KenLM language model for speech recognition tasks. How to tune certain parameters to achieve desired level of WER rate and latency while meeting the CPU, memory and energy budgets of the product has been discussed.

</details>

### [FAAG: Fast Adversarial Audio Generation through Interactive Attack Optimisation](2202.05416.md)
**Yuantian Miao, Chao Chen, Lei Pan, Jun Zhang et al.** · 2022-02-11

<details>
<summary>Abstract</summary>

Automatic Speech Recognition services (ASRs) inherit deep neural networks' vulnerabilities like crafted adversarial examples. Existing methods often suffer from low efficiency because the target phases are added to the entire audio sample, resulting in high demand for computational resources. This paper proposes a novel scheme named FAAG as an iterative optimization-based method to generate targeted adversarial examples quickly. By injecting the noise over the beginning part of the audio, FAAG generates adversarial audio in high quality with a high success rate timely. Specifically, we use audio's logits output to map each character in the transcription to an approximate position of the audio's frame. Thus, an adversarial example can be generated by FAAG in approximately two minutes using CPUs only and around ten seconds with one GPU while maintaining an average success rate over 85%. Specifically, the FAAG method can speed up around 60% compared with the baseline method during the adversarial example generation process. Furthermore, we found that appending benign audio to any suspicious examples can effectively defend against the targeted adversarial attack. We hope that this work paves the way for inventing new adversarial attacks against speech recognition with computational constraints.

</details>

### [Improving Automatic Speech Recognition for Non-Native English with Transfer Learning and Language Model Decoding](2202.05209.md)
**Peter Sullivan, Toshiko Shibano, Muhammad Abdul-Mageed** · 2022-02-10

<details>
<summary>Abstract</summary>

ASR systems designed for native English (L1) usually underperform on non-native English (L2). To address this performance gap, \textbf{(i)} we extend our previous work to investigate fine-tuning of a pre-trained wav2vec 2.0 model \cite{baevski2020wav2vec,xu2021self} under a rich set of L1 and L2 training conditions. We further \textbf{(ii)} incorporate language model decoding in the ASR system, along with the fine-tuning method. Quantifying gains acquired from each of these two approaches separately and an error analysis allows us to identify different sources of improvement within our models. We find that while the large self-trained wav2vec 2.0 may be internalizing sufficient decoding knowledge for clean L1 speech \cite{xu2021self}, this does not hold for L2 speech and accounts for the utility of employing language model decoding on L2 data.

</details>

### [ASRPU: A Programmable Accelerator for Low-Power Automatic Speech Recognition](2202.04971.md)
**Dennis Pinto, Jose-María Arnau, Antonio González** · 2022-02-10

<details>
<summary>Abstract</summary>

The outstanding accuracy achieved by modern Automatic Speech Recognition (ASR) systems is enabling them to quickly become a mainstream technology. ASR is essential for many applications, such as speech-based assistants, dictation systems and real-time language translation. However, highly accurate ASR systems are computationally expensive, requiring on the order of billions of arithmetic operations to decode each second of audio, which conflicts with a growing interest in deploying ASR on edge devices. On these devices, hardware acceleration is key for achieving acceptable performance. However, ASR is a rich and fast-changing field, and thus, any overly specialized hardware accelerator may quickly become obsolete. In this paper, we tackle those challenges by proposing ASRPU, a programmable accelerator for on-edge ASR. ASRPU contains a pool of general-purpose cores that execute small pieces of parallel code. Each of these programs computes one part of the overall decoder (e.g. a layer in a neural network). The accelerator automates some carefully chosen parts of the decoder to simplify the programming without sacrificing generality. We provide an analysis of a modern ASR system implemented on ASRPU and show that this architecture can achieve real-time decoding with a very low power budget.

</details>

### [The Volcspeech system for the ICASSP 2022 multi-channel multi-party meeting transcription challenge](2202.04261.md)
**Chen Shen, Yi Liu, Wenzhi Fan, Bin Wang et al.** · 2022-02-09

<details>
<summary>Abstract</summary>

This paper describes our submission to ICASSP 2022 Multi-channel Multi-party Meeting Transcription (M2MeT) Challenge. For Track 1, we propose several approaches to empower the clustering-based speaker diarization system to handle overlapped speech. Front-end dereverberation and the direction-of-arrival (DOA) estimation are used to improve the accuracy of speaker diarization. Multi-channel combination and overlap detection are applied to reduce the missed speaker error. A modified DOVER-Lap is also proposed to fuse the results of different systems. We achieve the final DER of 5.79% on the Eval set and 7.23% on the Test set. For Track 2, we develop our system using the Conformer model in a joint CTC-attention architecture. Serialized output training is adopted to multi-speaker overlapped speech recognition. We propose a neural front-end module to model multi-channel audio and train the model end-to-end. Various data augmentation methods are utilized to mitigate over-fitting in the multi-channel multi-speaker E2E system. Transformer language model fusion is developed to achieve better performance. The final CER is 19.2% on the Eval set and 20.8% on the Test set.

</details>

### [RNN Transducers for Nested Named Entity Recognition with constraints on alignment for long sequences](2203.03543.md)
**Hagen Soltau, Izhak Shafran, Mingqiu Wang, Laurent El Shafey** · 2022-02-08

<details>
<summary>Abstract</summary>

Popular solutions to Named Entity Recognition (NER) include conditional random fields, sequence-to-sequence models, or utilizing the question-answering framework. However, they are not suitable for nested and overlapping spans with large ontologies and for predicting the position of the entities. To fill this gap, we introduce a new model for NER task -- an RNN transducer (RNN-T). These models are trained using paired input and output sequences without explicitly specifying the alignment between them, similar to other seq-to-seq models. RNN-T models learn the alignment using a loss function that sums over all alignments. In NER tasks, however, the alignment between words and target labels are available from the human annotations. We propose a fixed alignment RNN-T model that utilizes the given alignment, while preserving the benefits of RNN-Ts such as modeling output dependencies. As a more general case, we also propose a constrained alignment model where users can specify a relaxation of the given input alignment and the model will learn an alignment within the given constraints. In other words, we propose a family of seq-to-seq models which can leverage alignments between input and target sequences when available. Through empirical experiments on a challenging real-world medical NER task with multiple nested ontologies, we demonstrate that our fixed alignment model outperforms the standard RNN-T model, improving F1-score from 0.70 to 0.74.

</details>

### [data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language](2202.03555.md)
**Alexei Baevski, Wei-Ning Hsu, Qiantong Xu, Arun Babu et al.** · 2022-02-07

<details>
<summary>Abstract</summary>

While the general idea of self-supervised learning is identical across modalities, the actual algorithms and objectives differ widely because they were developed with a single modality in mind. To get us closer to general self-supervised learning, we present data2vec, a framework that uses the same learning method for either speech, NLP or computer vision. The core idea is to predict latent representations of the full input data based on a masked view of the input in a self-distillation setup using a standard Transformer architecture. Instead of predicting modality-specific targets such as words, visual tokens or units of human speech which are local in nature, data2vec predicts contextualized latent representations that contain information from the entire input. Experiments on the major benchmarks of speech recognition, image classification, and natural language understanding demonstrate a new state of the art or competitive performance to predominant approaches.

</details>

### [Efficient Adapter Transfer of Self-Supervised Speech Models for Automatic Speech Recognition](2202.03218.md)
**Bethan Thomas, Samuel Kessler, Salah Karout** · 2022-02-07

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) is a powerful tool that allows learning of underlying representations from unlabeled data. Transformer based models such as wav2vec 2.0 and HuBERT are leading the field in the speech domain. Generally these models are fine-tuned on a small amount of labeled data for a downstream task such as Automatic Speech Recognition (ASR). This involves re-training the majority of the model for each task. Adapters are small lightweight modules which are commonly used in Natural Language Processing (NLP) to adapt pre-trained models to new tasks. In this paper we propose applying adapters to wav2vec 2.0 to reduce the number of parameters required for downstream ASR tasks, and increase scalability of the model to multiple tasks or languages. Using adapters we can perform ASR while training fewer than 10% of parameters per task compared to full fine-tuning with little degradation of performance. Ablations show that applying adapters into just the top few layers of the pre-trained network gives similar performance to full transfer, supporting the theory that higher pre-trained layers encode more phonemic information, and further optimizing efficiency.

</details>

### [T-NGA: Temporal Network Grafting Algorithm for Learning to Process Spiking Audio Sensor Events](2202.03204.md)
**Shu Wang, Yuhuang Hu, Shih-Chii Liu** · 2022-02-07

<details>
<summary>Abstract</summary>

Spiking silicon cochlea sensors encode sound as an asynchronous stream of spikes from different frequency channels. The lack of labeled training datasets for spiking cochleas makes it difficult to train deep neural networks on the outputs of these sensors. This work proposes a self-supervised method called Temporal Network Grafting Algorithm (T-NGA), which grafts a recurrent network pretrained on spectrogram features so that the network works with the cochlea event features. T-NGA training requires only temporally aligned audio spectrograms and event features. Our experiments show that the accuracy of the grafted network was similar to the accuracy of a supervised network trained from scratch on a speech recognition task using events from a software spiking cochlea model. Despite the circuit non-idealities of the spiking silicon cochlea, the grafted network accuracy on the silicon cochlea spike recordings was only about 5% lower than the supervised network accuracy using the N-TIDIGITS18 dataset. T-NGA can train networks to process spiking audio sensor events in the absence of large labeled spike datasets.

</details>

### [Semantic-aware Speech to Text Transmission with Redundancy Removal](2202.03211.md)
**Tianxiao Han, Qianqian Yang, Zhiguo Shi, Shibo He et al.** · 2022-02-07

<details>
<summary>Abstract</summary>

Deep learning (DL) based semantic communication methods have been explored for the efficient transmission of images, text, and speech in recent years. In contrast to traditional wireless communication methods that focus on the transmission of abstract symbols, semantic communication approaches attempt to achieve better transmission efficiency by only sending the semantic-related information of the source data. In this paper, we consider semantic-oriented speech to text transmission. We propose a novel end-to-end DL-based transceiver, which includes an attention-based soft alignment module and a redundancy removal module to compress the transmitted data. In particular, the former extracts only the text-related semantic features, and the latter further drops the semantically redundant content, greatly reducing the amount of semantic redundancy compared to existing methods. We also propose a two-stage training scheme, which speeds up the training of the proposed DL model. The simulation results indicate that our proposed method outperforms current methods in terms of the accuracy of the received text and transmission efficiency. Moreover, the proposed method also has a smaller model size and shorter end-to-end runtime.

</details>

### [Polyphonic pitch detection with convolutional recurrent neural networks](2202.02115.md)
**Carl Thomé, Sven Ahlbäck** · 2022-02-04

<details>
<summary>Abstract</summary>

Recent directions in automatic speech recognition (ASR) research have shown that applying deep learning models from image recognition challenges in computer vision is beneficial. As automatic music transcription (AMT) is superficially similar to ASR, in the sense that methods often rely on transforming spectrograms to symbolic sequences of events (e.g. words or notes), deep learning should benefit AMT as well. In this work, we outline an online polyphonic pitch detection system that streams audio to MIDI by ConvLSTMs. Our system achieves state-of-the-art results on the 2007 MIREX multi-F0 development set, with an F-measure of 83\% on the bassoon, clarinet, flute, horn and oboe ensemble recording without requiring any musical language modelling or assumptions of instrument timbre.

</details>

### [Self-supervised Learning with Random-projection Quantizer for Speech Recognition](2202.01855.md)
**Chung-Cheng Chiu, James Qin, Yu Zhang, Jiahui Yu et al.** · 2022-02-03

<details>
<summary>Abstract</summary>

We present a simple and effective self-supervised learning approach for speech recognition. The approach learns a model to predict the masked speech signals, in the form of discrete labels generated with a random-projection quantizer. In particular the quantizer projects speech inputs with a randomly initialized matrix, and does a nearest-neighbor lookup in a randomly-initialized codebook. Neither the matrix nor the codebook is updated during self-supervised learning. Since the random-projection quantizer is not trained and is separated from the speech recognition model, the design makes the approach flexible and is compatible with universal speech recognition architecture. On LibriSpeech our approach achieves similar word-error-rates as previous work using self-supervised learning with non-streaming models, and provides lower word-error-rates and latency than wav2vec 2.0 and w2v-BERT with streaming models. On multilingual tasks the approach also provides significant improvement over wav2vec 2.0 and w2v-BERT.

</details>

### [The RoyalFlush System of Speech Recognition for M2MeT Challenge](2202.01614.md)
**Shuaishuai Ye, Peiyao Wang, Shunfei Chen, Xinhui Hu et al.** · 2022-02-03

<details>
<summary>Abstract</summary>

This paper describes our RoyalFlush system for the track of multi-speaker automatic speech recognition (ASR) in the M2MeT challenge. We adopted the serialized output training (SOT) based multi-speakers ASR system with large-scale simulation data. Firstly, we investigated a set of front-end methods, including multi-channel weighted predicted error (WPE), beamforming, speech separation, speech enhancement and so on, to process training, validation and test sets. But we only selected WPE and beamforming as our frontend methods according to their experimental results. Secondly, we made great efforts in the data augmentation for multi-speaker ASR, mainly including adding noise and reverberation, overlapped speech simulation, multi-channel speech simulation, speed perturbation, front-end processing, and so on, which brought us a great performance improvement. Finally, in order to make full use of the performance complementary of different model architecture, we trained the standard conformer based joint CTC/Attention (Conformer) and U2++ ASR model with a bidirectional attention decoder, a modification of Conformer, to fuse their results. Comparing with the official baseline system, our system got a 12.22% absolute Character Error Rate (CER) reduction on the validation set and 12.11% on the test set.

</details>

### [Joint Speech Recognition and Audio Captioning](2202.01405.md)
**Chaitanya Narisetty, Emiru Tsunoo, Xuankai Chang, Yosuke Kashiwagi et al.** · 2022-02-03

<details>
<summary>Abstract</summary>

Speech samples recorded in both indoor and outdoor environments are often contaminated with secondary audio sources. Most end-to-end monaural speech recognition systems either remove these background sounds using speech enhancement or train noise-robust models. For better model interpretability and holistic understanding, we aim to bring together the growing field of automated audio captioning (AAC) and the thoroughly studied automatic speech recognition (ASR). The goal of AAC is to generate natural language descriptions of contents in audio samples. We propose several approaches for end-to-end joint modeling of ASR and AAC tasks and demonstrate their advantages over traditional approaches, which model these tasks independently. A major hurdle in evaluating our proposed approach is the lack of labeled audio datasets with both speech transcriptions and audio captions. Therefore we also create a multi-task dataset by mixing the clean speech Wall Street Journal corpus with multiple levels of background noises chosen from the AudioCaps dataset. We also perform extensive experimental evaluation and show improvements of our proposed methods as compared to existing state-of-the-art ASR and AAC methods.

</details>

### [mSLAM: Massively multilingual joint pre-training for speech and text](2202.01374.md)
**Ankur Bapna, Colin Cherry, Yu Zhang, Ye Jia et al.** · 2022-02-03

<details>
<summary>Abstract</summary>

We present mSLAM, a multilingual Speech and LAnguage Model that learns cross-lingual cross-modal representations of speech and text by pre-training jointly on large amounts of unlabeled speech and text in multiple languages. mSLAM combines w2v-BERT pre-training on speech with SpanBERT pre-training on character-level text, along with Connectionist Temporal Classification (CTC) losses on paired speech and transcript data, to learn a single model capable of learning from and representing both speech and text signals in a shared representation space. We evaluate mSLAM on several downstream speech understanding tasks and find that joint pre-training with text improves quality on speech translation, speech intent classification and speech language-ID while being competitive on multilingual ASR, when compared against speech-only pre-training. Our speech translation model demonstrates zero-shot text translation without seeing any text translation data, providing evidence for cross-modal alignment of representations. mSLAM also benefits from multi-modal fine-tuning, further improving the quality of speech translation by directly leveraging text translation data during the fine-tuning process. Our empirical analysis highlights several opportunities and challenges arising from large-scale multimodal pre-training, suggesting directions for future research.

</details>

### [ASR-Aware End-to-end Neural Diarization](2202.01286.md)
**Aparna Khare, Eunjung Han, Yuguang Yang, Andreas Stolcke** · 2022-02-02

<details>
<summary>Abstract</summary>

We present a Conformer-based end-to-end neural diarization (EEND) model that uses both acoustic input and features derived from an automatic speech recognition (ASR) model. Two categories of features are explored: features derived directly from ASR output (phones, position-in-word and word boundaries) and features derived from a lexical speaker change detection model, trained by fine-tuning a pretrained BERT model on the ASR output. Three modifications to the Conformer-based EEND architecture are proposed to incorporate the features. First, ASR features are concatenated with acoustic features. Second, we propose a new attention mechanism called contextualized self-attention that utilizes ASR features to build robust speaker representations. Finally, multi-task learning is used to train the model to minimize classification loss for the ASR features along with diarization loss. Experiments on the two-speaker English conversations of Switchboard+SRE data sets show that multi-task learning with position-in-word information is the most effective way of utilizing ASR features, reducing the diarization error rate (DER) by 20% relative to the baseline.

</details>

### [Error Correction in ASR using Sequence-to-Sequence Models](2202.01157.md)
**Samrat Dutta, Shreyansh Jain, Ayush Maheshwari, Souvik Pal et al.** · 2022-02-02

<details>
<summary>Abstract</summary>

Post-editing in Automatic Speech Recognition (ASR) entails automatically correcting common and systematic errors produced by the ASR system. The outputs of an ASR system are largely prone to phonetic and spelling errors. In this paper, we propose to use a powerful pre-trained sequence-to-sequence model, BART, further adaptively trained to serve as a denoising model, to correct errors of such types. The adaptive training is performed on an augmented dataset obtained by synthetically inducing errors as well as by incorporating actual errors from an existing ASR system. We also propose a simple approach to rescore the outputs using word level alignments. Experimental results on accented speech data demonstrate that our strategy effectively rectifies a significant number of ASR errors and produces improved WER results when compared against a competitive baseline. We also highlight a negative result obtained on the related grammatical error correction task in Hindi language showing the limitation in capturing wider context by our proposed model.

</details>

### [RescoreBERT: Discriminative Speech Recognition Rescoring with BERT](2202.01094.md)
**Liyan Xu, Yile Gu, Jari Kolehmainen, Haidar Khan et al.** · 2022-02-02

<details>
<summary>Abstract</summary>

Second-pass rescoring is an important component in automatic speech recognition (ASR) systems that is used to improve the outputs from a first-pass decoder by implementing a lattice rescoring or $n$-best re-ranking. While pretraining with a masked language model (MLM) objective has received great success in various natural language understanding (NLU) tasks, it has not gained traction as a rescoring model for ASR. Specifically, training a bidirectional model like BERT on a discriminative objective such as minimum WER (MWER) has not been explored. Here we show how to train a BERT-based rescoring model with MWER loss, to incorporate the improvements of a discriminative loss into fine-tuning of deep bidirectional pretrained models for ASR. Specifically, we propose a fusion strategy that incorporates the MLM into the discriminative training process to effectively distill knowledge from a pretrained model. We further propose an alternative discriminative loss. This approach, which we call RescoreBERT, reduces WER by 6.6%/3.4% relative on the LibriSpeech clean/other test sets over a BERT baseline without discriminative objective. We also evaluate our method on an internal dataset from a conversational agent and find that it reduces both latency and WER (by 3 to 8% relative) over an LSTM rescoring model.

</details>

### [Streaming Multi-Talker ASR with Token-Level Serialized Output Training](2202.00842.md)
**Naoyuki Kanda, Jian Wu, Yu Wu, Xiong Xiao et al.** · 2022-02-02

<details>
<summary>Abstract</summary>

This paper proposes a token-level serialized output training (t-SOT), a novel framework for streaming multi-talker automatic speech recognition (ASR). Unlike existing streaming multi-talker ASR models using multiple output branches, the t-SOT model has only a single output branch that generates recognition tokens (e.g., words, subwords) of multiple speakers in chronological order based on their emission times. A special token that indicates the change of ``virtual'' output channels is introduced to keep track of the overlapping utterances. Compared to the prior streaming multi-talker ASR models, the t-SOT model has the advantages of less inference cost and a simpler model architecture. Moreover, in our experiments with LibriSpeechMix and LibriCSS datasets, the t-SOT-based transformer transducer model achieves the state-of-the-art word error rates by a significant margin to the prior results. For non-overlapping speech, the t-SOT model is on par with a single-talker ASR model in terms of both accuracy and computational cost, opening the door for deploying one model for both single- and multi-talker scenarios.

</details>

### [BEA-Base: A Benchmark for ASR of Spontaneous Hungarian](2202.00601.md)
**P. Mihajlik, A. Balog, T. E. Gráczi, A. Kohári et al.** · 2022-02-01

<details>
<summary>Abstract</summary>

Hungarian is spoken by 15 million people, still, easily accessible Automatic Speech Recognition (ASR) benchmark datasets - especially for spontaneous speech - have been practically unavailable. In this paper, we introduce BEA-Base, a subset of the BEA spoken Hungarian database comprising mostly spontaneous speech of 140 speakers. It is built specifically to assess ASR, primarily for conversational AI applications. After defining the speech recognition subsets and task, several baselines - including classic HMM-DNN hybrid and end-to-end approaches augmented by cross-language transfer learning - are developed using open-source toolkits. The best results obtained are based on multilingual self-supervised pretraining, achieving a 45% recognition error rate reduction as compared to the classical approach - without the application of an external language model or additional supervised data. The results show the feasibility of using BEA-Base for training and evaluation of Hungarian speech recognition systems.

</details>

### [Visualizing Automatic Speech Recognition -- Means for a Better Understanding?](2202.00673.md)
**Karla Markert, Romain Parracone, Mykhailo Kulakov, Philip Sperl et al.** · 2022-02-01

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is improving ever more at mimicking human speech processing. The functioning of ASR, however, remains to a large extent obfuscated by the complex structure of the deep neural networks (DNNs) they are based on. In this paper, we show how so-called attribution methods, that we import from image recognition and suitably adapt to handle audio data, can help to clarify the working of ASR. Taking DeepSpeech, an end-to-end model for ASR, as a case study, we show how these techniques help to visualize which features of the input are the most influential in determining the output. We focus on three visualization techniques: Layer-wise Relevance Propagation (LRP), Saliency Maps, and Shapley Additive Explanations (SHAP). We compare these methods and discuss potential further applications, such as in the detection of adversarial examples.

</details>

### [NAS-Bench-Suite: NAS Evaluation is (Now) Surprisingly Easy](2201.13396.md)
**Yash Mehta, Colin White, Arber Zela, Arjun Krishnakumar et al.** · 2022-01-31

<details>
<summary>Abstract</summary>

The release of tabular benchmarks, such as NAS-Bench-101 and NAS-Bench-201, has significantly lowered the computational overhead for conducting scientific research in neural architecture search (NAS). Although they have been widely adopted and used to tune real-world NAS algorithms, these benchmarks are limited to small search spaces and focus solely on image classification. Recently, several new NAS benchmarks have been introduced that cover significantly larger search spaces over a wide range of tasks, including object detection, speech recognition, and natural language processing. However, substantial differences among these NAS benchmarks have so far prevented their widespread adoption, limiting researchers to using just a few benchmarks. In this work, we present an in-depth analysis of popular NAS algorithms and performance prediction methods across 25 different combinations of search spaces and datasets, finding that many conclusions drawn from a few NAS benchmarks do not generalize to other benchmarks. To help remedy this problem, we introduce NAS-Bench-Suite, a comprehensive and extensible collection of NAS benchmarks, accessible through a unified interface, created with the aim to facilitate reproducible, generalizable, and rapid NAS research. Our code is available at https://github.com/automl/naslib.

</details>

### [Improving End-to-End Contextual Speech Recognition with Fine-Grained Contextual Knowledge Selection](2201.12806.md)
**Minglun Han, Linhao Dong, Zhenlin Liang, Meng Cai et al.** · 2022-01-30

<details>
<summary>Abstract</summary>

Nowadays, most methods in end-to-end contextual speech recognition bias the recognition process towards contextual knowledge. Since all-neural contextual biasing methods rely on phrase-level contextual modeling and attention-based relevance modeling, they may encounter confusion between similar context-specific phrases, which hurts predictions at the token level. In this work, we focus on mitigating confusion problems with fine-grained contextual knowledge selection (FineCoS). In FineCoS, we introduce fine-grained knowledge to reduce the uncertainty of token predictions. Specifically, we first apply phrase selection to narrow the range of phrase candidates, and then conduct token attention on the tokens in the selected phrase candidates. Moreover, we re-normalize the attention weights of most relevant phrases in inference to obtain more focused phrase-level contextual representations, and inject position information to better discriminate phrases or tokens. On LibriSpeech and an in-house 160,000-hour dataset, we explore the proposed methods based on a controllable all-neural biasing method, collaborative decoding (ColDec). The proposed methods provide at most 6.1% relative word error rate reduction on LibriSpeech and 16.4% relative character error rate reduction on the in-house dataset over ColDec.

</details>

### [Reducing language context confusion for end-to-end code-switching automatic speech recognition](2201.12155.md)
**Shuai Zhang, Jiangyan Yi, Zhengkun Tian, Jianhua Tao et al.** · 2022-01-28

<details>
<summary>Abstract</summary>

Code-switching deals with alternative languages in communication process. Training end-to-end (E2E) automatic speech recognition (ASR) systems for code-switching is especially challenging as code-switching training data are always insufficient to combat the increased multilingual context confusion due to the presence of more than one language. We propose a language-related attention mechanism to reduce multilingual context confusion for the E2E code-switching ASR model based on the Equivalence Constraint (EC) Theory. The linguistic theory requires that any monolingual fragment that occurs in the code-switching sentence must occur in one of the monolingual sentences. The theory establishes a bridge between monolingual data and code-switching data. We leverage this linguistics theory to design the code-switching E2E ASR model. The proposed model efficiently transfers language knowledge from rich monolingual data to improve the performance of the code-switching ASR model. We evaluate our model on ASRU 2019 Mandarin-English code-switching challenge dataset. Compared to the baseline model, our proposed model achieves a 17.12% relative error reduction.

</details>

### [Improving End-to-End Models for Set Prediction in Spoken Language Understanding](2201.12105.md)
**Hong-Kwang J. Kuo, Zoltan Tuske, Samuel Thomas, Brian Kingsbury et al.** · 2022-01-28

<details>
<summary>Abstract</summary>

The goal of spoken language understanding (SLU) systems is to determine the meaning of the input speech signal, unlike speech recognition which aims to produce verbatim transcripts. Advances in end-to-end (E2E) speech modeling have made it possible to train solely on semantic entities, which are far cheaper to collect than verbatim transcripts. We focus on this set prediction problem, where entity order is unspecified. Using two classes of E2E models, RNN transducers and attention based encoder-decoders, we show that these models work best when the training entity sequence is arranged in spoken order. To improve E2E SLU models when entity spoken order is unknown, we propose a novel data augmentation technique along with an implicit attention based alignment method to infer the spoken order. F1 scores significantly increased by more than 11% for RNN-T and about 2% for attention based encoder-decoder SLU models, outperforming previously reported results.

</details>

### [Neural-FST Class Language Model for End-to-End Speech Recognition](2201.11867.md)
**Antoine Bruguier, Duc Le, Rohit Prabhavalkar, Dangna Li et al.** · 2022-01-28

<details>
<summary>Abstract</summary>

We propose Neural-FST Class Language Model (NFCLM) for end-to-end speech recognition, a novel method that combines neural network language models (NNLMs) and finite state transducers (FSTs) in a mathematically consistent framework. Our method utilizes a background NNLM which models generic background text together with a collection of domain-specific entities modeled as individual FSTs. Each output token is generated by a mixture of these components; the mixture weights are estimated with a separately trained neural decider. We show that NFCLM significantly outperforms NNLM by 15.8% relative in terms of Word Error Rate. NFCLM achieves similar performance as traditional NNLM and FST shallow fusion while being less prone to overbiasing and 12 times more compact, making it more suitable for on-device usage.

</details>

### [Synthesizing Dysarthric Speech Using Multi-talker TTS for Dysarthric Speech Recognition](2201.11571.md)
**Mohammad Soleymanpour, Michael T. Johnson, Rahim Soleymanpour, Jeffrey Berry** · 2022-01-27

<details>
<summary>Abstract</summary>

Dysarthria is a motor speech disorder often characterized by reduced speech intelligibility through slow, uncoordinated control of speech production muscles. Automatic Speech recognition (ASR) systems may help dysarthric talkers communicate more effectively. To have robust dysarthria-specific ASR, sufficient training speech is required, which is not readily available. Recent advances in Text-To-Speech (TTS) synthesis multi-speaker end-to-end TTS systems suggest the possibility of using synthesis for data augmentation. In this paper, we aim to improve multi-speaker end-to-end TTS systems to synthesize dysarthric speech for improved training of a dysarthria-specific DNN-HMM ASR. In the synthesized speech, we add dysarthria severity level and pause insertion mechanisms to other control parameters such as pitch, energy, and duration. Results show that a DNN-HMM model trained on additional synthetic dysarthric speech achieves WER improvement of 12.2% compared to the baseline, the addition of the severity level and pause insertion controls decrease WER by 6.5%, showing the effectiveness of adding these parameters. Audio samples are available at

</details>

### [On the Effectiveness of Pinyin-Character Dual-Decoding for End-to-End Mandarin Chinese ASR](2201.10792.md)
**Zhao Yang, Dianwen Ng, Xiao Fu, Liping Han et al.** · 2022-01-26

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) has achieved promising results. However, most existing end-to-end ASR methods neglect the use of specific language characteristics. For Mandarin Chinese ASR tasks, there exist mutual promotion relationship between Pinyin and Character where Chinese characters can be romanized by Pinyin. Based on the above intuition, we first investigate types of end-to-end encoder-decoder based models in the single-input dual-output (SIDO) multi-task framework, after which a novel asynchronous decoding with fuzzy Pinyin sampling method is proposed according to the one-to-one correspondence characteristics between Pinyin and Character. Furthermore, we proposed a two-stage training strategy to make training more stable and converge faster. The results on the test sets of AISHELL-1 dataset show that the proposed enhanced dual-decoder model without a language model is improved by a big margin compared to strong baseline models.

</details>

### [Tackling data scarcity in speech translation using zero-shot multilingual machine translation techniques](2201.11172.md)
**Tu Anh Dinh, Danni Liu, Jan Niehues** · 2022-01-26

<details>
<summary>Abstract</summary>

Recently, end-to-end speech translation (ST) has gained significant attention as it avoids error propagation. However, the approach suffers from data scarcity. It heavily depends on direct ST data and is less efficient in making use of speech transcription and text translation data, which is often more easily available. In the related field of multilingual text translation, several techniques have been proposed for zero-shot translation. A main idea is to increase the similarity of semantically similar sentences in different languages. We investigate whether these ideas can be applied to speech translation, by building ST models trained on speech transcription and text translation data. We investigate the effects of data augmentation and auxiliary loss function. The techniques were successfully applied to few-shot ST using limited ST data, with improvements of up to +12.9 BLEU points compared to direct end-to-end ST and +3.1 BLEU points compared to ST models fine-tuned from ASR model.

</details>

### [Transformer-Based Video Front-Ends for Audio-Visual Speech Recognition for Single and Multi-Person Video](2201.10439.md)
**Dmitriy Serdyuk, Otavio Braga, Olivier Siohan** · 2022-01-25

<details>
<summary>Abstract</summary>

Audio-visual automatic speech recognition (AV-ASR) extends speech recognition by introducing the video modality as an additional source of information. In this work, the information contained in the motion of the speaker's mouth is used to augment the audio features. The video modality is traditionally processed with a 3D convolutional neural network (e.g. 3D version of VGG). Recently, image transformer networks arXiv:2010.11929 demonstrated the ability to extract rich visual features for image classification tasks. Here, we propose to replace the 3D convolution with a video transformer to extract visual features. We train our baselines and the proposed model on a large scale corpus of YouTube videos. The performance of our approach is evaluated on a labeled subset of YouTube videos as well as on the LRS3-TED public corpus. Our best video-only model obtains 31.4% WER on YTDEV18 and 17.0% on LRS3-TED, a 10% and 15% relative improvements over our convolutional baseline. We achieve the state of the art performance of the audio-visual recognition on the LRS3-TED after fine-tuning our model (1.6% WER). In addition, in a series of experiments on multi-person AV-ASR, we obtained an average relative reduction of 2% over our convolutional video frontend.

</details>

### [Improving the fusion of acoustic and text representations in RNN-T](2201.10240.md)
**Chao Zhang, Bo Li, Zhiyun Lu, Tara N. Sainath et al.** · 2022-01-25

<details>
<summary>Abstract</summary>

The recurrent neural network transducer (RNN-T) has recently become the mainstream end-to-end approach for streaming automatic speech recognition (ASR). To estimate the output distributions over subword units, RNN-T uses a fully connected layer as the joint network to fuse the acoustic representations extracted using the acoustic encoder with the text representations obtained using the prediction network based on the previous subword units. In this paper, we propose to use gating, bilinear pooling, and a combination of them in the joint network to produce more expressive representations to feed into the output layer. A regularisation method is also proposed to enable better acoustic encoder training by reducing the gradients back-propagated into the prediction network at the beginning of RNN-T training. Experimental results on a multilingual ASR setting for voice search over nine languages show that the joint use of the proposed methods can result in 4%--5% relative word error rate reductions with only a few million extra parameters.

</details>

### [Run-and-back stitch search: novel block synchronous decoding for streaming encoder-decoder ASR](2201.10190.md)
**Emiru Tsunoo, Chaitanya Narisetty, Michael Hentschel, Yosuke Kashiwagi et al.** · 2022-01-25

<details>
<summary>Abstract</summary>

A streaming style inference of encoder-decoder automatic speech recognition (ASR) system is important for reducing latency, which is essential for interactive use cases. To this end, we propose a novel blockwise synchronous decoding algorithm with a hybrid approach that combines endpoint prediction and endpoint post-determination. In the endpoint prediction, we compute the expectation of the number of tokens that are yet to be emitted in the encoder features of the current blocks using the CTC posterior. Based on the expectation value, the decoder predicts the endpoint to realize continuous block synchronization, as a running stitch. Meanwhile, endpoint post-determination probabilistically detects backward jump of the source-target attention, which is caused by the misprediction of endpoints. Then it resumes decoding by discarding those hypotheses, as back stitch. We combine these methods into a hybrid approach, namely run-and-back stitch search, which reduces the computational cost and latency. Evaluations of various ASR tasks show the efficiency of our proposed decoding algorithm, which achieves a latency reduction, for instance in the Librispeech test set from 1487 ms to 821 ms at the 90th percentile, while maintaining a high recognition accuracy.

</details>

### [Improving non-autoregressive end-to-end speech recognition with pre-trained acoustic and language models](2201.10103.md)
**Keqi Deng, Zehui Yang, Shinji Watanabe, Yosuke Higuchi et al.** · 2022-01-25

<details>
<summary>Abstract</summary>

While Transformers have achieved promising results in end-to-end (E2E) automatic speech recognition (ASR), their autoregressive (AR) structure becomes a bottleneck for speeding up the decoding process. For real-world deployment, ASR systems are desired to be highly accurate while achieving fast inference. Non-autoregressive (NAR) models have become a popular alternative due to their fast inference speed, but they still fall behind AR systems in recognition accuracy. To fulfill the two demands, in this paper, we propose a NAR CTC/attention model utilizing both pre-trained acoustic and language models: wav2vec2.0 and BERT. To bridge the modality gap between speech and text representations obtained from the pre-trained models, we design a novel modality conversion mechanism, which is more suitable for logographic languages. During inference, we employ a CTC branch to generate a target length, which enables the BERT to predict tokens in parallel. We also design a cache-based CTC/attention joint decoding method to improve the recognition accuracy while keeping the decoding speed fast. Experimental results show that the proposed NAR model greatly outperforms our strong wav2vec2.0 CTC baseline (15.1% relative CER reduction on AISHELL-1). The proposed NAR model significantly surpasses previous NAR systems on the AISHELL-1 benchmark and shows a potential for English tasks.

</details>

### [SPIRAL: Self-supervised Perturbation-Invariant Representation Learning for Speech Pre-Training](2201.10207.md)
**Wenyong Huang, Zhenhe Zhang, Yu Ting Yeung, Xin Jiang et al.** · 2022-01-25

<details>
<summary>Abstract</summary>

We introduce a new approach for speech pre-training named SPIRAL which works by learning denoising representation of perturbed data in a teacher-student framework. Specifically, given a speech utterance, we first feed the utterance to a teacher network to obtain corresponding representation. Then the same utterance is perturbed and fed to a student network. The student network is trained to output representation resembling that of the teacher. At the same time, the teacher network is updated as moving average of student's weights over training steps. In order to prevent representation collapse, we apply an in-utterance contrastive loss as pre-training objective and impose position randomization on the input to the teacher. SPIRAL achieves competitive or better results compared to state-of-the-art speech pre-training method wav2vec 2.0, with significant reduction of training cost (80% for BASE model, 65% for LARGE model). Furthermore, we address the problem of noise-robustness that is critical to real-world speech applications. We propose multi-condition pre-training by perturbing the student's input with various types of additive noise. We demonstrate that multi-condition pre-trained SPIRAL models are more robust to noisy speech (9.0% - 13.3% relative word error rate reduction on real noisy test data), compared to applying multi-condition training solely in the fine-tuning stage. Source code is available at https://github.com/huawei-noah/Speech-Backbones/tree/main/SPIRAL.

</details>

### [Endpoint Detection for Streaming End-to-End Multi-talker ASR](2201.09979.md)
**Liang Lu, Jinyu Li, Yifan Gong** · 2022-01-24

<details>
<summary>Abstract</summary>

Streaming end-to-end multi-talker speech recognition aims at transcribing the overlapped speech from conversations or meetings with an all-neural model in a streaming fashion, which is fundamentally different from a modular-based approach that usually cascades the speech separation and the speech recognition models trained independently. Previously, we proposed the Streaming Unmixing and Recognition Transducer (SURT) model based on recurrent neural network transducer (RNN-T) for this problem and presented promising results. However, for real applications, the speech recognition system is also required to determine the timestamp when a speaker finishes speaking for prompt system response. This problem, known as endpoint (EP) detection, has not been studied previously for multi-talker end-to-end models. In this work, we address the EP detection problem in the SURT framework by introducing an end-of-sentence token as an output unit, following the practice of single-talker end-to-end models. Furthermore, we also present a latency penalty approach that can significantly cut down the EP detection latency. Our experimental results based on the 2-speaker LibrispeechMix dataset show that the SURT model can achieve promising EP detection without significantly degradation of the recognition accuracy.

</details>

### [PickNet: Real-Time Channel Selection for Ad Hoc Microphone Arrays](2201.09586.md)
**Takuya Yoshioka, Xiaofei Wang, Dongmei Wang** · 2022-01-24

<details>
<summary>Abstract</summary>

This paper proposes PickNet, a neural network model for real-time channel selection for an ad hoc microphone array consisting of multiple recording devices like cell phones. Assuming at most one person to be vocally active at each time point, PickNet identifies the device that is spatially closest to the active person for each time frame by using a short spectral patch of just hundreds of milliseconds. The model is applied to every time frame, and the short time frame signals from the selected microphones are concatenated across the frames to produce an output signal. As the personal devices are usually held close to their owners, the output signal is expected to have higher signal-to-noise and direct-to-reverberation ratios on average than the input signals. Since PickNet utilizes only limited acoustic context at each time frame, the system using the proposed model works in real time and is robust to changes in acoustic conditions. Speech recognition-based evaluation was carried out by using real conversational recordings obtained with various smartphones. The proposed model yielded significant gains in word error rate with limited computational cost over systems using a block-online beamformer and a single distant microphone.

</details>

### [Unified Multimodal Punctuation Restoration Framework for Mixed-Modality Corpus](2202.00468.md)
**Yaoming Zhu, Liwei Wu, Shanbo Cheng, Mingxuan Wang** · 2022-01-24

<details>
<summary>Abstract</summary>

The punctuation restoration task aims to correctly punctuate the output transcriptions of automatic speech recognition systems. Previous punctuation models, either using text only or demanding the corresponding audio, tend to be constrained by real scenes, where unpunctuated sentences are a mixture of those with and without audio. This paper proposes a unified multimodal punctuation restoration framework, named UniPunc, to punctuate the mixed sentences with a single model. UniPunc jointly represents audio and non-audio samples in a shared latent space, based on which the model learns a hybrid representation and punctuates both kinds of samples. We validate the effectiveness of the UniPunc on real-world datasets, which outperforms various strong baselines (e.g. BERT, MuSe) by at least 0.8 overall F1 scores, making a new state-of-the-art. Extensive experiments show that UniPunc's design is a pervasive solution: by grafting onto previous models, UniPunc enables them to punctuate on the mixed corpus. Our code is available at github.com/Yaoming95/UniPunc

</details>

### [Data and knowledge-driven approaches for multilingual training to improve the performance of speech recognition systems of Indian languages](2201.09494.md)
**A. Madhavaraj, Ramakrishnan Angarai Ganesan** · 2022-01-24

<details>
<summary>Abstract</summary>

We propose data and knowledge-driven approaches for multilingual training of the automated speech recognition (ASR) system for a target language by pooling speech data from multiple source languages. Exploiting the acoustic similarities between Indian languages, we implement two approaches. In phone/senone mapping, deep neural network (DNN) learns to map senones or phones from one language to the others, and the transcriptions of the source languages are modified such that they can be used along with the target language data to train and fine-tune the target language ASR system. In the other approach, we model the acoustic information for all the languages simultaneously by training a multitask DNN (MTDNN) to predict the senones of each language in different output layers. The cross-entropy loss and the weight update procedure are modified such that only the shared layers and the output layer responsible for predicting the senone classes of a language are updated during training, if the feature vector belongs to that particular language. In the low-resource setting (LRS), 40 hours of transcribed data each for Tamil, Telugu and Gujarati languages are used for training. The DNN based senone mapping technique gives relative improvements in word error rates (WER) of 9.66%, 7.2% and 15.21% over the baseline system for Tamil, Gujarati and Telugu languages, respectively. In medium-resourced setting (MRS), 160, 275 and 135 hours of data for Tamil, Kannada and Hindi languages are used, where, the same technique gives better relative improvements of 13.94%, 10.28% and 27.24% for Tamil, Kannada and Hindi, respectively. The MTDNN with senone mapping based training in LRS, gives higher relative WER improvements of 15.0%, 17.54% and 16.06%, respectively for Tamil, Gujarati and Telugu, whereas in MRS, we see improvements of 21.24% 21.05% and 30.17% for Tamil, Kannada and Hindi languages, respectively.

</details>

### [Investigation of Deep Neural Network Acoustic Modelling Approaches for Low Resource Accented Mandarin Speech Recognition](2201.09432.md)
**Xurong Xie, Xiang Sui, Xunying Liu, Lan Wang** · 2022-01-24

<details>
<summary>Abstract</summary>

The Mandarin Chinese language is known to be strongly influenced by a rich set of regional accents, while Mandarin speech with each accent is quite low resource. Hence, an important task in Mandarin speech recognition is to appropriately model the acoustic variabilities imposed by accents. In this paper, an investigation of implicit and explicit use of accent information on a range of deep neural network (DNN) based acoustic modelling techniques is conducted. Meanwhile, approaches of multi-accent modelling including multi-style training, multi-accent decision tree state tying, DNN tandem and multi-level adaptive network (MLAN) tandem hidden Markov model (HMM) modelling are combined and compared in this paper. On a low resource accented Mandarin speech recognition task consisting of four regional accents, an improved MLAN tandem HMM systems explicitly leveraging the accent information was proposed and significantly outperformed the baseline accent independent DNN tandem systems by 0.8%-1.5% absolute (6%-9% relative) in character error rate after sequence level discriminative training and adaptation.

</details>

### [Variational Auto-Encoder Based Variability Encoding for Dysarthric Speech Recognition](2201.09422.md)
**Xurong Xie, Rukiye Ruzi, Xunying Liu, Lan Wang** · 2022-01-24

<details>
<summary>Abstract</summary>

Dysarthric speech recognition is a challenging task due to acoustic variability and limited amount of available data. Diverse conditions of dysarthric speakers account for the acoustic variability, which make the variability difficult to be modeled precisely. This paper presents a variational auto-encoder based variability encoder (VAEVE) to explicitly encode such variability for dysarthric speech. The VAEVE makes use of both phoneme information and low-dimensional latent variable to reconstruct the input acoustic features, thereby the latent variable is forced to encode the phoneme-independent variability. Stochastic gradient variational Bayes algorithm is applied to model the distribution for generating variability encodings, which are further used as auxiliary features for DNN acoustic modeling. Experiment results conducted on the UASpeech corpus show that the VAEVE based variability encodings have complementary effect to the learning hidden unit contributions (LHUC) speaker adaptation. The systems using variability encodings consistently outperform the comparable baseline systems without using them, and" obtain absolute word error rate (WER) reduction by up to 2.2% on dysarthric speech with "Very lowintelligibility level, and up to 2% on the "Mixed" type of dysarthric speech with diverse or uncertain conditions.

</details>

### [Enabling Deep Learning on Edge Devices through Filter Pruning and Knowledge Transfer](2201.10947.md)
**Kaiqi Zhao, Yitao Chen, Ming Zhao** · 2022-01-22

<details>
<summary>Abstract</summary>

Deep learning models have introduced various intelligent applications to edge devices, such as image classification, speech recognition, and augmented reality. There is an increasing need of training such models on the devices in order to deliver personalized, responsive, and private learning. To address this need, this paper presents a new solution for deploying and training state-of-the-art models on the resource-constrained devices. First, the paper proposes a novel filter-pruning-based model compression method to create lightweight trainable models from large models trained in the cloud, without much loss of accuracy. Second, it proposes a novel knowledge transfer method to enable the on-device model to update incrementally in real time or near real time using incremental learning on new data and enable the on-device model to learn the unseen categories with the help of the in-cloud model in an unsupervised fashion. The results show that 1) our model compression method can remove up to 99.36% parameters of WRN-28-10, while preserving a Top-1 accuracy of over 90% on CIFAR-10; 2) our knowledge transfer method enables the compressed models to achieve more than 90% accuracy on CIFAR-10 and retain good accuracy on old categories; 3) it allows the compressed models to converge within real time (three to six minutes) on the edge for incremental learning tasks; 4) it enables the model to classify unseen categories of data (78.92% Top-1 accuracy) that it is never trained with.

</details>

### [A Noise-Robust Self-supervised Pre-training Model Based Speech Representation Learning for Automatic Speech Recognition](2201.08930.md)
**Qiu-Shi Zhu, Jie Zhang, Zi-Qiang Zhang, Ming-Hui Wu et al.** · 2022-01-22

<details>
<summary>Abstract</summary>

Wav2vec2.0 is a popular self-supervised pre-training framework for learning speech representations in the context of automatic speech recognition (ASR). It was shown that wav2vec2.0 has a good robustness against the domain shift, while the noise robustness is still unclear. In this work, we therefore first analyze the noise robustness of wav2vec2.0 via experiments. We observe that wav2vec2.0 pre-trained on noisy data can obtain good representations and thus improve the ASR performance on the noisy test set, which however brings a performance degradation on the clean test set. To avoid this issue, in this work we propose an enhanced wav2vec2.0 model. Specifically, the noisy speech and the corresponding clean version are fed into the same feature encoder, where the clean speech provides training targets for the model. Experimental results reveal that the proposed method can not only improve the ASR performance on the noisy test set which surpasses the original wav2vec2.0, but also ensure a tiny performance decrease on the clean test set. In addition, the effectiveness of the proposed method is demonstrated under different types of noise conditions.

</details>

### [Human and Automatic Speech Recognition Performance on German Oral History Interviews](2201.06841.md)
**Michael Gref, Nike Matthiesen, Christoph Schmidt, Sven Behnke et al.** · 2022-01-18

<details>
<summary>Abstract</summary>

Automatic speech recognition systems have accomplished remarkable improvements in transcription accuracy in recent years. On some domains, models now achieve near-human performance. However, transcription performance on oral history has not yet reached human accuracy. In the present work, we investigate how large this gap between human and machine transcription still is. For this purpose, we analyze and compare transcriptions of three humans on a new oral history data set. We estimate a human word error rate of 8.7% for recent German oral history interviews with clean acoustic conditions. For comparison with recent machine transcription accuracy, we present experiments on the adaptation of an acoustic model achieving near-human performance on broadcast speech. We investigate the influence of different adaptation data on robustness and generalization for clean and noisy oral history interviews. We optimize our acoustic models by 5 to 8% relative for this task and achieve 23.9% WER on noisy and 15.6% word error rate on clean oral history interviews.

</details>

### [Handling Compounding in Mobile Keyboard Input](2201.06469.md)
**Andreas Kabel, Keith Hall, Tom Ouyang, David Rybach et al.** · 2022-01-17

<details>
<summary>Abstract</summary>

This paper proposes a framework to improve the typing experience of mobile users in morphologically rich languages. Smartphone keyboards typically support features such as input decoding, corrections and predictions that all rely on language models. For latency reasons, these operations happen on device, so the models are of limited size and cannot easily cover all the words needed by users for their daily tasks, especially in morphologically rich languages. In particular, the compounding nature of Germanic languages makes their vocabulary virtually infinite. Similarly, heavily inflecting and agglutinative languages (e.g. Slavic, Turkic or Finno-Ugric languages) tend to have much larger vocabularies than morphologically simpler languages, such as English or Mandarin. We propose to model such languages with automatically selected subword units annotated with what we call binding types, allowing the decoder to know when to bind subword units into words. We show that this method brings around 20% word error rate reduction in a variety of compounding languages. This is more than twice the improvement we previously obtained with a more basic approach, also described in the paper.

</details>

### [A Comparison of Hybrid and End-to-End ASR Systems for the IberSpeech-RTVE 2020 Speech-to-Text Transcription Challenge](s2:a5d5a233bc54bd8ea1cabea7bb1275e9875df134.md)
**Juan M. Perero-Codosero, Fernando M. Espinoza-Cuadros, L. Hernández-Gómez** · 2022-01-17

<details>
<summary>Abstract</summary>

This paper describes a comparison between hybrid and end-to-end Automatic Speech Recognition (ASR) systems, which were evaluated on the IberSpeech-RTVE 2020 Speech-to-Text Transcription Challenge. Deep Neural Networks (DNNs) are becoming the most promising technology for ASR at present. In the last few years, traditional hybrid models have been evaluated and compared to other end-to-end ASR systems in terms of accuracy and efficiency. We contribute two different approaches: a hybrid ASR system based on a DNN-HMM and two state-of-the-art end-to-end ASR systems, based on Lattice-Free Maximum Mutual Information (LF-MMI). To address the high difficulty in the speech-to-text transcription of recordings with different speaking styles and acoustic conditions from TV studios to live recordings, data augmentation and Domain Adversarial Training (DAT) techniques were studied. Multi-condition data augmentation applied to our hybrid DNN-HMM demonstrated WER improvements in noisy scenarios (about 10% relatively). In contrast, the results obtained using an end-to-end PyChain-based ASR system were far from our expectations. Nevertheless, we found that when including DAT techniques, a relative WER improvement of 2.87% was obtained as compared to the PyChain-based system.

</details>

### [Recent Progress in the CUHK Dysarthric Speech Recognition System](2201.05845.md)
**Shansong Liu, Mengzhe Geng, Shoukang Hu, Xurong Xie et al.** · 2022-01-15

<details>
<summary>Abstract</summary>

Despite the rapid progress of automatic speech recognition (ASR) technologies in the past few decades, recognition of disordered speech remains a highly challenging task to date. Disordered speech presents a wide spectrum of challenges to current data intensive deep neural networks (DNNs) based ASR technologies that predominantly target normal speech. This paper presents recent research efforts at the Chinese University of Hong Kong (CUHK) to improve the performance of disordered speech recognition systems on the largest publicly available UASpeech dysarthric speech corpus. A set of novel modelling techniques including neural architectural search, data augmentation using spectra-temporal perturbation, model based speaker adaptation and cross-domain generation of visual features within an audio-visual speech recognition (AVSR) system framework were employed to address the above challenges. The combination of these techniques produced the lowest published word error rate (WER) of 25.21% on the UASpeech test set 16 dysarthric speakers, and an overall WER reduction of 5.4% absolute (17.6% relative) over the CUHK 2018 dysarthric speech recognition system featuring a 6-way DNN system combination and cross adaptation of out-of-domain normal speech data trained systems. Bayesian model adaptation further allows rapid adaptation to individual dysarthric speakers to be performed using as little as 3.06 seconds of speech. The efficacy of these techniques were further demonstrated on a CUDYS Cantonese dysarthric speech recognition task.

</details>

### [Spectro-Temporal Deep Features for Disordered Speech Assessment and Recognition](2201.05554.md)
**Mengzhe Geng, Shansong Liu, Jianwei Yu, Xurong Xie et al.** · 2022-01-14

<details>
<summary>Abstract</summary>

Automatic recognition of disordered speech remains a highly challenging task to date. Sources of variability commonly found in normal speech including accent, age or gender, when further compounded with the underlying causes of speech impairment and varying severity levels, create large diversity among speakers. To this end, speaker adaptation techniques play a vital role in current speech recognition systems. Motivated by the spectro-temporal level differences between disordered and normal speech that systematically manifest in articulatory imprecision, decreased volume and clarity, slower speaking rates and increased dysfluencies, novel spectro-temporal subspace basis embedding deep features derived by SVD decomposition of speech spectrum are proposed to facilitate both accurate speech intelligibility assessment and auxiliary feature based speaker adaptation of state-of-the-art hybrid DNN and end-to-end disordered speech recognition systems. Experiments conducted on the UASpeech corpus suggest the proposed spectro-temporal deep feature adapted systems consistently outperformed baseline i-Vector adaptation by up to 2.63% absolute (8.6% relative) reduction in word error rate (WER) with or without data augmentation. Learning hidden unit contribution (LHUC) based speaker adaptation was further applied. The final speaker adapted system using the proposed spectral basis embedding features gave an overall WER of 25.6% on the UASpeech test set of 16 dysarthric speakers

</details>

### [A Study of Transducer based End-to-End ASR with ESPnet: Architecture, Auxiliary Loss and Decoding Strategies](2201.05420.md)
**Florian Boyer, Yusuke Shinohara, Takaaki Ishii, Hirofumi Inaguma et al.** · 2022-01-14

<details>
<summary>Abstract</summary>

In this study, we present recent developments of models trained with the RNN-T loss in ESPnet. It involves the use of various architectures such as recently proposed Conformer, multi-task learning with different auxiliary criteria and multiple decoding strategies, including our own proposition. Through experiments and benchmarks, we show that our proposed systems can be competitive against other state-of-art systems on well-known datasets such as LibriSpeech and AISHELL-1. Additionally, we demonstrate that these models are promising against other already implemented systems in ESPnet in regards to both performance and decoding speed, enabling the possibility to have powerful systems for a streaming task. With these additions, we hope to expand the usefulness of the ESPnet toolkit for the research community and also give tools for the ASR industry to deploy our systems in realistic and production environments.

</details>

### [MLLP-VRAIN Spanish ASR Systems for the Albayzín-RTVE 2020 Speech-to-Text Challenge: Extension](s2:77c4378c31b60a37f3501226dc147cc416a894ff.md)
**Pau Baquero-Arnal, Javier Jorge, Adrià Giménez, Javier Iranzo-Sánchez et al.** · 2022-01-13

<details>
<summary>Abstract</summary>

This paper describes the automatic speech recognition (ASR) systems built by the MLLP-VRAIN research group of Universitat Politècnica de València for the Albayzín-RTVE 2020 Speech-to-Text Challenge, and includes an extension of the work consisting of building and evaluating equivalent systems under the closed data conditions from the 2018 challenge. The primary system (p-streaming_1500ms_nlt) was a hybrid ASR system using streaming one-pass decoding with a context window of 1.5 seconds. This system achieved 16.0% WER on the test-2020 set. We also submitted three contrastive systems. From these, we highlight the system c2-streaming_600ms_t which, following a similar configuration as the primary system with a smaller context window of 0.6 s, scored 16.9% WER points on the same test set, with a measured empirical latency of 0.81 ± 0.09 s (mean ± stdev). That is, we obtained state-of-the-art latencies for high-quality automatic live captioning with a small WER degradation of 6% relative. As an extension, the equivalent closed-condition systems obtained 23.3% WER and 23.5% WER, respectively. When evaluated with an unconstrained language model, we obtained 19.9% WER and 20.4% WER; i.e., not far behind the top-performing systems with only 5% of the full acoustic data and with the extra ability of being streaming-capable. Indeed, all of these streaming systems could be put into production environments for automatic captioning of live media streams.

</details>

### [Security for Machine Learning-based Software Systems: a survey of threats, practices and challenges](2201.04736.md)
**Huaming Chen, M. Ali Babar** · 2022-01-12

<details>
<summary>Abstract</summary>

The rapid development of Machine Learning (ML) has demonstrated superior performance in many areas, such as computer vision, video and speech recognition. It has now been increasingly leveraged in software systems to automate the core tasks. However, how to securely develop the machine learning-based modern software systems (MLBSS) remains a big challenge, for which the insufficient consideration will largely limit its application in safety-critical domains. One concern is that the present MLBSS development tends to be rush, and the latent vulnerabilities and privacy issues exposed to external users and attackers will be largely neglected and hard to be identified. Additionally, machine learning-based software systems exhibit different liabilities towards novel vulnerabilities at different development stages from requirement analysis to system maintenance, due to its inherent limitations from the model and data and the external adversary capabilities. The successful generation of such intelligent systems will thus solicit dedicated efforts jointly from different research areas, i.e., software engineering, system security and machine learning. Most of the recent works regarding the security issues for ML have a strong focus on the data and models, which has brought adversarial attacks into consideration. In this work, we consider that security for machine learning-based software systems may arise from inherent system defects or external adversarial attacks, and the secure development practices should be taken throughout the whole lifecycle. While machine learning has become a new threat domain for existing software engineering practices, there is no such review work covering the topic. Overall, we present a holistic review regarding the security for MLBSS, which covers a systematic understanding from a structure review of three distinct aspects in terms of security threats...

</details>

### [Learning to Enhance or Not: Neural Network-Based Switching of Enhanced and Observed Signals for Overlapping Speech Recognition](2201.03881.md)
**Hiroshi Sato, Tsubasa Ochiai, Marc Delcroix, Keisuke Kinoshita et al.** · 2022-01-11

<details>
<summary>Abstract</summary>

The combination of a deep neural network (DNN) -based speech enhancement (SE) front-end and an automatic speech recognition (ASR) back-end is a widely used approach to implement overlapping speech recognition. However, the SE front-end generates processing artifacts that can degrade the ASR performance. We previously found that such performance degradation can occur even under fully overlapping conditions, depending on the signal-to-interference ratio (SIR) and signal-to-noise ratio (SNR). To mitigate the degradation, we introduced a rule-based method to switch the ASR input between the enhanced and observed signals, which showed promising results. However, the rule's optimality was unclear because it was heuristically designed and based only on SIR and SNR values. In this work, we propose a DNN-based switching method that directly estimates whether ASR will perform better on the enhanced or observed signals. We also introduce soft-switching that computes a weighted sum of the enhanced and observed signals for ASR input, with weights given by the switching model's output posteriors. The proposed learning-based switching showed performance comparable to that of rule-based oracle switching. The soft-switching further improved the ASR performance and achieved a relative character error rate reduction of up to 23 % as compared with the conventional method.

</details>

### [Deep Learning-Aided 6G Wireless Networks: A Comprehensive Survey of Revolutionary PHY Architectures](2201.03866.md)
**Burak Ozpoyraz, A. Tugberk Dogukan, Yarkin Gevez, Ufuk Altun et al.** · 2022-01-11

<details>
<summary>Abstract</summary>

Deep learning (DL) has proven its unprecedented success in diverse fields such as computer vision, natural language processing, and speech recognition by its strong representation ability and ease of computation. As we move forward to a thoroughly intelligent society with 6G wireless networks, new applications and use-cases have been emerging with stringent requirements for next-generation wireless communications. Therefore, recent studies have focused on the potential of DL approaches in satisfying these rigorous needs and overcoming the deficiencies of existing model-based techniques. The main objective of this article is to unveil the state-of-the-art advancements in the field of DL-based physical layer (PHY) methods to pave the way for fascinating applications of 6G. In particular, we have focused our attention on four promising PHY concepts foreseen to dominate next-generation communications, namely massive multiple-input multiple-output (MIMO) systems, sophisticated multi-carrier (MC) waveform designs, reconfigurable intelligent surface (RIS)-empowered communications, and PHY security. We examine up-to-date developments in DL-based techniques, provide comparisons with state-of-the-art methods, and introduce a comprehensive guide for future directions. We also present an overview of the underlying concepts of DL, along with the theoretical background of well-known DL techniques. Furthermore, this article provides programming examples for a number of DL techniques and the implementation of a DL-based MIMO by sharing user-friendly code snippets, which might be useful for interested readers.

</details>

### [CI-AVSR: A Cantonese Audio-Visual Speech Dataset for In-car Command Recognition](2201.03804.md)
**Wenliang Dai, Samuel Cahyawijaya, Tiezheng Yu, Elham J. Barezi et al.** · 2022-01-11

<details>
<summary>Abstract</summary>

With the rise of deep learning and intelligent vehicle, the smart assistant has become an essential in-car component to facilitate driving and provide extra functionalities. In-car smart assistants should be able to process general as well as car-related commands and perform corresponding actions, which eases driving and improves safety. However, there is a data scarcity issue for low resource languages, hindering the development of research and applications. In this paper, we introduce a new dataset, Cantonese In-car Audio-Visual Speech Recognition (CI-AVSR), for in-car command recognition in the Cantonese language with both video and audio data. It consists of 4,984 samples (8.3 hours) of 200 in-car commands recorded by 30 native Cantonese speakers. Furthermore, we augment our dataset using common in-car background noises to simulate real environments, producing a dataset 10 times larger than the collected one. We provide detailed statistics of both the clean and the augmented versions of our dataset. Moreover, we implement two multimodal baselines to demonstrate the validity of CI-AVSR. Experiment results show that leveraging the visual signal improves the overall performance of the model. Although our best model can achieve a considerable quality on the clean test set, the speech recognition quality on the noisy data is still inferior and remains as an extremely challenging task for real in-car speech recognition systems. The dataset and code will be released at https://github.com/HLTCHKUST/CI-AVSR.

</details>

### [A Likelihood Ratio based Domain Adaptation Method for E2E Models](2201.03655.md)
**Chhavi Choudhury, Ankur Gandhe, Xiaohan Ding, Ivan Bulyko** · 2022-01-10

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition models like Recurrent Neural Networks Transducer (RNN-T) are becoming a popular choice for streaming ASR applications like voice assistants. While E2E models are very effective at learning representation of the training data they are trained on, their accuracy on unseen domains remains a challenging problem. Additionally, these models require paired audio and text training data, are computationally expensive and are difficult to adapt towards the fast evolving nature of conversational speech. In this work, we explore a contextual biasing approach using likelihood-ratio that leverages text data sources to adapt RNN-T model to new domains and entities. We show that this method is effective in improving rare words recognition, and results in a relative improvement of 10% in 1-best word error rate (WER) and 10% in n-best Oracle WER (n=8) on multiple out-of-domain datasets without any degradation on a general dataset. We also show that complementing the contextual biasing adaptation with adaptation of a second-pass rescoring model gives additive WER improvements.

</details>

### [Neural Architecture Search For LF-MMI Trained Time Delay Neural Networks](2201.03943.md)
**Shoukang Hu, Xurong Xie, Mingyu Cui, Jiajun Deng et al.** · 2022-01-08

<details>
<summary>Abstract</summary>

State-of-the-art automatic speech recognition (ASR) system development is data and computation intensive. The optimal design of deep neural networks (DNNs) for these systems often require expert knowledge and empirical evaluation. In this paper, a range of neural architecture search (NAS) techniques are used to automatically learn two types of hyper-parameters of factored time delay neural networks (TDNN-Fs): i) the left and right splicing context offsets; and ii) the dimensionality of the bottleneck linear projection at each hidden layer. These techniques include the differentiable neural architecture search (DARTS) method integrating architecture learning with lattice-free MMI training; Gumbel-Softmax and pipelined DARTS methods reducing the confusion over candidate architectures and improving the generalization of architecture selection; and Penalized DARTS incorporating resource constraints to balance the trade-off between performance and system complexity. Parameter sharing among TDNN-F architectures allows an efficient search over up to 7^28 different systems. Statistically significant word error rate (WER) reductions of up to 1.2% absolute and relative model size reduction of 31% were obtained over a state-of-the-art 300-hour Switchboard corpus trained baseline LF-MMI TDNN-F system featuring speed perturbation, i-Vector and learning hidden unit contribution (LHUC) based speaker adaptation as well as RNNLM rescoring. Performance contrasts on the same task against recent end-to-end systems reported in the literature suggest the best NAS auto-configured system achieves state-of-the-art WERs of 9.9% and 11.1% on the NIST Hub5' 00 and Rt03s test sets respectively with up to 96% model size reduction. Further analysis using Bayesian learning shows that ...

</details>

### [Two-Pass End-to-End ASR Model Compression](2201.02741.md)
**Nauman Dawalatabad, Tushar Vatsal, Ashutosh Gupta, Sungsoo Kim et al.** · 2022-01-08

<details>
<summary>Abstract</summary>

Speech recognition on smart devices is challenging owing to the small memory footprint. Hence small size ASR models are desirable. With the use of popular transducer-based models, it has become possible to practically deploy streaming speech recognition models on small devices [1]. Recently, the two-pass model [2] combining RNN-T and LAS modules has shown exceptional performance for streaming on-device speech recognition. In this work, we propose a simple and effective approach to reduce the size of the two-pass model for memory-constrained devices. We employ a popular knowledge distillation approach in three stages using the Teacher-Student training technique. In the first stage, we use a trained RNN-T model as a teacher model and perform knowledge distillation to train the student RNN-T model. The second stage uses the shared encoder and trains a LAS rescorer for student model using the trained RNN-T+LAS teacher model. Finally, we perform deep-finetuning for the student model with a shared RNN-T encoder, RNN-T decoder, and LAS rescorer. Our experimental results on standard LibriSpeech dataset show that our system can achieve a high compression rate of 55% without significant degradation in the WER compared to the two-pass teacher model.

</details>

### [Textual Data Augmentation for Arabic-English Code-Switching Speech Recognition](2201.02550.md)
**Amir Hussein, Shammur Absar Chowdhury, Ahmed Abdelali, Najim Dehak et al.** · 2022-01-07

<details>
<summary>Abstract</summary>

The pervasiveness of intra-utterance code-switching (CS) in spoken content requires that speech recognition (ASR) systems handle mixed language. Designing a CS-ASR system has many challenges, mainly due to data scarcity, grammatical structure complexity, and domain mismatch. The most common method for addressing CS is to train an ASR system with the available transcribed CS speech, along with monolingual data. In this work, we propose a zero-shot learning methodology for CS-ASR by augmenting the monolingual data with artificially generating CS text. We based our approach on random lexical replacements and Equivalence Constraint (EC) while exploiting aligned translation pairs to generate random and grammatically valid CS content. Our empirical results show a 65.5% relative reduction in language model perplexity, and 7.7% in ASR WER on two ecologically valid CS test sets. The human evaluation of the generated text using EC suggests that more than 80% is of adequate quality.

</details>

### [Automatic Speech Recognition Datasets in Cantonese: A Survey and New Dataset](2201.02419.md)
**Tiezheng Yu, Rita Frieske, Peng Xu, Samuel Cahyawijaya et al.** · 2022-01-07

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) on low resource languages improves the access of linguistic minorities to technological advantages provided by artificial intelligence (AI). In this paper, we address the problem of data scarcity for the Hong Kong Cantonese language by creating a new Cantonese dataset. Our dataset, Multi-Domain Cantonese Corpus (MDCC), consists of 73.6 hours of clean read speech paired with transcripts, collected from Cantonese audiobooks from Hong Kong. It comprises philosophy, politics, education, culture, lifestyle and family domains, covering a wide range of topics. We also review all existing Cantonese datasets and analyze them according to their speech type, data source, total size and availability. We further conduct experiments with Fairseq S2T Transformer, a state-of-the-art ASR model, on the biggest existing dataset, Common Voice zh-HK, and our proposed MDCC, and the results show the effectiveness of our dataset. In addition, we create a powerful and robust Cantonese ASR model by applying multi-dataset learning on MDCC and Common Voice zh-HK.

</details>

### [Improving Mandarin End-to-End Speech Recognition with Word N-gram Language Model](2201.01995.md)
**Jinchuan Tian, Jianwei Yu, Chao Weng, Yuexian Zou et al.** · 2022-01-06

<details>
<summary>Abstract</summary>

Despite the rapid progress of end-to-end (E2E) automatic speech recognition (ASR), it has been shown that incorporating external language models (LMs) into the decoding can further improve the recognition performance of E2E ASR systems. To align with the modeling units adopted in E2E ASR systems, subword-level (e.g., characters, BPE) LMs are usually used to cooperate with current E2E ASR systems. However, the use of subword-level LMs will ignore the word-level information, which may limit the strength of the external LMs in E2E ASR. Although several methods have been proposed to incorporate word-level external LMs in E2E ASR, these methods are mainly designed for languages with clear word boundaries such as English and cannot be directly applied to languages like Mandarin, in which each character sequence can have multiple corresponding word sequences. To this end, we propose a novel decoding algorithm where a word-level lattice is constructed on-the-fly to consider all possible word sequences for each partial hypothesis. Then, the LM score of the hypothesis is obtained by intersecting the generated lattice with an external word N-gram LM. The proposed method is examined on both Attention-based Encoder-Decoder (AED) and Neural Transducer (NT) frameworks. Experiments suggest that our method consistently outperforms subword-level LMs, including N-gram LM and neural network LM. We achieve state-of-the-art results on both Aishell-1 (CER 4.18%) and Aishell-2 (CER 5.06%) datasets and reduce CER by 14.8% relatively on a 21K-hour Mandarin dataset.

</details>

### [Robust Self-Supervised Audio-Visual Speech Recognition](2201.01763.md)
**Bowen Shi, Wei-Ning Hsu, Abdelrahman Mohamed** · 2022-01-05

<details>
<summary>Abstract</summary>

Audio-based automatic speech recognition (ASR) degrades significantly in noisy environments and is particularly vulnerable to interfering speech, as the model cannot determine which speaker to transcribe. Audio-visual speech recognition (AVSR) systems improve robustness by complementing the audio stream with the visual information that is invariant to noise and helps the model focus on the desired speaker. However, previous AVSR work focused solely on the supervised learning setup; hence the progress was hindered by the amount of labeled data available. In this work, we present a self-supervised AVSR framework built upon Audio-Visual HuBERT (AV-HuBERT), a state-of-the-art audio-visual speech representation learning model. On the largest available AVSR benchmark dataset LRS3, our approach outperforms prior state-of-the-art by ~50% (28.0% vs. 14.1%) using less than 10% of labeled data (433hr vs. 30hr) in the presence of babble noise, while reducing the WER of an audio-based model by over 75% (25.8% vs. 5.8%) on average.

</details>

### [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](2201.02184.md)
**Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, Abdelrahman Mohamed** · 2022-01-05

<details>
<summary>Abstract</summary>

Video recordings of speech contain correlated audio and visual information, providing a strong signal for speech representation learning from the speaker's lip movements and the produced sound. We introduce Audio-Visual Hidden Unit BERT (AV-HuBERT), a self-supervised representation learning framework for audio-visual speech, which masks multi-stream video input and predicts automatically discovered and iteratively refined multimodal hidden units. AV-HuBERT learns powerful audio-visual speech representation benefiting both lip-reading and automatic speech recognition. On the largest public lip-reading benchmark LRS3 (433 hours), AV-HuBERT achieves 32.5% WER with only 30 hours of labeled data, outperforming the former state-of-the-art approach (33.6%) trained with a thousand times more transcribed video data (31K hours). The lip-reading WER is further reduced to 26.9% when using all 433 hours of labeled data from LRS3 and combined with self-training. Using our audio-visual representation on the same benchmark for audio-only speech recognition leads to a 40% relative WER reduction over the state-of-the-art performance (1.3% vs 2.3%). Our code and models are available at https://github.com/facebookresearch/av_hubert

</details>

### [A Discriminative Hierarchical PLDA-based Model for Spoken Language Recognition](2201.01364.md)
**Luciana Ferrer, Diego Castan, Mitchell McLaren, Aaron Lawson** · 2022-01-04

<details>
<summary>Abstract</summary>

Spoken language recognition (SLR) refers to the automatic process used to determine the language present in a speech sample. SLR is an important task in its own right, for example, as a tool to analyze or categorize large amounts of multi-lingual data. Further, it is also an essential tool for selecting downstream applications in a work flow, for example, to chose appropriate speech recognition or machine translation models. SLR systems are usually composed of two stages, one where an embedding representing the audio sample is extracted and a second one which computes the final scores for each language. In this work, we approach the SLR task as a detection problem and implement the second stage as a probabilistic linear discriminant analysis (PLDA) model. We show that discriminative training of the PLDA parameters gives large gains with respect to the usual generative training. Further, we propose a novel hierarchical approach where two PLDA models are trained, one to generate scores for clusters of highly-related languages and a second one to generate scores conditional to each cluster. The final language detection scores are computed as a combination of these two sets of scores. The complete model is trained discriminatively to optimize a cross-entropy objective. We show that this hierarchical approach consistently outperforms the non-hierarchical one for detection of highly related languages, in many cases by large margins. We train our systems on a collection of datasets including over 100 languages, and test them both on matched and mismatched conditions, showing that the gains are robust to condition mismatch.

</details>

### [Speech-to-SQL: Towards Speech-driven SQL Query Generation From Natural Language Question](2201.01209.md)
**Yuanfeng Song, Raymond Chi-Wing Wong, Xuefang Zhao, Di Jiang** · 2022-01-04

<details>
<summary>Abstract</summary>

Speech-based inputs have been gaining significant momentum with the popularity of smartphones and tablets in our daily lives, since voice is the most easiest and efficient way for human-computer interaction. This paper works towards designing more effective speech-based interfaces to query the structured data in relational databases. We first identify a new task named Speech-to-SQL, which aims to understand the information conveyed by human speech and directly translate it into structured query language (SQL) statements. A naive solution to this problem can work in a cascaded manner, that is, an automatic speech recognition (ASR) component followed by a text-to-SQL component. However, it requires a high-quality ASR system and also suffers from the error compounding problem between the two components, resulting in limited performance. To handle these challenges, we further propose a novel end-to-end neural architecture named SpeechSQLNet to directly translate human speech into SQL queries without an external ASR step. SpeechSQLNet has the advantage of making full use of the rich linguistic information presented in speech. To the best of our knowledge, this is the first attempt to directly synthesize SQL based on arbitrary natural language questions, rather than a natural language-based version of SQL or its variants with a limited SQL grammar. To validate the effectiveness of the proposed problem and model, we further construct a dataset named SpeechQL, by piggybacking the widely-used text-to-SQL datasets. Extensive experimental evaluations on this dataset show that SpeechSQLNet can directly synthesize high-quality SQL queries from human speech, outperforming various competitive counterparts as well as the cascaded methods in terms of exact match accuracies.

</details>

### [Robust Natural Language Processing: Recent Advances, Challenges, and Future Directions](2201.00768.md)
**Marwan Omar, Soohyeon Choi, DaeHun Nyang, David Mohaisen** · 2022-01-03

<details>
<summary>Abstract</summary>

Recent natural language processing (NLP) techniques have accomplished high performance on benchmark datasets, primarily due to the significant improvement in the performance of deep learning. The advances in the research community have led to great enhancements in state-of-the-art production systems for NLP tasks, such as virtual assistants, speech recognition, and sentiment analysis. However, such NLP systems still often fail when tested with adversarial attacks. The initial lack of robustness exposed troubling gaps in current models' language understanding capabilities, creating problems when NLP systems are deployed in real life. In this paper, we present a structured overview of NLP robustness research by summarizing the literature in a systemic way across various dimensions. We then take a deep-dive into the various dimensions of robustness, across techniques, metrics, embeddings, and benchmarks. Finally, we argue that robustness should be multi-dimensional, provide insights into current research, identify gaps in the literature to suggest directions worth pursuing to address these gaps.

</details>

### [Cleanformer: A microphone array configuration-invariant, streaming, multichannel neural enhancement frontend for ASR](s2:d00656a769ca9a6850e4f2917867866e95aaab9c.md)
**Joseph Peter Caroselli, A. Naranayan, Tom O'Malley** · 2022-01-01

### [Sequentially Sampled Chunk Conformer for Streaming End-to-End ASR](s2:8121134ac69484563d1ba3de50f5818bced34129.md)
**Fangyuan Wang, Xiyuan Wang, Bo Xu** · 2022-01-01

### [Live Streaming Speech Recognition Using Deep Bidirectional LSTM Acoustic Models and Interpolated Language Models](s2:f665c1961f53412ca84cdf1b8baa3b86cefd37ea.md)
**Javier Jorge, Adrià Giménez, J. Silvestre-Cerdà, Jorge Civera Saiz et al.** · 2022-01-01

<details>
<summary>Abstract</summary>

Although Long-Short Term Memory (LSTM) networks and deep Transformers are now extensively used in offline ASR, it is unclear how best offline systems can be adapted to work with them under the streaming setup. After gaining considerable experience on this regard in recent years, in this paper we show how an optimized, low-latency streaming decoder can be built in which bidirectional LSTM acoustic models, together with general interpolated language models, can be nicely integrated with minimal perfomance degradation. In brief, our streaming decoder consists of a one-pass, real-time search engine relying on a limited-duration window sliding over time and a number of ad hoc acoustic and language model pruning techniques. Extensive empirical assessment is provided on truly streaming tasks derived from the well-known LibriSpeech and TED talks datasets, as well as from TV shows on a main Spanish broadcasting station.

</details>

### [LAMASSU: Streaming Language-Agnostic Multilingual Speech Recognition and Translation Using Neural Transducers](s2:50b67709507cbaef315ce6c6085aa62c386d1f28.md)
**Peidong Wang, Eric Sun, Jian Xue, Yu Wu et al.** · 2022-01-01

