# 2024

644 papers in this year.

### [Fotheidil: an Automatic Transcription System for the Irish Language](2501.00509.md)
**Liam Lonergan, Ibon Saratxaga, John Sloan, Oscar Maharog et al.** · 2024-12-31

<details>
<summary>Abstract</summary>

This paper sets out the first web-based transcription system for the Irish language - Fotheidil, a system that utilises speech-related AI technologies as part of the ABAIR initiative. The system includes both off-the-shelf pre-trained voice activity detection and speaker diarisation models and models trained specifically for Irish automatic speech recognition and capitalisation and punctuation restoration. Semi-supervised learning is explored to improve the acoustic model of a modular TDNN-HMM ASR system, yielding substantial improvements for out-of-domain test sets and dialects that are underrepresented in the supervised training set. A novel approach to capitalisation and punctuation restoration involving sequence-to-sequence models is compared with the conventional approach using a classification model. Experimental results show here also substantial improvements in performance. The system will be made freely available for public use, and represents an important resource to researchers and others who transcribe Irish language materials. Human-corrected transcriptions will be collected and included in the training dataset as the system is used, which should lead to incremental improvements to the ASR model in a cyclical, community-driven fashion.

</details>

### [Whisper Turns Stronger: Augmenting Wav2Vec 2.0 for Superior ASR in Low-Resource Languages](2501.00425.md)
**Or Haim Anidjar, Revital Marbel, Roi Yozevitch** · 2024-12-31

<details>
<summary>Abstract</summary>

Approaching Speech-to-Text and Automatic Speech Recognition problems in low-resource languages is notoriously challenging due to the scarcity of validated datasets and the diversity of dialects. Arabic, Russian, and Portuguese exemplify these difficulties, being low-resource languages due to the many dialects of these languages across different continents worldwide. Moreover, the variety of accents and pronunciations of such languages complicate ASR models' success. With the increasing popularity of Deep Learning and Transformers, acoustic models like the renowned Wav2Vec2 have achieved superior performance in the Speech Recognition field compared to state-of-the-art approaches. However, despite Wav2Vec2's improved efficiency over traditional methods, its performance significantly declines for under-represented languages, even though it requires significantly less labeled data. This paper introduces an end-to-end framework that enhances ASR systems fine-tuned on Wav2Vec2 through data augmentation techniques. To validate our framework's effectiveness, we conducted a detailed experimental evaluation using three datasets from Mozilla's Common Voice project in Arabic, Russian, and Portuguese. Additionally, the framework presented in this paper demonstrates robustness to different diacritics. Ultimately, our approach outperforms two previous baseline models, which are the pre-trained Wav2Vec2 and the well-known Whisper ASR model, resulting in an average relative improvement of 33.9\% in Word Error Rate and a 53.2\% relative improvement in Character Error Rate.

</details>

### [Utilizing Multimodal Data for Edge Case Robust Call-sign Recognition and Understanding](2412.20467.md)
**Alexander Blatt, Dietrich Klakow** · 2024-12-29

<details>
<summary>Abstract</summary>

Operational machine-learning based assistant systems must be robust in a wide range of scenarios. This hold especially true for the air-traffic control (ATC) domain. The robustness of an architecture is particularly evident in edge cases, such as high word error rate (WER) transcripts resulting from noisy ATC recordings or partial transcripts due to clipped recordings. To increase the edge-case robustness of call-sign recognition and understanding (CRU), a core tasks in ATC speech processing, we propose the multimodal call-sign-command recovery model (CCR). The CCR architecture leads to an increase in the edge case performance of up to 15%. We demonstrate this on our second proposed architecture, CallSBERT. A CRU model that has less parameters, can be fine-tuned noticeably faster and is more robust during fine-tuning than the state of the art for CRU. Furthermore, we demonstrate that optimizing for edge cases leads to a significantly higher accuracy across a wide operational range.

</details>

### [Towards a Single ASR Model That Generalizes to Disordered Speech](2412.19315.md)
**Jimmy Tobin, Katrin Tomanek, Subhashini Venugopalan** · 2024-12-26

<details>
<summary>Abstract</summary>

This study investigates the impact of integrating a dataset of disordered speech recordings ($\sim$1,000 hours) into the fine-tuning of a near state-of-the-art ASR baseline system. Contrary to what one might expect, despite the data being less than 1% of the training data of the ASR system, we find a considerable improvement in disordered speech recognition accuracy. Specifically, we observe a 33% improvement on prompted speech, and a 26% improvement on a newly gathered spontaneous, conversational dataset of disordered speech. Importantly, there is no significant performance decline on standard speech recognition benchmarks. Further, we observe that the proposed tuning strategy helps close the gap between the baseline system and personalized models by 64% highlighting the significant progress as well as the room for improvement. Given the substantial benefits of our findings, this experiment suggests that from a fairness perspective, incorporating a small fraction of high quality disordered speech data in a training recipe is an easy step that could be done to make speech technology more accessible for users with speech disabilities.

</details>

### [Structured Speaker-Deficiency Adaptation of Foundation Models for Dysarthric and Elderly Speech Recognition](2412.18832.md)
**Shujie Hu, Xurong Xie, Mengzhe Geng, Jiajun Deng et al.** · 2024-12-25

<details>
<summary>Abstract</summary>

Data-intensive fine-tuning of speech foundation models (SFMs) to scarce and diverse dysarthric and elderly speech leads to data bias and poor generalization to unseen speakers. This paper proposes novel structured speaker-deficiency adaptation approaches for SSL pre-trained SFMs on such data. Speaker and speech deficiency invariant SFMs were constructed in their supervised adaptive fine-tuning stage to reduce undue bias to training data speakers, and serves as a more neutral and robust starting point for test time unsupervised adaptation. Speech variability attributed to speaker identity and speech impairment severity, or aging induced neurocognitive decline, are modelled using separate adapters that can be combined together to model any seen or unseen speaker. Experiments on the UASpeech dysarthric and DementiaBank Pitt elderly speech corpora suggest structured speaker-deficiency adaptation of HuBERT and Wav2vec2-conformer models consistently outperforms baseline SFMs using either: a) no adapters; b) global adapters shared among all speakers; or c) single attribute adapters modelling speaker or deficiency labels alone by statistically significant WER reductions up to 3.01% and 1.50% absolute (10.86% and 6.94% relative) on the two tasks respectively. The lowest published WER of 19.45% (49.34% on very low intelligibility, 33.17% on unseen words) is obtained on the UASpeech test set of 16 dysarthric speakers.

</details>

### [Speech Recognition With LLMs Adapted to Disordered Speech Using Reinforcement Learning](2501.00039.md)
**Chirag Nagpal, Subhashini Venugopalan, Jimmy Tobin, Marilyn Ladewig et al.** · 2024-12-25

<details>
<summary>Abstract</summary>

We introduce a large language model (LLM) capable of processing speech inputs and show that tuning it further with reinforcement learning on human preference (RLHF) enables it to adapt better to disordered speech than traditional fine-tuning. Our method replaces low-frequency text tokens in an LLM's vocabulary with audio tokens and enables the model to recognize speech by fine-tuning it on speech with transcripts. We then use RL with rewards based on syntactic and semantic accuracy measures generalizing the LLM further to recognize disordered speech. While the resulting LLM does not outperform existing systems for speech recognition, we find that tuning with reinforcement learning using custom rewards leads to substantially better performance than supervised fine-tuning of the language model, specifically when adapting to speech in a different setting. This presents a compelling alternative tuning strategy for speech recognition using large language models.

</details>

### [MRI2Speech: Speech Synthesis from Articulatory Movements Recorded by Real-time MRI](2412.18836.md)
**Neil Shah, Ayan Kashyap, Shirish Karande, Vineet Gandhi** · 2024-12-25

<details>
<summary>Abstract</summary>

Previous real-time MRI (rtMRI)-based speech synthesis models depend heavily on noisy ground-truth speech. Applying loss directly over ground truth mel-spectrograms entangles speech content with MRI noise, resulting in poor intelligibility. We introduce a novel approach that adapts the multi-modal self-supervised AV-HuBERT model for text prediction from rtMRI and incorporates a new flow-based duration predictor for speaker-specific alignment. The predicted text and durations are then used by a speech decoder to synthesize aligned speech in any novel voice. We conduct thorough experiments on two datasets and demonstrate our method's generalization ability to unseen speakers. We assess our framework's performance by masking parts of the rtMRI video to evaluate the impact of different articulators on text prediction. Our method achieves a $15.18\%$ Word Error Rate (WER) on the USC-TIMIT MRI corpus, marking a huge improvement over the current state-of-the-art. Speech samples are available at https://mri2speech.github.io/MRI2Speech/

</details>

### [Zero-resource Speech Translation and Recognition with LLMs](2412.18566.md)
**Karel Mundnich, Xing Niu, Prashant Mathur, Srikanth Ronanki et al.** · 2024-12-24

<details>
<summary>Abstract</summary>

Despite recent advancements in speech processing, zero-resource speech translation (ST) and automatic speech recognition (ASR) remain challenging problems. In this work, we propose to leverage a multilingual Large Language Model (LLM) to perform ST and ASR in languages for which the model has never seen paired audio-text data. We achieve this by using a pre-trained multilingual speech encoder, a multilingual LLM, and a lightweight adaptation module that maps the audio representations to the token embedding space of the LLM. We perform several experiments both in ST and ASR to understand how to best train the model and what data has the most impact on performance in previously unseen languages. In ST, our best model is capable to achieve BLEU scores over 23 in CoVoST2 for two previously unseen languages, while in ASR, we achieve WERs of up to 28.2\%. We finally show that the performance of our system is bounded by the ability of the LLM to output text in the desired language.

</details>

### [Trading Devil RL: Backdoor attack via Stock market, Bayesian Optimization and Reinforcement Learning](2412.17908.md)
**Orson Mengara** · 2024-12-23

<details>
<summary>Abstract</summary>

With the rapid development of generative artificial intelligence, particularly large language models a number of sub-fields of deep learning have made significant progress and are now very useful in everyday applications. For example,financial institutions simulate a wide range of scenarios for various models created by their research teams using reinforcement learning, both before production and after regular operations. In this work, we propose a backdoor attack that focuses solely on data poisoning and a method of detection by dynamic systems and statistical analysis of the distribution of data. This particular backdoor attack is classified as an attack without prior consideration or trigger, and we name it FinanceLLMsBackRL. Our aim is to examine the potential effects of large language models that use reinforcement learning systems for text production or speech recognition, finance, physics, or the ecosystem of contemporary artificial intelligence models.

</details>

### [Deep Learning in Proteomics Informatics: Applications, Challenges, and Future Directions](2412.17349.md)
**Yindan Luo, Jiaxin Cai** · 2024-12-23

<details>
<summary>Abstract</summary>

Deep learning is an advanced technology that relies on large-scale data and complex models for feature extraction and pattern recognition. It has been widely applied across various fields, including computer vision, natural language processing, and speech recognition. In recent years, deep learning has demonstrated significant potential in the realm of proteomics informatics, particularly in deciphering complex biological information. The introduction of this technology not only accelerates the processing speed of protein data but also enhances the accuracy of predictions regarding protein structure and function. This provides robust support for both fundamental biology research and applied biotechnological studies. Currently, deep learning is primarily focused on applications such as protein sequence analysis, three-dimensional structure prediction, functional annotation, and the construction of protein interaction networks. These applications offer numerous advantages to proteomic research. Despite its growing prevalence in this field, deep learning faces several challenges including data scarcity, insufficient model interpretability, and computational complexity; these factors hinder its further advancement within proteomics. This paper comprehensively reviews the applications of deep learning in proteomics along with the challenges it encounters. The aim is to provide a systematic theoretical discussion and practical basis for research in this domain to facilitate ongoing development and innovation of deep learning technologies within proteomics.

</details>

### [Adapting Whisper for Code-Switching through Encoding Refining and Language-Aware Decoding](2412.16507.md)
**Jiahui Zhao, Hao Shi, Chenrui Cui, Tianrui Wang et al.** · 2024-12-21

<details>
<summary>Abstract</summary>

Code-switching (CS) automatic speech recognition (ASR) faces challenges due to the language confusion resulting from accents, auditory similarity, and seamless language switches. Adaptation on the pre-trained multi-lingual model has shown promising performance for CS-ASR. In this paper, we adapt Whisper, which is a large-scale multilingual pre-trained speech recognition model, to CS from both encoder and decoder parts. First, we propose an encoder refiner to enhance the encoder's capacity of intra-sentence swithching. Second, we propose using two sets of language-aware adapters with different language prompt embeddings to achieve language-specific decoding information in each decoder layer. Then, a fusion module is added to fuse the language-aware decoding. The experimental results using the SEAME dataset show that, compared with the baseline model, the proposed approach achieves a relative MER reduction of 4.1% and 7.2% on the dev_man and dev_sge test sets, respectively, surpassing state-of-the-art methods. Through experiments, we found that the proposed method significantly improves the performance on non-native language in CS speech, indicating that our approach enables Whisper to better distinguish between the two languages.

</details>

### [Speech Retrieval-Augmented Generation without Automatic Speech Recognition](2412.16500.md)
**Do June Min, Karel Mundnich, Andy Lapastora, Erfan Soltanmohammadi et al.** · 2024-12-21

<details>
<summary>Abstract</summary>

One common approach for question answering over speech data is to first transcribe speech using automatic speech recognition (ASR) and then employ text-based retrieval-augmented generation (RAG) on the transcriptions. While this cascaded pipeline has proven effective in many practical settings, ASR errors can propagate to the retrieval and generation steps. To overcome this limitation, we introduce SpeechRAG, a novel framework designed for open-question answering over spoken data. Our proposed approach fine-tunes a pre-trained speech encoder into a speech adapter fed into a frozen large language model (LLM)--based retrieval model. By aligning the embedding spaces of text and speech, our speech retriever directly retrieves audio passages from text-based queries, leveraging the retrieval capacity of the frozen text retriever. Our retrieval experiments on spoken question answering datasets show that direct speech retrieval does not degrade over the text-based baseline, and outperforms the cascaded systems using ASR. For generation, we use a speech language model (SLM) as a generator, conditioned on audio passages rather than transcripts. Without fine-tuning of the SLM, this approach outperforms cascaded text-based models when there is high WER in the transcripts.

</details>

### [Enhancing Multilingual ASR for Unseen Languages via Language Embedding Modeling](2412.16474.md)
**Shao-Syuan Huang, Kuan-Po Huang, Andy T. Liu, Hung-yi Lee** · 2024-12-21

<details>
<summary>Abstract</summary>

Multilingual Automatic Speech Recognition (ASR) aims to recognize and transcribe speech from multiple languages within a single system. Whisper, one of the most advanced ASR models, excels in this domain by handling 99 languages effectively, leveraging a vast amount of data and incorporating language tags as prefixes to guide the recognition process. However, despite its success, Whisper struggles with unseen languages, those not included in its pre-training. Motivated by the observation that many languages share linguistic characteristics, we propose methods that exploit these relationships to enhance ASR performance on unseen languages. Specifically, we introduce a weighted sum method, which computes a weighted sum of the embeddings of language tags, using Whisper's predicted language probabilities. In addition, we develop a predictor-based approach that refines the weighted sum embedding to more closely approximate the true embedding for unseen languages. Experimental results demonstrate substantial improvements in ASR performance, both in zero-shot and fine-tuning settings. Our proposed methods outperform baseline approaches, providing an effective solution for addressing unseen languages in multilingual ASR.

</details>

### [Fine-tuning Whisper on Low-Resource Languages for Real-World Applications](2412.15726.md)
**Vincenzo Timmel, Claudio Paonessa, Reza Kakooee, Manfred Vogel et al.** · 2024-12-20

<details>
<summary>Abstract</summary>

This paper presents a new approach to fine-tuning OpenAI's Whisper model for low-resource languages by introducing a novel data generation method that converts sentence-level data into a long-form corpus, using Swiss German as a case study. Non-sentence-level data, which could improve the performance of long-form audio, is difficult to obtain and often restricted by copyright laws. Our method bridges this gap by transforming more accessible sentence-level data into a format that preserves the model's ability to handle long-form audio and perform segmentation without requiring non-sentence-level data. Our data generation process improves performance in several real-world applications and leads to the development of a new state-of-the-art speech-to-text (STT) model for Swiss German. We compare our model with a non-fine-tuned Whisper and our previous state-of-the-art Swiss German STT models, where our new model achieves higher BLEU scores. Our results also indicate that the proposed method is adaptable to other low-resource languages, supported by written guidance and code that allows the creation of fine-tuned Whisper models, which keep segmentation capabilities and allow the transcription of longer audio files using only sentence-level data with high quality.

</details>

### [Transcribing and Translating, Fast and Slow: Joint Speech Translation and Recognition](2412.15415.md)
**Niko Moritz, Ruiming Xie, Yashesh Gaur, Ke Li et al.** · 2024-12-19

<details>
<summary>Abstract</summary>

We propose the joint speech translation and recognition (JSTAR) model that leverages the fast-slow cascaded encoder architecture for simultaneous end-to-end automatic speech recognition (ASR) and speech translation (ST). The model is transducer-based and uses a multi-objective training strategy that optimizes both ASR and ST objectives simultaneously. This allows JSTAR to produce high-quality streaming ASR and ST results. We apply JSTAR in a bilingual conversational speech setting with smart-glasses, where the model is also trained to distinguish speech from different directions corresponding to the wearer and a conversational partner. Different model pre-training strategies are studied to further improve results, including training of a transducer-based streaming machine translation (MT) model for the first time and applying it for parameter initialization of JSTAR. We demonstrate superior performances of JSTAR compared to a strong cascaded ST model in both BLEU scores and latency.

</details>

### [CAMEL: Cross-Attention Enhanced Mixture-of-Experts and Language Bias for Code-Switching Speech Recognition](2412.12760.md)
**He Wang, Xucheng Wan, Naijun Zheng, Kai Liu et al.** · 2024-12-17

<details>
<summary>Abstract</summary>

Code-switching automatic speech recognition (ASR) aims to transcribe speech that contains two or more languages accurately. To better capture language-specific speech representations and address language confusion in code-switching ASR, the mixture-of-experts (MoE) architecture and an additional language diarization (LD) decoder are commonly employed. However, most researches remain stagnant in simple operations like weighted summation or concatenation to fuse languagespecific speech representations, leaving significant opportunities to explore the enhancement of integrating language bias information. In this paper, we introduce CAMEL, a cross-attention-based MoE and language bias approach for code-switching ASR. Specifically, after each MoE layer, we fuse language-specific speech representations with cross-attention, leveraging its strong contextual modeling abilities. Additionally, we design a source attention-based mechanism to incorporate the language information from the LD decoder output into text embeddings. Experimental results demonstrate that our approach achieves state-of-the-art performance on the SEAME, ASRU200, and ASRU700+LibriSpeech460 Mandarin-English code-switching ASR datasets.

</details>

### [CLASP: Contrastive Language-Speech Pretraining for Multilingual Multimodal Information Retrieval](2412.13071.md)
**Mohammad Mahdi Abootorabi, Ehsaneddin Asgari** · 2024-12-17

<details>
<summary>Abstract</summary>

This study introduces CLASP (Contrastive Language-Speech Pretraining), a multilingual, multimodal representation tailored for audio-text information retrieval. CLASP leverages the synergy between spoken content and textual data. During training, we utilize our newly introduced speech-text dataset, which encompasses 15 diverse categories ranging from fiction to religion. CLASP's audio component integrates audio spectrograms with a pre-trained self-supervised speech model, while its language encoding counterpart employs a sentence encoder pre-trained on over 100 languages. This unified lightweight model bridges the gap between various modalities and languages, enhancing its effectiveness in handling and retrieving multilingual and multimodal data. Our evaluations across multiple languages demonstrate that CLASP establishes new benchmarks in HITS@1, MRR, and meanR metrics, outperforming traditional ASR-based retrieval methods that rely on transcribing speech into text for subsequent text retrieval, especially in specific scenarios.

</details>

### [Deep Speech Synthesis from Multimodal Articulatory Representations](2412.13387.md)
**Peter Wu, Bohan Yu, Kevin Scheck, Alan W Black et al.** · 2024-12-17

<details>
<summary>Abstract</summary>

The amount of articulatory data available for training deep learning models is much less compared to acoustic speech data. In order to improve articulatory-to-acoustic synthesis performance in these low-resource settings, we propose a multimodal pre-training framework. On single-speaker speech synthesis tasks from real-time magnetic resonance imaging and surface electromyography inputs, the intelligibility of synthesized outputs improves noticeably. For example, compared to prior work, utilizing our proposed transfer learning methods improves the MRI-to-speech performance by 36% word error rate. In addition to these intelligibility results, our multimodal pre-trained models consistently outperform unimodal baselines on three objective and subjective synthesis quality metrics.

</details>

### [MERaLiON-SpeechEncoder: Towards a Speech Foundation Model for Singapore and Beyond](2412.11538.md)
**Muhammad Huzaifah, Geyu Lin, Tianchi Liu, Hardik B. Sailor et al.** · 2024-12-16

<details>
<summary>Abstract</summary>

This technical report describes the MERaLiON-SpeechEncoder, a foundation model designed to support a wide range of downstream speech applications. Developed as part of Singapore's National Multimodal Large Language Model Programme, the MERaLiON-SpeechEncoder is tailored to address the speech processing needs in Singapore and the surrounding Southeast Asian region. The model currently supports mainly English, including the variety spoken in Singapore. We are actively expanding our datasets to gradually cover other languages in subsequent releases. The MERaLiON-SpeechEncoder was pre-trained from scratch on 200,000 hours of unlabelled speech data using a self-supervised learning approach based on masked language modelling. We describe our training procedure and hyperparameter tuning experiments in detail below. Our evaluation demonstrates improvements to spontaneous and Singapore speech benchmarks for speech recognition, while remaining competitive to other state-of-the-art speech encoders across ten other speech tasks. We commit to releasing our model, supporting broader research endeavours, both in Singapore and beyond.

</details>

### [Transliterated Zero-Shot Domain Adaptation for Automatic Speech Recognition](2412.11185.md)
**Han Zhu, Gaofeng Cheng, Qingwei Zhao, Pengyuan Zhang** · 2024-12-15

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition models often degenerates on domains not covered by the training data. Domain adaptation can address this issue, assuming the availability of the target domain data in the target language. However, such assumption does not stand in many real-world applications. To make domain adaptation more applicable, we address the problem of zero-shot domain adaptation (ZSDA), where target domain data is unavailable in the target language. Instead, we transfer the target domain knowledge from another source language where the target domain data is more accessible. To do that, we first perform cross-lingual pre-training (XLPT) to share domain knowledge across languages, then use target language fine-tuning to build the final model. One challenge in this practice is that the pre-trained knowledge can be forgotten during fine-tuning, resulting in sub-optimal adaptation performance. To address this issue, we propose transliterated ZSDA to achieve consistent pre-training and fine-tuning labels, leading to maximum preservation of the pre-trained knowledge. Experimental results show that transliterated ZSDA relatively decreases the word error rate by 9.2% compared with a wav2vec 2.0 baseline. Moreover, transliterated ZSDA consistently outperforms self-supervised ZSDA and performs on par with supervised ZSDA, proving the superiority of transliteration-based pre-training labels.

</details>

### [Robust Persian Digit Recognition in Noisy Environments Using Hybrid CNN-BiGRU Model](2412.10857.md)
**Ali Nasr-Esfahani, Mehdi Bekrani, Roozbeh Rajabi** · 2024-12-14

<details>
<summary>Abstract</summary>

Artificial intelligence (AI) has significantly advanced speech recognition applications. However, many existing neural network-based methods struggle with noise, reducing accuracy in real-world environments. This study addresses isolated spoken Persian digit recognition (zero to nine) under noisy conditions, particularly for phonetically similar numbers. A hybrid model combining residual convolutional neural networks and bidirectional gated recurrent units (BiGRU) is proposed, utilizing word units instead of phoneme units for speaker-independent recognition. The FARSDIGIT1 dataset, augmented with various approaches, is processed using Mel-Frequency Cepstral Coefficients (MFCC) for feature extraction. Experimental results demonstrate the model's effectiveness, achieving 98.53%, 96.10%, and 95.92% accuracy on training, validation, and test sets, respectively. In noisy conditions, the proposed approach improves recognition by 26.88% over phoneme unit-based LSTM models and surpasses the Mel-scale Two Dimension Root Cepstrum Coefficients (MTDRCC) feature extraction technique along with MLP model (MTDRCC+MLP) by 7.61%.

</details>

### [Efficient Adaptation of Multilingual Models for Japanese ASR](2412.10705.md)
**Mark Bajo, Haruka Fukukawa, Ryuji Morita, Yuma Ogasawara** · 2024-12-14

<details>
<summary>Abstract</summary>

This study explores fine-tuning multilingual ASR (Automatic Speech Recognition) models, specifically OpenAI's Whisper-Tiny, to improve performance in Japanese. While multilingual models like Whisper offer versatility, they often lack precision in specific languages. Conversely, monolingual models like ReazonSpeech excel in language-specific tasks but are less adaptable. Using Japanese-specific datasets and Low-Rank Adaptation (LoRA) along with end-to-end (E2E) training, we fine-tuned Whisper-Tiny to bridge this gap. Our results show that fine-tuning reduced Whisper-Tiny's Character Error Rate (CER) from 32.7 to 20.8 with LoRA and to 14.7 with end-to-end fine-tuning, surpassing Whisper-Base's CER of 20.2. However, challenges with domain-specific terms remain, highlighting the need for specialized datasets. These findings demonstrate that fine-tuning multilingual models can achieve strong language-specific performance while retaining their flexibility. This approach provides a scalable solution for improving ASR in resource-constrained environments and languages with complex writing systems like Japanese.

</details>

### [MERaLiON-AudioLLM: Bridging Audio and Language with Large Language Models](2412.09818.md)
**Yingxu He, Zhuohan Liu, Shuo Sun, Bin Wang et al.** · 2024-12-13

<details>
<summary>Abstract</summary>

We introduce MERaLiON-AudioLLM (Multimodal Empathetic Reasoning and Learning in One Network), the first speech-text model tailored for Singapore's multilingual and multicultural landscape. Developed under the National Large Language Models Funding Initiative, Singapore, MERaLiON-AudioLLM integrates advanced speech and text processing to address the diverse linguistic nuances of local accents and dialects, enhancing accessibility and usability in complex, multilingual environments. Our results demonstrate improvements in both speech recognition and task-specific understanding, positioning MERaLiON-AudioLLM as a pioneering solution for region specific AI applications. We envision this release to set a precedent for future models designed to address localised linguistic and cultural contexts in a global framework.

</details>

### [Greek2MathTex: A Greek Speech-to-Text Framework for LaTeX Equations Generation](2412.12167.md)
**Evangelia Gkritzali, Panagiotis Kaliosis, Sofia Galanaki, Elisavet Palogiannidi et al.** · 2024-12-11

<details>
<summary>Abstract</summary>

In the vast majority of the academic and scientific domains, LaTeX has established itself as the de facto standard for typesetting complex mathematical equations and formulae. However, LaTeX's complex syntax and code-like appearance present accessibility barriers for individuals with disabilities, as well as those unfamiliar with coding conventions. In this paper, we present a novel solution to this challenge through the development of a novel speech-to-LaTeX equations system specifically designed for the Greek language. We propose an end-to-end system that harnesses the power of Automatic Speech Recognition (ASR) and Natural Language Processing (NLP) techniques to enable users to verbally dictate mathematical expressions and equations in natural language, which are subsequently converted into LaTeX format. We present the architecture and design principles of our system, highlighting key components such as the ASR engine, the LLM-based prompt-driven equations generation mechanism, as well as the application of a custom evaluation metric employed throughout the development process. We have made our system open source and available at https://github.com/magcil/greek-speech-to-math.

</details>

### [Bilevel Joint Unsupervised and Supervised Training for Automatic Speech Recognition](2412.08548.md)
**Xiaodong Cui, A F M Saif, Songtao Lu, Lisha Chen et al.** · 2024-12-11

<details>
<summary>Abstract</summary>

In this paper, we propose a bilevel joint unsupervised and supervised training (BL-JUST) framework for automatic speech recognition. Compared to the conventional pre-training and fine-tuning strategy which is a disconnected two-stage process, BL-JUST tries to optimize an acoustic model such that it simultaneously minimizes both the unsupervised and supervised loss functions. Because BL-JUST seeks matched local optima of both loss functions, acoustic representations learned by the acoustic model strike a good balance between being generic and task-specific. We solve the BL-JUST problem using penalty-based bilevel gradient descent and evaluate the trained deep neural network acoustic models on various datasets with a variety of architectures and loss functions. We show that BL-JUST can outperform the widely-used pre-training and fine-tuning strategy and some other popular semi-supervised techniques.

</details>

### [LatentSpeech: Latent Diffusion for Text-To-Speech Generation](2412.08117.md)
**Haowei Lou, Helen Paik, Pari Delir Haghighi, Wen Hu et al.** · 2024-12-11

<details>
<summary>Abstract</summary>

Diffusion-based Generative AI gains significant attention for its superior performance over other generative techniques like Generative Adversarial Networks and Variational Autoencoders. While it has achieved notable advancements in fields such as computer vision and natural language processing, their application in speech generation remains under-explored. Mainstream Text-to-Speech systems primarily map outputs to Mel-Spectrograms in the spectral space, leading to high computational loads due to the sparsity of MelSpecs. To address these limitations, we propose LatentSpeech, a novel TTS generation approach utilizing latent diffusion models. By using latent embeddings as the intermediate representation, LatentSpeech reduces the target dimension to 5% of what is required for MelSpecs, simplifying the processing for the TTS encoder and vocoder and enabling efficient high-quality speech generation. This study marks the first integration of latent diffusion models in TTS, enhancing the accuracy and naturalness of generated speech. Experimental results on benchmark datasets demonstrate that LatentSpeech achieves a 25% improvement in Word Error Rate and a 24% improvement in Mel Cepstral Distortion compared to existing models, with further improvements rising to 49.5% and 26%, respectively, with additional training data. These findings highlight the potential of LatentSpeech to advance the state-of-the-art in TTS technology

</details>

### [Effective Text Adaptation for LLM-based ASR through Soft Prompt Fine-Tuning](2412.06967.md)
**Yingyi Ma, Zhe Liu, Ozlem Kalinli** · 2024-12-09

<details>
<summary>Abstract</summary>

The advent of Large Language Models (LLM) has reformed the Automatic Speech Recognition (ASR). Prompting LLM with audio embeddings to generate transcriptions becomes the new state-of-the-art ASR. Despite LLMs being trained with an extensive amount of text corpora, high-quality domain-specific text data can still significantly enhance ASR performance on domain adaptation tasks. Although LLM-based ASR can naturally incorporate more text corpora by fine-tuning the LLM decoder, fine-tuning such ASR on text-only data without paired prompts may diminish the effectiveness of domain-specific knowledge. To mitigate this issue, we propose a two-step soft prompt fine-tuning strategy that enhances domain-specific text adaptation. Experimental results show that text adaptation with our proposed method achieved a relative up to 9% Word Error Rate (WER) reduction and up to 18% Entity Error Rate (EER) reduction on the target domain compared to the baseline ASR. Combining this with domain-specific Language Model (LM) fusion can further improve the EER by a relative 2-5%

</details>

### [Adaptive Dropout for Pruning Conformers](2412.04836.md)
**Yotaro Kubo, Xingyu Cai, Michiel Bacchiani** · 2024-12-06

<details>
<summary>Abstract</summary>

This paper proposes a method to effectively perform joint training-and-pruning based on adaptive dropout layers with unit-wise retention probabilities. The proposed method is based on the estimation of a unit-wise retention probability in a dropout layer. A unit that is estimated to have a small retention probability can be considered to be prunable. The retention probability of the unit is estimated using back-propagation and the Gumbel-Softmax technique. This pruning method is applied at several application points in Conformers such that the effective number of parameters can be significantly reduced. Specifically, adaptive dropout layers are introduced in three locations in each Conformer block: (a) the hidden layer of the feed-forward-net component, (b) the query vectors and the value vectors of the self-attention component, and (c) the input vectors of the LConv component. The proposed method is evaluated by conducting a speech recognition experiment on the LibriSpeech task. It was shown that this approach could simultaneously achieve a parameter reduction and accuracy improvement. The word error rates improved by approx 1% while reducing the number of parameters by 54%.

</details>

### [Representation Purification for End-to-End Speech Translation](2412.04266.md)
**Chengwei Zhang, Yue Zhou, Rui Zhao, Yidong Chen et al.** · 2024-12-05

<details>
<summary>Abstract</summary>

Speech-to-text translation (ST) is a cross-modal task that involves converting spoken language into text in a different language. Previous research primarily focused on enhancing speech translation by facilitating knowledge transfer from machine translation, exploring various methods to bridge the gap between speech and text modalities. Despite substantial progress made, factors in speech that are not relevant to translation content, such as timbre and rhythm, often limit the efficiency of knowledge transfer. In this paper, we conceptualize speech representation as a combination of content-agnostic and content-relevant factors. We examine the impact of content-agnostic factors on translation performance through preliminary experiments and observe a significant performance deterioration when content-agnostic perturbations are introduced to speech signals. To address this issue, we propose a \textbf{S}peech \textbf{R}epresentation \textbf{P}urification with \textbf{S}upervision \textbf{E}nhancement (SRPSE) framework, which excludes the content-agnostic components within speech representations to mitigate their negative impact on ST. Experiments on MuST-C and CoVoST-2 datasets demonstrate that SRPSE significantly improves translation performance across all translation directions in three settings and achieves preeminent performance under a \textit{transcript-free} setting.

</details>

### [GLM-4-Voice: Towards Intelligent and Human-Like End-to-End Spoken Chatbot](2412.02612.md)
**Aohan Zeng, Zhengxiao Du, Mingdao Liu, Kedong Wang et al.** · 2024-12-03

<details>
<summary>Abstract</summary>

We introduce GLM-4-Voice, an intelligent and human-like end-to-end spoken chatbot. It supports both Chinese and English, engages in real-time voice conversations, and varies vocal nuances such as emotion, intonation, speech rate, and dialect according to user instructions. GLM-4-Voice uses an ultra-low bitrate (175bps), single-codebook speech tokenizer with 12.5Hz frame rate derived from an automatic speech recognition (ASR) model by incorporating a vector-quantized bottleneck into the encoder. To efficiently transfer knowledge from text to speech modalities, we synthesize speech-text interleaved data from existing text pre-training corpora using a text-to-token model. We continue pre-training from the pre-trained text language model GLM-4-9B with a combination of unsupervised speech data, interleaved speech-text data, and supervised speech-text data, scaling up to 1 trillion tokens, achieving state-of-the-art performance in both speech language modeling and spoken question answering. We then fine-tune the pre-trained model with high-quality conversational speech data, achieving superior performance compared to existing baselines in both conversational ability and speech quality. The open models can be accessed through https://github.com/THUDM/GLM-4-Voice and https://huggingface.co/THUDM/glm-4-voice-9b.

</details>

### [AlignFormer: Modality Matching Can Achieve Better Zero-shot Instruction-Following Speech-LLM](2412.01145.md)
**Ruchao Fan, Bo Ren, Yuxuan Hu, Rui Zhao et al.** · 2024-12-02

<details>
<summary>Abstract</summary>

Integrating speech into LLM (speech-LLM) has gaining increased attention recently. The mainstream solution is to connect a well-trained speech encoder and LLM with a neural adapter. However, the length mismatch between the speech and text sequences are not well handled, leading to imperfect modality matching between the speech and text. In this work, we propose a novel neural adapter, AlignFormer, to reduce the length gap between the two modalities. AlignFormer consists of CTC and dynamic-window QFormer layers, where the CTC alignment provides the dynamic window information for QFormer. The LLM backbone is frozen in training to preserve its text capability, especially the instruction following capability. When training with ASR data only, the proposed AlignFormer unlocks the instruction following capability for speech-LLM and the model can perform zero-shot speech translation (ST) and speech question answering (SQA) tasks. In fact, speech-LLM with AlignFormer can theoretically perform any tasks that the LLM backbone can deal with in the speech version. To evaluate the effectiveness of the instruction-following speech-LLM, we propose to use instruction following rate (IFR) and offer a systematic perspective for the IFR evaluation. In addition, we find that the audio position in training would affect the instruction following capability of speech-LLM and conduct an in-depth study on it. Our findings show that audio-first training achieves higher IFR than instruction-first training. The AlignFormer can achieve a near 100% IFR with audio-first training and game-changing improvements from zero to non-zero IFR on some evaluation data with instruction-first training. We believe that this study is a big step towards the perfect speech and text modality matching in the LLM embedding space.

</details>

### [Improving Transducer-Based Spoken Language Understanding With Self-Conditioned CTC and Knowledge Transfer](s2:66ff6a74fe647c5401da2a6b2e9b46a6abde075d.md)
**Vishal Sunder, E. Fosler-Lussier** · 2024-12-02

<details>
<summary>Abstract</summary>

In this paper, we propose to improve end-to-end (E2E) spoken language understand (SLU) in an RNN transducer model (RNN-T) by incorporating a joint self-conditioned CTC automatic speech recognition (ASR) objective. Our proposed model is akin to an E2E differentiable cascaded model which performs ASR and SLU sequentially and we ensure that the SLU task is conditioned on the ASR task by having CTC self conditioning. This novel joint modeling of ASR and SLU improves SLU performance significantly over just using SLU optimization. We further improve the performance by aligning the acoustic embeddings of this model with the semantically richer BERT model. Our proposed knowledge transfer strategy makes use of a bag-of-entity prediction layer on the aligned embeddings and the output of this is used to condition the RNN-T based SLU decoding. These techniques show significant improvement over several strong baselines and can perform at par with large models like Whisper with significantly fewer parameters.

</details>

### [A Comparative Study of LLM-based ASR and Whisper in Low Resource and Code Switching Scenario](2412.00721.md)
**Zheshu Song, Ziyang Ma, Yifan Yang, Jianheng Zhuo et al.** · 2024-12-01

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have showcased exceptional performance across diverse NLP tasks, and their integration with speech encoder is rapidly emerging as a dominant trend in the Automatic Speech Recognition (ASR) field. Previous works mainly concentrated on leveraging LLMs for speech recognition in English and Chinese. However, their potential for addressing speech recognition challenges in low resource settings remains underexplored. Hence, in this work, we aim to explore the capability of LLMs in low resource ASR and Mandarin-English code switching ASR. We also evaluate and compare the recognition performance of LLM-based ASR systems against Whisper model. Extensive experiments demonstrate that LLM-based ASR yields a relative gain of 12.8\% over the Whisper model in low resource ASR while Whisper performs better in Mandarin-English code switching ASR. We hope that this study could shed light on ASR for low resource scenarios.

</details>

### [SSDM 2.0: Time-Accurate Speech Rich Transcription with Non-Fluencies](2412.00265.md)
**Jiachen Lian, Xuanru Zhou, Zoe Ezzes, Jet Vonk et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

Speech is a hierarchical collection of text, prosody, emotions, dysfluencies, etc. Automatic transcription of speech that goes beyond text (words) is an underexplored problem. We focus on transcribing speech along with non-fluencies (dysfluencies). The current state-of-the-art pipeline SSDM suffers from complex architecture design, training complexity, and significant shortcomings in the local sequence aligner, and it does not explore in-context learning capacity. In this work, we propose SSDM 2.0, which tackles those shortcomings via four main contributions: (1) We propose a novel \textit{neural articulatory flow} to derive highly scalable speech representations. (2) We developed a \textit{full-stack connectionist subsequence aligner} that captures all types of dysfluencies. (3) We introduced a mispronunciation prompt pipeline and consistency learning module into LLM to leverage dysfluency \textit{in-context pronunciation learning} abilities. (4) We curated Libri-Dys and open-sourced the current largest-scale co-dysfluency corpus, \textit{Libri-Co-Dys}, for future research endeavors. In clinical experiments on pathological speech transcription, we tested SSDM 2.0 using nfvPPA corpus primarily characterized by \textit{articulatory dysfluencies}. Overall, SSDM 2.0 outperforms SSDM and all other dysfluency transcription models by a large margin. See our project demo page at \url{https://berkeley-speech-group.github.io/SSDM2.0/}.

</details>

### [AMPS: ASR with Multimodal Paraphrase Supervision](2411.18368.md)
**Abhishek Gupta, Amruta Parulekar, Sameep Chattopadhyay, Preethi Jyothi** · 2024-11-27

<details>
<summary>Abstract</summary>

Spontaneous or conversational multilingual speech presents many challenges for state-of-the-art automatic speech recognition (ASR) systems. In this work, we present a new technique AMPS that augments a multilingual multimodal ASR system with paraphrase-based supervision for improved conversational ASR in multiple languages, including Hindi, Marathi, Malayalam, Kannada, and Nyanja. We use paraphrases of the reference transcriptions as additional supervision while training the multimodal ASR model and selectively invoke this paraphrase objective for utterances with poor ASR performance. Using AMPS with a state-of-the-art multimodal model SeamlessM4T, we obtain significant relative reductions in word error rates (WERs) of up to 5%. We present detailed analyses of our system using both objective and human evaluation metrics.

</details>

### [Continual Learning in Machine Speech Chain Using Gradient Episodic Memory](2411.18320.md)
**Geoffrey Tyndall, Kurniawati Azizah, Dipta Tanaya, Ayu Purwarianti et al.** · 2024-11-27

<details>
<summary>Abstract</summary>

Continual learning for automatic speech recognition (ASR) systems poses a challenge, especially with the need to avoid catastrophic forgetting while maintaining performance on previously learned tasks. This paper introduces a novel approach leveraging the machine speech chain framework to enable continual learning in ASR using gradient episodic memory (GEM). By incorporating a text-to-speech (TTS) component within the machine speech chain, we support the replay mechanism essential for GEM, allowing the ASR model to learn new tasks sequentially without significant performance degradation on earlier tasks. Our experiments, conducted on the LJ Speech dataset, demonstrate that our method outperforms traditional fine-tuning and multitask learning approaches, achieving a substantial error rate reduction while maintaining high performance across varying noise conditions. We showed the potential of our semi-supervised machine speech chain approach for effective and efficient continual learning in speech recognition.

</details>

### [Aligning Pre-trained Models for Spoken Language Translation](2411.18294.md)
**Šimon Sedláček, Santosh Kesiraju, Alexander Polok, Jan Černocký** · 2024-11-27

<details>
<summary>Abstract</summary>

This paper investigates a novel approach to end-to-end speech translation (ST) based on aligning frozen pre-trained automatic speech recognition (ASR) and machine translation (MT) models via a small connector module (Q-Former, our Subsampler-Transformer Encoder). This connector bridges the gap between the speech and text modalities, transforming ASR encoder embeddings into the latent representation space of the MT encoder while being the only part of the system optimized during training. Experiments are conducted on the How2 English-Portuguese dataset as we investigate the alignment approach in a small-scale scenario focusing on ST. While keeping the size of the connector module constant and small in comparison ( < 5% of the size of the larger aligned models), increasing the size and capability of the foundation ASR and MT models universally improves translation results. We also find that the connectors can serve as domain adapters for the foundation MT models, significantly improving translation performance in the aligned ST setting. We conclude that this approach represents a viable and scalable approach to training end-to-end ST systems.

</details>

### [How to Learn a New Language? An Efficient Solution for Self-Supervised Learning Models Unseen Languages Adaption in Low-Resource Scenario](2411.18217.md)
**Shih-Heng Wang, Zih-Ching Chen, Jiatong Shi, Ming-To Chuang et al.** · 2024-11-27

<details>
<summary>Abstract</summary>

The utilization of speech Self-Supervised Learning (SSL) models achieves impressive performance on Automatic Speech Recognition (ASR). However, in low-resource language ASR, they encounter the domain mismatch problem between pre-trained and low-resource languages. Typical solutions like fine-tuning the SSL model suffer from high computation costs while using frozen SSL models as feature extractors comes with poor performance. To handle these issues, we extend a conventional efficient fine-tuning scheme based on the adapter. We add an extra intermediate adaptation to warm up the adapter and downstream model initialization. Remarkably, we update only 1-5% of the total model parameters to achieve the adaptation. Experimental results on the ML-SUPERB dataset show that our solution outperforms conventional efficient fine-tuning. It achieves up to a 28% relative improvement in the Character/Phoneme error rate when adapting to unseen languages.

</details>

### [MSA-ASR: Efficient Multilingual Speaker Attribution with frozen ASR Models](2411.18152.md)
**Thai-Binh Nguyen, Alexander Waibel** · 2024-11-27

<details>
<summary>Abstract</summary>

Speaker-attributed automatic speech recognition (SA-ASR) aims to transcribe speech while assigning transcripts to the corresponding speakers accurately. Existing methods often rely on complex modular systems or require extensive fine-tuning of joint modules, limiting their adaptability and general efficiency. This paper introduces a novel approach, leveraging a frozen multilingual ASR model to incorporate speaker attribution into the transcriptions, using only standard monolingual ASR datasets. Our method involves training a speaker module to predict speaker embeddings based on weak labels without requiring additional ASR model modifications. Despite being trained exclusively with non-overlapping monolingual data, our approach effectively extracts speaker attributes across diverse multilingual datasets, including those with overlapping speech. Experimental results demonstrate competitive performance compared to strong baselines, highlighting the model's robustness and potential for practical applications.

</details>

### [SALMONN-omni: A Codec-free LLM for Full-duplex Speech Understanding and Generation](2411.18138.md)
**Wenyi Yu, Siyin Wang, Xiaoyu Yang, Xianzhao Chen et al.** · 2024-11-27

<details>
<summary>Abstract</summary>

Full-duplex multimodal large language models (LLMs) provide a unified framework for addressing diverse speech understanding and generation tasks, enabling more natural and seamless human-machine conversations. Unlike traditional modularised conversational AI systems, which separate speech recognition, understanding, and text-to-speech generation into distinct components, multimodal LLMs operate as single end-to-end models. This streamlined design eliminates error propagation across components and fully leverages the rich non-verbal information embedded in input speech signals. We introduce SALMONN-omni, a codec-free, full-duplex speech understanding and generation model capable of simultaneously listening to its own generated speech and background sounds while speaking. To support this capability, we propose a novel duplex spoken dialogue framework incorporating a ``thinking'' mechanism that facilitates asynchronous text and speech generation relying on embeddings instead of codecs (quantized speech and audio tokens). Experimental results demonstrate SALMONN-omni's versatility across a broad range of streaming speech tasks, including speech recognition, speech enhancement, and spoken question answering. Additionally, SALMONN-omni excels at managing turn-taking, barge-in, and echo cancellation scenarios, establishing its potential as a robust prototype for full-duplex conversational AI systems. To the best of our knowledge, SALMONN-omni is the first codec-free model of its kind. A full technical report along with model checkpoints will be released soon.

</details>

### [Fusion of Discrete Representations and Self-Augmented Representations for Multilingual Automatic Speech Recognition](2411.18107.md)
**Shih-heng Wang, Jiatong Shi, Chien-yu Huang, Shinji Watanabe et al.** · 2024-11-27

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models have shown exceptional capabilities across various speech-processing tasks. Continuous SSL representations are effective but suffer from high computational and storage demands. On the other hand, discrete SSL representations, although with degraded performance, reduce transmission and storage costs, and improve input sequence efficiency through de-duplication and subword-modeling. To boost the performance of discrete representations for ASR, we introduce a novel fusion mechanism that integrates two discrete representations. The fusion mechanism preserves all the benefits of discrete representation while enhancing the model's performance by integrating complementary information. Additionally, we explore "self-augmented'' discrete representations, which apply transformations to a single continuous SSL representation, eliminating the fusion mechanism's dependency on multiple SSL models and further decreasing its inference costs. Experimental results on benchmarks, including LibriSpeech and ML-SUPERB, indicate up to 19% and 24% relative character error rate improvement compared with the non-fusion baseline, validating the effectiveness of our proposed methods.

</details>

### [Wearable intelligent throat enables natural speech in stroke patients with dysarthria](2411.18266.md)
**Chenyu Tang, Shuo Gao, Cong Li, Wentian Yi et al.** · 2024-11-27

<details>
<summary>Abstract</summary>

Wearable silent speech systems hold significant potential for restoring communication in patients with speech impairments. However, seamless, coherent speech remains elusive, and clinical efficacy is still unproven. Here, we present an AI-driven intelligent throat (IT) system that integrates throat muscle vibrations and carotid pulse signal sensors with large language model (LLM) processing to enable fluent, emotionally expressive communication. The system utilizes ultrasensitive textile strain sensors to capture high-quality signals from the neck area and supports token-level processing for real-time, continuous speech decoding, enabling seamless, delay-free communication. In tests with five stroke patients with dysarthria, IT's LLM agents intelligently corrected token errors and enriched sentence-level emotional and logical coherence, achieving low error rates (4.2% word error rate, 2.9% sentence error rate) and a 55% increase in user satisfaction. This work establishes a portable, intuitive communication platform for patients with dysarthria with the potential to be applied broadly across different neurological conditions and in multi-language support systems.

</details>

### [Disentangled-Transformer: An Explainable End-to-End Automatic Speech Recognition Model with Speech Content-Context Separation](2411.17846.md)
**Pu Wang, Hugo Van hamme** · 2024-11-26

<details>
<summary>Abstract</summary>

End-to-end transformer-based automatic speech recognition (ASR) systems often capture multiple speech traits in their learned representations that are highly entangled, leading to a lack of interpretability. In this study, we propose the explainable Disentangled-Transformer, which disentangles the internal representations into sub-embeddings with explicit content and speaker traits based on varying temporal resolutions. Experimental results show that the proposed Disentangled-Transformer produces a clear speaker identity, separated from the speech content, for speaker diarization while improving ASR performance.

</details>

### [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](2411.17607.md)
**Aohan Zeng, Zhengxiao Du, Mingdao Liu, Lei Zhang et al.** · 2024-11-26

<details>
<summary>Abstract</summary>

Speech language models (SpeechLMs) accept speech input and produce speech output, allowing for more natural human-computer interaction compared to text-based large language models (LLMs). Traditional approaches for developing SpeechLMs are constrained by the limited availability of unsupervised speech data and parallel speech-text data, which are significantly less abundant than text pre-training data, thereby limiting their scalability as LLMs. We propose a novel approach to scaling speech-text pre-training by leveraging large-scale synthetic interleaved data derived from text corpora, eliminating the need for parallel speech-text datasets. Our method efficiently constructs speech-text interleaved data by sampling text spans from existing text corpora and synthesizing corresponding speech spans using a text-to-token model, bypassing the need to generate actual speech. We also employ a supervised speech tokenizer derived from an automatic speech recognition (ASR) model by incorporating a vector-quantized bottleneck into the encoder. This supervised training approach results in discrete speech tokens with strong semantic preservation even at lower frame rates (e.g. 12.5Hz), while still maintaining speech reconstruction quality. Starting from a pre-trained language model and scaling our pre-training to 1 trillion tokens (with 600B synthetic interleaved speech-text data), we achieve state-of-the-art performance in speech language modeling and spoken question answering, improving performance on spoken questions tasks from the previous SOTA of 13% (Moshi) to 31%. We further demonstrate that by fine-tuning the pre-trained model with speech dialogue data, we can develop an end-to-end spoken chatbot that achieves competitive performance comparable to existing baselines in both conversational abilities and speech quality, even operating exclusively in the speech domain.

</details>

### [Towards Maximum Likelihood Training for Transducer-based Streaming Speech Recognition](2411.17537.md)
**Hyeonseung Lee, Ji Won Yoon, Sungsoo Kim, Nam Soo Kim** · 2024-11-26

<details>
<summary>Abstract</summary>

Transducer neural networks have emerged as the mainstream approach for streaming automatic speech recognition (ASR), offering state-of-the-art performance in balancing accuracy and latency. In the conventional framework, streaming transducer models are trained to maximize the likelihood function based on non-streaming recursion rules. However, this approach leads to a mismatch between training and inference, resulting in the issue of deformed likelihood and consequently suboptimal ASR accuracy. We introduce a mathematical quantification of the gap between the actual likelihood and the deformed likelihood, namely forward variable causal compensation (FoCC). We also present its estimator, FoCCE, as a solution to estimate the exact likelihood. Through experiments on the LibriSpeech dataset, we show that FoCCE training improves the accuracy of the streaming transducers.

</details>

### [Enhancing Code-Switching ASR Leveraging Non-Peaky CTC Loss and Deep Language Posterior Injection](2412.08651.md)
**Tzu-Ting Yang, Hsin-Wei Wang, Yi-Cheng Wang, Berlin Chen** · 2024-11-26

<details>
<summary>Abstract</summary>

Code-switching-where multilingual speakers alternately switch between languages during conversations-still poses significant challenges to end-to-end (E2E) automatic speech recognition (ASR) systems due to phenomena of both acoustic and semantic confusion. This issue arises because ASR systems struggle to handle the rapid alternation of languages effectively, which often leads to significant performance degradation. Our main contributions are at least threefold: First, we incorporate language identification (LID) information into several intermediate layers of the encoder, aiming to enrich output embeddings with more detailed language information. Secondly, through the novel application of language boundary alignment loss, the subsequent ASR modules are enabled to more effectively utilize the knowledge of internal language posteriors. Third, we explore the feasibility of using language posteriors to facilitate deep interaction between shared encoder and language-specific encoders. Through comprehensive experiments on the SEAME corpus, we have verified that our proposed method outperforms the prior-art method, disentangle based mixture-of-experts (D-MoE), further enhancing the acuity of the encoder to languages.

</details>

### [k2SSL: A Faster and Better Framework for Self-Supervised Speech Representation Learning](2411.17100.md)
**Yifan Yang, Jianheng Zhuo, Zengrui Jin, Ziyang Ma et al.** · 2024-11-26

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has achieved great success in speech-related tasks. While Transformer and Conformer architectures have dominated SSL backbones, encoders like Zipformer, which excel in automatic speech recognition (ASR), remain unexplored in SSL. Concurrently, inefficiencies in data processing within existing SSL training frameworks, such as fairseq, pose challenges in managing the growing volumes of training data. To address these issues, we propose k2SSL, an open-source framework that offers faster, more memory-efficient, and better-performing self-supervised speech representation learning, focusing on downstream ASR tasks. The optimized HuBERT and proposed Zipformer-based SSL systems exhibit substantial reductions in both training time and memory usage during SSL training. Experiments on LibriSpeech demonstrate that Zipformer Base significantly outperforms HuBERT and WavLM, achieving up to a 34.8% relative WER reduction compared to HuBERT Base after fine-tuning, along with a 3.5x pre-training speedup in GPU hours. When scaled to 60k hours of LibriLight data, Zipformer Large exhibits remarkable efficiency, matching HuBERT Large's performance while requiring only 5/8 pre-training steps.

</details>

### [High-precision medical speech recognition through synthetic data and semantic correction: UNITED-MEDASR](2412.00055.md)
**Sourav Banerjee, Ayushi Agarwal, Promila Ghosh** · 2024-11-24

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems in the clinical domain face significant challenges, notably the need to recognise specialised medical vocabulary accurately and meet stringent precision requirements. We introduce United-MedASR, a novel architecture that addresses these challenges by integrating synthetic data generation, precision ASR fine-tuning, and advanced semantic enhancement techniques. United-MedASR constructs a specialised medical vocabulary by synthesising data from authoritative sources such as ICD-10 (International Classification of Diseases, 10th Revision), MIMS (Monthly Index of Medical Specialties), and FDA databases. This enriched vocabulary helps finetune the Whisper ASR model to better cater to clinical needs. To enhance processing speed, we incorporate Faster Whisper, ensuring streamlined and high-speed ASR performance. Additionally, we employ a customised BART-based semantic enhancer to handle intricate medical terminology, thereby increasing accuracy efficiently. Our layered approach establishes new benchmarks in ASR performance, achieving a Word Error Rate (WER) of 0.985% on LibriSpeech test-clean, 0.26% on Europarl-ASR EN Guest-test, and demonstrating robust performance on Tedlium (0.29% WER) and FLEURS (0.336% WER). Furthermore, we present an adaptable architecture that can be replicated across different domains, making it a versatile solution for domain-specific ASR systems.

</details>

### [Transforming NLU with Babylon: A Case Study in Development of Real-time, Edge-Efficient, Multi-Intent Translation System for Automated Drive-Thru Ordering](2411.15372.md)
**Mostafa Varzaneh, Pooja Voladoddi, Tanmay Bakshi, Uma Gunturi** · 2024-11-22

<details>
<summary>Abstract</summary>

Real-time conversational AI agents face challenges in performing Natural Language Understanding (NLU) in dynamic, outdoor environments like automated drive-thru systems. These settings require NLU models to handle background noise, diverse accents, and multi-intent queries while operating under strict latency and memory constraints on edge devices. Additionally, robustness to errors from upstream Automatic Speech Recognition (ASR) is crucial, as ASR outputs in these environments are often noisy. We introduce Babylon, a transformer-based architecture that tackles NLU as an intent translation task, converting natural language inputs into sequences of regular language units ('transcodes') that encode both intents and slot information. This formulation allows Babylon to manage multi-intent scenarios in a single dialogue turn. Furthermore, Babylon incorporates an LSTM-based token pooling mechanism to preprocess phoneme sequences, reducing input length and optimizing for low-latency, low-memory edge deployment. This also helps mitigate inaccuracies in ASR outputs, enhancing system robustness. While this work focuses on drive-thru ordering, Babylon's design extends to similar noise-prone scenarios, for e.g. ticketing kiosks. Our experiments show that Babylon achieves significantly better accuracy-latency-memory footprint trade-offs over typically employed NMT models like Flan-T5 and BART, demonstrating its effectiveness for real-time NLU in edge deployment settings.

</details>

### [TSkips: Efficiency Through Explicit Temporal Delay Connections in Spiking Neural Networks](2411.16711.md)
**Prajna G. Malettira, Shubham Negi, Wachirawit Ponghiran, Kaushik Roy** · 2024-11-22

<details>
<summary>Abstract</summary>

Spiking Neural Networks (SNNs) with their bio-inspired Leaky Integrate-and-Fire (LIF) neurons inherently capture temporal information. This makes them well-suited for sequential tasks like processing event-based data from Dynamic Vision Sensors (DVS) and event-based speech tasks. Harnessing the temporal capabilities of SNNs requires mitigating vanishing spikes during training, capturing spatio-temporal patterns and enhancing precise spike timing. To address these challenges, we propose TSkips, augmenting SNN architectures with forward and backward skip connections that incorporate explicit temporal delays. These connections capture long-term spatio-temporal dependencies and facilitate better spike flow over long sequences. The introduction of TSkips creates a vast search space of possible configurations, encompassing skip positions and time delay values. To efficiently navigate this search space, this work leverages training-free Neural Architecture Search (NAS) to identify optimal network structures and corresponding delays. We demonstrate the effectiveness of our approach on four event-based datasets: DSEC-flow for optical flow estimation, DVS128 Gesture for hand gesture recognition and Spiking Heidelberg Digits (SHD) and Spiking Speech Commands (SSC) for speech recognition. Our method achieves significant improvements across these datasets: up to 18% reduction in Average Endpoint Error (AEE) on DSEC-flow, 8% increase in classification accuracy on DVS128 Gesture, and up to 8% and 16% higher classification accuracy on SHD and SSC, respectively.

</details>

### [Tiny-Align: Bridging Automatic Speech Recognition and Large Language Model on the Edge](2411.13766.md)
**Ruiyang Qin, Dancheng Liu, Gelei Xu, Zheyu Yan et al.** · 2024-11-21

<details>
<summary>Abstract</summary>

The combination of Large Language Models (LLM) and Automatic Speech Recognition (ASR), when deployed on edge devices (called edge ASR-LLM), can serve as a powerful personalized assistant to enable audio-based interaction for users. Compared to text-based interaction, edge ASR-LLM allows accessible and natural audio interactions. Unfortunately, existing ASR-LLM models are mainly trained in high-performance computing environments and produce substantial model weights, making them difficult to deploy on edge devices. More importantly, to better serve users' personalized needs, the ASR-LLM must be able to learn from each distinct user, given that audio input often contains highly personalized characteristics that necessitate personalized on-device training. Since individually fine-tuning the ASR or LLM often leads to suboptimal results due to modality-specific limitations, end-to-end training ensures seamless integration of audio features and language understanding (cross-modal alignment), ultimately enabling a more personalized and efficient adaptation on edge devices. However, due to the complex training requirements and substantial computational demands of existing approaches, cross-modal alignment between ASR audio and LLM can be challenging on edge devices. In this work, we propose a resource-efficient cross-modal alignment framework that bridges ASR and LLMs on edge devices to handle personalized audio input. Our framework enables efficient ASR-LLM alignment on resource-constrained devices like NVIDIA Jetson Orin (8GB RAM), achieving 50x training time speedup while improving the alignment quality by more than 50\%. To the best of our knowledge, this is the first work to study efficient ASR-LLM alignment on resource-constrained edge devices.

</details>

### [Whisper Finetuning on Nepali Language](2411.12587.md)
**Sanjay Rijal, Shital Adhikari, Manish Dahal, Manish Awale et al.** · 2024-11-19

<details>
<summary>Abstract</summary>

Despite the growing advancements in Automatic Speech Recognition (ASR) models, the development of robust models for underrepresented languages, such as Nepali, remains a challenge. This research focuses on making an exhaustive and generalized dataset followed by fine-tuning OpenAI's Whisper models of different sizes to improve transcription (speech-to-text) accuracy for the Nepali language. We leverage publicly available ASR datasets and self-recorded custom datasets with a diverse range of accents, dialects, and speaking styles further enriched through augmentation. Our experimental results demonstrate that fine-tuning Whisper models on our curated custom dataset substantially reduces the Word Error Rate (WER) across all model sizes attributed to larger data variations in terms of speaker's age, gender, and sentiment, acoustic environment, dialect, denser audio segments (15-30 seconds) that are more compatible with Whisper's input, and manual curation of audios and transcriptions. Notably, our approach outperforms Whisper's baseline models trained on Fleur's dataset, achieving WER reductions of up to 36.2% on the small and 23.8% on medium models. Furthermore, we show that data augmentation plays a significant role in enhancing model robustness. Our approach underlines the importance of dataset quality, variation, and augmentation in the adaptation of state-of-the-art models to underrepresented languages for developing accurate ASR systems.

</details>

### [DGSNA: Dynamic Generative Scene-based Noise Addition method](2411.12363.md)
**Zihao Chen, Zhentao Lin, Bi Zeng, Linyi Huang et al.** · 2024-11-19

<details>
<summary>Abstract</summary>

To ensure the reliable operation of speech systems across diverse environments, noise addition methods have emerged as the standard solution.However, existing methods offer limited coverage of real-world scenes and depend on pre-existing noise libraries and scene metadata.This paper presents prompt-based Dynamic Generative Scene-based Noise Addition (DGSNA), a novel approach driven by generative language models that integrates Dynamic Generation of Scene-based Information (DGSI) with Scene-based Noise Addition for Speech (SNAS).The DGSI module, with a BET (Background, Examples, Task) prompt framework, dynamically generates logic-compliant scene-based information, including scene dimensions, sound sources, and microphone positions, thereby addressing the challenges of scene enumeration and detailed description.Complementing this, the SNAS module employs a Time-Frequency Diffusion-based (TFD) Text-to-Audio model to synthesize scene-specific noise. By integrating this noise with clean speech via Room Impulse Response (RIR) filters, the module streamlines the traditionally labor-intensive process of replicating diverse acoustic environments.Experimental results show that DGSNA significantly enhances the robustness of speech recognition and keyword spotting models, achieving relative improvements of up to 11.32\%. Furthermore, DGSNA is highly compatible with existing noise addition techniques. Our implementation and demonstrations are available at https://dgsna.github.io.

</details>

### [A Novel Speech Analysis and Correction Tool for Arabic-Speaking Children](2411.13592.md)
**Lamia Berriche, Maha Driss, Areej Ahmed Almuntashri, Asma Mufreh Lghabi et al.** · 2024-11-18

<details>
<summary>Abstract</summary>

This paper introduces a new application named ArPA for Arabic kids who have trouble with pronunciation. Our application comprises two key components: the diagnostic module and the therapeutic module. The diagnostic process involves capturing the child's speech signal, preprocessing, and analyzing it using different machine learning classifiers like K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Decision Trees as well as deep neural network classifiers like ResNet18. The therapeutic module offers eye-catching gamified interfaces in which each correctly spoken letter earns a higher avatar level, providing positive reinforcement for the child's pronunciation improvement. Two datasets were used for experimental evaluation: one from a childcare centre and the other including Arabic alphabet pronunciation recordings. Our work uses a novel technique for speech recognition using Melspectrogram and MFCC images. The results show that the ResNet18 classifier on speech-to-image converted data effectively identifies mispronunciations in Arabic speech with an accuracy of 99.015\% with Mel-Spectrogram images outperforming ResNet18 with MFCC images.

</details>

### [BackdoorMBTI: A Backdoor Learning Multimodal Benchmark Tool Kit for Backdoor Defense Evaluation](2411.11006.md)
**Haiyang Yu, Tian Xie, Jiaping Gui, Pengyang Wang et al.** · 2024-11-17

<details>
<summary>Abstract</summary>

Over the past few years, the emergence of backdoor attacks has presented significant challenges to deep learning systems, allowing attackers to insert backdoors into neural networks. When data with a trigger is processed by a backdoor model, it can lead to mispredictions targeted by attackers, whereas normal data yields regular results. The scope of backdoor attacks is expanding beyond computer vision and encroaching into areas such as natural language processing and speech recognition. Nevertheless, existing backdoor defense methods are typically tailored to specific data modalities, restricting their application in multimodal contexts. While multimodal learning proves highly applicable in facial recognition, sentiment analysis, action recognition, visual question answering, the security of these models remains a crucial concern. Specifically, there are no existing backdoor benchmarks targeting multimodal applications or related tasks. In order to facilitate the research in multimodal backdoor, we introduce BackdoorMBTI, the first backdoor learning toolkit and benchmark designed for multimodal evaluation across three representative modalities from eleven commonly used datasets. BackdoorMBTI provides a systematic backdoor learning pipeline, encompassing data processing, data poisoning, backdoor training, and evaluation. The generated poison datasets and backdoor models enable detailed evaluation of backdoor defenses. Given the diversity of modalities, BackdoorMBTI facilitates systematic evaluation across different data types. Furthermore, BackdoorMBTI offers a standardized approach to handling practical factors in backdoor learning, such as issues related to data quality and erroneous labels. We anticipate that BackdoorMBTI will expedite future research in backdoor defense methods within a multimodal context. Code is available at https://github.com/SJTUHaiyangYu/BackdoorMBTI.

</details>

### [BanglaDialecto: An End-to-End AI-Powered Regional Speech Standardization](2411.10879.md)
**Md. Nazmus Sadat Samin, Jawad Ibn Ahad, Tanjila Ahmed Medha, Fuad Rahman et al.** · 2024-11-16

<details>
<summary>Abstract</summary>

This study focuses on recognizing Bangladeshi dialects and converting diverse Bengali accents into standardized formal Bengali speech. Dialects, often referred to as regional languages, are distinctive variations of a language spoken in a particular location and are identified by their phonetics, pronunciations, and lexicon. Subtle changes in pronunciation and intonation are also influenced by geographic location, educational attainment, and socioeconomic status. Dialect standardization is needed to ensure effective communication, educational consistency, access to technology, economic opportunities, and the preservation of linguistic resources while respecting cultural diversity. Being the fifth most spoken language with around 55 distinct dialects spoken by 160 million people, addressing Bangla dialects is crucial for developing inclusive communication tools. However, limited research exists due to a lack of comprehensive datasets and the challenges of handling diverse dialects. With the advancement in multilingual Large Language Models (mLLMs), emerging possibilities have been created to address the challenges of dialectal Automated Speech Recognition (ASR) and Machine Translation (MT). This study presents an end-to-end pipeline for converting dialectal Noakhali speech to standard Bangla speech. This investigation includes constructing a large-scale diverse dataset with dialectal speech signals that tailored the fine-tuning process in ASR and LLM for transcribing the dialect speech to dialect text and translating the dialect text to standard Bangla text. Our experiments demonstrated that fine-tuning the Whisper ASR model achieved a CER of 0.8% and WER of 1.5%, while the BanglaT5 model attained a BLEU score of 41.6% for dialect-to-standard text translation.

</details>

### [Brain-to-Text Decoding with Context-Aware Neural Representations and Large Language Models](2411.10657.md)
**Jingyuan Li, Trung Le, Chaofei Fan, Mingfei Chen et al.** · 2024-11-16

<details>
<summary>Abstract</summary>

Decoding attempted speech from neural activity offers a promising avenue for restoring communication abilities in individuals with speech impairments. Previous studies have focused on mapping neural activity to text using phonemes as the intermediate target. While successful, decoding neural activity directly to phonemes ignores the context dependent nature of the neural activity-to-phoneme mapping in the brain, leading to suboptimal decoding performance. In this work, we propose the use of diphone - an acoustic representation that captures the transitions between two phonemes - as the context-aware modeling target. We integrate diphones into existing phoneme decoding frameworks through a novel divide-and-conquer strategy in which we model the phoneme distribution by marginalizing over the diphone distribution. Our approach effectively leverages the enhanced context-aware representation of diphones while preserving the manageable class size of phonemes, a key factor in simplifying the subsequent phoneme-to-text conversion task. We demonstrate the effectiveness of our approach on the Brain-to-Text 2024 benchmark, where it achieves state-of-the-art Phoneme Error Rate (PER) of 15.34% compared to 16.62% PER of monophone-based decoding. When coupled with finetuned Large Language Models (LLMs), our method yields a Word Error Rate (WER) of 5.77%, significantly outperforming the 8.93% WER of the leading method in the benchmark.

</details>

### [Interactive Cycle Model: The Linkage Combination among Automatic Speech Recognition, Large Language Models and Smart Glasses](2411.10362.md)
**Libo Wang** · 2024-11-15

<details>
<summary>Abstract</summary>

This research proposes the interaction loop model "ASR-LLMs-Smart Glasses", which model combines automatic speech recognition, large language model and smart glasses to facilitate seamless human-computer interaction. And the methodology of this research involves decomposing the interaction process into different stages and elements. Speech is captured and processed by ASR, then analyzed and interpreted by LLMs. The results are then transmitted to smart glasses for display. The feedback loop is complete when the user interacts with the displayed data. Mathematical formulas are used to quantify the performance of the model that revolves around core evaluation points: accuracy, coherence, and latency during ASR speech-to-text conversion. The research results are provided theoretically to test and evaluate the feasibility and performance of the model. Detailed architectural details and experimental process have been uploaded to Github, the link is:https://github.com/brucewang123456789/GeniusTrail.git.

</details>

### [XLSR-Mamba: A Dual-Column Bidirectional State Space Model for Spoofing Attack Detection](2411.10027.md)
**Yang Xiao, Rohan Kumar Das** · 2024-11-15

<details>
<summary>Abstract</summary>

Transformers and their variants have achieved great success in speech processing. However, their multi-head self-attention mechanism is computationally expensive. Therefore, one novel selective state space model, Mamba, has been proposed as an alternative. Building on its success in automatic speech recognition, we apply Mamba for spoofing attack detection. Mamba is well-suited for this task as it can capture the artifacts in spoofed speech signals by handling long-length sequences. However, Mamba's performance may suffer when it is trained with limited labeled data. To mitigate this, we propose combining a new structure of Mamba based on a dual-column architecture with self-supervised learning, using the pre-trained wav2vec 2.0 model. The experiments show that our proposed approach achieves competitive results and faster inference on the ASVspoof 2021 LA and DF datasets, and on the more challenging In-the-Wild dataset, it emerges as the strongest candidate for spoofing attack detection. The code has been publicly released in https://github.com/swagshaw/XLSR-Mamba.

</details>

### [WavChat: A Survey of Spoken Dialogue Models](2411.13577.md)
**Shengpeng Ji, Yifu Chen, Minghui Fang, Jialong Zuo et al.** · 2024-11-15

<details>
<summary>Abstract</summary>

Recent advancements in spoken dialogue models, exemplified by systems like GPT-4o, have captured significant attention in the speech domain. Compared to traditional three-tier cascaded spoken dialogue models that comprise speech recognition (ASR), large language models (LLMs), and text-to-speech (TTS), modern spoken dialogue models exhibit greater intelligence. These advanced spoken dialogue models not only comprehend audio, music, and other speech-related features, but also capture stylistic and timbral characteristics in speech. Moreover, they generate high-quality, multi-turn speech responses with low latency, enabling real-time interaction through simultaneous listening and speaking capability. Despite the progress in spoken dialogue systems, there is a lack of comprehensive surveys that systematically organize and analyze these systems and the underlying technologies. To address this, we have first compiled existing spoken dialogue systems in the chronological order and categorized them into the cascaded and end-to-end paradigms. We then provide an in-depth overview of the core technologies in spoken dialogue models, covering aspects such as speech representation, training paradigm, streaming, duplex, and interaction capabilities. Each section discusses the limitations of these technologies and outlines considerations for future research. Additionally, we present a thorough review of relevant datasets, evaluation metrics, and benchmarks from the perspectives of training and evaluating spoken dialogue systems. We hope this survey will contribute to advancing both academic research and industrial applications in the field of spoken dialogue systems. The related material is available at https://github.com/jishengpeng/WavChat.

</details>

### [CJST: CTC Compressor based Joint Speech and Text Training for Decoder-Only ASR](2411.07607.md)
**Wei Zhou, Junteng Jia, Leda Sari, Jay Mahadeokar et al.** · 2024-11-12

<details>
<summary>Abstract</summary>

CTC compressor can be an effective approach to integrate audio encoders to decoder-only models, which has gained growing interest for different speech applications. In this work, we propose a novel CTC compressor based joint speech and text training (CJST) framework for decoder-only ASR. CJST matches speech and text modalities from both directions by exploring a simple modality adaptor and several features of the CTC compressor, including sequence compression, on-the-fly forced peaky alignment and CTC class embeddings. Experimental results on the Librispeech and TED-LIUM2 corpora show that the proposed CJST achieves an effective text injection without the need of duration handling, leading to the best performance for both in-domain and cross-domain scenarios. We also provide a comprehensive study on CTC compressor, covering various compression modes, edge case handling and behavior under both clean and noisy data conditions, which reveals the most robust setting to use CTC compressor for decoder-only models.

</details>

### [Mamba-based Decoder-Only Approach with Bidirectional Speech Modeling for Speech Recognition](2411.06968.md)
**Yoshiki Masuyama, Koichi Miyazaki, Masato Murata** · 2024-11-11

<details>
<summary>Abstract</summary>

Selective state space models (SSMs) represented by Mamba have demonstrated their computational efficiency and promising outcomes in various tasks, including automatic speech recognition (ASR). Mamba has been applied to ASR task with the attention-based encoder-decoder framework, where the cross-attention mechanism between encoder and decoder remains. This paper explores the capability of Mamba as the decoder-only architecture in ASR task. Our MAmba-based DEcoder-ONly approach (MADEON) consists of a single decoder that takes speech tokens as a condition and predicts text tokens in an autoregressive manner. To enhance MADEON, we further propose speech prefixing that performs bidirectional processing on speech tokens, which enriches the contextual information in the hidden states. Our experiments show that MADEON significantly outperforms a non-selective SSM. The combination of speech prefixing and the recently proposed Mamba-2 yields comparable performance to Transformer-based models on large datasets.

</details>

### [DCF-DS: Deep Cascade Fusion of Diarization and Separation for Speech Recognition under Realistic Single-Channel Conditions](2411.06667.md)
**Shu-Tong Niu, Jun Du, Ruo-Yu Wang, Gao-Bin Yang et al.** · 2024-11-11

<details>
<summary>Abstract</summary>

We propose a single-channel Deep Cascade Fusion of Diarization and Separation (DCF-DS) framework for back-end automatic speech recognition (ASR), combining neural speaker diarization (NSD) and speech separation (SS). First, we sequentially integrate the NSD and SS modules within a joint training framework, enabling the separation module to leverage speaker time boundaries from the diarization module effectively. Then, to complement DCF-DS training, we introduce a window-level decoding scheme that allows the DCF-DS framework to handle the sparse data convergence instability (SDCI) problem. We also explore using an NSD system trained on real datasets to provide more accurate speaker boundaries. Additionally, we incorporate an optional multi-input multi-output speech enhancement module (MIMO-SE) within the DCF-DS framework, which offers further performance gains. Finally, we enhance diarization results by re-clustering DCF-DS outputs, improving ASR accuracy. By incorporating the DCF-DS method, we achieved first place in the realistic single-channel track of the CHiME-8 NOTSOFAR-1 challenge. We also perform the evaluation on the open LibriCSS dataset, achieving a new state-of-the-art single-channel speech recognition performance.

</details>

### [Isochrony-Controlled Speech-to-Text Translation: A study on translating from Sino-Tibetan to Indo-European Languages](2411.07387.md)
**Midia Yousefi, Yao Qian, Junkun Chen, Gang Wang et al.** · 2024-11-11

<details>
<summary>Abstract</summary>

End-to-end speech translation (ST), which translates source language speech directly into target language text, has garnered significant attention in recent years. Many ST applications require strict length control to ensure that the translation duration matches the length of the source audio, including both speech and pause segments. Previous methods often controlled the number of words or characters generated by the Machine Translation model to approximate the source sentence's length without considering the isochrony of pauses and speech segments, as duration can vary between languages. To address this, we present improvements to the duration alignment component of our sequence-to-sequence ST model. Our method controls translation length by predicting the duration of speech and pauses in conjunction with the translation process. This is achieved by providing timing information to the decoder, ensuring it tracks the remaining duration for speech and pauses while generating the translation. The evaluation on the Zh-En test set of CoVoST 2, demonstrates that the proposed Isochrony-Controlled ST achieves 0.92 speech overlap and 8.9 BLEU, which has only a 1.4 BLEU drop compared to the ST baseline.

</details>

### [CTC-Assisted LLM-Based Contextual ASR](2411.06437.md)
**Guanrou Yang, Ziyang Ma, Zhifu Gao, Shiliang Zhang et al.** · 2024-11-10

<details>
<summary>Abstract</summary>

Contextual ASR or hotword customization holds substantial practical value. Despite the impressive performance of current end-to-end (E2E) automatic speech recognition (ASR) systems, they often face challenges in accurately recognizing rare words. Typical E2E contextual ASR models commonly feature complex architectures and decoding mechanisms, limited in performance and susceptible to interference from distractor words. With large language model (LLM)-based ASR models emerging as the new mainstream, we propose a CTC-Assisted LLM-Based Contextual ASR model with an efficient filtering algorithm. By using coarse CTC decoding results to filter potential relevant hotwords and incorporating them into LLM prompt input, our model attains WER/B-WER of 1.27%/3.67% and 2.72%/8.02% on the Librispeech test-clean and test-other sets targeting on recognizing rare long-tail words, demonstrating significant improvements compared to the baseline LLM-based ASR model, and substantially surpassing other related work. More remarkably, with the help of the large language model and proposed filtering algorithm, our contextual ASR model still performs well with 2000 biasing words.

</details>

### [NeKo: Cross-Modality Post-Recognition Error Correction with Tasks-Guided Mixture-of-Experts Language Model](2411.05945.md)
**Yen-Ting Lin, Zhehuai Chen, Piotr Zelasko, Zhen Wan et al.** · 2024-11-08

<details>
<summary>Abstract</summary>

Construction of a general-purpose post-recognition error corrector poses a crucial question: how can we most effectively train a model on a large mixture of domain datasets? The answer would lie in learning dataset-specific features and digesting their knowledge in a single model. Previous methods achieve this by having separate correction language models, resulting in a significant increase in parameters. In this work, we present Mixture-of-Experts as a solution, highlighting that MoEs are much more than a scalability tool. We propose a Multi-Task Correction MoE, where we train the experts to become an ``expert'' of speech-to-text, language-to-text and vision-to-text datasets by learning to route each dataset's tokens to its mapped expert. Experiments on the Open ASR Leaderboard show that we explore a new state-of-the-art performance by achieving an average relative 5.0% WER reduction and substantial improvements in BLEU scores for speech and translation tasks. On zero-shot evaluation, NeKo outperforms GPT-3.5 and Claude-Opus with 15.5% to 27.6% relative WER reduction in the Hyporadise benchmark. NeKo performs competitively on grammar and post-OCR correction as a multi-task model.

</details>

### [Multistage Fine-tuning Strategies for Automatic Speech Recognition in Low-resource Languages](2411.04573.md)
**Leena G Pillai, Kavya Manohar, Basil K Raju, Elizabeth Sherly** · 2024-11-07

<details>
<summary>Abstract</summary>

This paper presents a novel multistage fine-tuning strategy designed to enhance automatic speech recognition (ASR) performance in low-resource languages using OpenAI's Whisper model. In this approach we aim to build ASR model for languages with limited digital resources by sequentially adapting the model across linguistically similar languages. We experimented this on the Malasar language, a Dravidian language spoken by approximately ten thousand people in the Western Ghats of South India. Malasar language faces critical challenges for technological intervention due to its lack of a native script and absence of digital or spoken data resources. Working in collaboration with Wycliffe India and Malasar community members, we created a spoken Malasar corpus paired with transcription in Tamil script, a closely related major language. In our approach to build ASR model for Malasar, we first build an intermediate Tamil ASR, leveraging higher data availability for Tamil annotated speech. This intermediate model is subsequently fine-tuned on Malasar data, allowing for more effective ASR adaptation despite limited resources. The multistage fine-tuning strategy demonstrated significant improvements over direct fine-tuning on Malasar data alone, achieving a word error rate (WER) of 51.9%, which is 4.5% absolute reduction when compared to the direct fine-tuning method. Further a WER reduction to 47.3% was achieved through punctuation removal in post-processing, which addresses formatting inconsistencies that impact evaluation. Our results underscore the effectiveness of sequential multistage fine-tuning combined with targeted post-processing as a scalable strategy for ASR system development in low-resource languages, especially where linguistic similarities can be leveraged to bridge gaps in training data.

</details>

### [CUIfy the XR: An Open-Source Package to Embed LLM-powered Conversational Agents in XR](2411.04671.md)
**Kadir Burak Buldu, Süleyman Özdel, Ka Hei Carrie Lau, Mengdi Wang et al.** · 2024-11-07

<details>
<summary>Abstract</summary>

Recent developments in computer graphics, machine learning, and sensor technologies enable numerous opportunities for extended reality (XR) setups for everyday life, from skills training to entertainment. With large corporations offering affordable consumer-grade head-mounted displays (HMDs), XR will likely become pervasive, and HMDs will develop as personal devices like smartphones and tablets. However, having intelligent spaces and naturalistic interactions in XR is as important as technological advances so that users grow their engagement in virtual and augmented spaces. To this end, large language model (LLM)--powered non-player characters (NPCs) with speech-to-text (STT) and text-to-speech (TTS) models bring significant advantages over conventional or pre-scripted NPCs for facilitating more natural conversational user interfaces (CUIs) in XR. This paper provides the community with an open-source, customizable, extendable, and privacy-aware Unity package, CUIfy, that facilitates speech-based NPC-user interaction with widely used LLMs, STT, and TTS models. Our package also supports multiple LLM-powered NPCs per environment and minimizes latency between different computational models through streaming to achieve usable interactions between users and NPCs. We publish our source code in the following repository: https://gitlab.lrz.de/hctl/cuify

</details>

### [Layer-Adaptive Low-Rank Adaptation of Large ASR Model for Low-Resource Multilingual Scenarios](s2:8604c516cb12c68940e1ed0026c3a0fcf8b6ea89.md)
**Yi Han, Hang Chen, Jun Du, Changqing Kong et al.** · 2024-11-07

<details>
<summary>Abstract</summary>

Fine-tuning pre-trained ASR models is a practical approach for multilingual scenarios. Especially when facing the scarcity of annotated data, Low-Rank Adaptation (LoRA) exhibits commendable efficiency in this regard. However, when the available resources are further reduced, LoRA algorithms often suffer from severe overfitting due to the need to fine-tune all parameters, thereby compromising performance. In response to this challenge, we propose enhancing the LoRA algorithm by fine-tuning only a subset of parameters. Specifically, we introduce three manual layer selection strategies to the LoRA algorithm: Attention-Wise LoRA (AW-LoRA), Value-Output LoRA (VO-LoRA), and Rank-1 LoRA (R1-LoRA). Furthermore, we develop a Layer-Adaptive LoRA (LA-LoRA) that automatically assesses and selects critical layers based on the gradient's second moments. Experimental results on 4-hour datasets validate that our VO-LoRA achieves a comparable Word Error Rate (WER) to the raw LoRA algorithm while requiring only 27.25% parameters to be fine-tuned. The LA-LoRA algorithm further reduces the number of parameters needing fine-tuning to 10% and achieves a relative WER reduction of 1.82%. Moreover, Japanese and Korean experiments demonstrate that AW-LoRA, VO-LoRA, R1-LoRA, and LA-LoRA algorithms exhibit strong generalization capabilities across different languages. Our code is available at https://github.com/proudpie/LA-LoRA.

</details>

### [LASER: Attention with Exponential Transformation](2411.03493.md)
**Sai Surya Duvvuri, Inderjit S. Dhillon** · 2024-11-05

<details>
<summary>Abstract</summary>

Transformers have had tremendous impact for several sequence related tasks, largely due to their ability to retrieve from any part of the sequence via softmax based dot-product attention. This mechanism plays a crucial role in Transformer's performance. We analyze the gradients backpropagated through the softmax operation in the attention mechanism and observe that these gradients can often be small. This poor gradient signal backpropagation can lead to inefficient learning of parameters preceeding the attention operations. To this end, we introduce a new attention mechanism called LASER, which we analytically show to admit a larger gradient signal. We show that LASER attention can be implemented by making small modifications to existing attention implementations. We conduct experiments on autoregressive large language models (LLMs) with upto 7.7 billion parameters with an average improvement of upto 1.44% over standard attention on downstream evaluations and 1.65% finetuning improvements. Additionally, LASER demonstrates generalization performance improvement across a variety of tasks (vision, text and speech):Vision Transformer (ViT) on Imagenet, Conformer on the Librispeech speech-to-text and BERT with 2.2 billion parameters.

</details>

### [Unified Speech Recognition: A Single Model for Auditory, Visual, and Audiovisual Inputs](2411.02256.md)
**Alexandros Haliassos, Rodrigo Mira, Honglie Chen, Zoe Landgraf et al.** · 2024-11-04

<details>
<summary>Abstract</summary>

Research in auditory, visual, and audiovisual speech recognition (ASR, VSR, and AVSR, respectively) has traditionally been conducted independently. Even recent self-supervised studies addressing two or all three tasks simultaneously tend to yield separate models, leading to disjoint inference pipelines with increased memory requirements and redundancies. This paper proposes unified training strategies for these systems. We demonstrate that training a single model for all three tasks enhances VSR and AVSR performance, overcoming typical optimisation challenges when training from scratch. Moreover, we introduce a greedy pseudo-labelling approach to more effectively leverage unlabelled samples, addressing shortcomings in related self-supervised methods. Finally, we develop a self-supervised pre-training method within our framework, proving its effectiveness alongside our semi-supervised approach. Despite using a single model for all tasks, our unified approach achieves state-of-the-art performance compared to recent methods on LRS3 and LRS2 for ASR, VSR, and AVSR, as well as on the newly released WildVSR dataset. Code and models are available at https://github.com/ahaliassos/usr.

</details>

### [Enhancing AAC Software for Dysarthric Speakers in e-Health Settings: An Evaluation Using TORGO](2411.00980.md)
**Macarious Hui, Jinda Zhang, Aanchan Mohan** · 2024-11-01

<details>
<summary>Abstract</summary>

Individuals with cerebral palsy (CP) and amyotrophic lateral sclerosis (ALS) frequently face challenges with articulation, leading to dysarthria and resulting in atypical speech patterns. In healthcare settings, communication breakdowns reduce the quality of care. While building an augmentative and alternative communication (AAC) tool to enable fluid communication we found that state-of-the-art (SOTA) automatic speech recognition (ASR) technology like Whisper and Wav2vec2.0 marginalizes atypical speakers largely due to the lack of training data. Our work looks to leverage SOTA ASR followed by domain specific error-correction. English dysarthric ASR performance is often evaluated on the TORGO dataset. Prompt-overlap is a well-known issue with this dataset where phrases overlap between training and test speakers. Our work proposes an algorithm to break this prompt-overlap. After reducing prompt-overlap, results with SOTA ASR models produce extremely high word error rates for speakers with mild and severe dysarthria. Furthermore, to improve ASR, our work looks at the impact of n-gram language models and large-language model (LLM) based multi-modal generative error-correction algorithms like Whispering-LLaMA for a second pass ASR. Our work highlights how much more needs to be done to improve ASR for atypical speakers to enable equitable healthcare access both in-person and in e-health settings.

</details>

### [Optimizing Contextual Speech Recognition Using Vector Quantization for Efficient Retrieval](2411.00664.md)
**Nikolaos Flemotomos, Roger Hsiao, Pawel Swietojanski, Takaaki Hori et al.** · 2024-11-01

<details>
<summary>Abstract</summary>

Neural contextual biasing allows speech recognition models to leverage contextually relevant information, leading to improved transcription accuracy. However, the biasing mechanism is typically based on a cross-attention module between the audio and a catalogue of biasing entries, which means computational complexity can pose severe practical limitations on the size of the biasing catalogue and consequently on accuracy improvements. This work proposes an approximation to cross-attention scoring based on vector quantization and enables compute- and memory-efficient use of large biasing catalogues. We propose to use this technique jointly with a retrieval based contextual biasing approach. First, we use an efficient quantized retrieval module to shortlist biasing entries by grounding them on audio. Then we use retrieved entries for biasing. Since the proposed approach is agnostic to the biasing method, we investigate using full cross-attention, LLM prompting, and a combination of the two. We show that retrieval based shortlisting allows the system to efficiently leverage biasing catalogues of several thousands of entries, resulting in up to 71% relative error rate reduction in personal entity recognition. At the same time, the proposed approximation algorithm reduces compute time by 20% and memory usage by 85-95%, for lists of up to one million entries, when compared to standard dot-product cross-attention.

</details>

### [IO Transformer: Evaluating SwinV2-Based Reward Models for Computer Vision](2411.00252.md)
**Maxwell Meyer, Jack Spruyt** · 2024-10-31

<details>
<summary>Abstract</summary>

Transformers and their derivatives have achieved state-of-the-art performance across text, vision, and speech recognition tasks. However, minimal effort has been made to train transformers capable of evaluating the output quality of other models. This paper examines SwinV2-based reward models, called the Input-Output Transformer (IO Transformer) and the Output Transformer. These reward models can be leveraged for tasks such as inference quality evaluation, data categorization, and policy optimization. Our experiments demonstrate highly accurate model output quality assessment across domains where the output is entirely dependent on the input, with the IO Transformer achieving perfect evaluation accuracy on the Change Dataset 25 (CD25). We also explore modified Swin V2 architectures. Ultimately Swin V2 remains on top with a score of 95.41 % on the IO Segmentation Dataset, outperforming the IO Transformer in scenarios where the output is not entirely dependent on the input. Our work expands the application of transformer architectures to reward modeling in computer vision and provides critical insights into optimizing these models for various tasks.

</details>

### [Speech is More Than Words: Do Speech-to-Text Translation Systems Leverage Prosody?](2410.24019.md)
**Ioannis Tsiamas, Matthias Sperber, Andrew Finch, Sarthak Garg** · 2024-10-31

<details>
<summary>Abstract</summary>

The prosody of a spoken utterance, including features like stress, intonation and rhythm, can significantly affect the underlying semantics, and as a consequence can also affect its textual translation. Nevertheless, prosody is rarely studied within the context of speech-to-text translation (S2TT) systems. In particular, end-to-end (E2E) systems have been proposed as well-suited for prosody-aware translation because they have direct access to the speech signal when making translation decisions, but the understanding of whether this is successful in practice is still limited. A main challenge is the difficulty of evaluating prosody awareness in translation. To address this challenge, we introduce an evaluation methodology and a focused benchmark (named ContraProST) aimed at capturing a wide range of prosodic phenomena. Our methodology uses large language models and controllable text-to-speech (TTS) to generate contrastive examples. Through experiments in translating English speech into German, Spanish, and Japanese, we find that (a) S2TT models possess some internal representation of prosody, but the prosody signal is often not strong enough to affect the translations, (b) E2E systems outperform cascades of speech recognition and text translation systems, confirming their theoretical advantage in this regard, and (c) certain cascaded systems also capture prosodic information in the translation, but only to a lesser extent that depends on the particulars of the transcript's surface form.

</details>

### [Run-Time Adaptation of Neural Beamforming for Robust Speech Dereverberation and Denoising](2410.22805.md)
**Yoto Fujita, Aditya Arie Nugraha, Diego Di Carlo, Yoshiaki Bando et al.** · 2024-10-30

<details>
<summary>Abstract</summary>

This paper describes speech enhancement for realtime automatic speech recognition (ASR) in real environments. A standard approach to this task is to use neural beamforming that can work efficiently in an online manner. It estimates the masks of clean dry speech from a noisy echoic mixture spectrogram with a deep neural network (DNN) and then computes a enhancement filter used for beamforming. The performance of such a supervised approach, however, is drastically degraded under mismatched conditions. This calls for run-time adaptation of the DNN. Although the ground-truth speech spectrogram required for adaptation is not available at run time, blind dereverberation and separation methods such as weighted prediction error (WPE) and fast multichannel nonnegative matrix factorization (FastMNMF) can be used for generating pseudo groundtruth data from a mixture. Based on this idea, a prior work proposed a dual-process system based on a cascade of WPE and minimum variance distortionless response (MVDR) beamforming asynchronously fine-tuned by block-online FastMNMF. To integrate the dereverberation capability into neural beamforming and make it fine-tunable at run time, we propose to use weighted power minimization distortionless response (WPD) beamforming, a unified version of WPE and minimum power distortionless response (MPDR), whose joint dereverberation and denoising filter is estimated using a DNN. We evaluated the impact of run-time adaptation under various conditions with different numbers of speakers, reverberation times, and signal-to-noise ratios (SNRs).

</details>

### [Joint Beamforming and Speaker-Attributed ASR for Real Distant-Microphone Meeting Transcription](2410.21849.md)
**Can Cui, Imran Ahamad Sheikh, Mostafa Sadeghi, Emmanuel Vincent** · 2024-10-29

<details>
<summary>Abstract</summary>

Distant-microphone meeting transcription is a challenging task. State-of-the-art end-to-end speaker-attributed automatic speech recognition (SA-ASR) architectures lack a multichannel noise and reverberation reduction front-end, which limits their performance. In this paper, we introduce a joint beamforming and SA-ASR approach for real meeting transcription. We first describe a data alignment and augmentation method to pretrain a neural beamformer on real meeting data. We then compare fixed, hybrid, and fully neural beamformers as front-ends to the SA-ASR model. Finally, we jointly optimize the fully neural beamformer and the SA-ASR model. Experiments on the real AMI corpus show that, while state-of-the-art multi-frame cross-channel attention based channel fusion fails to improve ASR performance, fine-tuning SA-ASR on the fixed beamformer's output and jointly fine-tuning SA-ASR with the neural beamformer reduce the word error rate by 8% and 9% relative, respectively.

</details>

### [emg2qwerty: A Large Dataset with Baselines for Touch Typing using Surface Electromyography](2410.20081.md)
**Viswanath Sivakumar, Jeffrey Seely, Alan Du, Sean R Bittner et al.** · 2024-10-26

<details>
<summary>Abstract</summary>

Surface electromyography (sEMG) non-invasively measures signals generated by muscle activity with sufficient sensitivity to detect individual spinal neurons and richness to identify dozens of gestures and their nuances. Wearable wrist-based sEMG sensors have the potential to offer low friction, subtle, information rich, always available human-computer inputs. To this end, we introduce emg2qwerty, a large-scale dataset of non-invasive electromyographic signals recorded at the wrists while touch typing on a QWERTY keyboard, together with ground-truth annotations and reproducible baselines. With 1,135 sessions spanning 108 users and 346 hours of recording, this is the largest such public dataset to date. These data demonstrate non-trivial, but well defined hierarchical relationships both in terms of the generative process, from neurons to muscles and muscle combinations, as well as in terms of domain shift across users and user sessions. Applying standard modeling techniques from the closely related field of Automatic Speech Recognition (ASR), we show strong baseline performance on predicting key-presses using sEMG signals alone. We believe the richness of this task and dataset will facilitate progress in several problems of interest to both the machine learning and neuroscientific communities. Dataset and code can be accessed at https://github.com/facebookresearch/emg2qwerty.

</details>

### [kNN For Whisper And Its Effect On Bias And Speaker Adaptation](2410.18850.md)
**Maya K. Nachesa, Vlad Niculae** · 2024-10-24

<details>
<summary>Abstract</summary>

Speech recognition performance varies by language, domain, and speaker characteristics such as accent, but fine-tuning a model on any of these categories may lead to catastrophic forgetting. Token-level $k$ nearest neighbor search ($k$NN), first proposed for neural sequence decoders for natural language generation (NLG) and machine translation (MT), is a non-parametric method that instead adapts using inference-time search in an external datastore, without training the underlying model. We show that Whisper, a transformer end-to-end speech model, benefits from $k$NN. We investigate the differences between the speech and text setups. We discuss implications for speaker adaptation, and analyze improvements by gender, accent, and age.

</details>

### [Contextual Biasing to Improve Domain-specific Custom Vocabulary Audio Transcription without Explicit Fine-Tuning of Whisper Model](2410.18363.md)
**Vishakha Lall, Yisi Liu** · 2024-10-24

<details>
<summary>Abstract</summary>

OpenAI's Whisper Automated Speech Recognition model excels in generalizing across diverse datasets and domains. However, this broad adaptability can lead to diminished performance in tasks requiring recognition of specific vocabularies. Addressing this challenge typically involves fine-tuning the model, which demands extensive labeled audio data that is often difficult to acquire and unavailable for specific domains. In this study, we propose a method to enhance transcription accuracy without explicit fine-tuning or altering model parameters, using a relatively small training dataset. Our method leverages contextual biasing, to direct Whisper model's output towards a specific vocabulary by integrating a neural-symbolic prefix tree structure to guide the model's transcription output. To validate our approach, we conducted experiments using a validation dataset comprising maritime data collected within a simulated training environment. A comparison between the original Whisper models of varying parameter sizes and our biased model revealed a notable reduction in transcription word error rate and enhanced performance of downstream applications. Our findings suggest that this methodology holds promise for improving speech-to-text translation performance in domains characterized by limited vocabularies.

</details>

### [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](2410.17485.md)
**Yifan Peng, Krishna C. Puvvada, Zhehuai Chen, Piotr Zelasko et al.** · 2024-10-23

<details>
<summary>Abstract</summary>

Recent studies have augmented large language models (LLMs) with speech capabilities, leading to the development of speech language models (SpeechLMs). Earlier SpeechLMs focused on single-turn speech-based question answering (QA), where user input comprised a speech context and a text question. More recent studies have extended this to multi-turn conversations, though they often require complex, multi-stage supervised fine-tuning (SFT) with diverse data. Another critical challenge with SpeechLMs is catastrophic forgetting, where models optimized for speech tasks suffer significant degradation in text-only performance. To mitigate these issues, we propose a novel single-stage joint speech-text SFT approach on the low-rank adaptation (LoRA) of the LLM backbone. Our joint SFT combines text-only SFT data with three types of speech-related data: speech recognition and translation, speech-based QA, and mixed-modal SFT. Compared to previous SpeechLMs with 7B or 13B parameters, our 3B model demonstrates superior performance across various speech benchmarks while preserving the original capabilities on text-only tasks. Furthermore, our model shows emergent abilities of effectively handling previously unseen prompts and tasks, including multi-turn, mixed-modal inputs.

</details>

### [Improving Automatic Speech Recognition with Decoder-Centric Regularisation in Encoder-Decoder Models](2410.17437.md)
**Alexander Polok, Santosh Kesiraju, Karel Beneš, Lukáš Burget et al.** · 2024-10-22

<details>
<summary>Abstract</summary>

This paper proposes a simple yet effective way of regularising the encoder-decoder-based automatic speech recognition (ASR) models that enhance the robustness of the model and improve the generalisation to out-of-domain scenarios. The proposed approach is dubbed as $\textbf{De}$coder-$\textbf{C}$entric $\textbf{R}$egularisation in $\textbf{E}$ncoder-$\textbf{D}$ecoder (DeCRED) architecture for ASR, where auxiliary classifier(s) is introduced in layers of the decoder module. Leveraging these classifiers, we propose two decoding strategies that re-estimate the next token probabilities. Using the recent E-branchformer architecture, we build strong ASR systems that obtained competitive WERs as compared to Whisper-medium and outperformed OWSM v3; while relying only on a fraction of training data and model size. On top of such a strong baseline, we show that DeCRED can further improve the results and, moreover, generalise much better to out-of-domain scenarios, where we show an absolute reduction of 2.7 and 2.9 WERs on AMI and Gigaspeech datasets, respectively. We provide extensive analysis and accompanying experiments that support the benefits of the proposed regularisation scheme.

</details>

### [AlignVSR: Audio-Visual Cross-Modal Alignment for Visual Speech Recognition](2410.16438.md)
**Zehua Liu, Xiaolou Li, Chen Chen, Li Guo et al.** · 2024-10-21

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) aims to recognize corresponding text by analyzing visual information from lip movements. Due to the high variability and weak information of lip movements, VSR tasks require effectively utilizing any information from any source and at any level. In this paper, we propose a VSR method based on audio-visual cross-modal alignment, named AlignVSR. The method leverages the audio modality as an auxiliary information source and utilizes the global and local correspondence between the audio and visual modalities to improve visual-to-text inference. Specifically, the method first captures global alignment between video and audio through a cross-modal attention mechanism from video frames to a bank of audio units. Then, based on the temporal correspondence between audio and video, a frame-level local alignment loss is introduced to refine the global alignment, improving the utility of the audio information. Experimental results on the LRS2 and CNVSRC.Single datasets consistently show that AlignVSR outperforms several mainstream VSR methods, demonstrating its superior and robust performance.

</details>

### [Acoustic Model Optimization over Multiple Data Sources: Merging and Valuation](2410.15620.md)
**Victor Junqiu Wei, Weicheng Wang, Di Jiang, Conghui Tan et al.** · 2024-10-21

<details>
<summary>Abstract</summary>

Due to the rising awareness of privacy protection and the voluminous scale of speech data, it is becoming infeasible for Automatic Speech Recognition (ASR) system developers to train the acoustic model with complete data as before. For example, the data may be owned by different curators, and it is not allowed to share with others. In this paper, we propose a novel paradigm to solve salient problems plaguing the ASR field. In the first stage, multiple acoustic models are trained based upon different subsets of the complete speech data, while in the second phase, two novel algorithms are utilized to generate a high-quality acoustic model based upon those trained on data subsets. We first propose the Genetic Merge Algorithm (GMA), which is a highly specialized algorithm for optimizing acoustic models but suffers from low efficiency. We further propose the SGD-Based Optimizational Merge Algorithm (SOMA), which effectively alleviates the efficiency bottleneck of GMA and maintains superior model accuracy. Extensive experiments on public data show that the proposed methods can significantly outperform the state-of-the-art. Furthermore, we introduce Shapley Value to estimate the contribution score of the trained models, which is useful for evaluating the effectiveness of the data and providing fair incentives to their curators.

</details>

### [Moonshine: Speech Recognition for Live Transcription and Voice Commands](2410.15608.md)
**Nat Jeffries, Evan King, Manjunath Kudlur, Guy Nicholson et al.** · 2024-10-21

<details>
<summary>Abstract</summary>

This paper introduces Moonshine, a family of speech recognition models optimized for live transcription and voice command processing. Moonshine is based on an encoder-decoder transformer architecture and employs Rotary Position Embedding (RoPE) instead of traditional absolute position embeddings. The model is trained on speech segments of various lengths, but without using zero-padding, leading to greater efficiency for the encoder during inference time. When benchmarked against OpenAI's Whisper tiny-en, Moonshine Tiny demonstrates a 5x reduction in compute requirements for transcribing a 10-second speech segment while incurring no increase in word error rates across standard evaluation datasets. These results highlight Moonshine's potential for real-time and resource-constrained applications.

</details>

### [Ichigo: Mixed-Modal Early-Fusion Realtime Voice Assistant](2410.15316.md)
**Alan Dao, Dinh Bach Vu, Huy Hoang Ha** · 2024-10-20

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have revolutionized natural language processing, but their application to speech-based tasks remains challenging due to the complexities of integrating audio and text modalities. This paper introduces Ichigo, a mixed-modal model that seamlessly processes interleaved sequences of speech and text. Utilizing a tokenized early-fusion approach, Ichigo quantizes speech into discrete tokens and employs a uniform transformer-based architecture for both speech and text modalities. This method enables joint reasoning and generation across modalities without the need for separate adapters. We present a comprehensive training methodology, including pre-training on multilingual speech recognition datasets and fine-tuning on a curated instruction dataset. Ichigo demonstrates state-of-the-art performance on speech question-answering benchmarks, outperforming existing open-source speech language models and achieving comparable results to cascaded systems. Notably, Ichigo exhibits a latency of just 111 ms to first token generation, significantly lower than current models. Our approach not only advances the field of multimodal AI but also provides a framework for smaller research teams to contribute effectively to open-source speech-language models.

</details>

### [End-to-End Transformer-based Automatic Speech Recognition for Northern Kurdish: A Pioneering Approach](2410.16330.md)
**Abdulhady Abas Abdullah, Shima Tabibian, Hadi Veisi, Aso Mahmudi et al.** · 2024-10-19

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) for low-resource languages remains a challenging task due to limited training data. This paper introduces a comprehensive study exploring the effectiveness of Whisper, a pre-trained ASR model, for Northern Kurdish (Kurmanji) an under-resourced language spoken in the Middle East. We investigate three fine-tuning strategies: vanilla, specific parameters, and additional modules. Using a Northern Kurdish fine-tuning speech corpus containing approximately 68 hours of validated transcribed data, our experiments demonstrate that the additional module fine-tuning strategy significantly improves ASR accuracy on a specialized test set, achieving a Word Error Rate (WER) of 10.5% and Character Error Rate (CER) of 5.7% with Whisper version 3. These results underscore the potential of sophisticated transformer models for low-resource ASR and emphasize the importance of tailored fine-tuning techniques for optimal performance.

</details>

### [Enhancing Multimodal Sentiment Analysis for Missing Modality through Self-Distillation and Unified Modality Cross-Attention](2410.15029.md)
**Yuzhe Weng, Haotian Wang, Tian Gao, Kewei Li et al.** · 2024-10-19

<details>
<summary>Abstract</summary>

In multimodal sentiment analysis, collecting text data is often more challenging than video or audio due to higher annotation costs and inconsistent automatic speech recognition (ASR) quality. To address this challenge, our study has developed a robust model that effectively integrates multimodal sentiment information, even in the absence of text modality. Specifically, we have developed a Double-Flow Self-Distillation Framework, including Unified Modality Cross-Attention (UMCA) and Modality Imagination Autoencoder (MIA), which excels at processing both scenarios with complete modalities and those with missing text modality. In detail, when the text modality is missing, our framework uses the LLM-based model to simulate the text representation from the audio modality, while the MIA module supplements information from the other two modalities to make the simulated text representation similar to the real text representation. To further align the simulated and real representations, and to enable the model to capture the continuous nature of sample orders in sentiment valence regression tasks, we have also introduced the Rank-N Contrast (RNC) loss function. When testing on the CMU-MOSEI, our model achieved outstanding performance on MAE and significantly outperformed other models when text modality is missing. The code is available at: https://github.com/WarmCongee/SDUMC

</details>

### [DM-Codec: Distilling Multimodal Representations for Speech Tokenization](2410.15017.md)
**Md Mubtasim Ahasan, Md Fahim, Tasnim Mohiuddin, A K M Mahbubur Rahman et al.** · 2024-10-19

<details>
<summary>Abstract</summary>

Recent advancements in speech-language models have yielded significant improvements in speech tokenization and synthesis. However, effectively mapping the complex, multidimensional attributes of speech into discrete tokens remains challenging. This process demands acoustic, semantic, and contextual information for precise speech representations. Existing speech representations generally fall into two categories: acoustic tokens from audio codecs and semantic tokens from speech self-supervised learning models. Although recent efforts have unified acoustic and semantic tokens for improved performance, they overlook the crucial role of contextual representation in comprehensive speech modeling. Our empirical investigations reveal that the absence of contextual representations results in elevated Word Error Rate (WER) and Word Information Lost (WIL) scores in speech transcriptions. To address these limitations, we propose two novel distillation approaches: (1) a language model (LM)-guided distillation method that incorporates contextual information, and (2) a combined LM and self-supervised speech model (SM)-guided distillation technique that effectively distills multimodal representations (acoustic, semantic, and contextual) into a comprehensive speech tokenizer, termed DM-Codec. The DM-Codec architecture adopts a streamlined encoder-decoder framework with a Residual Vector Quantizer (RVQ) and incorporates the LM and SM during the training process. Experiments show DM-Codec significantly outperforms state-of-the-art speech tokenization models, reducing WER by up to 13.46%, WIL by 9.82%, and improving speech quality by 5.84% and intelligibility by 1.85% on the LibriSpeech benchmark dataset. Code, samples, and checkpoints are available at https://github.com/mubtasimahasan/DM-Codec.

</details>

### [AC-Mix: Self-Supervised Adaptation for Low-Resource Automatic Speech Recognition using Agnostic Contrastive Mixup](2410.14910.md)
**Carlos Carvalho, Alberto Abad** · 2024-10-18

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) leverages large amounts of unlabelled data to learn rich speech representations, fostering improvements in automatic speech recognition (ASR), even when only a small amount of labelled data is available for fine-tuning. Despite the advances in SSL, a significant challenge remains when the data used for pre-training (source domain) mismatches the fine-tuning data (target domain). To tackle this domain mismatch challenge, we propose a new domain adaptation method for low-resource ASR focused on contrastive mixup for joint-embedding architectures named AC-Mix (agnostic contrastive mixup). In this approach, the SSL model is adapted through additional pre-training using mixed data views created by interpolating samples from the source and the target domains. Our proposed adaptation method consistently outperforms the baseline system, using approximately 11 hours of adaptation data and requiring only 1 hour of adaptation time on a single GPU with WavLM-Large.

</details>

### [Endpoint Detection for Streaming ASR with Phoneme Modeling](s2:2529e665af463f96b65d5132142c77fe8731db33.md)
**Zhiwei Xie, Chengcheng He, Yanbing Li, Wushouer Silamu** · 2024-10-18

<details>
<summary>Abstract</summary>

Endpoint detection in speech recognition identifies when a natural sentence stops during recognition. Recent research on integrating endpoint detection and speech recognition into a single streaming ASR model is limited, with past methods often having high detection latency due to coarse modeling granularity. Therefore, we propose using phoneme information to model endpoint detection to assist the speech recognition system, achieving lower latency in endpoint detection for RNN-T-based streaming ASR systems. Validation on end-to-end endpoint detection-oriented speech recognition tasks shows that, compared to baseline methods, the phoneme-branch-based ASR system significantly reduces endpoint detection latency, improves coverage, and maintains speech recognition performance at the cost of only a slight increase in parameters and real-time factor.

</details>

### [Parameter-efficient Adaptation of Multilingual Multimodal Models for Low-resource ASR](2410.13445.md)
**Abhishek Gupta, Amruta Parulekar, Sameep Chattopadhyay, Preethi Jyothi** · 2024-10-17

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for low-resource languages remains a challenge due to the scarcity of labeled training data. Parameter-efficient fine-tuning and text-only adaptation are two popular methods that have been used to address such low-resource settings. In this work, we investigate how these techniques can be effectively combined using a multilingual multimodal model like SeamlessM4T. Multimodal models are able to leverage unlabeled text via text-only adaptation with further parameter-efficient ASR fine-tuning, thus boosting ASR performance. We also show cross-lingual transfer from a high-resource language, achieving up to a relative 17% WER reduction over a baseline in a zero-shot setting without any labeled speech.

</details>

### [Computational Approaches to Arabic-English Code-Switching](2410.13318.md)
**Caroline Sabty** · 2024-10-17

<details>
<summary>Abstract</summary>

Natural Language Processing (NLP) is a vital computational method for addressing language processing, analysis, and generation. NLP tasks form the core of many daily applications, from automatic text correction to speech recognition. While significant research has focused on NLP tasks for the English language, less attention has been given to Modern Standard Arabic and Dialectal Arabic. Globalization has also contributed to the rise of Code-Switching (CS), where speakers mix languages within conversations and even within individual words (intra-word CS). This is especially common in Arab countries, where people often switch between dialects or between dialects and a foreign language they master. CS between Arabic and English is frequent in Egypt, especially on social media. Consequently, a significant amount of code-switched content can be found online. Such code-switched data needs to be investigated and analyzed for several NLP tasks to tackle the challenges of this multilingual phenomenon and Arabic language challenges. No work has been done before for several integral NLP tasks on Arabic-English CS data. In this work, we focus on the Named Entity Recognition (NER) task and other tasks that help propose a solution for the NER task on CS data, e.g., Language Identification. This work addresses this gap by proposing and applying state-of-the-art techniques for Modern Standard Arabic and Arabic-English NER. We have created the first annotated CS Arabic-English corpus for the NER task. Also, we apply two enhancement techniques to improve the NER tagger on CS data using CS contextual embeddings and data augmentation techniques. All methods showed improvements in the performance of the NER taggers on CS data. Finally, we propose several intra-word language identification approaches to determine the language type of a mixed text and identify whether it is a named entity or not.

</details>

### [Roadmap towards Superhuman Speech Understanding using Large Language Models](2410.13268.md)
**Fan Bu, Yuhao Zhang, Xidong Wang, Benyou Wang et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

The success of large language models (LLMs) has prompted efforts to integrate speech and audio data, aiming to create general foundation models capable of processing both textual and non-textual inputs. Recent advances, such as GPT-4o, highlight the potential for end-to-end speech LLMs, which preserves non-semantic information and world knowledge for deeper speech understanding. To guide the development of speech LLMs, we propose a five-level roadmap, ranging from basic automatic speech recognition (ASR) to advanced superhuman models capable of integrating non-semantic information with abstract acoustic knowledge for complex tasks. Moreover, we design a benchmark, SAGI Bechmark, that standardizes critical aspects across various tasks in these five levels, uncovering challenges in using abstract acoustic knowledge and completeness of capability. Our findings reveal gaps in handling paralinguistic cues and abstract acoustic knowledge, and we offer future directions. This paper outlines a roadmap for advancing speech LLMs, introduces a benchmark for evaluation, and provides key insights into their current limitations and potential.

</details>

### [Failing Forward: Improving Generative Error Correction for ASR with Synthetic Data and Retrieval Augmentation](2410.13198.md)
**Sreyan Ghosh, Mohammad Sadegh Rasooli, Michael Levit, Peidong Wang et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

Generative Error Correction (GEC) has emerged as a powerful post-processing method to enhance the performance of Automatic Speech Recognition (ASR) systems. However, we show that GEC models struggle to generalize beyond the specific types of errors encountered during training, limiting their ability to correct new, unseen errors at test time, particularly in out-of-domain (OOD) scenarios. This phenomenon amplifies with named entities (NEs), where, in addition to insufficient contextual information or knowledge about the NEs, novel NEs keep emerging. To address these issues, we propose DARAG (Data- and Retrieval-Augmented Generative Error Correction), a novel approach designed to improve GEC for ASR in in-domain (ID) and OOD scenarios. We augment the GEC training dataset with synthetic data generated by prompting LLMs and text-to-speech models, thereby simulating additional errors from which the model can learn. For OOD scenarios, we simulate test-time errors from new domains similarly and in an unsupervised fashion. Additionally, to better handle named entities, we introduce retrieval-augmented correction by augmenting the input with entities retrieved from a database. Our approach is simple, scalable, and both domain- and language-agnostic. We experiment on multiple datasets and settings, showing that DARAG outperforms all our baselines, achieving 8\% -- 30\% relative WER improvements in ID and 10\% -- 33\% improvements in OOD settings.

</details>

### [EH-MAM: Easy-to-Hard Masked Acoustic Modeling for Self-Supervised Speech Representation Learning](2410.13179.md)
**Ashish Seth, Ramaneswaran Selvakumar, S Sakshi, Sonal Kumar et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

In this paper, we present EH-MAM (Easy-to-Hard adaptive Masked Acoustic Modeling), a novel self-supervised learning approach for speech representation learning. In contrast to the prior methods that use random masking schemes for Masked Acoustic Modeling (MAM), we introduce a novel selective and adaptive masking strategy. Specifically, during SSL training, we progressively introduce harder regions to the model for reconstruction. Our approach automatically selects hard regions and is built on the observation that the reconstruction loss of individual frames in MAM can provide natural signals to judge the difficulty of solving the MAM pre-text task for that frame. To identify these hard regions, we employ a teacher model that first predicts the frame-wise losses and then decides which frames to mask. By learning to create challenging problems, such as identifying harder frames and solving them simultaneously, the model is able to learn more effective representations and thereby acquire a more comprehensive understanding of the speech. Quantitatively, EH-MAM outperforms several state-of-the-art baselines across various low-resource speech recognition and SUPERB benchmarks by 5%-10%. Additionally, we conduct a thorough analysis to show that the regions masked by EH-MAM effectively capture useful context across speech frames.

</details>

### [Deep Learning-based Software Engineering: Progress, Challenges, and Opportunities](2410.13110.md)
**Xiangping Chen, Xing Hu, Yuan Huang, He Jiang et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

Researchers have recently achieved significant advances in deep learning techniques, which in turn has substantially advanced other research disciplines, such as natural language processing, image processing, speech recognition, and software engineering. Various deep learning techniques have been successfully employed to facilitate software engineering tasks, including code generation, software refactoring, and fault localization. Many papers have also been presented in top conferences and journals, demonstrating the applications of deep learning techniques in resolving various software engineering tasks. However, although several surveys have provided overall pictures of the application of deep learning techniques in software engineering, they focus more on learning techniques, that is, what kind of deep learning techniques are employed and how deep models are trained or fine-tuned for software engineering tasks. We still lack surveys explaining the advances of subareas in software engineering driven by deep learning techniques, as well as challenges and opportunities in each subarea. To this end, in this paper, we present the first task-oriented survey on deep learning-based software engineering. It covers twelve major software engineering subareas significantly impacted by deep learning techniques. Such subareas spread out the through the whole lifecycle of software development and maintenance, including requirements engineering, software development, testing, maintenance, and developer collaboration. As we believe that deep learning may provide an opportunity to revolutionize the whole discipline of software engineering, providing one survey covering as many subareas as possible in software engineering can help future research push forward the frontier of deep learning-based software engineering more systematically.

</details>

### [STCON System for the CHiME-8 Challenge](2410.13411.md)
**Anton Mitrofanov, Tatiana Prisyach, Tatiana Timofeeva, Sergei Novoselov et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

This paper describes the STCON system for the CHiME-8 Challenge Task 1 (DASR) aimed at distant automatic speech transcription and diarization with multiple recording devices. Our main attention was paid to carefully trained and tuned diarization pipeline and speaker counting. This allowed to significantly reduce diarization error rate (DER) and obtain more reliable segments for speech separation and recognition. To improve source separation, we designed a Guided Target speaker Extraction (G-TSE) model and used it in conjunction with the traditional Guided Source Separation (GSS) method. To train various parts of our pipeline, we investigated several data augmentation and generation techniques, which helped us to improve the overall system quality.

</details>

### [A Framework for Adapting Human-Robot Interaction to Diverse User Groups](2410.11377.md)
**Theresa Pekarek Rosin, Vanessa Hassouna, Xiaowen Sun, Luca Krohm et al.** · 2024-10-15

<details>
<summary>Abstract</summary>

To facilitate natural and intuitive interactions with diverse user groups in real-world settings, social robots must be capable of addressing the varying requirements and expectations of these groups while adapting their behavior based on user feedback. While previous research often focuses on specific demographics, we present a novel framework for adaptive Human-Robot Interaction (HRI) that tailors interactions to different user groups and enables individual users to modulate interactions through both minor and major interruptions. Our primary contributions include the development of an adaptive, ROS-based HRI framework with an open-source code base. This framework supports natural interactions through advanced speech recognition and voice activity detection, and leverages a large language model (LLM) as a dialogue bridge. We validate the efficiency of our framework through module tests and system trials, demonstrating its high accuracy in age recognition and its robustness to repeated user inputs and plan changes.

</details>

### [Evolutionary Retrofitting](2410.11330.md)
**Mathurin Videau, Mariia Zameshina, Alessandro Leite, Laurent Najman et al.** · 2024-10-15

<details>
<summary>Abstract</summary>

AfterLearnER (After Learning Evolutionary Retrofitting) consists in applying evolutionary optimization to refine fully trained machine learning models by optimizing a set of carefully chosen parameters or hyperparameters of the model, with respect to some actual, exact, and hence possibly non-differentiable error signal, performed on a subset of the standard validation set. The efficiency of AfterLearnER is demonstrated by tackling non-differentiable signals such as threshold-based criteria in depth sensing, the word error rate in speech re-synthesis, the number of kills per life at Doom, computational accuracy or BLEU in code translation, image quality in 3D generative adversarial networks (GANs), and user feedback in image generation via Latent Diffusion Models (LDM). This retrofitting can be done after training, or dynamically at inference time by taking into account the user feedback. The advantages of AfterLearnER are its versatility, the possibility to use non-differentiable feedback, including human evaluations (i.e., no gradient is needed), the limited overfitting supported by a theoretical study, and its anytime behavior. Last but not least, AfterLearnER requires only a small amount of feedback, i.e., a few dozen to a few hundred scalars, compared to the tens of thousands needed in most related published works.

</details>

### [In-Materia Speech Recognition](2410.10434.md)
**Mohamadreza Zolfagharinejad, Julian Büchel, Lorenzo Cassola, Sachin Kinge et al.** · 2024-10-14

<details>
<summary>Abstract</summary>

With the rise of decentralized computing, as in the Internet of Things, autonomous driving, and personalized healthcare, it is increasingly important to process time-dependent signals at the edge efficiently: right at the place where the temporal data are collected, avoiding time-consuming, insecure, and costly communication with a centralized computing facility (or cloud). However, modern-day processors often cannot meet the restrained power and time budgets of edge systems because of intrinsic limitations imposed by their architecture (von Neumann bottleneck) or domain conversions (analogue-to-digital and time-to-frequency). Here, we propose an edge temporal-signal processor based on two in-materia computing systems for both feature extraction and classification, reaching a software-level accuracy of 96.2% for the TI-46-Word speech-recognition task. First, a nonlinear, room-temperature dopant-network-processing-unit (DNPU) layer realizes analogue, time-domain feature extraction from the raw audio signals, similar to the human cochlea. Second, an analogue in-memory computing (AIMC) chip, consisting of memristive crossbar arrays, implements a compact neural network trained on the extracted features for classification. With the DNPU feature extraction consuming 100s nW and AIMC-based classification having the potential for less than 10 fJ per multiply-accumulate operation, our findings offer a promising avenue for advancing the compactness, efficiency, and performance of heterogeneous smart edge processors through in-materia computing hardware.

</details>

### [SLAM-AAC: Enhancing Audio Captioning with Paraphrasing Augmentation and CLAP-Refine through LLMs](2410.09503.md)
**Wenxi Chen, Ziyang Ma, Xiquan Li, Xuenan Xu et al.** · 2024-10-12

<details>
<summary>Abstract</summary>

Automated Audio Captioning (AAC) aims to generate natural textual descriptions for input audio signals. Recent progress in audio pre-trained models and large language models (LLMs) has significantly enhanced audio understanding and textual reasoning capabilities, making improvements in AAC possible. In this paper, we propose SLAM-AAC to further enhance AAC with paraphrasing augmentation and CLAP-Refine through LLMs. Our approach uses the self-supervised EAT model to extract fine-grained audio representations, which are then aligned with textual embeddings via lightweight linear layers. The caption generation LLM is efficiently fine-tuned using the LoRA adapter. Drawing inspiration from the back-translation method in machine translation, we implement paraphrasing augmentation to expand the Clotho dataset during pre-training. This strategy helps alleviate the limitation of scarce audio-text pairs and generates more diverse captions from a small set of audio clips. During inference, we introduce the plug-and-play CLAP-Refine strategy to fully exploit multiple decoding outputs, akin to the n-best rescoring strategy in speech recognition. Using the CLAP model for audio-text similarity calculation, we could select the textual descriptions generated by multiple searching beams that best match the input audio. Experimental results show that SLAM-AAC achieves state-of-the-art performance on Clotho V2 and AudioCaps, surpassing previous mainstream models.

</details>

### [Automatic Speech Recognition with BERT and CTC Transformers: A Review](2410.09456.md)
**Noussaiba Djeffal, Hamza Kheddar, Djamel Addou, Ahmed Cherif Mazari et al.** · 2024-10-12

<details>
<summary>Abstract</summary>

This review paper provides a comprehensive analysis of recent advances in automatic speech recognition (ASR) with bidirectional encoder representations from transformers BERT and connectionist temporal classification (CTC) transformers. The paper first introduces the fundamental concepts of ASR and discusses the challenges associated with it. It then explains the architecture of BERT and CTC transformers and their potential applications in ASR. The paper reviews several studies that have used these models for speech recognition tasks and discusses the results obtained. Additionally, the paper highlights the limitations of these models and outlines potential areas for further research. All in all, this review provides valuable insights for researchers and practitioners who are interested in ASR with BERT and CTC transformers.

</details>

### [Full-Rank No More: Low-Rank Weight Training for Modern Speech Recognition Models](2410.07771.md)
**Adriana Fernandez-Lopez, Shiwei Liu, Lu Yin, Stavros Petridis et al.** · 2024-10-10

<details>
<summary>Abstract</summary>

This paper investigates the under-explored area of low-rank weight training for large-scale Conformer-based speech recognition models from scratch. Our study demonstrates the viability of this training paradigm for such models, yielding several notable findings. Firstly, we discover that applying a low-rank structure exclusively to the attention modules can unexpectedly enhance performance, even with a significant rank reduction of 12%. In contrast, feed-forward layers present greater challenges, as they begin to exhibit performance degradation with a moderate 50% rank reduction. Furthermore, we find that both initialization and layer-wise rank assignment play critical roles in successful low-rank training. Specifically, employing SVD initialization and linear layer-wise rank mapping significantly boosts the efficacy of low-rank weight training. Building on these insights, we introduce the Low-Rank Speech Model from Scratch (LR-SMS), an approach that achieves performance parity with full-rank training while delivering substantial reductions in parameters count (by at least 2x), and training time speedups (by 1.3x for ASR and 1.15x for AVSR).

</details>

### [Unsupervised Data Validation Methods for Efficient Model Training](2410.07880.md)
**Yurii Paniv** · 2024-10-10

<details>
<summary>Abstract</summary>

This paper investigates the challenges and potential solutions for improving machine learning systems for low-resource languages. State-of-the-art models in natural language processing (NLP), text-to-speech (TTS), speech-to-text (STT), and vision-language models (VLM) rely heavily on large datasets, which are often unavailable for low-resource languages. This research explores key areas such as defining "quality data," developing methods for generating appropriate data and enhancing accessibility to model training. A comprehensive review of current methodologies, including data augmentation, multilingual transfer learning, synthetic data generation, and data selection techniques, highlights both advancements and limitations. Several open research questions are identified, providing a framework for future studies aimed at optimizing data utilization, reducing the required data quantity, and maintaining high-quality model performance. By addressing these challenges, the paper aims to make advanced machine learning models more accessible for low-resource languages, enhancing their utility and impact across various sectors.

</details>

### [A two-stage transliteration approach to improve performance of a multilingual ASR](2410.14709.md)
**Rohit Kumar** · 2024-10-09

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) systems are rapidly claiming to become state-of-art over other modeling methods. Several techniques have been introduced to improve their ability to handle multiple languages. However, due to variation in writing scripts for different languages, while decoding acoustically similar units, they do not always map to an appropriate grapheme in the target language. This restricts the scalability and adaptability of the model while dealing with multiple languages in code-mixing scenarios. This paper presents an approach to build a language-agnostic end-to-end model trained on a grapheme set obtained by projecting the multilingual grapheme data to the script of a more generic target language. This approach saves the acoustic model from retraining to span over a larger space and can easily be extended to multiple languages. A two-stage transliteration process realizes this approach and proves to minimize speech-class confusion. We performed experiments with an end-to-end multilingual speech recognition system for two Indic Languages, namely Nepali and Telugu. The original grapheme space of these languages is projected to the Devanagari script. We achieved a relative reduction of 20% in the Word Error Rate (WER) and 24% in the Character Error Rate (CER) in the transliterated space, over other language-dependent modeling methods.

</details>

### [UNCOM: Zero-shot Context-Aware Command Understanding for Tabletop Scenarios](2410.06355.md)
**Antonio Galiza Cerdeira Gonzalez, Paweł Gajewski, Bipin Indurkhya** · 2024-10-08

<details>
<summary>Abstract</summary>

This paper presents UNCOM, a novel hybrid framework for interpreting natural human commands in tabletop scenarios. The system integrates multiple sources of information -- speech, gestures, and scene context -- to extract structured, actionable instructions for robots. Addressing the need for general-purpose human-robot interaction in domestic environments, UNCOM is designed for zero-shot operation, without reliance on predefined object models or training data specific to a given task. Using foundational and task-specific deep learning models, it allows out-of-the-box speech recognition, natural language understanding, gesture detection, and object segmentation. The modular architecture enhances transparency and explainability by explicitly parsing commands into object-action-target representations, enabling integration with symbolic robotic frameworks. We demonstrate the system in a TIAGo++ robot and provide an evaluation on a real-world data set of human-robot interaction scenarios; achieving an 82.39\% success rate over our benchmark data set, highlighting the robustness of the system to diversity, noise, and communication ambiguity. The data set, evaluation scenarios, and the code are publicly available to support future research.

</details>

### [CR-CTC: Consistency regularization on CTC for improved speech recognition](2410.05101.md)
**Zengwei Yao, Wei Kang, Xiaoyu Yang, Fangjun Kuang et al.** · 2024-10-07

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) is a widely used method for automatic speech recognition (ASR), renowned for its simplicity and computational efficiency. However, it often falls short in recognition performance. In this work, we propose the Consistency-Regularized CTC (CR-CTC), which enforces consistency between two CTC distributions obtained from different augmented views of the input speech mel-spectrogram. We provide in-depth insights into its essential behaviors from three perspectives: 1) it conducts self-distillation between random pairs of sub-models that process different augmented views; 2) it learns contextual representation through masked prediction for positions within time-masked regions, especially when we increase the amount of time masking; 3) it suppresses the extremely peaky CTC distributions, thereby reducing overfitting and improving the generalization ability. Extensive experiments on LibriSpeech, Aishell-1, and GigaSpeech datasets demonstrate the effectiveness of our CR-CTC. It significantly improves the CTC performance, achieving state-of-the-art results comparable to those attained by transducer or systems combining CTC and attention-based encoder-decoder (CTC/AED). We release our code at https://github.com/k2-fsa/icefall.

</details>

### [Efficient and Robust Long-Form Speech Recognition with Hybrid H3-Conformer](2410.04159.md)
**Tomoki Honda, Shinsuke Sakai, Tatsuya Kawahara** · 2024-10-05

<details>
<summary>Abstract</summary>

Recently, Conformer has achieved state-of-the-art performance in many speech recognition tasks. However, the Transformer-based models show significant deterioration for long-form speech, such as lectures, because the self-attention mechanism becomes unreliable with the computation of the square order of the input length. To solve the problem, we incorporate a kind of state-space model, Hungry Hungry Hippos (H3), to replace or complement the multi-head self-attention (MHSA). H3 allows for efficient modeling of long-form sequences with a linear-order computation. In experiments using two datasets of CSJ and LibriSpeech, our proposed H3-Conformer model performs efficient and robust recognition of long-form speech. Moreover, we propose a hybrid of H3 and MHSA and show that using H3 in higher layers and MHSA in lower layers provides significant improvement in online recognition. We also investigate a parallel use of H3 and MHSA in all layers, resulting in the best performance.

</details>

### [The OCON model: an old but green solution for distributable supervised classification for acoustic monitoring in smart cities](2410.04098.md)
**Stefano Giacomelli, Marco Giordano, Claudia Rinaldi** · 2024-10-05

<details>
<summary>Abstract</summary>

This paper explores a structured application of the One-Class approach and the One-Class-One-Network model for supervised classification tasks, focusing on vowel phonemes classification and speakers recognition for the Automatic Speech Recognition (ASR) domain. For our case-study, the ASR model runs on a proprietary sensing and lightning system, exploited to monitor acoustic and air pollution on urban streets. We formalize combinations of pseudo-Neural Architecture Search and Hyper-Parameters Tuning experiments, using an informed grid-search methodology, to achieve classification accuracy comparable to nowadays most complex architectures, delving into the speaker recognition and energy efficiency aspects. Despite its simplicity, our model proposal has a very good chance to generalize the language and speaker genders context for widespread applicability in computational constrained contexts, proved by relevant statistical and performance metrics. Our experiments code is openly accessible on our GitHub.

</details>

### [The OCON model: an old but gold solution for distributable supervised classification](2410.05320.md)
**Stefano Giacomelli, Marco Giordano, Claudia Rinaldi** · 2024-10-05

<details>
<summary>Abstract</summary>

This paper introduces to a structured application of the One-Class approach and the One-Class-One-Network model for supervised classification tasks, specifically addressing a vowel phonemes classification case study within the Automatic Speech Recognition research field. Through pseudo-Neural Architecture Search and Hyper-Parameters Tuning experiments conducted with an informed grid-search methodology, we achieve classification accuracy comparable to nowadays complex architectures (90.0 - 93.7%). Despite its simplicity, our model prioritizes generalization of language context and distributed applicability, supported by relevant statistical and performance metrics. The experiments code is openly available at our GitHub.

</details>

### [Self-Powered LLM Modality Expansion for Large Speech-Text Models](2410.03798.md)
**Tengfei Yu, Xuebo Liu, Zhiyi Hou, Liang Ding et al.** · 2024-10-04

<details>
<summary>Abstract</summary>

Large language models (LLMs) exhibit remarkable performance across diverse tasks, indicating their potential for expansion into large speech-text models (LSMs) by integrating speech capabilities. Although unified speech-text pre-training and multimodal data instruction-tuning offer considerable benefits, these methods generally entail significant resource demands and tend to overfit specific tasks. This study aims to refine the use of speech datasets for LSM training by addressing the limitations of vanilla instruction tuning. We explore the instruction-following dynamics within LSMs, identifying a critical issue termed speech anchor bias-a tendency for LSMs to over-rely on speech inputs, mistakenly interpreting the entire speech modality as directives, thereby neglecting textual instructions. To counteract this bias, we introduce a self-powered LSM that leverages augmented automatic speech recognition data generated by the model itself for more effective instruction tuning. Our experiments across a range of speech-based tasks demonstrate that self-powered LSM mitigates speech anchor bias and improves the fusion of speech and text modalities in LSMs. Data, code and scripts are freely available at https://github.com/ytf-philp/Self-powered-LSM.

</details>

### [Searching for Best Practices in Medical Transcription with Large Language Model](2410.03797.md)
**Jiafeng Li, Yanda Mu** · 2024-10-04

<details>
<summary>Abstract</summary>

The transcription of medical monologues, especially those containing a high density of specialized terminology and delivered with a distinct accent, presents a significant challenge for existing automated systems. This paper introduces a novel approach leveraging a Large Language Model (LLM) to generate highly accurate medical transcripts from audio recordings of doctors' monologues, specifically focusing on Indian accents. Our methodology integrates advanced language modeling techniques to lower the Word Error Rate (WER) and ensure the precise recognition of critical medical terms. Through rigorous testing on a comprehensive dataset of medical recordings, our approach demonstrates substantial improvements in both overall transcription accuracy and the fidelity of key medical terminologies. These results suggest that our proposed system could significantly aid in clinical documentation processes, offering a reliable tool for healthcare providers to streamline their transcription needs while maintaining high standards of accuracy.

</details>

### [Algorithms For Automatic Accentuation And Transcription Of Russian Texts In Speech Recognition Systems](2410.02538.md)
**Olga Iakovenko, Ivan Bondarenko, Mariya Borovikova, Daniil Vodolazsky** · 2024-10-03

<details>
<summary>Abstract</summary>

This paper presents an overview of rule-based system for automatic accentuation and phonemic transcription of Russian texts for speech connected tasks, such as Automatic Speech Recognition (ASR). Two parts of the developed system, accentuation and transcription, use different approaches to achieve correct phonemic representations of input phrases. Accentuation is based on "Grammatical dictionary of the Russian language" of A.A. Zaliznyak and wiktionary corpus. To distinguish homographs, the accentuation system also utilises morphological information of the sentences based on Recurrent Neural Networks (RNN). Transcription algorithms apply the rules presented in the monograph of B.M. Lobanov and L.I. Tsirulnik "Computer Synthesis and Voice Cloning". The rules described in the present paper are implemented in an open-source module, which can be of use to any scientific study connected to ASR or Speech To Text (STT) tasks. Automatically marked up text annotations of the Russian Voxforge database were used as training data for an acoustic model in CMU Sphinx. The resulting acoustic model was evaluated on cross-validation, mean Word Accuracy being 71.2%. The developed toolkit is written in the Python language and is accessible on GitHub for any researcher interested.

</details>

### [Spoken Grammar Assessment Using LLM](2410.01579.md)
**Sunil Kumar Kopparapu, Chitralekha Bhat, Ashish Panda** · 2024-10-02

<details>
<summary>Abstract</summary>

Spoken language assessment (SLA) systems restrict themselves to evaluating the pronunciation and oral fluency of a speaker by analysing the read and spontaneous spoken utterances respectively. The assessment of language grammar or vocabulary is relegated to written language assessment (WLA) systems. Most WLA systems present a set of sentences from a curated finite-size database of sentences thereby making it possible to anticipate the test questions and train oneself. In this paper, we propose a novel end-to-end SLA system to assess language grammar from spoken utterances thus making WLA systems redundant; additionally, we make the assessment largely unteachable by employing a large language model (LLM) to bring in variations in the test. We further demonstrate that a hybrid automatic speech recognition (ASR) with a custom-built language model outperforms the state-of-the-art ASR engine for spoken grammar assessment.

</details>

### [Efficient Streaming LLM for Speech Recognition](2410.03752.md)
**Junteng Jia, Gil Keren, Wei Zhou, Egor Lakomkin et al.** · 2024-10-02

<details>
<summary>Abstract</summary>

Recent works have shown that prompting large language models with audio encodings can unlock speech recognition capabilities. However, existing techniques do not scale efficiently, especially while handling long form streaming audio inputs -- not only do they extrapolate poorly beyond the audio length seen during training, but they are also computationally inefficient due to the quadratic cost of attention. In this work, we introduce SpeechLLM-XL, a linear scaling decoder-only model for streaming speech recognition. We process audios in configurable chunks using limited attention window for reduced computation, and the text tokens for each audio chunk are generated auto-regressively until an EOS is predicted. During training, the transcript is segmented into chunks, using a CTC forced alignment estimated from encoder output. SpeechLLM-XL with 1.28 seconds chunk size achieves 2.7%/6.7% WER on LibriSpeech test clean/other, and it shows no quality degradation on long form utterances 10x longer than the training utterances.

</details>

### [Differentially Private Parameter-Efficient Fine-tuning for Large ASR Models](2410.01948.md)
**Hongbin Liu, Lun Wang, Om Thakkar, Abhradeep Thakurta et al.** · 2024-10-02

<details>
<summary>Abstract</summary>

Large ASR models can inadvertently leak sensitive information, which can be mitigated by formal privacy measures like differential privacy (DP). However, traditional DP training is computationally expensive, and can hurt model performance. Our study explores DP parameter-efficient fine-tuning as a way to mitigate privacy risks with smaller computation and performance costs for ASR models. Through extensive experimentation and progressive optimization, we achieve 4.6%/8.1% word error rate on LibriSpeech clean/other test-sets, setting a new performance benchmark while maintaining (10, 3.52e-6)-DP in fine-tuning a large ASR model with over 600M parameters.

</details>

### [Recent Advances in Speech Language Models: A Survey](2410.03751.md)
**Wenqian Cui, Dianzhi Yu, Xiaoqi Jiao, Ziqiao Meng et al.** · 2024-10-01

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have recently garnered significant attention, primarily for their capabilities in text-based interactions. However, natural human interaction often relies on speech, necessitating a shift towards voice-based models. A straightforward approach to achieve this involves a pipeline of ``Automatic Speech Recognition (ASR) + LLM + Text-to-Speech (TTS)", where input speech is transcribed to text, processed by an LLM, and then converted back to speech. Despite being straightforward, this method suffers from inherent limitations, such as information loss during modality conversion, significant latency due to the complex pipeline, and error accumulation across the three stages. To address these issues, Speech Language Models (SpeechLMs) -- end-to-end models that generate speech without converting from text -- have emerged as a promising alternative. This survey paper provides the first comprehensive overview of recent methodologies for constructing SpeechLMs, detailing the key components of their architecture and the various training recipes integral to their development. Additionally, we systematically survey the various capabilities of SpeechLMs, categorize their evaluation metrics, and discuss the challenges and future research directions in this rapidly evolving field. The GitHub repository is available at https://github.com/dreamtheater123/Awesome-SpeechLM-Survey

</details>

### [VHASR: A Multimodal Speech Recognition System With Vision Hotwords](2410.00822.md)
**Jiliang Hu, Zuchao Li, Ping Wang, Haojun Ai et al.** · 2024-10-01

<details>
<summary>Abstract</summary>

The image-based multimodal automatic speech recognition (ASR) model enhances speech recognition performance by incorporating audio-related image. However, some works suggest that introducing image information to model does not help improving ASR performance. In this paper, we propose a novel approach effectively utilizing audio-related image information and set up VHASR, a multimodal speech recognition system that uses vision as hotwords to strengthen the model's speech recognition capability. Our system utilizes a dual-stream architecture, which firstly transcribes the text on the two streams separately, and then combines the outputs. We evaluate the proposed model on four datasets: Flickr8k, ADE20k, COCO, and OpenImages. The experimental results show that VHASR can effectively utilize key information in images to enhance the model's speech recognition ability. Its performance not only surpasses unimodal ASR, but also achieves SOTA among existing image-based multimodal ASR.

</details>

### [Automatic Speech Recognition for the Ika Language](2410.00940.md)
**Uchenna Nzenwata, Daniel Ogbuigwe** · 2024-10-01

<details>
<summary>Abstract</summary>

We present a cost-effective approach for developing Automatic Speech Recognition (ASR) models for low-resource languages like Ika. We fine-tune the pretrained wav2vec 2.0 Massively Multilingual Speech Models on a high-quality speech dataset compiled from New Testament Bible translations in Ika. Our results show that fine-tuning multilingual pretrained models achieves a Word Error Rate (WER) of 0.5377 and Character Error Rate (CER) of 0.2651 with just over 1 hour of training data. The larger 1 billion parameter model outperforms the smaller 300 million parameter model due to its greater complexity and ability to store richer speech representations. However, we observe overfitting to the small training dataset, reducing generalizability. Our findings demonstrate the potential of leveraging multilingual pretrained models for low-resource languages. Future work should focus on expanding the dataset and exploring techniques to mitigate overfitting.

</details>

### [End-to-End Speech Recognition with Pre-trained Masked Language Model](2410.00528.md)
**Yosuke Higuchi, Tetsuji Ogawa, Tetsunori Kobayashi, Shinji Watanabe** · 2024-10-01

<details>
<summary>Abstract</summary>

We present a novel approach to end-to-end automatic speech recognition (ASR) that utilizes pre-trained masked language models (LMs) to facilitate the extraction of linguistic information. The proposed models, BERT-CTC and BECTRA, are specifically designed to effectively integrate pre-trained LMs (e.g., BERT) into end-to-end ASR models. BERT-CTC adapts BERT for connectionist temporal classification (CTC) by addressing the constraint of the conditional independence assumption between output tokens. This enables explicit conditioning of BERT's contextualized embeddings in the ASR process, seamlessly merging audio and linguistic information through an iterative refinement algorithm. BECTRA extends BERT-CTC to the transducer framework and trains the decoder network using a vocabulary suitable for ASR training. This aims to bridge the gap between the text processed in end-to-end ASR and BERT, as these models have distinct vocabularies with varying text formats and styles, such as the presence of punctuation. Experimental results on various ASR tasks demonstrate that the proposed models improve over both the CTC and transducer-based baselines, owing to the incorporation of BERT knowledge. Moreover, our in-depth analysis and investigation verify the effectiveness of the proposed formulations and architectural designs.

</details>

### [Boosting Hybrid Autoregressive Transducer-based ASR with Internal Acoustic Model Training and Dual Blank Thresholding](2409.20313.md)
**Takafumi Moriya, Takanori Ashihara, Masato Mimura, Hiroshi Sato et al.** · 2024-09-30

<details>
<summary>Abstract</summary>

A hybrid autoregressive transducer (HAT) is a variant of neural transducer that models blank and non-blank posterior distributions separately. In this paper, we propose a novel internal acoustic model (IAM) training strategy to enhance HAT-based speech recognition. IAM consists of encoder and joint networks, which are fully shared and jointly trained with HAT. This joint training not only enhances the HAT training efficiency but also encourages IAM and HAT to emit blanks synchronously which skips the more expensive non-blank computation, resulting in more effective blank thresholding for faster decoding. Experiments demonstrate that the relative error reductions of the HAT with IAM compared to the vanilla HAT are statistically significant. Moreover, we introduce dual blank thresholding, which combines both HAT- and IAM-blank thresholding and a compatible decoding algorithm. This results in a 42-75% decoding speed-up with no major performance degradation.

</details>

### [Alignment-Free Training for Transducer-based Multi-Talker ASR](2409.20301.md)
**Takafumi Moriya, Shota Horiguchi, Marc Delcroix, Ryo Masumura et al.** · 2024-09-30

<details>
<summary>Abstract</summary>

Extending the RNN Transducer (RNNT) to recognize multi-talker speech is essential for wider automatic speech recognition (ASR) applications. Multi-talker RNNT (MT-RNNT) aims to achieve recognition without relying on costly front-end source separation. MT-RNNT is conventionally implemented using architectures with multiple encoders or decoders, or by serializing all speakers' transcriptions into a single output stream. The first approach is computationally expensive, particularly due to the need for multiple encoder processing. In contrast, the second approach involves a complex label generation process, requiring accurate timestamps of all words spoken by all speakers in the mixture, obtained from an external ASR system. In this paper, we propose a novel alignment-free training scheme for the MT-RNNT (MT-RNNT-AFT) that adopts the standard RNNT architecture. The target labels are created by appending a prompt token corresponding to each speaker at the beginning of the transcription, reflecting the order of each speaker's appearance in the mixtures. Thus, MT-RNNT-AFT can be trained without relying on accurate alignments, and it can recognize all speakers' speech with just one round of encoder processing. Experiments show that MT-RNNT-AFT achieves performance comparable to that of the state-of-the-art alternatives, while greatly simplifying the training process.

</details>

### [Mamba for Streaming ASR Combined with Unimodal Aggregation](2410.00070.md)
**Ying Fang, Xiaofei Li** · 2024-09-30

<details>
<summary>Abstract</summary>

This paper works on streaming automatic speech recognition (ASR). Mamba, a recently proposed state space model, has demonstrated the ability to match or surpass Transformers in various tasks while benefiting from a linear complexity advantage. We explore the efficiency of Mamba encoder for streaming ASR and propose an associated lookahead mechanism for leveraging controllable future information. Additionally, a streaming-style unimodal aggregation (UMA) method is implemented, which automatically detects token activity and streamingly triggers token output, and meanwhile aggregates feature frames for better learning token representation. Based on UMA, an early termination (ET) method is proposed to further reduce recognition latency. Experiments conducted on two Mandarin Chinese datasets demonstrate that the proposed model achieves competitive ASR performance in terms of both recognition accuracy and latency.

</details>

### [AfriHuBERT: A self-supervised speech representation model for African languages](2409.20201.md)
**Jesujoba O. Alabi, Xuechen Liu, Dietrich Klakow, Junichi Yamagishi** · 2024-09-30

<details>
<summary>Abstract</summary>

In this work, we present AfriHuBERT, an extension of mHuBERT-147, a compact self-supervised learning (SSL) model pretrained on 147 languages. While mHuBERT-147 covered 16 African languages, we expand this to 1,226 through continued pretraining on 10K+ hours of speech data from diverse sources, benefiting an African population of over 600M. We evaluate AfriHuBERT on two key speech tasks, Spoken Language Identification (SLID) and Automatic Speech Recognition (ASR), using the FLEURS benchmark. Our results show a +3.6% F1 score improvement for SLID and a -2.1% average Word Error Rate (WER) reduction for ASR over mHuBERT-147, and demonstrates competitiveness with larger SSL models such as MMS and XEUS. Further analysis shows that ASR models trained on AfriHuBERT exhibit improved cross-corpus generalization and are competitive in extremely low-resource ASR scenarios.

</details>

### [Predictive Speech Recognition and End-of-Utterance Detection Towards Spoken Dialog Systems](2409.19990.md)
**Oswald Zink, Yosuke Higuchi, Carlos Mullov, Alexander Waibel et al.** · 2024-09-30

<details>
<summary>Abstract</summary>

Effective spoken dialog systems should facilitate natural interactions with quick and rhythmic timing, mirroring human communication patterns. To reduce response times, previous efforts have focused on minimizing the latency in automatic speech recognition (ASR) to optimize system efficiency. However, this approach requires waiting for ASR to complete processing until a speaker has finished speaking, which limits the time available for natural language processing (NLP) to formulate accurate responses. As humans, we continuously anticipate and prepare responses even while the other party is still speaking. This allows us to respond appropriately without missing the optimal time to speak. In this work, as a pioneering study toward a conversational system that simulates such human anticipatory behavior, we aim to realize a function that can predict the forthcoming words and estimate the time remaining until the end of an utterance (EOU), using the middle portion of an utterance. To achieve this, we propose a training strategy for an encoder-decoder-based ASR system, which involves masking future segments of an utterance and prompting the decoder to predict the words in the masked audio. Additionally, we develop a cross-attention-based algorithm that incorporates both acoustic and linguistic information to accurately detect the EOU. The experimental results demonstrate the proposed model's ability to predict upcoming words and estimate future EOU events up to 300ms prior to the actual EOU. Moreover, the proposed training strategy exhibits general improvements in ASR performance.

</details>

### [HDMoLE: Mixture of LoRA Experts with Hierarchical Routing and Dynamic Thresholds for Fine-Tuning LLM-based ASR Models](2409.19878.md)
**Bingshen Mu, Kun Wei, Qijie Shao, Yong Xu et al.** · 2024-09-30

<details>
<summary>Abstract</summary>

Recent advancements in integrating Large Language Models (LLM) with automatic speech recognition (ASR) have performed remarkably in general domains. While supervised fine-tuning (SFT) of all model parameters is often employed to adapt pre-trained LLM-based ASR models to specific domains, it imposes high computational costs and notably reduces their performance in general domains. In this paper, we propose a novel parameter-efficient multi-domain fine-tuning method for adapting pre-trained LLM-based ASR models to multi-accent domains without catastrophic forgetting named \textit{HDMoLE}, which leverages hierarchical routing and dynamic thresholds based on combining low-rank adaptation (LoRA) with the mixer of experts (MoE) and can be generalized to any linear layer. Hierarchical routing establishes a clear correspondence between LoRA experts and accent domains, improving cross-domain collaboration among the LoRA experts. Unlike the static Top-K strategy for activating LoRA experts, dynamic thresholds can adaptively activate varying numbers of LoRA experts at each MoE layer. Experiments on the multi-accent and standard Mandarin datasets demonstrate the efficacy of HDMoLE. Applying HDMoLE to an LLM-based ASR model projector module achieves similar performance to full fine-tuning in the target multi-accent domains while using only 9.6% of the trainable parameters required for full fine-tuning and minimal degradation in the source general domain.

</details>

### [Fine-Tuning Automatic Speech Recognition for People with Parkinson's: An Effective Strategy for Enhancing Speech Technology Accessibility](2409.19818.md)
**Xiuwen Zheng, Bornali Phukon, Mark Hasegawa-Johnson** · 2024-09-29

<details>
<summary>Abstract</summary>

This paper enhances dysarthric and dysphonic speech recognition by fine-tuning pretrained automatic speech recognition (ASR) models on the 2023-10-05 data package of the Speech Accessibility Project (SAP), which contains the speech of 253 people with Parkinson's disease. Experiments tested methods that have been effective for Cerebral Palsy, including the use of speaker clustering and severity-dependent models, weighted fine-tuning, and multi-task learning. Best results were obtained using a multi-task learning model, in which the ASR is trained to produce an estimate of the speaker's impairment severity as an auxiliary output. The resulting word error rates are considerably improved relative to a baseline model fine-tuned using only Librispeech data, with word error rate improvements of 37.62\% and 26.97\% compared to fine-tuning on 100h and 960h of LibriSpeech data, respectively.

</details>

### [Efficient Long-Form Speech Recognition for General Speech In-Context Learning](2409.19757.md)
**Hao Yen, Shaoshi Ling, Guoli Ye** · 2024-09-29

<details>
<summary>Abstract</summary>

We propose a novel approach to end-to-end automatic speech recognition (ASR) to achieve efficient speech in-context learning (SICL) for (i) long-form speech decoding, (ii) test-time speaker adaptation, and (iii) test-time contextual biasing. Specifically, we introduce an attention-based encoder-decoder (AED) model with SICL capability (referred to as SICL-AED), where the decoder utilizes an utterance-level cross-attention to integrate information from the encoder's output efficiently, and a document-level self-attention to learn contextual information. Evaluated on the benchmark TEDLIUM3 dataset, SICL-AED achieves an 8.64% relative word error rate (WER) reduction compared to a baseline utterance-level AED model by leveraging previously decoded outputs as in-context examples. It also demonstrates comparable performance to conventional long-form AED systems with significantly reduced runtime and memory complexity. Additionally, we introduce an in-context fine-tuning (ICFT) technique that further enhances SICL effectiveness during inference. Experiments on speaker adaptation and contextual biasing highlight the general speech in-context learning capabilities of our system, achieving effective results with provided contexts. Without specific fine-tuning, SICL-AED matches the performance of supervised AED baselines for speaker adaptation and improves entity recall by 64% for contextual biasing task.

</details>

### [Quantitative Analysis of Audio-Visual Tasks: An Information-Theoretic Perspective](2409.19575.md)
**Chen Chen, Xiaolou Li, Zehua Liu, Lantian Li et al.** · 2024-09-29

<details>
<summary>Abstract</summary>

In the field of spoken language processing, audio-visual speech processing is receiving increasing research attention. Key components of this research include tasks such as lip reading, audio-visual speech recognition, and visual-to-speech synthesis. Although significant success has been achieved, theoretical analysis is still insufficient for audio-visual tasks. This paper presents a quantitative analysis based on information theory, focusing on information intersection between different modalities. Our results show that this analysis is valuable for understanding the difficulties of audio-visual processing tasks as well as the benefits that could be obtained by modality integration.

</details>

### [Making LLMs Better Many-to-Many Speech-to-Text Translators with Curriculum Learning](2409.19510.md)
**Yexing Du, Youcheng Pan, Ziyang Ma, Bo Yang et al.** · 2024-09-29

<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have achieved significant success in Speech-to-Text Translation (S2TT) tasks. While most existing research has focused on English-centric translation directions, the exploration of many-to-many translation is still limited by the scarcity of parallel data. To address this, we propose a three-stage curriculum learning strategy that leverages the machine translation capabilities of large language models and adapts them to S2TT tasks, enabling effective learning in low-resource settings. We trained MLLMs with varying parameter sizes (3B, 7B, and 32B) and evaluated the proposed strategy using the FLEURS and CoVoST-2 datasets. Experimental results show that the proposed strategy achieves state-of-the-art average performance in $15\times14$ language pairs, requiring fewer than 10 hours of speech data per language to achieve competitive results. The source code and models are released at https://github.com/yxduir/LLM-SRT.

</details>

### [Scrambled text: training Language Models to correct OCR errors using synthetic data](2409.19735.md)
**Jonathan Bourne** · 2024-09-29

<details>
<summary>Abstract</summary>

OCR errors are common in digitised historical archives significantly affecting their usability and value. Generative Language Models (LMs) have shown potential for correcting these errors using the context provided by the corrupted text and the broader socio-cultural context, a process called Context Leveraging OCR Correction (CLOCR-C). However, getting sufficient training data for fine-tuning such models can prove challenging. This paper shows that fine-tuning a language model on synthetic data using an LM and using a character level Markov corruption process can significantly improve the ability to correct OCR errors. Models trained on synthetic data reduce the character error rate by 55% and word error rate by 32% over the base LM and outperform models trained on real data. Key findings include; training on under-corrupted data is better than over-corrupted data; non-uniform character level corruption is better than uniform corruption; More tokens-per-observation outperforms more observations for a fixed token budget. The outputs for this paper are a set of 8 heuristics for training effective CLOCR-C models, a dataset of 11,000 synthetic 19th century newspaper articles and scrambledtext a python library for creating synthetic corrupted data.

</details>

### [Advanced Clustering Techniques for Speech Signal Enhancement: A Review and Metanalysis of Fuzzy C-Means, K-Means, and Kernel Fuzzy C-Means Methods](2409.19448.md)
**Abdulhady Abas Abdullah, Aram Mahmood Ahmed, Tarik Rashid, Hadi Veisi** · 2024-09-28

<details>
<summary>Abstract</summary>

Speech signal processing is a cornerstone of modern communication technologies, tasked with improving the clarity and comprehensibility of audio data in noisy environments. The primary challenge in this field is the effective separation and recognition of speech from background noise, crucial for applications ranging from voice-activated assistants to automated transcription services. The quality of speech recognition directly impacts user experience and accessibility in technology-driven communication. This review paper explores advanced clustering techniques, particularly focusing on the Kernel Fuzzy C-Means (KFCM) method, to address these challenges. Our findings indicate that KFCM, compared to traditional methods like K-Means (KM) and Fuzzy C-Means (FCM), provides superior performance in handling non-linear and non-stationary noise conditions in speech signals. The most notable outcome of this review is the adaptability of KFCM to various noisy environments, making it a robust choice for speech enhancement applications. Additionally, the paper identifies gaps in current methodologies, such as the need for more dynamic clustering algorithms that can adapt in real time to changing noise conditions without compromising speech recognition quality. Key contributions include a detailed comparative analysis of current clustering algorithms and suggestions for further integrating hybrid models that combine KFCM with neural networks to enhance speech recognition accuracy. Through this review, we advocate for a shift towards more sophisticated, adaptive clustering techniques that can significantly improve speech enhancement and pave the way for more resilient speech processing systems.

</details>

### [A GEN AI Framework for Medical Note Generation](2410.01841.md)
**Hui Yi Leong, Yi Fan Gao, Shuai Ji, Bora Kalaycioglu et al.** · 2024-09-27

<details>
<summary>Abstract</summary>

The increasing administrative burden of medical documentation, particularly through Electronic Health Records (EHR), significantly reduces the time available for direct patient care and contributes to physician burnout. To address this issue, we propose MediNotes, an advanced generative AI framework designed to automate the creation of SOAP (Subjective, Objective, Assessment, Plan) notes from medical conversations. MediNotes integrates Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Automatic Speech Recognition (ASR) to capture and process both text and voice inputs in real time or from recorded audio, generating structured and contextually accurate medical notes. The framework also incorporates advanced techniques like Quantized Low-Rank Adaptation (QLoRA) and Parameter-Efficient Fine-Tuning (PEFT) for efficient model fine-tuning in resource-constrained environments. Additionally, MediNotes offers a query-based retrieval system, allowing healthcare providers and patients to access relevant medical information quickly and accurately. Evaluations using the ACI-BENCH dataset demonstrate that MediNotes significantly improves the accuracy, efficiency, and usability of automated medical documentation, offering a robust solution to reduce the administrative burden on healthcare professionals while improving the quality of clinical workflows.

</details>

### [Speech-Mamba: Long-Context Speech Recognition with Selective State Spaces Models](2409.18654.md)
**Xiaoxue Gao, Nancy F. Chen** · 2024-09-27

<details>
<summary>Abstract</summary>

Current automatic speech recognition systems struggle with modeling long speech sequences due to high quadratic complexity of Transformer-based models. Selective state space models such as Mamba has performed well on long-sequence modeling in natural language processing and computer vision tasks. However, research endeavors in speech technology tasks has been under-explored. We propose Speech-Mamba, which incorporates selective state space modeling in Transformer neural architectures. Long sequence representations with selective state space models in Speech-Mamba is complemented with lower-level representations from Transformer-based modeling. Speech-mamba achieves better capacity to model long-range dependencies, as it scales near-linearly with sequence length.

</details>

### [CCE-Net: Causal Convolution Embedding Network for Streaming Automatic Speech Recognition](s2:bfb9e1b05f0af863fbde0573b71a2de62cf180cd.md)
**Fei Deng, Yue Ming, Boyang Lyu** · 2024-09-27

<details>
<summary>Abstract</summary>

Article CCE-Net: Causal Convolution Embedding Network for Streaming Automatic Speech Recognition Feiteng Deng, Yue Ming *, and Boyang Lyu Beijing Key Laboratory of Work Safety and Intelligent Monitoring, School of Electronic Engineering, Beijing University of Posts and Telecommunications, Beijing 100876, China * Correspondence: yming@bupt.edu.cn Received: 11 March 2024 Accepted: 15 August 2024 Published: 27 September 2024 Abstract: Streaming Automatic Speech Recognition (ASR) has gained significant attention across various application scenarios, including video conferencing, live sports events, and intelligent terminals. However, chunk division for current streaming speech recognition results in insufficient contextual information, thus weakening the ability of attention modeling and leading to a decrease in recognition accuracy. For Mandarin speech recognition, there is also a risk of splitting Chinese character phonemes into different chunks, which may lead to incorrect recognition of Chinese characters at chunk boundaries due to incomplete phonemes. To alleviate these problems, we propose a novel front-end network - Causal Convolution Embedding Network (CCE-Net). The network introduces a causal convolution embedding module to obtain richer historical context information, while capturing Chinese character phoneme information at chunk boundaries and feeding it to the current chunk. We conducted experiments on Aishell-1 and Aidatatang. The results showed that our method achieves a character error rate (CER) of 5.07% and 4.90%, respectively, without introducing any additional latency, showing competitive performances.

</details>

### [Unveiling the Role of Pretraining in Direct Speech Translation](2409.18044.md)
**Belen Alastruey, Gerard I. Gállego, Marta R. Costa-jussà** · 2024-09-26

<details>
<summary>Abstract</summary>

Direct speech-to-text translation systems encounter an important drawback in data scarcity. A common solution consists on pretraining the encoder on automatic speech recognition, hence losing efficiency in the training process. In this study, we compare the training dynamics of a system using a pretrained encoder, the conventional approach, and one trained from scratch. We observe that, throughout the training, the randomly initialized model struggles to incorporate information from the speech inputs for its predictions. Hence, we hypothesize that this issue stems from the difficulty of effectively training an encoder for direct speech translation. While a model trained from scratch needs to learn acoustic and semantic modeling simultaneously, a pretrained one can just focus on the latter. Based on these findings, we propose a subtle change in the decoder cross-attention to integrate source information from earlier steps in training. We show that with this change, the model trained from scratch can achieve comparable performance to the pretrained one, while reducing the training time.

</details>

### [Are Transformers in Pre-trained LM A Good ASR Encoder? An Empirical Study](2409.17750.md)
**Keyu An, Shiliang Zhang, Zhijie Yan** · 2024-09-26

<details>
<summary>Abstract</summary>

In this study, we delve into the efficacy of transformers within pre-trained language models (PLMs) when repurposed as encoders for Automatic Speech Recognition (ASR). Our underlying hypothesis posits that, despite being initially trained on text-based corpora, these transformers possess a remarkable capacity to extract effective features from the input sequence. This inherent capability, we argue, is transferrable to speech data, thereby augmenting the acoustic modeling ability of ASR. Through rigorous empirical analysis, our findings reveal a notable improvement in Character Error Rate (CER) and Word Error Rate (WER) across diverse ASR tasks when transformers from pre-trained LMs are incorporated. Particularly, they serve as an advantageous starting point for initializing ASR encoders. Furthermore, we uncover that these transformers, when integrated into a well-established ASR encoder, can significantly boost performance, especially in scenarios where profound semantic comprehension is pivotal. This underscores the potential of leveraging the semantic prowess embedded within pre-trained transformers to advance ASR systems' capabilities.

</details>

### [Paraformer-v2: An improved non-autoregressive transformer for noise-robust speech recognition](2409.17746.md)
**Keyu An, Zerui Li, Zhifu Gao, Shiliang Zhang** · 2024-09-26

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder, e.g. transformer and its variants, generates the output sequence in an autoregressive (AR) manner. Despite its superior performance, AR model is computationally inefficient as its generation requires as many iterations as the output length. In this paper, we propose Paraformer-v2, an improved version of Paraformer, for fast, accurate, and noise-robust non-autoregressive speech recognition. In Paraformer-v2, we use a CTC module to extract the token embeddings, as the alternative to the continuous integrate-and-fire module in Paraformer. Extensive experiments demonstrate that Paraformer-v2 outperforms Paraformer on multiple datasets, especially on the English datasets (over 14% improvement on WER), and is more robust in noisy environments.

</details>

### [Deep CLAS: Deep Contextual Listen, Attend and Spell](2409.17603.md)
**Mengzhi Wang, Shifu Xiong, Genshun Wan, Hang Chen et al.** · 2024-09-26

<details>
<summary>Abstract</summary>

Contextual-LAS (CLAS) has been shown effective in improving Automatic Speech Recognition (ASR) of rare words. It relies on phrase-level contextual modeling and attention-based relevance scoring without explicit contextual constraint which lead to insufficient use of contextual information. In this work, we propose deep CLAS to use contextual information better. We introduce bias loss forcing model to focus on contextual information. The query of bias attention is also enriched to improve the accuracy of the bias attention score. To get fine-grained contextual information, we replace phrase-level encoding with character-level encoding and encode contextual information with conformer rather than LSTM. Moreover, we directly use the bias attention score to correct the output probability distribution of the model. Experiments using the public AISHELL-1 and AISHELL-NER. On AISHELL-1, compared to CLAS baselines, deep CLAS obtains a 65.78% relative recall and a 53.49% relative F1-score increase in the named entity recognition scene.

</details>

### [A Fly on the Wall -- Exploiting Acoustic Side-Channels in Differential Pressure Sensors](2409.18213.md)
**Yonatan Gizachew Achamyeleh, Mohamad Habib Fakih, Gabriel Garcia, Anomadarshi Barua et al.** · 2024-09-26

<details>
<summary>Abstract</summary>

Differential Pressure Sensors are widely deployed to monitor critical environments. However, our research unveils a previously overlooked vulnerability: their high sensitivity to pressure variations makes them susceptible to acoustic side-channel attacks. We demonstrate that the pressure-sensing diaphragms in DPS can inadvertently capture subtle air vibrations caused by speech, which propagate through the sensor's components and affect the pressure readings. Exploiting this discovery, we introduce BaroVox, a novel attack that reconstructs speech from DPS readings, effectively turning DPS into a "fly on the wall." We model the effect of sound on DPS, exploring the limits and challenges of acoustic leakage. To overcome these challenges, we propose two solutions: a signal-processing approach using a unique spectral subtraction method and a deep learning-based approach for keyword classification. Evaluations under various conditions demonstrate BaroVox's effectiveness, achieving a word error rate of 0.29 for manual recognition and 90.51% accuracy for automatic recognition. Our findings highlight the significant privacy implications of this vulnerability. We also discuss potential defense strategies to mitigate the risks posed by BaroVox.

</details>

### [How to Connect Speech Foundation Models and Large Language Models? What Matters and What Does Not](2409.17044.md)
**Francesco Verdini, Pierfrancesco Melucci, Stefano Perna, Francesco Cariaggi et al.** · 2024-09-25

<details>
<summary>Abstract</summary>

The remarkable performance achieved by Large Language Models (LLM) has driven research efforts to leverage them for a wide range of tasks and input modalities. In speech-to-text (S2T) tasks, the emerging solution consists of projecting the output of the encoder of a Speech Foundational Model (SFM) into the LLM embedding space through an adapter module. However, no work has yet investigated how much the downstream-task performance depends on each component (SFM, adapter, LLM) nor whether the best design of the adapter depends on the chosen SFM and LLM. To fill this gap, we evaluate the combination of 5 adapter modules, 2 LLMs (Mistral and Llama), and 2 SFMs (Whisper and SeamlessM4T) on two widespread S2T tasks, namely Automatic Speech Recognition and Speech Translation. Our results demonstrate that the SFM plays a pivotal role in downstream performance, while the adapter choice has moderate impact and depends on the SFM and LLM.

</details>

### [Spelling Correction through Rewriting of Non-Autoregressive ASR Lattices](2409.16469.md)
**Leonid Velikovich, Christopher Li, Diamantino Caseiro, Shankar Kumar et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

For end-to-end Automatic Speech Recognition (ASR) models, recognizing personal or rare phrases can be hard. A promising way to improve accuracy is through spelling correction (or rewriting) of the ASR lattice, where potentially misrecognized phrases are replaced with acoustically similar and contextually relevant alternatives. However, rewriting is challenging for ASR models trained with connectionist temporal classification (CTC) due to noisy hypotheses produced by a non-autoregressive, context-independent beam search. We present a finite-state transducer (FST) technique for rewriting wordpiece lattices generated by Transformer-based CTC models. Our algorithm performs grapheme-to-phoneme (G2P) conversion directly from wordpieces into phonemes, avoiding explicit word representations and exploiting the richness of the CTC lattice. Our approach requires no retraining or modification of the ASR model. We achieved up to a 15.2% relative reduction in sentence error rate (SER) on a test set with contextually relevant entities.

</details>

### [Revisiting Acoustic Features for Robust ASR](2409.16399.md)
**Muhammad A. Shah, Bhiksha Raj** · 2024-09-24

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems must be robust to the myriad types of noises present in real-world environments including environmental noise, room impulse response, special effects as well as attacks by malicious actors (adversarial attacks). Recent works seek to improve accuracy and robustness by developing novel Deep Neural Networks (DNNs) and curating diverse training datasets for them, while using relatively simple acoustic features. While this approach improves robustness to the types of noise present in the training data, it confers limited robustness against unseen noises and negligible robustness to adversarial attacks. In this paper, we revisit the approach of earlier works that developed acoustic features inspired by biological auditory perception that could be used to perform accurate and robust ASR. In contrast, Specifically, we evaluate the ASR accuracy and robustness of several biologically inspired acoustic features. In addition to several features from prior works, such as gammatone filterbank features (GammSpec), we also propose two new acoustic features called frequency masked spectrogram (FreqMask) and difference of gammatones spectrogram (DoGSpec) to simulate the neuro-psychological phenomena of frequency masking and lateral suppression. Experiments on diverse models and datasets show that (1) DoGSpec achieves significantly better robustness than the highly popular log mel spectrogram (LogMelSpec) with minimal accuracy degradation, and (2) GammSpec achieves better accuracy and robustness to non-adversarial noises from the Speech Robust Bench benchmark, but it is outperformed by DoGSpec against adversarial attacks.

</details>

### [Bridging Speech and Text: Enhancing ASR with Pinyin-to-Character Pre-training in LLMs](2409.16005.md)
**Yang Yuhang, Peng Yizhou, Eng Siong Chng, Xionghu Zhong** · 2024-09-24

<details>
<summary>Abstract</summary>

The integration of large language models (LLMs) with pre-trained speech models has opened up new avenues in automatic speech recognition (ASR). While LLMs excel in multimodal understanding tasks, effectively leveraging their capabilities for ASR remains a significant challenge. This paper presents a novel training approach to enhance LLM performance in ASR tasks. We propose pre-training LLMs on Pinyin embedding sequences, which represent pronunciation features, to generate corresponding Chinese characters. This step enables the LLM to adapt to generating text from pronunciation features before encountering real speech data. Furthermore, we fine-tune the LoRA parameters to enhance the LLM's understanding of speech modality information. In AISHELL-1 corpus, our approach yields a 9.5% relative improvement in ASR tasks compared to the baseline without Pinyi-to-Character pre-training. Additionally, incorporating auxiliary text data for Pinyi-to-Character pre-training further boosts performance, achieving a 19.0% relative improvement.

</details>

### [Boosting Code-Switching ASR with Mixture of Experts Enhanced Speech-Conditioned LLM](2409.15905.md)
**Fengrun Zhang, Wang Geng, Hukai Huang, Yahui Shan et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

In this paper, we introduce a speech-conditioned Large Language Model (LLM) integrated with a Mixture of Experts (MoE) based connector to address the challenge of Code-Switching (CS) in Automatic Speech Recognition (ASR). Specifically, we propose an Insertion and Deletion of Interruption Token (IDIT) mechanism for better transfer text generation ability of LLM to speech recognition task. We also present a connecter with MoE architecture that manages multiple languages efficiently. To further enhance the collaboration of multiple experts and leverage the understanding capabilities of LLM, we propose a two-stage progressive training strategy: 1) The connector is unfrozen and trained with language-specialized experts to map speech representations to the text space. 2) The connector and LLM LoRA adaptor are trained with the proposed IDIT mechanism and all experts are activated to learn general representations. Experimental results demonstrate that our method significantly outperforms state-of-the-art models, including end-to-end and large-scale audio-language models.

</details>

### [WeSep: A Scalable and Flexible Toolkit Towards Generalizable Target Speaker Extraction](2409.15799.md)
**Shuai Wang, Ke Zhang, Shaoxiong Lin, Junjie Li et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

Target speaker extraction (TSE) focuses on isolating the speech of a specific target speaker from overlapped multi-talker speech, which is a typical setup in the cocktail party problem. In recent years, TSE draws increasing attention due to its potential for various applications such as user-customized interfaces and hearing aids, or as a crutial front-end processing technologies for subsequential tasks such as speech recognition and speaker recongtion. However, there are currently few open-source toolkits or available pre-trained models for off-the-shelf usage. In this work, we introduce WeSep, a toolkit designed for research and practical applications in TSE. WeSep is featured with flexible target speaker modeling, scalable data management, effective on-the-fly data simulation, structured recipes and deployment support. The toolkit is publicly avaliable at \url{https://github.com/wenet-e2e/WeSep.}

</details>

### [Hypothesis Clustering and Merging: Novel MultiTalker Speech Recognition with Speaker Tokens](2409.15732.md)
**Yosuke Kashiwagi, Hayato Futami, Emiru Tsunoo, Siddhant Arora et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

In many real-world scenarios, such as meetings, multiple speakers are present with an unknown number of participants, and their utterances often overlap. We address these multi-speaker challenges by a novel attention-based encoder-decoder method augmented with special speaker class tokens obtained by speaker clustering. During inference, we select multiple recognition hypotheses conditioned on predicted speaker cluster tokens, and these hypotheses are merged by agglomerative hierarchical clustering (AHC) based on the normalized edit distance. The clustered hypotheses result in the multi-speaker transcriptions with the appropriate number of speakers determined by AHC. Our experiments on the LibriMix dataset demonstrate that our proposed method was particularly effective in complex 3-mix environments, achieving a 55% relative error reduction on clean data and a 36% relative error reduction on noisy data compared with conventional serialized output training.

</details>

### [Whisper in Medusa's Ear: Multi-head Efficient Decoding for Transformer-based ASR](2409.15869.md)
**Yael Segal-Feldman, Aviv Shamsian, Aviv Navon, Gill Hetz et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

Large transformer-based models have significant potential for speech transcription and translation. Their self-attention mechanisms and parallel processing enable them to capture complex patterns and dependencies in audio sequences. However, this potential comes with challenges, as these large and computationally intensive models lead to slow inference speeds. Various optimization strategies have been proposed to improve performance, including efficient hardware utilization and algorithmic enhancements. In this paper, we introduce Whisper-Medusa, a novel approach designed to enhance processing speed with minimal impact on Word Error Rate (WER). The proposed model extends the OpenAI's Whisper architecture by predicting multiple tokens per iteration, resulting in a 50% reduction in latency. We showcase the effectiveness of Whisper-Medusa across different learning setups and datasets.

</details>

### [Evaluation of Speech Foundation Models for ASR on Child-Adult Conversations in Autism Diagnostic Sessions](2409.16135.md)
**Aditya Ashvin, Rimita Lahiri, Aditya Kommineni, Somer Bishop et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

Reliable transcription of child-adult conversations in clinical settings is crucial for diagnosing developmental disorders like Autism. Recent advances in deep learning and availability of large scale transcribed data has led to development of speech foundation models that have shown dramatic improvements in ASR performance. However, their performance on conversational child-adult interactions remains underexplored. In this work, we provide a comprehensive evaluation of ASR performance on a dataset containing child-adult interactions from autism diagnostic sessions, using Whisper, Wav2Vec2, HuBERT, and WavLM. We find that speech foundation models show a noticeable performance drop (15-20% absolute WER) for child speech compared to adult speech in the conversational setting. Then, we fine-tune the best-performing zero-shot model (Whisper-large) using LoRA in a low-resource setting, yielding 8% and 13% absolute WER improvements for child and adult speech, respectively.

</details>

### [MultiMed: Multilingual Medical Speech Recognition via Attention Encoder Decoder](2409.14074.md)
**Khai Le-Duc, Phuc Phan, Tan-Hanh Pham, Bach Phan Tat et al.** · 2024-09-21

<details>
<summary>Abstract</summary>

Multilingual automatic speech recognition (ASR) in the medical domain serves as a foundational task for various downstream applications such as speech translation, spoken language understanding, and voice-activated assistants. This technology improves patient care by enabling efficient communication across language barriers, alleviating specialized workforce shortages, and facilitating improved diagnosis and treatment, particularly during pandemics. In this work, we introduce MultiMed, the first multilingual medical ASR dataset, along with the first collection of small-to-large end-to-end medical ASR models, spanning five languages: Vietnamese, English, German, French, and Mandarin Chinese. To our best knowledge, MultiMed stands as the world's largest medical ASR dataset across all major benchmarks: total duration, number of recording conditions, number of accents, and number of speaking roles. Furthermore, we present the first multilinguality study for medical ASR, which includes reproducible empirical baselines, a monolinguality-multilinguality analysis, Attention Encoder Decoder (AED) vs Hybrid comparative study and a linguistic analysis. We present practical ASR end-to-end training schemes optimized for a fixed number of trainable parameters that are common in industry settings. All code, data, and models are available online: https://github.com/leduckhai/MultiMed/tree/master/MultiMed.

</details>

### [Time and Tokens: Benchmarking End-to-End Speech Dysfluency Detection](2409.13582.md)
**Xuanru Zhou, Jiachen Lian, Cheol Jun Cho, Jingwen Liu et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

Speech dysfluency modeling is a task to detect dysfluencies in speech, such as repetition, block, insertion, replacement, and deletion. Most recent advancements treat this problem as a time-based object detection problem. In this work, we revisit this problem from a new perspective: tokenizing dysfluencies and modeling the detection problem as a token-based automatic speech recognition (ASR) problem. We propose rule-based speech and text dysfluency simulators and develop VCTK-token, and then develop a Whisper-like seq2seq architecture to build a new benchmark with decent performance. We also systematically compare our proposed token-based methods with time-based methods, and propose a unified benchmark to facilitate future research endeavors. We open-source these resources for the broader scientific community. The project page is available at https://rorizzz.github.io/

</details>

### [Unifying Global and Near-Context Biasing in a Single Trie Pass](2409.13514.md)
**Iuliia Thorbecke, Esaú Villatoro-Tello, Juan Zuluaga-Gomez, Shashi Kumar et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

Despite the success of end-to-end automatic speech recognition (ASR) models, challenges persist in recognizing rare, out-of-vocabulary words - including named entities (NE) - and in adapting to new domains using only text data. This work presents a practical approach to address these challenges through an unexplored combination of an NE bias list and a word-level n-gram language model (LM). This solution balances simplicity and effectiveness, improving entities' recognition while maintaining or even enhancing overall ASR performance. We efficiently integrate this enriched biasing method into a transducer-based ASR system, enabling context adaptation with almost no computational overhead. We present our results on three datasets spanning four languages and compare them to state-of-the-art biasing strategies. We demonstrate that the proposed combination of keyword biasing and n-gram LM improves entity recognition by up to 32% relative and reduces overall WER by up to a 12% relative.

</details>

### [Fast Streaming Transducer ASR Prototyping via Knowledge Distillation with Whisper](2409.13499.md)
**Iuliia Thorbecke, Juan Zuluaga-Gomez, Esaú Villatoro-Tello, Shashi Kumar et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

The training of automatic speech recognition (ASR) with little to no supervised data remains an open question. In this work, we demonstrate that streaming Transformer-Transducer (TT) models can be trained from scratch in consumer and accessible GPUs in their entirety with pseudo-labeled (PL) speech from foundational speech models (FSM). This allows training a robust ASR model just in one stage and does not require large data and computational budget compared to the two-step scenario with pre-training and fine-tuning. We perform a comprehensive ablation on different aspects of PL-based streaming TT models such as the impact of (1) shallow fusion of n-gram LMs, (2) contextual biasing with named entities, (3) chunk-wise decoding for low-latency streaming applications, and (4) TT overall performance as the function of the FSM size. Our results demonstrate that TT can be trained from scratch without supervised data, even with very noisy PLs. We validate the proposed framework on 6 languages from CommonVoice and propose multiple heuristics to filter out hallucinated PLs.

</details>

### [A Multimodal Dense Retrieval Approach for Speech-Based Open-Domain Question Answering](2409.13483.md)
**Georgios Sidiropoulos, Evangelos Kanoulas** · 2024-09-20

<details>
<summary>Abstract</summary>

Speech-based open-domain question answering (QA over a large corpus of text passages with spoken questions) has emerged as an important task due to the increasing number of users interacting with QA systems via speech interfaces. Passage retrieval is a key task in speech-based open-domain QA. So far, previous works adopted pipelines consisting of an automatic speech recognition (ASR) model that transcribes the spoken question before feeding it to a dense text retriever. Such pipelines have several limitations. The need for an ASR model limits the applicability to low-resource languages and specialized domains with no annotated speech data. Furthermore, the ASR model propagates its errors to the retriever. In this work, we try to alleviate these limitations by proposing an ASR-free, end-to-end trained multimodal dense retriever that can work directly on spoken questions. Our experimental results showed that, on shorter questions, our retriever is a promising alternative to the \textit{ASR and Retriever} pipeline, achieving better retrieval performance in cases where ASR would have mistranscribed important words in the question or have produced a transcription with a high word error rate.

</details>

### [Large Language Model Should Understand Pinyin for Chinese ASR Error Correction](2409.13262.md)
**Yuang Li, Xiaosong Qiao, Xiaofeng Zhao, Huan Zhao et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

Large language models can enhance automatic speech recognition systems through generative error correction. In this paper, we propose Pinyin-enhanced GEC, which leverages Pinyi, the phonetic representation of Mandarin Chinese, as supplementary information to improve Chinese ASR error correction. Our approach only utilizes synthetic errors for training and employs the one-best hypothesis during inference. Additionally, we introduce a multitask training approach involving conversion tasks between Pinyin and text to align their feature spaces. Experiments on the Aishell-1 and the Common Voice datasets demonstrate that our approach consistently outperforms GEC with text-only input. More importantly, we provide intuitive explanations for the effectiveness of PY-GEC and multitask training from two aspects: 1) increased attention weight on Pinyin features; and 2) aligned feature space between Pinyin and text hidden states.

</details>

### [On the Feasibility of Fully AI-automated Vishing Attacks](2409.13793.md)
**João Figueiredo, Afonso Carvalho, Daniel Castro, Daniel Gonçalves et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

A vishing attack is a form of social engineering where attackers use phone calls to deceive individuals into disclosing sensitive information, such as personal data, financial information, or security credentials. Attackers exploit the perceived urgency and authenticity of voice communication to manipulate victims, often posing as legitimate entities like banks or tech support. Vishing is a particularly serious threat as it bypasses security controls designed to protect information. In this work, we study the potential for vishing attacks to escalate with the advent of AI. In theory, AI-powered software bots may have the ability to automate these attacks by initiating conversations with potential victims via phone calls and deceiving them into disclosing sensitive information. To validate this thesis, we introduce ViKing, an AI-powered vishing system developed using publicly available AI technology. It relies on a Large Language Model (LLM) as its core cognitive processor to steer conversations with victims, complemented by a pipeline of speech-to-text and text-to-speech modules that facilitate audio-text conversion in phone calls. Through a controlled social experiment involving 240 participants, we discovered that ViKing has successfully persuaded many participants to reveal sensitive information, even those who had been explicitly warned about the risk of vishing campaigns. Interactions with ViKing's bots were generally considered realistic. From these findings, we conclude that tools like ViKing may already be accessible to potential malicious actors, while also serving as an invaluable resource for cyber awareness programs.

</details>

### [Target word activity detector: An approach to obtain ASR word boundaries without lexicon](2409.13913.md)
**Sunit Sivasankaran, Eric Sun, Jinyu Li, Yan Huang et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

Obtaining word timestamp information from end-to-end (E2E) ASR models remains challenging due to the lack of explicit time alignment during training. This issue is further complicated in multilingual models. Existing methods, either rely on lexicons or introduce additional tokens, leading to scalability issues and increased computational costs. In this work, we propose a new approach to estimate word boundaries without relying on lexicons. Our method leverages word embeddings from sub-word token units and a pretrained ASR model, requiring only word alignment information during training. Our proposed method can scale-up to any number of languages without incurring any additional cost. We validate our approach using a multilingual ASR model trained on five languages and demonstrate its effectiveness against a strong baseline.

</details>

### [Enhancing Synthetic Training Data for Speech Commands: From ASR-Based Filtering to Domain Adaptation in SSL Latent Space](2409.12745.md)
**Sebastião Quintas, Isabelle Ferrané, Thomas Pellegrini** · 2024-09-19

<details>
<summary>Abstract</summary>

The use of synthetic speech as data augmentation is gaining increasing popularity in fields such as automatic speech recognition and speech classification tasks. Despite novel text-to-speech systems with voice cloning capabilities, that allow the usage of a larger amount of voices based on short audio segments, it is known that these systems tend to hallucinate and oftentimes produce bad data that will most likely have a negative impact on the downstream task. In the present work, we conduct a set of experiments around zero-shot learning with synthetic speech data for the specific task of speech commands classification. Our results on the Google Speech Commands dataset show that a simple ASR-based filtering method can have a big impact in the quality of the generated data, translating to a better performance. Furthermore, despite the good quality of the generated speech data, we also show that synthetic and real speech can still be easily distinguishable when using self-supervised (WavLM) features, an aspect further explored with a CycleGAN to bridge the gap between the two types of speech material.

</details>

### [Hidden in Plain Sound: Environmental Backdoor Poisoning Attacks on Whisper, and Mitigations](2409.12553.md)
**Jonatan Bartolini, Todor Stoyanov, Alberto Giaretta** · 2024-09-19

<details>
<summary>Abstract</summary>

Thanks to the popularisation of transformer-based models, speech recognition (SR) is gaining traction in various application fields, such as industrial and robotics environments populated with mission-critical devices. While transformer-based SR can provide various benefits for simplifying human-machine interfacing, the research on the cybersecurity aspects of these models is lacklustre. In particular, concerning backdoor poisoning attacks. In this paper, we propose a new poisoning approach that maps different environmental trigger sounds to target phrases of different lengths, during the fine-tuning phase. We test our approach on Whisper, one of the most popular transformer-based SR model, showing that it is highly vulnerable to our attack, under several testing conditions. To mitigate the attack proposed in this paper, we investigate the use of Silero VAD, a state-of-the-art voice activity detection (VAD) model, as a defence mechanism. Our experiments show that it is possible to use VAD models to filter out malicious triggers and mitigate our attacks, with a varying degree of success, depending on the type of trigger sound and testing conditions.

</details>

### [Disentangling Speakers in Multi-Talker Speech Recognition with Speaker-Aware CTC](2409.12388.md)
**Jiawen Kang, Lingwei Meng, Mingyu Cui, Yuejiao Wang et al.** · 2024-09-19

<details>
<summary>Abstract</summary>

Multi-talker speech recognition (MTASR) faces unique challenges in disentangling and transcribing overlapping speech. To address these challenges, this paper investigates the role of Connectionist Temporal Classification (CTC) in speaker disentanglement when incorporated with Serialized Output Training (SOT) for MTASR. Our visualization reveals that CTC guides the encoder to represent different speakers in distinct temporal regions of acoustic embeddings. Leveraging this insight, we propose a novel Speaker-Aware CTC (SACTC) training objective, based on the Bayes risk CTC framework. SACTC is a tailored CTC variant for multi-talker scenarios, it explicitly models speaker disentanglement by constraining the encoder to represent different speakers' tokens at specific time frames. When integrated with SOT, the SOT-SACTC model consistently outperforms standard SOT-CTC across various degrees of speech overlap. Specifically, we observe relative word error rate reductions of 10% overall and 15% on low-overlap speech. This work represents an initial exploration of CTC-based enhancements for MTASR tasks, offering a new perspective on speaker disentanglement in multi-talker speech recognition. The code is available at https://github.com/kjw11/Speaker-Aware-CTC.

</details>

### [Channel-Aware Domain-Adaptive Generative Adversarial Network for Robust Speech Recognition](2409.12386.md)
**Chien-Chun Wang, Li-Wei Chen, Cheng-Kang Chou, Hung-Shin Lee et al.** · 2024-09-19

<details>
<summary>Abstract</summary>

While pre-trained automatic speech recognition (ASR) systems demonstrate impressive performance on matched domains, their performance often degrades when confronted with channel mismatch stemming from unseen recording environments and conditions. To mitigate this issue, we propose a novel channel-aware data simulation method for robust ASR training. Our method harnesses the synergistic power of channel-extractive techniques and generative adversarial networks (GANs). We first train a channel encoder capable of extracting embeddings from arbitrary audio. On top of this, channel embeddings are extracted using a minimal amount of target-domain data and used to guide a GAN-based speech synthesizer. This synthesizer generates speech that faithfully preserves the phonetic content of the input while mimicking the channel characteristics of the target domain. We evaluate our method on the challenging Hakka Across Taiwan (HAT) and Taiwanese Across Taiwan (TAT) corpora, achieving relative character error rate (CER) reductions of 20.02% and 9.64%, respectively, compared to the baselines. These results highlight the efficacy of our channel-aware data simulation method for bridging the gap between source- and target-domain acoustics.

</details>

### [META-CAT: Speaker-Informed Speech Embeddings via Meta Information Concatenation for Multi-talker ASR](2409.12352.md)
**Jinhan Wang, Weiqing Wang, Kunal Dhawan, Taejin Park et al.** · 2024-09-18

<details>
<summary>Abstract</summary>

We propose a novel end-to-end multi-talker automatic speech recognition (ASR) framework that enables both multi-speaker (MS) ASR and target-speaker (TS) ASR. Our proposed model is trained in a fully end-to-end manner, incorporating speaker supervision from a pre-trained speaker diarization module. We introduce an intuitive yet effective method for masking ASR encoder activations using output from the speaker supervision module, a technique we term Meta-Cat (meta-information concatenation), that can be applied to both MS-ASR and TS-ASR. Our results demonstrate that the proposed architecture achieves competitive performance in both MS-ASR and TS-ASR tasks, without the need for traditional methods, such as neural mask estimation or masking at the audio or feature level. Furthermore, we demonstrate a glimpse of a unified dual-task model which can efficiently handle both MS-ASR and TS-ASR tasks. Thus, this work illustrates that a robust end-to-end multi-talker ASR framework can be implemented with a streamlined architecture, obviating the need for the complex speaker filtering mechanisms employed in previous studies.

</details>

### [Large Language Models are Strong Audio-Visual Speech Recognition Learners](2409.12319.md)
**Umberto Cappellazzo, Minsu Kim, Honglie Chen, Pingchuan Ma et al.** · 2024-09-18

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) have recently become a focal point of research due to their formidable multimodal understanding capabilities. For example, in the audio and speech domains, an LLM can be equipped with (automatic) speech recognition (ASR) abilities by just concatenating the audio tokens, computed with an audio encoder, and the text tokens to achieve state-of-the-art results. On the contrary, tasks like visual and audio-visual speech recognition (VSR/AVSR), which also exploit noise-invariant lip movement information, have received little or no attention. To bridge this gap, we propose Llama-AVSR, a new MLLM with strong audio-visual speech recognition capabilities. It leverages pre-trained audio and video encoders to produce modality-specific tokens which, together with the text tokens, are processed by a pre-trained LLM (e.g., Llama3.1-8B) to yield the resulting response in an auto-regressive fashion. Llama-AVSR requires a small number of trainable parameters as only modality-specific projectors and LoRA modules are trained whereas the multi-modal encoders and LLM are kept frozen. We evaluate our proposed approach on LRS3, the largest public AVSR benchmark, and we achieve new state-of-the-art results for the tasks of ASR and AVSR with a WER of 0.79% and 0.77%, respectively. To bolster our results, we investigate the key factors that underpin the effectiveness of Llama-AVSR: the choice of the pre-trained encoders and LLM, the efficient integration of LoRA modules, and the optimal performance-efficiency trade-off obtained via modality-aware compression rates.

</details>

### [Chain-of-Thought Prompting for Speech Translation](2409.11538.md)
**Ke Hu, Zhehuai Chen, Chao-Han Huck Yang, Piotr Żelasko et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated remarkable advancements in language understanding and generation. Building on the success of text-based LLMs, recent research has adapted these models to use speech embeddings for prompting, resulting in Speech-LLM models that exhibit strong performance in automatic speech recognition (ASR) and automatic speech translation (AST). In this work, we propose a novel approach to leverage ASR transcripts as prompts for AST in a Speech-LLM built on an encoder-decoder text LLM. The Speech-LLM model consists of a speech encoder and an encoder-decoder structure Megatron-T5. By first decoding speech to generate ASR transcripts and subsequently using these transcripts along with encoded speech for prompting, we guide the speech translation in a two-step process like chain-of-thought (CoT) prompting. Low-rank adaptation (LoRA) is used for the T5 LLM for model adaptation and shows superior performance to full model fine-tuning. Experimental results show that the proposed CoT prompting significantly improves AST performance, achieving an average increase of 2.4 BLEU points across 6 En->X or X->En AST tasks compared to speech prompting alone. Additionally, compared to a related CoT prediction method that predicts a concatenated sequence of ASR and AST transcripts, our method performs better by an average of 2 BLEU points.

</details>

### [M-BEST-RQ: A Multi-Channel Speech Foundation Model for Smart Glasses](2409.11494.md)
**Yufeng Yang, Desh Raj, Ju Lin, Niko Moritz et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

The growing popularity of multi-channel wearable devices, such as smart glasses, has led to a surge of applications such as targeted speech recognition and enhanced hearing. However, current approaches to solve these tasks use independently trained models, which may not benefit from large amounts of unlabeled data. In this paper, we propose M-BEST-RQ, the first multi-channel speech foundation model for smart glasses, which is designed to leverage large-scale self-supervised learning (SSL) in an array-geometry agnostic approach. While prior work on multi-channel speech SSL only evaluated on simulated settings, we curate a suite of real downstream tasks to evaluate our model, namely (i) conversational automatic speech recognition (ASR), (ii) spherical active source localization, and (iii) glasses wearer voice activity detection, which are sourced from the MMCSG and EasyCom datasets. We show that a general-purpose M-BEST-RQ encoder is able to match or surpass supervised models across all tasks. For the conversational ASR task in particular, using only 8 hours of labeled speech, our model outperforms a supervised ASR baseline that is trained on 2000 hours of labeled data, which demonstrates the effectiveness of our approach.

</details>

### [Moshi: a speech-text foundation model for real-time dialogue](2410.00037.md)
**Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

We introduce Moshi, a speech-text foundation model and full-duplex spoken dialogue framework. Current systems for spoken dialogue rely on pipelines of independent components, namely voice activity detection, speech recognition, textual dialogue and text-to-speech. Such frameworks cannot emulate the experience of real conversations. First, their complexity induces a latency of several seconds between interactions. Second, text being the intermediate modality for dialogue, non-linguistic information that modifies meaning -- such as emotion or non-speech sounds -- is lost in the interaction. Finally, they rely on a segmentation into speaker turns, which does not take into account overlapping speech, interruptions and interjections. Moshi solves these independent issues altogether by casting spoken dialogue as speech-to-speech generation. Starting from a text language model backbone, Moshi generates speech as tokens from the residual quantizer of a neural audio codec, while modeling separately its own speech and that of the user into parallel streams. This allows for the removal of explicit speaker turns, and the modeling of arbitrary conversational dynamics. We moreover extend the hierarchical semantic-to-acoustic token generation of previous work to first predict time-aligned text tokens as a prefix to audio tokens. Not only this "Inner Monologue" method significantly improves the linguistic quality of generated speech, but we also illustrate how it can provide streaming speech recognition and text-to-speech. Our resulting model is the first real-time full-duplex spoken large language model, with a theoretical latency of 160ms, 200ms in practice, and is available at https://github.com/kyutai-labs/moshi.

</details>

### [Bio-Inspired Mamba: Temporal Locality and Bioplausible Learning in Selective State Space Models](2409.11263.md)
**Jiahao Qin** · 2024-09-17

<details>
<summary>Abstract</summary>

This paper introduces Bio-Inspired Mamba (BIM), a novel online learning framework for selective state space models that integrates biological learning principles with the Mamba architecture. BIM combines Real-Time Recurrent Learning (RTRL) with Spike-Timing-Dependent Plasticity (STDP)-like local learning rules, addressing the challenges of temporal locality and biological plausibility in training spiking neural networks. Our approach leverages the inherent connection between backpropagation through time and STDP, offering a computationally efficient alternative that maintains the ability to capture long-range dependencies. We evaluate BIM on language modeling, speech recognition, and biomedical signal analysis tasks, demonstrating competitive performance against traditional methods while adhering to biological learning principles. Results show improved energy efficiency and potential for neuromorphic hardware implementation. BIM not only advances the field of biologically plausible machine learning but also provides insights into the mechanisms of temporal information processing in biological neural networks.

</details>

### [Ideal-LLM: Integrating Dual Encoders and Language-Adapted LLM for Multilingual Speech-to-Text](2409.11214.md)
**Hongfei Xue, Wei Ren, Xuelong Geng, Kun Wei et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

Integrating audio encoders with LLMs through connectors has enabled these models to process and comprehend audio modalities, significantly enhancing speech-to-text tasks, including automatic speech recognition (ASR) and automatic speech translation (AST). However, these methods often overlook the critical aspect of language adaptation in multilingual settings, relying instead on multilingual data without adequately addressing language differences. To address this gap, we propose the Ideal-LLM model, which employs dual multilingual encoders to enrich language feature information and utilizes a language-adapted connector to target the adaptation of each language specifically. By leveraging the complementary strengths of Whisper and MMS encoders, our approach ensures richer multilingual representations. Additionally, the language-adapted connector enhances modal transformation via a language weight selector tailored for each language. Experimental results demonstrate that Ideal-LLM significantly improves ASR performance, achieving a 32.6% relative reduction in average word error rates compared to the standard speech encoder integrated with LLMs and yields an average BLEU score of 36.78 for AST task.

</details>

### [Enhancing Code-switched Text-to-Speech Synthesis Capability in Large Language Models with only Monolingual Corpora](2409.10969.md)
**Jing Xu, Daxin Tan, Jiaqi Wang, Xiao Chen** · 2024-09-17

<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have shown potential in speech generation and recognition, their applications are mainly confined to monolingual scenarios, with limited explorations in code-switched (CS) contexts. In this paper, we propose a Code-Switched Large Language Model (CS-LLM) to enhance the code-switched text-to-speech synthesis (CS TTS) capability in LLMs with only monolingual corpora. Specifically, we begin by enhancing the multilingual speech processing ability of LLMs through multilingual speech recognition and synthesis tasks. Then, we develop an effective code-switched (CS) data construction strategy that splits and concatenates words from different monolingual speech corpora to equip LLMs with improved CS TTS ability. Experiments show that our approach outperforms baselines in CS TTS in terms of naturalness, speaker consistency and similarity even with limited data. Additionally, the constructed CS data further improves multilingual speech synthesis and recognition.

</details>

### [Speech Recognition for Analysis of Police Radio Communication](2409.10858.md)
**Tejes Srivastava, Ju-Chieh Chou, Priyank Shroff, Karen Livescu et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

Police departments around the world use two-way radio for coordination. These broadcast police communications (BPC) are a unique source of information about everyday police activity and emergency response. Yet BPC are not transcribed, and their naturalistic audio properties make automatic transcription challenging. We collect a corpus of roughly 62,000 manually transcribed radio transmissions (~46 hours of audio) to evaluate the feasibility of automatic speech recognition (ASR) using modern recognition models. We evaluate the performance of off-the-shelf speech recognizers, models fine-tuned on BPC data, and customized end-to-end models. We find that both human and machine transcription is challenging in this domain. Large off-the-shelf ASR models perform poorly, but fine-tuned models can reach the approximate range of human performance. Our work suggests directions for future work, including analysis of short utterances and potential miscommunication in police radio interactions. We make our corpus and data annotation pipeline available to other researchers, to enable further research on recognition and analysis of police communication.

</details>

### [SMILE: Speech Meta In-Context Learning for Low-Resource Language Automatic Speech Recognition](2409.10429.md)
**Ming-Hao Hsu, Hung-yi Lee** · 2024-09-16

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) models demonstrate outstanding performance on high-resource languages but face significant challenges when applied to low-resource languages due to limited training data and insufficient cross-lingual generalization. Existing adaptation strategies, such as shallow fusion, data augmentation, and direct fine-tuning, either rely on external resources, suffer computational inefficiencies, or fail in test-time adaptation scenarios. To address these limitations, we introduce Speech Meta In-Context LEarning (SMILE), an innovative framework that combines meta-learning with speech in-context learning (SICL). SMILE leverages meta-training from high-resource languages to enable robust, few-shot generalization to low-resource languages without explicit fine-tuning on the target domain. Extensive experiments on the ML-SUPERB benchmark show that SMILE consistently outperforms baseline methods, significantly reducing character and word error rates in training-free few-shot multilingual ASR tasks.

</details>

### [Augmenting Automatic Speech Recognition Models with Disfluency Detection](2409.10177.md)
**Robin Amann, Zhaolin Li, Barbara Bruno, Jan Niehues** · 2024-09-16

<details>
<summary>Abstract</summary>

Speech disfluency commonly occurs in conversational and spontaneous speech. However, standard Automatic Speech Recognition (ASR) models struggle to accurately recognize these disfluencies because they are typically trained on fluent transcripts. Current research mainly focuses on detecting disfluencies within transcripts, overlooking their exact location and duration in the speech. Additionally, previous work often requires model fine-tuning and addresses limited types of disfluencies. In this work, we present an inference-only approach to augment any ASR model with the ability to detect open-set disfluencies. We first demonstrate that ASR models have difficulty transcribing speech disfluencies. Next, this work proposes a modified Connectionist Temporal Classification(CTC)-based forced alignment algorithm from \cite{kurzinger2020ctc} to predict word-level timestamps while effectively capturing disfluent speech. Additionally, we develop a model to classify alignment gaps between timestamps as either containing disfluent speech or silence. This model achieves an accuracy of 81.62% and an F1-score of 80.07%. We test the augmentation pipeline of alignment gap detection and classification on a disfluent dataset. Our results show that we captured 74.13% of the words that were initially missed by the transcription, demonstrating the potential of this pipeline for downstream tasks.

</details>

### [Optimizing Dysarthria Wake-Up Word Spotting: An End-to-End Approach for SLT 2024 LRDWWS Challenge](2409.10076.md)
**Shuiyun Liu, Yuxiang Kong, Pengcheng Guo, Weiji Zhuang et al.** · 2024-09-16

<details>
<summary>Abstract</summary>

Speech has emerged as a widely embraced user interface across diverse applications. However, for individuals with dysarthria, the inherent variability in their speech poses significant challenges. This paper presents an end-to-end Pretrain-based Dual-filter Dysarthria Wake-up word Spotting (PD-DWS) system for the SLT 2024 Low-Resource Dysarthria Wake-Up Word Spotting Challenge. Specifically, our system improves performance from two key perspectives: audio modeling and dual-filter strategy. For audio modeling, we propose an innovative 2branch-d2v2 model based on the pre-trained data2vec2 (d2v2), which can simultaneously model automatic speech recognition (ASR) and wake-up word spotting (WWS) tasks through a unified multi-task finetuning paradigm. Additionally, a dual-filter strategy is introduced to reduce the false accept rate (FAR) while maintaining the same false reject rate (FRR). Experimental results demonstrate that our PD-DWS system achieves an FAR of 0.00321 and an FRR of 0.005, with a total score of 0.00821 on the test-B eval set, securing first place in the challenge.

</details>

### [Large Language Model Based Generative Error Correction: A Challenge and Baselines for Speech Recognition, Speaker Tagging, and Emotion Recognition](2409.09785.md)
**Chao-Han Huck Yang, Taejin Park, Yuan Gong, Yuanchao Li et al.** · 2024-09-15

<details>
<summary>Abstract</summary>

Given recent advances in generative AI technology, a key question is how large language models (LLMs) can enhance acoustic modeling tasks using text decoding results from a frozen, pretrained automatic speech recognition (ASR) model. To explore new capabilities in language modeling for speech processing, we introduce the generative speech transcription error correction (GenSEC) challenge. This challenge comprises three post-ASR language modeling tasks: (i) post-ASR transcription correction, (ii) speaker tagging, and (iii) emotion recognition. These tasks aim to emulate future LLM-based agents handling voice-based interfaces while remaining accessible to a broad audience by utilizing open pretrained language models or agent-based APIs. We also discuss insights from baseline evaluations, as well as lessons learned for designing future evaluations.

</details>

### [ASR Error Correction using Large Language Models](2409.09554.md)
**Rao Ma, Mengjie Qian, Mark Gales, Kate Knill** · 2024-09-14

<details>
<summary>Abstract</summary>

Error correction (EC) models play a crucial role in refining Automatic Speech Recognition (ASR) transcriptions, enhancing the readability and quality of transcriptions. Without requiring access to the underlying code or model weights, EC can improve performance and provide domain adaptation for black-box ASR systems. This work investigates the use of large language models (LLMs) for error correction across diverse scenarios. 1-best ASR hypotheses are commonly used as the input to EC models. We propose building high-performance EC models using ASR N-best lists which should provide more contextual information for the correction process. Additionally, the generation process of a standard EC model is unrestricted in the sense that any output sequence can be generated. For some scenarios, such as unseen domains, this flexibility may impact performance. To address this, we introduce a constrained decoding approach based on the N-best list or an ASR lattice. Finally, most EC models are trained for a specific ASR system requiring retraining whenever the underlying ASR system is changed. This paper explores the ability of EC models to operate on the output of different ASR systems. This concept is further extended to zero-shot error correction using LLMs, such as ChatGPT. Experiments on three standard datasets demonstrate the efficacy of our proposed methods for both Transducer and attention-based encoder-decoder ASR systems. In addition, the proposed method can serve as an effective method for model ensembling.

</details>

### [M$^{3}$V: A multi-modal multi-view approach for Device-Directed Speech Detection](2409.09284.md)
**Anna Wang, Da Liu, Zhiyu Zhang, Shengqiang Liu et al.** · 2024-09-14

<details>
<summary>Abstract</summary>

With the goal of more natural and human-like interaction with virtual voice assistants, recent research in the field has focused on full duplex interaction mode without relying on repeated wake-up words. This requires that in scenes with complex sound sources, the voice assistant must classify utterances as device-oriented or non-device-oriented. The dual-encoder structure, which is jointly modeled by text and speech, has become the paradigm of device-directed speech detection. However, in practice, these models often produce incorrect predictions for unaligned input pairs due to the unavoidable errors of automatic speech recognition (ASR).To address this challenge, we propose M$^{3}$V, a multi-modal multi-view approach for device-directed speech detection, which frames we frame the problem as a multi-view learning task that introduces unimodal views and a text-audio alignment view in the network besides the multi-modal. Experimental results show that M$^{3}$V significantly outperforms models trained using only single or multi-modality and surpasses human judgment performance on ASR error data for the first time.

</details>

### [Joint Semantic Knowledge Distillation and Masked Acoustic Modeling for Full-band Speech Restoration with Improved Intelligibility](2409.09357.md)
**Xiaoyu Liu, Xu Li, Joan Serrà, Santiago Pascual** · 2024-09-14

<details>
<summary>Abstract</summary>

Speech restoration aims at restoring full-band speech with high quality and intelligibility, considering a diverse set of distortions. MaskSR is a recently proposed generative model for this task. As other models of its kind, MaskSR attains high quality but, as we show, intelligibility can be substantially improved. We do so by boosting the speech encoder component of MaskSR with predictions of semantic representations of the target speech, using a pre-trained self-supervised teacher model. Then, a masked language model is conditioned on the learned semantic features to predict acoustic tokens that encode low level spectral details of the target speech. We show that, with the same MaskSR model capacity and inference time, the proposed model, MaskSR2, significantly reduces the word error rate, a typical metric for intelligibility. MaskSR2 also achieves competitive word error rate among other models, while providing superior quality. An ablation study shows the effectiveness of various semantic representations.

</details>

### [Multi-modal Speech Transformer Decoders: When Do Multiple Modalities Improve Accuracy?](2409.09221.md)
**Yiwen Guan, Viet Anh Trinh, Vivek Voleti, Jacob Whitehill** · 2024-09-13

<details>
<summary>Abstract</summary>

Decoder-only discrete-token language models have recently achieved significant success in automatic speech recognition. However, systematic analyses of how different modalities impact performance in specific scenarios remain limited. In this paper, we investigate the effects of multiple modalities on recognition accuracy on both synthetic and real-world datasets. Our experiments suggest that: (1) Integrating more modalities can increase accuracy; in particular, our paper is, to our best knowledge, the first to show the benefit of combining audio, image context, and lip information; (2) Images as a supplementary modality for speech recognition provide the greatest benefit at moderate noise levels, moreover, they exhibit a different trend compared to inherently synchronized modalities like lip movements; (3) Performance improves on both synthetic and real-world datasets when the most relevant visual information is filtered as a preprocessing step.

</details>

### [Exploring the Impact of Data Quantity on ASR in Extremely Low-resource Languages](2409.08872.md)
**Yao-Fei Cheng, Li-Wei Chen, Hung-Shin Lee, Hsin-Min Wang** · 2024-09-13

<details>
<summary>Abstract</summary>

This study investigates the efficacy of data augmentation techniques for low-resource automatic speech recognition (ASR), focusing on two endangered Austronesian languages, Amis and Seediq. Recognizing the potential of self-supervised learning (SSL) in low-resource settings, we explore the impact of data volume on the continued pre-training of SSL models. We propose a novel data-selection scheme leveraging a multilingual corpus to augment the limited target language data. This scheme utilizes a language classifier to extract utterance embeddings and employs one-class classifiers to identify utterances phonetically and phonologically proximate to the target languages. Utterances are ranked and selected based on their decision scores, ensuring the inclusion of highly relevant data in the SSL-ASR pipeline. Our experimental results demonstrate the effectiveness of this approach, yielding substantial improvements in ASR performance for both Amis and Seediq. These findings underscore the feasibility and promise of data augmentation through cross-lingual transfer learning for low-resource language ASR.

</details>

### [Exploring SSL Discrete Tokens for Multilingual ASR](2409.08805.md)
**Mingyu Cui, Daxin Tan, Yifan Yang, Dingdong Wang et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

With the advancement of Self-supervised Learning (SSL) in speech-related tasks, there has been growing interest in utilizing discrete tokens generated by SSL for automatic speech recognition (ASR), as they offer faster processing techniques. However, previous studies primarily focused on multilingual ASR with Fbank features or English ASR with discrete tokens, leaving a gap in adapting discrete tokens for multilingual ASR scenarios. This study presents a comprehensive comparison of discrete tokens generated by various leading SSL models across multiple language domains. We aim to explore the performance and efficiency of speech discrete tokens across multiple language domains for both monolingual and multilingual ASR scenarios. Experimental results demonstrate that discrete tokens achieve comparable results against systems trained on Fbank features in ASR tasks across seven language domains with an average word error rate (WER) reduction of 0.31% and 1.76% absolute (2.80% and 15.70% relative) on dev and test sets respectively, with particularly WER reduction of 6.82% absolute (41.48% relative) on the Polish test set.

</details>

### [NEST-RQ: Next Token Prediction for Speech Self-Supervised Pre-Training](2409.08680.md)
**Minglun Han, Ye Bai, Chen Shen, Youjia Huang et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Speech self-supervised pre-training can effectively improve the performance of downstream tasks. However, previous self-supervised learning (SSL) methods for speech, such as HuBERT and BEST-RQ, focus on utilizing non-causal encoders with bidirectional context, and lack sufficient support for downstream streaming models. To address this issue, we introduce the next token prediction based speech pre-training method with random-projection quantizer (NEST-RQ). NEST-RQ employs causal encoders with only left context and uses next token prediction (NTP) as the training task. On the large-scale dataset, compared to BEST-RQ, the proposed NEST-RQ achieves comparable performance on non-streaming automatic speech recognition (ASR) and better performance on streaming ASR. We also conduct analytical experiments in terms of the future context size of streaming ASR, the codebook quality of SSL and the model size of the encoder. In summary, the paper demonstrates the feasibility of the NTP in speech SSL and provides empirical evidence and insights for speech SSL research.

</details>

### [Large Language Model Can Transcribe Speech in Multi-Talker Scenarios with Versatile Instructions](2409.08596.md)
**Lingwei Meng, Shujie Hu, Jiawen Kang, Zhaoqing Li et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Recent advancements in large language models (LLMs) have revolutionized various domains, bringing significant progress and new opportunities. Despite progress in speech-related tasks, LLMs have not been sufficiently explored in multi-talker scenarios. In this work, we present a pioneering effort to investigate the capability of LLMs in transcribing speech in multi-talker environments, following versatile instructions related to multi-talker automatic speech recognition (ASR), target talker ASR, and ASR based on specific talker attributes such as sex, occurrence order, language, and keyword spoken. Our approach utilizes WavLM and Whisper encoder to extract multi-faceted speech representations that are sensitive to speaker characteristics and semantic context. These representations are then fed into an LLM fine-tuned using LoRA, enabling the capabilities for speech comprehension and transcription. Comprehensive experiments reveal the promising performance of our proposed system, MT-LLM, in cocktail party scenarios, highlighting the potential of LLM to handle speech-related tasks based on user instructions in such complex settings. The code, model, and samples are available at https://github.com/cuhealthybrains/MT-LLM.

</details>

### [Optimizing Rare Word Accuracy in Direct Speech Translation with a Retrieval-and-Demonstration Approach](2409.09009.md)
**Siqi Li, Danni Liu, Jan Niehues** · 2024-09-13

<details>
<summary>Abstract</summary>

Direct speech translation (ST) models often struggle with rare words. Incorrect translation of these words can have severe consequences, impacting translation quality and user trust. While rare word translation is inherently challenging for neural models due to sparse learning signals, real-world scenarios often allow access to translations of past recordings on similar topics. To leverage these valuable resources, we propose a retrieval-and-demonstration approach to enhance rare word translation accuracy in direct ST models. First, we adapt existing ST models to incorporate retrieved examples for rare word translation, which allows the model to benefit from prepended examples, similar to in-context learning. We then develop a cross-modal (speech-to-speech, speech-to-text, text-to-text) retriever to locate suitable examples. We demonstrate that standard ST models can be effectively adapted to leverage examples for rare word translation, improving rare word translation accuracy over the baseline by 17.6% with gold examples and 8.5% with retrieved examples. Moreover, our speech-to-speech retrieval approach outperforms other modalities and exhibits higher robustness to unseen speakers. Our code is publicly available (https://github.com/SiqiLii/Retrieve-and-Demonstration-ST).

</details>

### [Exploring SSL Discrete Speech Features for Zipformer-based Contextual ASR](2409.08797.md)
**Mingyu Cui, Yifan Yang, Jiajun Deng, Jiawen Kang et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) based discrete speech representations are highly compact and domain adaptable. In this paper, SSL discrete speech features extracted from WavLM models are used as additional cross-utterance acoustic context features in Zipformer-Transducer ASR systems. The efficacy of replacing Fbank features with discrete token features for modelling either cross-utterance contexts (from preceding and future segments), or current utterance's internal contexts alone, or both at the same time, are demonstrated thoroughly on the Gigaspeech 1000-hr corpus. The best Zipformer-Transducer system using discrete tokens based cross-utterance context features outperforms the baseline using utterance internal context only with statistically significant word error rate (WER) reductions of 0.32% to 0.41% absolute (2.78% to 3.54% relative) on the dev and test data. The lowest published WER of 11.15% and 11.14% were obtained on the dev and test sets. Our work is open-source and publicly available at https://github.com/open-creator/icefall/tree/master/egs/gigaspeech/Context\_ASR.

</details>

### [Faster Speech-LLaMA Inference with Multi-token Prediction](2409.08148.md)
**Desh Raj, Gil Keren, Junteng Jia, Jay Mahadeokar et al.** · 2024-09-12

<details>
<summary>Abstract</summary>

Large language models (LLMs) have become proficient at solving a wide variety of tasks, including those involving multi-modal inputs. In particular, instantiating an LLM (such as LLaMA) with a speech encoder and training it on paired data imparts speech recognition (ASR) abilities to the decoder-only model, hence called Speech-LLaMA. Nevertheless, due to the sequential nature of auto-regressive inference and the relatively large decoder, Speech-LLaMA models require relatively high inference time. In this work, we propose to speed up Speech-LLaMA inference by predicting multiple tokens in the same decoding step. We explore several model architectures that enable this, and investigate their performance using threshold-based and verification-based inference strategies. We also propose a prefix-based beam search decoding method that allows efficient minimum word error rate (MWER) training for such models. We evaluate our models on a variety of public benchmarks, where they reduce the number of decoder calls by ~3.2x while maintaining or improving WER performance.

</details>

### [Full-text Error Correction for Chinese Speech Recognition with Large Language Model](2409.07790.md)
**Zhiyuan Tang, Dong Wang, Shen Huang, Shidong Shang** · 2024-09-12

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated substantial potential for error correction in Automatic Speech Recognition (ASR). However, most research focuses on utterances from short-duration speech recordings, which are the predominant form of speech data for supervised ASR training. This paper investigates the effectiveness of LLMs for error correction in full-text generated by ASR systems from longer speech recordings, such as transcripts from podcasts, news broadcasts, and meetings. First, we develop a Chinese dataset for full-text error correction, named ChFT, utilizing a pipeline that involves text-to-speech synthesis, ASR, and error-correction pair extractor. This dataset enables us to correct errors across contexts, including both full-text and segment, and to address a broader range of error types, such as punctuation restoration and inverse text normalization, thus making the correction process comprehensive. Second, we fine-tune a pre-trained LLM on the constructed dataset using a diverse set of prompts and target formats, and evaluate its performance on full-text error correction. Specifically, we design prompts based on full-text and segment, considering various output formats, such as directly corrected text and JSON-based error-correction pairs. Through various test settings, including homogeneous, up-to-date, and hard test sets, we find that the fine-tuned LLMs perform well in the full-text setting with different prompts, each presenting its own strengths and weaknesses. This establishes a promising baseline for further research. The dataset is available on the website.

</details>

### [Contextualization of ASR with LLM using phonetic retrieval-based augmentation](2409.15353.md)
**Zhihong Lei, Xingyu Na, Mingbin Xu, Ernest Pusateri et al.** · 2024-09-11

<details>
<summary>Abstract</summary>

Large language models (LLMs) have shown superb capability of modeling multimodal signals including audio and text, allowing the model to generate spoken or textual response given a speech input. However, it remains a challenge for the model to recognize personal named entities, such as contacts in a phone book, when the input modality is speech. In this work, we start with a speech recognition task and propose a retrieval-based solution to contextualize the LLM: we first let the LLM detect named entities in speech without any context, then use this named entity as a query to retrieve phonetically similar named entities from a personal database and feed them to the LLM, and finally run context-aware LLM decoding. In a voice assistant task, our solution achieved up to 30.2% relative word error rate reduction and 73.6% relative named entity error rate reduction compared to a baseline system without contextualization. Notably, our solution by design avoids prompting the LLM with the full named entity database, making it highly efficient and applicable to large named entity databases.

</details>

### [Rethinking Mamba in Speech Processing by Self-Supervised Models](2409.07273.md)
**Xiangyu Zhang, Jianbo Ma, Mostafa Shahin, Beena Ahmed et al.** · 2024-09-11

<details>
<summary>Abstract</summary>

The Mamba-based model has demonstrated outstanding performance across tasks in computer vision, natural language processing, and speech processing. However, in the realm of speech processing, the Mamba-based model's performance varies across different tasks. For instance, in tasks such as speech enhancement and spectrum reconstruction, the Mamba model performs well when used independently. However, for tasks like speech recognition, additional modules are required to surpass the performance of attention-based models. We propose the hypothesis that the Mamba-based model excels in "reconstruction" tasks within speech processing. However, for "classification tasks" such as Speech Recognition, additional modules are necessary to accomplish the "reconstruction" step. To validate our hypothesis, we analyze the previous Mamba-based Speech Models from an information theory perspective. Furthermore, we leveraged the properties of HuBERT in our study. We trained a Mamba-based HuBERT model, and the mutual information patterns, along with the model's performance metrics, confirmed our assumptions.

</details>

### [Linear Time Complexity Conformers with SummaryMixing for Streaming Speech Recognition](2409.07165.md)
**Titouan Parcollet, Rogier van Dalen, Shucong Zhang, Sourav Batthacharya** · 2024-09-11

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) with an encoder equipped with self-attention, whether streaming or non-streaming, takes quadratic time in the length of the speech utterance. This slows down training and decoding, increase their cost, and limit the deployment of the ASR in constrained devices. SummaryMixing is a promising linear-time complexity alternative to self-attention for non-streaming speech recognition that, for the first time, preserves or outperforms the accuracy of self-attention models. Unfortunately, the original definition of SummaryMixing is not suited to streaming speech recognition. Hence, this work extends SummaryMixing to a Conformer Transducer that works in both a streaming and an offline mode. It shows that this new linear-time complexity speech encoder outperforms self-attention in both scenarios while requiring less compute and memory during training and decoding.

</details>

### [An Effective Context-Balanced Adaptation Approach for Long-Tailed Speech Recognition](2409.06468.md)
**Yi-Cheng Wang, Li-Ting Pai, Bi-Cheng Yan, Hsin-Wei Wang et al.** · 2024-09-10

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) models have become standard practice for various commercial applications. However, in real-world scenarios, the long-tailed nature of word distribution often leads E2E ASR models to perform well on common words but fall short in recognizing uncommon ones. Recently, the notion of a contextual adapter (CA) was proposed to infuse external knowledge represented by a context word list into E2E ASR models. Although CA can improve recognition performance on rare words, two crucial data imbalance problems remain. First, when using low-frequency words as context words during training, since these words rarely occur in the utterance, CA becomes prone to overfit on attending to the <no-context> token due to higher-frequency words not being present in the context list. Second, the long-tailed distribution within the context list itself still causes the model to perform poorly on low-frequency context words. In light of this, we explore in-depth the impact of altering the context list to have words with different frequency distributions on model performance, and meanwhile extend CA with a simple yet effective context-balanced learning objective. A series of experiments conducted on the AISHELL-1 benchmark dataset suggests that using all vocabulary words from the training corpus as the context list and pairing them with our balanced objective yields the best performance, demonstrating a significant reduction in character error rate (CER) by up to 1.21% and a more pronounced 9.44% reduction in the error rate of zero-shot words.

</details>

### [Advancing Topic Segmentation of Broadcasted Speech with Multilingual Semantic Embeddings](2409.06222.md)
**Sakshi Deo Shukla, Pavel Denisov, Tugtekin Turan** · 2024-09-10

<details>
<summary>Abstract</summary>

Recent advancements in speech-based topic segmentation have highlighted the potential of pretrained speech encoders to capture semantic representations directly from speech. Traditionally, topic segmentation has relied on a pipeline approach in which transcripts of the automatic speech recognition systems are generated, followed by text-based segmentation algorithms. In this paper, we introduce an end-to-end scheme that bypasses this conventional two-step process by directly employing semantic speech encoders for segmentation. Focused on the broadcasted news domain, which poses unique challenges due to the diversity of speakers and topics within single recordings, we address the challenge of accessing topic change points efficiently in an end-to-end manner. Furthermore, we propose a new benchmark for spoken news topic segmentation by utilizing a dataset featuring approximately 1000 hours of publicly available recordings across six European languages and including an evaluation set in Hindi to test the model's cross-domain performance in a cross-lingual, zero-shot scenario. This setup reflects real-world diversity and the need for models adapting to various linguistic settings. Our results demonstrate that while the traditional pipeline approach achieves a state-of-the-art $P_k$ score of 0.2431 for English, our end-to-end model delivers a competitive $P_k$ score of 0.2564. When trained multilingually, these scores further improve to 0.1988 and 0.2370, respectively. To support further research, we release our model along with data preparation scripts, facilitating open research on multilingual spoken news topic segmentation.

</details>

### [Sortformer: A Novel Approach for Permutation-Resolved Speaker Supervision in Speech-to-Text Systems](2409.06656.md)
**Taejin Park, Ivan Medennikov, Kunal Dhawan, Weiqing Wang et al.** · 2024-09-10

<details>
<summary>Abstract</summary>

Sortformer is an encoder-based speaker diarization model designed for supervising speaker tagging in speech-to-text models. Instead of relying solely on permutation invariant loss (PIL), Sortformer introduces Sort Loss to resolve the permutation problem, either independently or in tandem with PIL. In addition, we propose a streamlined multi-speaker speech-to-text architecture that leverages Sortformer for speaker supervision, embedding speaker labels into the encoder using sinusoidal kernel functions. This design addresses the speaker permutation problem through sorted objectives, effectively bridging timestamps and tokens to supervise speaker labels in the output transcriptions. Experiments demonstrate that Sort Loss can boost speaker diarization performance, and incorporating the speaker supervision from Sortformer improves multi-speaker transcription accuracy. We anticipate that the proposed Sortformer and multi-speaker architecture will enable the seamless integration of speaker tagging capabilities into foundational speech-to-text systems and multimodal large language models (LLMs), offering an easily adoptable and user-friendly mechanism to enhance their versatility and performance in speaker-aware tasks. The code and trained models are made publicly available through the NVIDIA NeMo Framework.

</details>

### [LLaMA-Omni: Seamless Speech Interaction with Large Language Models](2409.06666.md)
**Qingkai Fang, Shoutao Guo, Yan Zhou, Zhengrui Ma et al.** · 2024-09-10

<details>
<summary>Abstract</summary>

Models like GPT-4o enable real-time interaction with large language models (LLMs) through speech, significantly enhancing user experience compared to traditional text-based interaction. However, there is still a lack of exploration on how to build speech interaction models based on open-source LLMs. To address this, we propose LLaMA-Omni, a novel model architecture designed for low-latency and high-quality speech interaction with LLMs. LLaMA-Omni integrates a pretrained speech encoder, a speech adaptor, an LLM, and a streaming speech decoder. It eliminates the need for speech transcription, and can simultaneously generate text and speech responses directly from speech instructions with extremely low latency. We build our model based on the latest Llama-3.1-8B-Instruct model. To align the model with speech interaction scenarios, we construct a dataset named InstructS2S-200K, which includes 200K speech instructions and corresponding speech responses. Experimental results show that compared to previous speech-language models, LLaMA-Omni provides better responses in both content and style, with a response latency as low as 226ms. Additionally, training LLaMA-Omni takes less than 3 days on just 4 GPUs, paving the way for the efficient development of speech-language models in the future.

</details>

### [Retrieval Augmented Correction of Named Entity Speech Recognition Errors](2409.06062.md)
**Ernest Pusateri, Anmol Walia, Anirudh Kashi, Bortik Bandyopadhyay et al.** · 2024-09-09

<details>
<summary>Abstract</summary>

In recent years, end-to-end automatic speech recognition (ASR) systems have proven themselves remarkably accurate and performant, but these systems still have a significant error rate for entity names which appear infrequently in their training data. In parallel to the rise of end-to-end ASR systems, large language models (LLMs) have proven to be a versatile tool for various natural language processing (NLP) tasks. In NLP tasks where a database of relevant knowledge is available, retrieval augmented generation (RAG) has achieved impressive results when used with LLMs. In this work, we propose a RAG-like technique for correcting speech recognition entity name errors. Our approach uses a vector database to index a set of relevant entities. At runtime, database queries are generated from possibly errorful textual ASR hypotheses, and the entities retrieved using these queries are fed, along with the ASR hypotheses, to an LLM which has been adapted to correct ASR errors. Overall, our best system achieves 33%-39% relative word error rate reductions on synthetic test sets focused on voice assistant queries of rare music entities without regressing on the STOP test set, a publicly available voice assistant test set covering many domains.

</details>

### [Longer is (Not Necessarily) Stronger: Punctuated Long-Sequence Training for Enhanced Speech Recognition and Translation](2409.05601.md)
**Nithin Rao Koluguri, Travis Bartley, Hainan Xu, Oleksii Hrinchuk et al.** · 2024-09-09

<details>
<summary>Abstract</summary>

This paper presents a new method for training sequence-to-sequence models for speech recognition and translation tasks. Instead of the traditional approach of training models on short segments containing only lowercase or partial punctuation and capitalization (PnC) sentences, we propose training on longer utterances that include complete sentences with proper punctuation and capitalization. We achieve this by using the FastConformer architecture which allows training 1 Billion parameter models with sequences up to 60 seconds long with full attention. However, while training with PnC enhances the overall performance, we observed that accuracy plateaus when training on sequences longer than 40 seconds across various evaluation settings. Our proposed method significantly improves punctuation and capitalization accuracy, showing a 25% relative word error rate (WER) improvement on the Earnings-21 and Earnings-22 benchmarks. Additionally, training on longer audio segments increases the overall model accuracy across speech recognition and translation benchmarks. The model weights and training code are open-sourced though NVIDIA NeMo.

</details>

### [NTT Multi-Speaker ASR System for the DASR Task of CHiME-8 Challenge](2409.05554.md)
**Naoyuki Kamo, Naohiro Tawara, Atsushi Ando, Takatomo Kano et al.** · 2024-09-09

<details>
<summary>Abstract</summary>

We present a distant automatic speech recognition (DASR) system developed for the CHiME-8 DASR track. It consists of a diarization first pipeline. For diarization, we use end-to-end diarization with vector clustering (EEND-VC) followed by target speaker voice activity detection (TS-VAD) refinement. To deal with various numbers of speakers, we developed a new multi-channel speaker counting approach. We then apply guided source separation (GSS) with several improvements to the baseline system. Finally, we perform ASR using a combination of systems built from strong pre-trained models. Our proposed system achieves a macro tcpWER of 21.3 % on the dev set, which is a 57 % relative improvement over the baseline.

</details>

### [Efficient learning-based sound propagation for virtual and real-world audio processing applications](2409.15335.md)
**Anton Jeran Ratnarajah** · 2024-09-08

<details>
<summary>Abstract</summary>

Sound propagation is the process by which sound energy travels through a medium, such as air, to the surrounding environment as sound waves. The room impulse response (RIR) describes this process and is influenced by the positions of the source and listener, the room's geometry, and its materials. Physics-based acoustic simulators have been used for decades to compute accurate RIRs for specific acoustic environments. However, we have encountered limitations with existing acoustic simulators. To address these limitations, we propose three novel solutions. First, we introduce a learning-based RIR generator that is two orders of magnitude faster than an interactive ray-tracing simulator. Our approach can be trained to input both statistical and traditional parameters directly, and it can generate both monaural and binaural RIRs for both reconstructed and synthetic 3D scenes. Our generated RIRs outperform interactive ray-tracing simulators in speech-processing applications, including ASR, Speech Enhancement, and Speech Separation. Secondly, we propose estimating RIRs from reverberant speech signals and visual cues without a 3D representation of the environment. By estimating RIRs from reverberant speech, we can augment training data to match test data, improving the word error rate of the ASR system. Our estimated RIRs achieve a 6.9% improvement over previous learning-based RIR estimators in far-field ASR tasks. We demonstrate that our audio-visual RIR estimator aids tasks like visual acoustic matching, novel-view acoustic synthesis, and voice dubbing, validated through perceptual evaluation. Finally, we introduce IR-GAN to augment accurate RIRs using real RIRs. IR-GAN parametrically controls acoustic parameters learned from real RIRs to generate new RIRs that imitate different acoustic environments, outperforming Ray-tracing simulators on the far-field ASR benchmark by 8.95%.

</details>

### [LAST: Language Model Aware Speech Tokenization](2409.03701.md)
**Arnon Turetzky, Yossi Adi** · 2024-09-05

<details>
<summary>Abstract</summary>

Speech tokenization serves as the foundation of speech language model (LM), enabling them to perform various tasks such as spoken language modeling, text-to-speech, speech-to-text, etc. Most speech tokenizers are trained independently of the LM training process, relying on separate acoustic models and quantization methods. Following such an approach may create a mismatch between the tokenization process and its usage afterward. In this study, we propose a novel approach to training a speech tokenizer by leveraging objectives from pre-trained textual LMs. We advocate for the integration of this objective into the process of learning discrete speech representations. Our aim is to transform features from a pre-trained speech model into a new feature space that enables better clustering for speech LMs. We empirically investigate the impact of various model design choices, including speech vocabulary size and text LM size. Our results demonstrate the proposed tokenization method outperforms the evaluated baselines considering both spoken language modeling and speech-to-text. More importantly, unlike prior work, the proposed method allows the utilization of a single pre-trained LM for processing both speech and text inputs, setting it apart from conventional tokenization approaches.

</details>

### [Probing self-attention in self-supervised speech models for cross-linguistic differences](2409.03115.md)
**Sai Gopinath, Joselyn Rodriguez** · 2024-09-04

<details>
<summary>Abstract</summary>

Speech models have gained traction thanks to increase in accuracy from novel transformer architectures. While this impressive increase in performance across automatic speech recognition (ASR) benchmarks is noteworthy, there is still much that is unknown about the use of attention mechanisms for speech-related tasks. For example, while it is assumed that these models are learning language-independent (i.e., universal) speech representations, there has not yet been an in-depth exploration of what it would mean for the models to be language-independent. In the current paper, we explore this question within the realm of self-attention mechanisms of one small self-supervised speech transformer model (TERA). We find that even with a small model, the attention heads learned are diverse ranging from almost entirely diagonal to almost entirely global regardless of the training language. We highlight some notable differences in attention patterns between Turkish and English and demonstrate that the models do learn important phonological information during pretraining. We also present a head ablation study which shows that models across languages primarily rely on diagonal heads to classify phonemes.

</details>

### [Efficient Extraction of Noise-Robust Discrete Units from Self-Supervised Speech Models](2409.02565.md)
**Jakob Poncelet, Yujun Wang, Hugo Van hamme** · 2024-09-04

<details>
<summary>Abstract</summary>

Continuous speech can be converted into a discrete sequence by deriving discrete units from the hidden features of self-supervised learned (SSL) speech models. Although SSL models are becoming larger and trained on more data, they are often sensitive to real-life distortions like additive noise or reverberation, which translates to a shift in discrete units. We propose a parameter-efficient approach to generate noise-robust discrete units from pre-trained SSL models by training a small encoder-decoder model, with or without adapters, to simultaneously denoise and discretise the hidden features of the SSL model. The model learns to generate a clean discrete sequence for a noisy utterance, conditioned on the SSL features. The proposed denoiser outperforms several pre-training methods on the tasks of noisy discretisation and noisy speech recognition, and can be finetuned to the target environment with a few recordings of unlabeled target data.

</details>

### [Temporal Order Preserved Optimal Transport-based Cross-modal Knowledge Transfer Learning for ASR](2409.02239.md)
**Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai** · 2024-09-03

<details>
<summary>Abstract</summary>

Transferring linguistic knowledge from a pretrained language model (PLM) to an acoustic model has been shown to greatly improve the performance of automatic speech recognition (ASR). However, due to the heterogeneous feature distributions in cross-modalities, designing an effective model for feature alignment and knowledge transfer between linguistic and acoustic sequences remains a challenging task. Optimal transport (OT), which efficiently measures probability distribution discrepancies, holds great potential for aligning and transferring knowledge between acoustic and linguistic modalities. Nonetheless, the original OT treats acoustic and linguistic feature sequences as two unordered sets in alignment and neglects temporal order information during OT coupling estimation. Consequently, a time-consuming pretraining stage is required to learn a good alignment between the acoustic and linguistic representations. In this paper, we propose a Temporal Order Preserved OT (TOT)-based Cross-modal Alignment and Knowledge Transfer (CAKT) (TOT-CAKT) for ASR. In the TOT-CAKT, local neighboring frames of acoustic sequences are smoothly mapped to neighboring regions of linguistic sequences, preserving their temporal order relationship in feature alignment and matching. With the TOT-CAKT model framework, we conduct Mandarin ASR experiments with a pretrained Chinese PLM for linguistic knowledge transfer. Our results demonstrate that the proposed TOT-CAKT significantly improves ASR performance compared to several state-of-the-art models employing linguistic knowledge transfer, and addresses the weaknesses of the original OT-based method in sequential feature alignment for ASR.

</details>

### [The USTC-NERCSLIP Systems for the CHiME-8 NOTSOFAR-1 Challenge](2409.02041.md)
**Shutong Niu, Ruoyu Wang, Jun Du, Gaobin Yang et al.** · 2024-09-03

<details>
<summary>Abstract</summary>

This technical report outlines our submission system for the CHiME-8 NOTSOFAR-1 Challenge. The primary difficulty of this challenge is the dataset recorded across various conference rooms, which captures real-world complexities such as high overlap rates, background noises, a variable number of speakers, and natural conversation styles. To address these issues, we optimized the system in several aspects: For front-end speech signal processing, we introduced a data-driven joint training method for diarization and separation (JDS) to enhance audio quality. Additionally, we also integrated traditional guided source separation (GSS) for multi-channel track to provide complementary information for the JDS. For back-end speech recognition, we enhanced Whisper with WavLM, ConvNeXt, and Transformer innovations, applying multi-task training and Noise KLD augmentation, to significantly advance ASR robustness and accuracy. Our system attained a Time-Constrained minimum Permutation Word Error Rate (tcpWER) of 14.265% and 22.989% on the CHiME-8 NOTSOFAR-1 Dev-set-2 multi-channel and single-channel tracks, respectively.

</details>

### [Resource-Efficient Adaptation of Speech Foundation Models for Multi-Speaker ASR](2409.01438.md)
**Weiqing Wang, Kunal Dhawan, Taejin Park, Krishna C. Puvvada et al.** · 2024-09-02

<details>
<summary>Abstract</summary>

Speech foundation models have achieved state-of-the-art (SoTA) performance across various tasks, such as automatic speech recognition (ASR) in hundreds of languages. However, multi-speaker ASR remains a challenging task for these models due to data scarcity and sparsity. In this paper, we present approaches to enable speech foundation models to process and understand multi-speaker speech with limited training data. Specifically, we adapt a speech foundation model for the multi-speaker ASR task using only telephonic data. Remarkably, the adapted model also performs well on meeting data without any fine-tuning, demonstrating the generalization ability of our approach. We conduct several ablation studies to analyze the impact of different parameters and strategies on model performance. Our findings highlight the effectiveness of our methods. Results show that less parameters give better overall cpWER, which, although counter-intuitive, provides insights into adapting speech foundation models for multi-speaker ASR tasks with minimal annotated data.

</details>

### [Refined Statistical Bounds for Classification Error Mismatches with Constrained Bayes Error](2409.01309.md)
**Zijian Yang, Vahe Eminyan, Ralf Schlüter, Hermann Ney** · 2024-09-02

<details>
<summary>Abstract</summary>

In statistical classification/multiple hypothesis testing and machine learning, a model distribution estimated from the training data is usually applied to replace the unknown true distribution in the Bayes decision rule, which introduces a mismatch between the Bayes error and the model-based classification error. In this work, we derive the classification error bound to study the relationship between the Kullback-Leibler divergence and the classification error mismatch. We first reconsider the statistical bounds based on classification error mismatch derived in previous works, employing a different method of derivation. Then, motivated by the observation that the Bayes error is typically low in machine learning tasks like speech recognition and pattern recognition, we derive a refined Kullback-Leibler-divergence-based bound on the error mismatch with the constraint that the Bayes error is lower than a threshold.

</details>

### [Serialized Speech Information Guidance with Overlapped Encoding Separation for Multi-Speaker Automatic Speech Recognition](2409.00815.md)
**Hao Shi, Yuan Gao, Zhaoheng Ni, Tatsuya Kawahara** · 2024-09-01

<details>
<summary>Abstract</summary>

Serialized output training (SOT) attracts increasing attention due to its convenience and flexibility for multi-speaker automatic speech recognition (ASR). However, it is not easy to train with attention loss only. In this paper, we propose the overlapped encoding separation (EncSep) to fully utilize the benefits of the connectionist temporal classification (CTC) and attention hybrid loss. This additional separator is inserted after the encoder to extract the multi-speaker information with CTC losses. Furthermore, we propose the serialized speech information guidance SOT (GEncSep) to further utilize the separated encodings. The separated streams are concatenated to provide single-speaker information to guide attention during decoding. The experimental results on LibriMix show that the single-speaker encoding can be separated from the overlapped encoding. The CTC loss helps to improve the encoder representation under complex scenarios. GEncSep further improved performance.

</details>

### [Comparing Discrete and Continuous Space LLMs for Speech Recognition](2409.00800.md)
**Yaoxun Xu, Shi-Xiong Zhang, Jianwei Yu, Zhiyong Wu et al.** · 2024-09-01

<details>
<summary>Abstract</summary>

This paper investigates discrete and continuous speech representations in Large Language Model (LLM)-based Automatic Speech Recognition (ASR), organizing them by feature continuity and training approach into four categories: supervised and unsupervised for both discrete and continuous types. We further classify LLMs based on their input and autoregressive feedback into continuous and discrete-space models. Using specialized encoders and comparative analysis with a Joint-Training-From-Scratch Language Model (JTFS LM) and pre-trained LLaMA2-7b, we provide a detailed examination of their effectiveness. Our work marks the first extensive comparison of speech representations in LLM-based ASR and explores various modeling techniques. We present an open-sourced achievement of a state-of-the-art Word Error Rate (WER) of 1.69\% on LibriSpeech using a HuBERT encoder, offering valuable insights for advancing ASR and natural language processing (NLP) research.

</details>

### [TfCleanformer: A streaming, array-agnostic, full- and sub-band modeling front-end for robust ASR](s2:99613a1bca497202c19f89d90b47e6987582810f.md)
**Jens Heitkaemper, Joe Caroselli, Arun Narayanan, Nathan Howard** · 2024-09-01

<details>
<summary>Abstract</summary>

Multiple recent publications have demonstrated the benefits of neural network based enhancement in the time-frequency domain. This paper builds on those findings to improve upon a recently published streaming, array agnostic multi-channel enhancement system called Cleanformer. The proposed streaming enhancement system achieves competitive results against a non-causal state-of-the-art model on a source separation task, outperforming Cleanformer. Additionally, the presented model improves upon Cleanformer enhancement results in multiple challenging environments without introducing further latency. A short ablation study is performed to evaluate the influence of the proposed changes on the improved performance.

</details>

### [Enhancing Neural Transducer for Multilingual ASR with Synchronized Language Diarization](s2:8f6b595c7e09a7bec11726e8e1520c3eb693fec4.md)
**Amir Hussein, Desh Raj, Matthew Wiesner, Dan Povey et al.** · 2024-09-01

<details>
<summary>Abstract</summary>

In multilingual environments, seamless language switching, including code-switching (CS) within utterances, is essential for real-time applications. Conventional Automatic Speech Recognition (ASR) combined with language diarization requires post-processing to synchronize language labels with recognized words accurately, presenting a considerable challenge. In this study, we introduce a multitask learning framework that syn-chronizes Language Identification (LID) with ASR, utilizing a neural transducer architecture. This auxiliary task integrates both acoustic and lexical features to perform LID. Furthermore, we use resulting language representation as an auxiliary input to improve ASR. We demonstrate the efficacy of our proposed approach on conversational multilingual (Arabic, Spanish, Mandarin) and CS (Spanish-English, Mandarin-English) test sets.

</details>

### [Investigating ASR Error Correction with Large Language Model and Multilingual 1-best Hypotheses](s2:7ad2bcba24044c6e51ccf44a71c0f76c561ffbb4.md)
**Sheng Li, Chen Chen, C. Kwok, Chenhui Chu et al.** · 2024-09-01

### [ProGRes: Prompted Generative Rescoring on ASR n-Best](2409.00217.md)
**Ada Defne Tur, Adel Moumen, Mirco Ravanelli** · 2024-08-30

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have shown their ability to improve the performance of speech recognizers by effectively rescoring the n-best hypotheses generated during the beam search process. However, the best way to exploit recent generative instruction-tuned LLMs for hypothesis rescoring is still unclear. This paper proposes a novel method that uses instruction-tuned LLMs to dynamically expand the n-best speech recognition hypotheses with new hypotheses generated through appropriately-prompted LLMs. Specifically, we introduce a new zero-shot method for ASR n-best rescoring, which combines confidence scores, LLM sequence scoring, and prompt-based hypothesis generation. We compare Llama-3-Instruct, GPT-3.5 Turbo, and GPT-4 Turbo as prompt-based generators with Llama-3 as sequence scorer LLM. We evaluated our approach using different speech recognizers and observed significant relative improvement in the word error rate (WER) ranging from 5% to 25%.

</details>

### [Advancing Multi-talker ASR Performance with Large Language Models](2408.17431.md)
**Mohan Shi, Zengrui Jin, Yaoxun Xu, Yong Xu et al.** · 2024-08-30

<details>
<summary>Abstract</summary>

Recognizing overlapping speech from multiple speakers in conversational scenarios is one of the most challenging problem for automatic speech recognition (ASR). Serialized output training (SOT) is a classic method to address multi-talker ASR, with the idea of concatenating transcriptions from multiple speakers according to the emission times of their speech for training. However, SOT-style transcriptions, derived from concatenating multiple related utterances in a conversation, depend significantly on modeling long contexts. Therefore, compared to traditional methods that primarily emphasize encoder performance in attention-based encoder-decoder (AED) architectures, a novel approach utilizing large language models (LLMs) that leverages the capabilities of pre-trained decoders may be better suited for such complex and challenging scenarios. In this paper, we propose an LLM-based SOT approach for multi-talker ASR, leveraging pre-trained speech encoder and LLM, fine-tuning them on multi-talker dataset using appropriate strategies. Experimental results demonstrate that our approach surpasses traditional AED-based methods on the simulated dataset LibriMix and achieves state-of-the-art performance on the evaluation set of the real-world dataset AMI, outperforming the AED model trained with 1000 times more supervised data in previous works.

</details>

### [Developing an End-to-End Framework for Predicting the Social Communication Severity Scores of Children with Autism Spectrum Disorder](2409.00158.md)
**Jihyun Mun, Sunhee Kim, Minhwa Chung** · 2024-08-30

<details>
<summary>Abstract</summary>

Autism Spectrum Disorder (ASD) is a lifelong condition that significantly influencing an individual's communication abilities and their social interactions. Early diagnosis and intervention are critical due to the profound impact of ASD's characteristic behaviors on foundational developmental stages. However, limitations of standardized diagnostic tools necessitate the development of objective and precise diagnostic methodologies. This paper proposes an end-to-end framework for automatically predicting the social communication severity of children with ASD from raw speech data. This framework incorporates an automatic speech recognition model, fine-tuned with speech data from children with ASD, followed by the application of fine-tuned pre-trained language models to generate a final prediction score. Achieving a Pearson Correlation Coefficient of 0.6566 with human-rated scores, the proposed method showcases its potential as an accessible and objective tool for the assessment of ASD.

</details>

### [Speaker Tagging Correction With Non-Autoregressive Language Models](2409.00151.md)
**Grigor Kirakosyan, Davit Karamyan** · 2024-08-30

<details>
<summary>Abstract</summary>

Speech applications dealing with conversations require not only recognizing the spoken words but also determining who spoke when. The task of assigning words to speakers is typically addressed by merging the outputs of two separate systems, namely, an automatic speech recognition (ASR) system and a speaker diarization (SD) system. In practical settings, speaker diarization systems can experience significant degradation in performance due to a variety of factors, including uniform segmentation with a high temporal resolution, inaccurate word timestamps, incorrect clustering and estimation of speaker numbers, as well as background noise. Therefore, it is important to automatically detect errors and make corrections if possible. We used a second-pass speaker tagging correction system based on a non-autoregressive language model to correct mistakes in words placed at the borders of sentences spoken by different speakers. We first show that the employed error correction approach leads to reductions in word diarization error rate (WDER) on two datasets: TAL and test set of Fisher. Additionally, we evaluated our system in the Post-ASR Speaker Tagging Correction challenge and observed significant improvements in cpWER compared to baseline methods.

</details>

### [Generative Modeling Perspective for Control and Reasoning in Robotics](2408.17041.md)
**Takuma Yoneda** · 2024-08-30

<details>
<summary>Abstract</summary>

Heralded by the initial success in speech recognition and image classification, learning-based approaches with neural networks, commonly referred to as deep learning, have spread across various fields. A primitive form of a neural network functions as a deterministic mapping from one vector to another, parameterized by trainable weights. This is well suited for point estimation in which the model learns a one-to-one mapping (e.g., mapping a front camera view to a steering angle) that is required to solve the task of interest. Although learning such a deterministic, one-to-one mapping is effective, there are scenarios where modeling \emph{multimodal} data distributions, namely learning one-to-many relationships, is helpful or even necessary. In this thesis, we adopt a generative modeling perspective on robotics problems. Generative models learn and produce samples from multimodal distributions, rather than performing point estimation. We will explore the advantages this perspective offers for three topics in robotics.

</details>

### [CrisperWhisper: Accurate Timestamps on Verbatim Speech Transcriptions](2408.16589.md)
**Laurin Wagner, Bernhard Thallinger, Mario Zusag** · 2024-08-29

<details>
<summary>Abstract</summary>

We demonstrate that carefully adjusting the tokenizer of the Whisper speech recognition model significantly improves the precision of word-level timestamps when applying dynamic time warping to the decoder's cross-attention scores. We fine-tune the model to produce more verbatim speech transcriptions and employ several techniques to increase robustness against multiple speakers and background noise. These adjustments achieve state-of-the-art performance on benchmarks for verbatim speech transcription, word segmentation, and the timed detection of filler events, and can further mitigate transcription hallucinations. The code is available open https://github.com/nyrahealth/CrisperWhisper.

</details>

### [Human-Inspired Computing for Robust and Efficient Audio-Visual Speech Recognition](2408.16564.md)
**Qianhui Liu, Jiadong Wang, Yang Wang, Xin Yang et al.** · 2024-08-29

<details>
<summary>Abstract</summary>

Humans naturally perform audiovisual speech recognition (AVSR), enhancing the accuracy and robustness by integrating auditory and visual information. Spiking neural networks (SNNs), which mimic the brain's information-processing mechanisms, are well-suited for emulating the human capability of AVSR. Despite their potential, research on SNNs for AVSR is scarce, with most existing audio-visual multimodal methods focused on object or digit recognition. These models simply integrate features from both modalities, neglecting their unique characteristics and interactions. Additionally, they often rely on future information for current processing, which increases recognition latency and limits real-time applicability. Inspired by human speech perception, this paper proposes a novel human-inspired SNN named HI-AVSNN for AVSR, incorporating three key characteristics: cueing interaction, causal processing and spike activity. For cueing interaction, we propose a visual-cued auditory attention module (VCA2M) that leverages visual cues to guide attention to auditory features. We achieve causal processing by aligning the SNN's temporal dimension with that of visual and auditory features and applying temporal masking to utilize only past and current information. To implement spike activity, in addition to using SNNs, we leverage the event camera to capture lip movement as spikes, mimicking the human retina and providing efficient visual data. We evaluate HI-AVSNN on an audiovisual speech recognition dataset combining the DVS-Lip dataset with its corresponding audio samples. Experimental results demonstrate the superiority of our proposed fusion method, outperforming existing audio-visual SNN fusion methods and achieving a 2.27% improvement in accuracy over the only existing SNN-based AVSR method.

</details>

### [Benchmarking Japanese Speech Recognition on ASR-LLM Setups with Multi-Pass Augmented Generative Error Correction](2408.16180.md)
**Yuka Ko, Sheng Li, Chao-Han Huck Yang, Tatsuya Kawahara** · 2024-08-29

<details>
<summary>Abstract</summary>

With the strong representational power of large language models (LLMs), generative error correction (GER) for automatic speech recognition (ASR) aims to provide semantic and phonetic refinements to address ASR errors. This work explores how LLM-based GER can enhance and expand the capabilities of Japanese language processing, presenting the first GER benchmark for Japanese ASR with 0.9-2.6k text utterances. We also introduce a new multi-pass augmented generative error correction (MPA GER) by integrating multiple system hypotheses on the input side with corrections from multiple LLMs on the output side and then merging them. To the best of our knowledge, this is the first investigation of the use of LLMs for Japanese GER, which involves second-pass language modeling on the output transcriptions generated by the ASR system (e.g., N-best hypotheses). Our experiments demonstrated performance improvement in the proposed methods of ASR quality and generalization both in SPREDS-U1-ja and CSJ data.

</details>

### [Speech Recognition Transformers: Topological-lingualism Perspective](2408.14991.md)
**Shruti Singh, Muskaan Singh, Virender Kadyan** · 2024-08-27

<details>
<summary>Abstract</summary>

Transformers have evolved with great success in various artificial intelligence tasks. Thanks to our recent prevalence of self-attention mechanisms, which capture long-term dependency, phenomenal outcomes in speech processing and recognition tasks have been produced. The paper presents a comprehensive survey of transformer techniques oriented in speech modality. The main contents of this survey include (1) background of traditional ASR, end-to-end transformer ecosystem, and speech transformers (2) foundational models in a speech via lingualism paradigm, i.e., monolingual, bilingual, multilingual, and cross-lingual (3) dataset and languages, acoustic features, architecture, decoding, and evaluation metric from a specific topological lingualism perspective (4) popular speech transformer toolkit for building end-to-end ASR systems. Finally, highlight the discussion of open challenges and potential research directions for the community to conduct further research in this domain.

</details>

### [MEDSAGE: Enhancing Robustness of Medical Dialogue Summarization to ASR Errors with LLM-generated Synthetic Dialogues](2408.14418.md)
**Kuluhan Binici, Abhinav Ramesh Kashyap, Viktor Schlegel, Andy T. Liu et al.** · 2024-08-26

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems are pivotal in transcribing speech into text, yet the errors they introduce can significantly degrade the performance of downstream tasks like summarization. This issue is particularly pronounced in clinical dialogue summarization, a low-resource domain where supervised data for fine-tuning is scarce, necessitating the use of ASR models as black-box solutions. Employing conventional data augmentation for enhancing the noise robustness of summarization models is not feasible either due to the unavailability of sufficient medical dialogue audio recordings and corresponding ASR transcripts. To address this challenge, we propose MEDSAGE, an approach for generating synthetic samples for data augmentation using Large Language Models (LLMs). Specifically, we leverage the in-context learning capabilities of LLMs and instruct them to generate ASR-like errors based on a few available medical dialogue examples with audio recordings. Experimental results show that LLMs can effectively model ASR noise, and incorporating this noisy data into the training process significantly improves the robustness and accuracy of medical dialogue summarization systems. This approach addresses the challenges of noisy ASR outputs in critical applications, offering a robust solution to enhance the reliability of clinical dialogue summarization.

</details>

### [Self-supervised Speech Representations Still Struggle with African American Vernacular English](2408.14262.md)
**Kalvin Chang, Yi-Hui Chou, Jiatong Shi, Hsuan-Ming Chen et al.** · 2024-08-26

<details>
<summary>Abstract</summary>

Underperformance of ASR systems for speakers of African American Vernacular English (AAVE) and other marginalized language varieties is a well-documented phenomenon, and one that reinforces the stigmatization of these varieties. We investigate whether or not the recent wave of Self-Supervised Learning (SSL) speech models can close the gap in ASR performance between AAVE and Mainstream American English (MAE). We evaluate four SSL models (wav2vec 2.0, HuBERT, WavLM, and XLS-R) on zero-shot Automatic Speech Recognition (ASR) for these two varieties and find that these models perpetuate the bias in performance against AAVE. Additionally, the models have higher word error rates on utterances with more phonological and morphosyntactic features of AAVE. Despite the success of SSL speech models in improving ASR for low resource varieties, SSL pre-training alone may not bridge the gap between AAVE and MAE. Our code is publicly available at https://github.com/cmu-llab/s3m-aave.

</details>

### [Literary and Colloquial Tamil Dialect Identification](2408.13739.md)
**M. Nanmalar, P. Vijayalakshmi, T. Nagarajan** · 2024-08-25

<details>
<summary>Abstract</summary>

Culture and language evolve together. The old literary form of Tamil is used commonly for writing and the contemporary colloquial Tamil is used for speaking. Human-computer interaction applications require Colloquial Tamil (CT) to make it more accessible and easy for the everyday user and, it requires Literary Tamil (LT) when information is needed in a formal written format. Continuing the use of LT alongside CT in computer aided language learning applications will both preserve LT, and provide ease of use via CT, at the same time. Hence there is a need for the conversion between LT and CT dialects, which demands as a first step, dialect identification. Dialect Identification (DID) of LT and CT is an unexplored area of research. In the current work, keeping the nuances of both these dialects in mind, five methods are explored which include two implicit methods - Gaussian Mixture Model (GMM) and Convolutional Neural Network (CNN); two explicit methods - Parallel Phone Recognition (PPR) and Parallel Large Vocabulary Continuous Speech Recognition (P-LVCSR); two versions of the proposed explicit Unified Phone Recognition method (UPR-1 and UPR-2). These methods vary based on: the need for annotated data, the size of the unit, the way in which modelling is carried out, and the way in which the final decision is made. Even though the average duration of the test utterances is less - 4.9s for LT and 2.5s for CT - the systems performed well, offering the following identification accuracies: 87.72% (GMM), 93.97% (CNN), 89.24% (PPR), 94.21% (P-LVCSR), 88.57% (UPR-1), 93.53% (UPR-1 with P-LVCSR), 94.55% (UPR-2), and 95.61% (UPR-2 with P-LVCSR).

</details>

### [Ancient but Digitized: Developing Handwritten Optical Character Recognition for East Syriac Script Through Creating KHAMIS Dataset](2408.13631.md)
**Ameer Majeed, Hossein Hassani** · 2024-08-24

<details>
<summary>Abstract</summary>

Many languages have vast amounts of handwritten texts, such as ancient scripts about folktale stories and historical narratives or contemporary documents and letters. Digitization of those texts has various applications, such as daily tasks, cultural studies, and historical research. Syriac is an ancient, endangered, and low-resourced language that has not received the attention it requires and deserves. This paper reports on a research project aimed at developing a optical character recognition (OCR) model based on the handwritten Syriac texts as a starting point to build more digital services for this endangered language. A dataset was created, KHAMIS (inspired by the East Syriac poet, Khamis bar Qardahe), which consists of handwritten sentences in the East Syriac script. We used it to fine-tune the Tesseract-OCR engine's pretrained Syriac model on handwritten data. The data was collected from volunteers capable of reading and writing in the language to create KHAMIS. KHAMIS currently consists of 624 handwritten Syriac sentences collected from 31 university students and one professor, and it will be partially available online and the whole dataset available in the near future for development and research purposes. As a result, the handwritten OCR model was able to achieve a character error rate of 1.097-1.610% and 8.963-10.490% on both training and evaluation sets, respectively, and both a character error rate of 18.89-19.71% and a word error rate of 62.83-65.42% when evaluated on the test set, which is twice as better than the default Syriac model of Tesseract.

</details>

### [Focused Discriminative Training For Streaming CTC-Trained Automatic Speech Recognition Models](2408.13008.md)
**Adnan Haider, Xingyu Na, Erik McDermott, Tim Ng et al.** · 2024-08-23

<details>
<summary>Abstract</summary>

This paper introduces a novel training framework called Focused Discriminative Training (FDT) to further improve streaming word-piece end-to-end (E2E) automatic speech recognition (ASR) models trained using either CTC or an interpolation of CTC and attention-based encoder-decoder (AED) loss. The proposed approach presents a novel framework to identify and improve a model's recognition on challenging segments of an audio. Notably, this training framework is independent of hidden Markov models (HMMs) and lattices, eliminating the need for substantial decision-making regarding HMM topology, lexicon, and graph generation, as typically required in standard discriminative training approaches. Compared to additional fine-tuning with MMI or MWER loss on the encoder, FDT is shown to be more effective in achieving greater reductions in Word Error Rate (WER) on streaming models trained on LibriSpeech. Additionally, this method is shown to be effective in further improving a converged word-piece streaming E2E model trained on 600k hours of assistant and dictation dataset.

</details>

### [Positional Description for Numerical Normalization](2408.12430.md)
**Deepanshu Gupta, Javier Latorre** · 2024-08-22

<details>
<summary>Abstract</summary>

We present a Positional Description Scheme (PDS) tailored for digit sequences, integrating placeholder value information for each digit. Given the structural limitations of subword tokenization algorithms, language models encounter critical Text Normalization (TN) challenges when handling numerical tasks. Our schema addresses this challenge through straightforward pre-processing, preserving the model architecture while significantly simplifying number normalization, rendering the problem tractable. This simplifies the task and facilitates more compact production-ready models capable of learning from smaller datasets. Furthermore, our investigations reveal that PDS enhances the arithmetic processing capabilities of language models, resulting in a relative accuracy improvement of 23% to 51% on complex arithmetic tasks. We demonstrate that PDS effectively mitigates fatal numerical normalization errors in neural models, requiring only a modest amount of training data without rule-based Finite State Transducers (FST). We demonstrate that PDS is essential for both the Text-To-Speech and Speech Recognition text processing, enabling effective TN under production constraints.

</details>

### [Developing vocal system impaired patient-aimed voice quality assessment approach using ASR representation-included multiple features](2408.12279.md)
**Shaoxiang Dang, Tetsuya Matsumoto, Yoshinori Takeuchi, Takashi Tsuboi et al.** · 2024-08-22

<details>
<summary>Abstract</summary>

The potential of deep learning in clinical speech processing is immense, yet the hurdles of limited and imbalanced clinical data samples loom large. This article addresses these challenges by showcasing the utilization of automatic speech recognition and self-supervised learning representations, pre-trained on extensive datasets of normal speech. This innovative approach aims to estimate voice quality of patients with impaired vocal systems. Experiments involve checks on PVQD dataset, covering various causes of vocal system damage in English, and a Japanese dataset focusing on patients with Parkinson's disease before and after undergoing subthalamic nucleus deep brain stimulation (STN-DBS) surgery. The results on PVQD reveal a notable correlation (>0.8 on PCC) and an extraordinary accuracy (<0.5 on MSE) in predicting Grade, Breathy, and Asthenic indicators. Meanwhile, progress has been achieved in predicting the voice quality of patients in the context of STN-DBS.

</details>

### [Approaching Deep Learning through the Spectral Dynamics of Weights](2408.11804.md)
**David Yunis, Kumar Kshitij Patel, Samuel Wheeler, Pedro Savarese et al.** · 2024-08-21

<details>
<summary>Abstract</summary>

We propose an empirical approach centered on the spectral dynamics of weights -- the behavior of singular values and vectors during optimization -- to unify and clarify several phenomena in deep learning. We identify a consistent bias in optimization across various experiments, from small-scale ``grokking'' to large-scale tasks like image classification with ConvNets, image generation with UNets, speech recognition with LSTMs, and language modeling with Transformers. We also demonstrate that weight decay enhances this bias beyond its role as a norm regularizer, even in practical systems. Moreover, we show that these spectral dynamics distinguish memorizing networks from generalizing ones, offering a novel perspective on this longstanding conundrum. Additionally, we leverage spectral dynamics to explore the emergence of well-performing sparse subnetworks (lottery tickets) and the structure of the loss surface through linear mode connectivity. Our findings suggest that spectral dynamics provide a coherent framework to better understand the behavior of neural networks across diverse settings.

</details>

### [Improving Speech Recognition Error Prediction for Modern and Off-the-shelf Speech Recognizers](2408.11258.md)
**Prashant Serai, Peidong Wang, Eric Fosler-Lussier** · 2024-08-21

<details>
<summary>Abstract</summary>

Modeling the errors of a speech recognizer can help simulate errorful recognized speech data from plain text, which has proven useful for tasks like discriminative language modeling, improving robustness of NLP systems, where limited or even no audio data is available at train time. Previous work typically considered replicating behavior of GMM-HMM based systems, but the behavior of more modern posterior-based neural network acoustic models is not the same and requires adjustments to the error prediction model. In this work, we extend a prior phonetic confusion based model for predicting speech recognition errors in two ways: first, we introduce a sampling-based paradigm that better simulates the behavior of a posterior-based acoustic model. Second, we investigate replacing the confusion matrix with a sequence-to-sequence model in order to introduce context dependency into the prediction. We evaluate the error predictors in two ways: first by predicting the errors made by a Switchboard ASR system on unseen data (Fisher), and then using that same predictor to estimate the behavior of an unrelated cloud-based ASR system on a novel task. Sampling greatly improves predictive accuracy within a 100-guess paradigm, while the sequence model performs similarly to the confusion matrix.

</details>

### [AI-Based IVR](2408.10549.md)
**Gassyrbek Kosherbay, Nurgissa Apbaz** · 2024-08-20

<details>
<summary>Abstract</summary>

The use of traditional IVR (Interactive Voice Response) methods often proves insufficient to meet customer needs. This article examines the application of artificial intelligence (AI) technologies to enhance the efficiency of IVR systems in call centers. A proposed approach is based on the integration of speech-to-text conversion solutions, text query classification using large language models (LLM), and speech synthesis. Special attention is given to adapting these technologies to work with the Kazakh language, including fine-tuning models on specialized datasets. The practical aspects of implementing the developed system in a real call center for query classification are described. The research results demonstrate that the application of AI technologies in call center IVR systems reduces operator workload, improves customer service quality, and increases the efficiency of query processing. The proposed approach can be adapted for use in call centers operating with various languages.

</details>

### [Toward Large-scale Spiking Neural Networks: A Comprehensive Survey and Future Directions](2409.02111.md)
**Yangfan Hu, Qian Zheng, Guoqi Li, Huajin Tang et al.** · 2024-08-19

<details>
<summary>Abstract</summary>

Deep learning has revolutionized artificial intelligence (AI), achieving remarkable progress in fields such as computer vision, speech recognition, and natural language processing. Moreover, the recent success of large language models (LLMs) has fueled a surge in research on large-scale neural networks. However, the escalating demand for computing resources and energy consumption has prompted the search for energy-efficient alternatives. Inspired by the human brain, spiking neural networks (SNNs) promise energy-efficient computation with event-driven spikes. To provide future directions toward building energy-efficient large SNN models, we present a survey of existing methods for developing deep spiking neural networks, with a focus on emerging Spiking Transformers. Our main contributions are as follows: (1) an overview of learning methods for deep spiking neural networks, categorized by ANN-to-SNN conversion and direct training with surrogate gradients; (2) an overview of network architectures for deep spiking neural networks, categorized by deep convolutional neural networks (DCNNs) and Transformer architecture; and (3) a comprehensive comparison of state-of-the-art deep SNNs with a focus on emerging Spiking Transformers. We then further discuss and outline future directions toward large-scale SNNs.

</details>

### [A Transcription Prompt-based Efficient Audio Large Language Model for Robust Speech Recognition](2408.09491.md)
**Yangze Li, Xiong Wang, Songjun Cao, Yike Zhang et al.** · 2024-08-18

<details>
<summary>Abstract</summary>

Audio-LLM introduces audio modality into a large language model (LLM) to enable a powerful LLM to recognize, understand, and generate audio. However, during speech recognition in noisy environments, we observed the presence of illusions and repetition issues in audio-LLM, leading to substitution and insertion errors. This paper proposes a transcription prompt-based audio-LLM by introducing an ASR expert as a transcription tokenizer and a hybrid Autoregressive (AR) Non-autoregressive (NAR) decoding approach to solve the above problems. Experiments on 10k-hour WenetSpeech Mandarin corpus show that our approach decreases 12.2% and 9.6% CER relatively on Test_Net and Test_Meeting evaluation sets compared with baseline. Notably, we reduce the decoding repetition rate on the evaluation set to zero, showing that the decoding repetition problem has been solved fundamentally.

</details>

### [Generating Data with Text-to-Speech and Large-Language Models for Conversational Speech Recognition](2408.09215.md)
**Samuele Cornell, Jordan Darefsky, Zhiyao Duan, Shinji Watanabe** · 2024-08-17

<details>
<summary>Abstract</summary>

Currently, a common approach in many speech processing tasks is to leverage large scale pre-trained models by fine-tuning them on in-domain data for a particular application. Yet obtaining even a small amount of such data can be problematic, especially for sensitive domains and conversational speech scenarios, due to both privacy issues and annotation costs. To address this, synthetic data generation using single speaker datasets has been employed. Yet, for multi-speaker cases, such an approach often requires extensive manual effort and is prone to domain mismatches. In this work, we propose a synthetic data generation pipeline for multi-speaker conversational ASR, leveraging a large language model (LLM) for content creation and a conversational multi-speaker text-to-speech (TTS) model for speech synthesis. We conduct evaluation by fine-tuning the Whisper ASR model for telephone and distant conversational speech settings, using both in-domain data and generated synthetic data. Our results show that the proposed method is able to significantly outperform classical multi-speaker generation approaches that use external, non-conversational speech datasets.

</details>

### [Enhancing Large Language Model-based Speech Recognition by Contextualization for Rare and Ambiguous Words](2408.08027.md)
**Kento Nozawa, Takashi Masuko, Toru Taniguchi** · 2024-08-15

<details>
<summary>Abstract</summary>

We develop a large language model (LLM) based automatic speech recognition (ASR) system that can be contextualized by providing keywords as prior information in text prompts. We adopt decoder-only architecture and use our in-house LLM, PLaMo-100B, pre-trained from scratch using datasets dominated by Japanese and English texts as the decoder. We adopt a pre-trained Whisper encoder as an audio encoder, and the audio embeddings from the audio encoder are projected to the text embedding space by an adapter layer and concatenated with text embeddings converted from text prompts to form inputs to the decoder. By providing keywords as prior information in the text prompts, we can contextualize our LLM-based ASR system without modifying the model architecture to transcribe ambiguous words in the input audio accurately. Experimental results demonstrate that providing keywords to the decoder can significantly improve the recognition performance of rare and ambiguous words.

</details>

### [DPSNN: Spiking Neural Network for Low-Latency Streaming Speech Enhancement](2408.07388.md)
**Tao Sun, Sander Bohté** · 2024-08-14

<details>
<summary>Abstract</summary>

Speech enhancement (SE) improves communication in noisy environments, affecting areas such as automatic speech recognition, hearing aids, and telecommunications. With these domains typically being power-constrained and event-based while requiring low latency, neuromorphic algorithms in the form of spiking neural networks (SNNs) have great potential. Yet, current effective SNN solutions require a contextual sampling window imposing substantial latency, typically around 32ms, too long for many applications. Inspired by Dual-Path Spiking Neural Networks (DPSNNs) in classical neural networks, we develop a two-phase time-domain streaming SNN framework -- the Dual-Path Spiking Neural Network (DPSNN). In the DPSNN, the first phase uses Spiking Convolutional Neural Networks (SCNNs) to capture global contextual information, while the second phase uses Spiking Recurrent Neural Networks (SRNNs) to focus on frequency-related features. In addition, the regularizer suppresses activation to further enhance energy efficiency of our DPSNNs. Evaluating on the VCTK and Intel DNS Datasets, we demonstrate that our approach achieves the very low latency (approximately 5ms) required for applications like hearing aids, while demonstrating excellent signal-to-noise ratio (SNR), perceptual quality, and energy efficiency.

</details>

### [CMU's IWSLT 2024 Simultaneous Speech Translation System](2408.07452.md)
**Xi Xu, Siqi Ouyang, Brian Yan, Patrick Fernandes et al.** · 2024-08-14

<details>
<summary>Abstract</summary>

This paper describes CMU's submission to the IWSLT 2024 Simultaneous Speech Translation (SST) task for translating English speech to German text in a streaming manner. Our end-to-end speech-to-text (ST) system integrates the WavLM speech encoder, a modality adapter, and the Llama2-7B-Base model as the decoder. We employ a two-stage training approach: initially, we align the representations of speech and text, followed by full fine-tuning. Both stages are trained on MuST-c v2 data with cross-entropy loss. We adapt our offline ST model for SST using a simple fixed hold-n policy. Experiments show that our model obtains an offline BLEU score of 31.1 and a BLEU score of 29.5 under 2 seconds latency on the MuST-C-v2 tst-COMMON.

</details>

### [Style-Talker: Finetuning Audio Language Model and Style-Based Text-to-Speech Model for Fast Spoken Dialogue Generation](2408.11849.md)
**Yinghao Aaron Li, Xilin Jiang, Jordan Darefsky, Ge Zhu et al.** · 2024-08-13

<details>
<summary>Abstract</summary>

The rapid advancement of large language models (LLMs) has significantly propelled the development of text-based chatbots, demonstrating their capability to engage in coherent and contextually relevant dialogues. However, extending these advancements to enable end-to-end speech-to-speech conversation bots remains a formidable challenge, primarily due to the extensive dataset and computational resources required. The conventional approach of cascading automatic speech recognition (ASR), LLM, and text-to-speech (TTS) models in a pipeline, while effective, suffers from unnatural prosody because it lacks direct interactions between the input audio and its transcribed text and the output audio. These systems are also limited by their inherent latency from the ASR process for real-time applications. This paper introduces Style-Talker, an innovative framework that fine-tunes an audio LLM alongside a style-based TTS model for fast spoken dialog generation. Style-Talker takes user input audio and uses transcribed chat history and speech styles to generate both the speaking style and text for the response. Subsequently, the TTS model synthesizes the speech, which is then played back to the user. While the response speech is being played, the input speech undergoes ASR processing to extract the transcription and speaking style, serving as the context for the ensuing dialogue turn. This novel pipeline accelerates the traditional cascade ASR-LLM-TTS systems while integrating rich paralinguistic information from input speech. Our experimental results show that Style-Talker significantly outperforms the conventional cascade and speech-to-speech baselines in terms of both dialogue naturalness and coherence while being more than 50% faster.

</details>

### [Enhancing Dialogue Speech Recognition with Robust Contextual Awareness via Noise Representation Learning](2408.06043.md)
**Wonjun Lee, San Kim, Gary Geunbae Lee** · 2024-08-12

<details>
<summary>Abstract</summary>

Recent dialogue systems rely on turn-based spoken interactions, requiring accurate Automatic Speech Recognition (ASR). Errors in ASR can significantly impact downstream dialogue tasks. To address this, using dialogue context from user and agent interactions for transcribing subsequent utterances has been proposed. This method incorporates the transcription of the user's speech and the agent's response as model input, using the accumulated context generated by each turn. However, this context is susceptible to ASR errors because it is generated by the ASR model in an auto-regressive fashion. Such noisy context can further degrade the benefits of context input, resulting in suboptimal ASR performance. In this paper, we introduce Context Noise Representation Learning (CNRL) to enhance robustness against noisy context, ultimately improving dialogue speech recognition accuracy. To maximize the advantage of context awareness, our approach includes decoder pre-training using text-based dialogue data and noise representation learning for a context encoder. Based on the evaluation of speech dialogues, our method shows superior results compared to baselines. Furthermore, the strength of our approach is highlighted in noisy environments where user speech is barely audible due to real-world noise, relying on contextual information to transcribe the input accurately.

</details>

### [LI-TTA: Language Informed Test-Time Adaptation for Automatic Speech Recognition](2408.05769.md)
**Eunseop Yoon, Hee Suk Yoon, John Harvill, Mark Hasegawa-Johnson et al.** · 2024-08-11

<details>
<summary>Abstract</summary>

Test-Time Adaptation (TTA) has emerged as a crucial solution to the domain shift challenge, wherein the target environment diverges from the original training environment. A prime exemplification is TTA for Automatic Speech Recognition (ASR), which enhances model performance by leveraging output prediction entropy minimization as a self-supervision signal. However, a key limitation of this self-supervision lies in its primary focus on acoustic features, with minimal attention to the linguistic properties of the input. To address this gap, we propose Language Informed Test-Time Adaptation (LI-TTA), which incorporates linguistic insights during TTA for ASR. LI-TTA integrates corrections from an external language model to merge linguistic with acoustic information by minimizing the CTC loss from the correction alongside the standard TTA loss. With extensive experiments, we show that LI-TTA effectively improves the performance of TTA for ASR in various distribution shift situations.

</details>

### [Improving Whisper's Recognition Performance for Under-Represented Language Kazakh Leveraging Unpaired Speech and Text](2408.05554.md)
**Jinpeng Li, Yu Pu, Qi Sun, Wei-Qiang Zhang** · 2024-08-10

<details>
<summary>Abstract</summary>

Whisper and other large-scale automatic speech recognition models have made significant progress in performance. However, their performance on many low-resource languages, such as Kazakh, is not satisfactory. It is worth researching how to utilize low-cost data to improve the performance of Whisper on under-represented languages. In this study, we utilized easily accessible unpaired speech and text data and combined the language model GPT with Whisper on Kazakh. We implemented end of transcript (EOT) judgment modification and hallucination penalty to improve the performance of speech recognition. Further, we employed the decoding average token log probability as a criterion to select samples from unlabeled speech data and used pseudo-labeled data to fine-tune the model to further improve its performance. Ultimately, we achieved more than 10\% absolute WER reduction in multiple experiments, and the whole process has the potential to be generalized to other under-represented languages.

</details>

### [HydraFormer: One Encoder For All Subsampling Rates](2408.04325.md)
**Yaoxun Xu, Xingchen Song, Zhiyong Wu, Di Wu et al.** · 2024-08-08

<details>
<summary>Abstract</summary>

In automatic speech recognition, subsampling is essential for tackling diverse scenarios. However, the inadequacy of a single subsampling rate to address various real-world situations often necessitates training and deploying multiple models, consequently increasing associated costs. To address this issue, we propose HydraFormer, comprising HydraSub, a Conformer-based encoder, and a BiTransformer-based decoder. HydraSub encompasses multiple branches, each representing a distinct subsampling rate, allowing for the flexible selection of any branch during inference based on the specific use case. HydraFormer can efficiently manage different subsampling rates, significantly reducing training and deployment expenses. Experiments on AISHELL-1 and LibriSpeech datasets reveal that HydraFormer effectively adapts to various subsampling rates and languages while maintaining high recognition performance. Additionally, HydraFormer showcases exceptional stability, sustaining consistent performance under various initialization conditions, and exhibits robust transferability by learning from pretrained single subsampling rate automatic speech recognition models\footnote{Model code and scripts: https://github.com/HydraFormer/hydraformer}.

</details>

### [wav2graph: A Framework for Supervised Learning Knowledge Graph from Speech](2408.04174.md)
**Khai Le-Duc, Quy-Anh Dang, Tan-Hanh Pham, Truong-Son Hy** · 2024-08-08

<details>
<summary>Abstract</summary>

Knowledge graphs (KGs) enhance the performance of large language models (LLMs) and search engines by providing structured, interconnected data that improves reasoning and context-awareness. However, KGs only focus on text data, thereby neglecting other modalities such as speech. In this work, we introduce wav2graph, the first framework for supervised learning knowledge graph from speech data. Our pipeline are straightforward: (1) constructing a KG based on transcribed spoken utterances and a named entity database, (2) converting KG into embedding vectors, and (3) training graph neural networks (GNNs) for node classification and link prediction tasks. Through extensive experiments conducted in inductive and transductive learning contexts using state-of-the-art GNN models, we provide baseline results and error analysis for node classification and link prediction tasks on human transcripts and automatic speech recognition (ASR) transcripts, including evaluations using both encoder-based and decoder-based node embeddings, as well as monolingual and multilingual acoustic pre-trained models. All related code, data, and models are published online.

</details>

### [MathBridge: A Large Corpus Dataset for Translating Spoken Mathematical Expressions into $LaTeX$ Formulas for Improved Readability](2408.07081.md)
**Kyudan Jung, Sieun Hyeon, Jeong Youn Kwon, Nam-Joon Kim et al.** · 2024-08-07

<details>
<summary>Abstract</summary>

Improving the readability of mathematical expressions in text-based document such as subtitle of mathematical video, is an significant task. To achieve this, mathematical expressions should be convert to compiled formulas. For instance, the spoken expression ``x equals minus b plus or minus the square root of b squared minus four a c, all over two a'' from automatic speech recognition is more readily comprehensible when displayed as a compiled formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. To convert mathematical spoken sentences to compiled formulas, two processes are required: spoken sentences are converted into LaTeX formulas, and LaTeX formulas are converted into compiled formulas. The latter can be managed by using LaTeX engines. However, there is no way to do the former effectively. Even if we try to solve this using language models, there is no paired data between spoken sentences and LaTeX formulas to train it. In this paper, we introduce MathBridge, the first extensive dataset for translating mathematical spoken sentences into LaTeX formulas. MathBridge comprises approximately 23 million LaTeX formulas paired with the corresponding mathematical spoken sentences. Through comprehensive evaluations, including fine-tuning with proposed data, we discovered that MathBridge significantly enhances the capabilities of pretrained language models for converting to LaTeX formulas from mathematical spoken sentences. Specifically, for the T5-large model, the sacreBLEU score increased from 4.77 to 46.8, demonstrating substantial enhancement.

</details>

### [Speaker Adaptation for Quantised End-to-End ASR Models](2408.03979.md)
**Qiuming Zhao, Guangzhi Sun, Chao Zhang, Mingxing Xu et al.** · 2024-08-07

<details>
<summary>Abstract</summary>

End-to-end models have shown superior performance for automatic speech recognition (ASR). However, such models are often very large in size and thus challenging to deploy on resource-constrained edge devices. While quantisation can reduce model sizes, it can lead to increased word error rates (WERs). Although improved quantisation methods were proposed to address the issue of performance degradation, the fact that quantised models deployed on edge devices often target only on a small group of users is under-explored. To this end, we propose personalisation for quantised models (P4Q), a novel strategy that uses speaker adaptation (SA) to improve quantised end-to-end ASR models by fitting them to the characteristics of the target speakers. In this paper, we study the P4Q strategy based on Whisper and Conformer attention-based encoder-decoder (AED) end-to-end ASR models, which leverages a 4-bit block-wise NormalFloat4 (NF4) approach for quantisation and the low-rank adaptation (LoRA) approach for SA. Experimental results on the LibriSpeech and the TED-LIUM 3 corpora show that, with a 7-time reduction in model size and 1% extra speaker-specific parameters, 15.1% and 23.3% relative WER reductions were achieved on quantised Whisper and Conformer AED models respectively, comparing to the full precision models.

</details>

### [Speech-MASSIVE: A Multilingual Speech Dataset for SLU and Beyond](2408.03900.md)
**Beomseok Lee, Ioan Calapodescu, Marco Gaido, Matteo Negri et al.** · 2024-08-07

<details>
<summary>Abstract</summary>

We present Speech-MASSIVE, a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart for a portion of the MASSIVE textual corpus. Speech-MASSIVE covers 12 languages from different families and inherits from MASSIVE the annotations for the intent prediction and slot-filling tasks. Our extension is prompted by the scarcity of massively multilingual SLU datasets and the growing need for versatile speech datasets to assess foundation models (LLMs, speech encoders) across languages and tasks. We provide a multimodal, multitask, multilingual dataset and report SLU baselines using both cascaded and end-to-end architectures in various training scenarios (zero-shot, few-shot, and full fine-tune). Furthermore, we demonstrate the suitability of Speech-MASSIVE for benchmarking other tasks such as speech transcription, language identification, and speech translation. The dataset, models, and code are publicly available at: https://github.com/hlt-mt/Speech-MASSIVE

</details>

### [Self-Supervised Learning for Multi-Channel Neural Transducer](2408.02945.md)
**Atsushi Kojima** · 2024-08-06

<details>
<summary>Abstract</summary>

Self-supervised learning, such as with the wav2vec 2.0 framework significantly improves the accuracy of end-to-end automatic speech recognition (ASR). Wav2vec 2.0 has been applied to single-channel end-to-end ASR models. In this work, we explored a self-supervised learning method for a multi-channel end-to-end ASR model based on the wav2vec 2.0 framework. As the multi-channel end-to-end ASR model, we focused on a multi-channel neural transducer. In pre-training, we compared three different methods for feature quantization to train a multi-channel conformer audio encoder: joint quantization, feature-wise quantization and channel-wise quantization. In fine-tuning, we trained the multi-channel conformer-transducer. All experiments were conducted using the far-field in-house and CHiME-4 datasets. The results of the experiments showed that feature-wise quantization was the most effective among the methods. We observed a 66% relative reduction in character error rate compared with the model without any pre-training for the far-field in-house dataset.

</details>

### [OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents](2408.03047.md)
**Qiang Sun, Yuanyi Luo, Sirui Li, Wenxiao Zhang et al.** · 2024-08-06

<details>
<summary>Abstract</summary>

Multimodal conversational agents are highly desirable because they offer natural and human-like interaction. However, there is a lack of comprehensive end-to-end solutions to support collaborative development and benchmarking. While proprietary systems like GPT-4o and Gemini demonstrating impressive integration of audio, video, and text with response times of 200-250ms, challenges remain in balancing latency, accuracy, cost, and data privacy. To better understand and quantify these issues, we developed OpenOmni, an open-source, end-to-end pipeline benchmarking tool that integrates advanced technologies such as Speech-to-Text, Emotion Detection, Retrieval Augmented Generation, Large Language Models, along with the ability to integrate customized models. OpenOmni supports local and cloud deployment, ensuring data privacy and supporting latency and accuracy benchmarking. This flexible framework allows researchers to customize the pipeline, focusing on real bottlenecks and facilitating rapid proof-of-concept development. OpenOmni can significantly enhance applications like indoor assistance for visually impaired individuals, advancing human-computer interaction. Our demonstration video is available https://www.youtube.com/watch?v=zaSiT3clWqY, demo is available via https://openomni.ai4wa.com, code is available via https://github.com/AI4WA/OpenOmniFramework.

</details>

### [Clustering and Mining Accented Speech for Inclusive and Fair Speech Recognition](2408.02582.md)
**Jaeyoung Kim, Han Lu, Soheil Khorram, Anshuman Tripathi et al.** · 2024-08-05

<details>
<summary>Abstract</summary>

Modern automatic speech recognition (ASR) systems are typically trained on more than tens of thousands hours of speech data, which is one of the main factors for their great success. However, the distribution of such data is typically biased towards common accents or typical speech patterns. As a result, those systems often poorly perform on atypical accented speech. In this paper, we present accent clustering and mining schemes for fair speech recognition systems which can perform equally well on under-represented accented speech. For accent recognition, we applied three schemes to overcome limited size of supervised accent data: supervised or unsupervised pre-training, distributionally robust optimization (DRO) and unsupervised clustering. Three schemes can significantly improve the accent recognition model especially for unbalanced and small accented speech. Fine-tuning ASR on the mined Indian accent speech using the proposed supervised or unsupervised clustering schemes showed 10.0% and 5.3% relative improvements compared to fine-tuning on the randomly sampled speech, respectively.

</details>

### [The NPU-ASLP System Description for Visual Speech Recognition in CNVSRC 2024](2408.02369.md)
**He Wang, Lei Xie** · 2024-08-05

<details>
<summary>Abstract</summary>

This paper delineates the visual speech recognition (VSR) system introduced by the NPU-ASLP (Team 237) in the second Chinese Continuous Visual Speech Recognition Challenge (CNVSRC 2024), engaging in all four tracks, including the fixed and open tracks of Single-Speaker VSR Task and Multi-Speaker VSR Task. In terms of data processing, we leverage the lip motion extractor from the baseline1 to produce multiscale video data. Besides, various augmentation techniques are applied during training, encompassing speed perturbation, random rotation, horizontal flipping, and color transformation. The VSR model adopts an end-to-end architecture with joint CTC/attention loss, introducing Enhanced ResNet3D visual frontend, E-Branchformer encoder, and Bi-directional Transformer decoder. Our approach yields a 30.47% CER for the Single-Speaker Task and 34.30% CER for the Multi-Speaker Task, securing second place in the open track of the Single-Speaker Task and first place in the other three tracks.

</details>

### [ALIF: Low-Cost Adversarial Audio Attacks on Black-Box Speech Platforms using Linguistic Features](2408.01808.md)
**Peng Cheng, Yuwei Wang, Peng Huang, Zhongjie Ba et al.** · 2024-08-03

<details>
<summary>Abstract</summary>

Extensive research has revealed that adversarial examples (AE) pose a significant threat to voice-controllable smart devices. Recent studies have proposed black-box adversarial attacks that require only the final transcription from an automatic speech recognition (ASR) system. However, these attacks typically involve many queries to the ASR, resulting in substantial costs. Moreover, AE-based adversarial audio samples are susceptible to ASR updates. In this paper, we identify the root cause of these limitations, namely the inability to construct AE attack samples directly around the decision boundary of deep learning (DL) models. Building on this observation, we propose ALIF, the first black-box adversarial linguistic feature-based attack pipeline. We leverage the reciprocal process of text-to-speech (TTS) and ASR models to generate perturbations in the linguistic embedding space where the decision boundary resides. Based on the ALIF pipeline, we present the ALIF-OTL and ALIF-OTA schemes for launching attacks in both the digital domain and the physical playback environment on four commercial ASRs and voice assistants. Extensive evaluations demonstrate that ALIF-OTL and -OTA significantly improve query efficiency by 97.7% and 73.3%, respectively, while achieving competitive performance compared to existing methods. Notably, ALIF-OTL can generate an attack sample with only one query. Furthermore, our test-of-time experiment validates the robustness of our approach against ASR updates.

</details>

### [SynesLM: A Unified Approach for Audio-visual Speech Recognition and Translation via Language Model and Synthetic Data](2408.00624.md)
**Yichen Lu, Jiaqi Song, Xuankai Chang, Hengwei Bian et al.** · 2024-08-01

<details>
<summary>Abstract</summary>

In this work, we present SynesLM, an unified model which can perform three multimodal language understanding tasks: audio-visual automatic speech recognition(AV-ASR) and visual-aided speech/machine translation(VST/VMT). Unlike previous research that focused on lip motion as visual cues for speech signals, our work explores more general visual information within entire frames, such as objects and actions. Additionally, we use synthetic image data to enhance the correlation between image and speech data. We benchmark SynesLM against the How2 dataset, demonstrating performance on par with state-of-the-art (SOTA) models dedicated to AV-ASR while maintaining our multitasking framework. Remarkably, for zero-shot AV-ASR, SynesLM achieved SOTA performance by lowering the Word Error Rate (WER) from 43.4% to 39.4% on the VisSpeech Dataset. Furthermore, our results in VST and VMT outperform the previous results, improving the BLEU score to 43.5 from 37.2 for VST, and to 54.8 from 54.4 for VMT.

</details>

### [Sentence-wise Speech Summarization: Task, Datasets, and End-to-End Modeling with LM Knowledge Distillation](2408.00205.md)
**Kohei Matsuura, Takanori Ashihara, Takafumi Moriya, Masato Mimura et al.** · 2024-08-01

<details>
<summary>Abstract</summary>

This paper introduces a novel approach called sentence-wise speech summarization (Sen-SSum), which generates text summaries from a spoken document in a sentence-by-sentence manner. Sen-SSum combines the real-time processing of automatic speech recognition (ASR) with the conciseness of speech summarization. To explore this approach, we present two datasets for Sen-SSum: Mega-SSum and CSJ-SSum. Using these datasets, our study evaluates two types of Transformer-based models: 1) cascade models that combine ASR and strong text summarization models, and 2) end-to-end (E2E) models that directly convert speech into a text summary. While E2E models are appealing to develop compute-efficient models, they perform worse than cascade models. Therefore, we propose knowledge distillation for E2E models using pseudo-summaries generated by the cascade models. Our experiments show that this proposed knowledge distillation effectively improves the performance of the E2E model on both datasets.

</details>

### [The Llama 3 Herd of Models](2407.21783.md)
**Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey et al.** · 2024-07-31

<details>
<summary>Abstract</summary>

Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development.

</details>

### [On the Problem of Text-To-Speech Model Selection for Synthetic Data Generation in Automatic Speech Recognition](2407.21476.md)
**Nick Rossenbach, Ralf Schlüter, Sakriani Sakti** · 2024-07-31

<details>
<summary>Abstract</summary>

The rapid development of neural text-to-speech (TTS) systems enabled its usage in other areas of natural language processing such as automatic speech recognition (ASR) or spoken language translation (SLT). Due to the large number of different TTS architectures and their extensions, selecting which TTS systems to use for synthetic data creation is not an easy task. We use the comparison of five different TTS decoder architectures in the scope of synthetic data generation to show the impact on CTC-based speech recognition training. We compare the recognition results to computable metrics like NISQA MOS and intelligibility, finding that there are no clear relations to the ASR performance. We also observe that for data generation auto-regressive decoding performs better than non-autoregressive decoding, and propose an approach to quantify TTS generalization capabilities.

</details>

### [Leveraging Self-Supervised Models for Automatic Whispered Speech Recognition](2407.21211.md)
**Aref Farhadipour, Homa Asadi, Volker Dellwo** · 2024-07-30

<details>
<summary>Abstract</summary>

In automatic speech recognition, any factor that alters the acoustic properties of speech can pose a challenge to the system's performance. This paper presents a novel approach for automatic whispered speech recognition in the Irish dialect using the self-supervised WavLM model. Conventional automatic speech recognition systems often fail to accurately recognise whispered speech due to its distinct acoustic properties and the scarcity of relevant training data. To address this challenge, we utilized a pre-trained WavLM model, fine-tuned with a combination of whispered and normal speech data from the wTIMIT and CHAINS datasets, which include the English language in Singaporean and Irish dialects, respectively. Our baseline evaluation with the OpenAI Whisper model highlighted its limitations, achieving a Word Error Rate (WER) of 18.8% and a Character Error Rate (CER) of 4.24% on whispered speech. In contrast, the proposed WavLM-based system significantly improved performance, achieving a WER of 9.22% and a CER of 2.59%. These results demonstrate the efficacy of our approach in recognising whispered speech and underscore the importance of tailored acoustic modeling for robust automatic speech recognition systems. This study provides valuable insights into developing effective automatic speech recognition solutions for challenging speech affected by whisper and dialect. The source codes for this paper are freely available.

</details>

### [Improving noisy student training for low-resource languages in End-to-End ASR using CycleGAN and inter-domain losses](2407.21061.md)
**Chia-Yu Li, Ngoc Thang Vu** · 2024-07-26

<details>
<summary>Abstract</summary>

Training a semi-supervised end-to-end speech recognition system using noisy student training has significantly improved performance. However, this approach requires a substantial amount of paired speech-text and unlabeled speech, which is costly for low-resource languages. Therefore, this paper considers a more extreme case of semi-supervised end-to-end automatic speech recognition where there are limited paired speech-text, unlabeled speech (less than five hours), and abundant external text. Firstly, we observe improved performance by training the model using our previous work on semi-supervised learning "CycleGAN and inter-domain losses" solely with external text. Secondly, we enhance "CycleGAN and inter-domain losses" by incorporating automatic hyperparameter tuning, calling it "enhanced CycleGAN inter-domain losses." Thirdly, we integrate it into the noisy student training approach pipeline for low-resource scenarios. Our experimental results, conducted on six non-English languages from Voxforge and Common Voice, show a 20% word error rate reduction compared to the baseline teacher model and a 10% word error rate reduction compared to the baseline best student model, highlighting the significant improvements achieved through our proposed method.

</details>

### [Speech Bandwidth Expansion Via High Fidelity Generative Adversarial Networks](2407.18571.md)
**Mahmoud Salhab, Haidar Harmanani** · 2024-07-26

<details>
<summary>Abstract</summary>

Speech bandwidth expansion is crucial for expanding the frequency range of low-bandwidth speech signals, thereby improving audio quality, clarity and perceptibility in digital applications. Its applications span telephony, compression, text-to-speech synthesis, and speech recognition. This paper presents a novel approach using a high-fidelity generative adversarial network, unlike cascaded systems, our system is trained end-to-end on paired narrowband and wideband speech signals. Our method integrates various bandwidth upsampling ratios into a single unified model specifically designed for speech bandwidth expansion applications. Our approach exhibits robust performance across various bandwidth expansion factors, including those not encountered during training, demonstrating zero-shot capability. To the best of our knowledge, this is the first work to showcase this capability. The experimental results demonstrate that our method outperforms previous end-to-end approaches, as well as interpolation and traditional techniques, showcasing its effectiveness in practical speech enhancement applications.

</details>

### [Enhancing Dysarthric Speech Recognition for Unseen Speakers via Prototype-Based Adaptation](2407.18461.md)
**Shiyao Wang, Shiwan Zhao, Jiaming Zhou, Aobo Kong et al.** · 2024-07-26

<details>
<summary>Abstract</summary>

Dysarthric speech recognition (DSR) presents a formidable challenge due to inherent inter-speaker variability, leading to severe performance degradation when applying DSR models to new dysarthric speakers. Traditional speaker adaptation methodologies typically involve fine-tuning models for each speaker, but this strategy is cost-prohibitive and inconvenient for disabled users, requiring substantial data collection. To address this issue, we introduce a prototype-based approach that markedly improves DSR performance for unseen dysarthric speakers without additional fine-tuning. Our method employs a feature extractor trained with HuBERT to produce per-word prototypes that encapsulate the characteristics of previously unseen speakers. These prototypes serve as the basis for classification. Additionally, we incorporate supervised contrastive learning to refine feature extraction. By enhancing representation quality, we further improve DSR performance, enabling effective personalized DSR. We release our code at https://github.com/NKU-HLT/PB-DSR.

</details>

### [Towards Improving NAM-to-Speech Synthesis Intelligibility using Self-Supervised Speech Models](2407.18541.md)
**Neil Shah, Shirish Karande, Vineet Gandhi** · 2024-07-26

<details>
<summary>Abstract</summary>

We propose a novel approach to significantly improve the intelligibility in the Non-Audible Murmur (NAM)-to-speech conversion task, leveraging self-supervision and sequence-to-sequence (Seq2Seq) learning techniques. Unlike conventional methods that explicitly record ground-truth speech, our methodology relies on self-supervision and speech-to-speech synthesis to simulate ground-truth speech. Despite utilizing simulated speech, our method surpasses the current state-of-the-art (SOTA) by 29.08% improvement in the Mel-Cepstral Distortion (MCD) metric. Additionally, we present error rates and demonstrate our model's proficiency to synthesize speech in novel voices of interest. Moreover, we present a methodology for augmenting the existing CSTR NAM TIMIT Plus corpus, setting a benchmark with a Word Error Rate (WER) of 42.57% to gauge the intelligibility of the synthesized speech. Speech samples can be found at https://nam2speech.github.io/NAM2Speech/

</details>

### [On the Effect of Purely Synthetic Training Data for Different Automatic Speech Recognition Architectures](2407.17997.md)
**Benedikt Hilmes, Nick Rossenbach, and Ralf Schlüter** · 2024-07-25

<details>
<summary>Abstract</summary>

In this work we evaluate the utility of synthetic data for training automatic speech recognition (ASR). We use the ASR training data to train a text-to-speech (TTS) system similar to FastSpeech-2. With this TTS we reproduce the original training data, training ASR systems solely on synthetic data. For ASR, we use three different architectures, attention-based encoder-decoder, hybrid deep neural network hidden Markov model and a Gaussian mixture hidden Markov model, showing the different sensitivity of the models to synthetic data generation. In order to extend previous work, we present a number of ablation studies on the effectiveness of synthetic vs. real training data for ASR. In particular we focus on how the gap between training on synthetic and real data changes by varying the speaker embedding or by scaling the model size. For the latter we show that the TTS models generalize well, even when training scores indicate overfitting.

</details>

### [Improving Domain-Specific ASR with LLM-Generated Contextual Descriptions](2407.17874.md)
**Jiwon Suh, Injae Na, Woohwan Jung** · 2024-07-25

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (E2E ASR) systems have significantly improved speech recognition through training on extensive datasets. Despite these advancements, they still struggle to accurately recognize domain specific words, such as proper nouns and technical terminologies. To address this problem, we propose a method to utilize the state-of-the-art Whisper without modifying its architecture, preserving its generalization performance while enabling it to leverage descriptions effectively. Moreover, we propose two additional training techniques to improve the domain specific ASR: decoder fine-tuning, and context perturbation. We also propose a method to use a Large Language Model (LLM) to generate descriptions with simple metadata, when descriptions are unavailable. Our experiments demonstrate that proposed methods notably enhance domain-specific ASR accuracy on real-life datasets, with LLM-generated descriptions outperforming human-crafted ones in effectiveness.

</details>

### [Scaling A Simple Approach to Zero-Shot Speech Recognition](2407.17852.md)
**Jinming Zhao, Vineel Pratap, Michael Auli** · 2024-07-25

<details>
<summary>Abstract</summary>

Despite rapid progress in increasing the language coverage of automatic speech recognition, the field is still far from covering all languages with a known writing script. Recent work showed promising results with a zero-shot approach requiring only a small amount of text data, however, accuracy heavily depends on the quality of the used phonemizer which is often weak for unseen languages. In this paper, we present MMS Zero-shot a conceptually simpler approach based on romanization and an acoustic model trained on data in 1,078 different languages or three orders of magnitude more than prior art. MMS Zero-shot reduces the average character error rate by a relative 46% over 100 unseen languages compared to the best previous work. Moreover, the error rate of our approach is only 2.5x higher compared to in-domain supervised baselines, while our approach uses no labeled data for the evaluation languages at all.

</details>

### [Sentiment Reasoning for Healthcare](2407.21054.md)
**Khai-Nguyen Nguyen, Khai Le-Duc, Bach Phan Tat, Duy Le et al.** · 2024-07-24

<details>
<summary>Abstract</summary>

Transparency in AI healthcare decision-making is crucial. By incorporating rationales to explain reason for each predicted label, users could understand Large Language Models (LLMs)'s reasoning to make better decision. In this work, we introduce a new task - Sentiment Reasoning - for both speech and text modalities, and our proposed multimodal multitask framework and the world's largest multimodal sentiment analysis dataset. Sentiment Reasoning is an auxiliary task in sentiment analysis where the model predicts both the sentiment label and generates the rationale behind it based on the input transcript. Our study conducted on both human transcripts and Automatic Speech Recognition (ASR) transcripts shows that Sentiment Reasoning helps improve model transparency by providing rationale for model prediction with quality semantically comparable to humans while also improving model's classification performance (+2% increase in both accuracy and macro-F1) via rationale-augmented fine-tuning. Also, no significant difference in the semantic quality of generated rationales between human and ASR transcripts. All code, data (five languages - Vietnamese, English, Chinese, German, and French) and models are published online: https://github.com/leduckhai/Sentiment-Reasoning

</details>

### [Quantifying the Role of Textual Predictability in Automatic Speech Recognition](2407.16537.md)
**Sean Robertson, Gerald Penn, Ewan Dunbar** · 2024-07-23

<details>
<summary>Abstract</summary>

A long-standing question in automatic speech recognition research is how to attribute errors to the ability of a model to model the acoustics, versus its ability to leverage higher-order context (lexicon, morphology, syntax, semantics). We validate a novel approach which models error rates as a function of relative textual predictability, and yields a single number, $k$, which measures the effect of textual predictability on the recognizer. We use this method to demonstrate that a Wav2Vec 2.0-based model makes greater stronger use of textual context than a hybrid ASR model, in spite of not using an explicit language model, and also use it to shed light on recent results demonstrating poor performance of standard ASR systems on African-American English. We demonstrate that these mostly represent failures of acoustic--phonetic modelling. We show how this approach can be used straightforwardly in diagnosing and improving ASR.

</details>

### [Evolutionary Prompt Design for LLM-Based Post-ASR Error Correction](2407.16370.md)
**Rithik Sachdev, Zhong-Qiu Wang, Chao-Han Huck Yang** · 2024-07-23

<details>
<summary>Abstract</summary>

Building upon the strength of modern large language models (LLMs), generative error correction (GEC) has emerged as a promising paradigm that can elevate the performance of modern automatic speech recognition (ASR) systems. One representative approach is to leverage in-context learning to prompt LLMs so that a better hypothesis can be generated by the LLMs based on a carefully-designed prompt and an $N$-best list of hypotheses produced by ASR systems. However, it is yet unknown whether the existing prompts are the most effective ones for the task of post-ASR error correction. In this context, this paper first explores alternative prompts to identify an initial set of effective prompts, and then proposes to employ an evolutionary prompt optimization algorithm to refine the initial prompts. Evaluations results on the CHiME-4 subset of the Task $1$ of the SLT $2024$ GenSEC challenge show the effectiveness and potential of the proposed algorithms.

</details>

### [Towards scalable efficient on-device ASR with transfer learning](2407.16664.md)
**Laxmi Pandey, Ke Li, Jinxi Guo, Debjyoti Paul et al.** · 2024-07-23

<details>
<summary>Abstract</summary>

Multilingual pretraining for transfer learning significantly boosts the robustness of low-resource monolingual ASR models. This study systematically investigates three main aspects: (a) the impact of transfer learning on model performance during initial training or fine-tuning, (b) the influence of transfer learning across dataset domains and languages, and (c) the effect on rare-word recognition compared to non-rare words. Our finding suggests that RNNT-loss pretraining, followed by monolingual fine-tuning with Minimum Word Error Rate (MinWER) loss, consistently reduces Word Error Rates (WER) across languages like Italian and French. WER Reductions (WERR) reach 36.2% and 42.8% compared to monolingual baselines for MLS and in-house datasets. Out-of-domain pretraining leads to 28% higher WERR than in-domain pretraining. Both rare and non-rare words benefit, with rare words showing greater improvements with out-of-domain pretraining, and non-rare words with in-domain pretraining.

</details>

### [Robustness of Speech Separation Models for Similar-pitch Speakers](2407.15749.md)
**Bunlong Lay, Sebastian Zaczek, Kristina Tesch, Timo Gerkmann** · 2024-07-22

<details>
<summary>Abstract</summary>

Single-channel speech separation is a crucial task for enhancing speech recognition systems in multi-speaker environments. This paper investigates the robustness of state-of-the-art Neural Network models in scenarios where the pitch differences between speakers are minimal. Building on earlier findings by Ditter and Gerkmann, which identified a significant performance drop for the 2018 Chimera++ under similar-pitch conditions, our study extends the analysis to more recent and sophisticated Neural Network models. Our experiments reveal that modern models have substantially reduced the performance gap for matched training and testing conditions. However, a substantial performance gap persists under mismatched conditions, with models performing well for large pitch differences but showing worse performance if the speakers' pitches are similar. These findings motivate further research into the generalizability of speech separation models to similar-pitch speakers and unseen data.

</details>

### [LLaST: Improved End-to-end Speech Translation System Leveraged by Large Language Models](2407.15415.md)
**Xi Chen, Songyang Zhang, Qibing Bai, Kai Chen et al.** · 2024-07-22

<details>
<summary>Abstract</summary>

We introduces LLaST, a framework for building high-performance Large Language model based Speech-to-text Translation systems. We address the limitations of end-to-end speech translation(E2E ST) models by exploring model architecture design and optimization techniques tailored for LLMs. Our approach includes LLM-based speech translation architecture design, ASR-augmented training, multilingual data augmentation, and dual-LoRA optimization. Our approach demonstrates superior performance on the CoVoST-2 benchmark and showcases exceptional scaling capabilities powered by LLMs. We believe this effective method will serve as a strong baseline for speech translation and provide insights for future improvements of the LLM-based speech translation framework. We release the data, code and models in https://github.com/openaudiolab/LLaST.

</details>

### [Schrödinger Bridge for Generative Speech Enhancement](2407.16074.md)
**Ante Jukić, Roman Korostik, Jagadeesh Balam, Boris Ginsburg** · 2024-07-22

<details>
<summary>Abstract</summary>

This paper proposes a generative speech enhancement model based on Schrödinger bridge (SB). The proposed model is employing a tractable SB to formulate a data-to-data process between the clean speech distribution and the observed noisy speech distribution. The model is trained with a data prediction loss, aiming to recover the complex-valued clean speech coefficients, and an auxiliary time-domain loss is used to improve training of the model. The effectiveness of the proposed SB-based model is evaluated in two different speech enhancement tasks: speech denoising and speech dereverberation. The experimental results demonstrate that the proposed SB-based outperforms diffusion-based models in terms of speech quality metrics and ASR performance, e.g., resulting in relative word error rate reduction of 20% for denoising and 6% for dereverberation compared to the best baseline model. The proposed model also demonstrates improved efficiency, achieving better quality than the baselines for the same number of sampling steps and with a reduced computational cost.

</details>

### [Trading Devil Final: Backdoor attack via Stock market and Bayesian Optimization](2407.14573.md)
**Orson Mengara** · 2024-07-21

<details>
<summary>Abstract</summary>

Since the advent of generative artificial intelligence, every company and researcher has been rushing to develop their own generative models, whether commercial or not. Given the large number of users of these powerful new tools, there is currently no intrinsically verifiable way to explain from the ground up what happens when LLMs (large language models) learn. For example, those based on automatic speech recognition systems, which have to rely on huge and astronomical amounts of data collected from all over the web to produce fast and efficient results, In this article, we develop a backdoor attack called MarketBackFinal 2.0, based on acoustic data poisoning, MarketBackFinal 2.0 is mainly based on modern stock market models. In order to show the possible vulnerabilities of speech-based transformers that may rely on LLMs.

</details>

### [GE2E-AC: Generalized End-to-End Loss Training for Accent Classification](2407.14021.md)
**Chihiro Watanabe, Hirokazu Kameoka** · 2024-07-19

<details>
<summary>Abstract</summary>

Accent classification or AC is a task to predict the accent type of an input utterance, and it can be used as a preliminary step toward accented speech recognition and accent conversion. Existing studies have often achieved such classification by training a neural network model to minimize the classification error of the predicted accent label, which can be obtained as a model output. Since we optimize the entire model only from the perspective of classification loss during training time in this approach, the model might learn to predict the accent type from irrelevant features, such as individual speaker identity, which are not informative during test time. To address this problem, we propose a GE2E-AC, in which we train a model to extract accent embedding or AE of an input utterance such that the AEs of the same accent class get closer, instead of directly minimizing the classification loss. We experimentally show the effectiveness of the proposed GE2E-AC, compared to the baseline model trained with the conventional cross-entropy-based loss.

</details>

### [Reexamining Racial Disparities in Automatic Speech Recognition Performance: The Role of Confounding by Provenance](2407.13982.md)
**Changye Li, Trevor Cohen, Serguei Pakhomov** · 2024-07-19

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) models trained on large amounts of audio data are now widely used to convert speech to written text in a variety of applications from video captioning to automated assistants used in healthcare and other domains. As such, it is important that ASR models and their use is fair and equitable. Prior work examining the performance of commercial ASR systems on the Corpus of Regional African American Language (CORAAL) demonstrated significantly worse ASR performance on African American English (AAE). The current study seeks to understand the factors underlying this disparity by examining the performance of the current state-of-the-art neural network based ASR system (Whisper, OpenAI) on the CORAAL dataset. Two key findings have been identified as a result of the current study. The first confirms prior findings of significant dialectal variation even across neighboring communities, and worse ASR performance on AAE that can be improved to some extent with fine-tuning of ASR models. The second is a novel finding not discussed in prior work on CORAAL: differences in audio recording practices within the dataset have a significant impact on ASR accuracy resulting in a ``confounding by provenance'' effect in which both language use and recording quality differ by study location. These findings highlight the need for further systematic investigation to disentangle the effects of recording quality and inherent linguistic diversity when examining the fairness and bias present in neural ASR models, as any bias in ASR accuracy may have negative downstream effects on disparities in various domains of life in which ASR technology is used.

</details>

### [Handling Numeric Expressions in Automatic Speech Recognition](2408.00004.md)
**Christian Huber, Alexander Waibel** · 2024-07-18

<details>
<summary>Abstract</summary>

This paper addresses the problem of correctly formatting numeric expressions in automatic speech recognition (ASR) transcripts. This is challenging since the expected transcript format depends on the context, e.g., 1945 (year) vs. 19:45 (timestamp). We compare cascaded and end-to-end approaches to recognize and format numeric expressions such as years, timestamps, currency amounts, and quantities. For the end-to-end approach, we employed a data generation strategy using a large language model (LLM) together with a text to speech (TTS) model to generate adaptation data. The results on our test data set show that while approaches based on LLMs perform well in recognizing formatted numeric expressions, adapted end-to-end models offer competitive performance with the advantage of lower latency and inference cost.

</details>

### [Low-Resourced Speech Recognition for Iu Mien Language via Weakly-Supervised Phoneme-based Multilingual Pre-training](2407.13292.md)
**Lukuan Dong, Donghong Qin, Fengbo Bai, Fanhua Song et al.** · 2024-07-18

<details>
<summary>Abstract</summary>

The mainstream automatic speech recognition (ASR) technology usually requires hundreds to thousands of hours of annotated speech data. Three approaches to low-resourced ASR are phoneme or subword based supervised pre-training, and self-supervised pre-training over multilingual data. The Iu Mien language is the main ethnic language of the Yao ethnic group in China and is low-resourced in the sense that the annotated speech is very limited. With less than 10 hours of transcribed Iu Mien language, this paper investigates and compares the three approaches for Iu Mien speech recognition. Our experiments are based on the recently released, three backbone models pretrained over the 10 languages from the CommonVoice dataset (CV-Lang10), which correspond to the three approaches for low-resourced ASR. It is found that phoneme supervision can achieve better results compared to subword supervision and self-supervision, thereby providing higher data-efficiency. Particularly, the Whistle models, i.e., obtained by the weakly-supervised phoneme-based multilingual pre-training, obtain the most competitive results.

</details>

### [A light-weight and efficient punctuation and word casing prediction model for on-device streaming ASR](2407.13142.md)
**Jian You, Xiangfeng Li** · 2024-07-18

<details>
<summary>Abstract</summary>

Punctuation and word casing prediction are necessary for automatic speech recognition (ASR). With the popularity of on-device end-to-end streaming ASR systems, the on-device punctuation and word casing prediction become a necessity while we found little discussion on this. With the emergence of Transformer, Transformer based models have been explored for this scenario. However, Transformer based models are too large for on-device ASR systems. In this paper, we propose a light-weight and efficient model that jointly predicts punctuation and word casing in real time. The model is based on Convolutional Neural Network (CNN) and Bidirectional Long Short-Term Memory (BiLSTM). Experimental results on the IWSLT2011 test set show that the proposed model obtains 9% relative improvement compared to the best of non-Transformer models on overall F1-score. Compared to the representative of Transformer based models, the proposed model achieves comparable results to the representative model while being only one-fortieth its size and 2.5 times faster in terms of inference time. It is suitable for on-device streaming ASR systems. Our code is publicly available.

</details>

### [Qalam : A Multimodal LLM for Arabic Optical Character and Handwriting Recognition](2407.13559.md)
**Gagan Bhatia, El Moatez Billah Nagoudi, Fakhraddin Alwajih, Muhammad Abdul-Mageed** · 2024-07-18

<details>
<summary>Abstract</summary>

Arabic Optical Character Recognition (OCR) and Handwriting Recognition (HWR) pose unique challenges due to the cursive and context-sensitive nature of the Arabic script. This study introduces Qalam, a novel foundation model designed for Arabic OCR and HWR, built on a SwinV2 encoder and RoBERTa decoder architecture. Our model significantly outperforms existing methods, achieving a Word Error Rate (WER) of just 0.80% in HWR tasks and 1.18% in OCR tasks. We train Qalam on a diverse dataset, including over 4.5 million images from Arabic manuscripts and a synthetic dataset comprising 60k image-text pairs. Notably, Qalam demonstrates exceptional handling of Arabic diacritics, a critical feature in Arabic scripts. Furthermore, it shows a remarkable ability to process high-resolution inputs, addressing a common limitation in current OCR systems. These advancements underscore Qalam's potential as a leading solution for Arabic script recognition, offering a significant leap in accuracy and efficiency.

</details>

### [Morphosyntactic Analysis for CHILDES](2407.12389.md)
**Houjun Liu, Brian MacWhinney** · 2024-07-17

<details>
<summary>Abstract</summary>

Language development researchers are interested in comparing the process of language learning across languages. Unfortunately, it has been difficult to construct a consistent quantitative framework for such comparisons. However, recent advances in AI (Artificial Intelligence) and ML (Machine Learning) are providing new methods for ASR (automatic speech recognition) and NLP (natural language processing) that can be brought to bear on this problem. Using the Batchalign2 program (Liu et al., 2023), we have been transcribing and linking data for the CHILDES database and have applied the UD (Universal Dependencies) framework to provide a consistent and comparable morphosyntactic analysis for 27 languages. These new resources open possibilities for deeper crosslinguistic study of language learning.

</details>

### [Adaptive Cascading Network for Continual Test-Time Adaptation](2407.12240.md)
**Kien X. Nguyen, Fengchun Qiao, Xi Peng** · 2024-07-17

<details>
<summary>Abstract</summary>

We study the problem of continual test-time adaption where the goal is to adapt a source pre-trained model to a sequence of unlabelled target domains at test time. Existing methods on test-time training suffer from several limitations: (1) Mismatch between the feature extractor and classifier; (2) Interference between the main and self-supervised tasks; (3) Lack of the ability to quickly adapt to the current distribution. In light of these challenges, we propose a cascading paradigm that simultaneously updates the feature extractor and classifier at test time, mitigating the mismatch between them and enabling long-term model adaptation. The pre-training of our model is structured within a meta-learning framework, thereby minimizing the interference between the main and self-supervised tasks and encouraging fast adaptation in the presence of limited unlabelled data. Additionally, we introduce innovative evaluation metrics, average accuracy and forward transfer, to effectively measure the model's adaptation capabilities in dynamic, real-world scenarios. Extensive experiments and ablation studies demonstrate the superiority of our approach in a range of tasks including image classification, text classification, and speech recognition.

</details>

### [Investigating the Effect of Label Topology and Training Criterion on ASR Performance and Alignment Quality](2407.11641.md)
**Tina Raissi, Christoph Lüscher, Simon Berger, Ralf Schlüter et al.** · 2024-07-16

<details>
<summary>Abstract</summary>

The ongoing research scenario for automatic speech recognition (ASR) envisions a clear division between end-to-end approaches and classic modular systems. Even though a high-level comparison between the two approaches in terms of their requirements and (dis)advantages is commonly addressed, a closer comparison under similar conditions is not readily available in the literature. In this work, we present a comparison focused on the label topology and training criterion. We compare two discriminative alignment models with hidden Markov model (HMM) and connectionist temporal classification topology, and two first-order label context ASR models utilizing factored HMM and strictly monotonic recurrent neural network transducer, respectively. We use different measurements for the evaluation of the alignment quality, and compare word error rate and real time factor of our best systems. Experiments are conducted on the LibriSpeech 960h and Switchboard 300h tasks.

</details>

### [Beyond Binary: Multiclass Paraphasia Detection with Generative Pretrained Transformers and End-to-End Models](2407.11345.md)
**Matthew Perez, Aneesha Sampath, Minxue Niu, Emily Mower Provost** · 2024-07-16

<details>
<summary>Abstract</summary>

Aphasia is a language disorder that can lead to speech errors known as paraphasias, which involve the misuse, substitution, or invention of words. Automatic paraphasia detection can help those with Aphasia by facilitating clinical assessment and treatment planning options. However, most automatic paraphasia detection works have focused solely on binary detection, which involves recognizing only the presence or absence of a paraphasia. Multiclass paraphasia detection represents an unexplored area of research that focuses on identifying multiple types of paraphasias and where they occur in a given speech segment. We present novel approaches that use a generative pretrained transformer (GPT) to identify paraphasias from transcripts as well as two end-to-end approaches that focus on modeling both automatic speech recognition (ASR) and paraphasia classification as multiple sequences vs. a single sequence. We demonstrate that a single sequence model outperforms GPT baselines for multiclass paraphasia detection.

</details>

### [Improving Neural Biasing for Contextual Speech Recognition by Early Context Injection and Text Perturbation](2407.10303.md)
**Ruizhe Huang, Mahsa Yarmohammadi, Sanjeev Khudanpur, Daniel Povey** · 2024-07-14

<details>
<summary>Abstract</summary>

Existing research suggests that automatic speech recognition (ASR) models can benefit from additional contexts (e.g., contact lists, user specified vocabulary). Rare words and named entities can be better recognized with contexts. In this work, we propose two simple yet effective techniques to improve context-aware ASR models. First, we inject contexts into the encoders at an early stage instead of merely at their last layers. Second, to enforce the model to leverage the contexts during training, we perturb the reference transcription with alternative spellings so that the model learns to rely on the contexts to make correct predictions. On LibriSpeech, our techniques together reduce the rare word error rate by 60% and 25% relatively compared to no biasing and shallow fusion, making the new state-of-the-art performance. On SPGISpeech and a real-world dataset ConEC, our techniques also yield good improvements over the baselines.

</details>

### [CUSIDE-T: Chunking, Simulating Future and Decoding for Transducer based Streaming ASR](2407.10255.md)
**Wenbo Zhao, Ziwei Li, Chuan Yu, Zhijian Ou** · 2024-07-14

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) is very important for many real-world ASR applications. However, a notable challenge for streaming ASR systems lies in balancing operational performance against latency constraint. Recently, a method of chunking, simulating future context and decoding, called CUSIDE, has been proposed for connectionist temporal classification (CTC) based streaming ASR, which obtains a good balance between reduced latency and high recognition accuracy. In this paper, we present CUSIDE-T, which successfully adapts the CUSIDE method over the recurrent neural network transducer (RNN-T) ASR architecture, instead of being based on the CTC architecture. We also incorporate language model rescoring in CUSIDE-T to further enhance accuracy, while only bringing a small additional latency. Extensive experiments are conducted over the AISHELL-1, WenetSpeech and SpeechIO datasets, comparing CUSIDE-T and U2++ (both based on RNN-T). U2++ is an existing counterpart of chunk based streaming ASR method. It is shown that CUSIDE-T achieves superior accuracy performance for streaming ASR, with equal settings of latency.

</details>

### [Empowering Whisper as a Joint Multi-Talker and Target-Talker Speech Recognition System](2407.09817.md)
**Lingwei Meng, Jiawen Kang, Yuejiao Wang, Zengrui Jin et al.** · 2024-07-13

<details>
<summary>Abstract</summary>

Multi-talker speech recognition and target-talker speech recognition, both involve transcription in multi-talker contexts, remain significant challenges. However, existing methods rarely attempt to simultaneously address both tasks. In this study, we propose a pioneering approach to empower Whisper, which is a speech foundation model, to tackle joint multi-talker and target-talker speech recognition tasks. Specifically, (i) we freeze Whisper and plug a Sidecar separator into its encoder to separate mixed embedding for multiple talkers; (ii) a Target Talker Identifier is introduced to identify the embedding flow of the target talker on the fly, requiring only three-second enrollment speech as a cue; (iii) soft prompt tuning for decoder is explored for better task adaptation. Our method outperforms previous methods on two- and three-talker LibriMix and LibriSpeechMix datasets for both tasks, and delivers acceptable zero-shot performance on multi-talker ASR on AishellMix Mandarin dataset.

</details>

### [CUSIDE-array: A Streaming Multi-Channel End-to-End Speech Recognition System with Realistic Evaluations](2407.09807.md)
**Xiangzhu Kong, Tianqi Ning, Hao Huang, Zhijian Ou** · 2024-07-13

<details>
<summary>Abstract</summary>

Recently multi-channel end-to-end (ME2E) ASR systems have emerged. While streaming single-channel end-to-end ASR has been extensively studied, streaming ME2E ASR is limited in exploration. Additionally, recent studies call attention to the gap between in-distribution (ID) and out-of-distribution (OOD) tests and doing realistic evaluations. This paper focuses on two research problems: realizing streaming ME2E ASR and improving OOD generalization. We propose the CUSIDE-array method, which integrates the recent CUSIDE methodology (Chunking, Simulating Future Context and Decoding) into the neural beamformer approach of ME2E ASR. It enables streaming processing of both front-end and back-end with a total latency of 402ms. The CUSIDE-array ME2E models are shown to achieve superior streaming results in both ID and OOD tests. Realistic evaluations confirm the advantage of CUSIDE-array in its capability to consume single-channel data to improve OOD generalization via back-end pre-training and ME2E fine-tuning.

</details>

### [Speech Slytherin: Examining the Performance and Efficiency of Mamba for Speech Separation, Recognition, and Synthesis](2407.09732.md)
**Xilin Jiang, Yinghao Aaron Li, Adrian Nicolas Florea, Cong Han et al.** · 2024-07-13

<details>
<summary>Abstract</summary>

It is too early to conclude that Mamba is a better alternative to transformers for speech before comparing Mamba with transformers in terms of both performance and efficiency in multiple speech-related tasks. To reach this conclusion, we propose and evaluate three models for three tasks: Mamba-TasNet for speech separation, ConMamba for speech recognition, and VALL-M for speech synthesis. We compare them with transformers of similar sizes in performance, memory, and speed. Our Mamba or Mamba-transformer hybrid models show comparable or higher performance than their transformer counterparts: Sepformer, Conformer, and VALL-E. They are more efficient than transformers in memory and speed for speech longer than a threshold duration, inversely related to the resolution of a speech token. Mamba for separation is the most efficient, and Mamba for recognition is the least. Further, we show that Mamba is not more efficient than transformer for speech shorter than the threshold duration and performs worse in models that require joint modeling of text and speech, such as cross or masked attention of two inputs. Therefore, we argue that the superiority of Mamba or transformer depends on particular problems and models. Code available at https://github.com/xi-j/Mamba-TasNet and https://github.com/xi-j/Mamba-ASR.

</details>

### [AI-Powered Immersive Assistance for Interactive Task Execution in Industrial Environments](2407.09147.md)
**Tomislav Duricic, Peter Müllner, Nicole Weidinger, Neven ElSayed et al.** · 2024-07-12

<details>
<summary>Abstract</summary>

Many industrial sectors rely on well-trained employees that are able to operate complex machinery. In this work, we demonstrate an AI-powered immersive assistance system that supports users in performing complex tasks in industrial environments. Specifically, our system leverages a VR environment that resembles a juice mixer setup. This digital twin of a physical setup simulates complex industrial machinery used to mix preparations or liquids (e.g., similar to the pharmaceutical industry) and includes various containers, sensors, pumps, and flow controllers. This setup demonstrates our system's capabilities in a controlled environment while acting as a proof-of-concept for broader industrial applications. The core components of our multimodal AI assistant are a large language model and a speech-to-text model that process a video and audio recording of an expert performing the task in a VR environment. The video and speech input extracted from the expert's video enables it to provide step-by-step guidance to support users in executing complex tasks. This demonstration showcases the potential of our AI-powered assistant to reduce cognitive load, increase productivity, and enhance safety in industrial environments.

</details>

### [Tamil Language Computing: the Present and the Future](2407.08618.md)
**Kengatharaiyer Sarveswaran** · 2024-07-11

<details>
<summary>Abstract</summary>

This paper delves into the text processing aspects of Language Computing, which enables computers to understand, interpret, and generate human language. Focusing on tasks such as speech recognition, machine translation, sentiment analysis, text summarization, and language modelling, language computing integrates disciplines including linguistics, computer science, and cognitive psychology to create meaningful human-computer interactions. Recent advancements in deep learning have made computers more accessible and capable of independent learning and adaptation. In examining the landscape of language computing, the paper emphasises foundational work like encoding, where Tamil transitioned from ASCII to Unicode, enhancing digital communication. It discusses the development of computational resources, including raw data, dictionaries, glossaries, annotated data, and computational grammars, necessary for effective language processing. The challenges of linguistic annotation, the creation of treebanks, and the training of large language models are also covered, emphasising the need for high-quality, annotated data and advanced language models. The paper underscores the importance of building practical applications for languages like Tamil to address everyday communication needs, highlighting gaps in current technology. It calls for increased research collaboration, digitization of historical texts, and fostering digital usage to ensure the comprehensive development of Tamil language processing, ultimately enhancing global communication and access to digital services.

</details>

### [Evaluating Voice Command Pipelines for Drone Control: From STT and LLM to Direct Classification and Siamese Networks](2407.08658.md)
**Lucca Emmanuel Pineli Simões, Lucas Brandão Rodrigues, Rafaela Mota Silva, Gustavo Rodrigues da Silva** · 2024-07-10

<details>
<summary>Abstract</summary>

This paper presents the development and comparative evaluation of three voice command pipelines for controlling a Tello drone, using speech recognition and deep learning techniques. The aim is to enhance human-machine interaction by enabling intuitive voice control of drone actions. The pipelines developed include: (1) a traditional Speech-to-Text (STT) followed by a Large Language Model (LLM) approach, (2) a direct voice-to-function mapping model, and (3) a Siamese neural network-based system. Each pipeline was evaluated based on inference time, accuracy, efficiency, and flexibility. Detailed methodologies, dataset preparation, and evaluation metrics are provided, offering a comprehensive analysis of each pipeline's strengths and applicability across different scenarios.

</details>

### [HebDB: a Weakly Supervised Dataset for Hebrew Speech Processing](2407.07566.md)
**Arnon Turetzky, Or Tal, Yael Segal-Feldman, Yehoshua Dissen et al.** · 2024-07-10

<details>
<summary>Abstract</summary>

We present HebDB, a weakly supervised dataset for spoken language processing in the Hebrew language. HebDB offers roughly 2500 hours of natural and spontaneous speech recordings in the Hebrew language, consisting of a large variety of speakers and topics. We provide raw recordings together with a pre-processed, weakly supervised, and filtered version. The goal of HebDB is to further enhance research and development of spoken language processing tools for the Hebrew language. Hence, we additionally provide two baseline systems for Automatic Speech Recognition (ASR): (i) a self-supervised model; and (ii) a fully supervised model. We present the performance of these two methods optimized on HebDB and compare them to current multi-lingual ASR alternatives. Results suggest the proposed method reaches better results than the evaluated baselines considering similar model sizes. Dataset, code, and models are publicly available under https://pages.cs.huji.ac.il/adiyoss-lab/HebDB/.

</details>

### [Dynamic Encoder Size Based on Data-Driven Layer-wise Pruning for Speech Recognition](2407.18930.md)
**Jingjing Xu, Wei Zhou, Zijian Yang, Eugen Beck et al.** · 2024-07-10

<details>
<summary>Abstract</summary>

Varying-size models are often required to deploy ASR systems under different hardware and/or application constraints such as memory and latency. To avoid redundant training and optimization efforts for individual models of different sizes, we present the dynamic encoder size approach, which jointly trains multiple performant models within one supernet from scratch. These subnets of various sizes are layer-wise pruned from the supernet, and thus, enjoy full parameter sharing. By combining score-based pruning with supernet training, we propose two novel methods, Simple-Top-k and Iterative-Zero-Out, to automatically select the best-performing subnets in a data-driven manner, avoiding resource-intensive search efforts. Our experiments using CTC on both Librispeech and TED-LIUM-v2 corpora show that our methods can achieve on-par performance as individually trained models of each size category. Also, our approach consistently brings small performance improvements for the full-size supernet.

</details>

### [Explaining Spectrograms in Machine Learning: A Study on Neural Networks for Speech Classification](2407.17416.md)
**Jesin James, Balamurali B. T., Binu Abeysinghe, Junchen Liu** · 2024-07-10

<details>
<summary>Abstract</summary>

This study investigates discriminative patterns learned by neural networks for accurate speech classification, with a specific focus on vowel classification tasks. By examining the activations and features of neural networks for vowel classification, we gain insights into what the networks "see" in spectrograms. Through the use of class activation mapping, we identify the frequencies that contribute to vowel classification and compare these findings with linguistic knowledge. Experiments on a American English dataset of vowels showcases the explainability of neural networks and provides valuable insights into the causes of misclassifications and their characteristics when differentiating them from unvoiced speech. This study not only enhances our understanding of the underlying acoustic cues in vowel classification but also offers opportunities for improving speech recognition by bridging the gap between abstract representations in neural networks and established linguistic knowledge

</details>

### [Tailored Design of Audio-Visual Speech Recognition Models using Branchformers](2407.06606.md)
**David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2024-07-09

<details>
<summary>Abstract</summary>

Recent advances in Audio-Visual Speech Recognition (AVSR) have led to unprecedented achievements in the field, improving the robustness of this type of system in adverse, noisy environments. In most cases, this task has been addressed through the design of models composed of two independent encoders, each dedicated to a specific modality. However, while recent works have explored unified audio-visual encoders, determining the optimal cross-modal architecture remains an ongoing challenge. Furthermore, such approaches often rely on models comprising vast amounts of parameters and high computational cost training processes. In this paper, we aim to bridge this research gap by introducing a novel audio-visual framework. Our proposed method constitutes, to the best of our knowledge, the first attempt to harness the flexibility and interpretability offered by encoder architectures, such as the Branchformer, in the design of parameter-efficient AVSR systems. To be more precise, the proposed framework consists of two steps: first, estimating audio- and video-only systems, and then designing a tailored audio-visual unified encoder based on the layer-level branch scores provided by the modality-specific models. Extensive experiments on English and Spanish AVSR benchmarks covering multiple data conditions and scenarios demonstrated the effectiveness of our proposed method. Even when trained on a moderate scale of data, our models achieve competitive word error rates (WER) of approximately 2.5\% for English and surpass existing approaches for Spanish, establishing a new benchmark with an average WER of around 9.1\%. These results reflect how our tailored AVSR system is able to reach state-of-the-art recognition rates while significantly reducing the model complexity w.r.t. the prevalent approach in the field. Code and pre-trained models are available at https://github.com/david-gimeno/tailored-avsr.

</details>

### [Spanish TrOCR: Leveraging Transfer Learning for Language Adaptation](2407.06950.md)
**Filipe Lauar, Valentin Laurent** · 2024-07-09

<details>
<summary>Abstract</summary>

This study explores the transfer learning capabilities of the TrOCR architecture to Spanish. TrOCR is a transformer-based Optical Character Recognition (OCR) model renowned for its state-of-the-art performance in English benchmarks. Inspired by Li et al. assertion regarding its adaptability to multilingual text recognition, we investigate two distinct approaches to adapt the model to a new language: integrating an English TrOCR encoder with a language specific decoder and train the model on this specific language, and fine-tuning the English base TrOCR model on a new language data. Due to the scarcity of publicly available datasets, we present a resource-efficient pipeline for creating OCR datasets in any language, along with a comprehensive benchmark of the different image generation methods employed with a focus on Visual Rich Documents (VRDs). Additionally, we offer a comparative analysis of the two approaches for the Spanish language, demonstrating that fine-tuning the English TrOCR on Spanish yields superior recognition than the language specific decoder for a fixed dataset size. We evaluate our model employing character and word error rate metrics on a public available printed dataset, comparing the performance against other open-source and cloud OCR spanish models. As far as we know, these resources represent the best open-source model for OCR in Spanish. The Spanish TrOCR models are publicly available on HuggingFace [20] and the code to generate the dataset is available on Github [25].

</details>

### [Analyzing Speech Unit Selection for Textless Speech-to-Speech Translation](2407.18332.md)
**Jarod Duret, Yannick Estève, Titouan Parcollet** · 2024-07-08

<details>
<summary>Abstract</summary>

Recent advancements in textless speech-to-speech translation systems have been driven by the adoption of self-supervised learning techniques. Although most state-of-the-art systems adopt a similar architecture to transform source language speech into sequences of discrete representations in the target language, the criteria for selecting these target speech units remains an open question. This work explores the selection process through a study of downstream tasks such as automatic speech recognition, speech synthesis, speaker recognition, and emotion recognition. Interestingly, our findings reveal a discrepancy in the optimization of discrete speech units: units that perform well in resynthesis performance do not necessarily correlate with those that enhance translation efficacy. This discrepancy underscores the nuanced complexity of target feature selection and its impact on the overall performance of speech-to-speech translation systems.

</details>

### [ERR@HRI 2024 Challenge: Multimodal Detection of Errors and Failures in Human-Robot Interactions](2407.06094.md)
**Micol Spitale, Maria Teresa Parreira, Maia Stiber, Minja Axelsson et al.** · 2024-07-08

<details>
<summary>Abstract</summary>

Despite the recent advancements in robotics and machine learning (ML), the deployment of autonomous robots in our everyday lives is still an open challenge. This is due to multiple reasons among which are their frequent mistakes, such as interrupting people or having delayed responses, as well as their limited ability to understand human speech, i.e., failure in tasks like transcribing speech to text. These mistakes may disrupt interactions and negatively influence human perception of these robots. To address this problem, robots need to have the ability to detect human-robot interaction (HRI) failures. The ERR@HRI 2024 challenge tackles this by offering a benchmark multimodal dataset of robot failures during human-robot interactions (HRI), encouraging researchers to develop and benchmark multimodal machine learning models to detect these failures. We created a dataset featuring multimodal non-verbal interaction data, including facial, speech, and pose features from video clips of interactions with a robotic coach, annotated with labels indicating the presence or absence of robot mistakes, user awkwardness, and interaction ruptures, allowing for the training and evaluation of predictive models. Challenge participants have been invited to submit their multimodal ML models for detection of robot errors and to be evaluated against various performance metrics such as accuracy, precision, recall, F1 score, with and without a margin of error reflecting the time-sensitivity of these metrics. The results of this challenge will help the research field in better understanding the robot failures in human-robot interactions and designing autonomous robots that can mitigate their own errors after successfully detecting them.

</details>

### [CosyVoice: A Scalable Multilingual Zero-shot Text-to-speech Synthesizer based on Supervised Semantic Tokens](2407.05407.md)
**Zhihao Du, Qian Chen, Shiliang Zhang, Kai Hu et al.** · 2024-07-07

<details>
<summary>Abstract</summary>

Recent years have witnessed a trend that large language model (LLM) based text-to-speech (TTS) emerges into the mainstream due to their high naturalness and zero-shot capacity. In this paradigm, speech signals are discretized into token sequences, which are modeled by an LLM with text as prompts and reconstructed by a token-based vocoder to waveforms. Obviously, speech tokens play a critical role in LLM-based TTS models. Current speech tokens are learned in an unsupervised manner, which lacks explicit semantic information and alignment to the text. In this paper, we propose to represent speech with supervised semantic tokens, which are derived from a multilingual speech recognition model by inserting vector quantization into the encoder. Based on the tokens, we further propose a scalable zero-shot TTS synthesizer, CosyVoice, which consists of an LLM for text-to-token generation and a conditional flow matching model for token-to-speech synthesis. Experimental results show that supervised semantic tokens significantly outperform existing unsupervised tokens in terms of content consistency and speaker similarity for zero-shot voice cloning. Moreover, we find that utilizing large-scale data further improves the synthesis performance, indicating the scalable capacity of CosyVoice. To the best of our knowledge, this is the first attempt to involve supervised speech tokens into TTS models.

</details>

### [Seed-ASR: Understanding Diverse Speech and Contexts with LLM-based Speech Recognition](2407.04675.md)
**Ye Bai, Jingping Chen, Jitong Chen, Wei Chen et al.** · 2024-07-05

<details>
<summary>Abstract</summary>

Modern automatic speech recognition (ASR) model is required to accurately transcribe diverse speech signals (from different domains, languages, accents, etc) given the specific contextual information in various application scenarios. Classic end-to-end models fused with extra language models perform well, but mainly in data matching scenarios and are gradually approaching a bottleneck. In this work, we introduce Seed-ASR, a large language model (LLM) based speech recognition model. Seed-ASR is developed based on the framework of audio conditioned LLM (AcLLM), leveraging the capabilities of LLMs by inputting continuous speech representations together with contextual information into the LLM. Through stage-wise large-scale training and the elicitation of context-aware capabilities in LLM, Seed-ASR demonstrates significant improvement over end-to-end models on comprehensive evaluation sets, including multiple domains, accents/dialects and languages. Additionally, Seed-ASR can be further deployed to support specific needs in various scenarios without requiring extra language models. Compared to recently released large ASR models, Seed-ASR achieves 10%-40% reduction in word (or character, for Chinese) error rates on Chinese and English public test sets, further demonstrating its powerful performance.

</details>

### [Multitaper mel-spectrograms for keyword spotting](2407.04662.md)
**Douglas Baptista de Souza, Khaled Jamal Bakri, Fernanda Ferreira, Juliana Inacio** · 2024-07-05

<details>
<summary>Abstract</summary>

Keyword spotting (KWS) is one of the speech recognition tasks most sensitive to the quality of the feature representation. However, the research on KWS has traditionally focused on new model topologies, putting little emphasis on other aspects like feature extraction. This paper investigates the use of the multitaper technique to create improved features for KWS. The experimental study is carried out for different test scenarios, windows and parameters, datasets, and neural networks commonly used in embedded KWS applications. Experiment results confirm the advantages of using the proposed improved features.

</details>

### [Pretraining End-to-End Keyword Search with Automatically Discovered Acoustic Units](2407.04652.md)
**Bolaji Yusuf, Jan "Honza" Černocký, Murat Saraçlar** · 2024-07-05

<details>
<summary>Abstract</summary>

End-to-end (E2E) keyword search (KWS) has emerged as an alternative and complimentary approach to conventional keyword search which depends on the output of automatic speech recognition (ASR) systems. While E2E methods greatly simplify the KWS pipeline, they generally have worse performance than their ASR-based counterparts, which can benefit from pretraining with untranscribed data. In this work, we propose a method for pretraining E2E KWS systems with untranscribed data, which involves using acoustic unit discovery (AUD) to obtain discrete units for untranscribed data and then learning to locate sequences of such units in the speech. We conduct experiments across languages and AUD systems: we show that finetuning such a model significantly outperforms a model trained from scratch, and the performance improvements are generally correlated with the quality of the AUD system used for pretraining.

</details>

### [Speculative Speech Recognition by Audio-Prefixed Low-Rank Adaptation of Language Models](2407.04641.md)
**Bolaji Yusuf, Murali Karthick Baskar, Andrew Rosenberg, Bhuvana Ramabhadran** · 2024-07-05

<details>
<summary>Abstract</summary>

This paper explores speculative speech recognition (SSR), where we empower conventional automatic speech recognition (ASR) with speculation capabilities, allowing the recognizer to run ahead of audio. We introduce a metric for measuring SSR performance and we propose a model which does SSR by combining a RNN-Transducer-based ASR system with an audio-prefixed language model (LM). The ASR system transcribes ongoing audio and feeds the resulting transcripts, along with an audio-dependent prefix, to the LM, which speculates likely completions for the transcriptions. We experiment with a variety of ASR datasets on which show the efficacy our method and the feasibility of SSR as a method of reducing ASR latency.

</details>

### [Written Term Detection Improves Spoken Term Detection](2407.04601.md)
**Bolaji Yusuf, Murat Saraçlar** · 2024-07-05

<details>
<summary>Abstract</summary>

End-to-end (E2E) approaches to keyword search (KWS) are considerably simpler in terms of training and indexing complexity when compared to approaches which use the output of automatic speech recognition (ASR) systems. This simplification however has drawbacks due to the loss of modularity. In particular, where ASR-based KWS systems can benefit from external unpaired text via a language model, current formulations of E2E KWS systems have no such mechanism. Therefore, in this paper, we propose a multitask training objective which allows unpaired text to be integrated into E2E KWS without complicating indexing and search. In addition to training an E2E KWS model to retrieve text queries from spoken documents, we jointly train it to retrieve text queries from masked written documents. We show empirically that this approach can effectively leverage unpaired text for KWS, with significant improvements in search performance across a wide variety of languages. We conduct analysis which indicates that these improvements are achieved because the proposed method improves document representations for words in the unpaired text. Finally, we show that the proposed method can be used for domain adaptation in settings where in-domain paired data is scarce or nonexistent.

</details>

### [Performance Analysis of Speech Encoders for Low-Resource SLU and ASR in Tunisian Dialect](2407.04533.md)
**Salima Mdhaffar, Haroun Elleuch, Fethi Bougares, Yannick Estève** · 2024-07-05

<details>
<summary>Abstract</summary>

Speech encoders pretrained through self-supervised learning (SSL) have demonstrated remarkable performance in various downstream tasks, including Spoken Language Understanding (SLU) and Automatic Speech Recognition (ASR). For instance, fine-tuning SSL models for such tasks has shown significant potential, leading to improvements in the SOTA performance across challenging datasets. In contrast to existing research, this paper contributes by comparing the effectiveness of SSL approaches in the context of (i) the low-resource spoken Tunisian Arabic dialect and (ii) its combination with a low-resource SLU and ASR scenario, where only a few semantic annotations are available for fine-tuning. We conduct experiments using many SSL speech encoders on the TARIC-SLU dataset. We use speech encoders that were pre-trained on either monolingual or multilingual speech data. Some of them have also been refined without in-domain nor Tunisian data through multimodal supervised teacher-student paradigm. This study yields numerous significant findings that we are discussing in this paper.

</details>

### [XLSR-Transducer: Streaming ASR for Self-Supervised Pretrained Models](2407.04439.md)
**Shashi Kumar, Srikanth Madikeri, Juan Zuluaga-Gomez, Esaú Villatoro-Tello et al.** · 2024-07-05

<details>
<summary>Abstract</summary>

Self-supervised pretrained models exhibit competitive performance in automatic speech recognition on finetuning, even with limited in-domain supervised data. However, popular pretrained models are not suitable for streaming ASR because they are trained with full attention context. In this paper, we introduce XLSR-Transducer, where the XLSR-53 model is used as encoder in transducer setup. Our experiments on the AMI dataset reveal that the XLSR-Transducer achieves 4% absolute WER improvement over Whisper large-v2 and 8% over a Zipformer transducer model trained from scratch. To enable streaming capabilities, we investigate different attention masking patterns in the self-attention computation of transformer layers within the XLSR-53 model. We validate XLSR-Transducer on AMI and 5 languages from CommonVoice under low-resource scenarios. Finally, with the introduction of attention sinks, we reduce the left context by half while achieving a relative 12% improvement in WER.

</details>

### [LearnerVoice: A Dataset of Non-Native English Learners' Spontaneous Speech](2407.04280.md)
**Haechan Kim, Junho Myung, Seoyoung Kim, Sungpah Lee et al.** · 2024-07-05

<details>
<summary>Abstract</summary>

Prevalent ungrammatical expressions and disfluencies in spontaneous speech from second language (L2) learners pose unique challenges to Automatic Speech Recognition (ASR) systems. However, few datasets are tailored to L2 learner speech. We publicly release LearnerVoice, a dataset consisting of 50.04 hours of audio and transcriptions of L2 learners' spontaneous speech. Our linguistic analysis reveals that transcriptions in our dataset contain L2S (L2 learner's Spontaneous speech) features, consisting of ungrammatical expressions and disfluencies (e.g., filler words, word repetitions, self-repairs, false starts), significantly more than native speech datasets. Fine-tuning whisper-small.en with LearnerVoice achieves a WER of 10.26%, 44.2% lower than vanilla whisper-small.en. Furthermore, our qualitative analysis indicates that 54.2% of errors from the vanilla model on LearnerVoice are attributable to L2S features, with 48.1% of them being reduced in the fine-tuned model.

</details>

### [Semi-supervised Learning for Code-Switching ASR with Large Language Model Filter](2407.04219.md)
**Yu Xi, Wen Ding, Kai Yu, Junjie Lai** · 2024-07-05

<details>
<summary>Abstract</summary>

Code-switching (CS) phenomenon occurs when words or phrases from different languages are alternated in a single sentence. Due to data scarcity, building an effective CS Automatic Speech Recognition (ASR) system remains challenging. In this paper, we propose to enhance CS-ASR systems by utilizing rich unsupervised monolingual speech data within a semi-supervised learning framework, particularly when access to CS data is limited. To achieve this, we establish a general paradigm for applying noisy student training (NST) to the CS-ASR task. Specifically, we introduce the LLM-Filter, which leverages well-designed prompt templates to activate the correction capability of large language models (LLMs) for monolingual data selection and pseudo-labels refinement during NST. Our experiments on the supervised ASRU-CS and unsupervised AISHELL-2 and LibriSpeech datasets show that our method not only achieves significant improvements over supervised and semi-supervised learning baselines for the CS task, but also attains better performance compared with the fully-supervised oracle upper-bound on the CS English part. Additionally, we further investigate the influence of accent on AESRC dataset and demonstrate that our method can get achieve additional benefits when the monolingual data contains relevant linguistic characteristic.

</details>

### [FunAudioLLM: Voice Understanding and Generation Foundation Models for Natural Interaction Between Humans and LLMs](2407.04051.md)
**Keyu An, Qian Chen, Chong Deng, Zhihao Du et al.** · 2024-07-04

<details>
<summary>Abstract</summary>

This report introduces FunAudioLLM, a model family designed to enhance natural voice interactions between humans and large language models (LLMs). At its core are two innovative models: SenseVoice, which handles multilingual speech recognition, emotion recognition, and audio event detection; and CosyVoice, which facilitates natural speech generation with control over multiple languages, timbre, speaking style, and speaker identity. SenseVoice-Small delivers exceptionally low-latency ASR for 5 languages, and SenseVoice-Large supports high-precision ASR for over 50 languages, while CosyVoice excels in multi-lingual voice generation, zero-shot in-context learning, cross-lingual voice cloning, and instruction-following capabilities. The models related to SenseVoice and CosyVoice have been open-sourced on Modelscope and Huggingface, along with the corresponding training, inference, and fine-tuning codes released on GitHub. By integrating these models with LLMs, FunAudioLLM enables applications such as speech-to-speech translation, emotional voice chat, interactive podcasts, and expressive audiobook narration, thereby pushing the boundaries of voice interaction technology. Demos are available at https://fun-audio-llm.github.io, and the code can be accessed at https://github.com/FunAudioLLM.

</details>

### [Improving Accented Speech Recognition using Data Augmentation based on Unsupervised Text-to-Speech Synthesis](2407.04047.md)
**Cong-Thanh Do, Shuhei Imai, Rama Doddipatla, Thomas Hain** · 2024-07-04

<details>
<summary>Abstract</summary>

This paper investigates the use of unsupervised text-to-speech synthesis (TTS) as a data augmentation method to improve accented speech recognition. TTS systems are trained with a small amount of accented speech training data and their pseudo-labels rather than manual transcriptions, and hence unsupervised. This approach enables the use of accented speech data without manual transcriptions to perform data augmentation for accented speech recognition. Synthetic accented speech data, generated from text prompts by using the TTS systems, are then combined with available non-accented speech data to train automatic speech recognition (ASR) systems. ASR experiments are performed in a self-supervised learning framework using a Wav2vec2.0 model which was pre-trained on large amount of unsupervised accented speech data. The accented speech data for training the unsupervised TTS are read speech, selected from L2-ARCTIC and British Isles corpora, while spontaneous conversational speech from the Edinburgh international accents of English corpus are used as the evaluation data. Experimental results show that Wav2vec2.0 models which are fine-tuned to downstream ASR task with synthetic accented speech data, generated by the unsupervised TTS, yield up to 6.1% relative word error rate reductions compared to a Wav2vec2.0 baseline which is fine-tuned with the non-accented speech data from Librispeech corpus.

</details>

### [Serialized Output Training by Learned Dominance](2407.03966.md)
**Ying Shi, Lantian Li, Shi Yin, Dong Wang et al.** · 2024-07-04

<details>
<summary>Abstract</summary>

Serialized Output Training (SOT) has showcased state-of-the-art performance in multi-talker speech recognition by sequentially decoding the speech of individual speakers. To address the challenging label-permutation issue, prior methods have relied on either the Permutation Invariant Training (PIT) or the time-based First-In-First-Out (FIFO) rule. This study presents a model-based serialization strategy that incorporates an auxiliary module into the Attention Encoder-Decoder architecture, autonomously identifying the crucial factors to order the output sequence of the speech components in multi-talker speech. Experiments conducted on the LibriSpeech and LibriMix databases reveal that our approach significantly outperforms the PIT and FIFO baselines in both 2-mix and 3-mix scenarios. Further analysis shows that the serialization module identifies dominant speech components in a mixture by factors including loudness and gender, and orders speech components based on the dominance score.

</details>

### [Finetuning End-to-End Models for Estonian Conversational Spoken Language Translation](2407.03809.md)
**Tiia Sildam, Andra Velve, Tanel Alumäe** · 2024-07-04

<details>
<summary>Abstract</summary>

This paper investigates the finetuning of end-to-end models for bidirectional Estonian-English and Estonian-Russian conversational speech-to-text translation. Due to the limited availability of speech translation data for Estonian, we created additional training data by web scraping and synthesizing data from speech recognition datasets using machine translation. We evaluated three publicly available end-to-end models: Whisper, OWSM 3.1, and SeamlessM4T. Our results indicate that fine-tuning with synthetic data enhances translation accuracy by a large margin, with SeamlessM4T matching or surpassing cascaded speech translation systems that use state-of-the-art speech recognition and machine translation models.

</details>

### [Improving Self-supervised Pre-training using Accent-Specific Codebooks](2407.03734.md)
**Darshan Prabhu, Abhishek Gupta, Omkar Nitsure, Preethi Jyothi et al.** · 2024-07-04

<details>
<summary>Abstract</summary>

Speech accents present a serious challenge to the performance of state-of-the-art end-to-end Automatic Speech Recognition (ASR) systems. Even with self-supervised learning and pre-training of ASR models, accent invariance is seldom achieved. In this work, we propose an accent-aware adaptation technique for self-supervised learning that introduces a trainable set of accent-specific codebooks to the self-supervised architecture. These learnable codebooks enable the model to capture accent specific information during pre-training, that is further refined during ASR finetuning. On the Mozilla Common Voice dataset, our proposed approach outperforms all other accent-adaptation approaches on both seen and unseen English accents, with up to 9% relative reduction in word error rate (WER).

</details>

### [Multi-Convformer: Extending Conformer with Multiple Convolution Kernels](2407.03718.md)
**Darshan Prabhu, Yifan Peng, Preethi Jyothi, Shinji Watanabe** · 2024-07-04

<details>
<summary>Abstract</summary>

Convolutions have become essential in state-of-the-art end-to-end Automatic Speech Recognition~(ASR) systems due to their efficient modelling of local context. Notably, its use in Conformers has led to superior performance compared to vanilla Transformer-based ASR systems. While components other than the convolution module in the Conformer have been reexamined, altering the convolution module itself has been far less explored. Towards this, we introduce Multi-Convformer that uses multiple convolution kernels within the convolution module of the Conformer in conjunction with gating. This helps in improved modeling of local dependencies at varying granularities. Our model rivals existing Conformer variants such as CgMLP and E-Branchformer in performance, while being more parameter efficient. We empirically compare our approach with Conformer and its variants across four different datasets and three different modelling paradigms and show up to 8% relative word error rate~(WER) improvements.

</details>

### [Learning Video Temporal Dynamics with Cross-Modal Attention for Robust Audio-Visual Speech Recognition](2407.03563.md)
**Sungnyun Kim, Kangwook Jang, Sangmin Bae, Hoirin Kim et al.** · 2024-07-04

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) aims to transcribe human speech using both audio and video modalities. In practical environments with noise-corrupted audio, the role of video information becomes crucial. However, prior works have primarily focused on enhancing audio features in AVSR, overlooking the importance of video features. In this study, we strengthen the video features by learning three temporal dynamics in video data: context order, playback direction, and the speed of video frames. Cross-modal attention modules are introduced to enrich video features with audio information so that speech variability can be taken into account when training on the video temporal dynamics. Based on our approach, we achieve the state-of-the-art performance on the LRS2 and LRS3 AVSR benchmarks for the noise-dominant settings. Our approach excels in scenarios especially for babble and speech noise, indicating the ability to distinguish the speech signal that should be recognized from lip movements in the video modality. We support the validity of our methodology by offering the ablation experiments for the temporal dynamics losses and the cross-modal attention architecture design.

</details>

### [Continual Learning Optimizations for Auto-regressive Decoder of Multilingual ASR systems](2407.03645.md)
**Chin Yuen Kwok, Jia Qi Yip, Eng Siong Chng** · 2024-07-04

<details>
<summary>Abstract</summary>

Continual Learning (CL) involves fine-tuning pre-trained models with new data while maintaining the performance on the pre-trained data. This is particularly relevant for expanding multilingual ASR (MASR) capabilities. However, existing CL methods, mainly designed for computer vision and reinforcement learning tasks, often yield sub-optimal results when directly applied to MASR. We hypothesise that this is because CL of the auto-regressive decoder in the MASR model is difficult. To verify this, we propose four optimizations on the decoder. They include decoder-layer gradient surgery, freezing unused token embeddings, suppressing output of newly added tokens, and learning rate re-scaling. Our experiments on adapting Whisper to 10 unseen languages from the Common Voice dataset demonstrate that these optimizations reduce the Average Word Error Rate (AWER) of pretrained languages from 14.2% to 12.4% compared with Experience Replay, without compromising the AWER of new languages.

</details>

### [Advanced Framework for Animal Sound Classification With Features Optimization](2407.03440.md)
**Qiang Yang, Xiuying Chen, Changsheng Ma, Carlos M. Duarte et al.** · 2024-07-03

<details>
<summary>Abstract</summary>

The automatic classification of animal sounds presents an enduring challenge in bioacoustics, owing to the diverse statistical properties of sound signals, variations in recording equipment, and prevalent low Signal-to-Noise Ratio (SNR) conditions. Deep learning models like Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) have excelled in human speech recognition but have not been effectively tailored to the intricate nature of animal sounds, which exhibit substantial diversity even within the same domain. We propose an automated classification framework applicable to general animal sound classification. Our approach first optimizes audio features from Mel-frequency cepstral coefficients (MFCC) including feature rearrangement and feature reduction. It then uses the optimized features for the deep learning model, i.e., an attention-based Bidirectional LSTM (Bi-LSTM), to extract deep semantic features for sound classification. We also contribute an animal sound benchmark dataset encompassing oceanic animals and birds1. Extensive experimentation with real-world datasets demonstrates that our approach consistently outperforms baseline methods by over 25% in precision, recall, and accuracy, promising advancements in animal sound classification.

</details>

### [Qifusion-Net: Layer-adapted Stream/Non-stream Model for End-to-End Multi-Accent Speech Recognition](2407.03026.md)
**Jinming Chen, Jingyi Fang, Yuanzhong Zheng, Yaoxuan Wang et al.** · 2024-07-03

<details>
<summary>Abstract</summary>

Currently, end-to-end (E2E) speech recognition methods have achieved promising performance. However, auto speech recognition (ASR) models still face challenges in recognizing multi-accent speech accurately. We propose a layer-adapted fusion (LAF) model, called Qifusion-Net, which does not require any prior knowledge about the target accent. Based on dynamic chunk strategy, our approach enables streaming decoding and can extract frame-level acoustic feature, facilitating fine-grained information fusion. Experiment results demonstrate that our proposed methods outperform the baseline with relative reductions of 22.1$\%$ and 17.2$\%$ in character error rate (CER) across multi accent test datasets on KeSpeech and MagicData-RMAC.

</details>

### [Investigating Decoder-only Large Language Models for Speech-to-text Translation](2407.03169.md)
**Chao-Wei Huang, Hui Lu, Hongyu Gong, Hirofumi Inaguma et al.** · 2024-07-03

<details>
<summary>Abstract</summary>

Large language models (LLMs), known for their exceptional reasoning capabilities, generalizability, and fluency across diverse domains, present a promising avenue for enhancing speech-related tasks. In this paper, we focus on integrating decoder-only LLMs to the task of speech-to-text translation (S2TT). We propose a decoder-only architecture that enables the LLM to directly consume the encoded speech representation and generate the text translation. Additionally, we investigate the effects of different parameter-efficient fine-tuning techniques and task formulation. Our model achieves state-of-the-art performance on CoVoST 2 and FLEURS among models trained without proprietary data. We also conduct analyses to validate the design choices of our proposed model and bring insights to the integration of LLMs to S2TT.

</details>

### [The USTC-NERCSLIP Systems for The ICMC-ASR Challenge](2407.02052.md)
**Minghui Wu, Luzhen Xu, Jie Zhang, Haitao Tang et al.** · 2024-07-02

<details>
<summary>Abstract</summary>

This report describes the submitted system to the In-Car Multi-Channel Automatic Speech Recognition (ICMC-ASR) challenge, which considers the ASR task with multi-speaker overlapping and Mandarin accent dynamics in the ICMC case. We implement the front-end speaker diarization using the self-supervised learning representation based multi-speaker embedding and beamforming using the speaker position, respectively. For ASR, we employ an iterative pseudo-label generation method based on fusion model to obtain text labels of unsupervised data. To mitigate the impact of accent, an Accent-ASR framework is proposed, which captures pronunciation-related accent features at a fine-grained level and linguistic information at a coarse-grained level. On the ICMC-ASR eval set, the proposed system achieves a CER of 13.16% on track 1 and a cpCER of 21.48% on track 2, which significantly outperforms the official baseline system and obtains the first rank on both tracks.

</details>

### [Towards the Next Frontier in Speech Representation Learning Using Disentanglement](2407.02543.md)
**Varun Krishna, Sriram Ganapathy** · 2024-07-02

<details>
<summary>Abstract</summary>

The popular frameworks for self-supervised learning of speech representations have largely focused on frame-level masked prediction of speech regions. While this has shown promising downstream task performance for speech recognition and related tasks, this has largely ignored factors of speech that are encoded at coarser level, like characteristics of the speaker or channel that remain consistent through-out a speech utterance. In this work, we propose a framework for Learning Disentangled Self Supervised (termed as Learn2Diss) representations of speech, which consists of frame-level and an utterance-level encoder modules. The two encoders are initially learned independently, where the frame-level model is largely inspired by existing self supervision techniques, thereby learning pseudo-phonemic representations, while the utterance-level encoder is inspired by constrastive learning of pooled embeddings, thereby learning pseudo-speaker representations. The joint learning of these two modules consists of disentangling the two encoders using a mutual information based criterion. With several downstream evaluation experiments, we show that the proposed Learn2Diss achieves state-of-the-art results on a variety of tasks, with the frame-level encoder representations improving semantic tasks, while the utterance-level representations improve non-semantic tasks.

</details>

### [Pinyin Regularization in Error Correction for Chinese Speech Recognition with Large Language Models](2407.01909.md)
**Zhiyuan Tang, Dong Wang, Shen Huang, Shidong Shang** · 2024-07-02

<details>
<summary>Abstract</summary>

Recent studies have demonstrated the efficacy of large language models (LLMs) in error correction for automatic speech recognition (ASR). However, much of the research focuses on the English language. This paper redirects the attention to Chinese. Firstly, we construct a specialized benchmark dataset aimed at error correction for Chinese ASR with 724K hypotheses-transcription pairs, named the Chinese Hypotheses Paradise dataset (ChineseHP), which contains a wide range of scenarios and presents significant challenges. Subsequently, we conduct a preliminary evaluation using the dataset for both direct-prompting and fine-tuning pre-trained LLMs. Furthermore, we propose a straightforward method of Pinyin regularization for prompts, which involves the transcription of Pinyin directly from text hypotheses. The experimental results reveal that Pinyin regularization consistently enhances the error-correcting ability of LLMs when compared with those without regularization. The dataset is available on the website.

</details>

### [Cross-Lingual Transfer Learning for Speech Translation](2407.01130.md)
**Rao Ma, Mengjie Qian, Yassir Fathullah, Siyuan Tang et al.** · 2024-07-01

<details>
<summary>Abstract</summary>

There has been increasing interest in building multilingual foundation models for NLP and speech research. This paper examines how to expand the speech translation capability of these models with restricted data. Whisper, a speech foundation model with strong performance on speech recognition and English translation, is used as the example model. Using speech-to-speech retrieval to analyse the audio representations generated by the encoder, we show that utterances from different languages are mapped to a shared semantic space. This shared embedding space can then be leveraged for zero-shot cross-lingual transfer in speech translation. By fine-tuning the Whisper decoder with only English-to-Chinese speech translation data, improved performance for translation to Chinese can be obtained for multiple languages, in addition to English. Furthermore, for languages related to those seen in training it is possible to perform speech translation, despite the model never seeing the language in training, or being able to perform transcription.

</details>

### [Less Forgetting for Better Generalization: Exploring Continual-learning Fine-tuning Methods for Speech Self-supervised Representations](2407.00756.md)
**Salah Zaiem, Titouan Parcollet, Slim Essid** · 2024-06-30

<details>
<summary>Abstract</summary>

Despite being trained on massive and diverse datasets, speech self-supervised encoders are generally used for downstream purposes as mere frozen feature extractors or model initializers before fine-tuning. The former severely limits the exploitation of large encoders, while the latter hurts the robustness acquired during pretraining, especially in low-resource scenarios. This work explores middle-ground solutions, conjecturing that reducing the forgetting of the self-supervised task during the downstream fine-tuning leads to better generalization. To prove this, focusing on speech recognition, we benchmark different continual-learning approaches during fine-tuning and show that they improve both in-domain and out-of-domain generalization abilities. Relative performance gains reach 15.7% and 22.5% with XLSR used as the encoder on two English and Danish speech recognition tasks. Further probing experiments show that these gains are indeed linked to less forgetting.

</details>

### [NAIST Simultaneous Speech Translation System for IWSLT 2024](2407.00826.md)
**Yuka Ko, Ryo Fukuda, Yuta Nishikawa, Yasumasa Kano et al.** · 2024-06-30

<details>
<summary>Abstract</summary>

This paper describes NAIST's submission to the simultaneous track of the IWSLT 2024 Evaluation Campaign: English-to-{German, Japanese, Chinese} speech-to-text translation and English-to-Japanese speech-to-speech translation. We develop a multilingual end-to-end speech-to-text translation model combining two pre-trained language models, HuBERT and mBART. We trained this model with two decoding policies, Local Agreement (LA) and AlignAtt. The submitted models employ the LA policy because it outperformed the AlignAtt policy in previous models. Our speech-to-speech translation method is a cascade of the above speech-to-text model and an incremental text-to-speech (TTS) module that incorporates a phoneme estimation model, a parallel acoustic model, and a parallel WaveGAN vocoder. We improved our incremental TTS by applying the Transformer architecture with the AlignAtt policy for the estimation model. The results show that our upgraded TTS module contributed to improving the system performance.

</details>

### [MoNet: A Mixture of Experts Solution for Multilingual and Low-Resource ASR Challenges](s2:ddf8522bb6067fc109b03fc2dd93904ca6bc4b56.md)
**Yongchao Li, Lixu Sun, Yineng Cai, Nurmemet Yolwas** · 2024-06-30

<details>
<summary>Abstract</summary>

Contemporary end-to-end automatic speech recognition models have demonstrated remarkable performance in monolingual contexts with abundant corpora. However, their efficacy is considerably compromised in multilingual and resource-scarce environments due to the models’ inability to effectively learn the diverse linguistic features from unevenly distributed corpora during training. Hence, enabling these models to assimilate a broader spectrum of effective features presents a significant challenge. In this paper, we introduce a novel multilingual automatic speech recognition network, MoNet, predicated on the Mixture of Experts (MoE) approach, which is capable of automatically and efficiently processing multilingual speech data without the need for any language-specific cues. Specifically, within MoNet, the MoE layer employs a router to select a fixed number of optimal experts from an expert pool to guide the network’s learning and provide efficacious reasoning, followed by the use of joint CTC/Attention training and the implementation of a secondary scoring mechanism to further enhance the model’s performance. We conducted hybrid training and evaluation of the proposed model using a compendium of corpora from six linguistically diverse languages with considerable variance in total training duration—Turkish, Uighur, Bashkir, Uzbek, Kyrgyz, and Russian—sourced from the publicly accessible CommonVoice dataset. Our findings indicate that compared to the baseline model, MoNet achieves significant improvements, with a maximum reduction in Word Error Rate (WER) of up to 4.1% for individual languages and an average decrease of 1.78% in WER across multiple languages, while still maintaining an inference cost comparable to that of the baseline model. The experimental outcomes underscore the significant advantages of our proposed model for low-resource, multilingual speech recognition tasks.

</details>

### [When Robots Get Chatty: Grounding Multimodal Human-Robot Conversation and Collaboration](2407.00518.md)
**Philipp Allgeuer, Hassan Ali, Stefan Wermter** · 2024-06-29

<details>
<summary>Abstract</summary>

We investigate the use of Large Language Models (LLMs) to equip neural robotic agents with human-like social and cognitive competencies, for the purpose of open-ended human-robot conversation and collaboration. We introduce a modular and extensible methodology for grounding an LLM with the sensory perceptions and capabilities of a physical robot, and integrate multiple deep learning models throughout the architecture in a form of system integration. The integrated models encompass various functions such as speech recognition, speech generation, open-vocabulary object detection, human pose estimation, and gesture detection, with the LLM serving as the central text-based coordinating unit. The qualitative and quantitative results demonstrate the huge potential of LLMs in providing emergent cognition and interactive language-oriented control of robots in a natural and social manner.

</details>

### [Error Correction by Paying Attention to Both Acoustic and Confidence References for Automatic Speech Recognition](2407.12817.md)
**Yuchun Shu, Bo Hu, Yifeng He, Hao Shi et al.** · 2024-06-29

<details>
<summary>Abstract</summary>

Accurately finding the wrong words in the automatic speech recognition (ASR) hypothesis and recovering them well-founded is the goal of speech error correction. In this paper, we propose a non-autoregressive speech error correction method. A Confidence Module measures the uncertainty of each word of the N-best ASR hypotheses as the reference to find the wrong word position. Besides, the acoustic feature from the ASR encoder is also used to provide the correct pronunciation references. N-best candidates from ASR are aligned using the edit path, to confirm each other and recover some missing character errors. Furthermore, the cross-attention mechanism fuses the information between error correction references and the ASR hypothesis. The experimental results show that both the acoustic and confidence references help with error correction. The proposed system reduces the error rate by 21% compared with the ASR model.

</details>

### [Open-Source Conversational AI with SpeechBrain 1.0](2407.00463.md)
**Mirco Ravanelli, Titouan Parcollet, Adel Moumen, Sylvain de Langen et al.** · 2024-06-29

<details>
<summary>Abstract</summary>

SpeechBrain is an open-source Conversational AI toolkit based on PyTorch, focused particularly on speech processing tasks such as speech recognition, speech enhancement, speaker recognition, text-to-speech, and much more. It promotes transparency and replicability by releasing both the pre-trained models and the complete "recipes" of code and algorithms required for training them. This paper presents SpeechBrain 1.0, a significant milestone in the evolution of the toolkit, which now has over 200 recipes for speech, audio, and language processing tasks, and more than 100 models available on Hugging Face. SpeechBrain 1.0 introduces new technologies to support diverse learning modalities, Large Language Model (LLM) integration, and advanced decoding strategies, along with novel models, tasks, and modalities. It also includes a new benchmark repository, offering researchers a unified platform for evaluating models across diverse tasks.

</details>

### [A Quality-Aware Voltage Overscaling Framework to Improve the Energy Efficiency and Lifetime of TPUs based on Statistical Error Modeling](2407.12029.md)
**Alireza Senobari, Jafar Vafaei, Omid Akbari, Christian Hochberger et al.** · 2024-06-29

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are a type of artificial intelligence models that are inspired by the structure and function of the human brain, designed to process and learn from large amounts of data, making them particularly well-suited for tasks such as image and speech recognition. However, applications of DNNs are experiencing emerging growth due to the deployment of specialized accelerators such as the Google Tensor Processing Units (TPUs). In large-scale deployments, the energy efficiency of such accelerators may become a critical concern. In the voltage overscaling (VOS) technique, the operating voltage of the system is scaled down beyond the nominal operating voltage, which increases the energy efficiency and lifetime of digital circuits. The VOS technique is usually performed without changing the frequency resulting in timing errors. However, some applications such as multimedia processing, including DNNs, have intrinsic resilience against errors and noise. In this paper, we exploit the inherent resilience of DNNs to propose a quality-aware voltage overscaling framework for TPUs, named X-TPU, which offers higher energy efficiency and lifetime compared to conventional TPUs. The X-TPU framework is composed of two main parts, a modified TPU architecture that supports a runtime voltage overscaling, and a statistical error modeling-based algorithm to determine the voltage of neurons such that the output quality is retained above a given user-defined quality threshold. We synthesized a single-neuron architecture using a 15-nm FinFET technology under various operating voltage levels. Then, we extracted different statistical error models for a neuron corresponding to those voltage levels. Using these models and the proposed algorithm, we determined the appropriate voltage of each neuron. Results show that running a DNN on X-TPU can achieve 32% energy saving for only 0.6% accuracy loss.

</details>

### [SAML: Speaker Adaptive Mixture of LoRA Experts for End-to-End ASR](2406.19706.md)
**Qiuming Zhao, Guangzhi Sun, Chao Zhang, Mingxing Xu et al.** · 2024-06-28

<details>
<summary>Abstract</summary>

Mixture-of-experts (MoE) models have achieved excellent results in many tasks. However, conventional MoE models are often very large, making them challenging to deploy on resource-constrained edge devices. In this paper, we propose a novel speaker adaptive mixture of LoRA experts (SAML) approach, which uses low-rank adaptation (LoRA) modules as experts to reduce the number of trainable parameters in MoE. Specifically, SAML is applied to the quantised and personalised end-to-end automatic speech recognition models, which combines test-time speaker adaptation to improve the performance of heavily compressed models in speaker-specific scenarios. Experiments have been performed on the LibriSpeech and the TED-LIUM 3 corpora. Remarkably, with a 7x reduction in model size, 29.1% and 31.1% relative word error rate reductions were achieved on the quantised Whisper model and Conformer-based attention-based encoder-decoder ASR model respectively, comparing to the original full precision models.

</details>

### [Less is More: Accurate Speech Recognition & Translation without Web-Scale Data](2406.19674.md)
**Krishna C. Puvvada, Piotr Żelasko, He Huang, Oleksii Hrinchuk et al.** · 2024-06-28

<details>
<summary>Abstract</summary>

Recent advances in speech recognition and translation rely on hundreds of thousands of hours of Internet speech data. We argue that state-of-the art accuracy can be reached without relying on web-scale data. Canary - multilingual ASR and speech translation model, outperforms current state-of-the-art models - Whisper, OWSM, and Seamless-M4T on English, French, Spanish, and German languages, while being trained on an order of magnitude less data than these models. Three key factors enables such data-efficient model: (1) a FastConformer-based attention encoder-decoder architecture (2) training on synthetic data generated with machine translation and (3) advanced training techniques: data-balancing, dynamic data blending, dynamic bucketing and noise-robust fine-tuning. The model, weights, and training code will be open-sourced.

</details>

### [Bestow: Efficient and Streamable Speech Language Model with The Best of Two Worlds in GPT and T5](2406.19954.md)
**Zhehuai Chen, He Huang, Oleksii Hrinchuk, Krishna C. Puvvada et al.** · 2024-06-28

<details>
<summary>Abstract</summary>

Incorporating speech understanding capabilities into pretrained large-language models has become a vital research direction (SpeechLLM). The previous architectures can be categorized as: i) GPT-style, prepend speech prompts to the text prompts as a sequence of LLM inputs like a decoder-only model; ii) T5-style, introduce speech cross-attention to each layer of the pretrained LLMs. We propose BESTOW architecture to bring the BESt features from $T w O$ Worlds into a single model that is highly efficient and has strong multitask capabilities. Moreover, there is no clear streaming solution for either style, especially considering the solution should generalize to speech multitask. We reformulate streamable SpeechLLM as a read-write policy problem and unifies the offline and streaming research with BESTOW architecture. Hence we demonstrate the first open-source SpeechLLM solution that enables Streaming and Multitask at scale (beyond ASR) at the same time. This streamable solution achieves very strong performance on a wide range of speech tasks (ASR, AST, SQA, unseen DynamicSuperb). It is end-to-end optimizable, with lower training/inference cost, and demonstrates LLM knowledge transferability to speech.

</details>

### [Tradition or Innovation: A Comparison of Modern ASR Methods for Forced Alignment](2406.19363.md)
**Rotem Rousso, Eyal Cohen, Joseph Keshet, Eleanor Chodroff** · 2024-06-27

<details>
<summary>Abstract</summary>

Forced alignment (FA) plays a key role in speech research through the automatic time alignment of speech signals with corresponding text transcriptions. Despite the move towards end-to-end architectures for speech technology, FA is still dominantly achieved through a classic GMM-HMM acoustic model. This work directly compares alignment performance from leading automatic speech recognition (ASR) methods, WhisperX and Massively Multilingual Speech Recognition (MMS), against a Kaldi-based GMM-HMM system, the Montreal Forced Aligner (MFA). Performance was assessed on the manually aligned TIMIT and Buckeye datasets, with comparisons conducted only on words correctly recognized by WhisperX and MMS. The MFA outperformed both WhisperX and MMS, revealing a shortcoming of modern ASR systems. These findings highlight the need for advancements in forced alignment and emphasize the importance of integrating traditional expertise with modern innovation to foster progress. Index Terms: forced alignment, phoneme alignment, word alignment

</details>

### [Applying LLMs for Rescoring N-best ASR Hypotheses of Casual Conversations: Effects of Domain Adaptation and Context Carry-over](2406.18972.md)
**Atsunori Ogawa, Naoyuki Kamo, Kohei Matsuura, Takanori Ashihara et al.** · 2024-06-27

<details>
<summary>Abstract</summary>

Large language models (LLMs) have been successfully applied for rescoring automatic speech recognition (ASR) hypotheses. However, their ability to rescore ASR hypotheses of casual conversations has not been sufficiently explored. In this study, we reveal it by performing N-best ASR hypotheses rescoring using Llama2 on the CHiME-7 distant ASR (DASR) task. Llama2 is one of the most representative LLMs, and the CHiME-7 DASR task provides datasets of casual conversations between multiple participants. We investigate the effects of domain adaptation of the LLM and context carry-over when performing N-best rescoring. Experimental results show that, even without domain adaptation, Llama2 outperforms a standard-size domain-adapted Transformer-LM, especially when using a long context. Domain adaptation shortens the context length needed with Llama2 to achieve its best performance, i.e., it reduces the computational cost of Llama2.

</details>

### [Streaming Decoder-Only Automatic Speech Recognition with Discrete Speech Units: A Pilot Study](2406.18862.md)
**Peikun Chen, Sining Sun, Changhao Shan, Qing Yang et al.** · 2024-06-27

<details>
<summary>Abstract</summary>

Unified speech-text models like SpeechGPT, VioLA, and AudioPaLM have shown impressive performance across various speech-related tasks, especially in Automatic Speech Recognition (ASR). These models typically adopt a unified method to model discrete speech and text tokens, followed by training a decoder-only transformer. However, they are all designed for non-streaming ASR tasks, where the entire speech utterance is needed during decoding. Hence, we introduce a decoder-only model exclusively designed for streaming recognition, incorporating a dedicated boundary token to facilitate streaming recognition and employing causal attention masking during the training phase. Furthermore, we introduce right-chunk attention and various data augmentation techniques to improve the model's contextual modeling abilities. While achieving streaming speech recognition, experiments on the AISHELL-1 and -2 datasets demonstrate the competitive performance of our streaming approach with non-streaming decoder-only counterparts.

</details>

### [Towards Crowd-Based Requirements Engineering for Digital Farming (CrowdRE4DF)](2406.19171.md)
**Eduard C. Groen, Kazi Rezoanur Rahman, Nikita Narsinghani, Joerg Doerr** · 2024-06-27

<details>
<summary>Abstract</summary>

The farming domain has seen a tremendous shift towards digital solutions. However, capturing farmers' requirements regarding Digital Farming (DF) technology remains a difficult task due to domain-specific challenges. Farmers form a diverse and international crowd of practitioners who use a common pool of agricultural products and services, which means we can consider the possibility of applying Crowd-based Requirements Engineering (CrowdRE) for DF: CrowdRE4DF. We found that online user feedback in this domain is limited, necessitating a way of capturing user feedback from farmers in situ. Our solution, the Farmers' Voice application, uses speech-to-text, Machine Learning (ML), and Web 2.0 technology. A preliminary evaluation with five farmers showed good technology acceptance, and accurate transcription and ML analysis even in noisy farm settings. Our findings help to drive the development of DF technology through in-situ requirements elicitation.

</details>

### [MSR-86K: An Evolving, Multilingual Corpus with 86,300 Hours of Transcribed Audio for Speech Recognition Research](2406.18301.md)
**Song Li, Yongbin You, Xuezhi Wang, Zhengkun Tian et al.** · 2024-06-26

<details>
<summary>Abstract</summary>

Recently, multilingual artificial intelligence assistants, exemplified by ChatGPT, have gained immense popularity. As a crucial gateway to human-computer interaction, multilingual automatic speech recognition (ASR) has also garnered significant attention, as evidenced by systems like Whisper. However, the proprietary nature of the training data has impeded researchers' efforts to study multilingual ASR. This paper introduces MSR-86K, an evolving, large-scale multilingual corpus for speech recognition research. The corpus is derived from publicly accessible videos on YouTube, comprising 15 languages and a total of 86,300 hours of transcribed ASR data. We also introduce how to use the MSR-86K corpus and other open-source corpora to train a robust multilingual ASR model that is competitive with Whisper. MSR-86K will be publicly released on HuggingFace, and we believe that such a large corpus will pave new avenues for research in multilingual ASR.

</details>

### [Automatic Speech Recognition for Hindi](2406.18135.md)
**Anish Saha, A. G. Ramakrishnan** · 2024-06-26

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is a key area in computational linguistics, focusing on developing technologies that enable computers to convert spoken language into text. This field combines linguistics and machine learning. ASR models, which map speech audio to transcripts through supervised learning, require handling real and unrestricted text. Text-to-speech systems directly work with real text, while ASR systems rely on language models trained on large text corpora. High-quality transcribed data is essential for training predictive models. The research involved two main components: developing a web application and designing a web interface for speech recognition. The web application, created with JavaScript and Node.js, manages large volumes of audio files and their transcriptions, facilitating collaborative human correction of ASR transcripts. It operates in real-time using a client-server architecture. The web interface for speech recognition records 16 kHz mono audio from any device running the web app, performs voice activity detection (VAD), and sends the audio to the recognition engine. VAD detects human speech presence, aiding efficient speech processing and reducing unnecessary processing during non-speech intervals, thus saving computation and network bandwidth in VoIP applications. The final phase of the research tested a neural network for accurately aligning the speech signal to hidden Markov model (HMM) states. This included implementing a novel backpropagation method that utilizes prior statistics of node co-activations.

</details>

### [SC-MoE: Switch Conformer Mixture of Experts for Unified Streaming and Non-streaming Code-Switching ASR](2406.18021.md)
**Shuaishuai Ye, Shunfei Chen, Xinhui Hu, Xinkang Xu** · 2024-06-26

<details>
<summary>Abstract</summary>

In this work, we propose a Switch-Conformer-based MoE system named SC-MoE for unified streaming and non-streaming code-switching (CS) automatic speech recognition (ASR), where we design a streaming MoE layer consisting of three language experts, which correspond to Mandarin, English, and blank, respectively, and equipped with a language identification (LID) network with a Connectionist Temporal Classification (CTC) loss as a router in the encoder of SC-MoE to achieve a real-time streaming CS ASR system. To further utilize the language information embedded in text, we also incorporate MoE layers into the decoder of SC-MoE. In addition, we introduce routers into every MoE layer of the encoder and the decoder and achieve better recognition performance. Experimental results show that the SC-MoE significantly improves CS ASR performances over baseline with comparable computational efficiency.

</details>

### [Continuous Sign Language Recognition Using Intra-inter Gloss Attention](2406.18333.md)
**Hossein Ranjbar, Alireza Taheri** · 2024-06-26

<details>
<summary>Abstract</summary>

Many continuous sign language recognition (CSLR) studies adopt transformer-based architectures for sequence modeling due to their powerful capacity for capturing global contexts. Nevertheless, vanilla self-attention, which serves as the core module of the transformer, calculates a weighted average over all time steps; therefore, the local temporal semantics of sign videos may not be fully exploited. In this study, we introduce a novel module in sign language recognition studies, called intra-inter gloss attention module, to leverage the relationships among frames within glosses and the semantic and grammatical dependencies between glosses in the video. In the intra-gloss attention module, the video is divided into equally sized chunks and a self-attention mechanism is applied within each chunk. This localized self-attention significantly reduces complexity and eliminates noise introduced by considering non-relative frames. In the inter-gloss attention module, we first aggregate the chunk-level features within each gloss chunk by average pooling along the temporal dimension. Subsequently, multi-head self-attention is applied to all chunk-level features. Given the non-significance of the signer-environment interaction, we utilize segmentation to remove the background of the videos. This enables the proposed model to direct its focus toward the signer. Experimental results on the PHOENIX-2014 benchmark dataset demonstrate that our method can effectively extract sign language features in an end-to-end manner without any prior knowledge, improve the accuracy of CSLR, and achieve the word error rate (WER) of 20.4 on the test set which is a competitive result compare to the state-of-the-art which uses additional supervisions.

</details>

### [Sequential Editing for Lifelong Training of Speech Recognition Models](2406.17935.md)
**Devang Kulshreshtha, Saket Dingliwal, Brady Houston, Nikolaos Pappas et al.** · 2024-06-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) traditionally assumes known domains, but adding data from a new domain raises concerns about computational inefficiencies linked to retraining models on both existing and new domains. Fine-tuning solely on new domain risks Catastrophic Forgetting (CF). To address this, Lifelong Learning (LLL) algorithms have been proposed for ASR. Prior research has explored techniques such as Elastic Weight Consolidation, Knowledge Distillation, and Replay, all of which necessitate either additional parameters or access to prior domain data. We propose Sequential Model Editing as a novel method to continually learn new domains in ASR systems. Different than previous methods, our approach does not necessitate access to prior datasets or the introduction of extra parameters. Our study demonstrates up to 15% Word Error Rate Reduction (WERR) over fine-tuning baseline, and superior efficiency over other LLL techniques on CommonVoice English multi-accent dataset.

</details>

### [FASA: a Flexible and Automatic Speech Aligner for Extracting High-quality Aligned Children Speech Data](2406.17926.md)
**Dancheng Liu, Jinjun Xiong** · 2024-06-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) for adults' speeches has made significant progress by employing deep neural network (DNN) models recently, but improvement in children's speech is still unsatisfactory due to children's speech's distinct characteristics. DNN models pre-trained on adult data often struggle in generalizing children's speeches with fine tuning because of the lack of high-quality aligned children's speeches. When generating datasets, human annotations are not scalable, and existing forced-alignment tools are not usable as they make impractical assumptions about the quality of the input transcriptions. To address these challenges, we propose a new forced-alignment tool, FASA, as a flexible and automatic speech aligner to extract high-quality aligned children's speech data from many of the existing noisy children's speech data. We demonstrate its usage on the CHILDES dataset and show that FASA can improve data quality by 13.6$\times$ over human annotations.

</details>

### [Towards Building an End-to-End Multilingual Automatic Lyrics Transcription Model](2406.17618.md)
**Jiawen Huang, Emmanouil Benetos** · 2024-06-25

<details>
<summary>Abstract</summary>

Multilingual automatic lyrics transcription (ALT) is a challenging task due to the limited availability of labelled data and the challenges introduced by singing, compared to multilingual automatic speech recognition. Although some multilingual singing datasets have been released recently, English continues to dominate these collections. Multilingual ALT remains underexplored due to the scale of data and annotation quality. In this paper, we aim to create a multilingual ALT system with available datasets. Inspired by architectures that have been proven effective for English ALT, we adapt these techniques to the multilingual scenario by expanding the target vocabulary set. We then evaluate the performance of the multilingual model in comparison to its monolingual counterparts. Additionally, we explore various conditioning methods to incorporate language information into the model. We apply analysis by language and combine it with the language classification performance. Our findings reveal that the multilingual model performs consistently better than the monolingual models trained on the language subsets. Furthermore, we demonstrate that incorporating language information significantly enhances performance.

</details>

### [MSRS: Training Multimodal Speech Recognition Models from Scratch with Sparse Mask Optimization](2406.17614.md)
**Adriana Fernandez-Lopez, Honglie Chen, Pingchuan Ma, Lu Yin et al.** · 2024-06-25

<details>
<summary>Abstract</summary>

Pre-trained models have been a foundational approach in speech recognition, albeit with associated additional costs. In this study, we propose a regularization technique that facilitates the training of visual and audio-visual speech recognition models (VSR and AVSR) from scratch. This approach, abbreviated as \textbf{MSRS} (Multimodal Speech Recognition from Scratch), introduces a sparse regularization that rapidly learns sparse structures within the dense model at the very beginning of training, which receives healthier gradient flow than the dense equivalent. Once the sparse mask stabilizes, our method allows transitioning to a dense model or keeping a sparse model by updating non-zero values. MSRS achieves competitive results in VSR and AVSR with 21.1% and 0.9% WER on the LRS3 benchmark, while reducing training time by at least 2x. We explore other sparse approaches and show that only MSRS enables training from scratch by implicitly masking the weights affected by vanishing gradients.

</details>

### [Automatic speech recognition for the Nepali language using CNN, bidirectional LSTM and ResNet](2406.17825.md)
**Manish Dhakal, Arman Chhetri, Aman Kumar Gupta, Prabin Lamichhane et al.** · 2024-06-25

<details>
<summary>Abstract</summary>

This paper presents an end-to-end deep learning model for Automatic Speech Recognition (ASR) that transcribes Nepali speech to text. The model was trained and tested on the OpenSLR (audio, text) dataset. The majority of the audio dataset have silent gaps at both ends which are clipped during dataset preprocessing for a more uniform mapping of audio frames and their corresponding texts. Mel Frequency Cepstral Coefficients (MFCCs) are used as audio features to feed into the model. The model having Bidirectional LSTM paired with ResNet and one-dimensional CNN produces the best results for this dataset out of all the models (neural networks with variations of LSTM, GRU, CNN, and ResNet) that have been trained so far. This novel model uses Connectionist Temporal Classification (CTC) function for loss calculation during training and CTC beam search decoding for predicting characters as the most likely sequence of Nepali text. On the test dataset, the character error rate (CER) of 17.06 percent has been achieved. The source code is available at: https://github.com/manishdhakal/ASR-Nepali-using-CNN-BiLSTM-ResNet.

</details>

### [A Comprehensive Solution to Connect Speech Encoder and Large Language Model for ASR](2406.17272.md)
**Van Tung Pham, Yist Lin, Tao Han, Wei Li et al.** · 2024-06-25

<details>
<summary>Abstract</summary>

Recent works have shown promising results in connecting speech encoders to large language models (LLMs) for speech recognition. However, several limitations persist, including limited fine-tuning options, a lack of mechanisms to enforce speech-text alignment, and high insertion errors especially in domain mismatch conditions. This paper presents a comprehensive solution to address these issues. We begin by investigating more thoughtful fine-tuning schemes. Next, we propose a matching loss to enhance alignment between modalities. Finally, we explore training and inference methods to mitigate high insertion errors. Experimental results on the Librispeech corpus demonstrate that partially fine-tuning the encoder and LLM using parameter-efficient methods, such as LoRA, is the most cost-effective approach. Additionally, the matching loss improves modality alignment, enhancing performance. The proposed training and inference methods significantly reduce insertion errors.

</details>

### [AG-LSEC: Audio Grounded Lexical Speaker Error Correction](2406.17266.md)
**Rohit Paturi, Xiang Li, Sundararajan Srinivasan** · 2024-06-25

<details>
<summary>Abstract</summary>

Speaker Diarization (SD) systems are typically audio-based and operate independently of the ASR system in traditional speech transcription pipelines and can have speaker errors due to SD and/or ASR reconciliation, especially around speaker turns and regions of speech overlap. To reduce these errors, a Lexical Speaker Error Correction (LSEC), in which an external language model provides lexical information to correct the speaker errors, was recently proposed. Though the approach achieves good Word Diarization error rate (WDER) improvements, it does not use any additional acoustic information and is prone to miscorrections. In this paper, we propose to enhance and acoustically ground the LSEC system with speaker scores directly derived from the existing SD pipeline. This approach achieves significant relative WDER reductions in the range of 25-40% over the audio-based SD, ASR system and beats the LSEC system by 15-25% relative on RT03-CTS, Callhome American English and Fisher datasets.

</details>

### [Exploring the Capability of Mamba in Speech Applications](2406.16808.md)
**Koichi Miyazaki, Yoshiki Masuyama, Masato Murata** · 2024-06-24

<details>
<summary>Abstract</summary>

This paper explores the capability of Mamba, a recently proposed architecture based on state space models (SSMs), as a competitive alternative to Transformer-based models. In the speech domain, well-designed Transformer-based models, such as the Conformer and E-Branchformer, have become the de facto standards. Extensive evaluations have demonstrated the effectiveness of these Transformer-based models across a wide range of speech tasks. In contrast, the evaluation of SSMs has been limited to a few tasks, such as automatic speech recognition (ASR) and speech synthesis. In this paper, we compared Mamba with state-of-the-art Transformer variants for various speech applications, including ASR, text-to-speech, spoken language understanding, and speech summarization. Experimental evaluations revealed that Mamba achieves comparable or better performance than Transformer-based models, and demonstrated its efficiency in long-form speech processing.

</details>

### [Blending LLMs into Cascaded Speech Translation: KIT's Offline Speech Translation System for IWSLT 2024](2406.16777.md)
**Sai Koneru, Thai-Binh Nguyen, Ngoc-Quan Pham, Danni Liu et al.** · 2024-06-24

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are currently under exploration for various tasks, including Automatic Speech Recognition (ASR), Machine Translation (MT), and even End-to-End Speech Translation (ST). In this paper, we present KIT's offline submission in the constrained + LLM track by incorporating recently proposed techniques that can be added to any cascaded speech translation. Specifically, we integrate Mistral-7B\footnote{mistralai/Mistral-7B-Instruct-v0.1} into our system to enhance it in two ways. Firstly, we refine the ASR outputs by utilizing the N-best lists generated by our system and fine-tuning the LLM to predict the transcript accurately. Secondly, we refine the MT outputs at the document level by fine-tuning the LLM, leveraging both ASR and MT predictions to improve translation quality. We find that integrating the LLM into the ASR and MT systems results in an absolute improvement of $0.3\%$ in Word Error Rate and $0.65\%$ in COMET for tst2019 test set. In challenging test sets with overlapping speakers and background noise, we find that integrating LLM is not beneficial due to poor ASR performance. Here, we use ASR with chunked long-form decoding to improve context usage that may be unavailable when transcribing with Voice Activity Detection segmentation alone.

</details>

### [Contextualized End-to-end Automatic Speech Recognition with Intermediate Biasing Loss](2406.16120.md)
**Muhammad Shakeel, Yui Sudo, Yifan Peng, Shinji Watanabe** · 2024-06-23

<details>
<summary>Abstract</summary>

Contextualized end-to-end automatic speech recognition has been an active research area, with recent efforts focusing on the implicit learning of contextual phrases based on the final loss objective. However, these approaches ignore the useful contextual knowledge encoded in the intermediate layers. We hypothesize that employing explicit biasing loss as an auxiliary task in the encoder intermediate layers may better align text tokens or audio frames with the desired objectives. Our proposed intermediate biasing loss brings more regularization and contextualization to the network. Our method outperforms a conventional contextual biasing baseline on the LibriSpeech corpus, achieving a relative improvement of 22.5% in biased word error rate (B-WER) and up to 44% compared to the non-contextual baseline with a biasing list size of 100. Moreover, employing RNN-transducer-driven joint decoding further reduces the unbiased word error rate (U-WER), resulting in a more robust network.

</details>

### [Decoder-only Architecture for Streaming End-to-end Speech Recognition](2406.16107.md)
**Emiru Tsunoo, Hayato Futami, Yosuke Kashiwagi, Siddhant Arora et al.** · 2024-06-23

<details>
<summary>Abstract</summary>

Decoder-only language models (LMs) have been successfully adopted for speech-processing tasks including automatic speech recognition (ASR). The LMs have ample expressiveness and perform efficiently. This efficiency is a suitable characteristic for streaming applications of ASR. In this work, we propose to use a decoder-only architecture for blockwise streaming ASR. In our approach, speech features are compressed using CTC output and context embedding using blockwise speech subnetwork, and are sequentially provided as prompts to the decoder. The decoder estimates the output tokens promptly at each block. To this end, we also propose a novel training scheme using random-length prefix prompts to make the model robust to the truncated prompts caused by blockwise processing. An experimental comparison shows that our proposed decoder-only streaming ASR achieves 8% relative word error rate reduction in the LibriSpeech test-other set while being twice as fast as the baseline model.

</details>

### [TacoLM: GaTed Attention Equipped Codec Language Model are Efficient Zero-Shot Text to Speech Synthesizers](2406.15752.md)
**Yakun Song, Zhuo Chen, Xiaofei Wang, Ziyang Ma et al.** · 2024-06-22

<details>
<summary>Abstract</summary>

Neural codec language model (LM) has demonstrated strong capability in zero-shot text-to-speech (TTS) synthesis. However, the codec LM often suffers from limitations in inference speed and stability, due to its auto-regressive nature and implicit alignment between text and audio. In this work, to handle these challenges, we introduce a new variant of neural codec LM, namely TacoLM. Specifically, TacoLM introduces a gated attention mechanism to improve the training and inference efficiency and reduce the model size. Meanwhile, an additional gated cross-attention layer is included for each decoder layer, which improves the efficiency and content accuracy of the synthesized speech. In the evaluation of the Librispeech corpus, the proposed TacoLM achieves a better word error rate, speaker similarity, and mean opinion score, with 90% fewer parameters and 5.2 times speed up, compared with VALL-E. Demo and code is available at https://ereboas.github.io/TacoLM/.

</details>

### [Perception of Phonological Assimilation by Neural Speech Recognition Models](2406.15265.md)
**Charlotte Pouw, Marianne de Heer Kloots, Afra Alishahi, Willem Zuidema** · 2024-06-21

<details>
<summary>Abstract</summary>

Human listeners effortlessly compensate for phonological changes during speech perception, often unconsciously inferring the intended sounds. For example, listeners infer the underlying /n/ when hearing an utterance such as "clea[m] pan", where [m] arises from place assimilation to the following labial [p]. This article explores how the neural speech recognition model Wav2Vec2 perceives assimilated sounds, and identifies the linguistic knowledge that is implemented by the model to compensate for assimilation during Automatic Speech Recognition (ASR). Using psycholinguistic stimuli, we systematically analyze how various linguistic context cues influence compensation patterns in the model's output. Complementing these behavioral experiments, our probing experiments indicate that the model shifts its interpretation of assimilated sounds from their acoustic form to their underlying form in its final layers. Finally, our causal intervention experiments suggest that the model relies on minimal phonological context cues to accomplish this shift. These findings represent a step towards better understanding the similarities and differences in phonological processing between neural ASR models and humans.

</details>

### [InterBiasing: Boost Unseen Word Recognition through Biasing Intermediate Predictions](2406.14890.md)
**Yu Nakagome, Michael Hentschel** · 2024-06-21

<details>
<summary>Abstract</summary>

Despite recent advances in end-to-end speech recognition methods, their output is biased to the training data's vocabulary, resulting in inaccurate recognition of unknown terms or proper nouns. To improve the recognition accuracy for a given set of such terms, we propose an adaptation parameter-free approach based on Self-conditioned CTC. Our method improves the recognition accuracy of misrecognized target keywords by substituting their intermediate CTC predictions with corrected labels, which are then passed on to the subsequent layers. First, we create pairs of correct labels and recognition error instances for a keyword list using Text-to-Speech and a recognition model. We use these pairs to replace intermediate prediction errors by the labels. Conditioning the subsequent layers of the encoder on the labels, it is possible to acoustically evaluate the target keywords. Experiments conducted in Japanese demonstrated that our method successfully improved the F1 score for unknown words.

</details>

### [An Adapter-Based Unified Model for Multiple Spoken Language Processing Tasks](2406.14747.md)
**Varsha Suresh, Salah Aït-Mokhtar, Caroline Brun, Ioan Calapodescu** · 2024-06-20

<details>
<summary>Abstract</summary>

Self-supervised learning models have revolutionized the field of speech processing. However, the process of fine-tuning these models on downstream tasks requires substantial computational resources, particularly when dealing with multiple speech-processing tasks. In this paper, we explore the potential of adapter-based fine-tuning in developing a unified model capable of effectively handling multiple spoken language processing tasks. The tasks we investigate are Automatic Speech Recognition, Phoneme Recognition, Intent Classification, Slot Filling, and Spoken Emotion Recognition. We validate our approach through a series of experiments on the SUPERB benchmark, and our results indicate that adapter-based fine-tuning enables a single encoder-decoder model to perform multiple speech processing tasks with an average improvement of 18.4% across the five target tasks while staying efficient in terms of parameter updates.

</details>

### [Intelligent Interface: Enhancing Lecture Engagement with Didactic Activity Summaries](2406.14266.md)
**Anna Wróblewska, Marcel Witas, Kinga Frańczak, Arkadiusz Kniaź et al.** · 2024-06-20

<details>
<summary>Abstract</summary>

Recently, multiple applications of machine learning have been introduced. They include various possibilities arising when image analysis methods are applied to, broadly understood, video streams. In this context, a novel tool, developed for academic educators to enhance the teaching process by automating, summarizing, and offering prompt feedback on conducting lectures, has been developed. The implemented prototype utilizes machine learning-based techniques to recognise selected didactic and behavioural teachers' features within lecture video recordings. Specifically, users (teachers) can upload their lecture videos, which are preprocessed and analysed using machine learning models. Next, users can view summaries of recognized didactic features through interactive charts and tables. Additionally, stored ML-based prediction results support comparisons between lectures based on their didactic content. In the developed application text-based models trained on lecture transcriptions, with enhancements to the transcription quality, by adopting an automatic speech recognition solution are applied. Furthermore, the system offers flexibility for (future) integration of new/additional machine-learning models and software modules for image and video analysis.

</details>

### [SimulSeamless: FBK at IWSLT 2024 Simultaneous Speech Translation](2406.14177.md)
**Sara Papi, Marco Gaido, Matteo Negri, Luisa Bentivogli** · 2024-06-20

<details>
<summary>Abstract</summary>

This paper describes the FBK's participation in the Simultaneous Translation Evaluation Campaign at IWSLT 2024. For this year's submission in the speech-to-text translation (ST) sub-track, we propose SimulSeamless, which is realized by combining AlignAtt and SeamlessM4T in its medium configuration. The SeamlessM4T model is used "off-the-shelf" and its simultaneous inference is enabled through the adoption of AlignAtt, a SimulST policy based on cross-attention that can be applied without any retraining or adaptation of the underlying model for the simultaneous task. We participated in all the Shared Task languages (English->{German, Japanese, Chinese}, and Czech->English), achieving acceptable or even better results compared to last year's submissions. SimulSeamless, covering more than 143 source languages and 200 target languages, is released at: https://github.com/hlt-mt/FBK-fairseq/.

</details>

### [Joint vs Sequential Speaker-Role Detection and Automatic Speech Recognition for Air-traffic Control](2406.13842.md)
**Alexander Blatt, Aravind Krishnan, Dietrich Klakow** · 2024-06-19

<details>
<summary>Abstract</summary>

Utilizing air-traffic control (ATC) data for downstream natural-language processing tasks requires preprocessing steps. Key steps are the transcription of the data via automatic speech recognition (ASR) and speaker diarization, respectively speaker role detection (SRD) to divide the transcripts into pilot and air-traffic controller (ATCO) transcripts. While traditional approaches take on these tasks separately, we propose a transformer-based joint ASR-SRD system that solves both tasks jointly while relying on a standard ASR architecture. We compare this joint system against two cascaded approaches for ASR and SRD on multiple ATC datasets. Our study shows in which cases our joint system can outperform the two traditional approaches and in which cases the other architectures are preferable. We additionally evaluate how acoustic and lexical differences influence all architectures and show how to overcome them for our joint architecture.

</details>

### [Transferable speech-to-text large language model alignment module](2406.13357.md)
**Boyong Wu, Chao Yan, Haoran Pu** · 2024-06-19

<details>
<summary>Abstract</summary>

By leveraging the power of Large Language Models(LLMs) and speech foundation models, state of the art speech-text bimodal works can achieve challenging tasks like spoken translation(ST) and question answering(SQA) altogether with much simpler architectures. In this paper, we utilize the capability of Whisper encoder and pre-trained Yi-6B. Empirical results reveal that modal alignment can be achieved with one layer module and hundred hours of speech-text multitask corpus. We further swap the Yi-6B with human preferences aligned version of Yi-6B-Chat during inference, and discover that the alignment capability is applicable as well. In addition, the alignment subspace revealed by singular value decomposition(SVD) also implies linear alignment subspace is sparse, which leaves the possibility to concatenate other features like voice-print or video to expand modality.

</details>

### [Bridging the Gap: Integrating Pre-trained Speech Enhancement and Recognition Models for Robust Speech Recognition](2406.12699.md)
**Kuan-Chen Wang, You-Jin Li, Wei-Lun Chen, Yu-Wen Chen et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

Noise robustness is critical when applying automatic speech recognition (ASR) in real-world scenarios. One solution involves the used of speech enhancement (SE) models as the front end of ASR. However, neural network-based (NN-based) SE often introduces artifacts into the enhanced signals and harms ASR performance, particularly when SE and ASR are independently trained. Therefore, this study introduces a simple yet effective SE post-processing technique to address the gap between various pre-trained SE and ASR models. A bridge module, which is a lightweight NN, is proposed to evaluate the signal-level information of the speech signal. Subsequently, using the signal-level information, the observation addition technique is applied to effectively reduce the shortcomings of SE. The experimental results demonstrate the success of our method in integrating diverse pre-trained SE and ASR models, considerably boosting the ASR robustness. Crucially, no prior knowledge of the ASR or speech contents is required during the training or inference stages. Moreover, the effectiveness of this approach extends to different datasets without necessitating the fine-tuning of the bridge module, ensuring efficiency and improved generalization.

</details>

### [Growing Trees on Sounds: Assessing Strategies for End-to-End Dependency Parsing of Speech](2406.12621.md)
**Adrien Pupier, Maximin Coavoux, Jérôme Goulian, Benjamin Lecouteux** · 2024-06-18

<details>
<summary>Abstract</summary>

Direct dependency parsing of the speech signal -- as opposed to parsing speech transcriptions -- has recently been proposed as a task (Pupier et al. 2022), as a way of incorporating prosodic information in the parsing system and bypassing the limitations of a pipeline approach that would consist of using first an Automatic Speech Recognition (ASR) system and then a syntactic parser. In this article, we report on a set of experiments aiming at assessing the performance of two parsing paradigms (graph-based parsing and sequence labeling based parsing) on speech parsing. We perform this evaluation on a large treebank of spoken French, featuring realistic spontaneous conversations. Our findings show that (i) the graph based approach obtain better results across the board (ii) parsing directly from speech outperforms a pipeline approach, despite having 30% fewer parameters.

</details>

### [Rapid Language Adaptation for Multilingual E2E Speech Recognition Using Encoder Prompting](2406.12611.md)
**Yosuke Kashiwagi, Hayato Futami, Emiru Tsunoo, Siddhant Arora et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

End-to-end multilingual speech recognition models handle multiple languages through a single model, often incorporating language identification to automatically detect the language of incoming speech. Since the common scenario is where the language is already known, these models can perform as language-specific by using language information as prompts, which is particularly beneficial for attention-based encoder-decoder architectures. However, the Connectionist Temporal Classification (CTC) approach, which enhances recognition via joint decoding and multi-task training, does not normally incorporate language prompts due to its conditionally independent output tokens. To overcome this, we introduce an encoder prompting technique within the self-conditioned CTC framework, enabling language-specific adaptation of the CTC model in a zero-shot manner. Our method has shown to significantly reduce errors by 28% on average and by 41% on low-resource languages.

</details>

### [Performant ASR Models for Medical Entities in Accented Speech](2406.12387.md)
**Tejumade Afonja, Tobi Olatunji, Sewade Ogun, Naome A. Etori et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

Recent strides in automatic speech recognition (ASR) have accelerated their application in the medical domain where their performance on accented medical named entities (NE) such as drug names, diagnoses, and lab results, is largely unknown. We rigorously evaluate multiple ASR models on a clinical English dataset of 93 African accents. Our analysis reveals that despite some models achieving low overall word error rates (WER), errors in clinical entities are higher, potentially posing substantial risks to patient safety. To empirically demonstrate this, we extract clinical entities from transcripts, develop a novel algorithm to align ASR predictions with these entities, and compute medical NE Recall, medical WER, and character error rate. Our results show that fine-tuning on accented clinical speech improves medical WER by a wide margin (25-34 % relative), improving their practical applicability in healthcare environments.

</details>

### [Finding Task-specific Subnetworks in Multi-task Spoken Language Understanding Model](2406.12317.md)
**Hayato Futami, Siddhant Arora, Yosuke Kashiwagi, Emiru Tsunoo et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

Recently, multi-task spoken language understanding (SLU) models have emerged, designed to address various speech processing tasks. However, these models often rely on a large number of parameters. Also, they often encounter difficulties in adapting to new data for a specific task without experiencing catastrophic forgetting of previously trained tasks. In this study, we propose finding task-specific subnetworks within a multi-task SLU model via neural network pruning. In addition to model compression, we expect that the forgetting of previously trained tasks can be mitigated by updating only a task-specific subnetwork. We conduct experiments on top of the state-of-the-art multi-task SLU model ``UniverSLU'', trained for several tasks such as emotion recognition (ER), intent classification (IC), and automatic speech recognition (ASR). We show that pruned models were successful in adapting to additional ASR or IC data with minimal performance degradation on previously trained tasks.

</details>

### [SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization](2406.12233.md)
**Young Jin Ahn, Jungwoo Park, Sangha Park, Jonghyun Choi et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) stands at the intersection of computer vision and speech recognition, aiming to interpret spoken content from visual cues. A prominent challenge in VSR is the presence of homophenes-visually similar lip gestures that represent different phonemes. Prior approaches have sought to distinguish fine-grained visemes by aligning visual and auditory semantics, but often fell short of full synchronization. To address this, we present SyncVSR, an end-to-end learning framework that leverages quantized audio for frame-level crossmodal supervision. By integrating a projection layer that synchronizes visual representation with acoustic data, our encoder learns to generate discrete audio tokens from a video sequence in a non-autoregressive manner. SyncVSR shows versatility across tasks, languages, and modalities at the cost of a forward pass. Our empirical evaluations show that it not only achieves state-of-the-art results but also reduces data usage by up to ninefold.

</details>

### [Continual Test-time Adaptation for End-to-end Speech Recognition on Noisy Speech](2406.11064.md)
**Guan-Ting Lin, Wei-Ping Huang, Hung-yi Lee** · 2024-06-16

<details>
<summary>Abstract</summary>

Deep Learning-based end-to-end Automatic Speech Recognition (ASR) has made significant strides but still struggles with performance on out-of-domain samples due to domain shifts in real-world scenarios. Test-Time Adaptation (TTA) methods address this issue by adapting models using test samples at inference time. However, current ASR TTA methods have largely focused on non-continual TTA, which limits cross-sample knowledge learning compared to continual TTA. In this work, we first propose a Fast-slow TTA framework for ASR that leverages the advantage of continual and non-continual TTA. Following this framework, we introduce Dynamic SUTA (DSUTA), an entropy-minimization-based continual TTA method for ASR. To enhance DSUTA robustness for time-varying data, we design a dynamic reset strategy to automatically detect domain shifts and reset the model, making it more effective at handling multi-domain data. Our method demonstrates superior performance on various noisy ASR datasets, outperforming both non-continual and continual TTA baselines while maintaining robustness to domain changes without requiring domain boundary information.

</details>

### [NAST: Noise Aware Speech Tokenization for Speech Language Models](2406.11037.md)
**Shoval Messica, Yossi Adi** · 2024-06-16

<details>
<summary>Abstract</summary>

Speech tokenization is the task of representing speech signals as a sequence of discrete units. Such representations can be later used for various downstream tasks including automatic speech recognition, text-to-speech, etc. More relevant to this study, such representation serves as the basis of Speech Language Models. In this work, we tackle the task of speech tokenization under the noisy setup and present NAST: Noise Aware Speech Tokenization for Speech Language Models. NAST is composed of three main components: (i) a predictor; (ii) a residual encoder; and (iii) a decoder. We evaluate the efficiency of NAST considering several spoken language modeling tasks and show that NAST is superior to the evaluated baselines across all setups. Lastly, we analyze NAST and show its disentanglement properties and robustness to signal variations in the form of noise, reverberation, pitch-shift, and time-stretch. Code and pre-trained models are available at https://github.com/ShovalMessica/NAST.

</details>

### [Large Language Models for Dysfluency Detection in Stuttered Speech](2406.11025.md)
**Dominik Wagner, Sebastian P. Bayerl, Ilja Baumann, Korbinian Riedhammer et al.** · 2024-06-16

<details>
<summary>Abstract</summary>

Accurately detecting dysfluencies in spoken language can help to improve the performance of automatic speech and language processing components and support the development of more inclusive speech and language technologies. Inspired by the recent trend towards the deployment of large language models (LLMs) as universal learners and processors of non-lexical inputs, such as audio and video, we approach the task of multi-label dysfluency detection as a language modeling problem. We present hypotheses candidates generated with an automatic speech recognition system and acoustic representations extracted from an audio encoder model to an LLM, and finetune the system to predict dysfluency labels on three datasets containing English and German stuttered speech. The experimental results show that our system effectively combines acoustic and lexical information and achieves competitive results on the multi-label stuttering detection task.

</details>

### [Outlier Reduction with Gated Attention for Improved Post-training Quantization in Large Sequence-to-sequence Speech Foundation Models](2406.11022.md)
**Dominik Wagner, Ilja Baumann, Korbinian Riedhammer, Tobias Bocklet** · 2024-06-16

<details>
<summary>Abstract</summary>

This paper explores the improvement of post-training quantization (PTQ) after knowledge distillation in the Whisper speech foundation model family. We address the challenge of outliers in weights and activation tensors, known to impede quantization quality in transformer-based language and vision models. Extending this observation to Whisper, we demonstrate that these outliers are also present when transformer-based models are trained to perform automatic speech recognition, necessitating mitigation strategies for PTQ. We show that outliers can be reduced by a recently proposed gating mechanism in the attention blocks of the student model, enabling effective 8-bit quantization, and lower word error rates compared to student models without the gating mechanism in place.

</details>

### [CoSTA: Code-Switched Speech Translation using Aligned Speech-Text Interleaving](2406.10993.md)
**Bhavani Shankar, Preethi Jyothi, Pushpak Bhattacharyya** · 2024-06-16

<details>
<summary>Abstract</summary>

Code-switching is a widely prevalent linguistic phenomenon in multilingual societies like India. Building speech-to-text models for code-switched speech is challenging due to limited availability of datasets. In this work, we focus on the problem of spoken translation (ST) of code-switched speech in Indian languages to English text. We present a new end-to-end model architecture COSTA that scaffolds on pretrained automatic speech recognition (ASR) and machine translation (MT) modules (that are more widely available for many languages). Speech and ASR text representations are fused using an aligned interleaving scheme and are fed further as input to a pretrained MT module; the whole pipeline is then trained end-to-end for spoken translation using synthetically created ST data. We also release a new evaluation benchmark for code-switched Bengali-English, Hindi-English, Marathi-English and Telugu- English speech to English text. COSTA significantly outperforms many competitive cascaded and end-to-end multimodal baselines by up to 3.5 BLEU points.

</details>

### [Trading Devil: Robust backdoor attack via Stochastic investment models and Bayesian approach](2406.10719.md)
**Orson Mengara** · 2024-06-15

<details>
<summary>Abstract</summary>

With the growing use of voice-activated systems and speech recognition technologies, the danger of backdoor attacks on audio data has grown significantly. This research looks at a specific type of attack, known as a Stochastic investment-based backdoor attack (MarketBack), in which adversaries strategically manipulate the stylistic properties of audio to fool speech recognition systems. The security and integrity of machine learning models are seriously threatened by backdoor attacks, in order to maintain the reliability of audio applications and systems, the identification of such attacks becomes crucial in the context of audio data. Experimental results demonstrated that MarketBack is feasible to achieve an average attack success rate close to 100% in seven victim models when poisoning less than 1% of the training data.

</details>

### [SOA: Reducing Domain Mismatch in SSL Pipeline by Speech Only Adaptation for Low Resource ASR](2406.10512.md)
**Natarajan Balaji Shankar, Ruchao Fan, Abeer Alwan** · 2024-06-15

<details>
<summary>Abstract</summary>

Recently, speech foundation models have gained popularity due to their superiority in finetuning downstream ASR tasks. However, models finetuned on certain domains, such as LibriSpeech (adult read speech), behave poorly on other domains (child or noisy speech). One solution could be collecting as much labeled and diverse data as possible for joint finetuning on various domains. However, collecting target domain speech-text paired data and retraining the model is often costly and computationally expensive. In this paper, we introduce a simple yet effective method, speech only adaptation (SOA), based on speech foundation models (Wav2vec 2.0), which requires only speech input data from the target domain. Specifically, the Wav2vec 2.0 feature encoder is continually pretrained with the Wav2vec 2.0 loss on both the source and target domain data for domain adaptation, while the contextual encoder is frozen. Compared to a source domain finetuned model with the feature encoder being frozen during training, we find that replacing the frozen feature encoder with the adapted one provides significant WER improvements to the target domain while preserving the performance of the source domain. The effectiveness of SOA is examined on various low resource or domain mismatched ASR settings, including adult-child and clean-noisy speech.

</details>

### [Benchmarking Children's ASR with Supervised and Self-supervised Speech Foundation Models](2406.10507.md)
**Ruchao Fan, Natarajan Balaji Shankar, Abeer Alwan** · 2024-06-15

<details>
<summary>Abstract</summary>

Speech foundation models (SFMs) have achieved state-of-the-art results for various speech tasks in supervised (e.g. Whisper) or self-supervised systems (e.g. WavLM). However, the performance of SFMs for child ASR has not been systematically studied. In addition, there is no benchmark for child ASR with standard evaluations, making the comparisons of novel ideas difficult. In this paper, we initiate and present a comprehensive benchmark on several child speech databases based on various SFMs (Whisper, Wav2vec2.0, HuBERT, and WavLM). Moreover, we investigate finetuning strategies by comparing various data augmentation and parameter-efficient finetuning (PEFT) methods. We observe that the behaviors of these methods are different when the model size increases. For example, PEFT matches the performance of full finetuning for large models but worse for small models. To stabilize finetuning using augmented data, we propose a perturbation invariant finetuning (PIF) loss as a regularization.

</details>

### [Multilingual end-to-end ASR for low-resource Turkic languages with common alphabets](s2:ab4b8fe73044fc944defef6dbdeb0465074429dd.md)
**A. Bekarystankyzy, Orken J. Mamyrbayev, Mateus Mendes, A. Fazylzhanova et al.** · 2024-06-15

<details>
<summary>Abstract</summary>

To obtain a reliable and accurate automatic speech recognition (ASR) machine learning model, it is necessary to have sufficient audio data transcribed, for training. Many languages in the world, especially the agglutinative languages of the Turkic family, suffer from a lack of this type of data. Many studies have been conducted in order to obtain better models for low-resource languages, using different approaches. The most popular approaches include multilingual training and transfer learning. In this study, we combined five agglutinative languages from the Turkic family—Kazakh, Bashkir, Kyrgyz, Sakha, and Tatar,—in order to provide multilingual training using connectionist temporal classification and an attention mechanism including a language model, because these languages have cognate words, sentence formation rules, and alphabet (Cyrillic). Data from the open-source database Common voice was used for the study, to make the experiments reproducible. The results of the experiments showed that multilingual training could improve ASR performances for all languages included in the experiment, except Bashkir language. A dramatic result was achieved for the Kyrgyz language: word error rate decreased to nearly one-fifth and character error rate decreased to one-fourth, which proves that this approach can be helpful for critically low-resource languages.

</details>

### [Inclusive ASR for Disfluent Speech: Cascaded Large-Scale Self-Supervised Learning with Targeted Fine-Tuning and Data Augmentation](2406.10177.md)
**Dena Mujtaba, Nihar R. Mahapatra, Megan Arney, J. Scott Yaruss et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems often falter while processing stuttering-related disfluencies -- such as involuntary blocks and word repetitions -- yielding inaccurate transcripts. A critical barrier to progress is the scarcity of large, annotated disfluent speech datasets. Therefore, we present an inclusive ASR design approach, leveraging large-scale self-supervised learning on standard speech followed by targeted fine-tuning and data augmentation on a smaller, curated dataset of disfluent speech. Our data augmentation technique enriches training datasets with various disfluencies, enhancing ASR processing of these speech patterns. Results show that fine-tuning wav2vec 2.0 with even a relatively small, labeled dataset, alongside data augmentation, can significantly reduce word error rates for disfluent speech. Our approach not only advances ASR inclusivity for people who stutter, but also paves the way for ASRs that can accommodate wider speech variations.

</details>

### [On the Evaluation of Speech Foundation Models for Spoken Language Understanding](2406.10083.md)
**Siddhant Arora, Ankita Pasad, Chung-Ming Chien, Jionghao Han et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

The Spoken Language Understanding Evaluation (SLUE) suite of benchmark tasks was recently introduced to address the need for open resources and benchmarking of complex spoken language understanding (SLU) tasks, including both classification and sequence generation tasks, on natural speech. The benchmark has demonstrated preliminary success in using pre-trained speech foundation models (SFM) for these SLU tasks. However, the community still lacks a fine-grained understanding of the comparative utility of different SFMs. Inspired by this, we ask: which SFMs offer the most benefits for these complex SLU tasks, and what is the most effective approach for incorporating these SFMs? To answer this, we perform an extensive evaluation of multiple supervised and self-supervised SFMs using several evaluation protocols: (i) frozen SFMs with a lightweight prediction head, (ii) frozen SFMs with a complex prediction head, and (iii) fine-tuned SFMs with a lightweight prediction head. Although the supervised SFMs are pre-trained on much more speech recognition data (with labels), they do not always outperform self-supervised SFMs; the latter tend to perform at least as well as, and sometimes better than, supervised SFMs, especially on the sequence generation tasks in SLUE. While there is no universally optimal way of incorporating SFMs, the complex prediction head gives the best performance for most tasks, although it increases the inference time. We also introduce an open-source toolkit and performance leaderboard, SLUE-PERB, for these tasks and modeling strategies.

</details>

### [Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation](2406.10082.md)
**Andrew Rouditchenko, Yuan Gong, Samuel Thomas, Leonid Karlinsky et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) uses lip-based video to improve performance in noise. Since videos are harder to obtain than audio, the video training data of AVSR models is usually limited to a few thousand hours. In contrast, speech models such as Whisper are trained with hundreds of thousands of hours of data, and thus learn a better speech-to-text decoder. The huge training data difference motivates us to adapt Whisper to handle video inputs. Inspired by Flamingo which injects visual features into language models, we propose Whisper-Flamingo which integrates visual features into the Whisper speech recognition and translation model with gated cross attention. Our models achieve state-of-the-art ASR WER (0.68%) and AVSR WER (0.76%) on LRS3, and state-of-the-art ASR WER (1.3%) and AVSR WER (1.4%) on LRS2. Audio-visual Whisper-Flamingo outperforms audio-only Whisper on English speech recognition and En-X translation for 6 languages in noisy conditions. Moreover, Whisper-Flamingo is versatile and conducts all of these tasks using one set of parameters, while prior methods are trained separately on each language.

</details>

### [Simul-Whisper: Attention-Guided Streaming Whisper with Truncation Detection](2406.10052.md)
**Haoyu Wang, Guoqiang Hu, Guodong Lin, Wei-Qiang Zhang et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

As a robust and large-scale multilingual speech recognition model, Whisper has demonstrated impressive results in many low-resource and out-of-distribution scenarios. However, its encoder-decoder structure hinders its application to streaming speech recognition. In this paper, we introduce Simul-Whisper, which uses the time alignment embedded in Whisper's cross-attention to guide auto-regressive decoding and achieve chunk-based streaming ASR without any fine-tuning of the pre-trained model. Furthermore, we observe the negative effect of the truncated words at the chunk boundaries on the decoding results and propose an integrate-and-fire-based truncation detection model to address this issue. Experiments on multiple languages and Whisper architectures show that Simul-Whisper achieves an average absolute word error rate degradation of only 1.46% at a chunk size of 1 second, which significantly outperforms the current state-of-the-art baseline.

</details>

### [MMM: Multi-Layer Multi-Residual Multi-Stream Discrete Speech Representation from Self-supervised Learning Model](2406.09869.md)
**Jiatong Shi, Xutai Ma, Hirofumi Inaguma, Anna Sun et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

Speech discrete representation has proven effective in various downstream applications due to its superior compression rate of the waveform, fast convergence during training, and compatibility with other modalities. Discrete units extracted from self-supervised learning (SSL) models have emerged as a prominent approach for obtaining speech discrete representation. However, while discrete units have shown effectiveness compared to spectral features, they still lag behind continuous SSL representations. In this work, we propose MMM, a multi-layer multi-residual multi-stream discrete units extraction method from SSL. Specifically, we introduce iterative residual vector quantization with K-means for different layers in an SSL model to extract multi-stream speech discrete representation. Through extensive experiments in speech recognition, speech resynthesis, and text-to-speech, we demonstrate the proposed MMM can surpass or on-par with neural codec's performance under various conditions.

</details>

### [Optimizing Byte-level Representation for End-to-end ASR](2406.09676.md)
**Roger Hsiao, Liuhui Deng, Erik McDermott, Ruchir Travadi et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

We propose a novel approach to optimizing a byte-level representation for end-to-end automatic speech recognition (ASR). Byte-level representation is often used by large scale multilingual ASR systems when the character set of the supported languages is large. The compactness and universality of byte-level representation allow the ASR models to use smaller output vocabularies and therefore, provide more flexibility. UTF-8 is a commonly used byte-level representation for multilingual ASR, but it is not designed to optimize machine learning tasks directly. By using auto-encoder and vector quantization, we show that we can optimize a byte-level representation for ASR and achieve better accuracy. Our proposed framework can incorporate information from different modalities, and provides an error correction mechanism. In an English/Mandarin dictation task, we show that a bilingual ASR model built with this approach can outperform UTF-8 representation by 5% relative in error rate.

</details>

### [Learning Language Structures through Grounding](2406.09662.md)
**Freda Shi** · 2024-06-14

<details>
<summary>Abstract</summary>

Language is highly structured, with syntactic and semantic structures, to some extent, agreed upon by speakers of the same language. With implicit or explicit awareness of such structures, humans can learn and use language efficiently and generalize to sentences that contain unseen words. Motivated by human language learning, in this dissertation, we consider a family of machine learning tasks that aim to learn language structures through grounding. We seek distant supervision from other data sources (i.e., grounds), including but not limited to other modalities (e.g., vision), execution results of programs, and other languages. We demonstrate the potential of this task formulation and advocate for its adoption through three schemes. In Part I, we consider learning syntactic parses through visual grounding. We propose the task of visually grounded grammar induction, present the first models to induce syntactic structures from visually grounded text and speech, and find that the visual grounding signals can help improve the parsing quality over language-only models. As a side contribution, we propose a novel evaluation metric that enables the evaluation of speech parsing without text or automatic speech recognition systems involved. In Part II, we propose two execution-aware methods to map sentences into corresponding semantic structures (i.e., programs), significantly improving compositional generalization and few-shot program synthesis. In Part III, we propose methods that learn language structures from annotations in other languages. Specifically, we propose a method that sets a new state of the art on cross-lingual word alignment. We then leverage the learned word alignments to improve the performance of zero-shot cross-lingual dependency parsing, by proposing a novel substructure-based projection method that preserves structural knowledge learned from the source language.

</details>

### [The BabyView dataset: High-resolution egocentric videos of infants' and young children's everyday experiences](2406.10447.md)
**Bria Long, Robert Z. Sparks, Violet Xiang, Stefan Stojanov et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

Human children far exceed modern machine learning algorithms in their sample efficiency, achieving high performance in key domains with much less data than current models. This ''data gap'' is a key challenge both for building intelligent artificial systems and for understanding human development. Egocentric video capturing children's experience--their ''training data''--is a key ingredient for comparison of humans and models and for the development of algorithmic innovations to bridge this gap. Yet there are few such datasets available, and extant data are low-resolution, have limited metadata, and importantly, represent only a small set of children's experiences. Here, we provide the first release of a large developmental egocentric video dataset--the BabyView dataset--recorded using a high-resolution camera with a large vertical field-of-view and gyroscope/accelerometer data. This 868 hour dataset includes egocentric videos from children spanning 6 months to 3 years of age in longitudinal, at-home contexts. We provide gold-standard annotations for the evaluation of speech transcription, speaker diarization, and human pose estimation, and evaluate models in each of these domains. We train self-supervised language and vision models and evaluate their transfer to out-of-distribution tasks, including syntactic structure learning, object recognition, depth estimation, and image segmentation. Although performance in each domain scales with dataset size, overall performance is relatively lower than when models are trained on curated datasets, especially in the visual domain. Our dataset stands as an open challenge for robust, human-like AI systems: how can such systems achieve human-levels of success on the same scale and distribution of training data as humans?

</details>

### [One-pass Multiple Conformer and Foundation Speech Systems Compression and Quantization Using An All-in-one Neural Model](2406.10160.md)
**Zhaoqing Li, Haoning Xu, Tianzi Wang, Shoukang Hu et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

We propose a novel one-pass multiple ASR systems joint compression and quantization approach using an all-in-one neural model. A single compression cycle allows multiple nested systems with varying Encoder depths, widths, and quantization precision settings to be simultaneously constructed without the need to train and store individual target systems separately. Experiments consistently demonstrate the multiple ASR systems compressed in a single all-in-one model produced a word error rate (WER) comparable to, or lower by up to 1.01\% absolute (6.98\% relative) than individually trained systems of equal complexity. A 3.4x overall system compression and training time speed-up was achieved. Maximum model size compression ratios of 12.8x and 3.93x were obtained over the baseline Switchboard-300hr Conformer and LibriSpeech-100hr fine-tuned wav2vec2.0 models, respectively, incurring no statistically significant WER increase.

</details>

### [Towards Effective and Efficient Non-autoregressive Decoding Using Block-based Attention Mask](2406.10034.md)
**Tianzi Wang, Xurong Xie, Zhaoqing Li, Shoukang Hu et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

This paper proposes a novel non-autoregressive (NAR) block-based Attention Mask Decoder (AMD) that flexibly balances performance-efficiency trade-offs for Conformer ASR systems. AMD performs parallel NAR inference within contiguous blocks of output labels that are concealed using attention masks, while conducting left-to-right AR prediction and history context amalgamation between blocks. A beam search algorithm is designed to leverage a dynamic fusion of CTC, AR Decoder, and AMD probabilities. Experiments on the LibriSpeech-100hr corpus suggest the tripartite Decoder incorporating the AMD module produces a maximum decoding speed-up ratio of 1.73x over the baseline CTC+AR decoding, while incurring no statistically significant word error rate (WER) increase on the test sets. When operating with the same decoding real time factors, statistically significant WER reductions of up to 0.7% and 0.3% absolute (5.3% and 6.1% relative) were obtained over the CTC+AR baseline.

</details>

### [Multi-Modal Retrieval For Large Language Model Based Speech Recognition](2406.09618.md)
**Jari Kolehmainen, Aditya Gourav, Prashanth Gurunath Shivakumar, Yile Gu et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

Retrieval is a widely adopted approach for improving language models leveraging external information. As the field moves towards multi-modal large language models, it is important to extend the pure text based methods to incorporate other modalities in retrieval as well for applications across the wide spectrum of machine learning tasks and data types. In this work, we propose multi-modal retrieval with two approaches: kNN-LM and cross-attention techniques. We demonstrate the effectiveness of our retrieval approaches empirically by applying them to automatic speech recognition tasks with access to external information. Under this setting, we show that speech-based multi-modal retrieval outperforms text based retrieval, and yields up to 50 % improvement in word error rate over the multi-modal language model baseline. Furthermore, we achieve state-of-the-art recognition results on the Spoken-Squad question answering dataset.

</details>

### [Speech ReaLLM -- Real-time Streaming Speech Recognition with Multimodal LLMs by Teaching the Flow of Time](2406.09569.md)
**Frank Seide, Morrie Doulaty, Yangyang Shi, Yashesh Gaur et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

We introduce Speech ReaLLM, a new ASR architecture that marries "decoder-only" ASR with the RNN-T to make multimodal LLM architectures capable of real-time streaming. This is the first "decoder-only" ASR architecture designed to handle continuous audio without explicit end-pointing. Speech ReaLLM is a special case of the more general ReaLLM ("real-time LLM") approach, also introduced here for the first time. The idea is inspired by RNN-T: Instead of generating a response only at the end of a user prompt, generate after every input token received in real time (it is often empty). On Librispeech "test", an 80M Speech ReaLLM achieves WERs of 3.0% and 7.4% in real time (without an external LM or auxiliary loss). This is only slightly above a 3x larger Attention-Encoder-Decoder baseline. We also show that this way, an LLM architecture can learn to represent and reproduce the flow of time; and that a pre-trained 7B LLM can be fine-tuned to do reasonably well on this task.

</details>

### [Language Complexity and Speech Recognition Accuracy: Orthographic Complexity Hurts, Phonological Complexity Doesn't](2406.09202.md)
**Chihiro Taguchi, David Chiang** · 2024-06-13

<details>
<summary>Abstract</summary>

We investigate what linguistic factors affect the performance of Automatic Speech Recognition (ASR) models. We hypothesize that orthographic and phonological complexities both degrade accuracy. To examine this, we fine-tune the multilingual self-supervised pretrained model Wav2Vec2-XLSR-53 on 25 languages with 15 writing systems, and we compare their ASR accuracy, number of graphemes, unigram grapheme entropy, logographicity (how much word/morpheme-level information is encoded in the writing system), and number of phonemes. The results demonstrate that orthographic complexities significantly correlate with low ASR accuracy, while phonological complexity shows no significant correlation.

</details>

### [LASER: Learning by Aligning Self-supervised Representations of Speech for Improving Content-related Tasks](2406.09153.md)
**Amit Meghanani, Thomas Hain** · 2024-06-13

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL)-based speech models are extensively used for full-stack speech processing. However, it has been observed that improving SSL-based speech representations using unlabeled speech for content-related tasks is challenging and computationally expensive. Recent attempts have been made to address this issue with cost-effective self-supervised fine-tuning (SSFT) approaches. Continuing in this direction, a cost-effective SSFT method named "LASER: Learning by Aligning Self-supervised Representations" is presented. LASER is based on the soft-DTW alignment loss with temporal regularisation term. Experiments are conducted with HuBERT and WavLM models and evaluated on the SUPERB benchmark for two content-related tasks: automatic speech recognition (ASR) and phoneme recognition (PR). A relative improvement of 3.7% and 8.2% for HuBERT, and 4.1% and 11.7% for WavLM are observed, for the ASR and PR tasks respectively, with only < 3 hours of fine-tuning on a single GPU.

</details>

### [Transcription-Free Fine-Tuning of Speech Separation Models for Noisy and Reverberant Multi-Speaker Automatic Speech Recognition](2406.08914.md)
**William Ravenscroft, George Close, Stefan Goetze, Thomas Hain et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

One solution to automatic speech recognition (ASR) of overlapping speakers is to separate speech and then perform ASR on the separated signals. Commonly, the separator produces artefacts which often degrade ASR performance. Addressing this issue typically requires reference transcriptions to jointly train the separation and ASR networks. This is often not viable for training on real-world in-domain audio where reference transcript information is not always available. This paper proposes a transcription-free method for joint training using only audio signals. The proposed method uses embedding differences of pre-trained ASR encoders as a loss with a proposed modification to permutation invariant training (PIT) called guided PIT (GPIT). The method achieves a 6.4% improvement in word error rate (WER) measures over a signal-level loss and also shows enhancement improvements in perceptual measures such as short-time objective intelligibility (STOI).

</details>

### [AdaPTwin: Low-Cost Adaptive Compression of Product Twins in Transformers](2406.08904.md)
**Emil Biju, Anirudh Sriram, Mert Pilanci** · 2024-06-13

<details>
<summary>Abstract</summary>

While large transformer-based models have exhibited remarkable performance in speaker-independent speech recognition, their large size and computational requirements make them expensive or impractical to use in resource-constrained settings. In this work, we propose a low-rank adaptive compression technique called AdaPTwin that jointly compresses product-dependent pairs of weight matrices in the transformer attention layer. Our approach can prioritize the compressed model's performance on a specific speaker while maintaining generalizability to new speakers and acoustic conditions. Notably, our technique requires only 8 hours of speech data for fine-tuning, which can be accomplished in under 20 minutes, making it highly cost-effective compared to other compression methods. We demonstrate the efficacy of our approach by compressing the Whisper and Distil-Whisper models by up to 45% while incurring less than a 2% increase in word error rate.

</details>

### [EffectiveASR: A Single-Step Non-Autoregressive Mandarin Speech Recognition Architecture with High Accuracy and Inference Speed](2406.08835.md)
**Ziyang Zhuang, Chenfeng Miao, Kun Zou, Ming Fang et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) automatic speech recognition (ASR) models predict tokens independently and simultaneously, bringing high inference speed. However, there is still a gap in the accuracy of the NAR models compared to the autoregressive (AR) models. In this paper, we propose a single-step NAR ASR architecture with high accuracy and inference speed, called EffectiveASR. It uses an Index Mapping Vector (IMV) based alignment generator to generate alignments during training, and an alignment predictor to learn the alignments for inference. It can be trained end-to-end (E2E) with cross-entropy loss combined with alignment loss. The proposed EffectiveASR achieves competitive results on the AISHELL-1 and AISHELL-2 Mandarin benchmarks compared to the leading models. Specifically, it achieves character error rates (CER) of 4.26%/4.62% on the AISHELL-1 dev/test dataset, which outperforms the AR Conformer with about 30x inference speedup.

</details>

### [On the Effects of Heterogeneous Data Sources on Speech-to-Text Foundation Models](2406.09282.md)
**Jinchuan Tian, Yifan Peng, William Chen, Kwanghee Choi et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

The Open Whisper-style Speech Model (OWSM) series was introduced to achieve full transparency in building advanced speech-to-text (S2T) foundation models. To this end, OWSM models are trained on 25 public speech datasets, which are heterogeneous in multiple ways. In this study, we advance the OWSM series by introducing OWSM v3.2, which improves on prior models by investigating and addressing the impacts of this data heterogeneity. Our study begins with a detailed analysis of each dataset, from which we derive two key strategies: data filtering with proxy task to enhance data quality, and the incorporation of punctuation and true-casing using an open large language model (LLM). With all other configurations staying the same, OWSM v3.2 improves performance over the OWSM v3.1 baseline while using 15% less training data.

</details>

### [ML-SUPERB 2.0: Benchmarking Multilingual Speech Models Across Modeling Constraints, Languages, and Datasets](2406.08641.md)
**Jiatong Shi, Shih-Heng Wang, William Chen, Martijn Bartelds et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

ML-SUPERB evaluates self-supervised learning (SSL) models on the tasks of language identification and automatic speech recognition (ASR). This benchmark treats the models as feature extractors and uses a single shallow downstream model, which can be fine-tuned for a downstream task. However, real-world use cases may require different configurations. This paper presents ML-SUPERB~2.0, which is a new benchmark for evaluating pre-trained SSL and supervised speech models across downstream models, fine-tuning setups, and efficient model adaptation approaches. We find performance improvements over the setup of ML-SUPERB. However, performance depends on the downstream model design. Also, we find large performance differences between languages and datasets, suggesting the need for more targeted approaches to improve multilingual ASR performance.

</details>

### [Training Data Augmentation for Dysarthric Automatic Speech Recognition by Text-to-Dysarthric-Speech Synthesis](2406.08568.md)
**Wing-Zin Leung, Mattias Cross, Anton Ragni, Stefan Goetze** · 2024-06-12

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) research has achieved impressive performance in recent years and has significant potential for enabling access for people with dysarthria (PwD) in augmentative and alternative communication (AAC) and home environment systems. However, progress in dysarthric ASR (DASR) has been limited by high variability in dysarthric speech and limited public availability of dysarthric training data. This paper demonstrates that data augmentation using text-to-dysarthic-speech (TTDS) synthesis for finetuning large ASR models is effective for DASR. Specifically, diffusion-based text-to-speech (TTS) models can produce speech samples similar to dysarthric speech that can be used as additional training data for fine-tuning ASR foundation models, in this case Whisper. Results show improved synthesis metrics and ASR performance for the proposed multi-speaker diffusion-based TTDS data augmentation for ASR fine-tuning compared to current DASR baselines.

</details>

### [Neural Blind Source Separation and Diarization for Distant Speech Recognition](2406.08396.md)
**Yoshiaki Bando, Tomohiko Nakamura, Shinji Watanabe** · 2024-06-12

<details>
<summary>Abstract</summary>

This paper presents a neural method for distant speech recognition (DSR) that jointly separates and diarizes speech mixtures without supervision by isolated signals. A standard separation method for multi-talker DSR is a statistical multichannel method called guided source separation (GSS). While GSS does not require signal-level supervision, it relies on speaker diarization results to handle unknown numbers of active speakers. To overcome this limitation, we introduce and train a neural inference model in a weakly-supervised manner, employing the objective function of a statistical separation method. This training requires only multichannel mixtures and their temporal annotations of speaker activities. In contrast to GSS, the trained model can jointly separate and diarize speech mixtures without any auxiliary information. The experiments with the AMI corpus show that our method outperforms GSS with oracle diarization results regarding word error rates. The code is available online.

</details>

### [Transformer-based Model for ASR N-Best Rescoring and Rewriting](2406.08207.md)
**Iwen E. Kang, Christophe Van Gysel, Man-Hung Siu** · 2024-06-12

<details>
<summary>Abstract</summary>

Voice assistants increasingly use on-device Automatic Speech Recognition (ASR) to ensure speed and privacy. However, due to resource constraints on the device, queries pertaining to complex information domains often require further processing by a search engine. For such applications, we propose a novel Transformer based model capable of rescoring and rewriting, by exploring full context of the N-best hypotheses in parallel. We also propose a new discriminative sequence training objective that can work well for both rescore and rewrite tasks. We show that our Rescore+Rewrite model outperforms the Rescore-only baseline, and achieves up to an average 8.6% relative Word Error Rate (WER) reduction over the ASR system by itself.

</details>

### [Audio-conditioned phonemic and prosodic annotation for building text-to-speech models from unlabeled speech data](2406.08111.md)
**Yuma Shirahata, Byeongseon Park, Ryuichi Yamamoto, Kentaro Tachibana** · 2024-06-12

<details>
<summary>Abstract</summary>

This paper proposes an audio-conditioned phonemic and prosodic annotation model for building text-to-speech (TTS) datasets from unlabeled speech samples. For creating a TTS dataset that consists of label-speech paired data, the proposed annotation model leverages an automatic speech recognition (ASR) model to obtain phonemic and prosodic labels from unlabeled speech samples. By fine-tuning a large-scale pre-trained ASR model, we can construct the annotation model using a limited amount of label-speech paired data within an existing TTS dataset. To alleviate the shortage of label-speech paired data for training the annotation model, we generate pseudo label-speech paired data using text-only corpora and an auxiliary TTS model. This TTS model is also trained with the existing TTS dataset. Experimental results show that the TTS model trained with the dataset created by the proposed annotation method can synthesize speech as naturally as the one trained with a fully-labeled dataset.

</details>

### [Guiding Frame-Level CTC Alignments Using Self-knowledge Distillation](2406.07909.md)
**Eungbeom Kim, Hantae Kim, Kyogu Lee** · 2024-06-12

<details>
<summary>Abstract</summary>

Transformer encoder with connectionist temporal classification (CTC) framework is widely used for automatic speech recognition (ASR). However, knowledge distillation (KD) for ASR displays a problem of disagreement between teacher-student models in frame-level alignment which ultimately hinders it from improving the student model's performance. In order to resolve this problem, this paper introduces a self-knowledge distillation (SKD) method that guides the frame-level alignment during the training time. In contrast to the conventional method using separate teacher and student models, this study introduces a simple and effective method sharing encoder layers and applying the sub-model as the student model. Overall, our approach is effective in improving both the resource efficiency as well as performance. We also conducted an experimental analysis of the spike timings to illustrate that the proposed method improves performance by reducing the alignment disagreement.

</details>

### [Dual-Pipeline with Low-Rank Adaptation for New Language Integration in Multilingual ASR](2406.07842.md)
**Yerbolat Khassanov, Zhipeng Chen, Tianfeng Chen, Tze Yuang Chong et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

This paper addresses challenges in integrating new languages into a pre-trained multilingual automatic speech recognition (mASR) system, particularly in scenarios where training data for existing languages is limited or unavailable. The proposed method employs a dual-pipeline with low-rank adaptation (LoRA). It maintains two data flow pipelines-one for existing languages and another for new languages. The primary pipeline follows the standard flow through the pre-trained parameters of mASR, while the secondary pipeline additionally utilizes language-specific parameters represented by LoRA and a separate output decoder module. Importantly, the proposed approach minimizes the performance degradation of existing languages and enables a language-agnostic operation mode, facilitated by a decoder selection strategy. We validate the effectiveness of the proposed method by extending the pre-trained Whisper model to 19 new languages from the FLEURS dataset

</details>

### [PRoDeliberation: Parallel Robust Deliberation for End-to-End Spoken Language Understanding](2406.07823.md)
**Trang Le, Daniel Lazar, Suyoun Kim, Shan Jiang et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is a critical component of voice assistants; it consists of converting speech to semantic parses for task execution. Previous works have explored end-to-end models to improve the quality and robustness of SLU models with Deliberation, however these models have remained autoregressive, resulting in higher latencies. In this work we introduce PRoDeliberation, a novel method leveraging a Connectionist Temporal Classification-based decoding strategy as well as a denoising objective to train robust non-autoregressive deliberation models. We show that PRoDeliberation achieves the latency reduction of parallel decoding (2-10x improvement over autoregressive models) while retaining the ability to correct Automatic Speech Recognition (ASR) mistranscriptions of autoregressive deliberation systems. We further show that the design of the denoising training allows PRoDeliberation to overcome the limitations of small ASR devices, and we provide analysis on the necessity of each component of the system.

</details>

### [PolySpeech: Exploring Unified Multitask Speech Models for Competitiveness with Single-task Models](2406.07801.md)
**Runyan Yang, Huibao Yang, Xiqing Zhang, Tiantian Ye et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

Recently, there have been attempts to integrate various speech processing tasks into a unified model. However, few previous works directly demonstrated that joint optimization of diverse tasks in multitask speech models has positive influence on the performance of individual tasks. In this paper we present a multitask speech model -- PolySpeech, which supports speech recognition, speech synthesis, and two speech classification tasks. PolySpeech takes multi-modal language model as its core structure and uses semantic representations as speech inputs. We introduce semantic speech embedding tokenization and speech reconstruction methods to PolySpeech, enabling efficient generation of high-quality speech for any given speaker. PolySpeech shows competitiveness across various tasks compared to single-task models. In our experiments, multitask optimization achieves performance comparable to single-task optimization and is especially beneficial for specific tasks.

</details>

### [AS-70: A Mandarin stuttered speech dataset for automatic speech recognition and stuttering event detection](2406.07256.md)
**Rong Gong, Hongfei Xue, Lezhi Wang, Xin Xu et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

The rapid advancements in speech technologies over the past two decades have led to human-level performance in tasks like automatic speech recognition (ASR) for fluent speech. However, the efficacy of these models diminishes when applied to atypical speech, such as stuttering. This paper introduces AS-70, the first publicly available Mandarin stuttered speech dataset, which stands out as the largest dataset in its category. Encompassing conversational and voice command reading speech, AS-70 includes verbatim manual transcription, rendering it suitable for various speech-related tasks. Furthermore, baseline systems are established, and experimental results are presented for ASR and stuttering event detection (SED) tasks. By incorporating this dataset into the model fine-tuning, significant improvements in the state-of-the-art ASR models, e.g., Whisper and Hubert, are observed, enhancing their inclusivity in addressing stuttered speech.

</details>

### [Tag and correct: high precision post-editing approach to correction of speech recognition errors](2406.07589.md)
**Tomasz Ziętkiewicz** · 2024-06-11

<details>
<summary>Abstract</summary>

This paper presents a new approach to the problem of correcting speech recognition errors by means of post-editing. It consists of using a neural sequence tagger that learns how to correct an ASR (Automatic Speech Recognition) hypothesis word by word and a corrector module that applies corrections returned by the tagger. The proposed solution is applicable to any ASR system, regardless of its architecture, and provides high-precision control over errors being corrected. This is especially crucial in production environments, where avoiding the introduction of new mistakes by the error correction model may be more important than the net gain in overall results. The results show that the performance of the proposed error correction models is comparable with previous approaches while requiring much smaller resources to train, which makes it suitable for industrial applications, where both inference latency and training times are critical factors that limit the use of other techniques.

</details>

### [Spoken Language Corpora Augmentation with Domain-Specific Voice-Cloned Speech](2406.07090.md)
**Mateusz Czyżnikiewicz, Łukasz Bondaruk, Jakub Kubiak, Adam Wiącek et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

In this paper we study the impact of augmenting spoken language corpora with domain-specific synthetic samples for the purpose of training a speech recognition system. Using both a conventional neural TTS system and a zero-shot one with voice cloning ability we generate speech corpora that vary in the number of voices. We compare speech recognition models trained with addition of different amounts of synthetic data generated using these two methods with a baseline model trained solely on voice recordings. We show that while the quality of voice-cloned dataset is lower, its increased multivoiceity makes it much more effective than the one with only a few voices synthesized with the use of a conventional neural TTS system. Furthermore, our experiments indicate that using low variability synthetic speech quickly leads to saturation in the quality of the ASR whereas high variability speech provides improvement even when increasing total amount of data used for training by 30%.

</details>

### [Can We Achieve High-quality Direct Speech-to-Speech Translation without Parallel Speech Data?](2406.07289.md)
**Qingkai Fang, Shaolei Zhang, Zhengrui Ma, Min Zhang et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

Recently proposed two-pass direct speech-to-speech translation (S2ST) models decompose the task into speech-to-text translation (S2TT) and text-to-speech (TTS) within an end-to-end model, yielding promising results. However, the training of these models still relies on parallel speech data, which is extremely challenging to collect. In contrast, S2TT and TTS have accumulated a large amount of data and pretrained models, which have not been fully utilized in the development of S2ST models. Inspired by this, in this paper, we first introduce a composite S2ST model named ComSpeech, which can seamlessly integrate any pretrained S2TT and TTS models into a direct S2ST model. Furthermore, to eliminate the reliance on parallel speech data, we propose a novel training method ComSpeech-ZS that solely utilizes S2TT and TTS data. It aligns representations in the latent space through contrastive learning, enabling the speech synthesis capability learned from the TTS data to generalize to S2ST in a zero-shot manner. Experimental results on the CVSS dataset show that when the parallel speech data is available, ComSpeech surpasses previous two-pass models like UnitY and Translatotron 2 in both translation quality and decoding speed. When there is no parallel speech data, ComSpeech-ZS lags behind \name by only 0.7 ASR-BLEU and outperforms the cascaded models.

</details>

### [A Non-autoregressive Generation Framework for End-to-End Simultaneous Speech-to-Speech Translation](2406.06937.md)
**Zhengrui Ma, Qingkai Fang, Shaolei Zhang, Shoutao Guo et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

Simultaneous translation models play a crucial role in facilitating communication. However, existing research primarily focuses on text-to-text or speech-to-text models, necessitating additional cascade components to achieve speech-to-speech translation. These pipeline methods suffer from error propagation and accumulate delays in each cascade component, resulting in reduced synchronization between the speaker and listener. To overcome these challenges, we propose a novel non-autoregressive generation framework for simultaneous speech translation (NAST-S2X), which integrates speech-to-text and speech-to-speech tasks into a unified end-to-end framework. We develop a non-autoregressive decoder capable of concurrently generating multiple text or acoustic unit tokens upon receiving fixed-length speech chunks. The decoder can generate blank or repeated tokens and employ CTC decoding to dynamically adjust its latency. Experimental results show that NAST-S2X outperforms state-of-the-art models in both speech-to-text and speech-to-speech tasks. It achieves high-quality simultaneous interpretation within a delay of less than 3 seconds and provides a 28 times decoding speedup in offline generation.

</details>

### [A Parameter-efficient Language Extension Framework for Multilingual ASR](2406.06329.md)
**Wei Liu, Jingyong Hou, Dong Yang, Muyong Cao et al.** · 2024-06-10

<details>
<summary>Abstract</summary>

Covering all languages with a multilingual speech recognition model (MASR) is very difficult. Performing language extension on top of an existing MASR is a desirable choice. In this study, the MASR continual learning problem is probabilistically decomposed into language identity prediction (LP) and cross-lingual adaptation (XLA) sub-problems. Based on this, we propose an architecture-based framework for language extension that can fundamentally solve catastrophic forgetting, debudded as PELE. PELE is designed to be parameter-efficient, incrementally incorporating an add-on module to adapt to a new language. Specifically, different parameter-efficient fine-tuning (PEFT) modules and their variants are explored as potential candidates to perform XLA. Experiments are carried out on 5 new languages with a wide range of low-resourced data sizes. The best-performing PEFT candidate can achieve satisfactory performance across all languages and demonstrates superiority in three of five languages over the continual joint learning setting. Notably, PEFT methods focusing on weight parameters or input features are revealed to be limited in performance, showing significantly inferior extension capabilities compared to inserting a lightweight module in between layers such as an Adapter.

</details>

### [Prompting Large Language Models with Audio for General-Purpose Speech Summarization](2406.05968.md)
**Wonjune Kang, Deb Roy** · 2024-06-10

<details>
<summary>Abstract</summary>

In this work, we introduce a framework for speech summarization that leverages the processing and reasoning capabilities of large language models (LLMs). We propose an end-to-end system that combines an instruction-tuned LLM with an audio encoder that converts speech into token representations that the LLM can interpret. Using a dataset with paired speech-text data, the overall system is trained to generate consistent responses to prompts with the same semantic information regardless of the input modality. The resulting framework allows the LLM to process speech inputs in the same way as text, enabling speech summarization by simply prompting the LLM. Unlike prior approaches, our method is able to summarize spoken content from any arbitrary domain, and it can produce summaries in different styles by varying the LLM prompting strategy. Experiments demonstrate that our approach outperforms a cascade baseline of speech recognition followed by LLM text processing.

</details>

### [StreamAtt: Direct Streaming Speech-to-Text Translation with Attention-based Audio History Selection](2406.06097.md)
**Sara Papi, Marco Gaido, Matteo Negri, Luisa Bentivogli** · 2024-06-10

<details>
<summary>Abstract</summary>

Streaming speech-to-text translation (StreamST) is the task of automatically translating speech while incrementally receiving an audio stream. Unlike simultaneous ST (SimulST), which deals with pre-segmented speech, StreamST faces the challenges of handling continuous and unbounded audio streams. This requires additional decisions about what to retain of the previous history, which is impractical to keep entirely due to latency and computational constraints. Despite the real-world demand for real-time ST, research on streaming translation remains limited, with existing works solely focusing on SimulST. To fill this gap, we introduce StreamAtt, the first StreamST policy, and propose StreamLAAL, the first StreamST latency metric designed to be comparable with existing metrics for SimulST. Extensive experiments across all 8 languages of MuST-C v1.0 show the effectiveness of StreamAtt compared to a naive streaming baseline and the related state-of-the-art SimulST policy, providing a first step in StreamST research.

</details>

### [Optimizing Multi-Stuttered Speech Classification: Leveraging Whisper's Encoder for Efficient Parameter Reduction in Automated Assessment](2406.05784.md)
**Huma Ameer, Seemab Latif, Mehwish Fatima** · 2024-06-09

<details>
<summary>Abstract</summary>

The automated classification of stuttered speech has significant implications for timely assessments providing assistance to speech language pathologists. Despite notable advancements in the field, the cases in which multiple disfluencies occur in speech require attention. We have taken a progressive approach to fill this gap by classifying multi-stuttered speech more efficiently. The problem has been addressed by firstly curating a dataset of multi-stuttered disfluencies from open source dataset SEP-28k audio clips. Secondly, employing Whisper, a state-of-the-art speech recognition model has been leveraged by using its encoder and taking the problem as multi label classification. Thirdly, using a 6 encoder layer Whisper and experimenting with various layer freezing strategies, a computationally efficient configuration of the model was identified. The proposed configuration achieved micro, macro, and weighted F1-scores of 0.88, 0.85, and 0.87, correspondingly on an external test dataset i.e. Fluency-Bank. In addition, through layer freezing strategies, we were able to achieve the aforementioned results by fine-tuning a single encoder layer, consequently, reducing the model's trainable parameters from 20.27 million to 3.29 million. This research study unveils the contribution of the last encoder layer in the identification of disfluencies in stuttered speech. Consequently, it has led to a computationally efficient approach, 83.7% less parameters to train, making the proposed approach more adaptable for various dialects and languages.

</details>

### [MS-HuBERT: Mitigating Pre-training and Inference Mismatch in Masked Language Modelling methods for learning Speech Representations](2406.05661.md)
**Hemant Yadav, Sunayana Sitaram, Rajiv Ratn Shah** · 2024-06-09

<details>
<summary>Abstract</summary>

In recent years, self-supervised pre-training methods have gained significant traction in learning high-level information from raw speech. Among these methods, HuBERT has demonstrated SOTA performance in automatic speech recognition (ASR). However, HuBERT's performance lags behind data2vec due to disparities in pre-training strategies. In this paper, we propose (i) a Swap method to address pre-training and inference mismatch observed in HuBERT and (ii) incorporates Multicluster masked prediction loss for more effective utilization of the models capacity. The resulting method is, MS-HuBERT, an end-to-end self-supervised pre-training method for learning robust speech representations. It beats vanilla HuBERT on the ASR Librispeech benchmark on average by a 5% margin when evaluated on different finetuning splits. Additionally, we demonstrate that the learned embeddings obtained during pre-training encode essential information for improving performance of content based tasks such as ASR.

</details>

### [LLM-based speaker diarization correction: A generalizable approach](2406.04927.md)
**Georgios Efstathiadis, Vijay Yadav, Anzar Abbas** · 2024-06-07

<details>
<summary>Abstract</summary>

Speaker diarization is necessary for interpreting conversations transcribed using automated speech recognition (ASR) tools. Despite significant developments in diarization methods, diarization accuracy remains an issue. Here, we investigate the use of large language models (LLMs) for diarization correction as a post-processing step. LLMs were fine-tuned using the Fisher corpus, a large dataset of transcribed conversations. The ability of the models to improve diarization accuracy in a holdout dataset from the Fisher corpus as well as an independent dataset was measured. We report that fine-tuned LLMs can markedly improve diarization accuracy. However, model performance is constrained to transcripts produced using the same ASR tool as the transcripts used for fine-tuning, limiting generalizability. To address this constraint, an ensemble model was developed by combining weights from three separate models, each fine-tuned using transcripts from a different ASR tool. The ensemble model demonstrated better overall performance than each of the ASR-specific models, suggesting that a generalizable and ASR-agnostic approach may be achievable. We have made the weights of these models publicly available on HuggingFace at https://huggingface.co/bklynhlth.

</details>

### [Speaker-Smoothed kNN Speaker Adaptation for End-to-End ASR](2406.04791.md)
**Shaojun Li, Daimeng Wei, Hengchao Shang, Jiaxin Guo et al.** · 2024-06-07

<details>
<summary>Abstract</summary>

Despite recent improvements in End-to-End Automatic Speech Recognition (E2E ASR) systems, the performance can degrade due to vocal characteristic mismatches between training and testing data, particularly with limited target speaker adaptation data. We propose a novel speaker adaptation approach Speaker-Smoothed kNN that leverages k-Nearest Neighbors (kNN) retrieval techniques to improve model output by finding correctly pronounced tokens from its pre-built datastore during the decoding phase. Moreover, we utilize x-vector to dynamically adjust kNN interpolation parameters for data sparsity issue. This approach was validated using KeSpeech and MagicData corpora under in-domain and all-domain settings. Our method consistently performs comparably to fine-tuning without the associated performance degradation during speaker changes. Furthermore, in the all-domain setting, our method achieves state-of-the-art results, reducing the CER in both single speaker and multi-speaker test scenarios.

</details>

### [LoRA-Whisper: Parameter-Efficient and Extensible Multilingual ASR](2406.06619.md)
**Zheshu Song, Jianheng Zhuo, Yifan Yang, Ziyang Ma et al.** · 2024-06-07

<details>
<summary>Abstract</summary>

Recent years have witnessed significant progress in multilingual automatic speech recognition (ASR), driven by the emergence of end-to-end (E2E) models and the scaling of multilingual datasets. Despite that, two main challenges persist in multilingual ASR: language interference and the incorporation of new languages without degrading the performance of the existing ones. This paper proposes LoRA-Whisper, which incorporates LoRA matrix into Whisper for multilingual ASR, effectively mitigating language interference. Furthermore, by leveraging LoRA and the similarities between languages, we can achieve better performance on new languages while upholding consistent performance on original ones. Experiments on a real-world task across eight languages demonstrate that our proposed LoRA-Whisper yields a relative gain of 18.5% and 23.0% over the baseline system for multilingual ASR and language expansion respectively.

</details>

### [Flexible Multichannel Speech Enhancement for Noise-Robust Frontend](2406.04552.md)
**Ante Jukić, Jagadeesh Balam, Boris Ginsburg** · 2024-06-06

<details>
<summary>Abstract</summary>

This paper proposes a flexible multichannel speech enhancement system with the main goal of improving robustness of automatic speech recognition (ASR) in noisy conditions. The proposed system combines a flexible neural mask estimator applicable to different channel counts and configurations and a multichannel filter with automatic reference selection. A transform-attend-concatenate layer is proposed to handle cross-channel information in the mask estimator, which is shown to be effective for arbitrary microphone configurations. The presented evaluation demonstrates the effectiveness of the flexible system for several seen and unseen compact array geometries, matching the performance of fixed configuration-specific systems. Furthermore, a significantly improved ASR performance is observed for configurations with randomly-placed microphones.

</details>

### [Label-Synchronous Neural Transducer for E2E Simultaneous Speech Translation](2406.04541.md)
**Keqi Deng, Philip C. Woodland** · 2024-06-06

<details>
<summary>Abstract</summary>

While the neural transducer is popular for online speech recognition, simultaneous speech translation (SST) requires both streaming and re-ordering capabilities. This paper presents the LS-Transducer-SST, a label-synchronous neural transducer for SST, which naturally possesses these two properties. The LS-Transducer-SST dynamically decides when to emit translation tokens based on an Auto-regressive Integrate-and-Fire (AIF) mechanism. A latency-controllable AIF is also proposed, which can control the quality-latency trade-off either only during decoding, or it can be used in both decoding and training. The LS-Transducer-SST can naturally utilise monolingual text-only data via its prediction network which helps alleviate the key issue of data sparsity for E2E SST. During decoding, a chunk-based incremental joint decoding technique is designed to refine and expand the search space. Experiments on the Fisher-CallHome Spanish (Es-En) and MuST-C En-De data show that the LS-Transducer-SST gives a better quality-latency trade-off than existing popular methods. For example, the LS-Transducer-SST gives a 3.1/2.9 point BLEU increase (Es-En/En-De) relative to CAAT at a similar latency and a 1.4 s reduction in average lagging latency with similar BLEU scores relative to Wait-k.

</details>

### [LipGER: Visually-Conditioned Generative Error Correction for Robust Automatic Speech Recognition](2406.04432.md)
**Sreyan Ghosh, Sonal Kumar, Ashish Seth, Purva Chiniya et al.** · 2024-06-06

<details>
<summary>Abstract</summary>

Visual cues, like lip motion, have been shown to improve the performance of Automatic Speech Recognition (ASR) systems in noisy environments. We propose LipGER (Lip Motion aided Generative Error Correction), a novel framework for leveraging visual cues for noise-robust ASR. Instead of learning the cross-modal correlation between the audio and visual modalities, we make an LLM learn the task of visually-conditioned (generative) ASR error correction. Specifically, we instruct an LLM to predict the transcription from the N-best hypotheses generated using ASR beam-search. This is further conditioned on lip motions. This approach addresses key challenges in traditional AVSR learning, such as the lack of large-scale paired datasets and difficulties in adapting to new domains. We experiment on 4 datasets in various settings and show that LipGER improves the Word Error Rate in the range of 1.1%-49.2%. We also release LipHyp, a large-scale dataset with hypothesis-transcription pairs that is additionally equipped with lip motion cues to promote further research in this space

</details>

### [Beyond Performance Plateaus: A Comprehensive Study on Scalability in Speech Enhancement](2406.04269.md)
**Wangyou Zhang, Kohei Saijo, Jee-weon Jung, Chenda Li et al.** · 2024-06-06

<details>
<summary>Abstract</summary>

Deep learning-based speech enhancement (SE) models have achieved impressive performance in the past decade. Numerous advanced architectures have been designed to deliver state-of-the-art performance; however, their scalability potential remains unrevealed. Meanwhile, the majority of research focuses on small-sized datasets with restricted diversity, leading to a plateau in performance improvement. In this paper, we aim to provide new insights for addressing the above issues by exploring the scalability of SE models in terms of architectures, model sizes, compute budgets, and dataset sizes. Our investigation involves several popular SE architectures and speech data from different domains. Experiments reveal both similarities and distinctions between the scaling effects in SE and other tasks such as speech recognition. These findings further provide insights into the under-explored SE directions, e.g., larger-scale multi-domain corpora and efficiently scalable architectures.

</details>

### [Hypernetworks for Personalizing ASR to Atypical Speech](2406.04240.md)
**Max Müller-Eberstein, Dianna Yee, Karren Yang, Gautam Varma Mantena et al.** · 2024-06-06

<details>
<summary>Abstract</summary>

Parameter-efficient fine-tuning (PEFT) for personalizing automatic speech recognition (ASR) has recently shown promise for adapting general population models to atypical speech. However, these approaches assume a priori knowledge of the atypical speech disorder being adapted for -- the diagnosis of which requires expert knowledge that is not always available. Even given this knowledge, data scarcity and high inter/intra-speaker variability further limit the effectiveness of traditional fine-tuning. To circumvent these challenges, we first identify the minimal set of model parameters required for ASR adaptation. Our analysis of each individual parameter's effect on adaptation performance allows us to reduce Word Error Rate (WER) by half while adapting 0.03% of all weights. Alleviating the need for cohort-specific models, we next propose the novel use of a meta-learned hypernetwork to generate highly individualized, utterance-level adaptations on-the-fly for a diverse set of atypical speech characteristics. Evaluating adaptation at the global, cohort and individual-level, we show that hypernetworks generalize better to out-of-distribution speakers, while maintaining an overall relative WER reduction of 75.2% using 0.1% of the full parameter budget.

</details>

### [Speed of Light Exact Greedy Decoding for RNN-T Speech Recognition Models on GPU](2406.03791.md)
**Daniel Galvez, Vladimir Bataev, Hainan Xu, Tim Kaldewey** · 2024-06-06

<details>
<summary>Abstract</summary>

The vast majority of inference time for RNN Transducer (RNN-T) models today is spent on decoding. Current state-of-the-art RNN-T decoding implementations leave the GPU idle ~80% of the time. Leveraging a new CUDA 12.4 feature, CUDA graph conditional nodes, we present an exact GPU-based implementation of greedy decoding for RNN-T models that eliminates this idle time. Our optimizations speed up a 1.1 billion parameter RNN-T model end-to-end by a factor of 2.5x. This technique can applied to the "label looping" alternative greedy decoding algorithm as well, achieving 1.7x and 1.4x end-to-end speedups when applied to 1.1 billion parameter RNN-T and Token and Duration Transducer models respectively. This work enables a 1.1 billion parameter RNN-T model to run only 16% slower than a similarly sized CTC model, contradicting the common belief that RNN-T models are not suitable for high throughput inference. The implementation is available in NVIDIA NeMo.

</details>

### [Enhancing CTC-based speech recognition with diverse modeling units](2406.03274.md)
**Shiyi Han, Zhihong Lei, Mingbin Xu, Xingyu Na et al.** · 2024-06-05

<details>
<summary>Abstract</summary>

In recent years, the evolution of end-to-end (E2E) automatic speech recognition (ASR) models has been remarkable, largely due to advances in deep learning architectures like transformer. On top of E2E systems, researchers have achieved substantial accuracy improvement by rescoring E2E model's N-best hypotheses with a phoneme-based model. This raises an interesting question about where the improvements come from other than the system combination effect. We examine the underlying mechanisms driving these gains and propose an efficient joint training approach, where E2E models are trained jointly with diverse modeling units. This methodology does not only align the strengths of both phoneme and grapheme-based models but also reveals that using these diverse modeling units in a synergistic way can significantly enhance model accuracy. Our findings offer new insights into the optimal integration of heterogeneous modeling units in the development of more robust and accurate ASR systems.

</details>

### [Error-preserving Automatic Speech Recognition of Young English Learners' Language](2406.03235.md)
**Janick Michot, Manuela Hürlimann, Jan Deriu, Luzia Sauer et al.** · 2024-06-05

<details>
<summary>Abstract</summary>

One of the central skills that language learners need to practice is speaking the language. Currently, students in school do not get enough speaking opportunities and lack conversational practice. Recent advances in speech technology and natural language processing allow for the creation of novel tools to practice their speaking skills. In this work, we tackle the first component of such a pipeline, namely, the automated speech recognition module (ASR), which faces a number of challenges: first, state-of-the-art ASR models are often trained on adult read-aloud data by native speakers and do not transfer well to young language learners' speech. Second, most ASR systems contain a powerful language model, which smooths out errors made by the speakers. To give corrective feedback, which is a crucial part of language learning, the ASR systems in our setting need to preserve the errors made by the language learners. In this work, we build an ASR system that satisfies these requirements: it works on spontaneous speech by young language learners and preserves their errors. For this, we collected a corpus containing around 85 hours of English audio spoken by learners in Switzerland from grades 4 to 6 on different language learning tasks, which we used to train an ASR model. Our experiments show that our model benefits from direct fine-tuning on children's voices and has a much higher error preservation rate than other models.

</details>

### [Joint Beam Search Integrating CTC, Attention, and Transducer Decoders](2406.02950.md)
**Yui Sudo, Muhammad Shakeel, Yosuke Fukumoto, Brian Yan et al.** · 2024-06-05

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (E2E-ASR) can be classified by its decoder architectures, such as connectionist temporal classification (CTC), recurrent neural network transducer (RNN-T), attention-based encoder-decoder, and Mask-CTC models. Each decoder architecture has advantages and disadvantages, leading practitioners to switch between these different models depending on application requirements. Instead of building separate models, we propose a joint modeling scheme where four decoders (CTC, RNN-T, attention, and Mask-CTC) share the same encoder -- we refer to this as 4D modeling. The 4D model is trained jointly, which will bring model regularization and maximize the model robustness thanks to their complementary properties. To efficiently train the 4D model, we introduce a two-stage training strategy that stabilizes the joint training. In addition, we propose three novel joint beam search algorithms by combining three decoders (CTC, RNN-T, and attention) to further improve performance. These three beam search algorithms differ in which decoder is used as the primary decoder. We carefully evaluate the performance and computational tradeoffs associated with each algorithm. Experimental results demonstrate that the jointly trained 4D model outperforms the E2E-ASR models trained with only one individual decoder. Furthermore, we demonstrate that the proposed joint beam search algorithm outperforms the previously proposed CTC/attention decoding.

</details>

### [Text Injection for Neural Contextual Biasing](2406.02921.md)
**Zhong Meng, Zelin Wu, Rohit Prabhavalkar, Cal Peyser et al.** · 2024-06-05

<details>
<summary>Abstract</summary>

Neural contextual biasing effectively improves automatic speech recognition (ASR) for crucial phrases within a speaker's context, particularly those that are infrequent in the training data. This work proposes contextual text injection (CTI) to enhance contextual ASR. CTI leverages not only the paired speech-text data, but also a much larger corpus of unpaired text to optimize the ASR model and its biasing component. Unpaired text is converted into speech-like representations and used to guide the model's attention towards relevant bias phrases. Moreover, we introduce a contextual text-injected (CTI) minimum word error rate (MWER) training, which minimizes the expected WER caused by contextual biasing when unpaired text is injected into the model. Experiments show that CTI with 100 billion text sentences can achieve up to 43.3% relative WER reduction from a strong neural biasing model. CTI-MWER provides a further relative improvement of 23.5%.

</details>

### [USM RNN-T model weights binarization](2406.02887.md)
**Oleg Rybakov, Dmitriy Serdyuk, Chengjian Zheng** · 2024-06-05

<details>
<summary>Abstract</summary>

Large-scale universal speech models (USM) are already used in production. However, as the model size grows, the serving cost grows too. Serving cost of large models is dominated by model size that is why model size reduction is an important research topic. In this work we are focused on model size reduction using weights only quantization. We present the weights binarization of USM Recurrent Neural Network Transducer (RNN-T) and show that its model size can be reduced by 15.9x times at cost of word error rate (WER) increase by only 1.9% in comparison to the float32 model. It makes it attractive for practical applications.

</details>

### [Discrete Multimodal Transformers with a Pretrained Large Language Model for Mixed-Supervision Speech Processing](2406.06582.md)
**Viet Anh Trinh, Rosy Southwell, Yiwen Guan, Xinlu He et al.** · 2024-06-04

<details>
<summary>Abstract</summary>

Recent work on discrete speech tokenization has paved the way for models that can seamlessly perform multiple tasks across modalities, e.g., speech recognition, text to speech, speech to speech translation. Moreover, large language models (LLMs) pretrained from vast text corpora contain rich linguistic information that can improve accuracy in a variety of tasks. In this paper, we present a decoder-only Discrete Multimodal Language Model (DMLM), which can be flexibly applied to multiple tasks (ASR, T2S, S2TT, etc.) and modalities (text, speech, vision). We explore several critical aspects of discrete multi-modal models, including the loss function, weight initialization, mixed training supervision, and codebook. Our results show that DMLM benefits significantly, across multiple tasks and datasets, from a combination of supervised and unsupervised training. Moreover, for ASR, it benefits from initializing DMLM from a pretrained LLM, and from a codebook derived from Whisper activations.

</details>

### [Keyword-Guided Adaptation of Automatic Speech Recognition](2406.02649.md)
**Aviv Shamsian, Aviv Navon, Neta Glazer, Gill Hetz et al.** · 2024-06-04

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) technology has made significant progress in recent years, providing accurate transcription across various domains. However, some challenges remain, especially in noisy environments and specialized jargon. In this paper, we propose a novel approach for improved jargon word recognition by contextual biasing Whisper-based models. We employ a keyword spotting model that leverages the Whisper encoder representation to dynamically generate prompts for guiding the decoder during the transcription process. We introduce two approaches to effectively steer the decoder towards these prompts: KG-Whisper, which is aimed at fine-tuning the Whisper decoder, and KG-Whisper-PT, which learns a prompt prefix. Our results show a significant improvement in the recognition accuracy of specified keywords and in reducing the overall word error rates. Specifically, in unseen language generalization, we demonstrate an average WER improvement of 5.1% over Whisper.

</details>

### [Whistle: Data-Efficient Multilingual and Crosslingual Speech Recognition via Weakly Phonetic Supervision](2406.02166.md)
**Saierdaer Yusuyin, Te Ma, Hao Huang, Wenbo Zhao et al.** · 2024-06-04

<details>
<summary>Abstract</summary>

There exist three approaches for multilingual and crosslingual automatic speech recognition (MCL-ASR) - supervised pretraining with phonetic or graphemic transcription, and self-supervised pretraining. We find that pretraining with phonetic supervision has been underappreciated so far for MCL-ASR, while conceptually it is more advantageous for information sharing between different languages. This paper explores the approach of pretraining with weakly phonetic supervision towards data-efficient MCL-ASR, which is called Whistle. We relax the requirement of gold-standard human-validated phonetic transcripts, and obtain International Phonetic Alphabet (IPA) based transcription by leveraging the LanguageNet grapheme-to-phoneme (G2P) models. We construct a common experimental setup based on the CommonVoice dataset, called CV-Lang10, with 10 seen languages and 2 unseen languages. A set of experiments are conducted on CV-Lang10 to compare, as fair as possible, the three approaches under the common setup for MCL-ASR. Experiments demonstrate the advantages of phoneme-based models (Whistle) for MCL-ASR, in terms of speech recognition for seen languages, crosslingual performance for unseen languages with different amounts of few-shot data, overcoming catastrophic forgetting, and training efficiency. It is found that when training data is more limited, phoneme supervision can achieve better results compared to subword supervision and self-supervision, thereby providing higher data-efficiency. To support reproducibility and promote future research along this direction, we release the code, models and data for the entire pipeline of Whistle at https://github.com/thu-spmi/CAT/tree/master/egs/cv-lang10.

</details>

### [Language-Universal Speech Attributes Modeling for Zero-Shot Multilingual Spoken Keyword Recognition](2406.02488.md)
**Hao Yen, Pin-Jui Ku, Sabato Marco Siniscalchi, Chin-Hui Lee** · 2024-06-04

<details>
<summary>Abstract</summary>

We propose a novel language-universal approach to end-to-end automatic spoken keyword recognition (SKR) leveraging upon (i) a self-supervised pre-trained model, and (ii) a set of universal speech attributes (manner and place of articulation). Specifically, Wav2Vec2.0 is used to generate robust speech representations, followed by a linear output layer to produce attribute sequences. A non-trainable pronunciation model then maps sequences of attributes into spoken keywords in a multilingual setting. Experiments on the Multilingual Spoken Words Corpus show comparable performances to character- and phoneme-based SKR in seen languages. The inclusion of domain adversarial training (DAT) improves the proposed framework, outperforming both character- and phoneme-based SKR approaches with 13.73% and 17.22% relative word error rate (WER) reduction in seen languages, and achieves 32.14% and 19.92% WER reduction for unseen languages in zero-shot settings.

</details>

### [Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs](2406.01943.md)
**Nik Bear Brown** · 2024-06-04

<details>
<summary>Abstract</summary>

This paper surveys evaluation techniques to enhance the trustworthiness and understanding of Large Language Models (LLMs). As reliance on LLMs grows, ensuring their reliability, fairness, and transparency is crucial. We explore algorithmic methods and metrics to assess LLM performance, identify weaknesses, and guide development towards more trustworthy applications. Key evaluation metrics include Perplexity Measurement, NLP metrics (BLEU, ROUGE, METEOR, BERTScore, GLEU, Word Error Rate, Character Error Rate), Zero-Shot and Few-Shot Learning Performance, Transfer Learning Evaluation, Adversarial Testing, and Fairness and Bias Evaluation. We introduce innovative approaches like LLMMaps for stratified evaluation, Benchmarking and Leaderboards for competitive assessment, Stratified Analysis for in-depth understanding, Visualization of Blooms Taxonomy for cognitive level accuracy distribution, Hallucination Score for quantifying inaccuracies, Knowledge Stratification Strategy for hierarchical analysis, and Machine Learning Models for Hierarchy Generation. Human Evaluation is highlighted for capturing nuances that automated metrics may miss. These techniques form a framework for evaluating LLMs, aiming to enhance transparency, guide development, and establish user trust. Future papers will describe metric visualization and demonstrate each approach on practical examples.

</details>

### [Compute-Efficient Medical Image Classification with Softmax-Free Transformers and Sequence Normalization](2406.01314.md)
**Firas Khader, Omar S. M. El Nahhas, Tianyu Han, Gustav Müller-Franzes et al.** · 2024-06-03

<details>
<summary>Abstract</summary>

The Transformer model has been pivotal in advancing fields such as natural language processing, speech recognition, and computer vision. However, a critical limitation of this model is its quadratic computational and memory complexity relative to the sequence length, which constrains its application to longer sequences. This is especially crucial in medical imaging where high-resolution images can reach gigapixel scale. Efforts to address this issue have predominantely focused on complex techniques, such as decomposing the softmax operation integral to the Transformer's architecture. This paper addresses this quadratic computational complexity of Transformer models and introduces a remarkably simple and effective method that circumvents this issue by eliminating the softmax function from the attention mechanism and adopting a sequence normalization technique for the key, query, and value tokens. Coupled with a reordering of matrix multiplications this approach reduces the memory- and compute complexity to a linear scale. We evaluate this approach across various medical imaging datasets comprising fundoscopic, dermascopic, radiologic and histologic imaging data. Our findings highlight that these models exhibit a comparable performance to traditional transformer models, while efficiently handling longer sequences.

</details>

### [Generative Pre-trained Speech Language Model with Efficient Hierarchical Transformer](2406.00976.md)
**Yongxin Zhu, Dan Su, Liqiang He, Linli Xu et al.** · 2024-06-03

<details>
<summary>Abstract</summary>

While recent advancements in speech language models have achieved significant progress, they face remarkable challenges in modeling the long acoustic sequences of neural audio codecs. In this paper, we introduce \textbf{G}enerative \textbf{P}re-trained \textbf{S}peech \textbf{T}ransformer (GPST), a hierarchical transformer designed for efficient speech language modeling. GPST quantizes audio waveforms into two distinct types of discrete speech representations and integrates them within a hierarchical transformer architecture, allowing for a unified one-stage generation process and enhancing Hi-Res audio generation capabilities. By training on large corpora of speeches in an end-to-end unsupervised manner, GPST can generate syntactically consistent speech with diverse speaker identities. Given a brief 3-second prompt, GPST can produce natural and coherent personalized speech, demonstrating in-context learning abilities. Moreover, our approach can be easily extended to spoken cross-lingual speech generation by incorporating multi-lingual semantic tokens and universal acoustic tokens. Experimental results indicate that GPST significantly outperforms the existing speech language models in terms of word error rate, speech quality, and speaker similarity. The code is available at \url{https://github.com/youngsheen/GPST}.

</details>

### [YODAS: Youtube-Oriented Dataset for Audio and Speech](2406.00899.md)
**Xinjian Li, Shinnosuke Takamichi, Takaaki Saeki, William Chen et al.** · 2024-06-02

<details>
<summary>Abstract</summary>

In this study, we introduce YODAS (YouTube-Oriented Dataset for Audio and Speech), a large-scale, multilingual dataset comprising currently over 500k hours of speech data in more than 100 languages, sourced from both labeled and unlabeled YouTube speech datasets. The labeled subsets, including manual or automatic subtitles, facilitate supervised model training. Conversely, the unlabeled subsets are apt for self-supervised learning applications. YODAS is distinctive as the first publicly available dataset of its scale, and it is distributed under a Creative Commons license. We introduce the collection methodology utilized for YODAS, which contributes to the large-scale speech dataset construction. Subsequently, we provide a comprehensive analysis of speech, text contained within the dataset. Finally, we describe the speech recognition baselines over the top-15 languages.

</details>

### [Wav2Prompt: End-to-End Speech Prompt Generation and Tuning For LLM in Zero and Few-shot Learning](2406.00522.md)
**Keqi Deng, Guangzhi Sun, Philip C. Woodland** · 2024-06-01

<details>
<summary>Abstract</summary>

Wav2Prompt is proposed which allows straightforward integration between spoken input and a text-based large language model (LLM). Wav2Prompt uses a simple training process with only the same data used to train an automatic speech recognition (ASR) model. After training, Wav2Prompt learns continuous representations from speech and uses them as LLM prompts. To avoid task over-fitting issues found in prior work and preserve the emergent abilities of LLMs, Wav2Prompt takes LLM token embeddings as the training targets and utilises a continuous integrate-and-fire mechanism for explicit speech-text alignment. Therefore, a Wav2Prompt-LLM combination can be applied to zero-shot spoken language tasks such as speech translation (ST), speech understanding (SLU), speech question answering (SQA) and spoken-query-based QA (SQQA). It is shown that for these zero-shot tasks, Wav2Prompt performs similarly to an ASR-LLM cascade and better than recent prior work. If relatively small amounts of task-specific paired data are available in few-shot scenarios, the Wav2Prompt-LLM combination can be end-to-end (E2E) fine-tuned. The Wav2Prompt-LLM combination then yields greatly improved results relative to an ASR-LLM cascade for the above tasks. For instance, for English-French ST with the BLOOMZ-7B1 LLM, a Wav2Prompt-LLM combination gave a 8.5 BLEU point increase over an ASR-LLM cascade.

</details>

### [Is Self-Supervised Learning Enough to Fill in the Gap? A Study on Speech Inpainting](2405.20101.md)
**Ihab Asaad, Maxime Jacquelin, Olivier Perrotin, Laurent Girin et al.** · 2024-05-30

<details>
<summary>Abstract</summary>

Speech inpainting consists in reconstructing corrupted or missing speech segments using surrounding context, a process that closely resembles the pretext tasks in Self-Supervised Learning (SSL) for speech encoders. This study investigates using SSL-trained speech encoders for inpainting without any additional training beyond the initial pretext task, and simply adding a decoder to generate a waveform. We compare this approach to supervised fine-tuning of speech encoders for a downstream task -- here, inpainting. Practically, we integrate HuBERT as the SSL encoder and HiFi-GAN as the decoder in two configurations: (1) fine-tuning the decoder to align with the frozen pre-trained encoder's output and (2) fine-tuning the encoder for an inpainting task based on a frozen decoder's input. Evaluations are conducted under single- and multi-speaker conditions using in-domain datasets and out-of-domain datasets (including unseen speakers, diverse speaking styles, and noise). Both informed and blind inpainting scenarios are considered, where the position of the corrupted segment is either known or unknown. The proposed SSL-based methods are benchmarked against several baselines, including a text-informed method combining automatic speech recognition with zero-shot text-to-speech synthesis. Performance is assessed using objective metrics and perceptual evaluations. The results demonstrate that both approaches outperform baselines, successfully reconstructing speech segments up to 200 ms, and sometimes up to 400 ms. Notably, fine-tuning the SSL encoder achieves more accurate speech reconstruction in single-speaker settings, while a pre-trained encoder proves more effective for multi-speaker scenarios. This demonstrates that an SSL pretext task can transfer to speech inpainting, enabling successful speech reconstruction with a pre-trained encoder.

</details>

### [Zipper: A Multi-Tower Decoder Architecture for Fusing Modalities](2405.18669.md)
**Vicky Zayats, Peter Chen, Melissa Ferrari, Dirk Padfield** · 2024-05-29

<details>
<summary>Abstract</summary>

Integrating multiple generative foundation models, especially those trained on different modalities, into something greater than the sum of its parts poses significant challenges. Two key hurdles are the availability of aligned data (concepts that contain similar meaning but is expressed differently in different modalities), and effectively leveraging unimodal representations in cross-domain generative tasks, without compromising their original unimodal capabilities. We propose Zipper, a multi-tower decoder architecture that addresses these concerns by using cross-attention to flexibly compose multimodal generative models from independently pre-trained unimodal decoders. In our experiments fusing speech and text modalities, we show the proposed architecture performs very competitively in scenarios with limited aligned text-speech data. We also showcase the flexibility of our model to selectively maintain unimodal (e.g., text-to-text generation) generation performance by freezing the corresponding modal tower (e.g. text). In cross-modal tasks such as automatic speech recognition (ASR) where the output modality is text, we show that freezing the text backbone results in negligible performance degradation. In cross-modal tasks such as text-to-speech generation (TTS) where the output modality is speech, we show that using a pre-trained speech backbone results in superior performance to the baseline.

</details>

### [Augmented Conversation with Embedded Speech-Driven On-the-Fly Referencing in AR](2405.18537.md)
**Shivesh Jadon, Mehrad Faridan, Edward Mah, Rajan Vaish et al.** · 2024-05-28

<details>
<summary>Abstract</summary>

This paper introduces the concept of augmented conversation, which aims to support co-located in-person conversations via embedded speech-driven on-the-fly referencing in augmented reality (AR). Today computing technologies like smartphones allow quick access to a variety of references during the conversation. However, these tools often create distractions, reducing eye contact and forcing users to focus their attention on phone screens and manually enter keywords to access relevant information. In contrast, AR-based on-the-fly referencing provides relevant visual references in real-time, based on keywords extracted automatically from the spoken conversation. By embedding these visual references in AR around the conversation partner, augmented conversation reduces distraction and friction, allowing users to maintain eye contact and supporting more natural social interactions. To demonstrate this concept, we developed \system, a Hololens-based interface that leverages real-time speech recognition, natural language processing and gaze-based interactions for on-the-fly embedded visual referencing. In this paper, we explore the design space of visual referencing for conversations, and describe our our implementation -- building on seven design guidelines identified through a user-centered design process. An initial user study confirms that our system decreases distraction and friction in conversations compared to smartphone searches, while providing highly useful and relevant information.

</details>

### [Intelligent Clinical Documentation: Harnessing Generative AI for Patient-Centric Clinical Note Generation](2405.18346.md)
**Anjanava Biswas, Wrick Talukdar** · 2024-05-28

<details>
<summary>Abstract</summary>

Comprehensive clinical documentation is crucial for effective healthcare delivery, yet it poses a significant burden on healthcare professionals, leading to burnout, increased medical errors, and compromised patient safety. This paper explores the potential of generative AI (Artificial Intelligence) to streamline the clinical documentation process, specifically focusing on generating SOAP (Subjective, Objective, Assessment, Plan) and BIRP (Behavior, Intervention, Response, Plan) notes. We present a case study demonstrating the application of natural language processing (NLP) and automatic speech recognition (ASR) technologies to transcribe patient-clinician interactions, coupled with advanced prompting techniques to generate draft clinical notes using large language models (LLMs). The study highlights the benefits of this approach, including time savings, improved documentation quality, and enhanced patient-centered care. Additionally, we discuss ethical considerations, such as maintaining patient confidentiality and addressing model biases, underscoring the need for responsible deployment of generative AI in healthcare settings. The findings suggest that generative AI has the potential to revolutionize clinical documentation practices, alleviating administrative burdens and enabling healthcare professionals to focus more on direct patient care.

</details>

### [TransVIP: Speech to Speech Translation System with Voice and Isochrony Preservation](2405.17809.md)
**Chenyang Le, Yao Qian, Dongmei Wang, Long Zhou et al.** · 2024-05-28

<details>
<summary>Abstract</summary>

There is a rising interest and trend in research towards directly translating speech from one language to another, known as end-to-end speech-to-speech translation. However, most end-to-end models struggle to outperform cascade models, i.e., a pipeline framework by concatenating speech recognition, machine translation and text-to-speech models. The primary challenges stem from the inherent complexities involved in direct translation tasks and the scarcity of data. In this study, we introduce a novel model framework TransVIP that leverages diverse datasets in a cascade fashion yet facilitates end-to-end inference through joint probability. Furthermore, we propose two separated encoders to preserve the speaker's voice characteristics and isochrony from the source speech during the translation process, making it highly suitable for scenarios such as video dubbing. Our experiments on the French-English language pair demonstrate that our model outperforms the current state-of-the-art speech-to-speech translation model.

</details>

### ["Pass the butter": A study on desktop-classic multitasking robotic arm based on advanced YOLOv7 and BERT](2405.17250.md)
**Haohua Que, Wenbin Pan, Jie Xu, Hao Luo et al.** · 2024-05-27

<details>
<summary>Abstract</summary>

In recent years, various intelligent autonomous robots have begun to appear in daily life and production. Desktop-level robots are characterized by their flexible deployment, rapid response, and suitability for light workload environments. In order to meet the current societal demand for service robot technology, this study proposes using a miniaturized desktop-level robot (by ROS) as a carrier, locally deploying a natural language model (NLP-BERT), and integrating visual recognition (CV-YOLO) and speech recognition technology (ASR-Whisper) as inputs to achieve autonomous decision-making and rational action by the desktop robot. Three comprehensive experiments were designed to validate the robotic arm, and the results demonstrate excellent performance using this approach across all three experiments. In Task 1, the execution rates for speech recognition and action performance were 92.6% and 84.3%, respectively. In Task 2, the highest execution rates under the given conditions reached 92.1% and 84.6%, while in Task 3, the highest execution rates were 95.2% and 80.8%, respectively. Therefore, it can be concluded that the proposed solution integrating ASR, NLP, and other technologies on edge devices is feasible and provides a technical and engineering foundation for realizing multimodal desktop-level robots.

</details>

### [Contrastive and Consistency Learning for Neural Noisy-Channel Model in Spoken Language Understanding](2405.15097.md)
**Suyoung Kim, Jiyeon Hwang, Ho-Young Jung** · 2024-05-23

<details>
<summary>Abstract</summary>

Recently, deep end-to-end learning has been studied for intent classification in Spoken Language Understanding (SLU). However, end-to-end models require a large amount of speech data with intent labels, and highly optimized models are generally sensitive to the inconsistency between the training and evaluation conditions. Therefore, a natural language understanding approach based on Automatic Speech Recognition (ASR) remains attractive because it can utilize a pre-trained general language model and adapt to the mismatch of the speech input environment. Using this module-based approach, we improve a noisy-channel model to handle transcription inconsistencies caused by ASR errors. We propose a two-stage method, Contrastive and Consistency Learning (CCL), that correlates error patterns between clean and noisy ASR transcripts and emphasizes the consistency of the latent features of the two transcripts. Experiments on four benchmark datasets show that CCL outperforms existing methods and improves the ASR robustness in various noisy environments. Code is available at https://github.com/syoung7388/CCL.

</details>

### [Let's Fuse Step by Step: A Generative Fusion Decoding Algorithm with LLMs for Robust and Instruction-Aware ASR and OCR](2405.14259.md)
**Chan-Jan Hsu, Yi-Chang Chen, Feng-Ting Liao, Pei-Chen Ho et al.** · 2024-05-23

<details>
<summary>Abstract</summary>

We propose "Generative Fusion Decoding" (GFD), a novel shallow fusion framework designed to integrate large language models (LLMs) into cross-modal text recognition systems for automatic speech recognition (ASR) and optical character recognition (OCR). We derive the necessary formulations to enable GFD to operate across mismatched token spaces of different models by calculating likelihood at the byte level, thereby enabling seamless fusion and synchronous progression during the decoding process. GFD is plug-and-play by design, making it readily compatible with various auto-regressive models without the need for any re-training. GFD proves effective for general ASR and OCR tasks through intermediate and frequent interactions with LLMs, surpassing cascaded methods in English and Mandarin benchmarks. In addition, GFD transfers in-context learning abilities of LLMs and allows for adaptive ASR in instruction-aware and long-context settings, yielding significant WER reductions of up to 17.7\%.

</details>

### [Self-Taught Recognizer: Toward Unsupervised Adaptation for Speech Foundation Models](2405.14161.md)
**Yuchen Hu, Chen Chen, Chao-Han Huck Yang, Chengwei Qin et al.** · 2024-05-23

<details>
<summary>Abstract</summary>

We propose an unsupervised adaptation framework, Self-TAught Recognizer (STAR), which leverages unlabeled data to enhance the robustness of automatic speech recognition (ASR) systems in diverse target domains, such as noise and accents. STAR is developed for prevalent speech foundation models based on Transformer-related architecture with auto-regressive decoding (e.g., Whisper, Canary). Specifically, we propose a novel indicator that empirically integrates step-wise information during decoding to assess the token-level quality of pseudo labels without ground truth, thereby guiding model updates for effective unsupervised adaptation. Experimental results show that STAR achieves an average of 13.5% relative reduction in word error rate across 14 target domains, and it sometimes even approaches the upper-bound performance of supervised adaptation. Surprisingly, we also observe that STAR prevents the adapted model from the common catastrophic forgetting problem without recalling source-domain data. Furthermore, STAR exhibits high data efficiency that only requires less than one-hour unlabeled data, and seamless generality to alternative large speech models and speech translation tasks. Our code aims to open source to the research communities.

</details>

### [Joint Optimization of Streaming and Non-Streaming Automatic Speech Recognition with Multi-Decoder and Knowledge Distillation](2405.13514.md)
**Muhammad Shakeel, Yui Sudo, Yifan Peng, Shinji Watanabe** · 2024-05-22

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) can operate in two modes: streaming and non-streaming, each with its pros and cons. Streaming ASR processes the speech frames in real-time as it is being received, while non-streaming ASR waits for the entire speech utterance; thus, professionals may have to operate in either mode to satisfy their application. In this work, we present joint optimization of streaming and non-streaming ASR based on multi-decoder and knowledge distillation. Primarily, we study 1) the encoder integration of these ASR modules, followed by 2) separate decoders to make the switching mode flexible, and enhancing performance by 3) incorporating similarity-preserving knowledge distillation between the two modular encoders and decoders. Evaluation results show 2.6%-5.3% relative character error rate reductions (CERR) on CSJ for streaming ASR, and 8.3%-9.7% relative CERRs for non-streaming ASR within a single model compared to multiple standalone modules.

</details>

### [A Near-Real-Time Processing Ego Speech Filtering Pipeline Designed for Speech Interruption During Human-Robot Interaction](2405.13477.md)
**Yue Li, Florian A. Kunneman, Koen V. Hindriks** · 2024-05-22

<details>
<summary>Abstract</summary>

With current state-of-the-art automatic speech recognition (ASR) systems, it is not possible to transcribe overlapping speech audio streams separately. Consequently, when these ASR systems are used as part of a social robot like Pepper for interaction with a human, it is common practice to close the robot's microphone while it is talking itself. This prevents the human users to interrupt the robot, which limits speech-based human-robot interaction. To enable a more natural interaction which allows for such interruptions, we propose an audio processing pipeline for filtering out robot's ego speech using only a single-channel microphone. This pipeline takes advantage of the possibility to feed the robot ego speech signal, generated by a text-to-speech API, as training data into a machine learning model. The proposed pipeline combines a convolutional neural network and spectral subtraction to extract overlapping human speech from the audio recorded by the robot-embedded microphone. When evaluating on a held-out test set, we find that this pipeline outperforms our previous approach to this task, as well as state-of-the-art target speech extraction systems that were retrained on the same dataset. We have also integrated the proposed pipeline into a lightweight robot software development framework to make it available for broader use. As a step towards demonstrating the feasibility of deploying our pipeline, we use this framework to evaluate the effectiveness of the pipeline in a small lab-based feasibility pilot using the social robot Pepper. Our results show that when participants interrupt the robot, the pipeline can extract the participant's speech from one-second streaming audio buffers received by the robot-embedded single-channel microphone, hence in near-real time.

</details>

### [Contextualized Automatic Speech Recognition with Dynamic Vocabulary](2405.13344.md)
**Yui Sudo, Yosuke Fukumoto, Muhammad Shakeel, Yifan Peng et al.** · 2024-05-22

<details>
<summary>Abstract</summary>

Deep biasing (DB) enhances the performance of end-to-end automatic speech recognition (E2E-ASR) models for rare words or contextual phrases using a bias list. However, most existing methods treat bias phrases as sequences of subwords in a predefined static vocabulary. This naive sequence decomposition produces unnatural token patterns, significantly lowering their occurrence probability. More advanced techniques address this problem by expanding the vocabulary with additional modules, including the external language model shallow fusion or rescoring. However, they result in increasing the workload due to the additional modules. This paper proposes a dynamic vocabulary where bias tokens can be added during inference. Each entry in a bias list is represented as a single token, unlike a sequence of existing subword tokens. This approach eliminates the need to learn subword dependencies within the bias phrases. This method is easily applied to various architectures because it only expands the embedding and output layers in common E2E-ASR architectures. Experimental results demonstrate that the proposed method improves the bias phrase WER on English and Japanese datasets by 3.1 -- 4.9 points compared with the conventional DB method.

</details>

### [Non-autoregressive real-time Accent Conversion model with voice cloning](2405.13162.md)
**Vladimir Nechaev, Sergey Kosyakov** · 2024-05-21

<details>
<summary>Abstract</summary>

Currently, the development of Foreign Accent Conversion (FAC) models utilizes deep neural network architectures, as well as ensembles of neural networks for speech recognition and speech generation. The use of these models is limited by architectural features, which does not allow flexible changes in the timbre of the generated speech and requires the accumulation of context, leading to increased delays in generation and makes these systems unsuitable for use in real-time multi-user communication scenarios. We have developed the non-autoregressive model for real-time accent conversion with voice cloning. The model generates native-sounding L1 speech with minimal latency based on input L2 accented speech. The model consists of interconnected modules for extracting accent, gender, and speaker embeddings, converting speech, generating spectrograms, and decoding the resulting spectrogram into an audio signal. The model has the ability to save, clone and change the timbre, gender and accent of the speaker's voice in real time. The results of the objective assessment show that the model improves speech quality, leading to enhanced recognition performance in existing ASR systems. The results of subjective tests show that the proposed accent and gender encoder improves the generation quality. The developed model demonstrates high-quality low-latency accent conversion, voice cloning, and speech enhancement capabilities, making it suitable for real-time multi-user communication scenarios.

</details>

### [Could a Computer Architect Understand our Brain?](2405.12815.md)
**Valentin Puente-Varona** · 2024-05-21

<details>
<summary>Abstract</summary>

This paper presents a highly speculative model encompassing the cortex, thalamus, and hippocampus of the mammalian brain. While the majority of computational neuroscience models are founded upon empirical evidence, this model is predicated upon a hardware proposal for a machine learning accelerator. Such a device was designed to perform a specific task, such as speech recognition. The design process employed the principles and techniques typically used by computer architects in the design of devices such as processors. However, it also sought to maintain plausibility with biological systems in accordance with the current understanding of the mammalian brain. In the course of our research, we have identified a functional framework that may help to fill the gaps in current neuroscience, thereby facilitating the explanations for many elusive cognitive-level effects. This paper does not describe the device itself or the rationale behind the design decision, but instead, it presents a concise description of the derived model. In brief, the model provides a functional definition of the cortical column and its structural definition by the minicolumns. It also offers a descriptive model for the corticothalamic and corticostriatal loops, a functional proposal for the hippocampal complex, and a simplified view of the brainstem circuitry involved in auditory processing. The proposed model appears to provide an explanation for a number of cognitive phenomena, including some ERP effects, bottom-up and top-down attention, and the relationship between phenomena such as the cocktail party effect, anterograde and retrograde amnesia following hippocampal complex damage, and so forth.

</details>

### [Mamba in Speech: Towards an Alternative to Self-Attention](2405.12609.md)
**Xiangyu Zhang, Qiquan Zhang, Hexin Liu, Tianyi Xiao et al.** · 2024-05-21

<details>
<summary>Abstract</summary>

Transformer and its derivatives have achieved success in diverse tasks across computer vision, natural language processing, and speech processing. To reduce the complexity of computations within the multi-head self-attention mechanism in Transformer, Selective State Space Models (i.e., Mamba) were proposed as an alternative. Mamba exhibited its effectiveness in natural language processing and computer vision tasks, but its superiority has rarely been investigated in speech signal processing. This paper explores solutions for applying Mamba to speech processing by discussing two typical speech processing tasks: speech recognition, which requires semantic and sequential information, and speech enhancement, which focuses primarily on sequential patterns. The experimental results confirm that bidirectional Mamba (BiMamba) consistently outperforms vanilla Mamba, highlighting the advantages of a bidirectional design for speech processing. Moreover, experiments demonstrate the effectiveness of BiMamba as an alternative to the self-attention module in the Transformer model and its derivates, particularly for the semantic-aware task. The crucial technologies for transferring Mamba to speech are then summarized in ablation studies and the discussion section, offering insights for extending this research to a broader scope of tasks.

</details>

### [Continuous Sign Language Recognition with Adapted Conformer via Unsupervised Pretraining](2405.12018.md)
**Neena Aloysius, Geetha M, Prema Nedungadi** · 2024-05-20

<details>
<summary>Abstract</summary>

Conventional Deep Learning frameworks for continuous sign language recognition (CSLR) are comprised of a single or multi-modal feature extractor, a sequence-learning module, and a decoder for outputting the glosses. The sequence learning module is a crucial part wherein transformers have demonstrated their efficacy in the sequence-to-sequence tasks. Analyzing the research progress in the field of Natural Language Processing and Speech Recognition, a rapid introduction of various transformer variants is observed. However, in the realm of sign language, experimentation in the sequence learning component is limited. In this work, the state-of-the-art Conformer model for Speech Recognition is adapted for CSLR and the proposed model is termed ConSignformer. This marks the first instance of employing Conformer for a vision-based task. ConSignformer has bimodal pipeline of CNN as feature extractor and Conformer for sequence learning. For improved context learning we also introduce Cross-Modal Relative Attention (CMRA). By incorporating CMRA into the model, it becomes more adept at learning and utilizing complex relationships within the data. To further enhance the Conformer model, unsupervised pretraining called Regressional Feature Extraction is conducted on a curated sign language dataset. The pretrained Conformer is then fine-tuned for the downstream recognition task. The experimental results confirm the effectiveness of the adopted pretraining strategy and demonstrate how CMRA contributes to the recognition process. Remarkably, leveraging a Conformer-based backbone, our model achieves state-of-the-art performance on the benchmark datasets: PHOENIX-2014 and PHOENIX-2014T.

</details>

### [VR-GPT: Visual Language Model for Intelligent Virtual Reality Applications](2405.11537.md)
**Mikhail Konenkov, Artem Lykov, Daria Trinitatova, Dzmitry Tsetserukou** · 2024-05-19

<details>
<summary>Abstract</summary>

The advent of immersive Virtual Reality applications has transformed various domains, yet their integration with advanced artificial intelligence technologies like Visual Language Models remains underexplored. This study introduces a pioneering approach utilizing VLMs within VR environments to enhance user interaction and task efficiency. Leveraging the Unity engine and a custom-developed VLM, our system facilitates real-time, intuitive user interactions through natural language processing, without relying on visual text instructions. The incorporation of speech-to-text and text-to-speech technologies allows for seamless communication between the user and the VLM, enabling the system to guide users through complex tasks effectively. Preliminary experimental results indicate that utilizing VLMs not only reduces task completion times but also improves user comfort and task engagement compared to traditional VR interaction methods.

</details>

### [LeaPformer: Enabling Linear Transformers for Autoregressive and Simultaneous Tasks via Learned Proportions](2405.13046.md)
**Victor Agostinelli, Sanghyun Hong, Lizhong Chen** · 2024-05-18

<details>
<summary>Abstract</summary>

A promising approach to preserving model performance in linearized transformers is to employ position-based re-weighting functions. However, state-of-the-art re-weighting functions rely heavily on target sequence lengths, making it difficult or impossible to apply them to autoregressive and simultaneous tasks, where the target and sometimes even the input sequence length are unknown. To address this issue, we propose Learned Proportions (LeaP) and LeaPformers. Our contribution is built on two major components. First, we generalize the dependence on explicit positional representations and sequence lengths into dependence on sequence proportions for re-weighting. Second, we replace static positional representations with dynamic proportions derived via a compact module, enabling more flexible attention concentration patterns. We evaluate LeaPformer against eight representative efficient transformers on the Long-Range Arena benchmark, showing that LeaPformer achieves the best quality-throughput trade-off, as well as LeaPformer to Wikitext-103 autoregressive language modeling and simultaneous speech-to-text translation for two language pairs, achieving competitive results.

</details>

### [Acoustic modeling for Overlapping Speech Recognition: JHU Chime-5 Challenge System](2405.11078.md)
**Vimal Manohar, Szu-Jui Chen, Zhiqi Wang, Yusuke Fujita et al.** · 2024-05-17

<details>
<summary>Abstract</summary>

This paper summarizes our acoustic modeling efforts in the Johns Hopkins University speech recognition system for the CHiME-5 challenge to recognize highly-overlapped dinner party speech recorded by multiple microphone arrays. We explore data augmentation approaches, neural network architectures, front-end speech dereverberation, beamforming and robust i-vector extraction with comparisons of our in-house implementations and publicly available tools. We finally achieved a word error rate of 69.4% on the development set, which is a 11.7% absolute improvement over the previous baseline of 81.1%, and release this improved baseline with refined techniques/tools as an advanced CHiME-5 recipe.

</details>

### [Listen Again and Choose the Right Answer: A New Paradigm for Automatic Speech Recognition with Large Language Models](2405.10025.md)
**Yuchen Hu, Chen Chen, Chengwei Qin, Qiushi Zhu et al.** · 2024-05-16

<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have promoted generative error correction (GER) for automatic speech recognition (ASR), which aims to predict the ground-truth transcription from the decoded N-best hypotheses. Thanks to the strong language generation ability of LLMs and rich information in the N-best list, GER shows great effectiveness in enhancing ASR results. However, it still suffers from two limitations: 1) LLMs are unaware of the source speech during GER, which may lead to results that are grammatically correct but violate the source speech content, 2) N-best hypotheses usually only vary in a few tokens, making it redundant to send all of them for GER, which could confuse LLM about which tokens to focus on and thus lead to increased miscorrection. In this paper, we propose ClozeGER, a new paradigm for ASR generative error correction. First, we introduce a multimodal LLM (i.e., SpeechGPT) to receive source speech as extra input to improve the fidelity of correction output. Then, we reformat GER as a cloze test with logits calibration to remove the input information redundancy and simplify GER with clear instructions. Experiments show that ClozeGER achieves a new breakthrough over vanilla GER on 9 popular ASR datasets.

</details>

### [No More Mumbles: Enhancing Robot Intelligibility through Speech Adaptation](2405.09708.md)
**Qiaoqiao Ren, Yuanbo Hou, Dick Botteldooren, Tony Belpaeme** · 2024-05-15

<details>
<summary>Abstract</summary>

Spoken language interaction is at the heart of interpersonal communication, and people flexibly adapt their speech to different individuals and environments. It is surprising that robots, and by extension other digital devices, are not equipped to adapt their speech and instead rely on fixed speech parameters, which often hinder comprehension by the user. We conducted a speech comprehension study involving 39 participants who were exposed to different environmental and contextual conditions. During the experiment, the robot articulated words using different vocal parameters, and the participants were tasked with both recognising the spoken words and rating their subjective impression of the robot's speech. The experiment's primary outcome shows that spaces with good acoustic quality positively correlate with intelligibility and user experience. However, increasing the distance between the user and the robot exacerbated the user experience, while distracting background sounds significantly reduced speech recognition accuracy and user satisfaction. We next built an adaptive voice for the robot. For this, the robot needs to know how difficult it is for a user to understand spoken language in a particular setting. We present a prediction model that rates how annoying the ambient acoustic environment is and, consequentially, how hard it is to understand someone in this setting. Then, we develop a convolutional neural network model to adapt the robot's speech parameters to different users and spaces, while taking into account the influence of ambient acoustics on intelligibility. Finally, we present an evaluation with 27 users, demonstrating superior intelligibility and user experience with adaptive voice parameters compared to fixed voice.

</details>

### [Towards Evaluating the Robustness of Automatic Speech Recognition Systems via Audio Style Transfer](2405.09470.md)
**Weifei Jin, Yuxin Cao, Junjie Su, Qi Shen et al.** · 2024-05-15

<details>
<summary>Abstract</summary>

In light of the widespread application of Automatic Speech Recognition (ASR) systems, their security concerns have received much more attention than ever before, primarily due to the susceptibility of Deep Neural Networks. Previous studies have illustrated that surreptitiously crafting adversarial perturbations enables the manipulation of speech recognition systems, resulting in the production of malicious commands. These attack methods mostly require adding noise perturbations under $\ell_p$ norm constraints, inevitably leaving behind artifacts of manual modifications. Recent research has alleviated this limitation by manipulating style vectors to synthesize adversarial examples based on Text-to-Speech (TTS) synthesis audio. However, style modifications based on optimization objectives significantly reduce the controllability and editability of audio styles. In this paper, we propose an attack on ASR systems based on user-customized style transfer. We first test the effect of Style Transfer Attack (STA) which combines style transfer and adversarial attack in sequential order. And then, as an improvement, we propose an iterative Style Code Attack (SCA) to maintain audio quality. Experimental results show that our method can meet the need for user-customized styles and achieve a success rate of 82% in attacks, while keeping sound naturalness due to our user study.

</details>

### [Investigating the 'Autoencoder Behavior' in Speech Self-Supervised Models: a focus on HuBERT's Pretraining](2405.08402.md)
**Valentin Vielzeuf** · 2024-05-14

<details>
<summary>Abstract</summary>

Self-supervised learning has shown great success in Speech Recognition. However, it has been observed that finetuning all layers of the learned model leads to lower performance compared to resetting top layers. This phenomenon is attributed to the ''autoencoder'' behavior: top layers contain information closer to the input and are less suitable for tasks that require linguistic information, such as Speech Recognition.To better our understanding of this behavior, we propose to study the evolution of high-level information within the model during pretraining. We focus on the HuBERT model, which exhibits a less pronounced ''autoencoder'' behavior. By experimentally exploring various factors that may have an impact, we aim to improve the training procedure and enhance the top layers of HuBERT for high-level tasks.Furthermore, our experiments demonstrate that these improvements in the training procedure result in faster convergence and competitive performance on downstream tasks.

</details>

### [SpeechVerse: A Large-scale Generalizable Audio Language Model](2405.08295.md)
**Nilaksh Das, Saket Dingliwal, Srikanth Ronanki, Rohit Paturi et al.** · 2024-05-14

<details>
<summary>Abstract</summary>

Large language models (LLMs) have shown incredible proficiency in performing tasks that require semantic understanding of natural language instructions. Recently, many works have further expanded this capability to perceive multimodal audio and text inputs, but their capabilities are often limited to specific fine-tuned tasks such as automatic speech recognition and translation. We therefore develop SpeechVerse, a robust multi-task training and curriculum learning framework that combines pre-trained speech and text foundation models via a small set of learnable parameters, while keeping the pre-trained models frozen during training. The models are instruction finetuned using continuous latent representations extracted from the speech foundation model to achieve optimal zero-shot performance on a diverse range of speech processing tasks using natural language instructions. We perform extensive benchmarking that includes comparing our model performance against traditional baselines across several datasets and tasks. Furthermore, we evaluate the model's capability for generalized instruction following by testing on out-of-domain datasets, novel prompts, and unseen tasks. Our empirical experiments reveal that our multi-task SpeechVerse model is even superior to conventional task-specific baselines on 9 out of the 11 tasks.

</details>

### [Semantic MIMO Systems for Speech-to-Text Transmission](2405.08096.md)
**Zhenzi Weng, Zhijin Qin, Huiqiang Xie, Xiaoming Tao et al.** · 2024-05-13

<details>
<summary>Abstract</summary>

Semantic communications have been utilized to execute numerous intelligent tasks by transmitting task-related semantic information instead of bits. In this article, we propose a semantic-aware speech-to-text transmission system for the single-user multiple-input multiple-output (MIMO) and multi-user MIMO communication scenarios, named SAC-ST. Particularly, a semantic communication system to serve the speech-to-text task at the receiver is first designed, which compresses the semantic information and generates the low-dimensional semantic features by leveraging the transformer module. In addition, a novel semantic-aware network is proposed to facilitate transmission with high semantic fidelity by identifying the critical semantic information and guaranteeing its accurate recovery. Furthermore, we extend the SAC-ST with a neural network-enabled channel estimation network to mitigate the dependence on accurate channel state information and validate the feasibility of SAC-ST in practical communication environments. Simulation results will show that the proposed SAC-ST outperforms the communication framework without the semantic-aware network for speech-to-text transmission over the MIMO channels in terms of the speech-to-text metrics, especially in the low signal-to-noise regime. Moreover, the SAC-ST with the developed channel estimation network is comparable to the SAC-ST with perfect channel state information.

</details>

### [SoccerNet-Echoes: A Soccer Game Audio Commentary Dataset](2405.07354.md)
**Sushant Gautam, Mehdi Houshmand Sarkhoosh, Jan Held, Cise Midoglu et al.** · 2024-05-12

<details>
<summary>Abstract</summary>

The application of Automatic Speech Recognition (ASR) technology in soccer offers numerous opportunities for sports analytics. Specifically, extracting audio commentaries with ASR provides valuable insights into the events of the game, and opens the door to several downstream applications such as automatic highlight generation. This paper presents SoccerNet-Echoes, an augmentation of the SoccerNet dataset with automatically generated transcriptions of audio commentaries from soccer game broadcasts, enhancing video content with rich layers of textual information derived from the game audio using ASR. These textual commentaries, generated using the Whisper model and translated with Google Translate, extend the usefulness of the SoccerNet dataset in diverse applications such as enhanced action spotting, automatic caption generation, and game summarization. By incorporating textual data alongside visual and auditory content, SoccerNet-Echoes aims to serve as a comprehensive resource for the development of algorithms specialized in capturing the dynamics of soccer games. We detail the methods involved in the curation of this dataset and the integration of ASR. We also highlight the implications of a multimodal approach in sports analytics, and how the enriched dataset can support diverse applications, thus broadening the scope of research and development in the field of sports analytics.

</details>

### [Large Language Models for Education: A Survey](2405.13001.md)
**Hanyi Xu, Wensheng Gan, Zhenlian Qi, Jiayang Wu et al.** · 2024-05-12

<details>
<summary>Abstract</summary>

Artificial intelligence (AI) has a profound impact on traditional education. In recent years, large language models (LLMs) have been increasingly used in various applications such as natural language processing, computer vision, speech recognition, and autonomous driving. LLMs have also been applied in many fields, including recommendation, finance, government, education, legal affairs, and finance. As powerful auxiliary tools, LLMs incorporate various technologies such as deep learning, pre-training, fine-tuning, and reinforcement learning. The use of LLMs for smart education (LLMEdu) has been a significant strategic direction for countries worldwide. While LLMs have shown great promise in improving teaching quality, changing education models, and modifying teacher roles, the technologies are still facing several challenges. In this paper, we conduct a systematic review of LLMEdu, focusing on current technologies, challenges, and future developments. We first summarize the current state of LLMEdu and then introduce the characteristics of LLMs and education, as well as the benefits of integrating LLMs into education. We also review the process of integrating LLMs into the education industry, as well as the introduction of related technologies. Finally, we discuss the challenges and problems faced by LLMEdu, as well as prospects for future optimization of LLMEdu.

</details>

### [AraSpell: A Deep Learning Approach for Arabic Spelling Correction](2405.06981.md)
**Mahmoud Salhab, Faisal Abu-Khzam** · 2024-05-11

<details>
<summary>Abstract</summary>

Spelling correction is the task of identifying spelling mistakes, typos, and grammatical mistakes in a given text and correcting them according to their context and grammatical structure. This work introduces "AraSpell," a framework for Arabic spelling correction using different seq2seq model architectures such as Recurrent Neural Network (RNN) and Transformer with artificial data generation for error injection, trained on more than 6.9 Million Arabic sentences. Thorough experimental studies provide empirical evidence of the effectiveness of the proposed approach, which achieved 4.8% and 1.11% word error rate (WER) and character error rate (CER), respectively, in comparison with labeled data of 29.72% WER and 5.03% CER. Our approach achieved 2.9% CER and 10.65% WER in comparison with labeled data of 10.02% CER and 50.94% WER. Both of these results are obtained on a test set of 100K sentences.

</details>

### [An Investigation of Incorporating Mamba for Speech Enhancement](2405.06573.md)
**Rong Chao, Wen-Huang Cheng, Moreno La Quatra, Sabato Marco Siniscalchi et al.** · 2024-05-10

<details>
<summary>Abstract</summary>

This work aims to investigate the use of a recently proposed, attention-free, scalable state-space model (SSM), Mamba, for the speech enhancement (SE) task. In particular, we employ Mamba to deploy different regression-based SE models (SEMamba) with different configurations, namely basic, advanced, causal, and non-causal. Furthermore, loss functions either based on signal-level distances or metric-oriented are considered. Experimental evidence shows that SEMamba attains a competitive PESQ of 3.55 on the VoiceBank-DEMAND dataset with the advanced, non-causal configuration. A new state-of-the-art PESQ of 3.69 is also reported when SEMamba is combined with Perceptual Contrast Stretching (PCS). Compared against Transformed-based equivalent SE solutions, a noticeable FLOPs reduction up to ~12% is observed with the advanced non-causal configurations. Finally, SEMamba can be used as a pre-processing step before automatic speech recognition (ASR), showing competitive performance against recent SE solutions.

</details>

### [DP-DyLoRA: Fine-Tuning Transformer-Based Models On-Device under Differentially Private Federated Learning using Dynamic Low-Rank Adaptation](2405.06368.md)
**Jie Xu, Karthikeyan Saravanan, Rogier van Dalen, Haaris Mehmood et al.** · 2024-05-10

<details>
<summary>Abstract</summary>

Federated learning (FL) allows clients to collaboratively train a global model without sharing their local data with a server. However, clients' contributions to the server can still leak sensitive information. Differential privacy (DP) addresses such leakage by providing formal privacy guarantees, with mechanisms that add randomness to the clients' contributions. The randomness makes it infeasible to train large transformer-based models, common in modern federated learning systems. In this work, we empirically evaluate the practicality of fine-tuning large scale on-device transformer-based models with differential privacy in a federated learning system. We conduct comprehensive experiments on various system properties for tasks spanning a multitude of domains: speech recognition, computer vision (CV) and natural language understanding (NLU). Our results show that full fine-tuning under differentially private federated learning (DP-FL) generally leads to huge performance degradation which can be alleviated by reducing the dimensionality of contributions through parameter-efficient fine-tuning (PEFT). Our benchmarks of existing DP-PEFT methods show that DP-Low-Rank Adaptation (DP-LoRA) consistently outperforms other methods. An even more promising approach, DyLoRA, which makes the low rank variable, when naively combined with FL would straightforwardly break differential privacy. We therefore propose an adaptation method that can be combined with differential privacy and call it DP-DyLoRA. Finally, we are able to reduce the accuracy degradation and word error rate (WER) increase due to DP to less than 2% and 7% respectively with 1 million clients and a stringent privacy budget of $ε=2$.

</details>

### [The RoyalFlush Automatic Speech Diarization and Recognition System for In-Car Multi-Channel Automatic Speech Recognition Challenge](2405.05498.md)
**Jingguang Tian, Shuaishuai Ye, Shunfei Chen, Yang Xiang et al.** · 2024-05-09

<details>
<summary>Abstract</summary>

This paper presents our system submission for the In-Car Multi-Channel Automatic Speech Recognition (ICMC-ASR) Challenge, which focuses on speaker diarization and speech recognition in complex multi-speaker scenarios. To address these challenges, we develop end-to-end speaker diarization models that notably decrease the diarization error rate (DER) by 49.58\% compared to the official baseline on the development set. For speech recognition, we utilize self-supervised learning representations to train end-to-end ASR models. By integrating these models, we achieve a character error rate (CER) of 16.93\% on the track 1 evaluation set, and a concatenated minimum permutation character error rate (cpCER) of 25.88\% on the track 2 evaluation set.

</details>

### [Open Implementation and Study of BEST-RQ for Speech Processing](2405.04296.md)
**Ryan Whetten, Titouan Parcollet, Marco Dinarelli, Yannick Estève** · 2024-05-07

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) has proven to be useful in various speech tasks. However, these methods are generally very demanding in terms of data, memory, and computational resources. BERT-based Speech pre-Training with Random-projection Quantizer (BEST-RQ), is an SSL method that has shown great performance on Automatic Speech Recognition (ASR) while being simpler than other SSL methods, such as wav2vec 2.0. Despite BEST-RQ's great performance, details are lacking in the original paper, such as the amount of GPU/TPU hours used in pre-training, and there is no official easy-to-use open-source implementation. Furthermore, BEST-RQ has not been evaluated on other downstream tasks aside from ASR and speech translation. In this work, we describe a re-implementation of a Random-projection quantizer and perform a preliminary study with a comparison to wav2vec 2.0 on four downstream tasks. We discuss the details and differences of our implementation. We show that a random projection quantizer can achieve similar downstream performance as wav2vec 2.0 while decreasing training time by over a factor of two.

</details>

### [Whispy: Adapting STT Whisper Models to Real-Time Environments](2405.03484.md)
**Antonio Bevilacqua, Paolo Saviano, Alessandro Amirante, Simon Pietro Romano** · 2024-05-06

<details>
<summary>Abstract</summary>

Large general-purpose transformer models have recently become the mainstay in the realm of speech analysis. In particular, Whisper achieves state-of-the-art results in relevant tasks such as speech recognition, translation, language identification, and voice activity detection. However, Whisper models are not designed to be used in real-time conditions, and this limitation makes them unsuitable for a vast plethora of practical applications. In this paper, we introduce Whispy, a system intended to bring live capabilities to the Whisper pretrained models. As a result of a number of architectural optimisations, Whispy is able to consume live audio streams and generate high level, coherent voice transcriptions, while still maintaining a low computational cost. We evaluate the performance of our system on a large repository of publicly available speech datasets, investigating how the transcription mechanism introduced by Whispy impacts on the Whisper output. Experimental results show how Whispy excels in robustness, promptness, and accuracy.

</details>

### [MMGER: Multi-modal and Multi-granularity Generative Error Correction with LLM for Joint Accent and Speech Recognition](2405.03152.md)
**Bingshen Mu, Yangze Li, Qijie Shao, Kun Wei et al.** · 2024-05-06

<details>
<summary>Abstract</summary>

Despite notable advancements in automatic speech recognition (ASR), performance tends to degrade when faced with adverse conditions. Generative error correction (GER) leverages the exceptional text comprehension capabilities of large language models (LLM), delivering impressive performance in ASR error correction, where N-best hypotheses provide valuable information for transcription prediction. However, GER encounters challenges such as fixed N-best hypotheses, insufficient utilization of acoustic information, and limited specificity to multi-accent scenarios. In this paper, we explore the application of GER in multi-accent scenarios. Accents represent deviations from standard pronunciation norms, and the multi-task learning framework for simultaneous ASR and accent recognition (AR) has effectively addressed the multi-accent scenarios, making it a prominent solution. In this work, we propose a unified ASR-AR GER model, named MMGER, leveraging multi-modal correction, and multi-granularity correction. Multi-task ASR-AR learning is employed to provide dynamic 1-best hypotheses and accent embeddings. Multi-modal correction accomplishes fine-grained frame-level correction by force-aligning the acoustic features of speech with the corresponding character-level 1-best hypothesis sequence. Multi-granularity correction supplements the global linguistic information by incorporating regular 1-best hypotheses atop fine-grained multi-modal correction to achieve coarse-grained utterance-level correction. MMGER effectively mitigates the limitations of GER and tailors LLM-based ASR error correction for the multi-accent scenarios. Experiments conducted on the multi-accent Mandarin KeSpeech dataset demonstrate the efficacy of MMGER, achieving a 26.72% relative improvement in AR accuracy and a 27.55% relative reduction in ASR character error rate, compared to a well-established standard baseline.

</details>

### [Combining X-Vectors and Bayesian Batch Active Learning: Two-Stage Active Learning Pipeline for Speech Recognition](2406.02566.md)
**Ognjen Kundacina, Vladimir Vincan, Dragisa Miskovic** · 2024-05-03

<details>
<summary>Abstract</summary>

This paper introduces a novel two-stage active learning (AL) pipeline for automatic speech recognition (ASR), combining unsupervised and supervised AL methods. The first stage utilizes unsupervised AL by using x-vectors clustering for diverse sample selection from unlabeled speech data, thus establishing a robust initial dataset for the subsequent supervised AL. The second stage incorporates a supervised AL strategy, with a batch AL method specifically developed for ASR, aimed at selecting diverse and informative batches of samples. Here, sample diversity is also achieved using x-vectors clustering, while the most informative samples are identified using a Bayesian AL method tailored for ASR with an adaptation of Monte Carlo dropout to approximate Bayesian inference. This approach enables precise uncertainty estimation, thereby enhancing ASR model training with significantly reduced data requirements. Our method has shown superior performance compared to competing methods on homogeneous, heterogeneous, and OOD test sets, demonstrating that strategic sample selection and innovative Bayesian modeling can substantially optimize both labeling effort and data utilization in deep learning-based ASR applications.

</details>

### [Unveiling the Potential of LLM-Based ASR on Chinese Open-Source Datasets](2405.02132.md)
**Xuelong Geng, Tianyi Xu, Kun Wei, Bingshen Mu et al.** · 2024-05-03

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated unparalleled effectiveness in various NLP tasks, and integrating LLMs with automatic speech recognition (ASR) is becoming a mainstream paradigm. Building upon this momentum, our research delves into an in-depth examination of this paradigm on a large open-source Chinese dataset. Specifically, our research aims to evaluate the impact of various configurations of speech encoders, LLMs, and projector modules in the context of the speech foundation encoder-LLM ASR paradigm. Furthermore, we introduce a three-stage training approach, expressly developed to enhance the model's ability to align auditory and textual information. The implementation of this approach, alongside the strategic integration of ASR components, enabled us to achieve the SOTA performance on the AISHELL-1, Test_Net, and Test_Meeting test sets. Our analysis presents an empirical foundation for future research in LLM-based ASR systems and offers insights into optimizing performance using Chinese datasets. We will publicly release all scripts used for data preparation, training, inference, and scoring, as well as pre-trained models and training logs to promote reproducible research.

</details>

### [Sequence-to-sequence models in peer-to-peer learning: A practical application](2406.02565.md)
**Robert Šajina, Ivo Ipšić** · 2024-05-02

<details>
<summary>Abstract</summary>

This paper explores the applicability of sequence-to-sequence (Seq2Seq) models based on LSTM units for Automatic Speech Recognition (ASR) task within peer-to-peer learning environments. Leveraging two distinct peer-to-peer learning methods, the study simulates the learning process of agents and evaluates their performance in ASR task using two different ASR datasets. In a centralized training setting, utilizing a scaled-down variant of the Deep Speech 2 model, a single model achieved a Word Error Rate (WER) of 84\% when trained on the UserLibri dataset, and 38\% when trained on the LJ Speech dataset. Conversely, in a peer-to-peer learning scenario involving 55 agents, the WER ranged from 87\% to 92\% for the UserLibri dataset, and from 52\% to 56\% for the LJ Speech dataset. The findings demonstrate the feasibility of employing Seq2Seq models in decentralized settings, albeit with slightly higher Word Error Rates (WER) compared to centralized training methods.

</details>

### [Low-resource speech recognition and dialect identification of Irish in a multi-task framework](2405.01293.md)
**Liam Lonergan, Mengjie Qian, Neasa Ní Chiaráin, Christer Gobl et al.** · 2024-05-02

<details>
<summary>Abstract</summary>

This paper explores the use of Hybrid CTC/Attention encoder-decoder models trained with Intermediate CTC (InterCTC) for Irish (Gaelic) low-resource speech recognition (ASR) and dialect identification (DID). Results are compared to the current best performing models trained for ASR (TDNN-HMM) and DID (ECAPA-TDNN). An optimal InterCTC setting is initially established using a Conformer encoder. This setting is then used to train a model with an E-branchformer encoder and the performance of both architectures are compared. A multi-task fine-tuning approach is adopted for language model (LM) shallow fusion. The experiments yielded an improvement in DID accuracy of 10.8% relative to a baseline ECAPA-TDNN, and WER performance approaching the TDNN-HMM model. This multi-task approach emerges as a promising strategy for Irish low-resource ASR and DID.

</details>

### [Deep Learning Models in Speech Recognition: Measuring GPU Energy Consumption, Impact of Noise and Model Quantization for Edge Deployment](2405.01004.md)
**Aditya Chakravarty** · 2024-05-02

<details>
<summary>Abstract</summary>

Recent transformer-based ASR models have achieved word-error rates (WER) below 4%, surpassing human annotator accuracy, yet they demand extensive server resources, contributing to significant carbon footprints. The traditional server-based architecture of ASR also presents privacy concerns, alongside reliability and latency issues due to network dependencies. In contrast, on-device (edge) ASR enhances privacy, boosts performance, and promotes sustainability by effectively balancing energy use and accuracy for specific applications. This study examines the effects of quantization, memory demands, and energy consumption on the performance of various ASR model inference on the NVIDIA Jetson Orin Nano. By analyzing WER and transcription speed across models using FP32, FP16, and INT8 quantization on clean and noisy datasets, we highlight the crucial trade-offs between accuracy, speeds, quantization, energy efficiency, and memory needs. We found that changing precision from fp32 to fp16 halves the energy consumption for audio transcription across different models, with minimal performance degradation. A larger model size and number of parameters neither guarantees better resilience to noise, nor predicts the energy consumption for a given transcription load. These, along with several other findings offer novel insights for optimizing ASR systems within energy- and memory-limited environments, crucial for the development of efficient on-device ASR solutions. The code and input data needed to reproduce the results in this article are open sourced are available on [https://github.com/zzadiues3338/ASR-energy-jetson].

</details>

### [Efficient Compression of Multitask Multilingual Speech Models](2405.00966.md)
**Thomas Palmeira Ferraz** · 2024-05-02

<details>
<summary>Abstract</summary>

Whisper is a multitask and multilingual speech model covering 99 languages. It yields commendable automatic speech recognition (ASR) results in a subset of its covered languages, but the model still underperforms on a non-negligible number of under-represented languages, a problem exacerbated in smaller model versions. In this work, we examine its limitations, demonstrating the presence of speaker-related (gender, age) and model-related (resourcefulness and model size) bias. Despite that, we show that only model-related bias are amplified by quantization, impacting more low-resource languages and smaller models. Searching for a better compression approach, we propose DistilWhisper, an approach that is able to bridge the performance gap in ASR for these languages while retaining the advantages of multitask and multilingual capabilities. Our approach involves two key strategies: lightweight modular ASR fine-tuning of whisper-small using language-specific experts, and knowledge distillation from whisper-large-v2. This dual approach allows us to effectively boost ASR performance while keeping the robustness inherited from the multitask and multilingual pre-training. Results demonstrate that our approach is more effective than standard fine-tuning or LoRA adapters, boosting performance in the targeted languages for both in- and out-of-domain test sets, while introducing only a negligible parameter overhead at inference.

</details>

### [A Toolchain for Comprehensive Audio/Video Analysis Using Deep Learning Based Multimodal Approach (A use case of riot or violent context detection)](2407.03110.md)
**Lam Pham, Phat Lam, Tin Nguyen, Hieu Tang et al.** · 2024-05-02

<details>
<summary>Abstract</summary>

In this paper, we present a toolchain for a comprehensive audio/video analysis by leveraging deep learning based multimodal approach. To this end, different specific tasks of Speech to Text (S2T), Acoustic Scene Classification (ASC), Acoustic Event Detection (AED), Visual Object Detection (VOD), Image Captioning (IC), and Video Captioning (VC) are conducted and integrated into the toolchain. By combining individual tasks and analyzing both audio \& visual data extracted from input video, the toolchain offers various audio/video-based applications: Two general applications of audio/video clustering, comprehensive audio/video summary and a specific application of riot or violent context detection. Furthermore, the toolchain presents a flexible and adaptable architecture that is effective to integrate new models for further audio/video-based applications.

</details>

### [Efficient Sample-Specific Encoder Perturbations](2405.01601.md)
**Yassir Fathullah, Mark J. F. Gales** · 2024-05-01

<details>
<summary>Abstract</summary>

Encoder-decoder foundation models have displayed state-of-the-art performance on a range of autoregressive sequence tasks. This paper proposes a simple and lightweight modification to such systems to control the behaviour according to a specific attribute of interest. This paper proposes a novel inference-efficient approach to modifying the behaviour of an encoder-decoder system according to a specific attribute of interest. Specifically, we show that a small proxy network can be used to find a sample-by-sample perturbation of the encoder output of a frozen foundation model to trigger the decoder to generate improved decodings. This work explores a specific realization of this framework focused on improving the COMET performance of Flan-T5 on Machine Translation and the WER of Whisper foundation models on Speech Recognition. Results display consistent improvements in performance evaluated through COMET and WER respectively. Furthermore, experiments also show that the proxies are robust to the exact nature of the data used to train them and can extend to other domains.

</details>

### [EfficientASR: Speech Recognition Network Compression via Attention Redundancy and Chunk-Level FFN Optimization](2404.19214.md)
**Jianzong Wang, Ziqi Liang, Xulong Zhang, Ning Cheng et al.** · 2024-04-30

<details>
<summary>Abstract</summary>

In recent years, Transformer networks have shown remarkable performance in speech recognition tasks. However, their deployment poses challenges due to high computational and storage resource requirements. To address this issue, a lightweight model called EfficientASR is proposed in this paper, aiming to enhance the versatility of Transformer models. EfficientASR employs two primary modules: Shared Residual Multi-Head Attention (SRMHA) and Chunk-Level Feedforward Networks (CFFN). The SRMHA module effectively reduces redundant computations in the network, while the CFFN module captures spatial knowledge and reduces the number of parameters. The effectiveness of the EfficientASR model is validated on two public datasets, namely Aishell-1 and HKUST. Experimental results demonstrate a 36% reduction in parameters compared to the baseline Transformer network, along with improvements of 0.3% and 0.2% in Character Error Rate (CER) on the Aishell-1 and HKUST datasets, respectively.

</details>

### [Towards Dog Bark Decoding: Leveraging Human Speech Processing for Automated Bark Classification](2404.18739.md)
**Artem Abzaliev, Humberto Pérez Espinosa, Rada Mihalcea** · 2024-04-29

<details>
<summary>Abstract</summary>

Similar to humans, animals make extensive use of verbal and non-verbal forms of communication, including a large range of audio signals. In this paper, we address dog vocalizations and explore the use of self-supervised speech representation models pre-trained on human speech to address dog bark classification tasks that find parallels in human-centered tasks in speech recognition. We specifically address four tasks: dog recognition, breed identification, gender classification, and context grounding. We show that using speech embedding representations significantly improves over simpler classification baselines. Further, we also find that models pre-trained on large human speech acoustics can provide additional performance boosts on several tasks.

</details>

### [A cost minimization approach to fix the vocabulary size in a tokenizer for an End-to-End ASR system](2406.02563.md)
**Sunil Kumar Kopparapu, Ashish Panda** · 2024-04-29

<details>
<summary>Abstract</summary>

Unlike hybrid speech recognition systems where the use of tokens was restricted to phones, biphones or triphones the choice of tokens in the end-to-end ASR systems is derived from the text corpus of the training data. The use of tokenization algorithms like Byte Pair Encoding (BPE) and WordPiece is popular in identifying the tokens that are used in the overall training process of the speech recognition system. Popular toolkits, like ESPNet use a pre-defined vocabulary size (number of tokens) for these tokenization algorithms, but there is no discussion on how vocabulary size was derived. In this paper, we build a cost function, assuming the tokenization process to be a black-box to enable choosing the number of tokens which might most benefit building an end-to-end ASR. We show through experiments on LibriSpeech 100 hour set that the performance of an end-to-end ASR system improves when the number of tokens are chosen carefully.

</details>

### [Child Speech Recognition in Human-Robot Interaction: Problem Solved?](2404.17394.md)
**Ruben Janssens, Eva Verhelst, Giulio Antonio Abbo, Qiaoqiao Ren et al.** · 2024-04-26

<details>
<summary>Abstract</summary>

Automated Speech Recognition shows superhuman performance for adult English speech on a range of benchmarks, but disappoints when fed children's speech. This has long sat in the way of child-robot interaction. Recent evolutions in data-driven speech recognition, including the availability of Transformer architectures and unprecedented volumes of training data, might mean a breakthrough for child speech recognition and social robot applications aimed at children. We revisit a study on child speech recognition from 2017 and show that indeed performance has increased, with newcomer OpenAI Whisper doing markedly better than leading commercial cloud services. Performance improves even more in highly structured interactions when priming models with specific phrases. While transcription is not perfect yet, the best model recognises 60.3% of sentences correctly barring small grammatical differences, with sub-second transcription time running on a local GPU, showing potential for usable autonomous child-robot speech interactions.

</details>

### [Alice's Adventures in a Differentiable Wonderland -- Volume I, A Tour of the Land](2404.17625.md)
**Simone Scardapane** · 2024-04-26

<details>
<summary>Abstract</summary>

Neural networks surround us, in the form of large language models, speech transcription systems, molecular discovery algorithms, robotics, and much more. Stripped of anything else, neural networks are compositions of differentiable primitives, and studying them means learning how to program and how to interact with these models, a particular example of what is called differentiable programming. This primer is an introduction to this fascinating field imagined for someone, like Alice, who has just ventured into this strange differentiable wonderland. I overview the basics of optimizing a function via automatic differentiation, and a selection of the most common designs for handling sequences, graphs, texts, and audios. The focus is on a intuitive, self-contained introduction to the most important design techniques, including convolutional, attentional, and recurrent blocks, hoping to bridge the gap between theory and code (PyTorch and JAX) and leaving the reader capable of understanding some of the most advanced models out there, such as large language models (LLMs) and multimodal architectures.

</details>

### [U2++ MoE: Scaling 4.7x parameters with minimal impact on RTF](2404.16407.md)
**Xingchen Song, Di Wu, Binbin Zhang, Dinghao Zhou et al.** · 2024-04-25

<details>
<summary>Abstract</summary>

Scale has opened new frontiers in natural language processing, but at a high cost. In response, by learning to only activate a subset of parameters in training and inference, Mixture-of-Experts (MoE) have been proposed as an energy efficient path to even larger and more capable language models and this shift towards a new generation of foundation models is gaining momentum, particularly within the field of Automatic Speech Recognition (ASR). Recent works that incorporating MoE into ASR models have complex designs such as routing frames via supplementary embedding network, improving multilingual ability for the experts, and utilizing dedicated auxiliary losses for either expert load balancing or specific language handling. We found that delicate designs are not necessary, while an embarrassingly simple substitution of MoE layers for all Feed-Forward Network (FFN) layers is competent for the ASR task. To be more specific, we benchmark our proposed model on a large scale inner-source dataset (160k hours), the results show that we can scale our baseline Conformer (Dense-225M) to its MoE counterparts (MoE-1B) and achieve Dense-1B level Word Error Rate (WER) while maintaining a Dense-225M level Real Time Factor (RTF). Furthermore, by applying Unified 2-pass framework with bidirectional attention decoders (U2++), we achieve the streaming and non-streaming decoding modes in a single MoE based model, which we call U2++ MoE. We hope that our study can facilitate the research on scaling speech foundation models without sacrificing deployment efficiency.

</details>

### [Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling: Methods, Applications, and Challenges](2404.16112.md)
**Badri Narayana Patro, Vijay Srinivas Agneeswaran** · 2024-04-24

<details>
<summary>Abstract</summary>

Sequence modeling is a crucial area across various domains, including Natural Language Processing (NLP), speech recognition, time series forecasting, music generation, and bioinformatics. Recurrent Neural Networks (RNNs) and Long Short Term Memory Networks (LSTMs) have historically dominated sequence modeling tasks like Machine Translation, Named Entity Recognition (NER), etc. However, the advancement of transformers has led to a shift in this paradigm, given their superior performance. Yet, transformers suffer from $O(N^2)$ attention complexity and challenges in handling inductive bias. Several variations have been proposed to address these issues which use spectral networks or convolutions and have performed well on a range of tasks. However, they still have difficulty in dealing with long sequences. State Space Models(SSMs) have emerged as promising alternatives for sequence modeling paradigms in this context, especially with the advent of S4 and its variants, such as S4nd, Hippo, Hyena, Diagnol State Spaces (DSS), Gated State Spaces (GSS), Linear Recurrent Unit (LRU), Liquid-S4, Mamba, etc. In this survey, we categorize the foundational SSMs based on three paradigms namely, Gating architectures, Structural architectures, and Recurrent architectures. This survey also highlights diverse applications of SSMs across domains such as vision, video, audio, speech, language (especially long sequence modeling), medical (including genomics), chemical (like drug design), recommendation systems, and time series analysis, including tabular data. Moreover, we consolidate the performance of SSMs on benchmark datasets like Long Range Arena (LRA), WikiText, Glue, Pile, ImageNet, Kinetics-400, sstv2, as well as video datasets such as Breakfast, COIN, LVU, and various time series datasets. The project page for Mamba-360 work is available on this webpage.\url{https://github.com/badripatro/mamba360}.

</details>

### [Gated Low-rank Adaptation for personalized Code-Switching Automatic Speech Recognition on the low-spec devices](2406.02562.md)
**Gwantae Kim, Bokyeung Lee, Donghyeon Kim, Hanseok Ko** · 2024-04-24

<details>
<summary>Abstract</summary>

In recent times, there has been a growing interest in utilizing personalized large models on low-spec devices, such as mobile and CPU-only devices. However, utilizing a personalized large model in the on-device is inefficient, and sometimes limited due to computational cost. To tackle the problem, this paper presents the weights separation method to minimize on-device model weights using parameter-efficient fine-tuning methods. Moreover, some people speak multiple languages in an utterance, as known as code-switching, the personalized ASR model is necessary to address such cases. However, current multilingual speech recognition models are limited to recognizing a single language within each utterance. To tackle this problem, we propose code-switching speech recognition models that incorporate fine-tuned monolingual and multilingual speech recognition models. Additionally, we introduce a gated low-rank adaptation(GLoRA) for parameter-efficient fine-tuning with minimal performance degradation. Our experiments, conducted on Korean-English code-switching datasets, demonstrate that fine-tuning speech recognition models for code-switching surpasses the performance of traditional code-switching speech recognition models trained from scratch. Furthermore, GLoRA enhances parameter-efficient fine-tuning performance compared to conventional LoRA.

</details>

### [Breaking Walls: Pioneering Automatic Speech Recognition for Central Kurdish: End-to-End Transformer Paradigm](2406.02561.md)
**Abdulhady Abas Abdullah, Hadi Veisi, Tarik Rashid** · 2024-04-23

<details>
<summary>Abstract</summary>

End-to-end transformer-based models epitomize the cutting-edge in Automatic Speech Recognition (ASR) systems. Despite their substantial benefits, these models demand extensive training data to perform optimally, presenting a significant challenge for low-resource languages such as Central Kurdish. Addressing this issue requires innovative methods and techniques. This paper aims to develop an ASR system for Intermediate Kurdish by collecting a robust corpus of speech, using the N-GRAM language model, and utilizing an external Kurdish tokenizer for refinement and integration techniques to enhance the model's performance. We collect a comprehensive 100-hour speech corpus from diverse sources. Additionally, applied fine-tuning techniques to our speech corpus on Persian, English, and Arabic pre-trained models, specifically utilizing the xls-r-300m, xls-r-1b, and xls-r-2b Wav2vec 2.0 models. And utilized language models trained by 3-gram and 4-gram from a large text corpus of 300 million tokens. The fine-tuned xls-r-2b model, combined with a 3-gram language model and included external Kurdish tokenizer, achieved the best performance, yielding a Word Error Rate (WER) of 10.0% on the validation set and 11.8% on the Asosoft test set. The ASR model has demonstrated the advantages of having a large vocabulary compared to the existing Kurdish ASR models. Compared to other models, it produced more accurate and higher performance outcomes by working with a lower error rate.

</details>

### [Exploring neural oscillations during speech perception via surrogate gradient spiking neural networks](2404.14024.md)
**Alexandre Bittar, Philip N. Garner** · 2024-04-22

<details>
<summary>Abstract</summary>

Understanding cognitive processes in the brain demands sophisticated models capable of replicating neural dynamics at large scales. We present a physiologically inspired speech recognition architecture, compatible and scalable with deep learning frameworks, and demonstrate that end-to-end gradient descent training leads to the emergence of neural oscillations in the central spiking neural network. Significant cross-frequency couplings, indicative of these oscillations, are measured within and across network layers during speech processing, whereas no such interactions are observed when handling background noise inputs. Furthermore, our findings highlight the crucial inhibitory role of feedback mechanisms, such as spike frequency adaptation and recurrent connections, in regulating and synchronising neural activity to improve recognition performance. Overall, on top of developing our understanding of synchronisation phenomena notably observed in the human auditory pathway, our architecture exhibits dynamic and efficient information processing, with relevance to neuromorphic technology.

</details>

### [Semantically Corrected Amharic Automatic Speech Recognition](2404.13362.md)
**Samuael Adnew, Paul Pu Liang** · 2024-04-20

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) can play a crucial role in enhancing the accessibility of spoken languages worldwide. In this paper, we build a set of ASR tools for Amharic, a language spoken by more than 50 million people primarily in eastern Africa. Amharic is written in the Ge'ez script, a sequence of graphemes with spacings denoting word boundaries. This makes computational processing of Amharic challenging since the location of spacings can significantly impact the meaning of formed sentences. We find that existing benchmarks for Amharic ASR do not account for these spacings and only measure individual grapheme error rates, leading to significantly inflated measurements of in-the-wild performance. In this paper, we first release corrected transcriptions of existing Amharic ASR test datasets, enabling the community to accurately evaluate progress. Furthermore, we introduce a post-processing approach using a transformer encoder-decoder architecture to organize raw ASR outputs into a grammatically complete and semantically meaningful Amharic sentence. Through experiments on the corrected test dataset, our model enhances the semantic correctness of Amharic speech recognition systems, achieving a Character Error Rate (CER) of 5.5\% and a Word Error Rate (WER) of 23.3\%.

</details>

### [Efficient infusion of self-supervised representations in Automatic Speech Recognition](2404.12628.md)
**Darshan Prabhu, Sai Ganesh Mirishkar, Pankaj Wasnik** · 2024-04-19

<details>
<summary>Abstract</summary>

Self-supervised learned (SSL) models such as Wav2vec and HuBERT yield state-of-the-art results on speech-related tasks. Given the effectiveness of such models, it is advantageous to use them in conventional ASR systems. While some approaches suggest incorporating these models as a trainable encoder or a learnable frontend, training such systems is extremely slow and requires a lot of computation cycles. In this work, we propose two simple approaches that use (1) framewise addition and (2) cross-attention mechanisms to efficiently incorporate the representations from the SSL model(s) into the ASR architecture, resulting in models that are comparable in size with standard encoder-decoder conformer systems while also avoiding the usage of SSL models during training. Our approach results in faster training and yields significant performance gains on the Librispeech and Tedlium datasets compared to baselines. We further provide detailed analysis and ablation studies that demonstrate the effectiveness of our approach.

</details>

### [Artificial Neural Networks to Recognize Speakers Division from Continuous Bengali Speech](2404.15168.md)
**Hasmot Ali, Md. Fahad Hossain, Md. Mehedi Hasan, Sheikh Abujar et al.** · 2024-04-18

<details>
<summary>Abstract</summary>

Voice based applications are ruling over the era of automation because speech has a lot of factors that determine a speakers information as well as speech. Modern Automatic Speech Recognition (ASR) is a blessing in the field of Human-Computer Interaction (HCI) for efficient communication among humans and devices using Artificial Intelligence technology. Speech is one of the easiest mediums of communication because it has a lot of identical features for different speakers. Nowadays it is possible to determine speakers and their identity using their speech in terms of speaker recognition. In this paper, we presented a method that will provide a speakers geographical identity in a certain region using continuous Bengali speech. We consider eight different divisions of Bangladesh as the geographical region. We applied the Mel Frequency Cepstral Coefficient (MFCC) and Delta features on an Artificial Neural Network to classify speakers division. We performed some preprocessing tasks like noise reduction and 8-10 second segmentation of raw audio before feature extraction. We used our dataset of more than 45 hours of audio data from 633 individual male and female speakers. We recorded the highest accuracy of 85.44%.

</details>

### [Simultaneous Interpretation Corpus Construction by Large Language Models in Distant Language Pair](2404.12299.md)
**Yusuke Sakai, Mana Makinae, Hidetaka Kamigaito, Taro Watanabe** · 2024-04-18

<details>
<summary>Abstract</summary>

In Simultaneous Machine Translation (SiMT) systems, training with a simultaneous interpretation (SI) corpus is an effective method for achieving high-quality yet low-latency systems. However, it is very challenging to curate such a corpus due to limitations in the abilities of annotators, and hence, existing SI corpora are limited. Therefore, we propose a method to convert existing speech translation corpora into interpretation-style data, maintaining the original word order and preserving the entire source content using Large Language Models (LLM-SI-Corpus). We demonstrate that fine-tuning SiMT models in text-to-text and speech-to-text settings with the LLM-SI-Corpus reduces latencies while maintaining the same level of quality as the models trained with offline datasets. The LLM-SI-Corpus is available at \url{https://github.com/yusuke1997/LLM-SI-Corpus}.

</details>

### [Teaching a Multilingual Large Language Model to Understand Multilingual Speech via Multi-Instructional Training](2404.10922.md)
**Pavel Denisov, Ngoc Thang Vu** · 2024-04-16

<details>
<summary>Abstract</summary>

Recent advancements in language modeling have led to the emergence of Large Language Models (LLMs) capable of various natural language processing tasks. Despite their success in text-based tasks, applying LLMs to the speech domain remains limited and challenging. This paper presents BLOOMZMMS, a novel model that integrates a multilingual LLM with a multilingual speech encoder, aiming to harness the capabilities of LLMs for speech recognition and beyond. Utilizing a multi-instructional training approach, we demonstrate the transferability of linguistic knowledge from the text to the speech modality. Our experiments, conducted on 1900 hours of transcribed data from 139 languages, establish that a multilingual speech representation can be effectively learned and aligned with a multilingual LLM. While this learned representation initially shows limitations in task generalization, we address this issue by generating synthetic targets in a multi-instructional style. Our zero-shot evaluation results confirm the robustness of our approach across multiple tasks, including speech translation and multilingual spoken language understanding, thereby opening new avenues for applying LLMs in the speech domain.

</details>

### [Anatomy of Industrial Scale Multilingual ASR](2404.09841.md)
**Francis McCann Ramirez, Luka Chkhetiani, Andrew Ehrenberg, Robert McHardy et al.** · 2024-04-15

<details>
<summary>Abstract</summary>

This paper describes AssemblyAI's industrial-scale automatic speech recognition (ASR) system, designed to meet the requirements of large-scale, multilingual ASR serving various application needs. Our system leverages a diverse training dataset comprising unsupervised (12.5M hours), supervised (188k hours), and pseudo-labeled (1.6M hours) data across four languages. We provide a detailed description of our model architecture, consisting of a full-context 600M-parameter Conformer encoder pre-trained with BEST-RQ and an RNN-T decoder fine-tuned jointly with the encoder. Our extensive evaluation demonstrates competitive word error rates (WERs) against larger and more computationally expensive models, such as Whisper large and Canary-1B. Furthermore, our architectural choices yield several key advantages, including an improved code-switching capability, a 5x inference speedup compared to an optimized Whisper baseline, a 30% reduction in hallucination rate on speech data, and a 90% reduction in ambient noise compared to Whisper, along with significantly improved time-stamp accuracy. Throughout this work, we adopt a system-centric approach to analyzing various aspects of fully-fledged ASR models to gain practically relevant insights useful for real-world services operating at scale.

</details>

### [Deferred NAM: Low-latency Top-K Context Injection via Deferred Context Encoding for Non-Streaming ASR](2404.10180.md)
**Zelin Wu, Gan Song, Christopher Li, Pat Rondon et al.** · 2024-04-15

<details>
<summary>Abstract</summary>

Contextual biasing enables speech recognizers to transcribe important phrases in the speaker's context, such as contact names, even if they are rare in, or absent from, the training data. Attention-based biasing is a leading approach which allows for full end-to-end cotraining of the recognizer and biasing system and requires no separate inference-time components. Such biasers typically consist of a context encoder; followed by a context filter which narrows down the context to apply, improving per-step inference time; and, finally, context application via cross attention. Though much work has gone into optimizing per-frame performance, the context encoder is at least as important: recognition cannot begin before context encoding ends. Here, we show the lightweight phrase selection pass can be moved before context encoding, resulting in a speedup of up to 16.1 times and enabling biasing to scale to 20K phrases with a maximum pre-decoding delay under 33ms. With the addition of phrase- and wordpiece-level cross-entropy losses, our technique also achieves up to a 37.5% relative WER reduction over the baseline without the losses and lightweight phrase selection pass.

</details>

### [Improving Speed/Accuracy Tradeoff for Online Streaming ASR via Real-Valued and Trainable Strides](s2:51f7d8815f8f7897869bd09f2e309ff09e67edf2.md)
**Dario Albesano, Nicola Ferri, F. Weninger, Puming Zhan** · 2024-04-14

<details>
<summary>Abstract</summary>

The Conformer Transducer (CT) is arguably the most popular architecture for online streaming end-to-end (E2E) ASR systems. Since it has quadratic complexity in the input sequence length for computing the attention weights, downsampling the input sequence to reduce its length is an effective way to mitigate the computing cost and speed up the inference process. However, in the traditional downsampling approach, the sampling factor (i.e. stride) has to be a pre-defined integer value. The speed up achieved by such kind of downsampling often comes with significant accuracy degradation, because it lacks the flexibility of trading accuracy with speed at fine-grained level. In this paper, we apply the spectral pooling and DiffStride techniques to the CT based online E2E ASR system. This makes the stride a real-valued trainable parameter. We optimize the implementation of these techniques for CT based ASR systems and develop recipes to train the stride together with the model parameters. We conduct experiments on an internal medical conversation dataset. Our results show that we can achieve better tradeoff between recognition accuracy and inference speed by training real-valued stride parameter. Compared to using decimation with integer stride value, our approach reduces real-time factor by 15.6 % on a medical dataset with less than 1 % relative accuracy degradation.

</details>

### [Hot-Fixing Wake Word Recognition for End-to-End ASR Via Neural Model Reprogramming](s2:b166dc55c8e281ecb1bafe5b6c8e59465714ebe2.md)
**Pin-Jui Ku, I-Fan Chen, Chao-Han Huck Yang, A. Raju et al.** · 2024-04-14

<details>
<summary>Abstract</summary>

This paper proposes two novel variants of neural reprogramming to enhance wake word recognition in streaming end-to-end ASR models without updating model weights. The first, "trigger-frame reprogramming", prepends the input speech feature sequence with the learned trigger-frames of the target wake word to adjust ASR model’s hidden states for improved wake word recognition. The second, "predictor-state initialization", trains only the initial state vectors (cell and hidden states) of the LSTMs in the prediction network. When applying to a baseline LibriSpeech Emformer RNN-T model with a 98% wake word verification false rejection rate (FRR) on unseen wake words, the proposed approaches achieve 76% and 97% relative FRR reductions with no increase on false acceptance rate. In-depth characteristic analyses of the proposed approaches are also conducted to provide deeper insights. These approaches offer an effective hot-fixing methods to improve wake word recognition performance in deployed production ASR models without the need for model updates.

</details>

### [Extending Multilingual ASR to New Languages Using Supplementary Encoder and Decoder Components](s2:d3a5ab10a1d86a7d1f168967a487195c4eb3c65c.md)
**Yerbolat Khassanov, Zhipeng Chen, Tianfeng Chen, Tze Yuang Chong et al.** · 2024-04-14

<details>
<summary>Abstract</summary>

Extending multilingual automatic speech recognition (mASR) systems to new languages poses challenges, particularly when training data for existing languages is limited or unavailable. To tackle this issue, we suggest utilizing supplementary encoder and decoder components. Specifically, we propose appending and fine-tuning a distinct decoder designed for new languages, while preserving the parameters of existing languages to minimize disruption to their performance. Furthermore, we advocate attaching an additional encoder component to enhance acoustic representation learning for new languages, resulting in substantial improvements in word error rate performance. Our experimental findings demonstrate the effectiveness of the proposed methods for the task of extending language support within mASR systems.

</details>

### [SGPRS: Seamless GPU Partitioning Real-Time Scheduler for Periodic Deep Learning Workloads](2406.09425.md)
**Amir Fakhim Babaei, Thidapat Chantem** · 2024-04-13

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) are useful in many applications, including transportation, healthcare, and speech recognition. Despite various efforts to improve accuracy, few works have studied DNN in the context of real-time requirements. Coarse resource allocation and sequential execution in existing frameworks result in underutilization. In this work, we conduct GPU speedup gain analysis and propose SGPRS, the first real-time GPU scheduler considering zero configuration partition switch. The proposed scheduler not only meets more deadlines for parallel tasks but also sustains overall performance beyond the pivot point.

</details>

### [Automatic Speech Recognition Advancements for Indigenous Languages of the Americas](2404.08368.md)
**Monica Romero, Sandra Gomez, Ivan G. Torre** · 2024-04-12

<details>
<summary>Abstract</summary>

Indigenous languages are a fundamental legacy in the development of human communication, embodying the unique identity and culture of local communities in America. The Second AmericasNLP (Americas Natural Language Processing) Competition Track 1 of NeurIPS (Neural Information Processing Systems) 2022 proposed the task of training automatic speech recognition (ASR) systems for five Indigenous languages: Quechua, Guarani, Bribri, Kotiria, and Wa'ikhana. In this paper, we describe the fine-tuning of a state-of-the-art ASR model for each target language, using approximately 36.65 h of transcribed speech data from diverse sources enriched with data augmentation methods. We systematically investigate, using a Bayesian search, the impact of the different hyperparameters on the Wav2vec2.0 XLS-R (Cross-Lingual Speech Representations) variants of 300 M and 1 B parameters. Our findings indicate that data and detailed hyperparameter tuning significantly affect ASR accuracy, but language complexity determines the final result. The Quechua model achieved the lowest character error rate (CER) (12.14), while the Kotiria model, despite having the most extensive dataset during the fine-tuning phase, showed the highest CER (36.59). Conversely, with the smallest dataset, the Guarani model achieved a CER of 15.59, while Bribri and Wa'ikhana obtained, respectively, CERs of 34.70 and 35.23. Additionally, Sobol' sensitivity analysis highlighted the crucial roles of freeze fine-tuning updates and dropout rates. We release our best models for each language, marking the first open ASR models for Wa'ikhana and Kotiria. This work opens avenues for future research to advance ASR techniques in preserving minority Indigenous languages

</details>

### [An Effective Automated Speaking Assessment Approach to Mitigating Data Scarcity and Imbalanced Distribution](2404.07575.md)
**Tien-Hong Lo, Fu-An Chao, Tzu-I Wu, Yao-Ting Sung et al.** · 2024-04-11

<details>
<summary>Abstract</summary>

Automated speaking assessment (ASA) typically involves automatic speech recognition (ASR) and hand-crafted feature extraction from the ASR transcript of a learner's speech. Recently, self-supervised learning (SSL) has shown stellar performance compared to traditional methods. However, SSL-based ASA systems are faced with at least three data-related challenges: limited annotated data, uneven distribution of learner proficiency levels and non-uniform score intervals between different CEFR proficiency levels. To address these challenges, we explore the use of two novel modeling strategies: metric-based classification and loss reweighting, leveraging distinct SSL-based embedding features. Extensive experimental results on the ICNALE benchmark dataset suggest that our approach can outperform existing strong baselines by a sizable margin, achieving a significant improvement of more than 10% in CEFR prediction accuracy.

</details>

### [Conformer-1: Robust ASR via Large-Scale Semisupervised Bootstrapping](2404.07341.md)
**Kevin Zhang, Luka Chkhetiani, Francis McCann Ramirez, Yash Khare et al.** · 2024-04-10

<details>
<summary>Abstract</summary>

This paper presents Conformer-1, an end-to-end Automatic Speech Recognition (ASR) model trained on an extensive dataset of 570k hours of speech audio data, 91% of which was acquired from publicly available sources. To achieve this, we perform Noisy Student Training after generating pseudo-labels for the unlabeled public data using a strong Conformer RNN-T baseline model. The addition of these pseudo-labeled data results in remarkable improvements in relative Word Error Rate (WER) by 11.5% and 24.3% for our asynchronous and realtime models, respectively. Additionally, the model is more robust to background noise owing to the addition of these data. The results obtained in this study demonstrate that the incorporation of pseudo-labeled publicly available data is a highly effective strategy for improving ASR accuracy and noise robustness.

</details>

### [An inclusive review on deep learning techniques and their scope in handwriting recognition](2404.08011.md)
**Sukhdeep Singh, Sudhir Rohilla, Anuj Sharma** · 2024-04-10

<details>
<summary>Abstract</summary>

Deep learning expresses a category of machine learning algorithms that have the capability to combine raw inputs into intermediate features layers. These deep learning algorithms have demonstrated great results in different fields. Deep learning has particularly witnessed for a great achievement of human level performance across a number of domains in computer vision and pattern recognition. For the achievement of state-of-the-art performances in diverse domains, the deep learning used different architectures and these architectures used activation functions to perform various computations between hidden and output layers of any architecture. This paper presents a survey on the existing studies of deep learning in handwriting recognition field. Even though the recent progress indicates that the deep learning methods has provided valuable means for speeding up or proving accurate results in handwriting recognition, but following from the extensive literature survey, the present study finds that the deep learning has yet to revolutionize more and has to resolve many of the most pressing challenges in this field, but promising advances have been made on the prior state of the art. Additionally, an inadequate availability of labelled data to train presents problems in this domain. Nevertheless, the present handwriting recognition survey foresees deep learning enabling changes at both bench and bedside with the potential to transform several domains as image processing, speech recognition, computer vision, machine translation, robotics and control, medical imaging, medical information processing, bio-informatics, natural language processing, cyber security, and many others.

</details>

### [Transducers with Pronunciation-aware Embeddings for Automatic Speech Recognition](2404.04295.md)
**Hainan Xu, Zhehuai Chen, Fei Jia, Boris Ginsburg** · 2024-04-04

<details>
<summary>Abstract</summary>

This paper proposes Transducers with Pronunciation-aware Embeddings (PET). Unlike conventional Transducers where the decoder embeddings for different tokens are trained independently, the PET model's decoder embedding incorporates shared components for text tokens with the same or similar pronunciations. With experiments conducted in multiple datasets in Mandarin Chinese and Korean, we show that PET models consistently improve speech recognition accuracy compared to conventional Transducers. Our investigation also uncovers a phenomenon that we call error chain reactions. Instead of recognition errors being evenly spread throughout an utterance, they tend to group together, with subsequent errors often following earlier ones. Our analysis shows that PET models effectively mitigate this issue by substantially reducing the likelihood of the model generating additional errors following a prior one. Our implementation will be open-sourced with the NeMo toolkit.

</details>

### [RALL-E: Robust Codec Language Modeling with Chain-of-Thought Prompting for Text-to-Speech Synthesis](2404.03204.md)
**Detai Xin, Xu Tan, Kai Shen, Zeqian Ju et al.** · 2024-04-04

<details>
<summary>Abstract</summary>

We present RALL-E, a robust language modeling method for text-to-speech (TTS) synthesis. While previous work based on large language models (LLMs) shows impressive performance on zero-shot TTS, such methods often suffer from poor robustness, such as unstable prosody (weird pitch and rhythm/duration) and a high word error rate (WER), due to the autoregressive prediction style of language models. The core idea behind RALL-E is chain-of-thought (CoT) prompting, which decomposes the task into simpler steps to enhance the robustness of LLM-based TTS. To accomplish this idea, RALL-E first predicts prosody features (pitch and duration) of the input text and uses them as intermediate conditions to predict speech tokens in a CoT style. Second, RALL-E utilizes the predicted duration prompt to guide the computing of self-attention weights in Transformer to enforce the model to focus on the corresponding phonemes and prosody features when predicting speech tokens. Results of comprehensive objective and subjective evaluations demonstrate that, compared to a powerful baseline method VALL-E, RALL-E significantly improves the WER of zero-shot TTS from $5.6\%$ (without reranking) and $1.7\%$ (with reranking) to $2.5\%$ and $1.0\%$, respectively. Furthermore, we demonstrate that RALL-E correctly synthesizes sentences that are hard for VALL-E and reduces the error rate from $68\%$ to $4\%$.

</details>

### [Mai Ho'omāuna i ka 'Ai: Language Models Improve Automatic Speech Recognition in Hawaiian](2404.03073.md)
**Kaavya Chaparala, Guido Zarrella, Bruce Torres Fischer, Larry Kimura et al.** · 2024-04-03

<details>
<summary>Abstract</summary>

In this paper we address the challenge of improving Automatic Speech Recognition (ASR) for a low-resource language, Hawaiian, by incorporating large amounts of independent text data into an ASR foundation model, Whisper. To do this, we train an external language model (LM) on ~1.5M words of Hawaiian text. We then use the LM to rescore Whisper and compute word error rates (WERs) on a manually curated test set of labeled Hawaiian data. As a baseline, we use Whisper without an external LM. Experimental results reveal a small but significant improvement in WER when ASR outputs are rescored with a Hawaiian LM. The results support leveraging all available data in the development of ASR systems for underrepresented languages.

</details>

### [CMULAB: An Open-Source Framework for Training and Deployment of Natural Language Processing Models](2404.02408.md)
**Zaid Sheikh, Antonios Anastasopoulos, Shruti Rijhwani, Lindia Tjuatja et al.** · 2024-04-03

<details>
<summary>Abstract</summary>

Effectively using Natural Language Processing (NLP) tools in under-resourced languages requires a thorough understanding of the language itself, familiarity with the latest models and training methodologies, and technical expertise to deploy these models. This could present a significant obstacle for language community members and linguists to use NLP tools. This paper introduces the CMU Linguistic Annotation Backend, an open-source framework that simplifies model deployment and continuous human-in-the-loop fine-tuning of NLP models. CMULAB enables users to leverage the power of multilingual models to quickly adapt and extend existing tools for speech recognition, OCR, translation, and syntactic analysis to new languages, even with limited training data. We describe various tools and APIs that are currently available and how developers can easily add new models/functionality to the framework. Code is available at https://github.com/neulab/cmulab along with a live demo at https://cmulab.dev

</details>

### [BRAVEn: Improving Self-Supervised Pre-training for Visual and Auditory Speech Recognition](2404.02098.md)
**Alexandros Haliassos, Andreas Zinonos, Rodrigo Mira, Stavros Petridis et al.** · 2024-04-02

<details>
<summary>Abstract</summary>

Self-supervision has recently shown great promise for learning visual and auditory speech representations from unlabelled data. In this work, we propose BRAVEn, an extension to the recent RAVEn method, which learns speech representations entirely from raw audio-visual data. Our modifications to RAVEn enable BRAVEn to achieve state-of-the-art results among self-supervised methods in various settings. Moreover, we observe favourable scaling behaviour by increasing the amount of unlabelled data well beyond other self-supervised works. In particular, we achieve 20.0% / 1.7% word error rate for VSR / ASR on the LRS3 test set, with only 30 hours of labelled data and no external ASR models. Our results suggest that readily available unlabelled audio-visual data can largely replace costly transcribed data.

</details>

### [Noise Masking Attacks and Defenses for Pretrained Speech Models](2404.02052.md)
**Matthew Jagielski, Om Thakkar, Lun Wang** · 2024-04-02

<details>
<summary>Abstract</summary>

Speech models are often trained on sensitive data in order to improve model performance, leading to potential privacy leakage. Our work considers noise masking attacks, introduced by Amid et al. 2022, which attack automatic speech recognition (ASR) models by requesting a transcript of an utterance which is partially replaced with noise. They show that when a record has been seen at training time, the model will transcribe the noisy record with its memorized sensitive transcript. In our work, we extend these attacks beyond ASR models, to attack pretrained speech encoders. Our method fine-tunes the encoder to produce an ASR model, and then performs noise masking on this model, which we find recovers private information from the pretraining data, despite the model never having seen transcripts at pretraining time! We show how to improve the precision of these attacks and investigate a number of countermeasures to our attacks.

</details>

### [Transfer Learning from Whisper for Microscopic Intelligibility Prediction](2404.01737.md)
**Paul Best, Santiago Cuervo, Ricard Marxer** · 2024-04-02

<details>
<summary>Abstract</summary>

Macroscopic intelligibility models predict the expected human word-error-rate for a given speech-in-noise stimulus. In contrast, microscopic intelligibility models aim to make fine-grained predictions about listeners' perception, e.g. predicting phonetic or lexical responses. State-of-the-art macroscopic models use transfer learning from large scale deep learning models for speech processing, whereas such methods have rarely been used for microscopic modeling. In this paper, we study the use of transfer learning from Whisper, a state-of-the-art deep learning model for automatic speech recognition, for microscopic intelligibility prediction at the level of lexical responses. Our method outperforms the considered baselines, even in a zero-shot setup, and yields a relative improvement of up to 66\% when fine-tuned to predict listeners' responses. Our results showcase the promise of large scale deep learning based methods for microscopic intelligibility prediction.

</details>

### [Effective internal language model training and fusion for factorized transducer model](2404.01716.md)
**Jinxi Guo, Niko Moritz, Yingyi Ma, Frank Seide et al.** · 2024-04-02

<details>
<summary>Abstract</summary>

The internal language model (ILM) of the neural transducer has been widely studied. In most prior work, it is mainly used for estimating the ILM score and is subsequently subtracted during inference to facilitate improved integration with external language models. Recently, various of factorized transducer models have been proposed, which explicitly embrace a standalone internal language model for non-blank token prediction. However, even with the adoption of factorized transducer models, limited improvement has been observed compared to shallow fusion. In this paper, we propose a novel ILM training and decoding strategy for factorized transducer models, which effectively combines the blank, acoustic and ILM scores. Our experiments show a 17% relative improvement over the standard decoding method when utilizing a well-trained ILM and the proposed decoding strategy on LibriSpeech datasets. Furthermore, when compared to a strong RNN-T baseline enhanced with external LM fusion, the proposed model yields a 5.5% relative improvement on general-sets and an 8.9% WER reduction for rare words. The proposed model can achieve superior performance without relying on external language models, rendering it highly efficient for production use-cases. To further improve the performance, we propose a novel and memory-efficient ILM-fusion-aware minimum word error rate (MWER) training method which improves ILM integration significantly.

</details>

### [Africa-Centric Self-Supervised Pre-Training for Multilingual Speech Representation in a Sub-Saharan Context](2404.02000.md)
**Antoine Caubrière, Elodie Gauthier** · 2024-04-02

<details>
<summary>Abstract</summary>

We present the first self-supervised multilingual speech model trained exclusively on African speech. The model learned from nearly 60 000 hours of unlabeled speech segments in 21 languages and dialects spoken in sub-Saharan Africa. On the SSA subset of the FLEURS-102 dataset, our approach based on a HuBERT$_{base}$ (0.09B) architecture shows competitive results, for ASR downstream task, compared to the w2v-bert-51 (0.6B) pre-trained model proposed in the FLEURS benchmark, while being more efficient by using 7x less data and 6x less parameters. Furthermore, in the context of a LID downstream task, our approach outperforms FLEURS baselines accuracy by over 22\%.

</details>

### [Houston we have a Divergence: A Subgroup Performance Analysis of ASR Models](2404.07226.md)
**Alkis Koudounas, Flavio Giobergia** · 2024-03-31

<details>
<summary>Abstract</summary>

The Fearless Steps APOLLO Community Resource provides unparalleled opportunities to explore the potential of multi-speaker team communications from NASA Apollo missions. This study focuses on discovering the characteristics that make Apollo recordings more or less intelligible to Automatic Speech Recognition (ASR) methods. We extract, for each audio recording, interpretable metadata on recordings (signal-to-noise ratio, spectral flatness, presence of pauses, sentence duration), transcript (number of words spoken, speaking rate), or known a priori (speaker). We identify subgroups of audio recordings based on combinations of these metadata and compute each subgroup's performance (e.g., Word Error Rate) and the difference in performance (''divergence'') w.r.t the overall population. We then apply the Whisper model in different sizes, trained on English-only or multilingual datasets, in zero-shot or after fine-tuning. We conduct several analyses to (i) automatically identify and describe the most problematic subgroups for a given model, (ii) examine the impact of fine-tuning w.r.t. zero-shot at the subgroup level, (iii) understand the effect of model size on subgroup performance, and (iv) analyze if multilingual models are more sensitive than monolingual to subgroup performance disparities. The insights enhance our understanding of subgroup-specific performance variations, paving the way for advancements in optimizing ASR systems for Earth-to-space communications.

</details>

### [Multi-Stage Multi-Modal Pre-Training for Automatic Speech Recognition](2403.19822.md)
**Yash Jain, David Chan, Pranav Dheram, Aparna Khare et al.** · 2024-03-28

<details>
<summary>Abstract</summary>

Recent advances in machine learning have demonstrated that multi-modal pre-training can improve automatic speech recognition (ASR) performance compared to randomly initialized models, even when models are fine-tuned on uni-modal tasks. Existing multi-modal pre-training methods for the ASR task have primarily focused on single-stage pre-training where a single unsupervised task is used for pre-training followed by fine-tuning on the downstream task. In this work, we introduce a novel method combining multi-modal and multi-task unsupervised pre-training with a translation-based supervised mid-training approach. We empirically demonstrate that such a multi-stage approach leads to relative word error rate (WER) improvements of up to 38.45% over baselines on both Librispeech and SUPERB. Additionally, we share several important findings for choosing pre-training methods and datasets.

</details>

### [LV-CTC: Non-autoregressive ASR with CTC and latent variable models](2403.19207.md)
**Yuya Fujita, Shinji Watanabe, Xuankai Chang, Takashi Maekaku** · 2024-03-28

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) models for automatic speech recognition (ASR) aim to achieve high accuracy and fast inference by simplifying the autoregressive (AR) generation process of conventional models. Connectionist temporal classification (CTC) is one of the key techniques used in NAR ASR models. In this paper, we propose a new model combining CTC and a latent variable model, which is one of the state-of-the-art models in the neural machine translation research field. A new neural network architecture and formulation specialized for ASR application are introduced. In the proposed model, CTC alignment is assumed to be dependent on the latent variables that are expected to capture dependencies between tokens. Experimental results on a 100 hours subset of Librispeech corpus showed the best recognition accuracy among CTC-based NAR models. On the TED-LIUM2 corpus, the best recognition accuracy is achieved including AR E2E models with faster inference speed.

</details>

### [PhysicsAssistant: An LLM-Powered Interactive Learning Robot for Physics Lab Investigations](2403.18721.md)
**Ehsan Latif, Ramviyas Parasuraman, Xiaoming Zhai** · 2024-03-27

<details>
<summary>Abstract</summary>

Robot systems in education can leverage Large language models' (LLMs) natural language understanding capabilities to provide assistance and facilitate learning. This paper proposes a multimodal interactive robot (PhysicsAssistant) built on YOLOv8 object detection, cameras, speech recognition, and chatbot using LLM to provide assistance to students' physics labs. We conduct a user study on ten 8th-grade students to empirically evaluate the performance of PhysicsAssistant with a human expert. The Expert rates the assistants' responses to student queries on a 0-4 scale based on Bloom's taxonomy to provide educational support. We have compared the performance of PhysicsAssistant (YOLOv8+GPT-3.5-turbo) with GPT-4 and found that the human expert rating of both systems for factual understanding is the same. However, the rating of GPT-4 for conceptual and procedural knowledge (3 and 3.2 vs 2.2 and 2.6, respectively) is significantly higher than PhysicsAssistant (p < 0.05). However, the response time of GPT-4 is significantly higher than PhysicsAssistant (3.54 vs 1.64 sec, p < 0.05). Hence, despite the relatively lower response quality of PhysicsAssistant than GPT-4, it has shown potential for being used as a real-time lab assistant to provide timely responses and can offload teachers' labor to assist with repetitive tasks. To the best of our knowledge, this is the first attempt to build such an interactive multimodal robotic assistant for K-12 science (physics) education.

</details>

### [PhoWhisper: Automatic Speech Recognition for Vietnamese](2406.02555.md)
**Thanh-Thien Le, Linh The Nguyen, Dat Quoc Nguyen** · 2024-03-27

<details>
<summary>Abstract</summary>

We introduce PhoWhisper in five versions for Vietnamese automatic speech recognition. PhoWhisper's robustness is achieved through fine-tuning the Whisper model on an 844-hour dataset that encompasses diverse Vietnamese accents. Our experimental study demonstrates state-of-the-art performances of PhoWhisper on benchmark Vietnamese ASR datasets. We have open-sourced PhoWhisper at: https://github.com/VinAIResearch/PhoWhisper

</details>

### [DANCER: Entity Description Augmented Named Entity Corrector for Automatic Speech Recognition](2403.17645.md)
**Yi-Cheng Wang, Hsin-Wei Wang, Bi-Cheng Yan, Chi-Han Lin et al.** · 2024-03-26

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (E2E ASR) systems often suffer from mistranscription of domain-specific phrases, such as named entities, sometimes leading to catastrophic failures in downstream tasks. A family of fast and lightweight named entity correction (NEC) models for ASR have recently been proposed, which normally build on phonetic-level edit distance algorithms and have shown impressive NEC performance. However, as the named entity (NE) list grows, the problems of phonetic confusion in the NE list are exacerbated; for example, homophone ambiguities increase substantially. In view of this, we proposed a novel Description Augmented Named entity CorrEctoR (dubbed DANCER), which leverages entity descriptions to provide additional information to facilitate mitigation of phonetic confusion for NEC on ASR transcription. To this end, an efficient entity description augmented masked language model (EDA-MLM) comprised of a dense retrieval model is introduced, enabling MLM to adapt swiftly to domain-specific entities for the NEC task. A series of experiments conducted on the AISHELL-1 and Homophone datasets confirm the effectiveness of our modeling approach. DANCER outperforms a strong baseline, the phonetic edit-distance-based NEC model (PED-NEC), by a character error rate (CER) reduction of about 7% relatively on AISHELL-1 for named entities. More notably, when tested on Homophone that contain named entities of high phonetic confusion, DANCER offers a more pronounced CER reduction of 46% relatively over PED-NEC for named entities.

</details>

### [Hierarchical Recurrent Adapters for Efficient Multi-Task Adaptation of Large Speech Models](2403.19709.md)
**Tsendsuren Munkhdalai, Youzheng Chen, Khe Chai Sim, Fadi Biadsy et al.** · 2024-03-25

<details>
<summary>Abstract</summary>

Parameter efficient adaptation methods have become a key mechanism to train large pre-trained models for downstream tasks. However, their per-task parameter overhead is considered still high when the number of downstream tasks to adapt for is large. We introduce an adapter module that has a better efficiency in large scale multi-task adaptation scenario. Our adapter is hierarchical in terms of how the adapter parameters are allocated. The adapter consists of a single shared controller network and multiple task-level adapter heads to reduce the per-task parameter overhead without performance regression on downstream tasks. The adapter is also recurrent so the entire adapter parameters are reused across different layers of the pre-trained model. Our Hierarchical Recurrent Adapter (HRA) outperforms the previous adapter-based approaches as well as full model fine-tuning baseline in both single and multi-task adaptation settings when evaluated on automatic speech recognition tasks.

</details>

### [Grammatical vs Spelling Error Correction: An Investigation into the Responsiveness of Transformer-based Language Models using BART and MarianMT](2403.16655.md)
**Rohit Raju, Peeta Basa Pati, SA Gandheesh, Gayatri Sanjana Sannala et al.** · 2024-03-25

<details>
<summary>Abstract</summary>

Text continues to remain a relevant form of representation for information. Text documents are created either in digital native platforms or through the conversion of other media files such as images and speech. While the digital native text is invariably obtained through physical or virtual keyboards, technologies such as OCR and speech recognition are utilized to transform the images and speech signals into text content. All these variety of mechanisms of text generation also introduce errors into the captured text. This project aims at analyzing different kinds of error that occurs in text documents. The work employs two of the advanced deep neural network-based language models, namely, BART and MarianMT, to rectify the anomalies present in the text. Transfer learning of these models with available dataset is performed to finetune their capacity for error correction. A comparative study is conducted to investigate the effectiveness of these models in handling each of the defined error categories. It is observed that while both models can bring down the erroneous sentences by 20+%, BART can handle spelling errors far better (24.6%) than grammatical errors (8.8%).

</details>

### [Privacy-Preserving End-to-End Spoken Language Understanding](2403.15510.md)
**Yinggui Wang, Wei Huang, Le Yang** · 2024-03-22

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU), one of the key enabling technologies for human-computer interaction in IoT devices, provides an easy-to-use user interface. Human speech can contain a lot of user-sensitive information, such as gender, identity, and sensitive content. New types of security and privacy breaches have thus emerged. Users do not want to expose their personal sensitive information to malicious attacks by untrusted third parties. Thus, the SLU system needs to ensure that a potential malicious attacker cannot deduce the sensitive attributes of the users, while it should avoid greatly compromising the SLU accuracy. To address the above challenge, this paper proposes a novel SLU multi-task privacy-preserving model to prevent both the speech recognition (ASR) and identity recognition (IR) attacks. The model uses the hidden layer separation technique so that SLU information is distributed only in a specific portion of the hidden layer, and the other two types of information are removed to obtain a privacy-secure hidden layer. In order to achieve good balance between efficiency and privacy, we introduce a new mechanism of model pre-training, namely joint adversarial training, to further enhance the user privacy. Experiments over two SLU datasets show that the proposed method can reduce the accuracy of both the ASR and IR attacks close to that of a random guess, while leaving the SLU performance largely unaffected.

</details>

### [A Multimodal Approach to Device-Directed Speech Detection with Large Language Models](2403.14438.md)
**Dominik Wagner, Alexander Churchill, Siddharth Sigtia, Panayiotis Georgiou et al.** · 2024-03-21

<details>
<summary>Abstract</summary>

Interactions with virtual assistants typically start with a predefined trigger phrase followed by the user command. To make interactions with the assistant more intuitive, we explore whether it is feasible to drop the requirement that users must begin each command with a trigger phrase. We explore this task in three ways: First, we train classifiers using only acoustic information obtained from the audio waveform. Second, we take the decoder outputs of an automatic speech recognition (ASR) system, such as 1-best hypotheses, as input features to a large language model (LLM). Finally, we explore a multimodal system that combines acoustic and lexical features, as well as ASR decoder signals in an LLM. Using multimodal information yields relative equal-error-rate improvements over text-only and audio-only models of up to 39% and 61%. Increasing the size of the LLM and training with low-rank adaption leads to further relative EER reductions of up to 18% on our dataset.

</details>

### [XLAVS-R: Cross-Lingual Audio-Visual Speech Representation Learning for Noise-Robust Speech Perception](2403.14402.md)
**HyoJung Han, Mohamed Anwar, Juan Pino, Wei-Ning Hsu et al.** · 2024-03-21

<details>
<summary>Abstract</summary>

Speech recognition and translation systems perform poorly on noisy inputs, which are frequent in realistic environments. Augmenting these systems with visual signals has the potential to improve robustness to noise. However, audio-visual (AV) data is only available in limited amounts and for fewer languages than audio-only resources. To address this gap, we present XLAVS-R, a cross-lingual audio-visual speech representation model for noise-robust speech recognition and translation in over 100 languages. It is designed to maximize the benefits of limited multilingual AV pre-training data, by building on top of audio-only multilingual pre-training and simplifying existing pre-training schemes. Extensive evaluation on the MuAViC benchmark shows the strength of XLAVS-R on downstream audio-visual speech recognition and translation tasks, where it outperforms the previous state of the art by up to 18.5% WER and 4.7 BLEU given noisy AV inputs, and enables strong zero-shot audio-visual ability with audio-only fine-tuning.

</details>

### [M$^3$AV: A Multimodal, Multigenre, and Multipurpose Audio-Visual Academic Lecture Dataset](2403.14168.md)
**Zhe Chen, Heyang Liu, Wenyi Yu, Guangzhi Sun et al.** · 2024-03-21

<details>
<summary>Abstract</summary>

Publishing open-source academic video recordings is an emergent and prevalent approach to sharing knowledge online. Such videos carry rich multimodal information including speech, the facial and body movements of the speakers, as well as the texts and pictures in the slides and possibly even the papers. Although multiple academic video datasets have been constructed and released, few of them support both multimodal content recognition and understanding tasks, which is partially due to the lack of high-quality human annotations. In this paper, we propose a novel multimodal, multigenre, and multipurpose audio-visual academic lecture dataset (M$^3$AV), which has almost 367 hours of videos from five sources covering computer science, mathematics, and medical and biology topics. With high-quality human annotations of the slide text and spoken words, in particular high-valued name entities, the dataset can be used for multiple audio-visual recognition and understanding tasks. Evaluations performed on contextual speech recognition, speech synthesis, and slide and script generation tasks demonstrate that the diversity of M$^3$AV makes it a challenging dataset.

</details>

### [Open Access NAO (OAN): a ROS2-based software framework for HRI applications with the NAO robot](2403.13960.md)
**Antonio Bono, Kenji Brameld, Luigi D'Alfonso, Giuseppe Fedele** · 2024-03-20

<details>
<summary>Abstract</summary>

This paper presents a new software framework for HRI experimentation with the sixth version of the common NAO robot produced by the United Robotics Group. Embracing the common demand of researchers for better performance and new features for NAO, the authors took advantage of the ability to run ROS2 onboard on the NAO to develop a framework independent of the APIs provided by the manufacturer. Such a system provides NAO with not only the basic skills of a humanoid robot such as walking and reproducing movements of interest but also features often used in HRI such as: speech recognition/synthesis, face and object detention, and the use of Generative Pre-trained Transformer (GPT) models for conversation. The developed code is therefore configured as a ready-to-use but also highly expandable and improvable tool thanks to the possibilities provided by the ROS community.

</details>

### [BanglaNum -- A Public Dataset for Bengali Digit Recognition from Speech](2403.13465.md)
**Mir Sayeed Mohammad, Azizul Zahid, Md Asif Iqbal** · 2024-03-20

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) converts the human voice into readily understandable and categorized text or words. Although Bengali is one of the most widely spoken languages in the world, there have been very few studies on Bengali ASR, particularly on Bangladeshi-accented Bengali. In this study, audio recordings of spoken digits (0-9) from university students were used to create a Bengali speech digits dataset that may be employed to train artificial neural networks for voice-based digital input systems. This paper also compares the Bengali digit recognition accuracy of several Convolutional Neural Networks (CNNs) using spectrograms and shows that a test accuracy of 98.23% is achievable using parameter-efficient models such as SqueezeNet on our dataset.

</details>

### [Advanced Long-Content Speech Recognition With Factorized Neural Transducer](2403.13423.md)
**Xun Gong, Yu Wu, Jinyu Li, Shujie Liu et al.** · 2024-03-20

<details>
<summary>Abstract</summary>

In this paper, we propose two novel approaches, which integrate long-content information into the factorized neural transducer (FNT) based architecture in both non-streaming (referred to as LongFNT ) and streaming (referred to as SLongFNT ) scenarios. We first investigate whether long-content transcriptions can improve the vanilla conformer transducer (C-T) models. Our experiments indicate that the vanilla C-T models do not exhibit improved performance when utilizing long-content transcriptions, possibly due to the predictor network of C-T models not functioning as a pure language model. Instead, FNT shows its potential in utilizing long-content information, where we propose the LongFNT model and explore the impact of long-content information in both text (LongFNT-Text) and speech (LongFNT-Speech). The proposed LongFNT-Text and LongFNT-Speech models further complement each other to achieve better performance, with transcription history proving more valuable to the model. The effectiveness of our LongFNT approach is evaluated on LibriSpeech and GigaSpeech corpora, and obtains relative 19% and 12% word error rate reduction, respectively. Furthermore, we extend the LongFNT model to the streaming scenario, which is named SLongFNT , consisting of SLongFNT-Text and SLongFNT-Speech approaches to utilize long-content text and speech information. Experiments show that the proposed SLongFNT model achieves relative 26% and 17% WER reduction on LibriSpeech and GigaSpeech respectively while keeping a good latency, compared to the FNT baseline. Overall, our proposed LongFNT and SLongFNT highlight the significance of considering long-content speech and transcription knowledge for improving both non-streaming and streaming speech recognition systems.

</details>

### [Isometric Neural Machine Translation using Phoneme Count Ratio Reward-based Reinforcement Learning](2403.15469.md)
**Shivam Ratnakant Mhaskar, Nirmesh J. Shah, Mohammadi Zaki, Ashishkumar P. Gudmalwar et al.** · 2024-03-20

<details>
<summary>Abstract</summary>

Traditional Automatic Video Dubbing (AVD) pipeline consists of three key modules, namely, Automatic Speech Recognition (ASR), Neural Machine Translation (NMT), and Text-to-Speech (TTS). Within AVD pipelines, isometric-NMT algorithms are employed to regulate the length of the synthesized output text. This is done to guarantee synchronization with respect to the alignment of video and audio subsequent to the dubbing process. Previous approaches have focused on aligning the number of characters and words in the source and target language texts of Machine Translation models. However, our approach aims to align the number of phonemes instead, as they are closely associated with speech duration. In this paper, we present the development of an isometric NMT system using Reinforcement Learning (RL), with a focus on optimizing the alignment of phoneme counts in the source and target language sentence pairs. To evaluate our models, we propose the Phoneme Count Compliance (PCC) score, which is a measure of length compliance. Our approach demonstrates a substantial improvement of approximately 36% in the PCC score compared to the state-of-the-art models when applied to English-Hindi language pairs. Moreover, we propose a student-teacher architecture within the framework of our RL approach to maintain a trade-off between the phoneme count and translation quality.

</details>

### [TDT-KWS: Fast and Accurate Keyword Spotting Using Token-and-Duration Transducer](2403.13332.md)
**Yu Xi, Hao Li, Baochen Yang, Haoyu Li et al.** · 2024-03-20

<details>
<summary>Abstract</summary>

Designing an efficient keyword spotting (KWS) system that delivers exceptional performance on resource-constrained edge devices has long been a subject of significant attention. Existing KWS search algorithms typically follow a frame-synchronous approach, where search decisions are made repeatedly at each frame despite the fact that most frames are keyword-irrelevant. In this paper, we propose TDT-KWS, which leverages token-and-duration Transducers (TDT) for KWS tasks. We also propose a novel KWS task-specific decoding algorithm for Transducer-based models, which supports highly effective frame-asynchronous keyword search in streaming speech scenarios. With evaluations conducted on both the public Hey Snips and self-constructed LibriKWS-20 datasets, our proposed KWS-decoding algorithm produces more accurate results than conventional ASR decoding algorithms. Additionally, TDTKWS achieves on-par or better wake word detection performance than both RNN-T and traditional TDT-ASR systems while achieving significant inference speed-up. Furthermore, experiments show that TDT-KWS is more robust to noisy environments compared to RNN-T KWS.

</details>

### [FlowerFormer: Empowering Neural Architecture Encoding using a Flow-aware Graph Transformer](2403.12821.md)
**Dongyeong Hwang, Hyunju Kim, Sunwoo Kim, Kijung Shin** · 2024-03-19

<details>
<summary>Abstract</summary>

The success of a specific neural network architecture is closely tied to the dataset and task it tackles; there is no one-size-fits-all solution. Thus, considerable efforts have been made to quickly and accurately estimate the performances of neural architectures, without full training or evaluation, for given tasks and datasets. Neural architecture encoding has played a crucial role in the estimation, and graphbased methods, which treat an architecture as a graph, have shown prominent performance. For enhanced representation learning of neural architectures, we introduce FlowerFormer, a powerful graph transformer that incorporates the information flows within a neural architecture. FlowerFormer consists of two key components: (a) bidirectional asynchronous message passing, inspired by the flows; (b) global attention built on flow-based masking. Our extensive experiments demonstrate the superiority of FlowerFormer over existing neural encoding methods, and its effectiveness extends beyond computer vision models to include graph neural networks and auto speech recognition models. Our code is available at http://github.com/y0ngjaenius/CVPR2024_FLOWERFormer.

</details>

### [Multimodal Human-Autonomous Agents Interaction Using Pre-Trained Language and Visual Foundation Models](2403.12273.md)
**Linus Nwankwo, Elmar Rueckert** · 2024-03-18

<details>
<summary>Abstract</summary>

In this paper, we extended the method proposed in [21] to enable humans to interact naturally with autonomous agents through vocal and textual conversations. Our extended method exploits the inherent capabilities of pre-trained large language models (LLMs), multimodal visual language models (VLMs), and speech recognition (SR) models to decode the high-level natural language conversations and semantic understanding of the robot's task environment, and abstract them to the robot's actionable commands or queries. We performed a quantitative evaluation of our framework's natural vocal conversation understanding with participants from different racial backgrounds and English language accents. The participants interacted with the robot using both spoken and textual instructional commands. Based on the logged interaction data, our framework achieved 87.55% vocal commands decoding accuracy, 86.27% commands execution success, and an average latency of 0.89 seconds from receiving the participants' vocal chat commands to initiating the robot's actual physical action. The video demonstrations of this paper can be found at https://linusnep.github.io/MTCC-IRoNL/.

</details>

### [TCNet: Continuous Sign Language Recognition from Trajectories and Correlated Regions](2403.11818.md)
**Hui Lu, Albert Ali Salah, Ronald Poppe** · 2024-03-18

<details>
<summary>Abstract</summary>

A key challenge in continuous sign language recognition (CSLR) is to efficiently capture long-range spatial interactions over time from the video input. To address this challenge, we propose TCNet, a hybrid network that effectively models spatio-temporal information from Trajectories and Correlated regions. TCNet's trajectory module transforms frames into aligned trajectories composed of continuous visual tokens. In addition, for a query token, self-attention is learned along the trajectory. As such, our network can also focus on fine-grained spatio-temporal patterns, such as finger movements, of a specific region in motion. TCNet's correlation module uses a novel dynamic attention mechanism that filters out irrelevant frame regions. Additionally, it assigns dynamic key-value tokens from correlated regions to each query. Both innovations significantly reduce the computation cost and memory. We perform experiments on four large-scale datasets: PHOENIX14, PHOENIX14-T, CSL, and CSL-Daily, respectively. Our results demonstrate that TCNet consistently achieves state-of-the-art performance. For example, we improve over the previous state-of-the-art by 1.5% and 1.0% word error rate on PHOENIX14 and PHOENIX14-T, respectively.

</details>

### [Energy-Based Models with Applications to Speech and Language Processing](2403.10961.md)
**Zhijian Ou** · 2024-03-16

<details>
<summary>Abstract</summary>

Energy-Based Models (EBMs) are an important class of probabilistic models, also known as random fields and undirected graphical models. EBMs are un-normalized and thus radically different from other popular self-normalized probabilistic models such as hidden Markov models (HMMs), autoregressive models, generative adversarial nets (GANs) and variational auto-encoders (VAEs). Over the past years, EBMs have attracted increasing interest not only from the core machine learning community, but also from application domains such as speech, vision, natural language processing (NLP) and so on, due to significant theoretical and algorithmic progress. The sequential nature of speech and language also presents special challenges and needs a different treatment from processing fix-dimensional data (e.g., images). Therefore, the purpose of this monograph is to present a systematic introduction to energy-based models, including both algorithmic progress and applications in speech and language processing. First, the basics of EBMs are introduced, including classic models, recent models parameterized by neural networks, sampling methods, and various learning methods from the classic learning algorithms to the most advanced ones. Then, the application of EBMs in three different scenarios is presented, i.e., for modeling marginal, conditional and joint distributions, respectively. 1) EBMs for sequential data with applications in language modeling, where the main focus is on the marginal distribution of a sequence itself; 2) EBMs for modeling conditional distributions of target sequences given observation sequences, with applications in speech recognition, sequence labeling and text generation; 3) EBMs for modeling joint distributions of both sequences of observations and targets, and their applications in semi-supervised learning and calibrated natural language understanding.

</details>

### [Initial Decoding with Minimally Augmented Language Model for Improved Lattice Rescoring in Low Resource ASR](2403.10937.md)
**Savitha Murthy, Dinkar Sitaram** · 2024-03-16

<details>
<summary>Abstract</summary>

This paper addresses the problem of improving speech recognition accuracy with lattice rescoring in low-resource languages where the baseline language model is insufficient for generating inclusive lattices. We minimally augment the baseline language model with word unigram counts that are present in a larger text corpus of the target language but absent in the baseline. The lattices generated after decoding with such an augmented baseline language model are more comprehensive. We obtain 21.8% (Telugu) and 41.8% (Kannada) relative word error reduction with our proposed method. This reduction in word error rate is comparable to 21.5% (Telugu) and 45.9% (Kannada) relative word error reduction obtained by decoding with full Wikipedia text augmented language mode while our approach consumes only 1/8th the memory. We demonstrate that our method is comparable with various text selection-based language model augmentation and also consistent for data sets of different sizes. Our approach is applicable for training speech recognition systems under low resource conditions where speech data and compute resources are insufficient, while there is a large text corpus that is available in the target language. Our research involves addressing the issue of out-of-vocabulary words of the baseline in general and does not focus on resolving the absence of named entities. Our proposed method is simple and yet computationally less expensive.

</details>

### [SpokeN-100: A Cross-Lingual Benchmarking Dataset for The Classification of Spoken Numbers in Different Languages](2403.09753.md)
**René Groh, Nina Goes, Andreas M. Kist** · 2024-03-14

<details>
<summary>Abstract</summary>

Benchmarking plays a pivotal role in assessing and enhancing the performance of compact deep learning models designed for execution on resource-constrained devices, such as microcontrollers. Our study introduces a novel, entirely artificially generated benchmarking dataset tailored for speech recognition, representing a core challenge in the field of tiny deep learning. SpokeN-100 consists of spoken numbers from 0 to 99 spoken by 32 different speakers in four different languages, namely English, Mandarin, German and French, resulting in 12,800 audio samples. We determine auditory features and use UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction) as a dimensionality reduction method to show the diversity and richness of the dataset. To highlight the use case of the dataset, we introduce two benchmark tasks: given an audio sample, classify (i) the used language and/or (ii) the spoken number. We optimized state-of-the-art deep neural networks and performed an evolutionary neural architecture search to find tiny architectures optimized for the 32-bit ARM Cortex-M4 nRF52840 microcontroller. Our results represent the first benchmark data achieved for SpokeN-100.

</details>

### [More than words: Advancements and challenges in speech recognition for singing](2403.09298.md)
**Anna Kruspe** · 2024-03-14

<details>
<summary>Abstract</summary>

This paper addresses the challenges and advancements in speech recognition for singing, a domain distinctly different from standard speech recognition. Singing encompasses unique challenges, including extensive pitch variations, diverse vocal styles, and background music interference. We explore key areas such as phoneme recognition, language identification in songs, keyword spotting, and full lyrics transcription. I will describe some of my own experiences when performing research on these tasks just as they were starting to gain traction, but will also show how recent developments in deep learning and large-scale datasets have propelled progress in this field. My goal is to illuminate the complexities of applying speech recognition to singing, evaluate current capabilities, and outline future research directions.

</details>

### [Skipformer: A Skip-and-Recover Strategy for Efficient Speech Recognition](2403.08258.md)
**Wenjing Zhu, Sining Sun, Changhao Shan, Peng Fan et al.** · 2024-03-13

<details>
<summary>Abstract</summary>

Conformer-based attention models have become the de facto backbone model for Automatic Speech Recognition tasks. A blank symbol is usually introduced to align the input and output sequences for CTC or RNN-T models. Unfortunately, the long input length overloads computational budget and memory consumption quadratically by attention mechanism. In this work, we propose a "Skip-and-Recover" Conformer architecture, named Skipformer, to squeeze sequence input length dynamically and inhomogeneously. Skipformer uses an intermediate CTC output as criteria to split frames into three groups: crucial, skipping and ignoring. The crucial group feeds into next conformer blocks and its output joint with skipping group by original temporal order as the final encoder output. Experiments show that our model reduces the input sequence length by 31 times on Aishell-1 and 22 times on Librispeech corpus. Meanwhile, the model can achieve better recognition accuracy and faster inference speed than recent baseline models. Our code is open-sourced and available online.

</details>

### [SpeechColab Leaderboard: An Open-Source Platform for Automatic Speech Recognition Evaluation](2403.08196.md)
**Jiayu Du, Jinpeng Li, Guoguo Chen, Wei-Qiang Zhang** · 2024-03-13

<details>
<summary>Abstract</summary>

In the wake of the surging tide of deep learning over the past decade, Automatic Speech Recognition (ASR) has garnered substantial attention, leading to the emergence of numerous publicly accessible ASR systems that are actively being integrated into our daily lives. Nonetheless, the impartial and replicable evaluation of these ASR systems encounters challenges due to various crucial subtleties. In this paper we introduce the SpeechColab Leaderboard, a general-purpose, open-source platform designed for ASR evaluation. With this platform: (i) We report a comprehensive benchmark, unveiling the current state-of-the-art panorama for ASR systems, covering both open-source models and industrial commercial services. (ii) We quantize how distinct nuances in the scoring pipeline influence the final benchmark outcomes. These include nuances related to capitalization, punctuation, interjection, contraction, synonym usage, compound words, etc. These issues have gained prominence in the context of the transition towards an End-to-End future. (iii) We propose a practical modification to the conventional Token-Error-Rate (TER) evaluation metric, with inspirations from Kolmogorov complexity and Normalized Information Distance (NID). This adaptation, called modified-TER (mTER), achieves proper normalization and symmetrical treatment of reference and hypothesis. By leveraging this platform as a large-scale testing ground, this study demonstrates the robustness and backward compatibility of mTER when compared to TER. The SpeechColab Leaderboard is accessible at https://github.com/SpeechColab/Leaderboard

</details>

### [Gujarati-English Code-Switching Speech Recognition using ensemble prediction of spoken language](2403.08011.md)
**Yash Sharma, Basil Abraham, Preethi Jyothi** · 2024-03-12

<details>
<summary>Abstract</summary>

An important and difficult task in code-switched speech recognition is to recognize the language, as lots of words in two languages can sound similar, especially in some accents. We focus on improving performance of end-to-end Automatic Speech Recognition models by conditioning transformer layers on language ID of words and character in the output in an per layer supervised manner. To this end, we propose two methods of introducing language specific parameters and explainability in the multi-head attention mechanism, and implement a Temporal Loss that helps maintain continuity in input alignment. Despite being unable to reduce WER significantly, our method shows promise in predicting the correct language from just spoken data. We introduce regularization in the language prediction by dropping LID in the sequence, which helps align long repeated output sequences.

</details>

### [Beyond the Labels: Unveiling Text-Dependency in Paralinguistic Speech Recognition Datasets](2403.07767.md)
**Jan Pešán, Santosh Kesiraju, Lukáš Burget, Jan ''Honza'' Černocký** · 2024-03-12

<details>
<summary>Abstract</summary>

Paralinguistic traits like cognitive load and emotion are increasingly recognized as pivotal areas in speech recognition research, often examined through specialized datasets like CLSE and IEMOCAP. However, the integrity of these datasets is seldom scrutinized for text-dependency. This paper critically evaluates the prevalent assumption that machine learning models trained on such datasets genuinely learn to identify paralinguistic traits, rather than merely capturing lexical features. By examining the lexical overlap in these datasets and testing the performance of machine learning models, we expose significant text-dependency in trait-labeling. Our results suggest that some machine learning models, especially large pre-trained models like HuBERT, might inadvertently focus on lexical characteristics rather than the intended paralinguistic features. The study serves as a call to action for the research community to reevaluate the reliability of existing datasets and methodologies, ensuring that machine learning models genuinely learn what they are designed to recognize.

</details>

### [The evaluation of a code-switched Sepedi-English automatic speech recognition system](2403.07947.md)
**Amanda Phaladi, Thipe Modipa** · 2024-03-11

<details>
<summary>Abstract</summary>

Speech technology is a field that encompasses various techniques and tools used to enable machines to interact with speech, such as automatic speech recognition (ASR), spoken dialog systems, and others, allowing a device to capture spoken words through a microphone from a human speaker. End-to-end approaches such as Connectionist Temporal Classification (CTC) and attention-based methods are the most used for the development of ASR systems. However, these techniques were commonly used for research and development for many high-resourced languages with large amounts of speech data for training and evaluation, leaving low-resource languages relatively underdeveloped. While the CTC method has been successfully used for other languages, its effectiveness for the Sepedi language remains uncertain. In this study, we present the evaluation of the Sepedi-English code-switched automatic speech recognition system. This end-to-end system was developed using the Sepedi Prompted Code Switching corpus and the CTC approach. The performance of the system was evaluated using both the NCHLT Sepedi test corpus and the Sepedi Prompted Code Switching corpus. The model produced the lowest WER of 41.9%, however, the model faced challenges in recognizing the Sepedi only text.

</details>

### [Real-Time Multimodal Cognitive Assistant for Emergency Medical Services](2403.06734.md)
**Keshara Weerasinghe, Saahith Janapati, Xueren Ge, Sion Kim et al.** · 2024-03-11

<details>
<summary>Abstract</summary>

Emergency Medical Services (EMS) responders often operate under time-sensitive conditions, facing cognitive overload and inherent risks, requiring essential skills in critical thinking and rapid decision-making. This paper presents CognitiveEMS, an end-to-end wearable cognitive assistant system that can act as a collaborative virtual partner engaging in the real-time acquisition and analysis of multimodal data from an emergency scene and interacting with EMS responders through Augmented Reality (AR) smart glasses. CognitiveEMS processes the continuous streams of data in real-time and leverages edge computing to provide assistance in EMS protocol selection and intervention recognition. We address key technical challenges in real-time cognitive assistance by introducing three novel components: (i) a Speech Recognition model that is fine-tuned for real-world medical emergency conversations using simulated EMS audio recordings, augmented with synthetic data generated by large language models (LLMs); (ii) an EMS Protocol Prediction model that combines state-of-the-art (SOTA) tiny language models with EMS domain knowledge using graph-based attention mechanisms; (iii) an EMS Action Recognition module which leverages multimodal audio and video data and protocol predictions to infer the intervention/treatment actions taken by the responders at the incident scene. Our results show that for speech recognition we achieve superior performance compared to SOTA (WER of 0.290 vs. 0.618) on conversational data. Our protocol prediction component also significantly outperforms SOTA (top-3 accuracy of 0.800 vs. 0.200) and the action recognition achieves an accuracy of 0.727, while maintaining an end-to-end latency of 3.78s for protocol prediction on the edge and 0.31s on the server.

</details>

### [SCORE: Self-supervised Correspondence Fine-tuning for Improved Content Representations](2403.06260.md)
**Amit Meghanani, Thomas Hain** · 2024-03-10

<details>
<summary>Abstract</summary>

There is a growing interest in cost-effective self-supervised fine-tuning (SSFT) of self-supervised learning (SSL)-based speech models to obtain task-specific representations. These task-specific representations are used for robust performance on various downstream tasks by fine-tuning on the labelled data. This work presents a cost-effective SSFT method named Self-supervised Correspondence (SCORE) fine-tuning to adapt the SSL speech representations for content-related tasks. The proposed method uses a correspondence training strategy, aiming to learn similar representations from perturbed speech and original speech. Commonly used data augmentation techniques for content-related tasks (ASR) are applied to obtain perturbed speech. SCORE fine-tuned HuBERT outperforms the vanilla HuBERT on SUPERB benchmark with only a few hours of fine-tuning (< 5 hrs) on a single GPU for automatic speech recognition, phoneme recognition, and query-by-example tasks, with relative improvements of 1.09%, 3.58%, and 12.65%, respectively. SCORE provides competitive results with the recently proposed SSFT method SPIN, using only 1/3 of the processed speech compared to SPIN.

</details>

### [Aligning Speech to Languages to Enhance Code-switching Speech Recognition](2403.05887.md)
**Hexin Liu, Xiangyu Zhang, Haoyang Zhang, Leibny Paola Garcia et al.** · 2024-03-09

<details>
<summary>Abstract</summary>

Code-switching (CS) refers to the switching of languages within a speech signal and results in language confusion for automatic speech recognition (ASR). To address language confusion, we propose a language alignment loss (LAL) that aligns acoustic features to pseudo-language labels learned from the ASR decoder during ASR training. This approach enables frame-level language identification without the need for frame-level language annotations. To further tackle the complex token alternatives for language modeling in bilingual scenarios, we propose to employ large language models via a generative error correction method. A linguistic hint, derived from LAL outputs and decoded hypotheses, is introduced to guide the prompting and enhance the LLM-based generative error correction for CS-ASR. The proposed methods are evaluated on the SEAME dataset and data from the ASRU 2019 Mandarin-English code-switching speech recognition challenge. The incorporation of the proposed language alignment loss improves CS-ASR performance for both hybrid CTC/attention and Whisper models on both datasets, with only a negligible increase in the number of parameters. This work also highlights the efficacy of language alignment loss in balancing primary-language-dominant bilingual data during training, with an 8.6% relative improvement on the ASRU dataset compared to the baseline model. Performance evaluation using large language models reveals the advantage of the linguistic hint by achieving 14.1% and 5.5% relative improvement on test sets of the ASRU and SEAME datasets, respectively.

</details>

### [Robust Semantic Communications for Speech Transmission](2403.05187.md)
**Zhenzi Weng, Zhijin Qin, Geoffrey Ye Li** · 2024-03-08

<details>
<summary>Abstract</summary>

In this paper, we propose a robust semantic communication system for speech transmission, named Ross-S2T, by delivering the essential semantic information. Specifically, we consider the speech-to-text translation (S2TT) as the transmission goal. First, a new deep semantic encoder is developed to convert speech in the source language to textual features associated with the target language, facilitating the end-to-end semantic exchange to perform the S2TT task and reducing the transmission data without performance degradation. To mitigate semantic impairments inherent in the corrupted speech, a novel generative adversarial network (GAN)-enabled deep semantic compensator is established to estimate the lost semantic information within the speech and extract deep semantic features simultaneously, which enables robust semantic transmission for corrupted speech. Furthermore, a semantic probe-aided compensator is devised to enhance the semantic fidelity of recovered semantic features and improve the understandability of the target text. According to simulation results, the proposed Ross-S2T exhibits superior S2TT performance compared to conventional approaches and high robustness against semantic impairments.

</details>

### [A Study of Dropout-Induced Modality Bias on Robustness to Missing Video Frames for Audio-Visual Speech Recognition](2403.04245.md)
**Yusheng Dai, Hang Chen, Jun Du, Ruoyu Wang et al.** · 2024-03-07

<details>
<summary>Abstract</summary>

Advanced Audio-Visual Speech Recognition (AVSR) systems have been observed to be sensitive to missing video frames, performing even worse than single-modality models. While applying the dropout technique to the video modality enhances robustness to missing frames, it simultaneously results in a performance loss when dealing with complete data input. In this paper, we investigate this contrasting phenomenon from the perspective of modality bias and reveal that an excessive modality bias on the audio caused by dropout is the underlying reason. Moreover, we present the Modality Bias Hypothesis (MBH) to systematically describe the relationship between modality bias and robustness against missing modality in multimodal systems. Building on these findings, we propose a novel Multimodal Distribution Approximation with Knowledge Distillation (MDA-KD) framework to reduce over-reliance on the audio modality and to maintain performance and robustness simultaneously. Finally, to address an entirely missing modality, we adopt adapters to dynamically switch decision strategies. The effectiveness of our proposed approach is evaluated and validated through a series of comprehensive experiments using the MISP2021 and MISP2022 datasets. Our code is available at https://github.com/dalision/ModalBiasAVSR

</details>

### [Non-verbal information in spontaneous speech -- towards a new framework of analysis](2403.03522.md)
**Tirza Biron, Moshe Barboy, Eran Ben-Artzy, Alona Golubchik et al.** · 2024-03-06

<details>
<summary>Abstract</summary>

Non-verbal signals in speech are encoded by prosody and carry information that ranges from conversation action to attitude and emotion. Despite its importance, the principles that govern prosodic structure are not yet adequately understood. This paper offers an analytical schema and a technological proof-of-concept for the categorization of prosodic signals and their association with meaning. The schema interprets surface-representations of multi-layered prosodic events. As a first step towards implementation, we present a classification process that disentangles prosodic phenomena of three orders. It relies on fine-tuning a pre-trained speech recognition model, enabling the simultaneous multi-class/multi-label detection. It generalizes over a large variety of spontaneous data, performing on a par with, or superior to, human annotation. In addition to a standardized formalization of prosody, disentangling prosodic patterns can direct a theory of communication and speech organization. A welcome by-product is an interpretation of prosody that will enhance speech- and language-related technologies.

</details>

### [PixIT: Joint Training of Speaker Diarization and Speech Separation from Real-world Multi-speaker Recordings](2403.02288.md)
**Joonas Kalda, Clément Pagés, Ricard Marxer, Tanel Alumäe et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

A major drawback of supervised speech separation (SSep) systems is their reliance on synthetic data, leading to poor real-world generalization. Mixture invariant training (MixIT) was proposed as an unsupervised alternative that uses real recordings, yet struggles with overseparation and adapting to long-form audio. We introduce PixIT, a joint approach that combines permutation invariant training (PIT) for speaker diarization (SD) and MixIT for SSep. With a small extra requirement of needing SD labels, it solves the problem of overseparation and allows stitching local separated sources leveraging existing work on clustering-based neural SD. We measure the quality of the separated sources via applying automatic speech recognition (ASR) systems to them. PixIT boosts the performance of various ASR systems across two meeting corpora both in terms of the speaker-attributed and utterance-based word error rates while not requiring any fine-tuning.

</details>

### [What has LeBenchmark Learnt about French Syntax?](2403.02173.md)
**Zdravko Dugonjić, Adrien Pupier, Benjamin Lecouteux, Maximin Coavoux** · 2024-03-04

<details>
<summary>Abstract</summary>

The paper reports on a series of experiments aiming at probing LeBenchmark, a pretrained acoustic model trained on 7k hours of spoken French, for syntactic information. Pretrained acoustic models are increasingly used for downstream speech tasks such as automatic speech recognition, speech translation, spoken language understanding or speech parsing. They are trained on very low level information (the raw speech signal), and do not have explicit lexical knowledge. Despite that, they obtained reasonable results on tasks that requires higher level linguistic knowledge. As a result, an emerging question is whether these models encode syntactic information. We probe each representation layer of LeBenchmark for syntax, using the Orféo treebank, and observe that it has learnt some syntactic information. Our results show that syntactic information is more easily extractable from the middle layers of the network, after which a very sharp decrease is observed.

</details>

### [SA-SOT: Speaker-Aware Serialized Output Training for Multi-Talker ASR](2403.02010.md)
**Zhiyun Fan, Linhao Dong, Jun Zhang, Lu Lu et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

Multi-talker automatic speech recognition plays a crucial role in scenarios involving multi-party interactions, such as meetings and conversations. Due to its inherent complexity, this task has been receiving increasing attention. Notably, the serialized output training (SOT) stands out among various approaches because of its simplistic architecture and exceptional performance. However, the frequent speaker changes in token-level SOT (t-SOT) present challenges for the autoregressive decoder in effectively utilizing context to predict output sequences. To address this issue, we introduce a masked t-SOT label, which serves as the cornerstone of an auxiliary training loss. Additionally, we utilize a speaker similarity matrix to refine the self-attention mechanism of the decoder. This strategic adjustment enhances contextual relationships within the same speaker's tokens while minimizing interactions between different speakers' tokens. We denote our method as speaker-aware SOT (SA-SOT). Experiments on the Librispeech datasets demonstrate that our SA-SOT obtains a relative cpWER reduction ranging from 12.75% to 22.03% on the multi-talker test sets. Furthermore, with more extensive training, our method achieves an impressive cpWER of 3.41%, establishing a new state-of-the-art result on the LibrispeechMix dataset.

</details>

### [JEP-KD: Joint-Embedding Predictive Architecture Based Knowledge Distillation for Visual Speech Recognition](2403.18843.md)
**Chang Sun, Hong Yang, Bo Qin** · 2024-03-04

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) tasks are generally recognized to have a lower theoretical performance ceiling than Automatic Speech Recognition (ASR), owing to the inherent limitations of conveying semantic information visually. To mitigate this challenge, this paper introduces an advanced knowledge distillation approach using a Joint-Embedding Predictive Architecture (JEPA), named JEP-KD, designed to more effectively utilize audio features during model training. Central to JEP-KD is the inclusion of a generative network within the embedding layer, which enhances the video encoder's capacity for semantic feature extraction and brings it into closer alignment with the audio features from a pre-trained ASR model's encoder. This approach aims to progressively reduce the performance gap between VSR and ASR. Moreover, a comprehensive multimodal, multistage training regimen for the JEP-KD framework is established, bolstering the robustness and efficacy of the training process. Experiment results demonstrate that JEP-KD significantly improves the performance of VSR models and demonstrates versatility across different VSR platforms, indicating its potential for broader application within other multimodal tasks.

</details>

### [Brilla AI: AI Contestant for the National Science and Maths Quiz](2403.01699.md)
**George Boateng, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

The African continent lacks enough qualified teachers which hampers the provision of adequate learning support. An AI could potentially augment the efforts of the limited number of teachers, leading to better learning outcomes. Towards that end, this work describes and evaluates the first key output for the NSMQ AI Grand Challenge, which proposes a robust, real-world benchmark for such an AI: "Build an AI to compete live in Ghana's National Science and Maths Quiz (NSMQ) competition and win - performing better than the best contestants in all rounds and stages of the competition". The NSMQ is an annual live science and mathematics competition for senior secondary school students in Ghana in which 3 teams of 2 students compete by answering questions across biology, chemistry, physics, and math in 5 rounds over 5 progressive stages until a winning team is crowned for that year. In this work, we built Brilla AI, an AI contestant that we deployed to unofficially compete remotely and live in the Riddles round of the 2023 NSMQ Grand Finale, the first of its kind in the 30-year history of the competition. Brilla AI is currently available as a web app that livestreams the Riddles round of the contest, and runs 4 machine learning systems: (1) speech to text (2) question extraction (3) question answering and (4) text to speech that work together in real-time to quickly and accurately provide an answer, and then say it with a Ghanaian accent. In its debut, our AI answered one of the 4 riddles ahead of the 3 human contesting teams, unofficially placing second (tied). Improvements and extensions of this AI could potentially be deployed to offer science tutoring to students and eventually enable millions across Africa to have one-on-one learning interactions, democratizing science education.

</details>

### [A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition](2403.05583.md)
**Tyler Benster, Guy Wilson, Reshef Elisha, Francis R Willett et al.** · 2024-03-02

<details>
<summary>Abstract</summary>

Silent Speech Interfaces (SSIs) offer a noninvasive alternative to brain-computer interfaces for soundless verbal communication. We introduce Multimodal Orofacial Neural Audio (MONA), a system that leverages cross-modal alignment through novel loss functions--cross-contrast (crossCon) and supervised temporal contrast (supTcon)--to train a multimodal model with a shared latent representation. This architecture enables the use of audio-only datasets like LibriSpeech to improve silent speech recognition. Additionally, our introduction of Large Language Model (LLM) Integrated Scoring Adjustment (LISA) significantly improves recognition accuracy. Together, MONA LISA reduces the state-of-the-art word error rate (WER) from 28.8% to 12.2% in the Gaddy (2020) benchmark dataset for silent speech on an open vocabulary. For vocal EMG recordings, our method improves the state-of-the-art from 23.3% to 3.7% WER. In the Brain-to-Text 2024 competition, LISA performs best, improving the top WER from 9.8% to 8.9%. To the best of our knowledge, this work represents the first instance where noninvasive silent speech recognition on an open vocabulary has cleared the threshold of 15% WER, demonstrating that SSIs can be a viable alternative to automatic speech recognition (ASR). Our work not only narrows the performance gap between silent and vocalized speech but also opens new possibilities in human-computer interaction, demonstrating the potential of cross-modal approaches in noisy and data-limited regimes.

</details>

### [Automatic Speech Recognition using Advanced Deep Learning Approaches: A survey](2403.01255.md)
**Hamza Kheddar, Mustapha Hemis, Yassine Himeur** · 2024-03-02

<details>
<summary>Abstract</summary>

Recent advancements in deep learning (DL) have posed a significant challenge for automatic speech recognition (ASR). ASR relies on extensive training datasets, including confidential ones, and demands substantial computational and storage resources. Enabling adaptive systems improves ASR performance in dynamic environments. DL techniques assume training and testing data originate from the same domain, which is not always true. Advanced DL techniques like deep transfer learning (DTL), federated learning (FL), and reinforcement learning (RL) address these issues. DTL allows high-performance models using small yet related datasets, FL enables training on confidential data without dataset possession, and RL optimizes decision-making in dynamic environments, reducing computation costs. This survey offers a comprehensive review of DTL, FL, and RL-based ASR frameworks, aiming to provide insights into the latest developments and aid researchers and professionals in understanding the current challenges. Additionally, transformers, which are advanced DL techniques heavily used in proposed ASR frameworks, are considered in this survey for their ability to capture extensive dependencies in the input ASR sequence. The paper starts by presenting the background of DTL, FL, RL, and Transformers and then adopts a well-designed taxonomy to outline the state-of-the-art approaches. Subsequently, a critical analysis is conducted to identify the strengths and weaknesses of each framework. Additionally, a comparative study is presented to highlight the existing challenges, paving the way for future research opportunities.

</details>

### [Post-decoder Biasing for End-to-End Speech Recognition of Multi-turn Medical Interview](2403.00370.md)
**Heyang Liu, Yu Wang, Yanfeng Wang** · 2024-03-01

<details>
<summary>Abstract</summary>

End-to-end (E2E) approach is gradually replacing hybrid models for automatic speech recognition (ASR) tasks. However, the optimization of E2E models lacks an intuitive method for handling decoding shifts, especially in scenarios with a large number of domain-specific rare words that hold specific important meanings. Furthermore, the absence of knowledge-intensive speech datasets in academia has been a significant limiting factor, and the commonly used speech corpora exhibit significant disparities with realistic conversation. To address these challenges, we present Medical Interview (MED-IT), a multi-turn consultation speech dataset that contains a substantial number of knowledge-intensive named entities. We also explore methods to enhance the recognition performance of rare words for E2E models. We propose a novel approach, post-decoder biasing, which constructs a transform probability matrix based on the distribution of training transcriptions. This guides the model to prioritize recognizing words in the biasing list. In our experiments, for subsets of rare words appearing in the training speech between 10 and 20 times, and between 1 and 5 times, the proposed method achieves a relative improvement of 9.3% and 5.1%, respectively.

</details>

### [Inappropriate Pause Detection In Dysarthric Speech Using Large-Scale Speech Recognition](2402.18923.md)
**Jeehyun Lee, Yerin Choi, Tae-Jin Song, Myoung-Wan Koo** · 2024-02-29

<details>
<summary>Abstract</summary>

Dysarthria, a common issue among stroke patients, severely impacts speech intelligibility. Inappropriate pauses are crucial indicators in severity assessment and speech-language therapy. We propose to extend a large-scale speech recognition model for inappropriate pause detection in dysarthric speech. To this end, we propose task design, labeling strategy, and a speech recognition model with an inappropriate pause prediction layer. First, we treat pause detection as speech recognition, using an automatic speech recognition (ASR) model to convert speech into text with pause tags. According to the newly designed task, we label pause locations at the text level and their appropriateness. We collaborate with speech-language pathologists to establish labeling criteria, ensuring high-quality annotated data. Finally, we extend the ASR model with an inappropriate pause prediction layer for end-to-end inappropriate pause detection. Moreover, we propose a task-tailored metric for evaluating inappropriate pause detection independent of ASR performance. Our experiments show that the proposed method better detects inappropriate pauses in dysarthric speech than baselines. (Inappropriate Pause Error Rate: 14.47%)

</details>

### [Compact Speech Translation Models via Discrete Speech Units Pretraining](2402.19333.md)
**Tsz Kin Lam, Alexandra Birch, Barry Haddow** · 2024-02-29

<details>
<summary>Abstract</summary>

We propose a pretraining method to use Self-Supervised Speech (SSS) model to creating more compact Speech-to-text Translation. In contrast to using the SSS model for initialization, our method is more suitable to memory constrained scenario such as on-device deployment. Our method is based on Discrete Speech Units (DSU) extracted from the SSS model. In the first step, our method pretrains two smaller encoder-decoder models on 1) Filterbank-to-DSU (Fbk-to-DSU) and 2) DSU-to-Translation (DSU-to-Trl) data respectively. The DSU thus become the distillation inputs of the smaller models. Subsequently, the encoder from the Fbk-to-DSU model and the decoder from the DSU-to-Trl model are taken to initialise the compact model. Finally, the compact model is finetuned on the paired Fbk-Trl data. In addition to being compact, our method requires no transcripts, making it applicable to low-resource settings. It also avoids speech discretization in inference and is more robust to the DSU tokenization. Evaluation on CoVoST-2 (X-En) shows that our method has consistent improvement over the baseline in three metrics while being compact i.e., only half the SSS model size.

</details>

### [Exploration of Adapter for Noise Robust Automatic Speech Recognition](2402.18275.md)
**Hao Shi, Tatsuya Kawahara** · 2024-02-28

<details>
<summary>Abstract</summary>

Adapting an automatic speech recognition (ASR) system to unseen noise environments is crucial. Integrating adapters into neural networks has emerged as a potent technique for transfer learning. This study thoroughly investigates adapter-based ASR adaptation in noisy environments. We conducted experiments using the CHiME--4 dataset. The results show that inserting the adapter in the shallow layer yields superior effectiveness, and there is no significant difference between adapting solely within the shallow layer and adapting across all layers. The simulated data helps the system to improve its performance under real noise conditions. Nonetheless, when the amount of data is the same, the real data is more effective than the simulated data. Multi-condition training is still useful for adapter training. Furthermore, integrating adapters into speech enhancement-based ASR systems yields substantial improvements.

</details>

### [An Effective Mixture-Of-Experts Approach For Code-Switching Speech Recognition Leveraging Encoder Disentanglement](2402.17189.md)
**Tzu-Ting Yang, Hsin-Wei Wang, Yi-Cheng Wang, Chi-Han Lin et al.** · 2024-02-27

<details>
<summary>Abstract</summary>

With the massive developments of end-to-end (E2E) neural networks, recent years have witnessed unprecedented breakthroughs in automatic speech recognition (ASR). However, the codeswitching phenomenon remains a major obstacle that hinders ASR from perfection, as the lack of labeled data and the variations between languages often lead to degradation of ASR performance. In this paper, we focus exclusively on improving the acoustic encoder of E2E ASR to tackle the challenge caused by the codeswitching phenomenon. Our main contributions are threefold: First, we introduce a novel disentanglement loss to enable the lower-layer of the encoder to capture inter-lingual acoustic information while mitigating linguistic confusion at the higher-layer of the encoder. Second, through comprehensive experiments, we verify that our proposed method outperforms the prior-art methods using pretrained dual-encoders, meanwhile having access only to the codeswitching corpus and consuming half of the parameterization. Third, the apparent differentiation of the encoders' output features also corroborates the complementarity between the disentanglement loss and the mixture-of-experts (MoE) architecture.

</details>

### [Extreme Encoder Output Frame Rate Reduction: Improving Computational Latencies of Large End-to-End Models](2402.17184.md)
**Rohit Prabhavalkar, Zhong Meng, Weiran Wang, Adam Stooke et al.** · 2024-02-27

<details>
<summary>Abstract</summary>

The accuracy of end-to-end (E2E) automatic speech recognition (ASR) models continues to improve as they are scaled to larger sizes, with some now reaching billions of parameters. Widespread deployment and adoption of these models, however, requires computationally efficient strategies for decoding. In the present work, we study one such strategy: applying multiple frame reduction layers in the encoder to compress encoder outputs into a small number of output frames. While similar techniques have been investigated in previous work, we achieve dramatically more reduction than has previously been demonstrated through the use of multiple funnel reduction layers. Through ablations, we study the impact of various architectural choices in the encoder to identify the most effective strategies. We demonstrate that we can generate one encoder output frame for every 2.56 sec of input speech, without significantly affecting word error rate on a large-scale voice search task, while improving encoder and decoder latencies by 48% and 92% respectively, relative to a strong but computationally expensive baseline.

</details>

### [Direct Punjabi to English speech translation using discrete units](2402.15967.md)
**Prabhjot Kaur, L. Andrew M. Bush, Weisong Shi** · 2024-02-25

<details>
<summary>Abstract</summary>

Speech-to-speech translation is yet to reach the same level of coverage as text-to-text translation systems. The current speech technology is highly limited in its coverage of over 7000 languages spoken worldwide, leaving more than half of the population deprived of such technology and shared experiences. With voice-assisted technology (such as social robots and speech-to-text apps) and auditory content (such as podcasts and lectures) on the rise, ensuring that the technology is available for all is more important than ever. Speech translation can play a vital role in mitigating technological disparity and creating a more inclusive society. With a motive to contribute towards speech translation research for low-resource languages, our work presents a direct speech-to-speech translation model for one of the Indic languages called Punjabi to English. Additionally, we explore the performance of using a discrete representation of speech called discrete acoustic units as input to the Transformer-based translation model. The model, abbreviated as Unit-to-Unit Translation (U2UT), takes a sequence of discrete units of the source language (the language being translated from) and outputs a sequence of discrete units of the target language (the language being translated to). Our results show that the U2UT model performs better than the Speech-to-Unit Translation (S2UT) model by a 3.69 BLEU score.

</details>

### [Text-guided HuBERT: Self-Supervised Speech Pre-training via Generative Adversarial Networks](2402.15725.md)
**Duo Ma, Xianghu Yue, Junyi Ao, Xiaoxue Gao et al.** · 2024-02-24

<details>
<summary>Abstract</summary>

Human language can be expressed in either written or spoken form, i.e. text or speech. Humans can acquire knowledge from text to improve speaking and listening. However, the quest for speech pre-trained models to leverage unpaired text has just started. In this paper, we investigate a new way to pre-train such a joint speech-text model to learn enhanced speech representations and benefit various speech-related downstream tasks. Specifically, we propose a novel pre-training method, text-guided HuBERT, or T-HuBERT, which performs self-supervised learning over speech to derive phoneme-like discrete representations. And these phoneme-like pseudo-label sequences are firstly derived from speech via the generative adversarial networks (GAN) to be statistically similar to those from additional unpaired textual data. In this way, we build a bridge between unpaired speech and text in an unsupervised manner. Extensive experiments demonstrate the significant superiority of our proposed method over various strong baselines, which achieves up to 15.3% relative Word Error Rate (WER) reduction on the LibriSpeech dataset.

</details>

### [Where Visual Speech Meets Language: VSP-LLM Framework for Efficient and Context-Aware Visual Speech Processing](2402.15151.md)
**Jeong Hun Yeo, Seunghee Han, Minsu Kim, Yong Man Ro** · 2024-02-23

<details>
<summary>Abstract</summary>

In visual speech processing, context modeling capability is one of the most important requirements due to the ambiguous nature of lip movements. For example, homophenes, words that share identical lip movements but produce different sounds, can be distinguished by considering the context. In this paper, we propose a novel framework, namely Visual Speech Processing incorporated with LLMs (VSP-LLM), to maximize the context modeling ability by bringing the overwhelming power of LLMs. Specifically, VSP-LLM is designed to perform multi-tasks of visual speech recognition and translation, where the given instructions control the type of task. The input video is mapped to the input latent space of an LLM by employing a self-supervised visual speech model. Focused on the fact that there is redundant information in input frames, we propose a novel deduplication method that reduces the embedded visual features by employing visual speech units. Through the proposed deduplication and Low Rank Adaptation (LoRA), VSP-LLM can be trained in a computationally efficient manner. In the translation dataset, the MuAViC benchmark, we demonstrate that VSP-LLM trained on just 30 hours of labeled data can more effectively translate lip movements compared to the recent model trained with 433 hours of data.

</details>

### [Hands-Free VR](2402.15083.md)
**Jorge Askur Vazquez Fernandez, Jae Joong Lee, Santiago Andrés Serrano Vacca, Alejandra Magana et al.** · 2024-02-23

<details>
<summary>Abstract</summary>

The paper introduces Hands-Free VR, a voice-based natural-language interface for VR. The user gives a command using their voice, the speech audio data is converted to text using a speech-to-text deep learning model that is fine-tuned for robustness to word phonetic similarity and to spoken English accents, and the text is mapped to an executable VR command using a large language model that is robust to natural language diversity. Hands-Free VR was evaluated in a controlled within-subjects study (N = 22) that asked participants to find specific objects and to place them in various configurations. In the control condition participants used a conventional VR user interface to grab, carry, and position the objects using the handheld controllers. In the experimental condition participants used Hands-Free VR. The results confirm that: (1) Hands-Free VR is robust to spoken English accents, as for 20 of our participants English was not their first language, and to word phonetic similarity, correctly transcribing the voice command 96.71% of the time; (2) Hands-Free VR is robust to natural language diversity, correctly mapping the transcribed command to an executable command in 97.83% of the time; (3) Hands-Free VR had a significant efficiency advantage over the conventional VR interface in terms of task completion time, total viewpoint translation, total view direction rotation, and total left and right hand translations; (4) Hands-Free VR received high user preference ratings in terms of ease of use, intuitiveness, ergonomics, reliability, and desirability.

</details>

### [Alternating Weak Triphone/BPE Alignment Supervision from Hybrid Model Improves End-to-End ASR](2402.15594.md)
**Jintao Jiang, Yingbo Gao, Mohammad Zeineldeen, Zoltan Tuske** · 2024-02-23

<details>
<summary>Abstract</summary>

In this paper, alternating weak triphone/BPE alignment supervision is proposed to improve end-to-end model training. Towards this end, triphone and BPE alignments are extracted using a pre-existing hybrid ASR system. Then, regularization effect is obtained by cross-entropy based intermediate auxiliary losses computed on such alignments at a mid-layer representation of the encoder for triphone alignments and at the encoder for BPE alignments. Weak supervision is achieved through strong label smoothing with parameter of 0.5. Experimental results on TED-LIUM 2 indicate that either triphone or BPE alignment based weak supervision improves ASR performance over standard CTC auxiliary loss. Moreover, their combination lowers the word error rate further. We also investigate the alternation of the two auxiliary tasks during model training, and additional performance gain is observed. Overall, the proposed techniques result in over 10% relative error rate reduction over a CTC-regularized baseline system.

</details>

### [HINT: High-quality INPainting Transformer with Mask-Aware Encoding and Enhanced Attention](2402.14185.md)
**Shuang Chen, Amir Atapour-Abarghouei, Hubert P. H. Shum** · 2024-02-22

<details>
<summary>Abstract</summary>

Existing image inpainting methods leverage convolution-based downsampling approaches to reduce spatial dimensions. This may result in information loss from corrupted images where the available information is inherently sparse, especially for the scenario of large missing regions. Recent advances in self-attention mechanisms within transformers have led to significant improvements in many computer vision tasks including inpainting. However, limited by the computational costs, existing methods cannot fully exploit the efficacy of long-range modelling capabilities of such models. In this paper, we propose an end-to-end High-quality INpainting Transformer, abbreviated as HINT, which consists of a novel mask-aware pixel-shuffle downsampling module (MPD) to preserve the visible information extracted from the corrupted image while maintaining the integrity of the information available for high-level inferences made within the model. Moreover, we propose a Spatially-activated Channel Attention Layer (SCAL), an efficient self-attention mechanism interpreting spatial awareness to model the corrupted image at multiple scales. To further enhance the effectiveness of SCAL, motivated by recent advanced in speech recognition, we introduce a sandwich structure that places feed-forward networks before and after the SCAL module. We demonstrate the superior performance of HINT compared to contemporary state-of-the-art models on four datasets, CelebA, CelebA-HQ, Places2, and Dunhuang.

</details>

### [An Augmented Lagrangian Method for Training Recurrent Neural Networks](2402.13687.md)
**Yue Wang, Chao Zhang, Xiaojun Chen** · 2024-02-21

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are widely used to model sequential data in a wide range of areas, such as natural language processing, speech recognition, machine translation, and time series analysis. In this paper, we model the training process of RNNs with the ReLU activation function as a constrained optimization problem with a smooth nonconvex objective function and piecewise smooth nonconvex constraints. We prove that any feasible point of the optimization problem satisfies the no nonzero abnormal multiplier constraint qualification (NNAMCQ), and any local minimizer is a Karush-Kuhn-Tucker (KKT) point of the problem. Moreover, we propose an augmented Lagrangian method (ALM) and design an efficient block coordinate descent (BCD) method to solve the subproblems of the ALM. The update of each block of the BCD method has a closed-form solution. The stop criterion for the inner loop is easy to check and can be stopped in finite steps. Moreover, we show that the BCD method can generate a directional stationary point of the subproblem. Furthermore, we establish the global convergence of the ALM to a KKT point of the constrained optimization problem. Compared with the state-of-the-art algorithms, numerical results demonstrate the efficiency and effectiveness of the ALM for training RNNs.

</details>

### [Mel-FullSubNet: Mel-Spectrogram Enhancement for Improving Both Speech Quality and ASR](2402.13511.md)
**Rui Zhou, Xian Li, Ying Fang, Xiaofei Li** · 2024-02-21

<details>
<summary>Abstract</summary>

In this work, we propose Mel-FullSubNet, a single-channel Mel-spectrogram denoising and dereverberation network for improving both speech quality and automatic speech recognition (ASR) performance. Mel-FullSubNet takes as input the noisy and reverberant Mel-spectrogram and predicts the corresponding clean Mel-spectrogram. The enhanced Mel-spectrogram can be either transformed to speech waveform with a neural vocoder or directly used for ASR. Mel-FullSubNet encapsulates interleaved full-band and sub-band networks, for learning the full-band spectral pattern of signals and the sub-band/narrow-band properties of signals, respectively. Compared to linear-frequency domain or time-domain speech enhancement, the major advantage of Mel-spectrogram enhancement is that Mel-frequency presents speech in a more compact way and thus is easier to learn, which will benefit both speech quality and ASR. Experimental results demonstrate a significant improvement in both speech quality and ASR performance achieved by the proposed model.

</details>

### [How do Hyenas deal with Human Speech? Speech Recognition and Translation with ConfHyena](2402.13208.md)
**Marco Gaido, Sara Papi, Matteo Negri, Luisa Bentivogli** · 2024-02-20

<details>
<summary>Abstract</summary>

The attention mechanism, a cornerstone of state-of-the-art neural models, faces computational hurdles in processing long sequences due to its quadratic complexity. Consequently, research efforts in the last few years focused on finding more efficient alternatives. Among them, Hyena (Poli et al., 2023) stands out for achieving competitive results in both language modeling and image classification, while offering sub-quadratic memory and computational complexity. Building on these promising results, we propose ConfHyena, a Conformer whose encoder self-attentions are replaced with an adaptation of Hyena for speech processing, where the long input sequences cause high computational costs. Through experiments in automatic speech recognition (for English) and translation (from English into 8 target languages), we show that our best ConfHyena model significantly reduces the training time by 27%, at the cost of minimal quality degradation (~1%), which, in most cases, is not statistically significant.

</details>

### [Comparison of Conventional Hybrid and CTC/Attention Decoders for Continuous Visual Speech Recognition](2402.13004.md)
**David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2024-02-20

<details>
<summary>Abstract</summary>

Thanks to the rise of deep learning and the availability of large-scale audio-visual databases, recent advances have been achieved in Visual Speech Recognition (VSR). Similar to other speech processing tasks, these end-to-end VSR systems are usually based on encoder-decoder architectures. While encoders are somewhat general, multiple decoding approaches have been explored, such as the conventional hybrid model based on Deep Neural Networks combined with Hidden Markov Models (DNN-HMM) or the Connectionist Temporal Classification (CTC) paradigm. However, there are languages and tasks in which data is scarce, and in this situation, there is not a clear comparison between different types of decoders. Therefore, we focused our study on how the conventional DNN-HMM decoder and its state-of-the-art CTC/Attention counterpart behave depending on the amount of data used for their estimation. We also analyzed to what extent our visual speech features were able to adapt to scenarios for which they were not explicitly trained, either considering a similar dataset or another collected for a different language. Results showed that the conventional paradigm reached recognition rates that improve the CTC/Attention model in data-scarcity scenarios along with a reduced training time and fewer parameters.

</details>

### [OWSM-CTC: An Open Encoder-Only Speech Foundation Model for Speech Recognition, Translation, and Language Identification](2402.12654.md)
**Yifan Peng, Yui Sudo, Muhammad Shakeel, Shinji Watanabe** · 2024-02-20

<details>
<summary>Abstract</summary>

There has been an increasing interest in large speech models that can perform multiple tasks in a single model. Such models usually adopt an encoder-decoder or decoder-only architecture due to their popularity and good performance in many domains. However, autoregressive models can be slower during inference compared to non-autoregressive models and also have potential risks of hallucination. Though prior studies observed promising results of non-autoregressive models for certain tasks at small scales, it remains unclear if they can be scaled to speech-to-text generation in diverse languages and tasks. Inspired by the Open Whisper-style Speech Model (OWSM) project, we propose OWSM-CTC, a novel encoder-only speech foundation model based on Connectionist Temporal Classification (CTC). It is trained on 180k hours of public audio data for multilingual automatic speech recognition (ASR), speech translation (ST), and language identification (LID). Compared to encoder-decoder OWSM, our OWSM-CTC achieves competitive results on ASR and up to 24% relative improvement on ST, while it is more robust and 3 to 4 times faster for inference. OWSM-CTC also improves the long-form ASR result with 20x speed-up. We will publicly release our code, pre-trained model, and training logs to promote open science in speech foundation models.

</details>

### [Television Discourse Decoded: Comprehensive Multimodal Analytics at Scale](2402.12629.md)
**Anmol Agarwal, Pratyush Priyadarshi, Shiven Sinha, Shrey Gupta et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

In this paper, we tackle the complex task of analyzing televised debates, with a focus on a prime time news debate show from India. Previous methods, which often relied solely on text, fall short in capturing the multimodal essence of these debates. To address this gap, we introduce a comprehensive automated toolkit that employs advanced computer vision and speech-to-text techniques for large-scale multimedia analysis. Utilizing state-of-the-art computer vision algorithms and speech-to-text methods, we transcribe, diarize, and analyze thousands of YouTube videos of a prime-time television debate show in India. These debates are a central part of Indian media but have been criticized for compromised journalistic integrity and excessive dramatization. Our toolkit provides concrete metrics to assess bias and incivility, capturing a comprehensive multimedia perspective that includes text, audio utterances, and video frames. Our findings reveal significant biases in topic selection and panelist representation, along with alarming levels of incivility. This work offers a scalable, automated approach for future research in multimedia analysis, with profound implications for the quality of public discourse and democratic debate. To catalyze further research in this area, we also release the code, dataset collected and supplemental pdf.

</details>

### [Aria Everyday Activities Dataset](2402.13349.md)
**Zhaoyang Lv, Nicholas Charron, Pierre Moulon, Alexander Gamino et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

We present Aria Everyday Activities (AEA) Dataset, an egocentric multimodal open dataset recorded using Project Aria glasses. AEA contains 143 daily activity sequences recorded by multiple wearers in five geographically diverse indoor locations. Each of the recording contains multimodal sensor data recorded through the Project Aria glasses. In addition, AEA provides machine perception data including high frequency globally aligned 3D trajectories, scene point cloud, per-frame 3D eye gaze vector and time aligned speech transcription. In this paper, we demonstrate a few exemplar research applications enabled by this dataset, including neural scene reconstruction and prompted segmentation. AEA is an open source dataset that can be downloaded from https://www.projectaria.com/datasets/aea/. We are also providing open-source implementations and examples of how to use the dataset in Project Aria Tools https://github.com/facebookresearch/projectaria_tools.

</details>

### [Speech Translation with Speech Foundation Models and Large Language Models: What is There and What is Missing?](2402.12025.md)
**Marco Gaido, Sara Papi, Matteo Negri, Luisa Bentivogli** · 2024-02-19

<details>
<summary>Abstract</summary>

The field of natural language processing (NLP) has recently witnessed a transformative shift with the emergence of foundation models, particularly Large Language Models (LLMs) that have revolutionized text-based NLP. This paradigm has extended to other modalities, including speech, where researchers are actively exploring the combination of Speech Foundation Models (SFMs) and LLMs into single, unified models capable of addressing multimodal tasks. Among such tasks, this paper focuses on speech-to-text translation (ST). By examining the published papers on the topic, we propose a unified view of the architectural solutions and training strategies presented so far, highlighting similarities and differences among them. Based on this examination, we not only organize the lessons learned but also show how diverse settings and evaluation approaches hinder the identification of the best-performing solution for each architectural building block and training choice. Lastly, we outline recommendations for future works on the topic aimed at better understanding the strengths and weaknesses of the SFM+LLM solutions for ST.

</details>

### [Cross-Attention Fusion of Visual and Geometric Features for Large Vocabulary Arabic Lipreading](2402.11520.md)
**Samar Daou, Achraf Ben-Hamadou, Ahmed Rekik, Abdelaziz Kallel** · 2024-02-18

<details>
<summary>Abstract</summary>

Lipreading involves using visual data to recognize spoken words by analyzing the movements of the lips and surrounding area. It is a hot research topic with many potential applications, such as human-machine interaction and enhancing audio speech recognition. Recent deep-learning based works aim to integrate visual features extracted from the mouth region with landmark points on the lip contours. However, employing a simple combination method such as concatenation may not be the most effective approach to get the optimal feature vector. To address this challenge, firstly, we propose a cross-attention fusion-based approach for large lexicon Arabic vocabulary to predict spoken words in videos. Our method leverages the power of cross-attention networks to efficiently integrate visual and geometric features computed on the mouth region. Secondly, we introduce the first large-scale Lipreading in the Wild for Arabic (LRW-AR) dataset containing 20,000 videos for 100-word classes, uttered by 36 speakers. The experimental results obtained on LRW-AR and ArabicVisual databases showed the effectiveness and robustness of the proposed approach in recognizing Arabic words. Our work provides insights into the feasibility and effectiveness of applying lipreading techniques to the Arabic language, opening doors for further research in this field. Link to the project page: https://crns-smartvision.github.io/lrwar

</details>

### [Pushing the Limits of Zero-shot End-to-End Speech Translation](2402.10422.md)
**Ioannis Tsiamas, Gerard I. Gállego, José A. R. Fonollosa, Marta R. Costa-jussà** · 2024-02-16

<details>
<summary>Abstract</summary>

Data scarcity and the modality gap between the speech and text modalities are two major obstacles of end-to-end Speech Translation (ST) systems, thus hindering their performance. Prior work has attempted to mitigate these challenges by leveraging external MT data and optimizing distance metrics that bring closer the speech-text representations. However, achieving competitive results typically requires some ST data. For this reason, we introduce ZeroSwot, a method for zero-shot ST that bridges the modality gap without any paired ST data. Leveraging a novel CTC compression and Optimal Transport, we train a speech encoder using only ASR data, to align with the representation space of a massively multilingual MT model. The speech encoder seamlessly integrates with the MT model at inference, enabling direct translation from speech to text, across all languages supported by the MT model. Our experiments show that we can effectively close the modality gap without ST data, while our results on MuST-C and CoVoST demonstrate our method's superiority over not only previous zero-shot models, but also supervised ones, achieving state-of-the-art results.

</details>

### [Listening to Multi-talker Conversations: Modular and End-to-end Perspectives](2402.08932.md)
**Desh Raj** · 2024-02-14

<details>
<summary>Abstract</summary>

Since the first speech recognition systems were built more than 30 years ago, improvement in voice technology has enabled applications such as smart assistants and automated customer support. However, conversation intelligence of the future requires recognizing free-flowing multi-party conversations, which is a crucial and challenging component that still remains unsolved. In this dissertation, we focus on this problem of speaker-attributed multi-talker speech recognition, and propose two perspectives which result from its probabilistic formulation. In the modular perspective, we build a pipeline of sub-tasks involving speaker diarization, target speaker extraction, and speech recognition. Our first contribution is a method to perform overlap-aware diarization by reformulating spectral clustering as a constrained optimization problem. We also describe an algorithm to ensemble diarization outputs, either to combine overlap-aware systems or to perform multi-channel diarization by late fusion. Once speaker segments are identified, we robustly extract single-speaker utterances from the mixture using a GPU-accelerated implementation of guided source separation, which allows us to use an off-the-shelf ASR system to obtain speaker-attributed transcripts. Since the modular approach suffers from error propagation, we propose an alternate "end-to-end" perspective on the problem. For this, we describe the Streaming Unmixing and Recognition Transducer (SURT). We show how to train SURT models efficiently by carefully designing the network architecture, objective functions, and mixture simulation techniques. Finally, we add an auxiliary speaker branch to enable joint prediction of speaker labels synchronized with the speech tokens. We demonstrate that training on synthetic mixtures and adapting with real data helps these models transfer well for streaming transcription of real meeting sessions.

</details>

### [UniEnc-CASSNAT: An Encoder-only Non-autoregressive ASR for Speech SSL Models](2402.08898.md)
**Ruchao Fan, Natarajan Balaji Shanka, Abeer Alwan** · 2024-02-14

<details>
<summary>Abstract</summary>

Non-autoregressive automatic speech recognition (NASR) models have gained attention due to their parallelism and fast inference. The encoder-based NASR, e.g. connectionist temporal classification (CTC), can be initialized from the speech foundation models (SFM) but does not account for any dependencies among intermediate tokens. The encoder-decoder-based NASR, like CTC alignment-based single-step non-autoregressive transformer (CASS-NAT), can mitigate the dependency problem but is not able to efficiently integrate SFM. Inspired by the success of recent work of speech-text joint pre-training with a shared transformer encoder, we propose a new encoder-based NASR, UniEnc-CASSNAT, to combine the advantages of CTC and CASS-NAT. UniEnc-CASSNAT consists of only an encoder as the major module, which can be the SFM. The encoder plays the role of both the CASS-NAT encoder and decoder by two forward passes. The first pass of the encoder accepts the speech signal as input, while the concatenation of the speech signal and the token-level acoustic embedding is used as the input for the second pass. Examined on the Librispeech 100h, MyST, and Aishell1 datasets, the proposed UniEnc-CASSNAT achieves state-of-the-art NASR results and is better or comparable to CASS-NAT with only an encoder and hence, fewer model parameters. Our codes are publicly available.

</details>

### [An Embarrassingly Simple Approach for LLM with Strong ASR Capacity](2402.08846.md)
**Ziyang Ma, Guanrou Yang, Yifan Yang, Zhifu Gao et al.** · 2024-02-13

<details>
<summary>Abstract</summary>

In this paper, we focus on solving one of the most important tasks in the field of speech processing, i.e., automatic speech recognition (ASR), with speech foundation encoders and large language models (LLM). Recent works have complex designs such as compressing the output temporally for the speech encoder, tackling modal alignment for the projector, and utilizing parameter-efficient fine-tuning for the LLM. We found that delicate designs are not necessary, while an embarrassingly simple composition of off-the-shelf speech encoder, LLM, and the only trainable linear projector is competent for the ASR task. To be more specific, we benchmark and explore various combinations of LLMs and speech encoders, leading to the optimal LLM-based ASR system, which we call SLAM-ASR. The proposed SLAM-ASR provides a clean setup and little task-specific design, where only the linear projector is trained. To the best of our knowledge, SLAM-ASR achieves the best performance on the Librispeech benchmark among LLM-based ASR models and even outperforms the latest LLM-based audio-universal model trained on massive pair data. Finally, we explore the capability emergence of LLM-based ASR in the process of modal alignment. We hope that our study can facilitate the research on extending LLM with cross-modality capacity and shed light on the LLM-based ASR community.

</details>

### [Syllable based DNN-HMM Cantonese Speech to Text System](2402.08788.md)
**Timothy Wong, Claire Li, Sam Lam, Billy Chiu et al.** · 2024-02-13

<details>
<summary>Abstract</summary>

This paper reports our work on building up a Cantonese Speech-to-Text (STT) system with a syllable based acoustic model. This is a part of an effort in building a STT system to aid dyslexic students who have cognitive deficiency in writing skills but have no problem expressing their ideas through speech. For Cantonese speech recognition, the basic unit of acoustic models can either be the conventional Initial-Final (IF) syllables, or the Onset-Nucleus-Coda (ONC) syllables where finals are further split into nucleus and coda to reflect the intra-syllable variations in Cantonese. By using the Kaldi toolkit, our system is trained using the stochastic gradient descent optimization model with the aid of GPUs for the hybrid Deep Neural Network and Hidden Markov Model (DNN-HMM) with and without I-vector based speaker adaptive training technique. The input features of the same Gaussian Mixture Model with speaker adaptive training (GMM-SAT) to DNN are used in all cases. Experiments show that the ONC-based syllable acoustic modeling with I-vector based DNN-HMM achieves the best performance with the word error rate (WER) of 9.66% and the real time factor (RTF) of 1.38812.

</details>

### [AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension](2402.07729.md)
**Qian Yang, Jin Xu, Wenrui Liu, Yunfei Chu et al.** · 2024-02-12

<details>
<summary>Abstract</summary>

Recently, instruction-following audio-language models have received broad attention for human-audio interaction. However, the absence of benchmarks capable of evaluating audio-centric interaction capabilities has impeded advancements in this field. Previous models primarily focus on assessing different fundamental tasks, such as Automatic Speech Recognition (ASR), and lack an assessment of the open-ended generative capabilities centered around audio. Thus, it is challenging to track the progression in the Large Audio-Language Models (LALMs) domain and to provide guidance for future improvement. In this paper, we introduce AIR-Bench (\textbf{A}udio \textbf{I}nst\textbf{R}uction \textbf{Bench}mark), the first benchmark designed to evaluate the ability of LALMs to understand various types of audio signals (including human speech, natural sounds, and music), and furthermore, to interact with humans in the textual format. AIR-Bench encompasses two dimensions: \textit{foundation} and \textit{chat} benchmarks. The former consists of 19 tasks with approximately 19k single-choice questions, intending to inspect the basic single-task ability of LALMs. The latter one contains 2k instances of open-ended question-and-answer data, directly assessing the comprehension of the model on complex audio and its capacity to follow instructions. Both benchmarks require the model to generate hypotheses directly. We design a unified framework that leverages advanced language models, such as GPT-4, to evaluate the scores of generated hypotheses given the meta-information of the audio. Experimental results demonstrate a high level of consistency between GPT-4-based evaluation and human evaluation. By revealing the limitations of existing LALMs through evaluation results, AIR-Bench can provide insights into the direction of future research.

</details>

### [DeepCover: Advancing RNN Test Coverage and Online Error Prediction using State Machine Extraction](2402.06966.md)
**Pouria Golshanrad, Fathiyeh Faghih** · 2024-02-10

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) have emerged as powerful tools for processing sequential data in various fields, including natural language processing and speech recognition. However, the lack of explainability in RNN models has limited their interpretability, posing challenges in understanding their internal workings. To address this issue, this paper proposes a methodology for extracting a state machine (SM) from an RNN-based model to provide insights into its internal function. The proposed SM extraction algorithm was assessed using four newly proposed metrics: Purity, Richness, Goodness, and Scale. The proposed methodology along with its assessment metrics contribute to increasing explainability in RNN models by providing a clear representation of their internal decision making process through the extracted SM. In addition to improving the explainability of RNNs, the extracted SM can be used to advance testing and and monitoring of the primary RNN-based model. To enhance RNN testing, we introduce six model coverage criteria based on the extracted SM, serving as metrics for evaluating the effectiveness of test suites designed to analyze the primary model. We also propose a tree-based model to predict the error probability of the primary model for each input based on the extracted SM. We evaluated our proposed online error prediction approach using the MNIST dataset and Mini Speech Commands dataset, achieving an area under the curve (AUC) exceeding 80\% for the receiver operating characteristic (ROC) chart.

</details>

### [Self-consistent context aware conformer transducer for speech recognition](2402.06592.md)
**Konstantin Kolokolov, Pavel Pekichev, Karthik Raghunathan** · 2024-02-09

<details>
<summary>Abstract</summary>

We introduce a novel neural network module that adeptly handles recursive data flow in neural network architectures. At its core, this module employs a self-consistent approach where a set of recursive equations is solved iteratively, halting when the difference between two consecutive iterations falls below a defined threshold. Leveraging this mechanism, we construct a new neural network architecture, an extension of the conformer transducer, which enriches automatic speech recognition systems with a stream of contextual information. Our method notably improves the accuracy of recognizing rare words without adversely affecting the word error rate for common vocabulary. We investigate the improvement in accuracy for these uncommon words using our novel model, both independently and in conjunction with shallow fusion with a context language model. Our findings reveal that the combination of both approaches can improve the accuracy of detecting rare words by as much as 4.5 times. Our proposed self-consistent recursive methodology is versatile and adaptable, compatible with many recently developed encoders, and has the potential to drive model improvements in speech recognition and beyond.

</details>

### [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](2402.05457.md)
**Chen Chen, Ruizhe Li, Yuchen Hu, Sabato Marco Siniscalchi et al.** · 2024-02-08

<details>
<summary>Abstract</summary>

Recent studies have successfully shown that large language models (LLMs) can be successfully used for generative error correction (GER) on top of the automatic speech recognition (ASR) output. Specifically, an LLM is utilized to carry out a direct mapping from the N-best hypotheses list generated by an ASR system to the predicted output transcription. However, despite its effectiveness, GER introduces extra data uncertainty since the LLM is trained without taking into account acoustic information available in the speech signal. In this work, we aim to overcome such a limitation by infusing acoustic information before generating the predicted transcription through a novel late fusion solution termed Uncertainty-Aware Dynamic Fusion (UADF). UADF is a multimodal fusion approach implemented into an auto-regressive decoding process and works in two stages: (i) It first analyzes and calibrates the token-level LLM decision, and (ii) it then dynamically assimilates the information from the acoustic modality. Experimental evidence collected from various ASR tasks shows that UADF surpasses existing fusion mechanisms in several ways. It yields significant improvements in word error rate (WER) while mitigating data uncertainty issues in LLM and addressing the poor generalization relied with sole modality during fusion. We also demonstrate that UADF seamlessly adapts to audio-visual speech recognition.

</details>

### [Spirit LM: Interleaved Spoken and Written Language Model](2402.05755.md)
**Tu Anh Nguyen, Benjamin Muller, Bokai Yu, Marta R. Costa-jussa et al.** · 2024-02-08

<details>
<summary>Abstract</summary>

We introduce Spirit LM, a foundation multimodal language model that freely mixes text and speech. Our model is based on a 7B pretrained text language model that we extend to the speech modality by continuously training it on text and speech units. Speech and text sequences are concatenated as a single stream of tokens, and trained with a word-level interleaving method using a small automatically-curated speech-text parallel corpus. Spirit LM comes in two versions: a Base version that uses speech phonetic units (HuBERT) and an Expressive version that models expressivity using pitch and style units in addition to the phonetic units. For both versions, the text is encoded with subword BPE tokens. The resulting model displays both the semantic abilities of text models and the expressive abilities of speech models. Additionally, we demonstrate that Spirit LM can learn new tasks in a few-shot fashion across modalities (i.e. ASR, TTS, Speech Classification). We make available model weights and inference code.

</details>

### [Named Entity Recognition for Address Extraction in Speech-to-Text Transcriptions Using Synthetic Data](2402.05545.md)
**Bibiána Lajčinová, Patrik Valábek, Michal Spišiak** · 2024-02-08

<details>
<summary>Abstract</summary>

This paper introduces an approach for building a Named Entity Recognition (NER) model built upon a Bidirectional Encoder Representations from Transformers (BERT) architecture, specifically utilizing the SlovakBERT model. This NER model extracts address parts from data acquired from speech-to-text transcriptions. Due to scarcity of real data, a synthetic dataset using GPT API was generated. The importance of mimicking spoken language variability in this artificial data is emphasized. The performance of our NER model, trained solely on synthetic data, is evaluated using small real test dataset.

</details>

### [Resolving Transcription Ambiguity in Spanish: A Hybrid Acoustic-Lexical System for Punctuation Restoration](2402.03519.md)
**Xiliang Zhu, Chia-Tien Chang, Shayna Gardiner, David Rossouw et al.** · 2024-02-05

<details>
<summary>Abstract</summary>

Punctuation restoration is a crucial step after Automatic Speech Recognition (ASR) systems to enhance transcript readability and facilitate subsequent NLP tasks. Nevertheless, conventional lexical-based approaches are inadequate for solving the punctuation restoration task in Spanish, where ambiguity can be often found between unpunctuated declaratives and questions. In this study, we propose a novel hybrid acoustic-lexical punctuation restoration system for Spanish transcription, which consolidates acoustic and lexical signals through a modular process. Our experiment results show that the proposed system can effectively improve F1 score of question marks and overall punctuation restoration on both public and internal Spanish conversational datasets. Additionally, benchmark comparison against LLMs (Large Language Model) indicates the superiority of our approach in accuracy, reliability and latency. Furthermore, we demonstrate that the Word Error Rate (WER) of the ASR module also benefits from our proposed system.

</details>

### [A Comprehensive Study of the Current State-of-the-Art in Nepali Automatic Speech Recognition Systems](2402.03050.md)
**Rupak Raj Ghimire, Bal Krishna Bal, Prakash Poudyal** · 2024-02-05

<details>
<summary>Abstract</summary>

In this paper, we examine the research conducted in the field of Nepali Automatic Speech Recognition (ASR). The primary objective of this survey is to conduct a comprehensive review of the works on Nepali Automatic Speech Recognition Systems completed to date, explore the different datasets used, examine the technology utilized, and take account of the obstacles encountered in implementing the Nepali ASR system. In tandem with the global trends of ever-increasing research on speech recognition based research, the number of Nepalese ASR-related projects are also growing. Nevertheless, the investigation of language and acoustic models of the Nepali language has not received adequate attention compared to languages that possess ample resources. In this context, we provide a framework as well as directions for future investigations.

</details>

### [A Light-Weight Autoregressive CNN-Based Frame Level Transducer Decoder for End-to-End ASR](s2:e49d260bd3956f0b5e3d4d8de813790b59f706be.md)
**Hyeon-Kyu Noh, Hong-June Park** · 2024-02-04

<details>
<summary>Abstract</summary>

A convolutional neural network (CNN) transducer decoder was proposed to reduce the decoding time of an end-to-end automatic speech recognition (ASR) system while maintaining accuracy. The CNN of 177 k parameters and a kernel size of 6 generates the probabilities of the current token at the token level, at the token transition of the output token sequence. Two probabilities of the current token, one from the encoder and the other from the CNN are added to the frame level to reduce the decoding step to the number of input frames. An encoder composed of an 18-layer conformer was combined with the proposed decoder for training with the Librispeech data set. The forward-backward algorithm was used for training. The space and re-appearance tokens are added to the 300-word piece tokens to represent the token string. A space token appears at a frame between two words. A comparison with the autoregressive decoders such as transformer and RNN-T decoders demonstrates that this work provides comparable WERs with much less decoding time. A comparison with non-autoregressive decoders such as CTC indicates that this work enhanced WERs.

</details>

### [Streaming Sequence Transduction through Dynamic Compression](2402.01172.md)
**Weiting Tan, Yunmo Chen, Tongfei Chen, Guanghui Qin et al.** · 2024-02-02

<details>
<summary>Abstract</summary>

We introduce STAR (Stream Transduction with Anchor Representations), a novel Transformer-based model designed for efficient sequence-to-sequence transduction over streams. STAR dynamically segments input streams to create compressed anchor representations, achieving nearly lossless compression (12x) in Automatic Speech Recognition (ASR) and outperforming existing methods. Moreover, STAR demonstrates superior segmentation and latency-quality trade-offs in simultaneous speech-to-text tasks, optimizing latency, memory footprint, and quality.

</details>

### [A Case Study on Filtering for End-to-End Speech Translation](2402.01945.md)
**Md Mahfuz Ibn Alam, Antonios Anastasopoulos** · 2024-02-02

<details>
<summary>Abstract</summary>

It is relatively easy to mine a large parallel corpus for any machine learning task, such as speech-to-text or speech-to-speech translation. Although these mined corpora are large in volume, their quality is questionable. This work shows that the simplest filtering technique can trim down these big, noisy datasets to a more manageable, clean dataset. We also show that using this clean dataset can improve the model's performance, as in the case of the multilingual-to-English Speech Translation (ST) model, where, on average, we obtain a 4.65 BLEU score improvement.

</details>

### [Retrieval Augmented End-to-End Spoken Dialog Models](2402.01828.md)
**Mingqiu Wang, Izhak Shafran, Hagen Soltau, Wei Han et al.** · 2024-02-02

<details>
<summary>Abstract</summary>

We recently developed SLM, a joint speech and language model, which fuses a pretrained foundational speech model and a large language model (LLM), while preserving the in-context learning capability intrinsic to the pretrained LLM. In this paper, we apply SLM to speech dialog applications where the dialog states are inferred directly from the audio signal. Task-oriented dialogs often contain domain-specific entities, i.e., restaurants, hotels, train stations, and city names, which are difficult to recognize, however, critical for the downstream applications. Inspired by the RAG (retrieval-augmented generation) paradigm, we propose a retrieval augmented SLM (ReSLM) that overcomes this weakness. We first train a speech retriever to retrieve text entities mentioned in the audio. The retrieved entities are then added as text inputs to the underlying SLM to bias model predictions. We evaluated ReSLM on speech MultiWoz task (DSTC-11 challenge), and found that this retrieval augmentation boosts model performance, achieving joint goal accuracy (38.6% vs 32.7%), slot error rate (20.6% vs 24.8%) and ASR word error rate (5.5% vs 6.7%). While demonstrated on dialog state tracking, our approach is broadly applicable to other speech tasks requiring contextual information or domain-specific entities, such as contextual ASR with biasing capability.

</details>

### [Introduction to speech recognition](2402.01778.md)
**Gabriel Dauphin** · 2024-02-01

<details>
<summary>Abstract</summary>

This document contains lectures and practical experimentations using Matlab and implementing a system which is actually correctly classifying three words (one, two and three) with the help of a very small database. To achieve this performance, it uses speech modeling specificities, powerful computer algorithms (dynamic time warping and Dijktra's algorithm) and machine learning (nearest neighbor). This document introduces also some machine learning evaluation metrics.

</details>

### [Exploring the limits of decoder-only models trained on public speech recognition corpora](2402.00235.md)
**Ankit Gupta, George Saon, Brian Kingsbury** · 2024-01-31

<details>
<summary>Abstract</summary>

The emergence of industrial-scale speech recognition (ASR) models such as Whisper and USM, trained on 1M hours of weakly labelled and 12M hours of audio only proprietary data respectively, has led to a stronger need for large scale public ASR corpora and competitive open source pipelines. Unlike the said models, large language models are typically based on Transformer decoders, and it remains unclear if decoder-only models trained on public data alone can deliver competitive performance. In this work, we investigate factors such as choice of training datasets and modeling components necessary for obtaining the best performance using public English ASR corpora alone. Our Decoder-Only Transformer for ASR (DOTA) model comprehensively outperforms the encoder-decoder open source replication of Whisper (OWSM) on nearly all English ASR benchmarks and outperforms Whisper large-v3 on 7 out of 15 test sets. We release our codebase and model checkpoints under permissive license.

</details>

### [Computation and Parameter Efficient Multi-Modal Fusion Transformer for Cued Speech Recognition](2401.17604.md)
**Lei Liu, Li Liu, Haizhou Li** · 2024-01-31

<details>
<summary>Abstract</summary>

Cued Speech (CS) is a pure visual coding method used by hearing-impaired people that combines lip reading with several specific hand shapes to make the spoken language visible. Automatic CS recognition (ACSR) seeks to transcribe visual cues of speech into text, which can help hearing-impaired people to communicate effectively. The visual information of CS contains lip reading and hand cueing, thus the fusion of them plays an important role in ACSR. However, most previous fusion methods struggle to capture the global dependency present in long sequence inputs of multi-modal CS data. As a result, these methods generally fail to learn the effective cross-modal relationships that contribute to the fusion. Recently, attention-based transformers have been a prevalent idea for capturing the global dependency over the long sequence in multi-modal fusion, but existing multi-modal fusion transformers suffer from both poor recognition accuracy and inefficient computation for the ACSR task. To address these problems, we develop a novel computation and parameter efficient multi-modal fusion transformer by proposing a novel Token-Importance-Aware Attention mechanism (TIAA), where a token utilization rate (TUR) is formulated to select the important tokens from the multi-modal streams. More precisely, TIAA firstly models the modality-specific fine-grained temporal dependencies over all tokens of each modality, and then learns the efficient cross-modal interaction for the modality-shared coarse-grained temporal dependencies over the important tokens of different modalities. Besides, a light-weight gated hidden projection is designed to control the feature flows of TIAA. The resulting model, named Economical Cued Speech Fusion Transformer (EcoCued), achieves state-of-the-art performance on all existing CS datasets, compared with existing transformer-based fusion methods and ACSR fusion methods.

</details>

### [Exploiting Audio-Visual Features with Pretrained AV-HuBERT for Multi-Modal Dysarthric Speech Reconstruction](2401.17796.md)
**Xueyuan Chen, Yuejiao Wang, Xixin Wu, Disong Wang et al.** · 2024-01-31

<details>
<summary>Abstract</summary>

Dysarthric speech reconstruction (DSR) aims to transform dysarthric speech into normal speech by improving the intelligibility and naturalness. This is a challenging task especially for patients with severe dysarthria and speaking in complex, noisy acoustic environments. To address these challenges, we propose a novel multi-modal framework to utilize visual information, e.g., lip movements, in DSR as extra clues for reconstructing the highly abnormal pronunciations. The multi-modal framework consists of: (i) a multi-modal encoder to extract robust phoneme embeddings from dysarthric speech with auxiliary visual features; (ii) a variance adaptor to infer the normal phoneme duration and pitch contour from the extracted phoneme embeddings; (iii) a speaker encoder to encode the speaker's voice characteristics; and (iv) a mel-decoder to generate the reconstructed mel-spectrogram based on the extracted phoneme embeddings, prosodic features and speaker embeddings. Both objective and subjective evaluations conducted on the commonly used UASpeech corpus show that our proposed approach can achieve significant improvements over baseline systems in terms of speech intelligibility and naturalness, especially for the speakers with more severe symptoms. Compared with original dysarthric speech, the reconstructed speech achieves 42.1\% absolute word error rate reduction for patients with more severe dysarthria levels.

</details>

### [OWSM v3.1: Better and Faster Open Whisper-Style Speech Models based on E-Branchformer](2401.16658.md)
**Yifan Peng, Jinchuan Tian, William Chen, Siddhant Arora et al.** · 2024-01-30

<details>
<summary>Abstract</summary>

Recent studies have highlighted the importance of fully open foundation models. The Open Whisper-style Speech Model (OWSM) is an initial step towards reproducing OpenAI Whisper using public data and open-source toolkits. However, previous versions of OWSM (v1 to v3) are still based on standard Transformer, which might lead to inferior performance compared to state-of-the-art speech encoder architectures. This work aims to improve the performance and efficiency of OWSM without additional data. We present a series of E-Branchformer-based models named OWSM v3.1, ranging from 100M to 1B parameters. OWSM v3.1 outperforms its predecessor, OWSM v3, in most evaluation benchmarks, while showing an improved inference speed of up to 25%. We further reveal the emergent ability of OWSM v3.1 in zero-shot contextual biasing speech recognition. We also provide a model trained on a subset of data with low license restrictions. We will publicly release the code, pre-trained models, and training logs.

</details>

### [Towards Event Extraction from Speech with Contextual Clues](2401.15385.md)
**Jingqi Kang, Tongtong Wu, Jinming Zhao, Guitao Wang et al.** · 2024-01-27

<details>
<summary>Abstract</summary>

While text-based event extraction has been an active research area and has seen successful application in many domains, extracting semantic events from speech directly is an under-explored problem. In this paper, we introduce the Speech Event Extraction (SpeechEE) task and construct three synthetic training sets and one human-spoken test set. Compared to event extraction from text, SpeechEE poses greater challenges mainly due to complex speech signals that are continuous and have no word boundaries. Additionally, unlike perceptible sound events, semantic events are more subtle and require a deeper understanding. To tackle these challenges, we introduce a sequence-to-structure generation paradigm that can produce events from speech signals in an end-to-end manner, together with a conditioned generation method that utilizes speech recognition transcripts as the contextual clue. We further propose to represent events with a flat format to make outputs more natural language-like. Our experimental results show that our method brings significant improvements on all datasets, achieving a maximum F1 gain of 10.7%. The code and datasets are released on https://github.com/jodie-kang/SpeechEE.

</details>

### [UNIT-DSR: Dysarthric Speech Reconstruction System Using Speech Unit Normalization](2401.14664.md)
**Yuejiao Wang, Xixin Wu, Disong Wang, Lingwei Meng et al.** · 2024-01-26

<details>
<summary>Abstract</summary>

Dysarthric speech reconstruction (DSR) systems aim to automatically convert dysarthric speech into normal-sounding speech. The technology eases communication with speakers affected by the neuromotor disorder and enhances their social inclusion. NED-based (Neural Encoder-Decoder) systems have significantly improved the intelligibility of the reconstructed speech as compared with GAN-based (Generative Adversarial Network) approaches, but the approach is still limited by training inefficiency caused by the cascaded pipeline and auxiliary tasks of the content encoder, which may in turn affect the quality of reconstruction. Inspired by self-supervised speech representation learning and discrete speech units, we propose a Unit-DSR system, which harnesses the powerful domain-adaptation capacity of HuBERT for training efficiency improvement and utilizes speech units to constrain the dysarthric content restoration in a discrete linguistic space. Compared with NED approaches, the Unit-DSR system only consists of a speech unit normalizer and a Unit HiFi-GAN vocoder, which is considerably simpler without cascaded sub-modules or auxiliary tasks. Results on the UASpeech corpus indicate that Unit-DSR outperforms competitive baselines in terms of content restoration, reaching a 28.2% relative average word error rate reduction when compared to original dysarthric speech, and shows robustness against speed perturbation and noise.

</details>

### [VALL-T: Decoder-Only Generative Transducer for Robust and Decoding-Controllable Text-to-Speech](2401.14321.md)
**Chenpeng Du, Yiwei Guo, Hankun Wang, Yifan Yang et al.** · 2024-01-25

<details>
<summary>Abstract</summary>

Recent TTS models with decoder-only Transformer architecture, such as SPEAR-TTS and VALL-E, achieve impressive naturalness and demonstrate the ability for zero-shot adaptation given a speech prompt. However, such decoder-only TTS models lack monotonic alignment constraints, sometimes leading to hallucination issues such as mispronunciation, word skipping and repeating. To address this limitation, we propose VALL-T, a generative Transducer model that introduces shifting relative position embeddings for input phoneme sequence, explicitly indicating the monotonic generation process while maintaining the architecture of decoder-only Transformer. Consequently, VALL-T retains the capability of prompt-based zero-shot adaptation and demonstrates better robustness against hallucinations with a relative reduction of 28.3% in the word error rate.

</details>

### [CNN architecture extraction on edge GPU](2401.13575.md)
**Peter Horvath, Lukasz Chmielewski, Leo Weissbart, Lejla Batina et al.** · 2024-01-24

<details>
<summary>Abstract</summary>

Neural networks have become popular due to their versatility and state-of-the-art results in many applications, such as image classification, natural language processing, speech recognition, forecasting, etc. These applications are also used in resource-constrained environments such as embedded devices. In this work, the susceptibility of neural network implementations to reverse engineering is explored on the NVIDIA Jetson Nano microcomputer via side-channel analysis. To this end, an architecture extraction attack is presented. In the attack, 15 popular convolutional neural network architectures (EfficientNets, MobileNets, NasNet, etc.) are implemented on the GPU of Jetson Nano and the electromagnetic radiation of the GPU is analyzed during the inference operation of the neural networks. The results of the analysis show that neural network architectures are easily distinguishable using deep learning-based side-channel analysis.

</details>

### [SpeechDPR: End-to-End Spoken Passage Retrieval for Open-Domain Spoken Question Answering](2401.13463.md)
**Chyi-Jiunn Lin, Guan-Ting Lin, Yung-Sung Chuang, Wei-Lun Wu et al.** · 2024-01-24

<details>
<summary>Abstract</summary>

Spoken Question Answering (SQA) is essential for machines to reply to user's question by finding the answer span within a given spoken passage. SQA has been previously achieved without ASR to avoid recognition errors and Out-of-Vocabulary (OOV) problems. However, the real-world problem of Open-domain SQA (openSQA), in which the machine needs to first retrieve passages that possibly contain the answer from a spoken archive in addition, was never considered. This paper proposes the first known end-to-end framework, Speech Dense Passage Retriever (SpeechDPR), for the retrieval component of the openSQA problem. SpeechDPR learns a sentence-level semantic representation by distilling knowledge from the cascading model of unsupervised ASR (UASR) and text dense retriever (TDR). No manually transcribed speech data is needed. Initial experiments showed performance comparable to the cascading model of UASR and TDR, and significantly better when UASR was poor, verifying this approach is more robust to speech recognition errors.

</details>

### [Locality enhanced dynamic biasing and sampling strategies for contextual ASR](2401.13146.md)
**Md Asif Jalal, Pablo Peso Parada, George Pavlidis, Vasileios Moschopoulos et al.** · 2024-01-23

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) still face challenges when recognizing time-variant rare-phrases. Contextual biasing (CB) modules bias ASR model towards such contextually-relevant phrases. During training, a list of biasing phrases are selected from a large pool of phrases following a sampling strategy. In this work we firstly analyse different sampling strategies to provide insights into the training of CB for ASR with correlation plots between the bias embeddings among various training stages. Secondly, we introduce a neighbourhood attention (NA) that localizes self attention (SA) to the nearest neighbouring frames to further refine the CB output. The results show that this proposed approach provides on average a 25.84% relative WER improvement on LibriSpeech sets and rare-word evaluation compared to the baseline.

</details>

### [Multilingual and Fully Non-Autoregressive ASR with Large Language Model Fusion: A Comprehensive Study](2401.12789.md)
**W. Ronny Huang, Cyril Allauzen, Tongzhou Chen, Kilol Gupta et al.** · 2024-01-23

<details>
<summary>Abstract</summary>

In the era of large models, the autoregressive nature of decoding often results in latency serving as a significant bottleneck. We propose a non-autoregressive LM-fused ASR system that effectively leverages the parallelization capabilities of accelerator hardware. Our approach combines the Universal Speech Model (USM) and the PaLM 2 language model in per-segment scoring mode, achieving an average relative WER improvement across all languages of 10.8% on FLEURS and 3.6% on YouTube captioning. Furthermore, our comprehensive ablation study analyzes key parameters such as LLM size, context length, vocabulary size, fusion methodology. For instance, we explore the impact of LLM size ranging from 128M to 340B parameters on ASR performance. This study provides valuable insights into the factors influencing the effectiveness of practical large-scale LM-fused speech recognition systems.

</details>

### [Keep Decoding Parallel with Effective Knowledge Distillation from Language Models to End-to-end Speech Recognisers](2401.11700.md)
**Michael Hentschel, Yuta Nishikawa, Tatsuya Komatsu, Yusuke Fujita** · 2024-01-22

<details>
<summary>Abstract</summary>

This study presents a novel approach for knowledge distillation (KD) from a BERT teacher model to an automatic speech recognition (ASR) model using intermediate layers. To distil the teacher's knowledge, we use an attention decoder that learns from BERT's token probabilities. Our method shows that language model (LM) information can be more effectively distilled into an ASR model using both the intermediate layers and the final layer. By using the intermediate layers as distillation target, we can more effectively distil LM knowledge into the lower network layers. Using our method, we achieve better recognition accuracy than with shallow fusion of an external LM, allowing us to maintain fast parallel decoding. Experiments on the LibriSpeech dataset demonstrate the effectiveness of our approach in enhancing greedy decoding with connectionist temporal classification (CTC).

</details>

### [Benchmarking Large Multimodal Models against Common Corruptions](2401.11943.md)
**Jiawei Zhang, Tianyu Pang, Chao Du, Yi Ren et al.** · 2024-01-22

<details>
<summary>Abstract</summary>

This technical report aims to fill a deficiency in the assessment of large multimodal models (LMMs) by specifically examining the self-consistency of their outputs when subjected to common corruptions. We investigate the cross-modal interactions between text, image, and speech, encompassing four essential generation tasks: text-to-image, image-to-text, text-to-speech, and speech-to-text. We create a comprehensive benchmark, named MMCBench, that covers more than 100 popular LMMs (totally over 150 model checkpoints). A thorough evaluation under common corruptions is critical for practical deployment and facilitates a better understanding of the reliability of cutting-edge LMMs. The benchmarking code is available at https://github.com/sail-sg/MMCBench

</details>

### [Streaming Bilingual End-to-End ASR model using Attention over Multiple Softmax](2401.11645.md)
**Aditya Patil, Vikas Joshi, Purvi Agrawal, Rupesh Mehta** · 2024-01-22

<details>
<summary>Abstract</summary>

Even with several advancements in multilingual modeling, it is challenging to recognize multiple languages using a single neural model, without knowing the input language and most multilingual models assume the availability of the input language. In this work, we propose a novel bilingual end-to-end (E2E) modeling approach, where a single neural model can recognize both languages and also support switching between the languages, without any language input from the user. The proposed model has shared encoder and prediction networks, with language-specific joint networks that are combined via a self-attention mechanism. As the language-specific posteriors are combined, it produces a single posterior probability over all the output symbols, enabling a single beam search decoding and also allowing dynamic switching between the languages. The proposed approach outperforms the conventional bilingual baseline with 13.3%, 8.23% and 1.3% word error rate relative reduction on Hindi, English and code-mixed test sets, respectively.

</details>

### [Using Large Language Model for End-to-End Chinese ASR and NER](2401.11382.md)
**Yuang Li, Jiawei Yu, Min Zhang, Mengxin Ren et al.** · 2024-01-21

<details>
<summary>Abstract</summary>

Mapping speech tokens to the same feature space as text tokens has become the paradigm for the integration of speech modality into decoder-only large language models (LLMs). An alternative approach is to use an encoder-decoder architecture that incorporates speech features through cross-attention. This approach, however, has received less attention in the literature. In this work, we connect the Whisper encoder with ChatGLM3 and provide in-depth comparisons of these two approaches using Chinese automatic speech recognition (ASR) and name entity recognition (NER) tasks. We evaluate them not only by conventional metrics like the F1 score but also by a novel fine-grained taxonomy of ASR-NER errors. Our experiments reveal that encoder-decoder architecture outperforms decoder-only architecture with a short context, while decoder-only architecture benefits from a long context as it fully exploits all layers of the LLM. By using LLM, we significantly reduced the entity omission errors and improved the entity ASR accuracy compared to the Conformer baseline. Additionally, we obtained a state-of-the-art (SOTA) F1 score of 0.805 on the AISHELL-NER test set by using chain-of-thought (CoT) NER which first infers long-form ASR transcriptions and then predicts NER labels.

</details>

### [Word-Level ASR Quality Estimation for Efficient Corpus Sampling and Post-Editing through Analyzing Attentions of a Reference-Free Metric](2401.11268.md)
**Golara Javadi, Kamer Ali Yuksel, Yunsu Kim, Thiago Castro Ferreira et al.** · 2024-01-20

<details>
<summary>Abstract</summary>

In the realm of automatic speech recognition (ASR), the quest for models that not only perform with high accuracy but also offer transparency in their decision-making processes is crucial. The potential of quality estimation (QE) metrics is introduced and evaluated as a novel tool to enhance explainable artificial intelligence (XAI) in ASR systems. Through experiments and analyses, the capabilities of the NoRefER (No Reference Error Rate) metric are explored in identifying word-level errors to aid post-editors in refining ASR hypotheses. The investigation also extends to the utility of NoRefER in the corpus-building process, demonstrating its effectiveness in augmenting datasets with insightful annotations. The diagnostic aspects of NoRefER are examined, revealing its ability to provide valuable insights into model behaviors and decision patterns. This has proven beneficial for prioritizing hypotheses in post-editing workflows and fine-tuning ASR models. The findings suggest that NoRefER is not merely a tool for error detection but also a comprehensive framework for enhancing ASR systems' transparency, efficiency, and effectiveness. To ensure the reproducibility of the results, all source codes of this study are made publicly available.

</details>

### [Contextualized Automatic Speech Recognition with Attention-Based Bias Phrase Boosted Beam Search](2401.10449.md)
**Yui Sudo, Muhammad Shakeel, Yosuke Fukumoto, Yifan Peng et al.** · 2024-01-19

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) methods exhibit remarkable performance. However, since the performance of such methods is intrinsically linked to the context present in the training data, E2E-ASR methods do not perform as desired for unseen user contexts (e.g., technical terms, personal names, and playlists). Thus, E2E-ASR methods must be easily contextualized by the user or developer. This paper proposes an attention-based contextual biasing method that can be customized using an editable phrase list (referred to as a bias list). The proposed method can be trained effectively by combining a bias phrase index loss and special tokens to detect the bias phrases in the input speech data. In addition, to improve the contextualization performance during inference further, we propose a bias phrase boosted (BPB) beam search algorithm based on the bias phrase index probability. Experimental results demonstrate that the proposed method consistently improves the word error rate and the character error rate of the target phrases in the bias list on both the Librispeech-960 (English) and our in-house (Japanese) dataset, respectively.

</details>

### [Large Language Models are Efficient Learners of Noise-Robust Speech Recognition](2401.10446.md)
**Yuchen Hu, Chen Chen, Chao-Han Huck Yang, Ruizhe Li et al.** · 2024-01-19

<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have promoted generative error correction (GER) for automatic speech recognition (ASR), which leverages the rich linguistic knowledge and powerful reasoning ability of LLMs to improve recognition results. The latest work proposes a GER benchmark with HyPoradise dataset to learn the mapping from ASR N-best hypotheses to ground-truth transcription by efficient LLM finetuning, which shows great effectiveness but lacks specificity on noise-robust ASR. In this work, we extend the benchmark to noisy conditions and investigate if we can teach LLMs to perform denoising for GER just like what robust ASR do}, where one solution is introducing noise information as a conditioner into LLM. However, directly incorporating noise embeddings from audio encoder could harm the LLM tuning due to cross-modality gap. To this end, we propose to extract a language-space noise embedding from the N-best list to represent the noise conditions of source speech, which can promote the denoising process in GER. Furthermore, in order to enhance its representation ability of audio noise, we design a knowledge distillation (KD) approach via mutual information estimation to distill the real noise information in audio embeddings to our language embedding. Experiments on various latest LLMs demonstrate our approach achieves a new breakthrough with up to 53.9% correction improvement in terms of word error rate while with limited training data. Analysis shows that our language-space noise embedding can well represent the noise conditions of source speech, under which off-the-shelf LLMs show strong ability of language-space denoising.

</details>

### [Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks](2401.10070.md)
**Yichao Du, Zhirui Zhang, Linan Yue, Xu Huang et al.** · 2024-01-18

<details>
<summary>Abstract</summary>

To protect privacy and meet legal regulations, federated learning (FL) has gained significant attention for training speech-to-text (S2T) systems, including automatic speech recognition (ASR) and speech translation (ST). However, the commonly used FL approach (i.e., \textsc{FedAvg}) in S2T tasks typically suffers from extensive communication overhead due to multi-round interactions based on the whole model and performance degradation caused by data heterogeneity among clients.To address these issues, we propose a personalized federated S2T framework that introduces \textsc{FedLoRA}, a lightweight LoRA module for client-side tuning and interaction with the server to minimize communication overhead, and \textsc{FedMem}, a global model equipped with a $k$-nearest-neighbor ($k$NN) classifier that captures client-specific distributional shifts to achieve personalization and overcome data heterogeneity. Extensive experiments based on Conformer and Whisper backbone models on CoVoST and GigaSpeech benchmarks show that our approach significantly reduces the communication overhead on all S2T tasks and effectively personalizes the global model to overcome data heterogeneity.

</details>

### [Efficient Training for Multilingual Visual Speech Recognition: Pre-training with Discretized Visual Speech Representation](2401.09802.md)
**Minsu Kim, Jeong Hun Yeo, Se Jin Park, Hyeongseop Rha et al.** · 2024-01-18

<details>
<summary>Abstract</summary>

This paper explores sentence-level multilingual Visual Speech Recognition (VSR) that can recognize different languages with a single trained model. As the massive multilingual modeling of visual data requires huge computational costs, we propose a novel training strategy, processing with visual speech units. Motivated by the recent success of the audio speech unit, we propose to use a visual speech unit that can be obtained by discretizing the visual speech features extracted from the self-supervised visual speech model. Through analysis, we verify that the visual speech units mainly contain viseme information while suppressing non-linguistic information. By using the visual speech units as the inputs of our system, we propose to pre-train a VSR model to predict corresponding text outputs on multilingual data constructed by merging several VSR databases. As both the inputs (i.e., visual speech units) and outputs (i.e., text) are discrete, we can greatly improve the training efficiency compared to the standard VSR training. Specifically, the input data size is reduced to 0.016% of the original video inputs. In order to complement the insufficient visual information in speech recognition, we apply curriculum learning where the inputs of the system begin with audio-visual speech units and gradually change to visual speech units. After pre-training, the model is finetuned on continuous features. We set new state-of-the-art multilingual VSR performances by achieving comparable performances to the previous language-specific VSR models, with a single trained model.

</details>

### [SlideAVSR: A Dataset of Paper Explanation Videos for Audio-Visual Speech Recognition](2401.09759.md)
**Hao Wang, Shuhei Kurita, Shuichiro Shimizu, Daisuke Kawahara** · 2024-01-18

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) is a multimodal extension of automatic speech recognition (ASR), using video as a complement to audio. In AVSR, considerable efforts have been directed at datasets for facial features such as lip-readings, while they often fall short in evaluating the image comprehension capabilities in broader contexts. In this paper, we construct SlideAVSR, an AVSR dataset using scientific paper explanation videos. SlideAVSR provides a new benchmark where models transcribe speech utterances with texts on the slides on the presentation recordings. As technical terminologies that are frequent in paper explanations are notoriously challenging to transcribe without reference texts, our SlideAVSR dataset spotlights a new aspect of AVSR problems. As a simple yet effective baseline, we propose DocWhisper, an AVSR model that can refer to textual information from slides, and confirm its effectiveness on SlideAVSR.

</details>

### [On Speech Pre-emphasis as a Simple and Inexpensive Method to Boost Speech Enhancement](2401.09315.md)
**Iván López-Espejo, Aditya Joglekar, Antonio M. Peinado, Jesper Jensen** · 2024-01-17

<details>
<summary>Abstract</summary>

Pre-emphasis filtering, compensating for the natural energy decay of speech at higher frequencies, has been considered as a common pre-processing step in a number of speech processing tasks over the years. In this work, we demonstrate, for the first time, that pre-emphasis filtering may also be used as a simple and computationally-inexpensive way to leverage deep neural network-based speech enhancement performance. Particularly, we look into pre-emphasizing the estimated and actual clean speech prior to loss calculation so that different speech frequency components better mirror their perceptual importance during the training phase. Experimental results on a noisy version of the TIMIT dataset show that integrating the pre-emphasis-based methodology at hand yields relative estimated speech quality improvements of up to 4.6% and 3.4% for noise types seen and unseen, respectively, during the training phase. Similar to the case of pre-emphasis being considered as a default pre-processing step in classical automatic speech recognition and speech coding systems, the pre-emphasis-based methodology analyzed in this article may potentially become a default add-on for modern speech enhancement.

</details>

### [Efficient Adapter Finetuning for Tail Languages in Streaming Multilingual ASR](2401.08992.md)
**Junwen Bai, Bo Li, Qiujia Li, Tara N. Sainath et al.** · 2024-01-17

<details>
<summary>Abstract</summary>

The end-to-end ASR model is often desired in the streaming multilingual scenario since it is easier to deploy and can benefit from pre-trained speech models such as powerful foundation models. Meanwhile, the heterogeneous nature and imbalanced data abundance of different languages may cause performance degradation, leading to asynchronous peak performance for different languages during training, especially on tail ones. Sometimes even the data itself may become unavailable as a result of the enhanced privacy protection. Existing work tend to significantly increase the model size or learn language-specific decoders to accommodate each language separately. In this study, we explore simple yet effective Language-Dependent Adapter (LDA) finetuning under a cascaded Conformer transducer framework enhanced by teacher pseudo-labeling for tail languages in the streaming multilingual ASR. The adapter only accounts for 0.4% of the full model per language. It is plugged into the frozen foundation model and is the only trainable module during the finetuning process with noisy student training. The final model merges the adapter parameters from different checkpoints for different languages. The model performance is validated on a challenging multilingual dictation dataset, which includes 39 tail languages across Latin, Greek, Arabic, etc. Our proposed method brings 12.2% word error rate reduction on average and up to 37.5% on a single locale. Furthermore, we show that our parameter-efficient LDA can match the quality of the full model finetuning, thus greatly alleviating the asynchronous peak performance issue.

</details>

### [Improving ASR Contextual Biasing with Guided Attention](2401.08835.md)
**Jiyang Tang, Kwangyoun Kim, Suwon Shon, Felix Wu et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

In this paper, we propose a Guided Attention (GA) auxiliary training loss, which improves the effectiveness and robustness of automatic speech recognition (ASR) contextual biasing without introducing additional parameters. A common challenge in previous literature is that the word error rate (WER) reduction brought by contextual biasing diminishes as the number of bias phrases increases. To address this challenge, we employ a GA loss as an additional training objective besides the Transducer loss. The proposed GA loss aims to teach the cross attention how to align bias phrases with text tokens or audio frames. Compared to studies with similar motivations, the proposed loss operates directly on the cross attention weights and is easier to implement. Through extensive experiments based on Conformer Transducer with Contextual Adapter, we demonstrate that the proposed method not only leads to a lower WER but also retains its effectiveness as the number of bias phrases increases. Specifically, the GA loss decreases the WER of rare vocabularies by up to 19.2% on LibriSpeech compared to the contextual biasing baseline, and up to 49.3% compared to a vanilla Transducer.

</details>

### [Revisiting Self-supervised Learning of Speech Representation from a Mutual Information Perspective](2401.08833.md)
**Alexander H. Liu, Sung-Lin Yeh, James Glass** · 2024-01-16

<details>
<summary>Abstract</summary>

Existing studies on self-supervised speech representation learning have focused on developing new training methods and applying pre-trained models for different applications. However, the quality of these models is often measured by the performance of different downstream tasks. How well the representations access the information of interest is less studied. In this work, we take a closer look into existing self-supervised methods of speech from an information-theoretic perspective. We aim to develop metrics using mutual information to help practical problems such as model design and selection. We use linear probes to estimate the mutual information between the target information and learned representations, showing another insight into the accessibility to the target information from speech representations. Further, we explore the potential of evaluating representations in a self-supervised fashion, where we estimate the mutual information between different parts of the data without using any labels. Finally, we show that both supervised and unsupervised measures echo the performance of the models on layer-wise linear probing and speech recognition.

</details>

### [Multi-Input Multi-Output Target-Speaker Voice Activity Detection For Unified, Flexible, and Robust Audio-Visual Speaker Diarization](2401.08052.md)
**Ming Cheng, Ming Li** · 2024-01-16

<details>
<summary>Abstract</summary>

Audio-visual learning has demonstrated promising results in many classical speech tasks (e.g., speech separation, automatic speech recognition, wake-word spotting). We believe that introducing visual modality will also benefit speaker diarization. To date, Target-Speaker Voice Activity Detection (TS-VAD) plays an important role in highly accurate speaker diarization. However, previous TS-VAD models take audio features and utilize the speaker's acoustic footprint to distinguish his or her personal speech activities, which is easily affected by overlapped speech in multi-speaker scenarios. Although visual information naturally tolerates overlapped speech, it suffers from spatial occlusion, low resolution, etc. The potential modality-missing problem blocks TS-VAD towards an audio-visual approach. This paper proposes a novel Multi-Input Multi-Output Target-Speaker Voice Activity Detection (MIMO-TSVAD) framework for speaker diarization. The proposed method can take audio-visual input and leverage the speaker's acoustic footprint or lip track to flexibly conduct audio-based, video-based, and audio-visual speaker diarization in a unified sequence-to-sequence framework. Experimental results show that the MIMO-TSVAD framework demonstrates state-of-the-art performance on the VoxConverse, DIHARD-III, and MISP 2022 datasets under corresponding evaluation metrics, obtaining the Diarization Error Rates (DERs) of 4.18%, 10.10%, and 8.15%, respectively. In addition, it can perform robustly in heavy lip-missing scenarios.

</details>

### [Machine Perceptual Quality: Evaluating the Impact of Severe Lossy Compression on Audio and Image Models](2401.07957.md)
**Dan Jacobellis, Daniel Cummings, Neeraja J. Yadwadkar** · 2024-01-15

<details>
<summary>Abstract</summary>

In the field of neural data compression, the prevailing focus has been on optimizing algorithms for either classical distortion metrics, such as PSNR or SSIM, or human perceptual quality. With increasing amounts of data consumed by machines rather than humans, a new paradigm of machine-oriented compression$\unicode{x2013}$which prioritizes the retention of features salient for machine perception over traditional human-centric criteria$\unicode{x2013}$has emerged, creating several new challenges to the development, evaluation, and deployment of systems utilizing lossy compression. In particular, it is unclear how different approaches to lossy compression will affect the performance of downstream machine perception tasks. To address this under-explored area, we evaluate various perception models$\unicode{x2013}$including image classification, image segmentation, speech recognition, and music source separation$\unicode{x2013}$under severe lossy compression. We utilize several popular codecs spanning conventional, neural, and generative compression architectures. Our results indicate three key findings: (1) using generative compression, it is feasible to leverage highly compressed data while incurring a negligible impact on machine perceptual quality; (2) machine perceptual quality correlates strongly with deep similarity metrics, indicating a crucial role of these metrics in the development of machine-oriented codecs; and (3) using lossy compressed datasets, (e.g. ImageNet) for pre-training can lead to counter-intuitive scenarios where lossy compression increases machine perceptual quality rather than degrading it. To encourage engagement on this growing area of research, our code and experiments are available at: https://github.com/danjacobellis/MPQ.

</details>

### [Cascaded Cross-Modal Transformer for Audio-Textual Classification](2401.07575.md)
**Nicolae-Catalin Ristea, Andrei Anghel, Radu Tudor Ionescu** · 2024-01-15

<details>
<summary>Abstract</summary>

Speech classification tasks often require powerful language understanding models to grasp useful features, which becomes problematic when limited training data is available. To attain superior classification performance, we propose to harness the inherent value of multimodal representations by transcribing speech using automatic speech recognition (ASR) models and translating the transcripts into different languages via pretrained translation models. We thus obtain an audio-textual (multimodal) representation for each data sample. Subsequently, we combine language-specific Bidirectional Encoder Representations from Transformers (BERT) with Wav2Vec2.0 audio features via a novel cascaded cross-modal transformer (CCMT). Our model is based on two cascaded transformer blocks. The first one combines text-specific features from distinct languages, while the second one combines acoustic features with multilingual features previously learned by the first transformer block. We employed our system in the Requests Sub-Challenge of the ACM Multimedia 2023 Computational Paralinguistics Challenge. CCMT was declared the winning solution, obtaining an unweighted average recall (UAR) of 65.41% and 85.87% for complaint and request detection, respectively. Moreover, we applied our framework on the Speech Commands v2 and HarperValleyBank dialog data sets, surpassing previous studies reporting results on these benchmarks. Our code is freely available for download at: https://github.com/ristea/ccmt.

</details>

### [Promptformer: Prompted Conformer Transducer for ASR](2401.07360.md)
**Sergio Duarte-Torres, Arunasish Sen, Aman Rana, Lukas Drude et al.** · 2024-01-14

<details>
<summary>Abstract</summary>

Context cues carry information which can improve multi-turn interactions in automatic speech recognition (ASR) systems. In this paper, we introduce a novel mechanism inspired by hyper-prompting to fuse textual context with acoustic representations in the attention mechanism. Results on a test set with multi-turn interactions show that our method achieves 5.9% relative word error rate reduction (rWERR) over a strong baseline. We show that our method does not degrade in the absence of context and leads to improvements even if the model is trained without context. We further show that leveraging a pre-trained sentence-piece model for context embedding generation can outperform an external BERT model.

</details>

### [Joint Unsupervised and Supervised Training for Automatic Speech Recognition via Bilevel Optimization](2401.06980.md)
**A F M Saif, Xiaodong Cui, Han Shen, Songtao Lu et al.** · 2024-01-13

<details>
<summary>Abstract</summary>

In this paper, we present a novel bilevel optimization-based training approach to training acoustic models for automatic speech recognition (ASR) tasks that we term {bi-level joint unsupervised and supervised training (BL-JUST)}. {BL-JUST employs a lower and upper level optimization with an unsupervised loss and a supervised loss respectively, leveraging recent advances in penalty-based bilevel optimization to solve this challenging ASR problem with affordable complexity and rigorous convergence guarantees.} To evaluate BL-JUST, extensive experiments on the LibriSpeech and TED-LIUM v2 datasets have been conducted. BL-JUST achieves superior performance over the commonly used pre-training followed by fine-tuning strategy.

</details>

### [Dynamic Behaviour of Connectionist Speech Recognition with Strong Latency Constraints](2401.06588.md)
**Giampiero Salvi** · 2024-01-12

<details>
<summary>Abstract</summary>

This paper describes the use of connectionist techniques in phonetic speech recognition with strong latency constraints. The constraints are imposed by the task of deriving the lip movements of a synthetic face in real time from the speech signal, by feeding the phonetic string into an articulatory synthesiser. Particular attention has been paid to analysing the interaction between the time evolution model learnt by the multi-layer perceptrons and the transition model imposed by the Viterbi decoder, in different latency conditions. Two experiments were conducted in which the time dependencies in the language model (LM) were controlled by a parameter. The results show a strong interaction between the three factors involved, namely the neural network topology, the length of time dependencies in the LM and the decoder latency.

</details>

### [XLS-R Deep Learning Model for Multilingual ASR on Low- Resource Languages: Indonesian, Javanese, and Sundanese](2401.06832.md)
**Panji Arisaputra, Alif Tri Handoyo, Amalia Zahra** · 2024-01-12

<details>
<summary>Abstract</summary>

This research paper focuses on the development and evaluation of Automatic Speech Recognition (ASR) technology using the XLS-R 300m model. The study aims to improve ASR performance in converting spoken language into written text, specifically for Indonesian, Javanese, and Sundanese languages. The paper discusses the testing procedures, datasets used, and methodology employed in training and evaluating the ASR systems. The results show that the XLS-R 300m model achieves competitive Word Error Rate (WER) measurements, with a slight compromise in performance for Javanese and Sundanese languages. The integration of a 5-gram KenLM language model significantly reduces WER and enhances ASR accuracy. The research contributes to the advancement of ASR technology by addressing linguistic diversity and improving performance across various languages. The findings provide insights into optimizing ASR accuracy and applicability for diverse linguistic contexts.

</details>

### [LCB-net: Long-Context Biasing for Audio-Visual Speech Recognition](2401.06390.md)
**Fan Yu, Haoxu Wang, Xian Shi, Shiliang Zhang** · 2024-01-12

<details>
<summary>Abstract</summary>

The growing prevalence of online conferences and courses presents a new challenge in improving automatic speech recognition (ASR) with enriched textual information from video slides. In contrast to rare phrase lists, the slides within videos are synchronized in real-time with the speech, enabling the extraction of long contextual bias. Therefore, we propose a novel long-context biasing network (LCB-net) for audio-visual speech recognition (AVSR) to leverage the long-context information available in videos effectively. Specifically, we adopt a bi-encoder architecture to simultaneously model audio and long-context biasing. Besides, we also propose a biasing prediction module that utilizes binary cross entropy (BCE) loss to explicitly determine biased phrases in the long-context biasing. Furthermore, we introduce a dynamic contextual phrases simulation to enhance the generalization and robustness of our LCB-net. Experiments on the SlideSpeech, a large-scale audio-visual corpus enriched with slides, reveal that our proposed LCB-net outperforms general ASR model by 9.4%/9.1%/10.9% relative WER/U-WER/B-WER reduction on test set, which enjoys high unbiased and biased performance. Moreover, we also evaluate our model on LibriSpeech corpus, leading to 23.8%/19.2%/35.4% relative WER/U-WER/B-WER reduction over the ASR model.

</details>

### [UCorrect: An Unsupervised Framework for Automatic Speech Recognition Error Correction](2401.05689.md)
**Jiaxin Guo, Minghan Wang, Xiaosong Qiao, Daimeng Wei et al.** · 2024-01-11

<details>
<summary>Abstract</summary>

Error correction techniques have been used to refine the output sentences from automatic speech recognition (ASR) models and achieve a lower word error rate (WER). Previous works usually adopt end-to-end models and has strong dependency on Pseudo Paired Data and Original Paired Data. But when only pre-training on Pseudo Paired Data, previous models have negative effect on correction. While fine-tuning on Original Paired Data, the source side data must be transcribed by a well-trained ASR model, which takes a lot of time and not universal. In this paper, we propose UCorrect, an unsupervised Detector-Generator-Selector framework for ASR Error Correction. UCorrect has no dependency on the training data mentioned before. The whole procedure is first to detect whether the character is erroneous, then to generate some candidate characters and finally to select the most confident one to replace the error character. Experiments on the public AISHELL-1 dataset and WenetSpeech dataset show the effectiveness of UCorrect for ASR error correction: 1) it achieves significant WER reduction, achieves 6.83\% even without fine-tuning and 14.29\% after fine-tuning; 2) it outperforms the popular NAR correction models by a large margin with a competitive low latency; and 3) it is an universal method, as it reduces all WERs of the ASR model with different decoding strategies and reduces all WERs of ASR models trained on different scale datasets.

</details>

### [End to end Hindi to English speech conversion using Bark, mBART and a finetuned XLSR Wav2Vec2](2401.06183.md)
**Aniket Tathe, Anand Kamble, Suyash Kumbharkar, Atharva Bhandare et al.** · 2024-01-11

<details>
<summary>Abstract</summary>

Speech has long been a barrier to effective communication and connection, persisting as a challenge in our increasingly interconnected world. This research paper introduces a transformative solution to this persistent obstacle an end-to-end speech conversion framework tailored for Hindi-to-English translation, culminating in the synthesis of English audio. By integrating cutting-edge technologies such as XLSR Wav2Vec2 for automatic speech recognition (ASR), mBART for neural machine translation (NMT), and a Text-to-Speech (TTS) synthesis component, this framework offers a unified and seamless approach to cross-lingual communication. We delve into the intricate details of each component, elucidating their individual contributions and exploring the synergies that enable a fluid transition from spoken Hindi to synthesized English audio.

</details>

### [Continuously Learning New Words in Automatic Speech Recognition](2401.04482.md)
**Christian Huber, Alexander Waibel** · 2024-01-09

<details>
<summary>Abstract</summary>

Despite recent advances, Automatic Speech Recognition (ASR) systems are still far from perfect. Typical errors include acronyms, named entities, and domain-specific special words for which little or no labeled data is available. To address the problem of recognizing these words, we propose a self-supervised continual learning approach: Given the audio of a lecture talk with the corresponding slides, we bias the model towards decoding new words from the slides by using a memory-enhanced ASR model from the literature. Then, we perform inference on the talk, collecting utterances that contain detected new words into an adaptation data set. Continual learning is then performed by training adaptation weights added to the model on this data set. The whole procedure is iterated for many talks. We show that with this approach, we obtain increasing performance on the new words when they occur more frequently (more than 80% recall) while preserving the general performance of the model.

</details>

### [High-precision Voice Search Query Correction via Retrievable Speech-text Embedings](2401.04235.md)
**Christopher Li, Gary Wang, Kyle Kastner, Heng Su et al.** · 2024-01-08

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems can suffer from poor recall for various reasons, such as noisy audio, lack of sufficient training data, etc. Previous work has shown that recall can be improved by retrieving rewrite candidates from a large database of likely, contextually-relevant alternatives to the hypothesis text using nearest-neighbors search over embeddings of the ASR hypothesis text to correct and candidate corrections. However, ASR-hypothesis-based retrieval can yield poor precision if the textual hypotheses are too phonetically dissimilar to the transcript truth. In this paper, we eliminate the hypothesis-audio mismatch problem by querying the correction database directly using embeddings derived from the utterance audio; the embeddings of the utterance audio and candidate corrections are produced by multimodal speech-text embedding networks trained to place the embedding of the audio of an utterance and the embedding of its corresponding textual transcript close together. After locating an appropriate correction candidate using nearest-neighbor search, we score the candidate with its speech-text embedding distance before adding the candidate to the original n-best list. We show a relative word error rate (WER) reduction of 6% on utterances whose transcripts appear in the candidate set, without increasing WER on general utterances.

</details>

### [Cross-Speaker Encoding Network for Multi-Talker Speech Recognition](2401.04152.md)
**Jiawen Kang, Lingwei Meng, Mingyu Cui, Haohan Guo et al.** · 2024-01-08

<details>
<summary>Abstract</summary>

End-to-end multi-talker speech recognition has garnered great interest as an effective approach to directly transcribe overlapped speech from multiple speakers. Current methods typically adopt either 1) single-input multiple-output (SIMO) models with a branched encoder, or 2) single-input single-output (SISO) models based on attention-based encoder-decoder architecture with serialized output training (SOT). In this work, we propose a Cross-Speaker Encoding (CSE) network to address the limitations of SIMO models by aggregating cross-speaker representations. Furthermore, the CSE model is integrated with SOT to leverage both the advantages of SIMO and SISO while mitigating their drawbacks. To the best of our knowledge, this work represents an early effort to integrate SIMO and SISO for multi-talker speech recognition. Experiments on the two-speaker LibrispeechMix dataset show that the CES model reduces word error rate (WER) by 8% over the SIMO baseline. The CSE-SOT model reduces WER by 10% overall and by 16% on high-overlap speech compared to the SOT model. Code is available at https://github.com/kjw11/CSEnet-ASR.

</details>

### [LUPET: Incorporating Hierarchical Information Path into Multilingual ASR](2401.03689.md)
**Wei Liu, Jingyong Hou, Dong Yang, Muyong Cao et al.** · 2024-01-08

<details>
<summary>Abstract</summary>

Toward high-performance multilingual automatic speech recognition (ASR), various types of linguistic information and model design have demonstrated their effectiveness independently. They include language identity (LID), phoneme information, language-specific processing modules, and cross-lingual self-supervised speech representation. It is expected that leveraging their benefits synergistically in a unified solution would further improve the overall system performance. This paper presents a novel design of a hierarchical information path, named LUPET, which sequentially encodes, from the shallow layers to deep layers, multiple aspects of linguistic and acoustic information at diverse granularity scales. The path starts from LID prediction, followed by acoustic unit discovery, phoneme sharing, and finally token recognition routed by a mixture-of-expert. ASR experiments are carried out on 10 languages in the Common Voice corpus. The results demonstrate the superior performance of LUPET as compared to the baseline systems. Most importantly, LUPET effectively mitigates the issue of performance compromise of high-resource languages with low-resource ones in the multilingual setting.

</details>

### [FunnyNet-W: Multimodal Learning of Funny Moments in Videos in the Wild](2401.04210.md)
**Zhi-Song Liu, Robin Courant, Vicky Kalogeiton** · 2024-01-08

<details>
<summary>Abstract</summary>

Automatically understanding funny moments (i.e., the moments that make people laugh) when watching comedy is challenging, as they relate to various features, such as body language, dialogues and culture. In this paper, we propose FunnyNet-W, a model that relies on cross- and self-attention for visual, audio and text data to predict funny moments in videos. Unlike most methods that rely on ground truth data in the form of subtitles, in this work we exploit modalities that come naturally with videos: (a) video frames as they contain visual information indispensable for scene understanding, (b) audio as it contains higher-level cues associated with funny moments, such as intonation, pitch and pauses and (c) text automatically extracted with a speech-to-text model as it can provide rich information when processed by a Large Language Model. To acquire labels for training, we propose an unsupervised approach that spots and labels funny audio moments. We provide experiments on five datasets: the sitcoms TBBT, MHD, MUStARD, Friends, and the TED talk UR-Funny. Extensive experiments and analysis show that FunnyNet-W successfully exploits visual, auditory and textual cues to identify funny moments, while our findings reveal FunnyNet-W's ability to predict funny moments in the wild. FunnyNet-W sets the new state of the art for funny moment detection with multimodal cues on all datasets with and without using ground truth information.

</details>

### [The NPU-ASLP-LiAuto System Description for Visual Speech Recognition in CNVSRC 2023](2401.06788.md)
**He Wang, Pengcheng Guo, Wei Chen, Pan Zhou et al.** · 2024-01-07

<details>
<summary>Abstract</summary>

This paper delineates the visual speech recognition (VSR) system introduced by the NPU-ASLP-LiAuto (Team 237) in the first Chinese Continuous Visual Speech Recognition Challenge (CNVSRC) 2023, engaging in the fixed and open tracks of Single-Speaker VSR Task, and the open track of Multi-Speaker VSR Task. In terms of data processing, we leverage the lip motion extractor from the baseline1 to produce multi-scale video data. Besides, various augmentation techniques are applied during training, encompassing speed perturbation, random rotation, horizontal flipping, and color transformation. The VSR model adopts an end-to-end architecture with joint CTC/attention loss, comprising a ResNet3D visual frontend, an E-Branchformer encoder, and a Transformer decoder. Experiments show that our system achieves 34.76% CER for the Single-Speaker Task and 41.06% CER for the Multi-Speaker Task after multi-system fusion, ranking first place in all three tracks we participate.

</details>

### [Multichannel AV-wav2vec2: A Framework for Learning Multichannel Multi-Modal Speech Representation](2401.03468.md)
**Qiushi Zhu, Jie Zhang, Yu Gu, Yuchen Hu et al.** · 2024-01-07

<details>
<summary>Abstract</summary>

Self-supervised speech pre-training methods have developed rapidly in recent years, which show to be very effective for many near-field single-channel speech tasks. However, far-field multichannel speech processing is suffering from the scarcity of labeled multichannel data and complex ambient noises. The efficacy of self-supervised learning for far-field multichannel and multi-modal speech processing has not been well explored. Considering that visual information helps to improve speech recognition performance in noisy scenes, in this work we propose a multichannel multi-modal speech self-supervised learning framework AV-wav2vec2, which utilizes video and multichannel audio data as inputs. First, we propose a multi-path structure to process multichannel audio streams and a visual stream in parallel, with intra- and inter-channel contrastive losses as training targets to fully exploit the spatiotemporal information in multichannel speech data. Second, based on contrastive learning, we use additional single-channel audio data, which is trained jointly to improve the performance of speech representation. Finally, we use a Chinese multichannel multi-modal dataset in real scenarios to validate the effectiveness of the proposed method on audio-visual speech recognition (AVSR), automatic speech recognition (ASR), visual speech recognition (VSR) and audio-visual speaker diarization (AVSD) tasks.

</details>

### [MLCA-AVSR: Multi-Layer Cross Attention Fusion based Audio-Visual Speech Recognition](2401.03424.md)
**He Wang, Pengcheng Guo, Pan Zhou, Lei Xie** · 2024-01-07

<details>
<summary>Abstract</summary>

While automatic speech recognition (ASR) systems degrade significantly in noisy environments, audio-visual speech recognition (AVSR) systems aim to complement the audio stream with noise-invariant visual cues and improve the system's robustness. However, current studies mainly focus on fusing the well-learned modality features, like the output of modality-specific encoders, without considering the contextual relationship during the modality feature learning. In this study, we propose a multi-layer cross-attention fusion based AVSR (MLCA-AVSR) approach that promotes representation learning of each modality by fusing them at different levels of audio/visual encoders. Experimental results on the MISP2022-AVSR Challenge dataset show the efficacy of our proposed system, achieving a concatenated minimum permutation character error rate (cpCER) of 30.57% on the Eval set and yielding up to 3.17% relative improvement compared with our previous system which ranked the second place in the challenge. Following the fusion of multiple systems, our proposed approach surpasses the first-place system, establishing a new SOTA cpCER of 29.13% on this dataset.

</details>

### [TeLeS: Temporal Lexeme Similarity Score to Estimate Confidence in End-to-End ASR](2401.03251.md)
**Nagarathna Ravi, Thishyan Raj T, Vipul Arora** · 2024-01-06

<details>
<summary>Abstract</summary>

Confidence estimation of predictions from an End-to-End (E2E) Automatic Speech Recognition (ASR) model benefits ASR's downstream and upstream tasks. Class-probability-based confidence scores do not accurately represent the quality of overconfident ASR predictions. An ancillary Confidence Estimation Model (CEM) calibrates the predictions. State-of-the-art (SOTA) solutions use binary target scores for CEM training. However, the binary labels do not reveal the granular information of predicted words, such as temporal alignment between reference and hypothesis and whether the predicted word is entirely incorrect or contains spelling errors. Addressing this issue, we propose a novel Temporal-Lexeme Similarity (TeLeS) confidence score to train CEM. To address the data imbalance of target scores while training CEM, we use shrinkage loss to focus on hard-to-learn data points and minimise the impact of easily learned data points. We conduct experiments with ASR models trained in three languages, namely Hindi, Tamil, and Kannada, with varying training data sizes. Experiments show that TeLeS generalises well across domains. To demonstrate the applicability of the proposed method, we formulate a TeLeS-based Acquisition (TeLeS-A) function for sampling uncertainty in active learning. We observe a significant reduction in the Word Error Rate (WER) as compared to SOTA methods.

</details>

### [Part-of-Speech Tagger for Bodo Language using Deep Learning approach](2401.03175.md)
**Dhrubajyoti Pathak, Sanjib Narzary, Sukumar Nandi, Bidisha Som** · 2024-01-06

<details>
<summary>Abstract</summary>

Language Processing systems such as Part-of-speech tagging, Named entity recognition, Machine translation, Speech recognition, and Language modeling (LM) are well-studied in high-resource languages. Nevertheless, research on these systems for several low-resource languages, including Bodo, Mizo, Nagamese, and others, is either yet to commence or is in its nascent stages. Language model plays a vital role in the downstream tasks of modern NLP. Extensive studies are carried out on LMs for high-resource languages. Nevertheless, languages such as Bodo, Rabha, and Mising continue to lack coverage. In this study, we first present BodoBERT, a language model for the Bodo language. To the best of our knowledge, this work is the first such effort to develop a language model for Bodo. Secondly, we present an ensemble DL-based POS tagging model for Bodo. The POS tagging model is based on combinations of BiLSTM with CRF and stacked embedding of BodoBERT with BytePairEmbeddings. We cover several language models in the experiment to see how well they work in POS tagging tasks. The best-performing model achieves an F1 score of 0.8041. A comparative experiment was also conducted on Assamese POS taggers, considering that the language is spoken in the same region as Bodo.

</details>

### [A unified multichannel far-field speech recognition system: combining neural beamforming with attention based end-to-end model](2401.02673.md)
**Dongdi Zhao, Jianbo Ma, Lu Lu, Jinke Li et al.** · 2024-01-05

<details>
<summary>Abstract</summary>

Far-field speech recognition is a challenging task that conventionally uses signal processing beamforming to attack noise and interference problem. But the performance has been found usually limited due to heavy reliance on environmental assumption. In this paper, we propose a unified multichannel far-field speech recognition system that combines the neural beamforming and transformer-based Listen, Spell, Attend (LAS) speech recognition system, which extends the end-to-end speech recognition system further to include speech enhancement. Such framework is then jointly trained to optimize the final objective of interest. Specifically, factored complex linear projection (fCLP) has been adopted to form the neural beamforming. Several pooling strategies to combine look directions are then compared in order to find the optimal approach. Moreover, information of the source direction is also integrated in the beamforming to explore the usefulness of source direction as a prior, which is usually available especially in multi-modality scenario. Experiments on different microphone array geometry are conducted to evaluate the robustness against spacing variance of microphone array. Large in-house databases are used to evaluate the effectiveness of the proposed framework and the proposed method achieve 19.26\% improvement when compared with a strong baseline.

</details>

### [Task Oriented Dialogue as a Catalyst for Self-Supervised Automatic Speech Recognition](2401.02417.md)
**David M. Chan, Shalini Ghosh, Hitesh Tulsiani, Ariya Rastrow et al.** · 2024-01-04

<details>
<summary>Abstract</summary>

While word error rates of automatic speech recognition (ASR) systems have consistently fallen, natural language understanding (NLU) applications built on top of ASR systems still attribute significant numbers of failures to low-quality speech recognition results. Existing assistant systems collect large numbers of these unsuccessful interactions, but these systems usually fail to learn from these interactions, even in an offline fashion. In this work, we introduce CLC: Contrastive Learning for Conversations, a family of methods for contrastive fine-tuning of models in a self-supervised fashion, making use of easily detectable artifacts in unsuccessful conversations with assistants. We demonstrate that our CLC family of approaches can improve the performance of ASR models on OD3, a new public large-scale semi-synthetic meta-dataset of audio task-oriented dialogues, by up to 19.2%. These gains transfer to real-world systems as well, where we show that CLC can help to improve performance by up to 6.7% over baselines. We make OD3 publicly available at https://github.com/amazon-science/amazon-od3 .

</details>

### [CTC Blank Triggered Dynamic Layer-Skipping for Efficient CTC-based Speech Recognition](2401.02046.md)
**Junfeng Hou, Peiyao Wang, Jincheng Zhang, Meng Yang et al.** · 2024-01-04

<details>
<summary>Abstract</summary>

Deploying end-to-end speech recognition models with limited computing resources remains challenging, despite their impressive performance. Given the gradual increase in model size and the wide range of model applications, selectively executing model components for different inputs to improve the inference efficiency is of great interest. In this paper, we propose a dynamic layer-skipping method that leverages the CTC blank output from intermediate layers to trigger the skipping of the last few encoder layers for frames with high blank probabilities. Furthermore, we factorize the CTC output distribution and perform knowledge distillation on intermediate layers to reduce computation and improve recognition accuracy. Experimental results show that by utilizing the CTC blank, the encoder layer depth can be adjusted dynamically, resulting in 29% acceleration of the CTC model inference with minor performance degradation.

</details>

### [Hallucinations in Neural Automatic Speech Recognition: Identifying Errors and Hallucinatory Models](2401.01572.md)
**Rita Frieske, Bertram E. Shi** · 2024-01-03

<details>
<summary>Abstract</summary>

Hallucinations are a type of output error produced by deep neural networks. While this has been studied in natural language processing, they have not been researched previously in automatic speech recognition. Here, we define hallucinations in ASR as transcriptions generated by a model that are semantically unrelated to the source utterance, yet still fluent and coherent. The similarity of hallucinations to probable natural language outputs of the model creates a danger of deception and impacts the credibility of the system. We show that commonly used metrics, such as word error rates, cannot differentiate between hallucinatory and non-hallucinatory models. To address this, we propose a perturbation-based method for assessing the susceptibility of an automatic speech recognition (ASR) model to hallucination at test time, which does not require access to the training dataset. We demonstrate that this method helps to distinguish between hallucinatory and non-hallucinatory models that have similar baseline word error rates. We further explore the relationship between the types of ASR errors and the types of dataset noise to determine what types of noise are most likely to create hallucinatory outputs. We devise a framework for identifying hallucinations by analysing their semantic connection with the ground truth and their fluency. Finally, we discover how to induce hallucinations with a random noise injection to the utterance.

</details>

### [The Art of Deception: Robust Backdoor Attack using Dynamic Stacking of Triggers](2401.01537.md)
**Orson Mengara** · 2024-01-03

<details>
<summary>Abstract</summary>

The area of Machine Learning as a Service (MLaaS) is experiencing increased implementation due to recent advancements in the AI (Artificial Intelligence) industry. However, this spike has prompted concerns regarding AI defense mechanisms, specifically regarding potential covert attacks from third-party providers that cannot be entirely trusted. Recent research has uncovered that auditory backdoors may use certain modifications as their initiating mechanism. DynamicTrigger is introduced as a methodology for carrying out dynamic backdoor attacks that use cleverly designed tweaks to ensure that corrupted samples are indistinguishable from clean. By utilizing fluctuating signal sampling rates and masking speaker identities through dynamic sound triggers (such as the clapping of hands), it is possible to deceive speech recognition systems (ASR). Our empirical testing demonstrates that DynamicTrigger is both potent and stealthy, achieving impressive success rates during covert attacks while maintaining exceptional accuracy with non-poisoned datasets.

</details>

### [Enhancing Pre-trained ASR System Fine-tuning for Dysarthric Speech Recognition using Adversarial Data Augmentation](2401.00662.md)
**Huimeng Wang, Zengrui Jin, Mengzhe Geng, Shujie Hu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Automatic recognition of dysarthric speech remains a highly challenging task to date. Neuro-motor conditions and co-occurring physical disabilities create difficulty in large-scale data collection for ASR system development. Adapting SSL pre-trained ASR models to limited dysarthric speech via data-intensive parameter fine-tuning leads to poor generalization. To this end, this paper presents an extensive comparative study of various data augmentation approaches to improve the robustness of pre-trained ASR model fine-tuning to dysarthric speech. These include: a) conventional speaker-independent perturbation of impaired speech; b) speaker-dependent speed perturbation, or GAN-based adversarial perturbation of normal, control speech based on their time alignment against parallel dysarthric speech; c) novel Spectral basis GAN-based adversarial data augmentation operating on non-parallel data. Experiments conducted on the UASpeech corpus suggest GAN-based data augmentation consistently outperforms fine-tuned Wav2vec2.0 and HuBERT models using no data augmentation and speed perturbation across different data expansion operating points by statistically significant word error rate (WER) reductions up to 2.01% and 0.96% absolute (9.03% and 4.63% relative) respectively on the UASpeech test set of 16 dysarthric speakers. After cross-system outputs rescoring, the best system produced the lowest published WER of 16.53% (46.47% on very low intelligibility) on UASpeech.

</details>

### [Double Decoder: Improving latency for Streaming End-to-end ASR Models](s2:70d9fd8dd0841614dca8e7cd3f396cbf0eabc945.md)
**Riqiang Wang, Shreekantha Nadig, Daniil Kulko, Simon Vandieken et al.** · 2024-01-01

### [Fine-Tuning ASR models for Very Low-Resource Languages: A Study on Mvskoke](s2:34b4f6f36a6f0158d4a7b2da89d382a44394ea97.md)
**Julia Mainzinger, Gina-Anne Levow** · 2024-01-01

<details>
<summary>Abstract</summary>

Recent advancements in multilingual models for automatic speech recognition (ASR) have been able to achieve a high accuracy for languages with extremely limited resources. This study examines ASR modeling for the Mvskoke language, an indigenous language of America. The parameter efficiency of adapter training is contrasted with training entire models, and it is demonstrated how performance varies with different amounts of data. Ad-ditionally, the models are evaluated with tri-gram language model decoding, and the outputs are compared across different types of speech recordings. Results show that training an adapter is both parameter efficient and gives higher accuracy for a relatively small amount of data.

</details>

### [4D ASR: Joint Beam Search Integrating CTC, Attention, Transducer, and Mask Predict Decoders](s2:0ce0c19c712705451709eafb0eaeca37196ec6aa.md)
**Yui Sudo, Muhammad Shakeel, Yosuke Fukumoto, Brian Yan et al.** · 2024-01-01

### [Massive End-to-end Speech Recognition Models with Time Reduction](s2:ead12d7dddceb7555d7b1094f0d1893b07490111.md)
**Weiran Wang, Rohit Prabhavalkar, Haozhe Shan, Zhong Meng et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

We investigate massive end-to-end automatic speech recognition (ASR) models with efficiency improvements achieved by time reduction. The encoders of our models use the neural architecture of Google’s universal speech model (USM), with additional funnel pooling layers to significantly reduce the frame rate and speed up training and inference. We also explore a few practical methods to mitigate potential accuracy loss due to time reduction, while enjoying most efficiency gain. Our methods are demonstrated to work with both Connectionist Temporal Classification (CTC) and RNN-Transducer (RNN-T), with up to 2B model parameters, and over two domains. For a large-scale voice search recognition task, we perform extensive studies on vocabulary size, time reduction strategy, and its generalization performance on long-form test sets, and show that a 900M RNN-T is very tolerant to severe time reduction, with as low encoder output frame rate as 640ms. We also provide ablation studies on the Librispeech benchmark for important training hyperparameters and architecture designs, in training 600M RNN-T models at the frame rate of 160ms.

</details>

### [Speech Recognition Enhancement and Compression Perception in Russian Translation Teaching Cooperative System Application](s2:8474f01ceb44492aeb63d469daac951c969c8345.md)
**Di Xu** · 2024-01-01

<details>
<summary>Abstract</summary>

Abstract In the digital age, characterized by the ubiquity of big data and artificial intelligence, Russian translation education is poised for transformative change. This study explores the integration of advanced speech recognition and compressed perception technologies into Russian translation instruction, highlighting their potential to elevate educational quality and translator training. Utilizing the Spring Boot framework, we developed a comprehensive Russian translation teaching system, incorporating a Russian-Chinese speech translation model that leverages the RNN Transducer model and an N-gram language model, alongside compressed perception theory for efficient speech signal processing. Our findings reveal a notable enhancement in Russian speech recognition accuracy and processing speed, with a 4.73% improvement in endto-end speech detection accuracy and a significant reduction in word error rate, outperforming CTC and CTC-LM models by 14.79% to 24.85%. Furthermore, speech quality and intelligibility scores experienced marked improvements. The application of speech recognition enhancement and compressed perception technologies emerges as a vital strategy for enriching Russian translation pedagogy and fostering the development of proficient translators.

</details>

