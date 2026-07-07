# 2021

648 papers in this year.

### [Temporal Attention Augmented Transformer Hawkes Process](2112.14472.md)
**Lu-ning Zhang, Jian-wei Liu, Zhi-yan Song, Xin Zuo** · 2021-12-29

<details>
<summary>Abstract</summary>

In recent years, mining the knowledge from asynchronous sequences by Hawkes process is a subject worthy of continued attention, and Hawkes processes based on the neural network have gradually become the most hotly researched fields, especially based on the recurrence neural network (RNN). However, these models still contain some inherent shortcomings of RNN, such as vanishing and exploding gradient and long-term dependency problems. Meanwhile, Transformer based on self-attention has achieved great success in sequential modeling like text processing and speech recognition. Although the Transformer Hawkes process (THP) has gained huge performance improvement, THPs do not effectively utilize the temporal information in the asynchronous events, for these asynchronous sequences, the event occurrence instants are as important as the types of events, while conventional THPs simply convert temporal information into position encoding and add them as the input of transformer. With this in mind, we come up with a new kind of Transformer-based Hawkes process model, Temporal Attention Augmented Transformer Hawkes Process (TAA-THP), we modify the traditional dot-product attention structure, and introduce the temporal encoding into attention structure. We conduct numerous experiments on a wide range of synthetic and real-life datasets to validate the performance of our proposed TAA-THP model, significantly improvement compared with existing baseline models on the different measurements is achieved, including log-likelihood on the test dataset, and prediction accuracies of event types and occurrence times. In addition, through the ablation studies, we vividly demonstrate the merit of introducing additional temporal attention by comparing the performance of the model with and without temporal attention.

</details>

### [Bridging the Gap: Using Deep Acoustic Representations to Learn Grounded Language from Percepts and Raw Speech](2112.13758.md)
**Gaoussou Youssouf Kebe, Luke E. Richards, Edward Raff, Francis Ferraro et al.** · 2021-12-27

<details>
<summary>Abstract</summary>

Learning to understand grounded language, which connects natural language to percepts, is a critical research area. Prior work in grounded language acquisition has focused primarily on textual inputs. In this work we demonstrate the feasibility of performing grounded language acquisition on paired visual percepts and raw speech inputs. This will allow interactions in which language about novel tasks and environments is learned from end users, reducing dependence on textual inputs and potentially mitigating the effects of demographic bias found in widely available speech recognition systems. We leverage recent work in self-supervised speech representation models and show that learned representations of speech can make language grounding systems more inclusive towards specific groups while maintaining or even increasing general performance.

</details>

### [Multi-Dialect Arabic Speech Recognition](2112.14678.md)
**Abbas Raza Ali** · 2021-12-25

<details>
<summary>Abstract</summary>

This paper presents the design and development of multi-dialect automatic speech recognition for Arabic. Deep neural networks are becoming an effective tool to solve sequential data problems, particularly, adopting an end-to-end training of the system. Arabic speech recognition is a complex task because of the existence of multiple dialects, non-availability of large corpora, and missing vocalization. Thus, the first contribution of this work is the development of a large multi-dialectal corpus with either full or at least partially vocalized transcription. Additionally, the open-source corpus has been gathered from multiple sources that bring non-standard Arabic alphabets in transcription which are normalized by defining a common character-set. The second contribution is the development of a framework to train an acoustic model achieving state-of-the-art performance. The network architecture comprises of a combination of convolutional and recurrent layers. The spectrogram features of the audio data are extracted in the frequency vs time domain and fed in the network. The output frames, produced by the recurrent model, are further trained to align the audio features with its corresponding transcription sequences. The sequence alignment is performed using a beam search decoder with a tetra-gram language model. The proposed system achieved a 14% error rate which outperforms previous systems.

</details>

### [Multi-Variant Consistency based Self-supervised Learning for Robust Automatic Speech Recognition](2112.12522.md)
**Changfeng Gao, Gaofeng Cheng, Pengyuan Zhang** · 2021-12-23

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has shown rapid advances in recent years but still degrades significantly in far-field and noisy environments. The recent development of self-supervised learning (SSL) technology can improve the ASR performance by pre-training the model with additional unlabeled speech and the SSL pre-trained model has achieved the state-of-the-art result on several speech benchmarks. Nevertheless, most of the previous SSL methods ignore the influence of the background noise or reverberation, which is crucial to deploying ASR systems in real-world speech applications. This study addresses the robust ASR by introducing a multi-variant consistency (MVC) based SSL method that adapts to different environments. The MVC-SSL is a robust SSL pre-training method designed for noisy and distant-talking speech in real-world applications. Compared to the previous SSL method, the MVC-SSL can calculate the contrastive loss among audios from different acoustic conditions or channels and can learn invariant representations with the change in the environment or the recording equipment. We also explore different SSL training pipelines to balance the noisy distant-talking speech and extra high resource clean speech. We evaluate the proposed method on the commercially-motivated dataset, CHiME-4, and the meeting dataset, AMI. With the help of the MVC-SSL and appropriate training pipeline, we can achieve up to 30% relative word error rate reductions over the baseline wav2vec2.0, one of the most successful SSL methods for ASR.

</details>

### [InstaIndoor and Multi-modal Deep Learning for Indoor Scene Recognition](2112.12409.md)
**Andreea Glavan, Estefania Talavera** · 2021-12-23

<details>
<summary>Abstract</summary>

Indoor scene recognition is a growing field with great potential for behaviour understanding, robot localization, and elderly monitoring, among others. In this study, we approach the task of scene recognition from a novel standpoint, using multi-modal learning and video data gathered from social media. The accessibility and variety of social media videos can provide realistic data for modern scene recognition techniques and applications. We propose a model based on fusion of transcribed speech to text and visual features, which is used for classification on a novel dataset of social media videos of indoor scenes named InstaIndoor. Our model achieves up to 70% accuracy and 0.7 F1-Score. Furthermore, we highlight the potential of our approach by benchmarking on a YouTube-8M subset of indoor scenes as well, where it achieves 74% accuracy and 0.74 F1-Score. We hope the contributions of this work pave the way to novel research in the challenging field of indoor scene recognition.

</details>

### [VoiceMoji: A Novel On-Device Pipeline for Seamless Emoji Insertion in Dictation](2112.12028.md)
**Sumit Kumar, Harichandana B S S, Himanshu Arora** · 2021-12-22

<details>
<summary>Abstract</summary>

Most of the speech recognition systems recover only words in the speech and fail to capture emotions. Users have to manually add emoji(s) in text for adding tone and making communication fun. Though there is much work done on punctuation addition on transcribed speech, the area of emotion addition is untouched. In this paper, we propose a novel on-device pipeline to enrich the voice input experience. It involves, given a blob of transcribed text, intelligently processing and identifying structure where emoji insertion makes sense. Moreover, it includes semantic text analysis to predict emoji for each of the sub-parts for which we propose a novel architecture Attention-based Char Aware (ACA) LSTM which handles Out-Of-Vocabulary (OOV) words as well. All these tasks are executed completely on-device and hence can aid on-device dictation systems. To the best of our knowledge, this is the first work that shows how to add emoji(s) in the transcribed text. We demonstrate that our components achieve comparable results to previous neural approaches for punctuation addition and emoji prediction with 80% fewer parameters. Overall, our proposed model has a very small memory footprint of a mere 4MB to suit on-device deployment.

</details>

### [Voice Quality and Pitch Features in Transformer-Based Speech Recognition](2112.11391.md)
**Guillermo Cámbara, Jordi Luque, Mireia Farrús** · 2021-12-21

<details>
<summary>Abstract</summary>

Jitter and shimmer measurements have shown to be carriers of voice quality and prosodic information which enhance the performance of tasks like speaker recognition, diarization or automatic speech recognition (ASR). However, such features have been seldom used in the context of neural-based ASR, where spectral features often prevail. In this work, we study the effects of incorporating voice quality and pitch features altogether and separately to a Transformer-based ASR model, with the intuition that the attention mechanisms might exploit latent prosodic traits. For doing so, we propose separated convolutional front-ends for prosodic and spectral features, showing that this architectural choice yields better results than simple concatenation of such pitch and voice quality features to mel-spectrogram filterbanks. Furthermore, we find mean Word Error Rate relative reductions of up to 5.6% with the LibriSpeech benchmark. Such findings motivate further research on the application of prosody knowledge for increasing the robustness of Transformer-based ASR.

</details>

### [Regularizing End-to-End Speech Translation with Triangular Decomposition Agreement](2112.10991.md)
**Yichao Du, Zhirui Zhang, Weizhi Wang, Boxing Chen et al.** · 2021-12-21

<details>
<summary>Abstract</summary>

End-to-end speech-to-text translation (E2E-ST) is becoming increasingly popular due to the potential of its less error propagation, lower latency, and fewer parameters. Given the triplet training corpus $\langle speech, transcription, translation\rangle$, the conventional high-quality E2E-ST system leverages the $\langle speech, transcription\rangle$ pair to pre-train the model and then utilizes the $\langle speech, translation\rangle$ pair to optimize it further. However, this process only involves two-tuple data at each stage, and this loose coupling fails to fully exploit the association between triplet data. In this paper, we attempt to model the joint probability of transcription and translation based on the speech input to directly leverage such triplet data. Based on that, we propose a novel regularization method for model training to improve the agreement of dual-path decomposition within triplet data, which should be equal in theory. To achieve this goal, we introduce two Kullback-Leibler divergence regularization terms into the model training objective to reduce the mismatch between output probabilities of dual-path. Then the well-trained model can be naturally transformed as the E2E-ST models by the pre-defined early stop tag. Experiments on the MuST-C benchmark demonstrate that our proposed approach significantly outperforms state-of-the-art E2E-ST baselines on all 8 language pairs, while achieving better performance in the automatic speech recognition task. Our code is open-sourced at https://github.com/duyichao/E2E-ST-TDA.

</details>

### [Load-balanced Gather-scatter Patterns for Sparse Deep Neural Networks](2112.10898.md)
**Fei Sun, Minghai Qin, Tianyun Zhang, Xiaolong Ma et al.** · 2021-12-20

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been proven to be effective in solving many real-life problems, but its high computation cost prohibits those models from being deployed to edge devices. Pruning, as a method to introduce zeros to model weights, has shown to be an effective method to provide good trade-offs between model accuracy and computation efficiency, and is a widely-used method to generate compressed models. However, the granularity of pruning makes important trade-offs. At the same sparsity level, a coarse-grained structured sparse pattern is more efficient on conventional hardware but results in worse accuracy, while a fine-grained unstructured sparse pattern can achieve better accuracy but is inefficient on existing hardware. On the other hand, some modern processors are equipped with fast on-chip scratchpad memories and gather/scatter engines that perform indirect load and store operations on such memories. In this work, we propose a set of novel sparse patterns, named gather-scatter (GS) patterns, to utilize the scratchpad memories and gather/scatter engines to speed up neural network inferences. Correspondingly, we present a compact sparse format. The proposed set of sparse patterns, along with a novel pruning methodology, address the load imbalance issue and result in models with quality close to unstructured sparse models and computation efficiency close to structured sparse models. Our experiments show that GS patterns consistently make better trade-offs between accuracy and computation efficiency compared to conventional structured sparse patterns. GS patterns can reduce the runtime of the DNN components by two to three times at the same accuracy levels. This is confirmed on three different deep learning tasks and popular models, namely, GNMT for machine translation, ResNet50 for image recognition, and Japser for acoustic speech recognition.

</details>

### [Integrating Knowledge in End-to-End Automatic Speech Recognition for Mandarin-English Code-Switching](2112.10202.md)
**Chia-Yu Li, Ngoc Thang Vu** · 2021-12-19

<details>
<summary>Abstract</summary>

Code-Switching (CS) is a common linguistic phenomenon in multilingual communities that consists of switching between languages while speaking. This paper presents our investigations on end-to-end speech recognition for Mandarin-English CS speech. We analyse different CS specific issues such as the properties mismatches between languages in a CS language pair, the unpredictable nature of switching points, and the data scarcity problem. We exploit and improve the state-of-the-art end-to-end system by merging nonlinguistic symbols, by integrating language identification using hierarchical softmax, by modeling sub-word units, by artificially lowering the speaking rate, and by augmenting data using speed perturbed technique and several monolingual datasets to improve the final performance not only on CS speech but also on monolingual benchmarks in order to make the system more applicable on real life settings. Finally, we explore the effect of different language model integration methods on the performance of the proposed model. Our experimental results reveal that all the proposed techniques improve the recognition performance. The best combined system improves the baseline system by up to 35% relatively in terms of mixed error rate and delivers acceptable performance on monolingual benchmarks.

</details>

### [Multi-turn RNN-T for streaming recognition of multi-party speech](2112.10200.md)
**Ilya Sklyar, Anna Piunova, Xianrui Zheng, Yulan Liu** · 2021-12-19

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) of single channel far-field recordings with an unknown number of speakers is traditionally tackled by cascaded modules. Recent research shows that end-to-end (E2E) multi-speaker ASR models can achieve superior recognition accuracy compared to modular systems. However, these models do not ensure real-time applicability due to their dependency on full audio context. This work takes real-time applicability as the first priority in model design and addresses a few challenges in previous work on multi-speaker recurrent neural network transducer (MS-RNN-T). First, we introduce on-the-fly overlapping speech simulation during training, yielding 14% relative word error rate (WER) improvement on LibriSpeechMix test set. Second, we propose a novel multi-turn RNN-T (MT-RNN-T) model with an overlap-based target arrangement strategy that generalizes to an arbitrary number of speakers without changes in the model architecture. We investigate the impact of the maximum number of speakers seen during training on MT-RNN-T performance on LibriCSS test set, and report 28% relative WER improvement over the two-speaker MS-RNN-T. Third, we experiment with a rich transcription strategy for joint recognition and segmentation of multi-party speech. Through an in-depth analysis, we discuss potential pitfalls of the proposed system as well as promising future research directions.

</details>

### [Investigation of Densely Connected Convolutional Networks with Domain Adversarial Learning for Noise Robust Speech Recognition](2112.10108.md)
**Chia Yu Li, Ngoc Thang Vu** · 2021-12-19

<details>
<summary>Abstract</summary>

We investigate densely connected convolutional networks (DenseNets) and their extension with domain adversarial training for noise robust speech recognition. DenseNets are very deep, compact convolutional neural networks which have demonstrated incredible improvements over the state-of-the-art results in computer vision. Our experimental results reveal that DenseNets are more robust against noise than other neural network based models such as deep feed forward neural networks and convolutional neural networks. Moreover, domain adversarial learning can further improve the robustness of DenseNets against both, known and unknown noise conditions.

</details>

### [A singular Riemannian geometry approach to Deep Neural Networks I. Theoretical foundations](2201.09656.md)
**Alessandro Benfenati, Alessio Marta** · 2021-12-17

<details>
<summary>Abstract</summary>

Deep Neural Networks are widely used for solving complex problems in several scientific areas, such as speech recognition, machine translation, image analysis. The strategies employed to investigate their theoretical properties mainly rely on Euclidean geometry, but in the last years new approaches based on Riemannian geometry have been developed. Motivated by some open problems, we study a particular sequence of maps between manifolds, with the last manifold of the sequence equipped with a Riemannian metric. We investigate the structures induced trough pullbacks on the other manifolds of the sequence and on some related quotients. In particular, we show that the pullbacks of the final Riemannian metric to any manifolds of the sequence is a degenerate Riemannian metric inducing a structure of pseudometric space, we show that the Kolmogorov quotient of this pseudometric space yields a smooth manifold, which is the base space of a particular vertical bundle. We investigate the theoretical properties of the maps of such sequence, eventually we focus on the case of maps between manifolds implementing neural networks of practical interest and we present some applications of the geometric framework we introduced in the first part of the paper.

</details>

### [Continual Learning for Monolingual End-to-End Automatic Speech Recognition](2112.09427.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2021-12-17

<details>
<summary>Abstract</summary>

Adapting Automatic Speech Recognition (ASR) models to new domains results in a deterioration of performance on the original domain(s), a phenomenon called Catastrophic Forgetting (CF). Even monolingual ASR models cannot be extended to new accents, dialects, topics, etc. without suffering from CF, making them unable to be continually enhanced without storing all past data. Fortunately, Continual Learning (CL) methods, which aim to enable continual adaptation while overcoming CF, can be used. In this paper, we implement an extensive number of CL methods for End-to-End ASR and test and compare their ability to extend a monolingual Hybrid CTC-Transformer model across four new tasks. We find that the best performing CL method closes the gap between the fine-tuned model (lower bound) and the model trained jointly on all tasks (upper bound) by more than 40%, while requiring access to only 0.6% of the original data.

</details>

### [Automated Deep Learning: Neural Architecture Search Is Not the End](2112.09245.md)
**Xuanyi Dong, David Jacob Kedziora, Katarzyna Musial, Bogdan Gabrys** · 2021-12-16

<details>
<summary>Abstract</summary>

Deep learning (DL) has proven to be a highly effective approach for developing models in diverse contexts, including visual perception, speech recognition, and machine translation. However, the end-to-end process for applying DL is not trivial. It requires grappling with problem formulation and context understanding, data engineering, model development, deployment, continuous monitoring and maintenance, and so on. Moreover, each of these steps typically relies heavily on humans, in terms of both knowledge and interactions, which impedes the further advancement and democratization of DL. Consequently, in response to these issues, a new field has emerged over the last few years: automated deep learning (AutoDL). This endeavor seeks to minimize the need for human involvement and is best known for its achievements in neural architecture search (NAS), a topic that has been the focus of several surveys. That stated, NAS is not the be-all and end-all of AutoDL. Accordingly, this review adopts an overarching perspective, examining research efforts into automation across the entirety of an archetypal DL workflow. In so doing, this work also proposes a comprehensive set of ten criteria by which to assess existing work in both individual publications and broader research areas. These criteria are: novelty, solution quality, efficiency, stability, interpretability, reproducibility, engineering quality, scalability, generalizability, and eco-friendliness. Thus, ultimately, this review provides an evaluative overview of AutoDL in the early 2020s, identifying where future opportunities for progress may exist.

</details>

### [Self-Supervised Learning for speech recognition with Intermediate layer supervision](2112.08778.md)
**Chengyi Wang, Yu Wu, Sanyuan Chen, Shujie Liu et al.** · 2021-12-16

<details>
<summary>Abstract</summary>

Recently, pioneer work finds that speech pre-trained models can solve full-stack speech processing tasks, because the model utilizes bottom layers to learn speaker-related information and top layers to encode content-related information. Since the network capacity is limited, we believe the speech recognition performance could be further improved if the model is dedicated to audio content information learning. To this end, we propose Intermediate Layer Supervision for Self-Supervised Learning (ILS-SSL), which forces the model to concentrate on content information as much as possible by adding an additional SSL loss on the intermediate layers. Experiments on LibriSpeech test-other set show that our method outperforms HuBERT significantly, which achieves a 23.5%/11.6% relative word error rate reduction in the w/o language model setting for base/large models. Detailed analysis shows the bottom layers of our model have a better correlation with phonetic units, which is consistent with our intuition and explains the success of our method for ASR.

</details>

### [Prompt Tuning GPT-2 language model for parameter-efficient domain adaptation of ASR systems](2112.08718.md)
**Saket Dingliwal, Ashish Shenoy, Sravan Bodapati, Ankur Gandhe et al.** · 2021-12-16

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have found their use in numerous industrial applications in very diverse domains creating a need to adapt to new domains with small memory and deployment overhead. In this work, we introduce domain-prompts, a methodology that involves training a small number of domain embedding parameters to prime a Transformer-based Language Model (LM) to a particular domain. Using this domain-adapted LM for rescoring ASR hypotheses can achieve 7-13% WER reduction for a new domain with just 1000 unlabeled textual domain-specific sentences. This improvement is comparable or even better than fully fine-tuned models even though just 0.02% of the parameters of the base LM are updated. Additionally, our method is deployment-friendly as the learnt domain embeddings are prefixed to the input to the model rather than changing the base model architecture. Therefore, our method is an ideal choice for on-the-fly adaptation of LMs used in ASR systems to progressively scale it to new domains.

</details>

### [On the Use of External Data for Spoken Named Entity Recognition](2112.07648.md)
**Ankita Pasad, Felix Wu, Suwon Shon, Karen Livescu et al.** · 2021-12-14

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) tasks involve mapping from speech audio signals to semantic labels. Given the complexity of such tasks, good performance might be expected to require large labeled datasets, which are difficult to collect for each new task and domain. However, recent advances in self-supervised speech representations have made it feasible to consider learning SLU models with limited labeled data. In this work we focus on low-resource spoken named entity recognition (NER) and address the question: Beyond self-supervised pre-training, how can we use external speech and/or text data that are not annotated for the task? We draw on a variety of approaches, including self-training, knowledge distillation, and transfer learning, and consider their applicability to both end-to-end models and pipeline (speech recognition followed by text NER model) approaches. We find that several of these approaches improve performance in resource-constrained settings beyond the benefits from pre-trained representations alone. Compared to prior work, we find improved F1 scores of up to 16%. While the best baseline model is a pipeline approach, the best performance when using external data is ultimately achieved by an end-to-end model. We provide detailed comparisons and analyses, showing for example that end-to-end models are able to focus on the more NER-specific words.

</details>

### [Robustifying automatic speech recognition by extracting slowly varying features](2112.07400.md)
**Matías Pizarro, Dorothea Kolossa, Asja Fischer** · 2021-12-14

<details>
<summary>Abstract</summary>

In the past few years, it has been shown that deep learning systems are highly vulnerable under attacks with adversarial examples. Neural-network-based automatic speech recognition (ASR) systems are no exception. Targeted and untargeted attacks can modify an audio input signal in such a way that humans still recognise the same words, while ASR systems are steered to predict a different transcription. In this paper, we propose a defense mechanism against targeted adversarial attacks consisting in removing fast-changing features from the audio signals, either by applying slow feature analysis, a low-pass filter, or both, before feeding the input to the ASR system. We perform an empirical analysis of hybrid ASR models trained on data pre-processed in such a way. While the resulting models perform quite well on benign data, they are significantly more robust against targeted adversarial attacks: Our final, proposed model shows a performance on clean data similar to the baseline model, while being more than four times more robust.

</details>

### [Improving Hybrid CTC/Attention End-to-end Speech Recognition with Pretrained Acoustic and Language Model](2112.07254.md)
**Keqi Deng, Songjun Cao, Yike Zhang, Long Ma** · 2021-12-14

<details>
<summary>Abstract</summary>

Recently, self-supervised pretraining has achieved impressive results in end-to-end (E2E) automatic speech recognition (ASR). However, the dominant sequence-to-sequence (S2S) E2E model is still hard to fully utilize the self-supervised pre-training methods because its decoder is conditioned on acoustic representation thus cannot be pretrained separately. In this paper, we propose a pretrained Transformer (Preformer) S2S ASR architecture based on hybrid CTC/attention E2E models to fully utilize the pretrained acoustic models (AMs) and language models (LMs). In our framework, the encoder is initialized with a pretrained AM (wav2vec2.0). The Preformer leverages CTC as an auxiliary task during training and inference. Furthermore, we design a one-cross decoder (OCD), which relaxes the dependence on acoustic representations so that it can be initialized with pretrained LM (DistilGPT2). Experiments are conducted on the AISHELL-1 corpus and achieve a $4.6\%$ character error rate (CER) on the test set. Compared with our vanilla hybrid CTC/attention Transformer baseline, our proposed CTC/attention-based Preformer yields $27\%$ relative CER reduction. To the best of our knowledge, this is the first work to utilize both pretrained AM and LM in a S2S ASR system.

</details>

### [Real-Time Neural Voice Camouflage](2112.07076.md)
**Mia Chiquier, Chengzhi Mao, Carl Vondrick** · 2021-12-14

<details>
<summary>Abstract</summary>

Automatic speech recognition systems have created exciting possibilities for applications, however they also enable opportunities for systematic eavesdropping. We propose a method to camouflage a person's voice over-the-air from these systems without inconveniencing the conversation between people in the room. Standard adversarial attacks are not effective in real-time streaming situations because the characteristics of the signal will have changed by the time the attack is executed. We introduce predictive attacks, which achieve real-time performance by forecasting the attack that will be the most effective in the future. Under real-time constraints, our method jams the established speech recognition system DeepSpeech 3.9x more than baselines as measured through word error rate, and 6.6x more as measured through character error rate. We furthermore demonstrate our approach is practically effective in realistic environments over physical distances.

</details>

### [PM-MMUT: Boosted Phone-Mask Data Augmentation using Multi-Modeling Unit Training for Phonetic-Reduction-Robust E2E Speech Recognition](2112.06721.md)
**Guodong Ma, Pengfei Hu, Nurmemet Yolwas, Shen Huang et al.** · 2021-12-13

<details>
<summary>Abstract</summary>

Consonant and vowel reduction are often encountered in speech, which might cause performance degradation in automatic speech recognition (ASR). Our recently proposed learning strategy based on masking, Phone Masking Training (PMT), alleviates the impact of such phenomenon in Uyghur ASR. Although PMT achieves remarkably improvements, there still exists room for further gains due to the granularity mismatch between the masking unit of PMT (phoneme) and the modeling unit (word-piece). To boost the performance of PMT, we propose multi-modeling unit training (MMUT) architecture fusion with PMT (PM-MMUT). The idea of MMUT framework is to split the Encoder into two parts including acoustic feature sequences to phoneme-level representation (AF-to-PLR) and phoneme-level representation to word-piece-level representation (PLR-to-WPLR). It allows AF-to-PLR to be optimized by an intermediate phoneme-based CTC loss to learn the rich phoneme-level context information brought by PMT. Experimental results on Uyghur ASR show that the proposed approaches outperform obviously the pure PMT. We also conduct experiments on the 960-hour Librispeech benchmark using ESPnet1, which achieves about 10% relative WER reduction on all the test set without LM fusion comparing with the latest official ESPnet1 pre-trained model.

</details>

### [Detecting Audio Adversarial Examples with Logit Noising](2112.06443.md)
**Namgyu Park, Sangwoo Ji, Jong Kim** · 2021-12-13

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems are vulnerable to audio adversarial examples that attempt to deceive ASR systems by adding perturbations to benign speech signals. Although an adversarial example and the original benign wave are indistinguishable to humans, the former is transcribed as a malicious target sentence by ASR systems. Several methods have been proposed to generate audio adversarial examples and feed them directly into the ASR system (over-line). Furthermore, many researchers have demonstrated the feasibility of robust physical audio adversarial examples(over-air). To defend against the attacks, several studies have been proposed. However, deploying them in a real-world situation is difficult because of accuracy drop or time overhead. In this paper, we propose a novel method to detect audio adversarial examples by adding noise to the logits before feeding them into the decoder of the ASR. We show that carefully selected noise can significantly impact the transcription results of the audio adversarial examples, whereas it has minimal impact on the transcription results of benign audio waves. Based on this characteristic, we detect audio adversarial examples by comparing the transcription altered by logit noising with its original transcription. The proposed method can be easily applied to ASR systems without any structural changes or additional training. The experimental results show that the proposed method is robust to over-line audio adversarial examples as well as over-air audio adversarial examples compared with state-of-the-art detection methods.

</details>

### [Learning How Long to Wait: Adaptively-Constrained Monotonic Multihead Attention for Streaming ASR](s2:581280ae8d65eb65e75afbae7af05debce28e844.md)
**Jae-gyun Song, Hajin Shim, Eunho Yang** · 2021-12-13

<details>
<summary>Abstract</summary>

Monotonic Multihead Attention, which allows multiple heads to learn their own alignments per head, shows great performance on simultaneous machine translation and streaming speech recognition. However, it causes high latency waiting for the slowest head. Some recent advances such as Head-Synchronous Beam Search Decoding and its learnable version Mutually-Constrained Monotonic Multihead Attention, try to address this issue by restricting the difference in times of chosen frames among multi-heads to a fixed waiting time threshold. In this paper, we hypothesis that the optimal threshold for high performance with low latency depends on the input sequence, and propose an adaptive algorithm that learns how long to wait depending on input tokens by introducing a threshold prediction module. We evaluate our approach on two benchmark datasets for online Automatic Speech Recognition task and demonstrate that our method reduces the latency together with even improving the recognition accuracy.

</details>

### [Comparative Study of Different Tokenization Strategies for Streaming End-to-End ASR](s2:5e421487a60cbdd93156da354bb1d8f455db683f.md)
**Sachin Singh, Ashutosh Gupta, Aman Maghan, Dhananjaya N. Gowda et al.** · 2021-12-13

<details>
<summary>Abstract</summary>

Most End-to-End Automatic Speech Recognition (ASR) models use character-based vocabularies: characters, sub-words (BPE), or words. While these work well for training a monolingual model, there are certain limitations when ap-plying these to a multilingual model. Rare characters from character-rich languages like Korean can easily result in large vocabulary size, limiting the model's compactness. Repre-senting text at the level of bytes has also been proposed. However, a byte sequence representation of text is often much longer, which increases the decoding time and makes it computationally expensive for on-device use. Byte-based sub-words (BBPE) are proposed in neural machine translation for word representation but are still unexplored in the ASR domain. In this work, we conduct an empirical study comparing the above three tokenization strategies across three metrics: Word Error Rate (WER), model size, and the decoding time, which are critical for an on-device ASR. We did extensive experiments for both monolingual and bilingual, with languages belonging to same (English and Spanish) and different (English and Korean) language families. Our exper-iments show that BBPE and BPE models yield a similar WER for English and Spanish. While for a character-rich language like Korean, we get 26% and 14% relative WER improvement with BBPE monolingual and bilingual models, respectively. In contrast, the byte models trade-off small model size and a fixed vocabulary at the cost of high xRT. Among all three, we found the BBPE strategy to be the most flexible and optimal for most cases.

</details>

### [Improving HS-DACS Based Streaming Transformer ASR with Deep Reinforcement Learning](s2:8c0b6708cffd7a26bcdc7544b1a6084a976447c6.md)
**Mohan Li, R. Doddipatla** · 2021-12-13

<details>
<summary>Abstract</summary>

Transformer-based systems, though have achieved state-of-the-art performance on a wide range of automatic speech recognition (ASR) tasks, are subject to severe latency issues during inference that limit their deployment in real world applications. To enable online decoding, we recently proposed Decoder-end adaptive computation steps (DACS) and the head-synchronous version (HS-DACS) algorithms, which were shown to reduce the computational cost for decoding and close the gap in performance between offline and streaming Transformer ASR. In DACS/HS-DACS based systems, the halting position that triggers the ASR output was determined with an accumulation threshold that was set arbitrarily. In this paper, we propose a deep reinforcement learning approach to improve HS-DACS where an external agent is utilised to optimise the halting position. Experiments on AIShell-1, Tedlium-2 and Librispeech datasets show that the proposed method can further cut down the computation cost in inference with relative gains of 40.0%, 32.8% and 53.4% respectively, and still maintain similar ASR performance when compared with HS-DACS.

</details>

### [Improving Code-switching Language Modeling with Artificially Generated Texts using Cycle-consistent Adversarial Networks](2112.06327.md)
**Chia-Yu Li, Ngoc Thang Vu** · 2021-12-12

<details>
<summary>Abstract</summary>

This paper presents our latest effort on improving Code-switching language models that suffer from data scarcity. We investigate methods to augment Code-switching training text data by artificially generating them. Concretely, we propose a cycle-consistent adversarial networks based framework to transfer monolingual text into Code-switching text, considering Code-switching as a speaking style. Our experimental results on the SEAME corpus show that utilising artificially generated Code-switching text data improves consistently the language model as well as the automatic speech recognition performance.

</details>

### [Revisiting the Boundary between ASR and NLU in the Age of Conversational Dialog Systems](2112.05842.md)
**Manaal Faruqui, Dilek Hakkani-Tür** · 2021-12-10

<details>
<summary>Abstract</summary>

As more users across the world are interacting with dialog agents in their daily life, there is a need for better speech understanding that calls for renewed attention to the dynamics between research in automatic speech recognition (ASR) and natural language understanding (NLU). We briefly review these research areas and lay out the current relationship between them. In light of the observations we make in this paper, we argue that (1) NLU should be cognizant of the presence of ASR models being used upstream in a dialog system's pipeline, (2) ASR should be able to learn from errors found in NLU, (3) there is a need for end-to-end datasets that provide semantic annotations on spoken input, (4) there should be stronger collaboration between ASR and NLU research communities.

</details>

### [Sequence-level self-learning with multiple hypotheses](2112.05826.md)
**Kenichi Kumatani, Dimitrios Dimitriadis, Yashesh Gaur, Robert Gmyr et al.** · 2021-12-10

<details>
<summary>Abstract</summary>

In this work, we develop new self-learning techniques with an attention-based sequence-to-sequence (seq2seq) model for automatic speech recognition (ASR). For untranscribed speech data, the hypothesis from an ASR system must be used as a label. However, the imperfect ASR result makes unsupervised learning difficult to consistently improve recognition performance especially in the case that multiple powerful teacher models are unavailable. In contrast to conventional unsupervised learning approaches, we adopt the \emph{multi-task learning} (MTL) framework where the $n$-th best ASR hypothesis is used as the label of each task. The seq2seq network is updated through the MTL framework so as to find the common representation that can cover multiple hypotheses. By doing so, the effect of the \emph{hard-decision} errors can be alleviated. We first demonstrate the effectiveness of our self-learning methods through ASR experiments in an accent adaptation task between the US and British English speech. Our experiment results show that our method can reduce the WER on the British speech data from 14.55\% to 10.36\% compared to the baseline model trained with the US English data only. Moreover, we investigate the effect of our proposed methods in a federated learning scenario.

</details>

### [Building a great multi-lingual teacher with sparsely-gated mixture of experts for speech recognition](2112.05820.md)
**Kenichi Kumatani, Robert Gmyr, Felipe Cruz Salinas, Linquan Liu et al.** · 2021-12-10

<details>
<summary>Abstract</summary>

The sparsely-gated Mixture of Experts (MoE) can magnify a network capacity with a little computational complexity. In this work, we investigate how multi-lingual Automatic Speech Recognition (ASR) networks can be scaled up with a simple routing algorithm in order to achieve better accuracy. More specifically, we apply the sparsely-gated MoE technique to two types of networks: Sequence-to-Sequence Transformer (S2S-T) and Transformer Transducer (T-T). We demonstrate through a set of ASR experiments on multiple language data that the MoE networks can reduce the relative word error rates by 16.3% and 4.6% with the S2S-T and T-T, respectively. Moreover, we thoroughly investigate the effect of the MoE on the T-T architecture in various conditions: streaming mode, non-streaming mode, the use of language ID and the label decoder with the MoE.

</details>

### [Are E2E ASR models ready for an industrial usage?](2112.12572.md)
**Valentin Vielzeuf, Grigory Antipov** · 2021-12-09

<details>
<summary>Abstract</summary>

The Automated Speech Recognition (ASR) community experiences a major turning point with the rise of the fully-neural (End-to-End, E2E) approaches. At the same time, the conventional hybrid model remains the standard choice for the practical usage of ASR. According to previous studies, the adoption of E2E ASR in real-world applications was hindered by two main limitations: their ability to generalize on unseen domains and their high operational cost. In this paper, we investigate both above-mentioned drawbacks by performing a comprehensive multi-domain benchmark of several contemporary E2E models and a hybrid baseline. Our experiments demonstrate that E2E models are viable alternatives for the hybrid approach, and even outperform the baseline both in accuracy and in operational efficiency. As a result, our study shows that the generalization and complexity issues are no longer the major obstacle for industrial integration, and draws the community's attention to other potential limitations of the E2E approaches in some specific use-cases.

</details>

### [LipSound2: Self-Supervised Pre-Training for Lip-to-Speech Reconstruction and Lip Reading](2112.04748.md)
**Leyuan Qu, Cornelius Weber, Stefan Wermter** · 2021-12-09

<details>
<summary>Abstract</summary>

The aim of this work is to investigate the impact of crossmodal self-supervised pre-training for speech reconstruction (video-to-audio) by leveraging the natural co-occurrence of audio and visual streams in videos. We propose LipSound2 which consists of an encoder-decoder architecture and location-aware attention mechanism to map face image sequences to mel-scale spectrograms directly without requiring any human annotations. The proposed LipSound2 model is firstly pre-trained on $\sim$2400h multi-lingual (e.g. English and German) audio-visual data (VoxCeleb2). To verify the generalizability of the proposed method, we then fine-tune the pre-trained model on domain-specific datasets (GRID, TCD-TIMIT) for English speech reconstruction and achieve a significant improvement on speech quality and intelligibility compared to previous approaches in speaker-dependent and -independent settings. In addition to English, we conduct Chinese speech reconstruction on the CMLR dataset to verify the impact on transferability. Lastly, we train the cascaded lip reading (video-to-text) system by fine-tuning the generated audios on a pre-trained speech recognition system and achieve state-of-the-art performance on both English and Chinese benchmark datasets.

</details>

### [A study on native American English speech recognition by Indian listeners with varying word familiarity level](2112.04151.md)
**Abhayjeet Singh, Achuth Rao MV, Rakesh Vaideeswaran, Chiranjeevi Yarra et al.** · 2021-12-08

<details>
<summary>Abstract</summary>

In this study, listeners of varied Indian nativities are asked to listen and recognize TIMIT utterances spoken by American speakers. We have three kinds of responses from each listener while they recognize an utterance: 1. Sentence difficulty ratings, 2. Speaker difficulty ratings, and 3. Transcription of the utterance. From these transcriptions, word error rate (WER) is calculated and used as a metric to evaluate the similarity between the recognized and the original sentences.The sentences selected in this study are categorized into three groups: Easy, Medium and Hard, based on the frequency ofoccurrence of the words in them. We observe that the sentence, speaker difficulty ratings and the WERs increase from easy to hard categories of sentences. We also compare the human speech recognition performance with that using three automatic speech recognition (ASR) under following three combinations of acoustic model (AM) and language model(LM): ASR1) AM trained with recordings from speakers of Indian origin and LM built on TIMIT text, ASR2) AM using recordings from native American speakers and LM built ontext from LIBRI speech corpus, and ASR3) AM using recordings from native American speakers and LM build on LIBRI speech and TIMIT text. We observe that HSR performance is similar to that of ASR1 whereas ASR3 achieves the best performance. Speaker nativity wise analysis shows that utterances from speakers of some nativity are more difficult to recognize by Indian listeners compared to few other nativities

</details>

### [Training end-to-end speech-to-text models on mobile phones](2112.03871.md)
**Zitha S, Raghavendra Rao Suresh, Pooja Rao, T. V. Prabhakar** · 2021-12-07

<details>
<summary>Abstract</summary>

Training the state-of-the-art speech-to-text (STT) models in mobile devices is challenging due to its limited resources relative to a server environment. In addition, these models are trained on generic datasets that are not exhaustive in capturing user-specific characteristics. Recently, on-device personalization techniques have been making strides in mitigating the problem. Although many current works have already explored the effectiveness of on-device personalization, the majority of their findings are limited to simulation settings or a specific smartphone. In this paper, we develop and provide a detailed explanation of our framework to train end-to-end models in mobile phones. To make it simple, we considered a model based on connectionist temporal classification (CTC) loss. We evaluated the framework on various mobile phones from different brands and reported the results. We provide enough evidence that fine-tuning the models and choosing the right hyperparameter values is a trade-off between the lowest WER achievable, training time on-device, and memory consumption. Hence, this is vital for a successful deployment of on-device training onto a resource-limited environment like mobile phones. We use training sets from speakers with different accents and record a 7.6% decrease in average word error rate (WER). We also report the associated computational cost measurements with respect to time, memory usage, and cpu utilization in mobile phones in real-time.

</details>

### [Consistent Training and Decoding For End-to-end Speech Recognition Using Lattice-free MMI](2112.02498.md)
**Jinchuan Tian, Jianwei Yu, Chao Weng, Shi-Xiong Zhang et al.** · 2021-12-05

<details>
<summary>Abstract</summary>

Recently, End-to-End (E2E) frameworks have achieved remarkable results on various Automatic Speech Recognition (ASR) tasks. However, Lattice-Free Maximum Mutual Information (LF-MMI), as one of the discriminative training criteria that show superior performance in hybrid ASR systems, is rarely adopted in E2E ASR frameworks. In this work, we propose a novel approach to integrate LF-MMI criterion into E2E ASR frameworks in both training and decoding stages. The proposed approach shows its effectiveness on two of the most widely used E2E frameworks including Attention-Based Encoder-Decoders (AEDs) and Neural Transducers (NTs). Experiments suggest that the introduction of the LF-MMI criterion consistently leads to significant performance improvements on various datasets and different E2E ASR frameworks. The best of our models achieves competitive CER of 4.1\% / 4.4\% on Aishell-1 dev/test set; we also achieve significant error reduction on Aishell-2 and Librispeech datasets over strong baselines.

</details>

### [Catch Me If You Can: Blackbox Adversarial Attacks on Automatic Speech Recognition using Frequency Masking](2112.01821.md)
**Xiaoliang Wu, Ajitha Rajan** · 2021-12-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) models are prevalent, particularly in applications for voice navigation and voice control of domestic appliances. The computational core of ASRs are deep neural networks (DNNs) that have been shown to be susceptible to adversarial perturbations; easily misused by attackers to generate malicious outputs. To help test the security and robustnesss of ASRS, we propose techniques that generate blackbox (agnostic to the DNN), untargeted adversarial attacks that are portable across ASRs. This is in contrast to existing work that focuses on whitebox targeted attacks that are time consuming and lack portability. Our techniques generate adversarial attacks that have no human audible difference by manipulating the audio signal using a psychoacoustic model that maintains the audio perturbations below the thresholds of human perception. We evaluate portability and effectiveness of our techniques using three popular ASRs and two input audio datasets using the metrics - Word Error Rate (WER) of output transcription, Similarity to original audio, attack Success Rate on different ASRs and Detection score by a defense system. We found our adversarial attacks were portable across ASRs, not easily detected by a state-of-the-art defense system, and had significant difference in output transcriptions while sounding similar to original audio.

</details>

### [BBS-KWS:The Mandarin Keyword Spotting System Won the Video Keyword Wakeup Challenge](2112.01757.md)
**Yuting Yang, Binbin Du, Yingxin Zhang, Wenxuan Wang et al.** · 2021-12-03

<details>
<summary>Abstract</summary>

This paper introduces the system submitted by the Yidun NISP team to the video keyword wakeup challenge. We propose a mandarin keyword spotting system (KWS) with several novel and effective improvements, including a big backbone (B) model, a keyword biasing (B) mechanism and the introduction of syllable modeling units (S). By considering this, we term the total system BBS-KWS as an abbreviation. The BBS-KWS system consists of an end-to-end automatic speech recognition (ASR) module and a KWS module. The ASR module converts speech features to text representations, which applies a big backbone network to the acoustic model and takes syllable modeling units into consideration as well. In addition, the keyword biasing mechanism is used to improve the recall rate of keywords in the ASR inference stage. The KWS module applies multiple criteria to determine the absence or presence of the keywords, such as multi-stage matching, fuzzy matching, and connectionist temporal classification (CTC) prefix score. To further improve our system, we conduct semi-supervised learning on the CN-Celeb dataset for better generalization. In the VKW task, the BBS-KWS system achieves significant gains over the baseline and won the first place in two tracks.

</details>

### [Loss Landscape Dependent Self-Adjusting Learning Rates in Decentralized Stochastic Gradient Descent](2112.01433.md)
**Wei Zhang, Mingrui Liu, Yu Feng, Xiaodong Cui et al.** · 2021-12-02

<details>
<summary>Abstract</summary>

Distributed Deep Learning (DDL) is essential for large-scale Deep Learning (DL) training. Synchronous Stochastic Gradient Descent (SSGD) 1 is the de facto DDL optimization method. Using a sufficiently large batch size is critical to achieving DDL runtime speedup. In a large batch setting, the learning rate must be increased to compensate for the reduced number of parameter updates. However, a large learning rate may harm convergence in SSGD and training could easily diverge. Recently, Decentralized Parallel SGD (DPSGD) has been proposed to improve distributed training speed. In this paper, we find that DPSGD not only has a system-wise run-time benefit but also a significant convergence benefit over SSGD in the large batch setting. Based on a detailed analysis of the DPSGD learning dynamics, we find that DPSGD introduces additional landscape-dependent noise that automatically adjusts the effective learning rate to improve convergence. In addition, we theoretically show that this noise smoothes the loss landscape, hence allowing a larger learning rate. We conduct extensive studies over 18 state-of-the-art DL models/tasks and demonstrate that DPSGD often converges in cases where SSGD diverges for large learning rates in the large batch setting. Our findings are consistent across two different application domains: Computer Vision (CIFAR10 and ImageNet-1K) and Automatic Speech Recognition (SWB300 and SWB2000), and two different types of neural network models: Convolutional Neural Networks and Long Short-Term Memory Recurrent Neural Networks.

</details>

### [A Mixture of Expert Based Deep Neural Network for Improved ASR](2112.01025.md)
**Vishwanath Pratap Singh, Shakti P. Rath, Abhishek Pandey** · 2021-12-02

<details>
<summary>Abstract</summary>

This paper presents a novel deep learning architecture for acoustic model in the context of Automatic Speech Recognition (ASR), termed as MixNet. Besides the conventional layers, such as fully connected layers in DNN-HMM and memory cells in LSTM-HMM, the model uses two additional layers based on Mixture of Experts (MoE). The first MoE layer operating at the input is based on pre-defined broad phonetic classes and the second layer operating at the penultimate layer is based on automatically learned acoustic classes. In natural speech, overlap in distribution across different acoustic classes is inevitable, which leads to inter-class mis-classification. The ASR accuracy is expected to improve if the conventional architecture of acoustic model is modified to make them more suitable to account for such overlaps. MixNet is developed keeping this in mind. Analysis conducted by means of scatter diagram verifies that MoE indeed improves the separation between classes that translates to better ASR accuracy. Experiments are conducted on a large vocabulary ASR task which show that the proposed architecture provides 13.6% and 10.0% relative reduction in word error rates compared to the conventional models, namely, DNN and LSTM respectively, trained using sMBR criteria. In comparison to an existing method developed for phone-classification (by Eigen et al), our proposed method yields a significant improvement.

</details>

### [A higher order Minkowski loss for improved prediction ability of acoustic model in ASR](2112.01023.md)
**Vishwanath Pratap Singh, Shakti P. Rath, Abhishek Pandey** · 2021-12-02

<details>
<summary>Abstract</summary>

Conventional automatic speech recognition (ASR) system uses second-order minkowski loss during inference time which is suboptimal as it incorporates only first order statistics in posterior estimation [2]. In this paper we have proposed higher order minkowski loss (4th Order and 6th Order) during inference time, without any changes during training time. The main contribution of the paper is to show that higher order loss uses higher order statistics in posterior estimation, which improves the prediction ability of acoustic model in ASR system. We have shown mathematically that posterior probability obtained due to higher order loss is function of second order posterior and thus the method can be incorporated in standard ASR system in an easy manner. It is to be noted that all changes are proposed during test(inference) time, we do not make any change in any training pipeline. Multiple baseline systems namely, TDNN1, TDNN2, DNN and LSTM are developed to verify the improvement incurred due to higher order minkowski loss. All experiments are conducted on LibriSpeech dataset and performance metrics are word error rate (WER) on "dev-clean", "test-clean", "dev-other" and "test-other" datasets.

</details>

### [Deliberation of Streaming RNN-Transducer by Non-autoregressive Decoding](2112.11442.md)
**Weiran Wang, Ke Hu, Tara Sainath** · 2021-12-01

<details>
<summary>Abstract</summary>

We propose to deliberate the hypothesis alignment of a streaming RNN-T model with the previously proposed Align-Refine non-autoregressive decoding method and its improved versions. The method performs a few refinement steps, where each step shares a transformer decoder that attends to both text features (extracted from alignments) and audio features, and outputs complete updated alignments. The transformer decoder is trained with the CTC loss which facilitates parallel greedy decoding, and performs full-context attention to capture label dependencies. We improve Align-Refine by introducing cascaded encoder that captures more audio context before refinement, and alignment augmentation which enforces learning label dependency. We show that, conditioned on hypothesis alignments of a streaming RNN-T model, our method obtains significantly more accurate recognition results than the first-pass RNN-T, with only small amount of model parameters.

</details>

### [An investigation of neural uncertainty estimation for target speaker extraction equipped RNN transducer](s2:d66110a315f5f216b42d99cfafec31e8e30a03ea.md)
**Jiatong Shi, Chunlei Zhang, Chao Weng, Shinji Watanabe et al.** · 2021-12-01

### [Joint Modeling of Code-Switched and Monolingual ASR via Conditional Factorization](2111.15016.md)
**Brian Yan, Chunlei Zhang, Meng Yu, Shi-Xiong Zhang et al.** · 2021-11-29

<details>
<summary>Abstract</summary>

Conversational bilingual speech encompasses three types of utterances: two purely monolingual types and one intra-sententially code-switched type. In this work, we propose a general framework to jointly model the likelihoods of the monolingual and code-switch sub-tasks that comprise bilingual speech recognition. By defining the monolingual sub-tasks with label-to-frame synchronization, our joint modeling framework can be conditionally factorized such that the final bilingual output, which may or may not be code-switched, is obtained given only monolingual information. We show that this conditionally factorized joint framework can be modeled by an end-to-end differentiable neural network. We demonstrate the efficacy of our proposed model on bilingual Mandarin-English speech recognition across both monolingual and code-switched corpora.

</details>

### [Do We Still Need Automatic Speech Recognition for Spoken Language Understanding?](2111.14842.md)
**Lasse Borgholt, Jakob Drachmann Havtorn, Mostafa Abdou, Joakim Edin et al.** · 2021-11-29

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) tasks are usually solved by first transcribing an utterance with automatic speech recognition (ASR) and then feeding the output to a text-based model. Recent advances in self-supervised representation learning for speech data have focused on improving the ASR component. We investigate whether representation learning for speech has matured enough to replace ASR in SLU. We compare learned speech features from wav2vec 2.0, state-of-the-art ASR transcripts, and the ground truth text as input for a novel speech-based named entity recognition task, a cardiac arrest detection task on real-world emergency calls and two existing SLU benchmarks. We show that learned speech features are superior to ASR transcripts on three classification tasks. For machine translation, ASR transcripts are still the better choice. We highlight the intrinsic robustness of wav2vec 2.0 representations to out-of-vocabulary words as key to better performance.

</details>

### [Mixed Precision Low-bit Quantization of Neural Network Language Models for Speech Recognition](2112.11438.md)
**Junhao Xu, Jianwei Yu, Shoukang Hu, Xunying Liu et al.** · 2021-11-29

<details>
<summary>Abstract</summary>

State-of-the-art language models (LMs) represented by long-short term memory recurrent neural networks (LSTM-RNNs) and Transformers are becoming increasingly complex and expensive for practical applications. Low-bit neural network quantization provides a powerful solution to dramatically reduce their model size. Current quantization methods are based on uniform precision and fail to account for the varying performance sensitivity at different parts of LMs to quantization errors. To this end, novel mixed precision neural network LM quantization methods are proposed in this paper. The optimal local precision choices for LSTM-RNN and Transformer based neural LMs are automatically learned using three techniques. The first two approaches are based on quantization sensitivity metrics in the form of either the KL-divergence measured between full precision and quantized LMs, or Hessian trace weighted quantization perturbation that can be approximated efficiently using matrix free techniques. The third approach is based on mixed precision neural architecture search. In order to overcome the difficulty in using gradient descent methods to directly estimate discrete quantized weights, alternating direction methods of multipliers (ADMM) are used to efficiently train quantized LMs. Experiments were conducted on state-of-the-art LF-MMI CNN-TDNN systems featuring speed perturbation, i-Vector and learning hidden unit contribution (LHUC) based speaker adaptation on two tasks: Switchboard telephone speech and AMI meeting transcription. The proposed mixed precision quantization techniques achieved "lossless" quantization on both tasks, by producing model size compression ratios of up to approximately 16 times over the full precision LSTM and Transformer baseline LMs, while incurring no statistically significant word error rate increase.

</details>

### [Mixed Precision of Quantization of Transformer Language Models for Speech Recognition](2112.11540.md)
**Junhao Xu, Shoukang Hu, Jianwei Yu, Xunying Liu et al.** · 2021-11-29

<details>
<summary>Abstract</summary>

State-of-the-art neural language models represented by Transformers are becoming increasingly complex and expensive for practical applications. Low-bit deep neural network quantization techniques provides a powerful solution to dramatically reduce their model size. Current low-bit quantization methods are based on uniform precision and fail to account for the varying performance sensitivity at different parts of the system to quantization errors. To this end, novel mixed precision DNN quantization methods are proposed in this paper. The optimal local precision settings are automatically learned using two techniques. The first is based on a quantization sensitivity metric in the form of Hessian trace weighted quantization perturbation. The second is based on mixed precision Transformer architecture search. Alternating direction methods of multipliers (ADMM) are used to efficiently train mixed precision quantized DNN systems. Experiments conducted on Penn Treebank (PTB) and a Switchboard corpus trained LF-MMI TDNN system suggest the proposed mixed precision Transformer quantization techniques achieved model size compression ratios of up to 16 times over the full precision baseline with no recognition performance degradation. When being used to compress a larger full precision Transformer LM with more layers, overall word error rate (WER) reductions up to 1.7% absolute (18% relative) were obtained.

</details>

### [Mixed Precision DNN Qunatization for Overlapped Speech Separation and Recognition](2111.14479.md)
**Junhao Xu, Jianwei Yu, Xunying Liu, Helen Meng** · 2021-11-29

<details>
<summary>Abstract</summary>

Recognition of overlapped speech has been a highly challenging task to date. State-of-the-art multi-channel speech separation system are becoming increasingly complex and expensive for practical applications. To this end, low-bit neural network quantization provides a powerful solution to dramatically reduce their model size. However, current quantization methods are based on uniform precision and fail to account for the varying performance sensitivity at different model components to quantization errors. In this paper, novel mixed precision DNN quantization methods are proposed by applying locally variable bit-widths to individual TCN components of a TF masking based multi-channel speech separation system. The optimal local precision settings are automatically learned using three techniques. The first two approaches utilize quantization sensitivity metrics based on either the mean square error (MSE) loss function curvature, or the KL-divergence measured between full precision and quantized separation models. The third approach is based on mixed precision neural architecture search. Experiments conducted on the LRS3-TED corpus simulated overlapped speech data suggest that the proposed mixed precision quantization techniques consistently outperform the uniform precision baseline speech separation systems of comparable bit-widths in terms of SI-SNR and PESQ scores as well as word error rate (WER) reductions up to 2.88% absolute (8% relative).

</details>

### [Romanian Speech Recognition Experiments from the ROBIN Project](2111.12028.md)
**Andrei-Marius Avram, Vasile Păiş, Dan Tufiş** · 2021-11-23

<details>
<summary>Abstract</summary>

One of the fundamental functionalities for accepting a socially assistive robot is its communication capabilities with other agents in the environment. In the context of the ROBIN project, situational dialogue through voice interaction with a robot was investigated. This paper presents different speech recognition experiments with deep neural networks focusing on producing fast (under 100ms latency from the network itself), while still reliable models. Even though one of the key desired characteristics is low latency, the final deep neural network model achieves state of the art results for recognizing Romanian language, obtaining a 9.91% word error rate (WER), when combined with a language model, thus improving over the previous results while offering at the same time an improved runtime performance. Additionally, we explore two modules for correcting the ASR output (hyphen and capitalization restoration and unknown words correction), targeting the ROBIN project's goals (dialogue in closed micro-worlds). We design a modular architecture based on APIs allowing an integration engine (either in the robot or external) to chain together the available modules as needed. Finally, we test the proposed design by integrating it in the RELATE platform and making the ASR service available to web users by either uploading a file or recording new speech.

</details>

### [Guided-TTS: A Diffusion Model for Text-to-Speech via Classifier Guidance](2111.11755.md)
**Heeseung Kim, Sungwon Kim, Sungroh Yoon** · 2021-11-23

<details>
<summary>Abstract</summary>

We propose Guided-TTS, a high-quality text-to-speech (TTS) model that does not require any transcript of target speaker using classifier guidance. Guided-TTS combines an unconditional diffusion probabilistic model with a separately trained phoneme classifier for classifier guidance. Our unconditional diffusion model learns to generate speech without any context from untranscribed speech data. For TTS synthesis, we guide the generative process of the diffusion model with a phoneme classifier trained on a large-scale speech recognition dataset. We present a norm-based scaling method that reduces the pronunciation errors of classifier guidance in Guided-TTS. We show that Guided-TTS achieves a performance comparable to that of the state-of-the-art TTS model, Grad-TTS, without any transcript for LJSpeech. We further demonstrate that Guided-TTS performs well on diverse datasets including a long-form untranscribed dataset.

</details>

### [Effect of noise suppression losses on speech distortion and ASR performance](2111.11606.md)
**Sebastian Braun, Hannes Gamper** · 2021-11-23

<details>
<summary>Abstract</summary>

Deep learning based speech enhancement has made rapid development towards improving quality, while models are becoming more compact and usable for real-time on-the-edge inference. However, the speech quality scales directly with the model size, and small models are often still unable to achieve sufficient quality. Furthermore, the introduced speech distortion and artifacts greatly harm speech quality and intelligibility, and often significantly degrade automatic speech recognition (ASR) rates. In this work, we shed light on the success of the spectral complex compressed mean squared error (MSE) loss, and how its magnitude and phase-aware terms are related to the speech distortion vs. noise reduction trade off. We further investigate integrating pre-trained reference-less predictors for mean opinion score (MOS) and word error rate (WER), and pre-trained embeddings on ASR and sound event detection. Our analyses reveal that none of the pre-trained networks added significant performance over the strong spectral loss.

</details>

### [Multi-Channel Multi-Speaker ASR Using 3D Spatial Feature](2111.11023.md)
**Yiwen Shao, Shi-Xiong Zhang, Dong Yu** · 2021-11-22

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) of multi-channel multi-speaker overlapped speech remains one of the most challenging tasks to the speech community. In this paper, we look into this challenge by utilizing the location information of target speakers in the 3D space for the first time. To explore the strength of proposed the 3D spatial feature, two paradigms are investigated. 1) a pipelined system with a multi-channel speech separation module followed by the state-of-the-art single-channel ASR module; 2) a "All-In-One" model where the 3D spatial feature is directly used as an input to ASR system without explicit separation modules. Both of them are fully differentiable and can be back-propagated end-to-end. We test them on simulated overlapped speech and real recordings. Experimental results show that 1) the proposed ALL-In-One model achieved a comparable error rate to the pipelined system while reducing the inference time by half; 2) the proposed 3D spatial feature significantly outperformed (31\% CERR) all previous works of using the 1D directional information in both paradigms.

</details>

### [Deep Spoken Keyword Spotting: An Overview](2111.10592.md)
**Iván López-Espejo, Zheng-Hua Tan, John Hansen, Jesper Jensen** · 2021-11-20

<details>
<summary>Abstract</summary>

Spoken keyword spotting (KWS) deals with the identification of keywords in audio streams and has become a fast-growing technology thanks to the paradigm shift introduced by deep learning a few years ago. This has allowed the rapid embedding of deep KWS in a myriad of small electronic devices with different purposes like the activation of voice assistants. Prospects suggest a sustained growth in terms of social use of this technology. Thus, it is not surprising that deep KWS has become a hot research topic among speech scientists, who constantly look for KWS performance improvement and computational complexity reduction. This context motivates this paper, in which we conduct a literature review into deep spoken KWS to assist practitioners and researchers who are interested in this technology. Specifically, this overview has a comprehensive nature by covering a thorough analysis of deep KWS systems (which includes speech features, acoustic modeling and posterior handling), robustness methods, applications, datasets, evaluation metrics, performance of deep KWS systems and audio-visual KWS. The analysis performed in this paper allows us to identify a number of directions for future research, including directions adopted from automatic speech recognition research and directions that are unique to the problem of spoken KWS.

</details>

### [Lattention: Lattice-attention in ASR rescoring](2111.10157.md)
**Prabhat Pandey, Sergio Duarte Torres, Ali Orkan Bayer, Ankur Gandhe et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

Lattices form a compact representation of multiple hypotheses generated from an automatic speech recognition system and have been shown to improve performance of downstream tasks like spoken language understanding and speech translation, compared to using one-best hypothesis. In this work, we look into the effectiveness of lattice cues for rescoring n-best lists in second-pass. We encode lattices with a recurrent network and train an attention encoder-decoder model for n-best rescoring. The rescoring model with attention to lattices achieves 4-5% relative word error rate reduction over first-pass and 6-8% with attention to both lattices and acoustic features. We show that rescoring models with attention to lattices outperform models with attention to n-best hypotheses. We also study different ways to incorporate lattice weights in the lattice encoder and demonstrate their importance for n-best rescoring.

</details>

### [Semi-supervised transfer learning for language expansion of end-to-end speech recognition models to low-resource languages](2111.10047.md)
**Jiyeon Kim, Mehul Kumar, Dhananjaya Gowda, Abhinav Garg et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

In this paper, we propose a three-stage training methodology to improve the speech recognition accuracy of low-resource languages. We explore and propose an effective combination of techniques such as transfer learning, encoder freezing, data augmentation using Text-To-Speech (TTS), and Semi-Supervised Learning (SSL). To improve the accuracy of a low-resource Italian ASR, we leverage a well-trained English model, unlabeled text corpus, and unlabeled audio corpus using transfer learning, TTS augmentation, and SSL respectively. In the first stage, we use transfer learning from a well-trained English model. This primarily helps in learning the acoustic information from a resource-rich language. This stage achieves around 24% relative Word Error Rate (WER) reduction over the baseline. In stage two, We utilize unlabeled text data via TTS data-augmentation to incorporate language information into the model. We also explore freezing the acoustic encoder at this stage. TTS data augmentation helps us further reduce the WER by ~ 21% relatively. Finally, In stage three we reduce the WER by another 4% relative by using SSL from unlabeled audio data. Overall, our two-pass speech recognition system with a Monotonic Chunkwise Attention (MoChA) in the first pass and a full-attention in the second pass achieves a WER reduction of ~ 42% relative to the baseline.

</details>

### [A comparison of streaming models and data augmentation methods for robust speech recognition](2111.10043.md)
**Jiyeon Kim, Mehul Kumar, Dhananjaya Gowda, Abhinav Garg et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

In this paper, we present a comparative study on the robustness of two different online streaming speech recognition models: Monotonic Chunkwise Attention (MoChA) and Recurrent Neural Network-Transducer (RNN-T). We explore three recently proposed data augmentation techniques, namely, multi-conditioned training using an acoustic simulator, Vocal Tract Length Perturbation (VTLP) for speaker variability, and SpecAugment. Experimental results show that unidirectional models are in general more sensitive to noisy examples in the training set. It is observed that the final performance of the model depends on the proportion of training examples processed by data augmentation techniques. MoChA models generally perform better than RNN-T models. However, we observe that training of MoChA models seems to be more sensitive to various factors such as the characteristics of training sets and the incorporation of additional augmentations techniques. On the other hand, RNN-T models perform better than MoChA models in terms of latency, inference time, and the stability of training. Additionally, RNN-T models are generally more robust against noise and reverberation. All these advantages make RNN-T models a better choice for streaming on-device speech recognition compared to MoChA models.

</details>

### [Towards Measuring Fairness in Speech Recognition: Casual Conversations Dataset Transcriptions](2111.09983.md)
**Chunxi Liu, Michael Picheny, Leda Sarı, Pooja Chitkara et al.** · 2021-11-18

<details>
<summary>Abstract</summary>

It is well known that many machine learning systems demonstrate bias towards specific groups of individuals. This problem has been studied extensively in the Facial Recognition area, but much less so in Automatic Speech Recognition (ASR). This paper presents initial Speech Recognition results on "Casual Conversations" -- a publicly released 846 hour corpus designed to help researchers evaluate their computer vision and audio models for accuracy across a diverse set of metadata, including age, gender, and skin tone. The entire corpus has been manually transcribed, allowing for detailed ASR evaluations across these metadata. Multiple ASR models are evaluated, including models trained on LibriSpeech, 14,000 hour transcribed, and over 2 million hour untranscribed social media videos. Significant differences in word error rate across gender and skin tone are observed at times for all models. We are releasing human transcripts from the Casual Conversations dataset to encourage the community to develop a variety of techniques to reduce these statistical biases.

</details>

### [A Conformer-based ASR Frontend for Joint Acoustic Echo Cancellation, Speech Enhancement and Speech Separation](2111.09935.md)
**Tom O'Malley, Arun Narayanan, Quan Wang, Alex Park et al.** · 2021-11-18

<details>
<summary>Abstract</summary>

We present a frontend for improving robustness of automatic speech recognition (ASR), that jointly implements three modules within a single model: acoustic echo cancellation, speech enhancement, and speech separation. This is achieved by using a contextual enhancement neural network that can optionally make use of different types of side inputs: (1) a reference signal of the playback audio, which is necessary for echo cancellation; (2) a noise context, which is useful for speech enhancement; and (3) an embedding vector representing the voice characteristic of the target speaker of interest, which is not only critical in speech separation, but also helpful for echo cancellation and speech enhancement. We present detailed evaluations to show that the joint model performs almost as well as the task-specific models, and significantly reduces word error rate in noisy conditions even when using a large-scale state-of-the-art ASR model. Compared to the noisy baseline, the joint model reduces the word error rate in low signal-to-noise ratio conditions by at least 71% on our echo cancellation dataset, 10% on our noisy dataset, and 26% on our multi-speaker dataset. Compared to task-specific models, the joint model performs within 10% on our echo cancellation dataset, 2% on the noisy dataset, and 3% on the multi-speaker dataset.

</details>

### [The People's Speech: A Large-Scale Diverse English Speech Recognition Dataset for Commercial Usage](2111.09344.md)
**Daniel Galvez, Greg Diamos, Juan Ciro, Juan Felipe Cerón et al.** · 2021-11-17

<details>
<summary>Abstract</summary>

The People's Speech is a free-to-download 30,000-hour and growing supervised conversational English speech recognition dataset licensed for academic and commercial usage under CC-BY-SA (with a CC-BY subset). The data is collected via searching the Internet for appropriately licensed audio data with existing transcriptions. We describe our data collection methodology and release our data collection system under the Apache 2.0 license. We show that a model trained on this dataset achieves a 9.98% word error rate on Librispeech's test-clean test set.Finally, we discuss the legal and ethical issues surrounding the creation of a sizable machine learning corpora and plans for continued maintenance of the project under MLCommons's sponsorship.

</details>

### [XLS-R: Self-supervised Cross-lingual Speech Representation Learning at Scale](2111.09296.md)
**Arun Babu, Changhan Wang, Andros Tjandra, Kushal Lakhotia et al.** · 2021-11-17

<details>
<summary>Abstract</summary>

This paper presents XLS-R, a large-scale model for cross-lingual speech representation learning based on wav2vec 2.0. We train models with up to 2B parameters on nearly half a million hours of publicly available speech audio in 128 languages, an order of magnitude more public data than the largest known prior work. Our evaluation covers a wide range of tasks, domains, data regimes and languages, both high and low-resource. On the CoVoST-2 speech translation benchmark, we improve the previous state of the art by an average of 7.4 BLEU over 21 translation directions into English. For speech recognition, XLS-R improves over the best known prior work on BABEL, MLS, CommonVoice as well as VoxPopuli, lowering error rates by 14-34% relative on average. XLS-R also sets a new state of the art on VoxLingua107 language identification. Moreover, we show that with sufficient model size, cross-lingual pretraining can outperform English-only pretraining when translating English speech into other languages, a setting which favors monolingual pretraining. We hope XLS-R can help to improve speech processing tasks for many more languages of the world.

</details>

### [Unsupervised Speech Enhancement with speech recognition embedding and disentanglement losses](2111.08678.md)
**Viet Anh Trinh, Sebastian Braun** · 2021-11-16

<details>
<summary>Abstract</summary>

Speech enhancement has recently achieved great success with various deep learning methods. However, most conventional speech enhancement systems are trained with supervised methods that impose two significant challenges. First, a majority of training datasets for speech enhancement systems are synthetic. When mixing clean speech and noisy corpora to create the synthetic datasets, domain mismatches occur between synthetic and real-world recordings of noisy speech or audio. Second, there is a trade-off between increasing speech enhancement performance and degrading speech recognition (ASR) performance. Thus, we propose an unsupervised loss function to tackle those two problems. Our function is developed by extending the MixIT loss function with speech recognition embedding and disentanglement loss. Our results show that the proposed function effectively improves the speech enhancement performance compared to a baseline trained in a supervised way on the noisy VoxCeleb dataset. While fully unsupervised training is unable to exceed the corresponding baseline, with joint super- and unsupervised training, the system is able to achieve similar speech quality and better ASR performance than the best supervised baseline.

</details>

### [Integrated Semantic and Phonetic Post-correction for Chinese Speech Recognition](2111.08400.md)
**Yi-Chang Chen, Chun-Yen Cheng, Chien-An Chen, Ming-Chieh Sung et al.** · 2021-11-16

<details>
<summary>Abstract</summary>

Due to the recent advances of natural language processing, several works have applied the pre-trained masked language model (MLM) of BERT to the post-correction of speech recognition. However, existing pre-trained models only consider the semantic correction while the phonetic features of words is neglected. The semantic-only post-correction will consequently decrease the performance since homophonic errors are fairly common in Chinese ASR. In this paper, we proposed a novel approach to collectively exploit the contextualized representation and the phonetic information between the error and its replacing candidates to alleviate the error rate of Chinese ASR. Our experiment results on real world speech recognition datasets showed that our proposed method has evidently lower CER than the baseline model, which utilized a pre-trained BERT MLM as the corrector.

</details>

### [Attention-based Multi-hypothesis Fusion for Speech Summarization](2111.08201.md)
**Takatomo Kano, Atsunori Ogawa, Marc Delcroix, Shinji Watanabe** · 2021-11-16

<details>
<summary>Abstract</summary>

Speech summarization, which generates a text summary from speech, can be achieved by combining automatic speech recognition (ASR) and text summarization (TS). With this cascade approach, we can exploit state-of-the-art models and large training datasets for both subtasks, i.e., Transformer for ASR and Bidirectional Encoder Representations from Transformers (BERT) for TS. However, ASR errors directly affect the quality of the output summary in the cascade approach. We propose a cascade speech summarization model that is robust to ASR errors and that exploits multiple hypotheses generated by ASR to attenuate the effect of ASR errors on the summary. We investigate several schemes to combine ASR hypotheses. First, we propose using the sum of sub-word embedding vectors weighted by their posterior values provided by an ASR system as an input to a BERT-based TS system. Then, we introduce a more general scheme that uses an attention-based fusion module added to a pre-trained BERT module to align and combine several ASR hypotheses. Finally, we perform speech summarization experiments on the How2 dataset and a newly assembled TED-based dataset that we will release with this paper. These experiments show that retraining the BERT-based TS system with these schemes can improve summarization performance and that the attention-based fusion module is particularly effective.

</details>

### [Joint Unsupervised and Supervised Training for Multilingual ASR](2111.08137.md)
**Junwen Bai, Bo Li, Yu Zhang, Ankur Bapna et al.** · 2021-11-15

<details>
<summary>Abstract</summary>

Self-supervised training has shown promising gains in pretraining models and facilitating the downstream finetuning for speech recognition, like multilingual ASR. Most existing methods adopt a 2-stage scheme where the self-supervised loss is optimized in the first pretraining stage, and the standard supervised finetuning resumes in the second stage. In this paper, we propose an end-to-end (E2E) Joint Unsupervised and Supervised Training (JUST) method to combine the supervised RNN-T loss and the self-supervised contrastive and masked language modeling (MLM) losses. We validate its performance on the public dataset Multilingual LibriSpeech (MLS), which includes 8 languages and is extremely imbalanced. On MLS, we explore (1) JUST trained from scratch, and (2) JUST finetuned from a pretrained checkpoint. Experiments show that JUST can consistently outperform other existing state-of-the-art methods, and beat the monolingual baseline by a significant margin, demonstrating JUST's capability of handling low-resource languages in multilingual ASR. Our average WER of all languages outperforms average monolingual baseline by 33.3%, and the state-of-the-art 2-stage XLSR by 32%. On low-resource languages like Polish, our WER is less than half of the monolingual baseline and even beats the supervised transfer learning method which uses external supervision.

</details>

### [Analysis of Data Augmentation Methods for Low-Resource Maltese ASR](2111.07793.md)
**Andrea DeMarco, Carlos Mena, Albert Gatt, Claudia Borg et al.** · 2021-11-15

<details>
<summary>Abstract</summary>

Recent years have seen an increased interest in the computational speech processing of Maltese, but resources remain sparse. In this paper, we consider data augmentation techniques for improving speech recognition for low-resource languages, focusing on Maltese as a test case. We consider three different types of data augmentation: unsupervised training, multilingual training and the use of synthesized speech as training data. The goal is to determine which of these techniques, or combination of them, is the most effective to improve speech recognition for languages where the starting point is a small corpus of approximately 7 hours of transcribed speech. Our results show that combining the data augmentation techniques studied here lead us to an absolute WER improvement of 15% without the use of a language model.

</details>

### [Monaural source separation: From anechoic to reverberant environments](2111.07578.md)
**Tobias Cord-Landwehr, Christoph Boeddeker, Thilo von Neumann, Catalin Zorila et al.** · 2021-11-15

<details>
<summary>Abstract</summary>

Impressive progress in neural network-based single-channel speech source separation has been made in recent years. But those improvements have been mostly reported on anechoic data, a situation that is hardly met in practice. Taking the SepFormer as a starting point, which achieves state-of-the-art performance on anechoic mixtures, we gradually modify it to optimize its performance on reverberant mixtures. Although this leads to a word error rate improvement by 7 percentage points compared to the standard SepFormer implementation, the system ends up with only marginally better performance than a PIT-BLSTM separation system, that is optimized with rather straightforward means. This is surprising and at the same time sobering, challenging the practical usefulness of many improvements reported in recent years for monaural source separation on nonreverberant data.

</details>

### [Prediction of Listener Perception of Argumentative Speech in a Crowdsourced Dataset Using (Psycho-)Linguistic and Fluency Features](2111.07130.md)
**Yu Qiao, Sourabh Zanwar, Rishab Bhattacharyya, Daniel Wiechmann et al.** · 2021-11-13

<details>
<summary>Abstract</summary>

One of the key communicative competencies is the ability to maintain fluency in monologic speech and the ability to produce sophisticated language to argue a position convincingly. In this paper we aim to predict TED talk-style affective ratings in a crowdsourced dataset of argumentative speech consisting of 7 hours of speech from 110 individuals. The speech samples were elicited through task prompts relating to three debating topics. The samples received a total of 2211 ratings from 737 human raters pertaining to 14 affective categories. We present an effective approach to the classification task of predicting these categories through fine-tuning a model pre-trained on a large dataset of TED talks public speeches. We use a combination of fluency features derived from a state-of-the-art automatic speech recognition system and a large set of human-interpretable linguistic features obtained from an automatic text analysis system. Classification accuracy was greater than 60% for all 14 rating categories, with a peak performance of 72% for the rating category 'informative'. In a secondary experiment, we determined the relative importance of features from different groups using SP-LIME.

</details>

### [Measuring the Contribution of Multiple Model Representations in Detecting Adversarial Instances](2111.07035.md)
**Daniel Steinberg, Paul Munro** · 2021-11-13

<details>
<summary>Abstract</summary>

Deep learning models have been used for a wide variety of tasks. They are prevalent in computer vision, natural language processing, speech recognition, and other areas. While these models have worked well under many scenarios, it has been shown that they are vulnerable to adversarial attacks. This has led to a proliferation of research into ways that such attacks could be identified and/or defended against. Our goal is to explore the contribution that can be attributed to using multiple underlying models for the purpose of adversarial instance detection. Our paper describes two approaches that incorporate representations from multiple models for detecting adversarial examples. We devise controlled experiments for measuring the detection impact of incrementally utilizing additional models. For many of the scenarios we consider, the results show that performance increases with the number of underlying models used for extracting representations.

</details>

### [Can neural networks predict dynamics they have never seen?](2111.06783.md)
**Anton Pershin, Cedric Beaume, Kuan Li, Steven M. Tobias** · 2021-11-12

<details>
<summary>Abstract</summary>

Neural networks have proven to be remarkably successful for a wide range of complicated tasks, from image recognition and object detection to speech recognition and machine translation. One of their successes is the skill in prediction of future dynamics given a suitable training set of data. Previous studies have shown how Echo State Networks (ESNs), a subset of Recurrent Neural Networks, can successfully predict even chaotic systems for times longer than the Lyapunov time. This study shows that, remarkably, ESNs can successfully predict dynamical behavior that is qualitatively different from any behavior contained in the training set. Evidence is provided for a fluid dynamics problem where the flow can transition between laminar (ordered) and turbulent (disordered) regimes. Despite being trained on the turbulent regime only, ESNs are found to predict laminar behavior. Moreover, the statistics of turbulent-to-laminar and laminar-to-turbulent transitions are also predicted successfully, and the utility of ESNs in acting as an early-warning system for transition is discussed. These results are expected to be widely applicable to data-driven modelling of temporal behaviour in a range of physical, climate, biological, ecological and finance models characterized by the presence of tipping points and sudden transitions between several competing states.

</details>

### [A Convolutional Neural Network Based Approach to Recognize Bangla Spoken Digits from Speech Signal](2111.06625.md)
**Ovishake Sen, Al-Mahmud, Pias Roy** · 2021-11-12

<details>
<summary>Abstract</summary>

Speech recognition is a technique that converts human speech signals into text or words or in any form that can be easily understood by computers or other machines. There have been a few studies on Bangla digit recognition systems, the majority of which used small datasets with few variations in genders, ages, dialects, and other variables. Audio recordings of Bangladeshi people of various genders, ages, and dialects were used to create a large speech dataset of spoken '0-9' Bangla digits in this study. Here, 400 noisy and noise-free samples per digit have been recorded for creating the dataset. Mel Frequency Cepstrum Coefficients (MFCCs) have been utilized for extracting meaningful features from the raw speech data. Then, to detect Bangla numeral digits, Convolutional Neural Networks (CNNs) were utilized. The suggested technique recognizes '0-9' Bangla spoken digits with 97.1% accuracy throughout the whole dataset. The efficiency of the model was also assessed using 10-fold crossvalidation, which yielded a 96.7% accuracy.

</details>

### [Deciphering Speech: a Zero-Resource Approach to Cross-Lingual Transfer in ASR](2111.06799.md)
**Ondrej Klejch, Electra Wallington, Peter Bell** · 2021-11-12

<details>
<summary>Abstract</summary>

We present a method for cross-lingual training an ASR system using absolutely no transcribed training data from the target language, and with no phonetic knowledge of the language in question. Our approach uses a novel application of a decipherment algorithm, which operates given only unpaired speech and text data from the target language. We apply this decipherment to phone sequences generated by a universal phone recogniser trained on out-of-language speech corpora, which we follow with flat-start semi-supervised training to obtain an acoustic model for the new language. To the best of our knowledge, this is the first practical approach to zero-resource cross-lingual ASR which does not rely on any hand-crafted phonetic information. We carry out experiments on read speech from the GlobalPhone corpus, and show that it is possible to learn a decipherment model on just 20 minutes of data from the target language. When used to generate pseudo-labels for semi-supervised training, we obtain WERs that range from 32.5% to just 1.9% absolute worse than the equivalent fully supervised models trained on the same data.

</details>

### [Self-Normalized Importance Sampling for Neural Language Modeling](2111.06310.md)
**Zijian Yang, Yingbo Gao, Alexander Gerstenberger, Jintao Jiang et al.** · 2021-11-11

<details>
<summary>Abstract</summary>

To mitigate the problem of having to traverse over the full vocabulary in the softmax normalization of a neural language model, sampling-based training criteria are proposed and investigated in the context of large vocabulary word-based neural language models. These training criteria typically enjoy the benefit of faster training and testing, at a cost of slightly degraded performance in terms of perplexity and almost no visible drop in word error rate. While noise contrastive estimation is one of the most popular choices, recently we show that other sampling-based criteria can also perform well, as long as an extra correction step is done, where the intended class posterior probability is recovered from the raw model outputs. In this work, we propose self-normalized importance sampling. Compared to our previous work, the criteria considered in this work are self-normalized and there is no need to further conduct a correction step. Through self-normalized language model training as well as lattice rescoring experiments, we show that our proposed self-normalized importance sampling is competitive in both research-oriented and production-oriented automatic speech recognition tasks.

</details>

### [Joint Neural AEC and Beamforming with Double-Talk Detection](2111.04904.md)
**Vinay Kothapally, Yong Xu, Meng Yu, Shi-Xiong Zhang et al.** · 2021-11-09

<details>
<summary>Abstract</summary>

Acoustic echo cancellation (AEC) in full-duplex communication systems eliminates acoustic feedback. However, nonlinear distortions induced by audio devices, background noise, reverberation, and double-talk reduce the efficiency of conventional AEC systems. Several hybrid AEC models were proposed to address this, which use deep learning models to suppress residual echo from standard adaptive filtering. This paper proposes deep learning-based joint AEC and beamforming model (JAECBF) building on our previous self-attentive recurrent neural network (RNN) beamformer. The proposed network consists of two modules: (i) multi-channel neural-AEC, and (ii) joint AEC-RNN beamformer with a double-talk detection (DTD) that computes time-frequency (T-F) beamforming weights. We train the proposed model in an end-to-end approach to eliminate background noise and echoes from far-end audio devices, which include nonlinear distortions. From experimental evaluations, we find the proposed network outperforms other multi-channel AEC and denoising systems in terms of speech recognition rate and overall speech quality.

</details>

### [Privacy attacks for automatic speech recognition acoustic models in a federated learning framework](2111.03777.md)
**Natalia Tomashenko, Salima Mdhaffar, Marc Tommasi, Yannick Estève et al.** · 2021-11-06

<details>
<summary>Abstract</summary>

This paper investigates methods to effectively retrieve speaker information from the personalized speaker adapted neural network acoustic models (AMs) in automatic speech recognition (ASR). This problem is especially important in the context of federated learning of ASR acoustic models where a global model is learnt on the server based on the updates received from multiple clients. We propose an approach to analyze information in neural network AMs based on a neural network footprint on the so-called Indicator dataset. Using this method, we develop two attack models that aim to infer speaker identity from the updated personalized models without access to the actual users' speech data. Experiments on the TED-LIUM 3 corpus demonstrate that the proposed approaches are very effective and can provide equal error rate (EER) of 1-2%.

</details>

### [Conformer-based Hybrid ASR System for Switchboard Dataset](2111.03442.md)
**Mohammad Zeineldeen, Jingjing Xu, Christoph Lüscher, Wilfried Michel et al.** · 2021-11-05

<details>
<summary>Abstract</summary>

The recently proposed conformer architecture has been successfully used for end-to-end automatic speech recognition (ASR) architectures achieving state-of-the-art performance on different datasets. To our best knowledge, the impact of using conformer acoustic model for hybrid ASR is not investigated. In this paper, we present and evaluate a competitive conformer-based hybrid model training recipe. We study different training aspects and methods to improve word-error-rate as well as to increase training speed. We apply time downsampling methods for efficient training and use transposed convolutions to upsample the output sequence again. We conduct experiments on Switchboard 300h dataset and our conformer-based hybrid model achieves competitive results compared to other architectures. It generalizes very well on Hub5'01 test set and outperforms the BLSTM-based hybrid model significantly.

</details>

### [Effective Cross-Utterance Language Modeling for Conversational Speech Recognition](2111.03333.md)
**Bi-Cheng Yan, Hsin-Wei Wang, Shih-Hsuan Chiu, Hsuan-Sheng Chiu et al.** · 2021-11-05

<details>
<summary>Abstract</summary>

Conversational speech normally is embodied with loose syntactic structures at the utterance level but simultaneously exhibits topical coherence relations across consecutive utterances. Prior work has shown that capturing longer context information with a recurrent neural network or long short-term memory language model (LM) may suffer from the recent bias while excluding the long-range context. In order to capture the long-term semantic interactions among words and across utterances, we put forward disparate conversation history fusion methods for language modeling in automatic speech recognition (ASR) of conversational speech. Furthermore, a novel audio-fusion mechanism is introduced, which manages to fuse and utilize the acoustic embeddings of a current utterance and the semantic content of its corresponding conversation history in a cooperative way. To flesh out our ideas, we frame the ASR N-best hypothesis rescoring task as a prediction problem, leveraging BERT, an iconic pre-trained LM, as the ingredient vehicle to facilitate selection of the oracle hypothesis from a given N-best hypothesis list. Empirical experiments conducted on the AMI benchmark dataset seem to demonstrate the feasibility and efficacy of our methods in relation to some current top-of-line methods. The proposed methods not only achieve significant inference time reduction but also improve the ASR performance for conversational speech.

</details>

### [Learning of Time-Frequency Attention Mechanism for Automatic Modulation Recognition](2111.03258.md)
**Shangao Lin, Yuan Zeng, Yi Gong** · 2021-11-05

<details>
<summary>Abstract</summary>

Recent learning-based image classification and speech recognition approaches make extensive use of attention mechanisms to achieve state-of-the-art recognition power, which demonstrates the effectiveness of attention mechanisms. Motivated by the fact that the frequency and time information of modulated radio signals are crucial for modulation mode recognition, this paper proposes a time-frequency attention mechanism for a convolutional neural network (CNN)-based modulation recognition framework. The proposed time-frequency attention module is designed to learn which channel, frequency and time information is more meaningful in CNN for modulation recognition. We analyze the effectiveness of the proposed time-frequency attention mechanism and compare the proposed method with two existing learning-based methods. Experiments on an open-source modulation recognition dataset show that the recognition performance of the proposed framework is better than those of the framework without time-frequency attention and existing learning-based methods.

</details>

### [Context-Aware Transformer Transducer for Speech Recognition](2111.03250.md)
**Feng-Ju Chang, Jing Liu, Martin Radfar, Athanasios Mouchtaris et al.** · 2021-11-05

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) systems often have difficulty recognizing uncommon words, that appear infrequently in the training data. One promising method, to improve the recognition accuracy on such rare words, is to latch onto personalized/contextual information at inference. In this work, we present a novel context-aware transformer transducer (CATT) network that improves the state-of-the-art transformer-based ASR system by taking advantage of such contextual signals. Specifically, we propose a multi-head attention-based context-biasing network, which is jointly trained with the rest of the ASR sub-networks. We explore different techniques to encode contextual data and to create the final attention context vectors. We also leverage both BLSTM and pretrained BERT based models to encode contextual data and guide the network training. Using an in-house far-field dataset, we show that CATT, using a BERT based context encoder, improves the word error rate of the baseline transformer transducer and outperforms an existing deep contextual model by 24.2% and 19.4% respectively.

</details>

### [MT3: Multi-Task Multitrack Music Transcription](2111.03017.md)
**Josh Gardner, Ian Simon, Ethan Manilow, Curtis Hawthorne et al.** · 2021-11-04

<details>
<summary>Abstract</summary>

Automatic Music Transcription (AMT), inferring musical notes from raw audio, is a challenging task at the core of music understanding. Unlike Automatic Speech Recognition (ASR), which typically focuses on the words of a single speaker, AMT often requires transcribing multiple instruments simultaneously, all while preserving fine-scale pitch and timing information. Further, many AMT datasets are "low-resource", as even expert musicians find music transcription difficult and time-consuming. Thus, prior work has focused on task-specific architectures, tailored to the individual instruments of each task. In this work, motivated by the promising results of sequence-to-sequence transfer learning for low-resource Natural Language Processing (NLP), we demonstrate that a general-purpose Transformer model can perform multi-task AMT, jointly transcribing arbitrary combinations of musical instruments across several transcription datasets. We show this unified training framework achieves high-quality transcription results across a range of datasets, dramatically improving performance for low-resource instruments (such as guitar), while preserving strong performance for abundant instruments (such as piano). Finally, by expanding the scope of AMT, we expose the need for more consistent evaluation metrics and better dataset alignment, and provide a strong baseline for this new direction of multi-task AMT.

</details>

### [Speech recognition for air traffic control via feature learning and end-to-end training](2111.02654.md)
**Peng Fan, Dongyue Guo, Yi Lin, Bo Yang et al.** · 2021-11-04

<details>
<summary>Abstract</summary>

In this work, we propose a new automatic speech recognition (ASR) system based on feature learning and an end-to-end training procedure for air traffic control (ATC) systems. The proposed model integrates the feature learning block, recurrent neural network (RNN), and connectionist temporal classification loss to build an end-to-end ASR model. Facing the complex environments of ATC speech, instead of the handcrafted features, a learning block is designed to extract informative features from raw waveforms for acoustic modeling. Both the SincNet and 1D convolution blocks are applied to process the raw waveforms, whose outputs are concatenated to the RNN layers for the temporal modeling. Thanks to the ability to learn representations from raw waveforms, the proposed model can be optimized in a complete end-to-end manner, i.e., from waveform to text. Finally, the multilingual issue in the ATC domain is also considered to achieve the ASR task by constructing a combined vocabulary of Chinese characters and English letters. The proposed approach is validated on a multilingual real-world corpus (ATCSpeech), and the experimental results demonstrate that the proposed approach outperforms other baselines, achieving a 6.9\% character error rate.

</details>

### [Recent Advances in End-to-End Automatic Speech Recognition](2111.01690.md)
**Jinyu Li** · 2021-11-02

<details>
<summary>Abstract</summary>

Recently, the speech community is seeing a significant trend of moving from deep neural network based hybrid modeling to end-to-end (E2E) modeling for automatic speech recognition (ASR). While E2E models achieve the state-of-the-art results in most benchmarks in terms of ASR accuracy, hybrid models are still used in a large proportion of commercial ASR systems at the current time. There are lots of practical factors that affect the production model deployment decision. Traditional hybrid models, being optimized for production for decades, are usually good at these factors. Without providing excellent solutions to all these factors, it is hard for E2E models to be widely commercialized. In this paper, we will overview the recent advances in E2E models, focusing on technologies addressing those challenges from the industry's perspective.

</details>

### [Sequence Transduction with Graph-based Supervision](2111.01272.md)
**Niko Moritz, Takaaki Hori, Shinji Watanabe, Jonathan Le Roux** · 2021-11-01

<details>
<summary>Abstract</summary>

The recurrent neural network transducer (RNN-T) objective plays a major role in building today's best automatic speech recognition (ASR) systems for production. Similarly to the connectionist temporal classification (CTC) objective, the RNN-T loss uses specific rules that define how a set of alignments is generated to form a lattice for the full-sum training. However, it is yet largely unknown if these rules are optimal and do lead to the best possible ASR results. In this work, we present a new transducer objective function that generalizes the RNN-T loss to accept a graph representation of the labels, thus providing a flexible and efficient framework to manipulate training lattices, e.g., for studying different transition rules, implementing different transducer losses, or restricting alignments. We demonstrate that transducer-based ASR with CTC-like lattice achieves better results compared to standard RNN-T, while also ensuring a strictly monotonic alignment, which will allow better optimization of the decoding procedure. For example, the proposed CTC-like transducer achieves an improvement of 4.8% on the test-other condition of LibriSpeech relative to an equivalent RNN-T based system.

</details>

### [A transfer learning based approach for pronunciation scoring](2111.00976.md)
**Marcelo Sancinetti, Jazmin Vidal, Cyntia Bonomi, Luciana Ferrer** · 2021-11-01

<details>
<summary>Abstract</summary>

Phone-level pronunciation scoring is a challenging task, with performance far from that of human annotators. Standard systems generate a score for each phone in a phrase using models trained for automatic speech recognition (ASR) with native data only. Better performance has been shown when using systems that are trained specifically for the task using non-native data. Yet, such systems face the challenge that datasets labelled for this task are scarce and usually small. In this paper, we present a transfer learning-based approach that leverages a model trained for ASR, adapting it for the task of pronunciation scoring. We analyze the effect of several design choices and compare the performance with a state-of-the-art goodness of pronunciation (GOP) system. Our final system is 20% better than the GOP system on EpaDB, a database for pronunciation scoring research, for a cost function that prioritizes low rates of unnecessary corrections.

</details>

### [Revisiting joint decoding based multi-talker speech recognition with DNN acoustic model](2111.00009.md)
**Martin Kocour, Kateřina Žmolíková, Lucas Ondel, Ján Švec et al.** · 2021-10-31

<details>
<summary>Abstract</summary>

In typical multi-talker speech recognition systems, a neural network-based acoustic model predicts senone state posteriors for each speaker. These are later used by a single-talker decoder which is applied on each speaker-specific output stream separately. In this work, we argue that such a scheme is sub-optimal and propose a principled solution that decodes all speakers jointly. We modify the acoustic model to predict joint state posteriors for all speakers, enabling the network to express uncertainty about the attribution of parts of the speech signal to the speakers. We employ a joint decoder that can make use of this uncertainty together with higher-level language information. For this, we revisit decoding algorithms used in factorial generative models in early multi-talker speech recognition systems. In contrast with these early works, we replace the GMM acoustic model with DNN, which provides greater modeling power and simplifies part of the inference. We demonstrate the advantage of joint decoding in proof of concept experiments on a mixed-TIDIGITS dataset.

</details>

### [Speaker conditioning of acoustic models using affine transformation for multi-speaker speech recognition](2111.00320.md)
**Midia Yousefi, John H. L. Hanse** · 2021-10-30

<details>
<summary>Abstract</summary>

This study addresses the problem of single-channel Automatic Speech Recognition of a target speaker within an overlap speech scenario. In the proposed method, the hidden representations in the acoustic model are modulated by speaker auxiliary information to recognize only the desired speaker. Affine transformation layers are inserted into the acoustic model network to integrate speaker information with the acoustic features. The speaker conditioning process allows the acoustic model to perform computation in the context of target-speaker auxiliary information. The proposed speaker conditioning method is a general approach and can be applied to any acoustic model architecture. Here, we employ speaker conditioning on a ResNet acoustic model. Experiments on the WSJ corpus show that the proposed speaker conditioning method is an effective solution to fuse speaker auxiliary information with acoustic features for multi-speaker speech recognition, achieving +9% and +20% relative WER reduction for clean and overlap speech scenarios, respectively, compared to the original ResNet acoustic model baseline.

</details>

### [Pseudo-Labeling for Massively Multilingual Speech Recognition](2111.00161.md)
**Loren Lugosch, Tatiana Likhomanenko, Gabriel Synnaeve, Ronan Collobert** · 2021-10-30

<details>
<summary>Abstract</summary>

Semi-supervised learning through pseudo-labeling has become a staple of state-of-the-art monolingual speech recognition systems. In this work, we extend pseudo-labeling to massively multilingual speech recognition with 60 languages. We propose a simple pseudo-labeling recipe that works well even with low-resource languages: train a supervised multilingual model, fine-tune it with semi-supervised learning on a target language, generate pseudo-labels for that language, and train a final model using pseudo-labels for all languages, either from scratch or by fine-tuning. Experiments on the labeled Common Voice and unlabeled VoxPopuli datasets show that our recipe can yield a model with better performance for many languages that also transfers well to LibriSpeech.

</details>

### [Cross-attention conformer for context modeling in speech enhancement for ASR](2111.00127.md)
**Arun Narayanan, Chung-Cheng Chiu, Tom O'Malley, Quan Wang et al.** · 2021-10-30

<details>
<summary>Abstract</summary>

This work introduces \emph{cross-attention conformer}, an attention-based architecture for context modeling in speech enhancement. Given that the context information can often be sequential, and of different length as the audio that is to be enhanced, we make use of cross-attention to summarize and merge contextual information with input features. Building upon the recently proposed conformer model that uses self attention layers as building blocks, the proposed cross-attention conformer can be used to build deep contextual models. As a concrete example, we show how noise context, i.e., short noise-only audio segment preceding an utterance, can be used to build a speech enhancement feature frontend using cross-attention conformer layers for improving noise robustness of automatic speech recognition.

</details>

### [Combining Unsupervised and Text Augmented Semi-Supervised Learning for Low Resourced Autoregressive Speech Recognition](2110.15836.md)
**Chak-Fai Li, Francis Keith, William Hartmann, Matthew Snover** · 2021-10-29

<details>
<summary>Abstract</summary>

Recent advances in unsupervised representation learning have demonstrated the impact of pretraining on large amounts of read speech. We adapt these techniques for domain adaptation in low-resource -- both in terms of data and compute -- conversational and broadcast domains. Moving beyond CTC, we pretrain state-of-the-art Conformer models in an unsupervised manner. While the unsupervised approach outperforms traditional semi-supervised training, the techniques are complementary. Combining the techniques is a 5% absolute improvement in WER, averaged over all conditions, compared to semi-supervised training alone. Additional text data is incorporated through external language models. By using CTC-based decoding, we are better able to take advantage of the additional text data. When used as a transcription model, it allows the Conformer model to better incorporate the knowledge from the language model through semi-supervised training than shallow fusion. Final performance is an additional 2% better absolute when using CTC-based decoding for semi-supervised training compared to shallow fusion.

</details>

### [Improving Noise Robustness of Contrastive Speech Representation Learning with Speech Reconstruction](2110.15430.md)
**Heming Wang, Yao Qian, Xiaofei Wang, Yiming Wang et al.** · 2021-10-28

<details>
<summary>Abstract</summary>

Noise robustness is essential for deploying automatic speech recognition (ASR) systems in real-world environments. One way to reduce the effect of noise interference is to employ a preprocessing module that conducts speech enhancement, and then feed the enhanced speech to an ASR backend. In this work, instead of suppressing background noise with a conventional cascaded pipeline, we employ a noise-robust representation learned by a refined self-supervised framework for noisy speech recognition. We propose to combine a reconstruction module with contrastive learning and perform multi-task continual pre-training on noisy data. The reconstruction module is used for auxiliary learning to improve the noise robustness of the learned representation and thus is not required during inference. Experiments demonstrate the effectiveness of our proposed method. Our model substantially reduces the word error rate (WER) for the synthesized noisy LibriSpeech test sets, and yields around 4.1/7.5% WER reduction on noisy clean/other test sets compared to data augmentation. For the real-world noisy speech from the CHiME-4 challenge (1-channel track), we have obtained the state of the art ASR performance without any denoising front-end. Moreover, we achieve comparable performance to the best supervised approach reported with only 16% of labeled data.

</details>

### [Continuous Speech Separation with Recurrent Selective Attention Network](2110.14838.md)
**Yixuan Zhang, Zhuo Chen, Jian Wu, Takuya Yoshioka et al.** · 2021-10-28

<details>
<summary>Abstract</summary>

While permutation invariant training (PIT) based continuous speech separation (CSS) significantly improves the conversation transcription accuracy, it often suffers from speech leakages and failures in separation at "hot spot" regions because it has a fixed number of output channels. In this paper, we propose to apply recurrent selective attention network (RSAN) to CSS, which generates a variable number of output channels based on active speaker counting. In addition, we propose a novel block-wise dependency extension of RSAN by introducing dependencies between adjacent processing blocks in the CSS framework. It enables the network to utilize the separation results from the previous blocks to facilitate the current block processing. Experimental results on the LibriCSS dataset show that the RSAN-based CSS (RSAN-CSS) network consistently improves the speech recognition accuracy over PIT-based models. The proposed block-wise dependency modeling further boosts the performance of RSAN-CSS.

</details>

### [Closing the Gap Between Time-Domain Multi-Channel Speech Enhancement on Real and Simulation Conditions](2110.14139.md)
**Wangyou Zhang, Jing Shi, Chenda Li, Shinji Watanabe et al.** · 2021-10-27

<details>
<summary>Abstract</summary>

The deep learning based time-domain models, e.g. Conv-TasNet, have shown great potential in both single-channel and multi-channel speech enhancement. However, many experiments on the time-domain speech enhancement model are done in simulated conditions, and it is not well studied whether the good performance can generalize to real-world scenarios. In this paper, we aim to provide an insightful investigation of applying multi-channel Conv-TasNet based speech enhancement to both simulation and real data. Our preliminary experiments show a large performance gap between the two conditions in terms of the ASR performance. Several approaches are applied to close this gap, including the integration of multi-channel Conv-TasNet into the beamforming model with various strategies, and the joint training of speech enhancement and speech recognition models. Our experiments on the CHiME-4 corpus show that our proposed approaches can greatly reduce the speech recognition performance discrepancy between simulation and real data, while preserving the strong speech enhancement capability in the frontend.

</details>

### [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](2110.13900.md)
**Sanyuan Chen, Chengyi Wang, Zhengyang Chen, Yu Wu et al.** · 2021-10-26

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) achieves great success in speech recognition, while limited exploration has been attempted for other speech processing tasks. As speech signal contains multi-faceted information including speaker identity, paralinguistics, spoken content, etc., learning universal representations for all speech tasks is challenging. To tackle the problem, we propose a new pre-trained model, WavLM, to solve full-stack downstream speech tasks. WavLM jointly learns masked speech prediction and denoising in pre-training. By this means, WavLM does not only keep the speech content modeling capability by the masked speech prediction, but also improves the potential to non-ASR tasks by the speech denoising. In addition, WavLM employs gated relative position bias for the Transformer structure to better capture the sequence ordering of input speech. We also scale up the training dataset from 60k hours to 94k hours. WavLM Large achieves state-of-the-art performance on the SUPERB benchmark, and brings significant improvements for various speech processing tasks on their representative benchmarks. The code and pre-trained models are available at https://aka.ms/wavlm.

</details>

### [Beyond $L_p$ clipping: Equalization-based Psychoacoustic Attacks against ASRs](2110.13250.md)
**Hadi Abdullah, Muhammad Sajidur Rahman, Christian Peeters, Cassidy Gibson et al.** · 2021-10-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems convert speech into text and can be placed into two broad categories: traditional and fully end-to-end. Both types have been shown to be vulnerable to adversarial audio examples that sound benign to the human ear but force the ASR to produce malicious transcriptions. Of these attacks, only the "psychoacoustic" attacks can create examples with relatively imperceptible perturbations, as they leverage the knowledge of the human auditory system. Unfortunately, existing psychoacoustic attacks can only be applied against traditional models, and are obsolete against the newer, fully end-to-end ASRs. In this paper, we propose an equalization-based psychoacoustic attack that can exploit both traditional and fully end-to-end ASRs. We successfully demonstrate our attack against real-world ASRs that include DeepSpeech and Wav2Letter. Moreover, we employ a user study to verify that our method creates low audible distortion. Specifically, 80 of the 100 participants voted in favor of all our attack audio samples as less noisier than the existing state-of-the-art attack. Through this, we demonstrate both types of existing ASR pipelines can be exploited with minimum degradation to attack audio quality.

</details>

### [Lhotse: a speech data representation library for the modern deep learning ecosystem](2110.12561.md)
**Piotr Żelasko, Daniel Povey, Jan "Yenda" Trmal, Sanjeev Khudanpur** · 2021-10-25

<details>
<summary>Abstract</summary>

Speech data is notoriously difficult to work with due to a variety of codecs, lengths of recordings, and meta-data formats. We present Lhotse, a speech data representation library that draws upon lessons learned from Kaldi speech recognition toolkit and brings its concepts into the modern deep learning ecosystem. Lhotse provides a common JSON description format with corresponding Python classes and data preparation recipes for over 30 popular speech corpora. Various datasets can be easily combined together and re-purposed for different tasks. The library handles multi-channel recordings, long recordings, local and cloud storage, lazy and on-the-fly operations amongst other features. We introduce Cut and CutSet concepts, which simplify common data wrangling tasks for audio and help incorporate acoustic context of speech utterances. Finally, we show how Lhotse leverages PyTorch data API abstractions and adopts them to handle speech data for deep learning.

</details>

### [Game of Gradients: Mitigating Irrelevant Clients in Federated Learning](2110.12257.md)
**Lokesh Nagalapatti, Ramasuri Narayanam** · 2021-10-23

<details>
<summary>Abstract</summary>

The paradigm of Federated learning (FL) deals with multiple clients participating in collaborative training of a machine learning model under the orchestration of a central server. In this setup, each client's data is private to itself and is not transferable to other clients or the server. Though FL paradigm has received significant interest recently from the research community, the problem of selecting the relevant clients w.r.t. the central server's learning objective is under-explored. We refer to these problems as Federated Relevant Client Selection (FRCS). Because the server doesn't have explicit control over the nature of data possessed by each client, the problem of selecting relevant clients is significantly complex in FL settings. In this paper, we resolve important and related FRCS problems viz., selecting clients with relevant data, detecting clients that possess data relevant to a particular target label, and rectifying corrupted data samples of individual clients. We follow a principled approach to address the above FRCS problems and develop a new federated learning method using the Shapley value concept from cooperative game theory. Towards this end, we propose a cooperative game involving the gradients shared by the clients. Using this game, we compute Shapley values of clients and then present Shapley value based Federated Averaging (S-FedAvg) algorithm that empowers the server to select relevant clients with high probability. S-FedAvg turns out to be critical in designing specific algorithms to address the FRCS problems. We finally conduct a thorough empirical analysis on image classification and speech recognition tasks to show the superior performance of S-FedAvg than the baselines in the context of supervised federated learning settings.

</details>

### [Optimizing Alignment of Speech and Language Latent Spaces for End-to-End Speech Recognition and Understanding](2110.12138.md)
**Wei Wang, Shuo Ren, Yao Qian, Shujie Liu et al.** · 2021-10-23

<details>
<summary>Abstract</summary>

The advances in attention-based encoder-decoder (AED) networks have brought great progress to end-to-end (E2E) automatic speech recognition (ASR). One way to further improve the performance of AED-based E2E ASR is to introduce an extra text encoder for leveraging extensive text data and thus capture more context-aware linguistic information. However, this approach brings a mismatch problem between the speech encoder and the text encoder due to the different units used for modeling. In this paper, we propose an embedding aligner and modality switch training to better align the speech and text latent spaces. The embedding aligner is a shared linear projection between text encoder and speech encoder trained by masked language modeling (MLM) loss and connectionist temporal classification (CTC), respectively. The modality switch training randomly swaps speech and text embeddings based on the forced alignment result to learn a joint representation space. Experimental results show that our proposed approach achieves a relative 14% to 19% word error rate (WER) reduction on Librispeech ASR task. We further verify its effectiveness on spoken language understanding (SLU), i.e., an absolute 2.5% to 2.8% F1 score improvement on SNIPS slot filling task.

</details>

### [Synt++: Utilizing Imperfect Synthetic Data to Improve Speech Recognition](2110.11479.md)
**Ting-Yao Hu, Mohammadreza Armandpour, Ashish Shrivastava, Jen-Hao Rick Chang et al.** · 2021-10-21

<details>
<summary>Abstract</summary>

With recent advances in speech synthesis, synthetic data is becoming a viable alternative to real data for training speech recognition models. However, machine learning with synthetic data is not trivial due to the gap between the synthetic and the real data distributions. Synthetic datasets may contain artifacts that do not exist in real data such as structured noise, content errors, or unrealistic speaking styles. Moreover, the synthesis process may introduce a bias due to uneven sampling of the data manifold. We propose two novel techniques during training to mitigate the problems due to the distribution gap: (i) a rejection sampling algorithm and (ii) using separate batch normalization statistics for the real and the synthetic samples. We show that these methods significantly improve the training of speech recognition models using synthetic data. We evaluate the proposed approach on keyword detection and Automatic Speech Recognition (ASR) tasks, and observe up to 18% and 13% relative error reduction, respectively, compared to naively using the synthetic data.

</details>

### [Asynchronous Decentralized Distributed Training of Acoustic Models](2110.11199.md)
**Xiaodong Cui, Wei Zhang, Abdullah Kayi, Mingrui Liu et al.** · 2021-10-21

<details>
<summary>Abstract</summary>

Large-scale distributed training of deep acoustic models plays an important role in today's high-performance automatic speech recognition (ASR). In this paper we investigate a variety of asynchronous decentralized distributed training strategies based on data parallel stochastic gradient descent (SGD) to show their superior performance over the commonly-used synchronous distributed training via allreduce, especially when dealing with large batch sizes. Specifically, we study three variants of asynchronous decentralized parallel SGD (ADPSGD), namely, fixed and randomized communication patterns on a ring as well as a delay-by-one scheme. We introduce a mathematical model of ADPSGD, give its theoretical convergence rate, and compare the empirical convergence behavior and straggler resilience properties of the three variants. Experiments are carried out on an IBM supercomputer for training deep long short-term memory (LSTM) acoustic models on the 2000-hour Switchboard dataset. Recognition and speedup performance of the proposed strategies are evaluated under various training configurations. We show that ADPSGD with fixed and randomized communication patterns cope well with slow learners. When learners are equally fast, ADPSGD with the delay-by-one strategy has the fastest convergence with large batches. In particular, using the delay-by-one strategy, we can train the acoustic model in less than 2 hours using 128 V100 GPUs with competitive word error rates.

</details>

### [Knowledge distillation from language model to acoustic model: a hierarchical multi-task learning approach](2110.10429.md)
**Mun-Hak Lee, Joon-Hyuk Chang** · 2021-10-20

<details>
<summary>Abstract</summary>

The remarkable performance of the pre-trained language model (LM) using self-supervised learning has led to a major paradigm shift in the study of natural language processing. In line with these changes, leveraging the performance of speech recognition systems with massive deep learning-based LMs is a major topic of speech recognition research. Among the various methods of applying LMs to speech recognition systems, in this paper, we focus on a cross-modal knowledge distillation method that transfers knowledge between two types of deep neural networks with different modalities. We propose an acoustic model structure with multiple auxiliary output layers for cross-modal distillation and demonstrate that the proposed method effectively compensates for the shortcomings of the existing label-interpolation-based distillation method. In addition, we extend the proposed method to a hierarchical distillation method using LMs trained in different units (senones, monophones, and subwords) and reveal the effectiveness of the hierarchical distillation method through an ablation study.

</details>

### [An Investigation of Enhancing CTC Model for Triggered Attention-based Streaming ASR](2110.10402.md)
**Huaibo Zhao, Yosuke Higuchi, Tetsuji Ogawa, Tetsunori Kobayashi** · 2021-10-20

<details>
<summary>Abstract</summary>

In the present paper, an attempt is made to combine Mask-CTC and the triggered attention mechanism to construct a streaming end-to-end automatic speech recognition (ASR) system that provides high performance with low latency. The triggered attention mechanism, which performs autoregressive decoding triggered by the CTC spike, has shown to be effective in streaming ASR. However, in order to maintain high accuracy of alignment estimation based on CTC outputs, which is the key to its performance, it is inevitable that decoding should be performed with some future information input (i.e., with higher latency). It should be noted that in streaming ASR, it is desirable to be able to achieve high recognition accuracy while keeping the latency low. Therefore, the present study aims to achieve highly accurate streaming ASR with low latency by introducing Mask-CTC, which is capable of learning feature representations that anticipate future information (i.e., that can consider long-term contexts), to the encoder pre-training. Experimental comparisons conducted using WSJ data demonstrate that the proposed method achieves higher accuracy with lower latency than the conventional triggered attention-based streaming ASR system.

</details>

### [SLAM: A Unified Encoder for Speech and Language Modeling via Speech-Text Joint Pre-Training](2110.10329.md)
**Ankur Bapna, Yu-an Chung, Nan Wu, Anmol Gulati et al.** · 2021-10-20

<details>
<summary>Abstract</summary>

Unsupervised pre-training is now the predominant approach for both text and speech understanding. Self-attention models pre-trained on large amounts of unannotated data have been hugely successful when fine-tuned on downstream tasks from a variety of domains and languages. This paper takes the universality of unsupervised language pre-training one step further, by unifying speech and text pre-training within a single model. We build a single encoder with the BERT objective on unlabeled text together with the w2v-BERT objective on unlabeled speech. To further align our model representations across modalities, we leverage alignment losses, specifically Translation Language Modeling (TLM) and Speech Text Matching (STM) that make use of supervised speech-text recognition data. We demonstrate that incorporating both speech and text data during pre-training can significantly improve downstream quality on CoVoST~2 speech translation, by around 1 BLEU compared to single-modality pre-trained models, while retaining close to SotA performance on LibriSpeech and SpeechStew ASR tasks. On four GLUE tasks and text-normalization, we observe evidence of capacity limitations and interference between the two modalities, leading to degraded performance compared to an equivalent text-only model, while still being competitive with BERT. Through extensive empirical analysis we also demonstrate the importance of the choice of objective function for speech pre-training, and the beneficial effect of adding additional supervised signals on the quality of the learned representations.

</details>

### [Speech Pattern based Black-box Model Watermarking for Automatic Speech Recognition](2110.09814.md)
**Haozhe Chen, Weiming Zhang, Kunlin Liu, Kejiang Chen et al.** · 2021-10-19

<details>
<summary>Abstract</summary>

As an effective method for intellectual property (IP) protection, model watermarking technology has been applied on a wide variety of deep neural networks (DNN), including speech classification models. However, how to design a black-box watermarking scheme for automatic speech recognition (ASR) models is still an unsolved problem, which is a significant demand for protecting remote ASR Application Programming Interface (API) deployed in cloud servers. Due to conditional independence assumption and label-detection-based evasion attack risk of ASR models, the black-box model watermarking scheme for speech classification models cannot apply to ASR models. In this paper, we propose the first black-box model watermarking framework for protecting the IP of ASR models. Specifically, we synthesize trigger audios by spreading the speech clips of model owners over the entire input audios and labeling the trigger audios with the stego texts, which hides the authorship information with linguistic steganography. Experiments on the state-of-the-art open-source ASR system DeepSpeech demonstrate the feasibility of the proposed watermarking scheme, which is robust against five kinds of attacks and has little impact on accuracy.

</details>

### [Personalized Speech Enhancement: New Models and Comprehensive Evaluation](2110.09625.md)
**Sefik Emre Eskimez, Takuya Yoshioka, Huaming Wang, Xiaofei Wang et al.** · 2021-10-18

<details>
<summary>Abstract</summary>

Personalized speech enhancement (PSE) models utilize additional cues, such as speaker embeddings like d-vectors, to remove background noise and interfering speech in real-time and thus improve the speech quality of online video conferencing systems for various acoustic scenarios. In this work, we propose two neural networks for PSE that achieve superior performance to the previously proposed VoiceFilter. In addition, we create test sets that capture a variety of scenarios that users can encounter during video conferencing. Furthermore, we propose a new metric to measure the target speaker over-suppression (TSOS) problem, which was not sufficiently investigated before despite its critical importance in deployment. Besides, we propose multi-task training with a speech recognition back-end. Our results show that the proposed models can yield better speech recognition accuracy, speech intelligibility, and perceptual quality than the baseline models, and the multi-task training can alleviate the TSOS issue in addition to improving the speech recognition accuracy.

</details>

### [Automatic Learning of Subword Dependent Model Scales](2110.09324.md)
**Felix Meyer, Wilfried Michel, Mohammad Zeineldeen, Ralf Schlüter et al.** · 2021-10-18

<details>
<summary>Abstract</summary>

To improve the performance of state-of-the-art automatic speech recognition systems it is common practice to include external knowledge sources such as language models or prior corrections. This is usually done via log-linear model combination using separate scaling parameters for each model. Typically these parameters are manually optimized on some held-out data. In this work we propose to optimize these scaling parameters via automatic differentiation and stochastic gradient decent similar to the neural network model parameters. We show on the LibriSpeech (LBS) and Switchboard (SWB) corpora that the model scales for a combination of attentionbased encoder-decoder acoustic model and language model can be learned as effectively as with manual tuning. We further extend this approach to subword dependent model scales which could not be tuned manually which leads to 7% improvement on LBS and 3% on SWB. We also show that joint training of scales and model parameters is possible and gives additional 6% improvement on LBS.

</details>

### [Intent Classification Using Pre-trained Language Agnostic Embeddings For Low Resource Languages](2110.09264.md)
**Hemant Yadav, Akshat Gupta, Sai Krishna Rallabandi, Alan W Black et al.** · 2021-10-18

<details>
<summary>Abstract</summary>

Building Spoken Language Understanding (SLU) systems that do not rely on language specific Automatic Speech Recognition (ASR) is an important yet less explored problem in language processing. In this paper, we present a comparative study aimed at employing a pre-trained acoustic model to perform SLU in low resource scenarios. Specifically, we use three different embeddings extracted using Allosaurus, a pre-trained universal phone decoder: (1) Phone (2) Panphone, and (3) Allo embeddings. These embeddings are then used in identifying the spoken intent. We perform experiments across three different languages: English, Sinhala, and Tamil each with different data sizes to simulate high, medium, and low resource scenarios. Our system improves on the state-of-the-art (SOTA) intent classification accuracy by approximately 2.11% for Sinhala and 7.00% for Tamil and achieves competitive results on English. Furthermore, we present a quantitative analysis of how the performance scales with the number of training examples used per intent.

</details>

### [Efficient Sequence Training of Attention Models using Approximative Recombination](2110.09245.md)
**Nils-Philipp Wynands, Wilfried Michel, Jan Rosendahl, Ralf Schlüter et al.** · 2021-10-18

<details>
<summary>Abstract</summary>

Sequence discriminative training is a great tool to improve the performance of an automatic speech recognition system. It does, however, necessitate a sum over all possible word sequences, which is intractable to compute in practice. Current state-of-the-art systems with unlimited label context circumvent this problem by limiting the summation to an n-best list of relevant competing hypotheses obtained from beam search. This work proposes to perform (approximative) recombinations of hypotheses during beam search, if they share a common local history. The error that is incurred by the approximation is analyzed and it is shown that using this technique the effective beam size can be increased by several orders of magnitude without significantly increasing the computational requirements. Lastly, it is shown that this technique can be used to effectively perform sequence discriminative training for attention-based encoder-decoder acoustic models on the LibriSpeech task.

</details>

### [Analysis of French Phonetic Idiosyncrasies for Accent Recognition](2110.09179.md)
**Pierre Berjon, Avishek Nag, Soumyabrata Dev** · 2021-10-18

<details>
<summary>Abstract</summary>

Speech recognition systems have made tremendous progress since the last few decades. They have developed significantly in identifying the speech of the speaker. However, there is a scope of improvement in speech recognition systems in identifying the nuances and accents of a speaker. It is known that any specific natural language may possess at least one accent. Despite the identical word phonemic composition, if it is pronounced in different accents, we will have sound waves, which are different from each other. Differences in pronunciation, in accent and intonation of speech in general, create one of the most common problems of speech recognition. If there are a lot of accents in language we should create the acoustic model for each separately. We carry out a systematic analysis of the problem in the accurate classification of accents. We use traditional machine learning techniques and convolutional neural networks, and show that the classical techniques are not sufficiently efficient to solve this problem. Using spectrograms of speech signals, we propose a multi-class classification framework for accent recognition. In this paper, we focus our attention on the French accent. We also identify its limitation by understanding the impact of French idiosyncrasies on its spectrograms.

</details>

### [Similarity-and-Independence-Aware Beamformer with Iterative Casting and Boost Start for Target Source Extraction Using Reference](2110.09019.md)
**Atsuo Hiroe** · 2021-10-18

<details>
<summary>Abstract</summary>

Target source extraction is significant for improving human speech intelligibility and the speech recognition performance of computers. This study describes a method for target source extraction, called the similarity-and-independence-aware beamformer (SIBF). The SIBF extracts the target source using a rough magnitude spectrogram as the reference signal. The advantage of the SIBF is that it can obtain a more accurate signal than the spectrogram generated by target-enhancing methods such as speech enhancement based on deep neural networks. For the extraction, we extend the framework of deflationary independent component analysis (ICA) by considering the similarities between the reference and extracted target sources, in addition to the mutual independence of all the potential sources. To solve the extraction problem by maximum-likelihood estimation, we introduce three source models that can reflect the similarities. The major contributions of this study are as follows. First, the extraction performance is improved using two methods, namely boost start for faster convergence and iterative casting for generating a more accurate reference. The effectiveness of these methods is verified through experiments using the CHiME3 dataset. Second, a concept of a fixed point pertaining to accuracy is developed. This concept facilitates understanding the relationship between the reference and SIBF output in terms of accuracy. Third, a unified formulation of the SIBF and mask-based beamformer is realized to apply the expertise of conventional BFs to the SIBF. The findings of this study can also improve the performance of the SIBF and promote research on ICA and conventional beamformers. Index Terms: beamformer, independent component analysis, source separation, speech enhancement, target source extraction

</details>

### [A Unified Speaker Adaptation Approach for ASR](2110.08545.md)
**Yingzhu Zhao, Chongjia Ni, Cheung-Chi Leung, Shafiq Joty et al.** · 2021-10-16

<details>
<summary>Abstract</summary>

Transformer models have been used in automatic speech recognition (ASR) successfully and yields state-of-the-art results. However, its performance is still affected by speaker mismatch between training and test data. Further finetuning a trained model with target speaker data is the most natural approach for adaptation, but it takes a lot of compute and may cause catastrophic forgetting to the existing speakers. In this work, we propose a unified speaker adaptation approach consisting of feature adaptation and model adaptation. For feature adaptation, we employ a speaker-aware persistent memory model which generalizes better to unseen test speakers by making use of speaker i-vectors to form a persistent memory. For model adaptation, we use a novel gradual pruning method to adapt to target speakers without changing the model architecture, which to the best of our knowledge, has never been explored in ASR. Specifically, we gradually prune less contributing parameters on model encoder to a certain sparsity level, and use the pruned parameters for adaptation, while freezing the unpruned parameters to keep the original model performance. We conduct experiments on the Librispeech dataset. Our proposed approach brings relative 2.74-6.52% word error rate (WER) reduction on general speaker adaptation. On target speaker adaptation, our method outperforms the baseline with up to 20.58% relative WER reduction, and surpasses the finetuning method by up to relative 2.54%. Besides, with extremely low-resource adaptation data (e.g., 1 utterance), our method could improve the WER by relative 6.53% with only a few epochs of training.

</details>

### [Omni-sparsity DNN: Fast Sparsity Optimization for On-Device Streaming E2E ASR via Supernet](2110.08352.md)
**Haichuan Yang, Yuan Shangguan, Dilin Wang, Meng Li et al.** · 2021-10-15

<details>
<summary>Abstract</summary>

From wearables to powerful smart devices, modern automatic speech recognition (ASR) models run on a variety of edge devices with different computational budgets. To navigate the Pareto front of model accuracy vs model size, researchers are trapped in a dilemma of optimizing model accuracy by training and fine-tuning models for each individual edge device while keeping the training GPU-hours tractable. In this paper, we propose Omni-sparsity DNN, where a single neural network can be pruned to generate optimized model for a large range of model sizes. We develop training strategies for Omni-sparsity DNN that allows it to find models along the Pareto front of word-error-rate (WER) vs model size while keeping the training GPU-hours to no more than that of training one singular model. We demonstrate the Omni-sparsity DNN with streaming E2E ASR models. Our results show great saving on training time and resources with similar or better accuracy on LibriSpeech compared to individually pruned sparse models: 2%-6.6% better WER on Test-other.

</details>

### [Multilingual Speech Recognition using Knowledge Transfer across Learning Processes](2110.07909.md)
**Rimita Lahiri, Kenichi Kumatani, Eric Sun, Yao Qian** · 2021-10-15

<details>
<summary>Abstract</summary>

Multilingual end-to-end(E2E) models have shown a great potential in the expansion of the language coverage in the realm of automatic speech recognition(ASR). In this paper, we aim to enhance the multilingual ASR performance in two ways, 1)studying the impact of feeding a one-hot vector identifying the language, 2)formulating the task with a meta-learning objective combined with self-supervised learning (SSL). We associate every language with a distinct task manifold and attempt to improve the performance by transferring knowledge across learning processes itself as compared to transferring through final model parameters. We employ this strategy on a dataset comprising of 6 languages for an in-domain ASR task, by minimizing an objective related to expected gradient path length. Experimental results reveal the best pre-training strategy resulting in 3.55% relative reduction in overall WER. A combination of LEAP and SSL yields 3.51% relative reduction in overall WER when using language ID.

</details>

### [Advances and Challenges in Deep Lip Reading](2110.07879.md)
**Marzieh Oghbaie, Arian Sabaghi, Kooshan Hashemifard, Mohammad Akbari** · 2021-10-15

<details>
<summary>Abstract</summary>

Driven by deep learning techniques and large-scale datasets, recent years have witnessed a paradigm shift in automatic lip reading. While the main thrust of Visual Speech Recognition (VSR) was improving accuracy of Audio Speech Recognition systems, other potential applications, such as biometric identification, and the promised gains of VSR systems, have motivated extensive efforts on developing the lip reading technology. This paper provides a comprehensive survey of the state-of-the-art deep learning based VSR research with a focus on data challenges, task-specific complications, and the corresponding solutions. Advancements in these directions will expedite the transformation of silent speech interface from theory to practice. We also discuss the main modules of a VSR pipeline and the influential datasets. Finally, we introduce some typical VSR application concerns and impediments to real-world scenarios as well as future research directions.

</details>

### [Sub-word Level Lip Reading With Visual Attention](2110.07603.md)
**K R Prajwal, Triantafyllos Afouras, Andrew Zisserman** · 2021-10-14

<details>
<summary>Abstract</summary>

The goal of this paper is to learn strong lip reading models that can recognise speech in silent videos. Most prior works deal with the open-set visual speech recognition problem by adapting existing automatic speech recognition techniques on top of trivially pooled visual features. Instead, in this paper we focus on the unique challenges encountered in lip reading and propose tailored solutions. To this end, we make the following contributions: (1) we propose an attention-based pooling mechanism to aggregate visual speech representations; (2) we use sub-word units for lip reading for the first time and show that this allows us to better model the ambiguities of the task; (3) we propose a model for Visual Speech Detection (VSD), trained on top of the lip reading network. Following the above, we obtain state-of-the-art results on the challenging LRS2 and LRS3 benchmarks when training on public datasets, and even surpass models trained on large-scale industrial datasets by using an order of magnitude less data. Our best model achieves 22.6% word error rate on the LRS2 dataset, a performance unprecedented for lip reading models, significantly reducing the performance gap between lip reading and automatic speech recognition. Moreover, on the AVA-ActiveSpeaker benchmark, our VSD model surpasses all visual-only baselines and even outperforms several recent audio-visual methods.

</details>

### [M2MeT: The ICASSP 2022 Multi-Channel Multi-Party Meeting Transcription Challenge](2110.07393.md)
**Fan Yu, Shiliang Zhang, Yihui Fu, Lei Xie et al.** · 2021-10-14

<details>
<summary>Abstract</summary>

Recent development of speech processing, such as speech recognition, speaker diarization, etc., has inspired numerous applications of speech technologies. The meeting scenario is one of the most valuable and, at the same time, most challenging scenarios for the deployment of speech technologies. Specifically, two typical tasks, speaker diarization and multi-speaker automatic speech recognition have attracted much attention recently. However, the lack of large public meeting data has been a major obstacle for the advancement of the field. Therefore, we make available the AliMeeting corpus, which consists of 120 hours of recorded Mandarin meeting data, including far-field data collected by 8-channel microphone array as well as near-field data collected by headset microphone. Each meeting session is composed of 2-4 speakers with different speaker overlap ratio, recorded in rooms with different size. Along with the dataset, we launch the ICASSP 2022 Multi-channel Multi-party Meeting Transcription Challenge (M2MeT) with two tracks, namely speaker diarization and multi-speaker ASR, aiming to provide a common testbed for meeting rich transcription and promote reproducible research in this field. In this paper we provide a detailed introduction of the AliMeeting dateset, challenge rules, evaluation methods and baseline systems.

</details>

### [Identifying Introductions in Podcast Episodes from Automatically Generated Transcripts](2110.07096.md)
**Elise Jing, Kristiana Schneck, Dennis Egan, Scott A. Waterman** · 2021-10-14

<details>
<summary>Abstract</summary>

As the volume of long-form spoken-word content such as podcasts explodes, many platforms desire to present short, meaningful, and logically coherent segments extracted from the full content. Such segments can be consumed by users to sample content before diving in, as well as used by the platform to promote and recommend content. However, little published work is focused on the segmentation of spoken-word content, where the errors (noise) in transcripts generated by automatic speech recognition (ASR) services poses many challenges. Here we build a novel dataset of complete transcriptions of over 400 podcast episodes, in which we label the position of introductions in each episode. These introductions contain information about the episodes' topics, hosts, and guests, providing a valuable summary of the episode content, as it is created by the authors. We further augment our dataset with word substitutions to increase the amount of available training data. We train three Transformer models based on the pre-trained BERT and different augmentation strategies, which achieve significantly better performance compared with a static embedding model, showing that it is possible to capture generalized, larger-scale structural information from noisy, loosely-organized speech data. This is further demonstrated through an analysis of the models' inner architecture. Our methods and dataset can be used to facilitate future work on the structure-based segmentation of spoken-word content.

</details>

### [Continual learning using lattice-free MMI for speech recognition](2110.07055.md)
**Hossein Hadian, Arseniy Gorin** · 2021-10-13

<details>
<summary>Abstract</summary>

Continual learning (CL), or domain expansion, recently became a popular topic for automatic speech recognition (ASR) acoustic modeling because practical systems have to be updated frequently in order to work robustly on types of speech not observed during initial training. While sequential adaptation allows tuning a system to a new domain, it may result in performance degradation on the old domains due to catastrophic forgetting. In this work we explore regularization-based CL for neural network acoustic models trained with the lattice-free maximum mutual information (LF-MMI) criterion. We simulate domain expansion by incrementally adapting the acoustic model on different public datasets that include several accents and speaking styles. We investigate two well-known CL techniques, elastic weight consolidation (EWC) and learning without forgetting (LWF), which aim to reduce forgetting by preserving model weights or network outputs. We additionally introduce a sequence-level LWF regularization, which exploits posteriors from the denominator graph of LF-MMI to further reduce forgetting. Empirical results show that the proposed sequence-level LWF can improve the best average word error rate across all domains by up to 9.4% relative compared with using regular LWF.

</details>

### [On Language Model Integration for RNN Transducer based Speech Recognition](2110.06841.md)
**Wei Zhou, Zuoyun Zheng, Ralf Schlüter, Hermann Ney** · 2021-10-13

<details>
<summary>Abstract</summary>

The mismatch between an external language model (LM) and the implicitly learned internal LM (ILM) of RNN-Transducer (RNN-T) can limit the performance of LM integration such as simple shallow fusion. A Bayesian interpretation suggests to remove this sequence prior as ILM correction. In this work, we study various ILM correction-based LM integration methods formulated in a common RNN-T framework. We provide a decoding interpretation on two major reasons for performance improvement with ILM correction, which is further experimentally verified with detailed analysis. We also propose an exact-ILM training framework by extending the proof given in the hybrid autoregressive transducer, which enables a theoretical justification for other ILM approaches. Systematic comparison is conducted for both in-domain and cross-domain evaluation on the Librispeech and TED-LIUM Release 2 corpora, respectively. Our proposed exact-ILM training can further improve the best ILM method.

</details>

### [Perception Point: Identifying Critical Learning Periods in Speech for Bilingual Networks](2110.06507.md)
**Anuj Saraswat, Mehar Bhatia, Yaman Kumar Singla, Changyou Chen et al.** · 2021-10-13

<details>
<summary>Abstract</summary>

Recent studies in speech perception have been closely linked to fields of cognitive psychology, phonology, and phonetics in linguistics. During perceptual attunement, a critical and sensitive developmental trajectory has been examined in bilingual and monolingual infants where they can best discriminate common phonemes. In this paper, we compare and identify these cognitive aspects on deep neural-based visual lip-reading models. We conduct experiments on the two most extensive public visual speech recognition datasets for English and Mandarin. Through our experimental results, we observe a strong correlation between these theories in cognitive psychology and our unique modeling. We inspect how these computational models develop similar phases in speech perception and acquisitions.

</details>

### [Prompt-tuning in ASR systems for efficient domain-adaptation](2110.06502.md)
**Saket Dingliwal, Ashish Shenoy, Sravan Bodapati, Ankur Gandhe et al.** · 2021-10-13

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have found their use in numerous industrial applications in very diverse domains. Since domain-specific systems perform better than their generic counterparts on in-domain evaluation, the need for memory and compute-efficient domain adaptation is obvious. Particularly, adapting parameter-heavy transformer-based language models used for rescoring ASR hypothesis is challenging. In this work, we overcome the problem using prompt-tuning, a methodology that trains a small number of domain token embedding parameters to prime a transformer-based LM to a particular domain. With just a handful of extra parameters per domain, we achieve much better perplexity scores over the baseline of using an unadapted LM. Despite being parameter-efficient, these improvements are comparable to those of fully-fine-tuned models with hundreds of millions of parameters. We replicate our findings in perplexity numbers to Word Error Rate in a domain-specific ASR system for one such domain.

</details>

### [All-neural beamformer for continuous speech separation](2110.06428.md)
**Zhuohuang Zhang, Takuya Yoshioka, Naoyuki Kanda, Zhuo Chen et al.** · 2021-10-13

<details>
<summary>Abstract</summary>

Continuous speech separation (CSS) aims to separate overlapping voices from a continuous influx of conversational audio containing an unknown number of utterances spoken by an unknown number of speakers. A common application scenario is transcribing a meeting conversation recorded by a microphone array. Prior studies explored various deep learning models for time-frequency mask estimation, followed by a minimum variance distortionless response (MVDR) filter to improve the automatic speech recognition (ASR) accuracy. The performance of these methods is fundamentally upper-bounded by MVDR's spatial selectivity. Recently, the all deep learning MVDR (ADL-MVDR) model was proposed for neural beamforming and demonstrated superior performance in a target speech extraction task using pre-segmented input. In this paper, we further adapt ADL-MVDR to the CSS task with several enhancements to enable end-to-end neural beamforming. The proposed system achieves significant word error rate reduction over a baseline spectral masking system on the LibriCSS dataset. Moreover, the proposed neural beamformer is shown to be comparable to a state-of-the-art MVDR-based system in real meeting transcription tasks, including AMI, while showing potentials to further simplify the runtime implementation and reduce the system latency with frame-wise processing.

</details>

### [Independence-based Joint Dereverberation and Separation with Neural Source Model](2110.06545.md)
**Kohei Saijo, Robin Scheibler** · 2021-10-13

<details>
<summary>Abstract</summary>

We propose an independence-based joint dereverberation and separation method with a neural source model. We introduce a neural network in the framework of time-decorrelation iterative source steering, which is an extension of independent vector analysis to joint dereverberation and separation. The network is trained in an end-to-end manner with a permutation invariant loss on the time-domain separation output signals. Our proposed method can be applied in any situation with at least as many microphones as sources, regardless of their number. In experiments, we demonstrate that our method results in high performance in terms of both speech quality metrics and word error rate (WER), even for mixtures with a different number of speakers than training. Furthermore, the model, trained on synthetic mixtures, without any modifications, greatly reduces the WER on the recorded dataset LibriCSS.

</details>

### [Speech Summarization using Restricted Self-Attention](2110.06263.md)
**Roshan Sharma, Shruti Palaskar, Alan W Black, Florian Metze** · 2021-10-12

<details>
<summary>Abstract</summary>

Speech summarization is typically performed by using a cascade of speech recognition and text summarization models. End-to-end modeling of speech summarization models is challenging due to memory and compute constraints arising from long input audio sequences. Recent work in document summarization has inspired methods to reduce the complexity of self-attentions, which enables transformer models to handle long sequences. In this work, we introduce a single model optimized end-to-end for speech summarization. We apply the restricted self-attention technique from text-based models to speech models to address the memory and compute constraints. We demonstrate that the proposed model learns to directly summarize speech for the How-2 corpus of instructional videos. The proposed end-to-end model outperforms the previously proposed cascaded model by 3 points absolute on ROUGE. Further, we consider the spoken language understanding task of predicting concepts from speech inputs and show that the proposed end-to-end model outperforms the cascade model by 4 points absolute F-1.

</details>

### [Multi-Modal Pre-Training for Automated Speech Recognition](2110.09890.md)
**David M. Chan, Shalini Ghosh, Debmalya Chakrabarty, Björn Hoffmeister** · 2021-10-12

<details>
<summary>Abstract</summary>

Traditionally, research in automated speech recognition has focused on local-first encoding of audio representations to predict the spoken phonemes in an utterance. Unfortunately, approaches relying on such hyper-local information tend to be vulnerable to both local-level corruption (such as audio-frame drops, or loud noises) and global-level noise (such as environmental noise, or background noise) that has not been seen during training. In this work, we introduce a novel approach which leverages a self-supervised learning technique based on masked language modeling to compute a global, multi-modal encoding of the environment in which the utterance occurs. We then use a new deep-fusion framework to integrate this global context into a traditional ASR method, and demonstrate that the resulting method can outperform baseline methods by up to 7% on Librispeech; gains on internal datasets range from 6% (on larger models) to 45% (on smaller models).

</details>

### [Word Order Does Not Matter For Speech Recognition](2110.05994.md)
**Vineel Pratap, Qiantong Xu, Tatiana Likhomanenko, Gabriel Synnaeve et al.** · 2021-10-12

<details>
<summary>Abstract</summary>

In this paper, we study training of automatic speech recognition system in a weakly supervised setting where the order of words in transcript labels of the audio training data is not known. We train a word-level acoustic model which aggregates the distribution of all output frames using LogSumExp operation and uses a cross-entropy loss to match with the ground-truth words distribution. Using the pseudo-labels generated from this model on the training set, we then train a letter-based acoustic model using Connectionist Temporal Classification loss. Our system achieves 2.3%/4.6% on test-clean/test-other subsets of LibriSpeech, which closely matches with the supervised baseline's performance.

</details>

### [Improving Character Error Rate Is Not Equal to Having Clean Speech: Speech Enhancement for ASR Systems with Black-box Acoustic Models](2110.05968.md)
**Ryosuke Sawata, Yosuke Kashiwagi, Shusuke Takahashi** · 2021-10-12

<details>
<summary>Abstract</summary>

A deep neural network (DNN)-based speech enhancement (SE) aiming to maximize the performance of an automatic speech recognition (ASR) system is proposed in this paper. In order to optimize the DNN-based SE model in terms of the character error rate (CER), which is one of the metric to evaluate the ASR system and generally non-differentiable, our method uses two DNNs: one for speech processing and one for mimicking the output CERs derived through an acoustic model (AM). Then both of DNNs are alternately optimized in the training phase. Even if the AM is a black-box, e.g., like one provided by a third-party, the proposed method enables the DNN-based SE model to be optimized in terms of the CER since the DNN mimicking the AM is differentiable. Consequently, it becomes feasible to build CER-centric SE model that has no negative effect, e.g., additional calculation cost and changing network architecture, on the inference phase since our method is merely a training scheme for the existing DNN-based methods. Experimental results show that our method improved CER by 8.8% relative derived through a black-box AM although certain noise levels are kept.

</details>

### [Partial Variable Training for Efficient On-Device Federated Learning](2110.05607.md)
**Tien-Ju Yang, Dhruv Guliani, Françoise Beaufays, Giovanni Motta** · 2021-10-11

<details>
<summary>Abstract</summary>

This paper aims to address the major challenges of Federated Learning (FL) on edge devices: limited memory and expensive communication. We propose a novel method, called Partial Variable Training (PVT), that only trains a small subset of variables on edge devices to reduce memory usage and communication cost. With PVT, we show that network accuracy can be maintained by utilizing more local training steps and devices, which is favorable for FL involving a large population of devices. According to our experiments on two state-of-the-art neural networks for speech recognition and two different datasets, PVT can reduce memory usage by up to 1.9$\times$ and communication cost by up to 593$\times$ while attaining comparable accuracy when compared with full network training.

</details>

### [SRU++: Pioneering Fast Recurrence with Attention for Speech Recognition](2110.05571.md)
**Jing Pan, Tao Lei, Kwangyoun Kim, Kyu Han et al.** · 2021-10-11

<details>
<summary>Abstract</summary>

The Transformer architecture has been well adopted as a dominant architecture in most sequence transduction tasks including automatic speech recognition (ASR), since its attention mechanism excels in capturing long-range dependencies. While models built solely upon attention can be better parallelized than regular RNN, a novel network architecture, SRU++, was recently proposed. By combining the fast recurrence and attention mechanism, SRU++ exhibits strong capability in sequence modeling and achieves near-state-of-the-art results in various language modeling and machine translation tasks with improved compute efficiency. In this work, we present the advantages of applying SRU++ in ASR tasks by comparing with Conformer across multiple ASR benchmarks and study how the benefits can be generalized to long-form speech inputs. On the popular LibriSpeech benchmark, our SRU++ model achieves 2.0% / 4.7% WER on test-clean / test-other, showing competitive performances compared with the state-of-the-art Conformer encoder under the same set-up. Specifically, SRU++ can surpass Conformer on long-form speech input with a large margin, based on our analysis.

</details>

### [Evaluating User Perception of Speech Recognition System Quality with Semantic Distance Metric](2110.05376.md)
**Suyoun Kim, Duc Le, Weiyi Zheng, Tarun Singh et al.** · 2021-10-11

<details>
<summary>Abstract</summary>

Measuring automatic speech recognition (ASR) system quality is critical for creating user-satisfying voice-driven applications. Word Error Rate (WER) has been traditionally used to evaluate ASR system quality; however, it sometimes correlates poorly with user perception/judgement of transcription quality. This is because WER weighs every word equally and does not consider semantic correctness which has a higher impact on user perception. In this work, we propose evaluating ASR output hypotheses quality with SemDist that can measure semantic correctness by using the distance between the semantic vectors of the reference and hypothesis extracted from a pre-trained language model. Our experimental results of 71K and 36K user annotated ASR output quality show that SemDist achieves higher correlation with user perception than WER. We also show that SemDist has higher correlation with downstream Natural Language Understanding (NLU) tasks than WER.

</details>

### [Interactive Feature Fusion for End-to-End Noise-Robust Speech Recognition](2110.05267.md)
**Yuchen Hu, Nana Hou, Chen Chen, Eng Siong Chng** · 2021-10-11

<details>
<summary>Abstract</summary>

Speech enhancement (SE) aims to suppress the additive noise from a noisy speech signal to improve the speech's perceptual quality and intelligibility. However, the over-suppression phenomenon in the enhanced speech might degrade the performance of downstream automatic speech recognition (ASR) task due to the missing latent information. To alleviate such problem, we propose an interactive feature fusion network (IFF-Net) for noise-robust speech recognition to learn complementary information from the enhanced feature and original noisy feature. Experimental results show that the proposed method achieves absolute word error rate (WER) reduction of 4.1% over the best baseline on RATS Channel-A corpus. Our further analysis indicates that the proposed IFF-Net can complement some missing information in the over-suppressed enhanced feature.

</details>

### [A Comparative Study on Non-Autoregressive Modelings for Speech-to-Text Generation](2110.05249.md)
**Yosuke Higuchi, Nanxin Chen, Yuya Fujita, Hirofumi Inaguma et al.** · 2021-10-11

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) models simultaneously generate multiple outputs in a sequence, which significantly reduces the inference speed at the cost of accuracy drop compared to autoregressive baselines. Showing great potential for real-time applications, an increasing number of NAR models have been explored in different fields to mitigate the performance gap against AR models. In this work, we conduct a comparative study of various NAR modeling methods for end-to-end automatic speech recognition (ASR). Experiments are performed in the state-of-the-art setting using ESPnet. The results on various tasks provide interesting findings for developing an understanding of NAR ASR, such as the accuracy-speed trade-off and robustness against long-form utterances. We also show that the techniques can be combined for further improvement and applied to NAR end-to-end speech translation. All the implementations are publicly available to encourage further research in NAR speech processing.

</details>

### [K-Wav2vec 2.0: Automatic Speech Recognition based on Joint Decoding of Graphemes and Syllables](2110.05172.md)
**Jounghee Kim, Pilsung Kang** · 2021-10-11

<details>
<summary>Abstract</summary>

Wav2vec 2.0 is an end-to-end framework of self-supervised learning for speech representation that is successful in automatic speech recognition (ASR), but most of the work on the topic has been developed with a single language: English. Therefore, it is unclear whether the self-supervised framework is effective in recognizing other languages with different writing systems, such as Korean which uses the Hangul having a unique writing system. In this paper, we present K-Wav2Vec 2.0, which is a modified version of Wav2vec 2.0 designed for Korean automatic speech recognition by exploring and optimizing various factors of the original Wav2vec 2.0. In fine-tuning, we propose a multi-task hierarchical architecture to reflect the Korean writing structure. Moreover, a joint decoder is applied to alleviate the problem of words existing outside of the vocabulary. In pre-training, we attempted the cross-lingual transfer of the pre-trained model by further pre-training the English Wav2vec 2.0 on a Korean dataset, considering limited resources. Our experimental results demonstrate that the proposed method yields the best performance on both Korean ASR datasets: Ksponspeech (a large-scale Korean speech corpus) and Clovacall (a call-based dialog corpus). Further pre-training is also effective in language adaptation, leading to large improvements without additional data.

</details>

### [Advancing Momentum Pseudo-Labeling with Conformer and Initialization Strategy](2110.04948.md)
**Yosuke Higuchi, Niko Moritz, Jonathan Le Roux, Takaaki Hori** · 2021-10-11

<details>
<summary>Abstract</summary>

Pseudo-labeling (PL), a semi-supervised learning (SSL) method where a seed model performs self-training using pseudo-labels generated from untranscribed speech, has been shown to enhance the performance of end-to-end automatic speech recognition (ASR). Our prior work proposed momentum pseudo-labeling (MPL), which performs PL-based SSL via an interaction between online and offline models, inspired by the mean teacher framework. MPL achieves remarkable results on various semi-supervised settings, showing robustness to variations in the amount of data and domain mismatch severity. However, there is further room for improving the seed model used to initialize the MPL training, as it is in general critical for a PL-based method to start training from high-quality pseudo-labels. To this end, we propose to enhance MPL by (1) introducing the Conformer architecture to boost the overall recognition accuracy and (2) exploiting iterative pseudo-labeling with a language model to improve the seed model before applying MPL. The experimental results demonstrate that the proposed approaches effectively improve MPL performance, outperforming other PL-based methods. We also present in-depth investigations to make our improvements effective, e.g., with regard to batch normalization typically used in Conformer and LM quality.

</details>

### [Wav2vec-Switch: Contrastive Learning from Original-noisy Speech Pairs for Robust Speech Recognition](2110.04934.md)
**Yiming Wang, Jinyu Li, Heming Wang, Yao Qian et al.** · 2021-10-11

<details>
<summary>Abstract</summary>

The goal of self-supervised learning (SSL) for automatic speech recognition (ASR) is to learn good speech representations from a large amount of unlabeled speech for the downstream ASR task. However, most SSL frameworks do not consider noise robustness which is crucial for real-world applications. In this paper we propose wav2vec-Switch, a method to encode noise robustness into contextualized representations of speech via contrastive learning. Specifically, we feed original-noisy speech pairs simultaneously into the wav2vec 2.0 network. In addition to the existing contrastive learning task, we switch the quantized representations of the original and noisy speech as additional prediction targets of each other. By doing this, it enforces the network to have consistent predictions for the original and noisy speech, thus allows to learn contextualized representation with noise robustness. Our experiments on synthesized and real noisy data show the effectiveness of our method: it achieves 2.9--4.9% relative word error rate (WER) reduction on the synthesized noisy LibriSpeech data without deterioration on the original data, and 5.7% on CHiME-4 real 1-channel noisy data compared to a data augmentation baseline even with a strong language model for decoding. Our results on CHiME-4 can match or even surpass those with well-designed speech enhancement components.

</details>

### [Have best of both worlds: two-pass hybrid and E2E cascading framework for speech recognition](2110.04891.md)
**Guoli Ye, Vadim Mazalov, Jinyu Li, Yifan Gong** · 2021-10-10

<details>
<summary>Abstract</summary>

Hybrid and end-to-end (E2E) systems have their individual advantages, with different error patterns in the speech recognition results. By jointly modeling audio and text, the E2E model performs better in matched scenarios and scales well with a large amount of paired audio-text training data. The modularized hybrid model is easier for customization, and better to make use of a massive amount of unpaired text data. This paper proposes a two-pass hybrid and E2E cascading (HEC) framework to combine the hybrid and E2E model in order to take advantage of both sides, with hybrid in the first pass and E2E in the second pass. We show that the proposed system achieves 8-10% relative word error rate reduction with respect to each individual system. More importantly, compared with the pure E2E system, we show the proposed system has the potential to keep the advantages of hybrid system, e.g., customization and segmentation capabilities. We also show the second pass E2E model in HEC is robust with respect to the change in the first pass hybrid model.

</details>

### [Long Expressive Memory for Sequence Modeling](2110.04744.md)
**T. Konstantin Rusch, Siddhartha Mishra, N. Benjamin Erichson, Michael W. Mahoney** · 2021-10-10

<details>
<summary>Abstract</summary>

We propose a novel method called Long Expressive Memory (LEM) for learning long-term sequential dependencies. LEM is gradient-based, it can efficiently process sequential tasks with very long-term dependencies, and it is sufficiently expressive to be able to learn complicated input-output maps. To derive LEM, we consider a system of multiscale ordinary differential equations, as well as a suitable time-discretization of this system. For LEM, we derive rigorous bounds to show the mitigation of the exploding and vanishing gradients problem, a well-known challenge for gradient-based recurrent sequential learning methods. We also prove that LEM can approximate a large class of dynamical systems to high accuracy. Our empirical results, ranging from image and time-series classification through dynamical systems prediction to speech recognition and language modeling, demonstrate that LEM outperforms state-of-the-art recurrent neural networks, gated recurrent units, and long short-term memory models.

</details>

### [An Exploration of Self-Supervised Pretrained Representations for End-to-End Speech Recognition](2110.04590.md)
**Xuankai Chang, Takashi Maekaku, Pengcheng Guo, Jing Shi et al.** · 2021-10-09

<details>
<summary>Abstract</summary>

Self-supervised pretraining on speech data has achieved a lot of progress. High-fidelity representation of the speech signal is learned from a lot of untranscribed data and shows promising performance. Recently, there are several works focusing on evaluating the quality of self-supervised pretrained representations on various tasks without domain restriction, e.g. SUPERB. However, such evaluations do not provide a comprehensive comparison among many ASR benchmark corpora. In this paper, we focus on the general applications of pretrained speech representations, on advanced end-to-end automatic speech recognition (E2E-ASR) models. We select several pretrained speech representations and present the experimental results on various open-source and publicly available corpora for E2E-ASR. Without any modification of the back-end model architectures or training strategy, some of the experiments with pretrained representations, e.g., WSJ, WSJ0-2mix with HuBERT, reach or outperform current state-of-the-art (SOTA) recognition performance. Moreover, we further explore more scenarios for whether the pretraining representations are effective, such as the cross-language or overlapped speech. The scripts, configuratons and the trained models have been released in ESPnet to let the community reproduce our experiments and improve them.

</details>

### [Data Augmentation with Locally-time Reversed Speech for Automatic Speech Recognition](2110.04511.md)
**Si-Ioi Ng, Tan Lee** · 2021-10-09

<details>
<summary>Abstract</summary>

Psychoacoustic studies have shown that locally-time reversed (LTR) speech, i.e., signal samples time-reversed within a short segment, can be accurately recognised by human listeners. This study addresses the question of how well a state-of-the-art automatic speech recognition (ASR) system would perform on LTR speech. The underlying objective is to explore the feasibility of deploying LTR speech in the training of end-to-end (E2E) ASR models, as an attempt to data augmentation for improving the recognition performance. The investigation starts with experiments to understand the effect of LTR speech on general-purpose ASR. LTR speech with reversed segment duration of 5 ms - 50 ms is rendered and evaluated. For ASR training data augmentation with LTR speech, training sets are created by combining natural speech with different partitions of LTR speech. The efficacy of data augmentation is confirmed by ASR results on speech corpora in various languages and speaking styles. ASR on LTR speech with reversed segment duration of 15 ms - 30 ms is found to have lower error rate than with other segment duration. Data augmentation with these LTR speech achieves satisfactory and consistent improvement on ASR performance.

</details>

### [Wav2vec-S: Semi-Supervised Pre-Training for Low-Resource ASR](2110.04484.md)
**Han Zhu, Li Wang, Jindong Wang, Gaofeng Cheng et al.** · 2021-10-09

<details>
<summary>Abstract</summary>

Self-supervised pre-training could effectively improve the performance of low-resource automatic speech recognition (ASR). However, existing self-supervised pre-training are task-agnostic, i.e., could be applied to various downstream tasks. Although it enlarges the scope of its application, the capacity of the pre-trained model is not fully utilized for the ASR task, and the learned representations may not be optimal for ASR. In this work, in order to build a better pre-trained model for low-resource ASR, we propose a pre-training approach called wav2vec-S, where we use task-specific semi-supervised pre-training to refine the self-supervised pre-trained model for the ASR task thus more effectively utilize the capacity of the pre-trained model to generate task-specific representations for ASR. Experiments show that compared to wav2vec 2.0, wav2vec-S only requires a marginal increment of pre-training time but could significantly improve ASR performance on in-domain, cross-domain and cross-lingual datasets. Average relative WER reductions are 24.5% and 6.6% for 1h and 10h fine-tuning, respectively. Furthermore, we show that semi-supervised pre-training could close the representation gap between the self-supervised pre-trained model and the corresponding fine-tuned model through canonical correlation analysis.

</details>

### [Exploring Heterogeneous Characteristics of Layers in ASR Models for More Efficient Training](2110.04267.md)
**Lillian Zhou, Dhruv Guliani, Andreas Kabel, Giovanni Motta et al.** · 2021-10-08

<details>
<summary>Abstract</summary>

Transformer-based architectures have been the subject of research aimed at understanding their overparameterization and the non-uniform importance of their layers. Applying these approaches to Automatic Speech Recognition, we demonstrate that the state-of-the-art Conformer models generally have multiple ambient layers. We study the stability of these layers across runs and model sizes, propose that group normalization may be used without disrupting their formation, and examine their correlation with model weight updates in each layer. Finally, we apply these findings to Federated Learning in order to improve the training procedure, by targeting Federated Dropout to layers by importance. This allows us to reduce the model size optimized by clients without quality degradation, and shows potential for future exploration.

</details>

### [SCaLa: Supervised Contrastive Learning for End-to-End Speech Recognition](2110.04187.md)
**Li Fu, Xiaoxiao Li, Runyu Wang, Lu Fan et al.** · 2021-10-08

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) models are usually trained to optimize the loss of the whole token sequence, while neglecting explicit phonemic-granularity supervision. This could result in recognition errors due to similar-phoneme confusion or phoneme reduction. To alleviate this problem, we propose a novel framework based on Supervised Contrastive Learning (SCaLa) to enhance phonemic representation learning for end-to-end ASR systems. Specifically, we extend the self-supervised Masked Contrastive Predictive Coding (MCPC) to a fully-supervised setting, where the supervision is applied in the following way. First, SCaLa masks variable-length encoder features according to phoneme boundaries given phoneme forced-alignment extracted from a pre-trained acoustic model; it then predicts the masked features via contrastive learning. The forced-alignment can provide phoneme labels to mitigate the noise introduced by positive-negative pairs in self-supervised MCPC. Experiments on reading and spontaneous speech datasets show that our proposed approach achieves 2.8 and 1.4 points Character Error Rate (CER) absolute reductions compared to the baseline, respectively.

</details>

### [Hierarchical Conditional End-to-End ASR with CTC and Multi-Granular Subword Units](2110.04109.md)
**Yosuke Higuchi, Keita Karube, Tetsuji Ogawa, Tetsunori Kobayashi** · 2021-10-08

<details>
<summary>Abstract</summary>

In end-to-end automatic speech recognition (ASR), a model is expected to implicitly learn representations suitable for recognizing a word-level sequence. However, the huge abstraction gap between input acoustic signals and output linguistic tokens makes it challenging for a model to learn the representations. In this work, to promote the word-level representation learning in end-to-end ASR, we propose a hierarchical conditional model that is based on connectionist temporal classification (CTC). Our model is trained by auxiliary CTC losses applied to intermediate layers, where the vocabulary size of each target subword sequence is gradually increased as the layer becomes close to the word-level output. Here, we make each level of sequence prediction explicitly conditioned on the previous sequences predicted at lower levels. With the proposed approach, we expect the proposed model to learn the word-level representations effectively by exploiting a hierarchy of linguistic structures. Experimental results on LibriSpeech-{100h, 960h} and TEDLIUM2 demonstrate that the proposed model improves over a standard CTC-based model and other competitive models from prior work. We further analyze the results to confirm the effectiveness of the intended representation learning with our model.

</details>

### [Improving Pseudo-label Training For End-to-end Speech Recognition Using Gradient Mask](2110.04056.md)
**Shaoshi Ling, Chen Shen, Meng Cai, Zejun Ma** · 2021-10-08

<details>
<summary>Abstract</summary>

In the recent trend of semi-supervised speech recognition, both self-supervised representation learning and pseudo-labeling have shown promising results. In this paper, we propose a novel approach to combine their ideas for end-to-end speech recognition model. Without any extra loss function, we utilize the Gradient Mask to optimize the model when training on pseudo-label. This method forces the speech recognition model to predict from the masked input to learn strong acoustic representation and make training robust to label noise. In our semi-supervised experiments, the method can improve the model performance when training on pseudo-label and our method achieved competitive results comparing with other semi-supervised approaches on the Librispeech 100 hours experiments.

</details>

### [Explaining the Attention Mechanism of End-to-End Speech Recognition Using Decision Trees](2110.03879.md)
**Yuanchao Wang, Wenji Du, Chenghao Cai, Yanyan Xu** · 2021-10-08

<details>
<summary>Abstract</summary>

The attention mechanism has largely improved the performance of end-to-end speech recognition systems. However, the underlying behaviours of attention is not yet clearer. In this study, we use decision trees to explain how the attention mechanism impact itself in speech recognition. The results indicate that attention levels are largely impacted by their previous states rather than the encoder and decoder patterns. Additionally, the default attention mechanism seems to put more weights on closer states, but behaves poorly on modelling long-term dependencies of attention states.

</details>

### [Input Length Matters: Improving RNN-T and MWER Training for Long-form Telephony Speech Recognition](2110.03841.md)
**Zhiyun Lu, Yanwei Pan, Thibault Doutre, Parisa Haghani et al.** · 2021-10-08

<details>
<summary>Abstract</summary>

End-to-end models have achieved state-of-the-art results on several automatic speech recognition tasks. However, they perform poorly when evaluated on long-form data, e.g., minutes long conversational telephony audio. One reason the model fails on long-form speech is that it has only seen short utterances during training. In this paper we study the effect of training utterance length on the word error rate (WER) for RNN-transducer (RNN-T) model. We compare two widely used training objectives, log loss (or RNN-T loss) and minimum word error rate (MWER) loss. We conduct experiments on telephony datasets in four languages. Our experiments show that for both losses, the WER on long-form speech reduces substantially as the training utterance length increases. The average relative WER gain is 15.7% for log loss and 8.8% for MWER loss. When training on short utterances, MWER loss leads to a lower WER than the log loss. Such difference between the two losses diminishes when the input length increases.

</details>

### [Streaming Transformer Transducer Based Speech Recognition Using Non-Causal Convolution](2110.05241.md)
**Yangyang Shi, Chunyang Wu, Dilin Wang, Alex Xiao et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

This paper improves the streaming transformer transducer for speech recognition by using non-causal convolution. Many works apply the causal convolution to improve streaming transformer ignoring the lookahead context. We propose to use non-causal convolution to process the center block and lookahead context separately. This method leverages the lookahead context in convolution and maintains similar training and decoding efficiency. Given the similar latency, using the non-causal convolution with lookahead context gives better accuracy than causal convolution, especially for open-domain dictation scenarios. Besides, this paper applies talking-head attention and a novel history context compression scheme to further improve the performance. The talking-head attention improves the multi-head self-attention by transferring information among different heads. The history context compression method introduces more extended history context compactly. On our in-house data, the proposed methods improve a small Emformer baseline with lookahead context by relative WERR 5.1\%, 14.5\%, 8.4\% on open-domain dictation, assistant general scenarios, and assistant calling scenarios, respectively.

</details>

### [Enabling On-Device Training of Speech Recognition Models with Federated Dropout](2110.03634.md)
**Dhruv Guliani, Lillian Zhou, Changwan Ryu, Tien-Ju Yang et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

Federated learning can be used to train machine learning models on the edge on local data that never leave devices, providing privacy by default. This presents a challenge pertaining to the communication and computation costs associated with clients' devices. These costs are strongly correlated with the size of the model being trained, and are significant for state-of-the-art automatic speech recognition models. We propose using federated dropout to reduce the size of client models while training a full-size model server-side. We provide empirical evidence of the effectiveness of federated dropout, and propose a novel approach to vary the dropout rate applied at each layer. Furthermore, we find that federated dropout enables a set of smaller sub-models within the larger model to independently have low word error rates, making it easier to dynamically adjust the size of the model deployed for inference.

</details>

### [Analyzing the Robustness of Unsupervised Speech Recognition](2110.03509.md)
**Guan-Ting Lin, Chan-Jan Hsu, Da-Rong Liu, Hung-Yi Lee et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

Unsupervised speech recognition (unsupervised ASR) aims to learn the ASR system with non-parallel speech and text corpus only. Wav2vec-U has shown promising results in unsupervised ASR by self-supervised speech representations coupled with Generative Adversarial Network (GAN) training, but the robustness of the unsupervised ASR framework is unknown. In this work, we further analyze the training robustness of unsupervised ASR on the domain mismatch scenarios in which the domains of unpaired speech and text are different. Three domain mismatch scenarios include: (1) using speech and text from different datasets, (2) utilizing noisy/spontaneous speech, and (3) adjusting the amount of speech and text data. We also quantify the degree of the domain mismatch by calculating the JS-divergence of phoneme n-gram between the transcription of speech and text. This metric correlates with the performance highly. Experimental results show that domain mismatch leads to inferior performance, but a self-supervised model pre-trained on the targeted speech domain can extract better representation to alleviate the performance drop.

</details>

### [Mandarin-English Code-switching Speech Recognition with Self-supervised Speech Representation Models](2110.03504.md)
**Liang-Hsuan Tseng, Yu-Kuan Fu, Heng-Jui Chang, Hung-yi Lee** · 2021-10-07

<details>
<summary>Abstract</summary>

Code-switching (CS) is common in daily conversations where more than one language is used within a sentence. The difficulties of CS speech recognition lie in alternating languages and the lack of transcribed data. Therefore, this paper uses the recently successful self-supervised learning (SSL) methods to leverage many unlabeled speech data without CS. We show that hidden representations of SSL models offer frame-level language identity even if the models are trained with English speech only. Jointly training CTC and language identification modules with self-supervised speech representations improves CS speech recognition performance. Furthermore, using multilingual speech data for pre-training obtains the best CS speech recognition.

</details>

### [WenetSpeech: A 10000+ Hours Multi-domain Mandarin Corpus for Speech Recognition](2110.03370.md)
**Binbin Zhang, Hang Lv, Pengcheng Guo, Qijie Shao et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

In this paper, we present WenetSpeech, a multi-domain Mandarin corpus consisting of 10000+ hours high-quality labeled speech, 2400+ hours weakly labeled speech, and about 10000 hours unlabeled speech, with 22400+ hours in total. We collect the data from YouTube and Podcast, which covers a variety of speaking styles, scenarios, domains, topics, and noisy conditions. An optical character recognition (OCR) based method is introduced to generate the audio/text segmentation candidates for the YouTube data on its corresponding video captions, while a high-quality ASR transcription system is used to generate audio/text pair candidates for the Podcast data. Then we propose a novel end-to-end label error detection approach to further validate and filter the candidates. We also provide three manually labelled high-quality test sets along with WenetSpeech for evaluation -- Dev for cross-validation purpose in training, Test_Net, collected from Internet for matched test, and Test\_Meeting, recorded from real meetings for more challenging mismatched test. Baseline systems trained with WenetSpeech are provided for three popular speech recognition toolkits, namely Kaldi, ESPnet, and WeNet, and recognition results on the three test sets are also provided as benchmarks. To the best of our knowledge, WenetSpeech is the current largest open-sourced Mandarin speech corpus with transcriptions, which benefits research on production-level speech recognition.

</details>

### [Knowledge Distillation for Neural Transducers from Large Self-Supervised Pre-trained Models](2110.03334.md)
**Xiaoyu Yang, Qiujia Li, Philip C. Woodland** · 2021-10-07

<details>
<summary>Abstract</summary>

Self-supervised pre-training is an effective approach to leveraging a large amount of unlabelled data to reduce word error rates (WERs) of automatic speech recognition (ASR) systems. Since it is impractical to use large pre-trained models for many real-world ASR applications, it is desirable to have a much smaller model while retaining the performance of the pre-trained model. In this paper, we propose a simple knowledge distillation (KD) loss function for neural transducers that focuses on the one-best path in the output probability lattice under both streaming and non-streaming setups, which allows a small student model to approach the performance of the large pre-trained teacher model. Experiments on the LibriSpeech dataset show that despite being 10 times smaller than the teacher model, the proposed loss results in relative WER reductions (WERRs) of 11.5% and 6.8% on the test-other set for non-streaming and streaming student models compared to the baseline transducers trained without KD using the labelled 100-hour clean data. With an additional 860 hours of unlabelled data for KD, the WERRs increase to 48.2% and 38.5% for non-streaming and streaming students. If language model shallow fusion is used for producing distillation targets, a further improvement in the student model is observed.

</details>

### [Improving Confidence Estimation on Out-of-Domain Data for End-to-End Speech Recognition](2110.03327.md)
**Qiujia Li, Yu Zhang, David Qiu, Yanzhang He et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

As end-to-end automatic speech recognition (ASR) models reach promising performance, various downstream tasks rely on good confidence estimators for these systems. Recent research has shown that model-based confidence estimators have a significant advantage over using the output softmax probabilities. If the input data to the speech recogniser is from mismatched acoustic and linguistic conditions, the ASR performance and the corresponding confidence estimators may exhibit severe degradation. Since confidence models are often trained on the same in-domain data as the ASR, generalising to out-of-domain (OOD) scenarios is challenging. By keeping the ASR model untouched, this paper proposes two approaches to improve the model-based confidence estimators on OOD data: using pseudo transcriptions and an additional OOD language model. With an ASR model trained on LibriSpeech, experiments show that the proposed methods can greatly improve the confidence metrics on TED-LIUM and Switchboard datasets while preserving in-domain performance. Furthermore, the improved confidence estimators are better calibrated on OOD data and can provide a much more reliable criterion for data selection.

</details>

### [Back from the future: bidirectional CTC decoding using future information in speech recognition](2110.03326.md)
**Namkyu Jung, Geonmin Kim, Han-Gyu Kim** · 2021-10-07

<details>
<summary>Abstract</summary>

In this paper, we propose a simple but effective method to decode the output of Connectionist Temporal Classifier (CTC) model using a bi-directional neural language model. The bidirectional language model uses the future as well as the past information in order to predict the next output in the sequence. The proposed method based on bi-directional beam search takes advantage of the CTC greedy decoding output to represent the noisy future information. Experiments on the Librispeechdataset demonstrate the superiority of our proposed method compared to baselines using unidirectional decoding. In particular, the boost inaccuracy is most apparent at the start of a sequence which is the most erroneous part for existing systems based on unidirectional decoding.

</details>

### [A Novel Blind Source Separation Framework Towards Maximum Signal-To-Interference Ratio](2110.03272.md)
**Jianju Gu, Longbiao Cheng, Dingding Yao, Junfeng Li et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

This letter proposes a new blind source separation (BSS) framework termed minimum variance independent component analysis (MVICA), which can potentially achieve the maximum output signal-to-interference ratio (SIR) while also allowing more flexibility in real implementations. The statistical independence assumption has been the foundation of the most dominant BSS techniques in recent decades. However, this assumption does not always hold true and the accurate probabilistic modeling of source is inherently difficult. To overcome these limitations and improve the separation performance, the MVICA framework is rigorously derived by optimizing the design of these independence-based BSS algorithms with the maximum SIR criterion. A deep neural network-supported implementation of MVICA is subsequently described. Experimental results under various conditions show the superiority of MVICA over the state-of-the-art BSS algorithms, in terms of not only SIR but also signal-to-distortion ratio and automatic speech recognition rate.

</details>

### [FAST-RIR: Fast neural diffuse room impulse response generator](2110.04057.md)
**Anton Ratnarajah, Shi-Xiong Zhang, Meng Yu, Zhenyu Tang et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

We present a neural-network-based fast diffuse room impulse response generator (FAST-RIR) for generating room impulse responses (RIRs) for a given acoustic environment. Our FAST-RIR takes rectangular room dimensions, listener and speaker positions, and reverberation time as inputs and generates specular and diffuse reflections for a given acoustic environment. Our FAST-RIR is capable of generating RIRs for a given input reverberation time with an average error of 0.02s. We evaluate our generated RIRs in automatic speech recognition (ASR) applications using Google Speech API, Microsoft Speech API, and Kaldi tools. We show that our proposed FAST-RIR with batch size 1 is 400 times faster than a state-of-the-art diffuse acoustic simulator (DAS) on a CPU and gives similar performance to DAS in ASR experiments. Our FAST-RIR is 12 times faster than an existing GPU-based RIR generator (gpuRIR). We show that our FAST-RIR outperforms gpuRIR by 2.5% in an AMI far-field ASR benchmark.

</details>

### [Minimum word error training for non-autoregressive Transformer-based code-switching ASR](2110.03573.md)
**Yizhou Peng, Jicheng Zhang, Haihua Xu, Hao Huang et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

Non-autoregressive end-to-end ASR framework might be potentially appropriate for code-switching recognition task thanks to its inherent property that present output token being independent of historical ones. However, it still under-performs the state-of-the-art autoregressive ASR frameworks. In this paper, we propose various approaches to boosting the performance of a CTC-mask-based nonautoregressive Transformer under code-switching ASR scenario. To begin with, we attempt diversified masking method that are closely related with code-switching point, yielding an improved baseline model. More importantly, we employ MinimumWord Error (MWE) criterion to train the model. One of the challenges is how to generate a diversified hypothetical space, so as to obtain the average loss for a given ground truth. To address such a challenge, we explore different approaches to yielding desired N-best-based hypothetical space. We demonstrate the efficacy of the proposed methods on SEAME corpus, a challenging English-Mandarin code-switching corpus for Southeast Asia community. Compared with the crossentropy-trained strong baseline, the proposed MWE training method achieves consistent performance improvement on the test sets.

</details>

### [Internal Language Model Adaptation with Text-Only Data for End-to-End Speech Recognition](2110.05354.md)
**Zhong Meng, Yashesh Gaur, Naoyuki Kanda, Jinyu Li et al.** · 2021-10-06

<details>
<summary>Abstract</summary>

Text-only adaptation of an end-to-end (E2E) model remains a challenging task for automatic speech recognition (ASR). Language model (LM) fusion-based approaches require an additional external LM during inference, significantly increasing the computation cost. To overcome this, we propose an internal LM adaptation (ILMA) of the E2E model using text-only data. Trained with audio-transcript pairs, an E2E model implicitly learns an internal LM that characterizes the token sequence probability which is approximated by the E2E model output after zeroing out the encoder contribution. During ILMA, we fine-tune the internal LM, i.e., the E2E components excluding the encoder, to minimize a cross-entropy loss. To make ILMA effective, it is essential to train the E2E model with an internal LM loss besides the standard E2E loss. Furthermore, we propose to regularize ILMA by minimizing the Kullback-Leibler divergence between the output distributions of the adapted and unadapted internal LMs. ILMA is the most effective when we update only the last linear layer of the joint network. ILMA enables a fast text-only adaptation of the E2E model without increasing the run-time computational cost. Experimented with 30K-hour trained transformer transducer models, ILMA achieves up to 34.9% relative word error rate reduction from the unadapted baseline.

</details>

### [Integrating Categorical Features in End-to-End ASR](2110.03047.md)
**Rongqing Huang** · 2021-10-06

<details>
<summary>Abstract</summary>

All-neural, end-to-end ASR systems gained rapid interest from the speech recognition community. Such systems convert speech input to text units using a single trainable neural network model. E2E models require large amounts of paired speech text data that is expensive to obtain. The amount of data available varies across different languages and dialects. It is critical to make use of all these data so that both low resource languages and high resource languages can be improved. When we want to deploy an ASR system for a new application domain, the amount of domain specific training data is very limited. To be able to leverage data from existing domains is important for ASR accuracy in the new domain. In this paper, we treat all these aspects as categorical information in an ASR system, and propose a simple yet effective way to integrate categorical features into E2E model. We perform detailed analysis on various training strategies, and find that building a joint model that includes categorical features can be more accurate than multiple independently trained models.

</details>

### [Spell my name: keyword boosted speech recognition](2110.02791.md)
**Namkyu Jung, Geonmin Kim, Joon Son Chung** · 2021-10-06

<details>
<summary>Abstract</summary>

Recognition of uncommon words such as names and technical terminology is important to understanding conversations in context. However, the ability to recognise such words remains a challenge in modern automatic speech recognition (ASR) systems. In this paper, we propose a simple but powerful ASR decoding method that can better recognise these uncommon keywords, which in turn enables better readability of the results. The method boosts the probabilities of given keywords in a beam search based on acoustic model predictions. The method does not require any training in advance. We demonstrate the effectiveness of our method on the LibriSpeeech test sets and also internal data of real-world conversations. Our method significantly boosts keyword accuracy on the test sets, while maintaining the accuracy of the other words, and as well as providing significant qualitative improvements. This method is applicable to other tasks such as machine translation, or wherever unseen and difficult keywords need to be recognised in beam search.

</details>

### [EdiTTS: Score-based Editing for Controllable Text-to-Speech](2110.02584.md)
**Jaesung Tae, Hyeongju Kim, Taesu Kim** · 2021-10-06

<details>
<summary>Abstract</summary>

We present EdiTTS, an off-the-shelf speech editing methodology based on score-based generative modeling for text-to-speech synthesis. EdiTTS allows for targeted, granular editing of audio, both in terms of content and pitch, without the need for any additional training, task-specific optimization, or architectural modifications to the score-based model backbone. Specifically, we apply coarse yet deliberate perturbations in the Gaussian prior space to induce desired behavior from the diffusion model while applying masks and softening kernels to ensure that iterative edits are applied only to the target region. Through listening tests and speech-to-text back transcription, we show that EdiTTS outperforms existing baselines and produces robust samples that satisfy user-imposed requirements.

</details>

### [Is Attention always needed? A Case Study on Language Identification from Speech](2110.03427.md)
**Atanu Mandal, Santanu Pal, Indranil Dutta, Mahidas Bhattacharya et al.** · 2021-10-05

<details>
<summary>Abstract</summary>

Language Identification (LID) is a crucial preliminary process in the field of Automatic Speech Recognition (ASR) that involves the identification of a spoken language from audio samples. Contemporary systems that can process speech in multiple languages require users to expressly designate one or more languages prior to utilization. The LID task assumes a significant role in scenarios where ASR systems are unable to comprehend the spoken language in multilingual settings, leading to unsuccessful speech recognition outcomes. The present study introduces convolutional recurrent neural network (CRNN) based LID, designed to operate on the Mel-frequency Cepstral Coefficient (MFCC) characteristics of audio samples. Furthermore, we replicate certain state-of-the-art methodologies, specifically the Convolutional Neural Network (CNN) and Attention-based Convolutional Recurrent Neural Network (CRNN with attention), and conduct a comparative analysis with our CRNN-based approach. We conducted comprehensive evaluations on thirteen distinct Indian languages and our model resulted in over 98\% classification accuracy. The LID model exhibits high-performance levels ranging from 97% to 100% for languages that are linguistically similar. The proposed LID model exhibits a high degree of extensibility to additional languages and demonstrates a strong resistance to noise, achieving 91.2% accuracy in a noisy setting when applied to a European Language (EU) dataset.

</details>

### [Late reverberation suppression using U-nets](2110.02144.md)
**Diego León, Felipe Tobar** · 2021-10-05

<details>
<summary>Abstract</summary>

In real-world settings, speech signals are almost always affected by reverberation produced by the working environment; these corrupted signals need to be \emph{dereverberated} prior to performing, e.g., speech recognition, speech-to-text conversion, compression, or general audio enhancement. In this paper, we propose a supervised dereverberation technique using \emph{U-nets with skip connections}, which are fully-convolutional encoder-decoder networks with layers arranged in the form of an "U" and connections that "skip" some layers. Building on this architecture, we address speech dereverberation through the lens of Late Reverberation Suppression (LS). Via experiments on synthetic and real-world data with different noise levels and reverberation settings, we show that our proposed method termed "LS U-net" improves quality, intelligibility and other performance metrics compared to the original U-net method and it is on par with the state-of-the-art GAN-based approaches.

</details>

### [ASR Rescoring and Confidence Estimation with ELECTRA](2110.01857.md)
**Hayato Futami, Hirofumi Inaguma, Masato Mimura, Shinsuke Sakai et al.** · 2021-10-05

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR) rescoring, the hypothesis with the fewest errors should be selected from the n-best list using a language model (LM). However, LMs are usually trained to maximize the likelihood of correct word sequences, not to detect ASR errors. We propose an ASR rescoring method for directly detecting errors with ELECTRA, which is originally a pre-training method for NLP tasks. ELECTRA is pre-trained to predict whether each word is replaced by BERT or not, which can simulate ASR error detection on large text corpora. To make this pre-training closer to ASR error detection, we further propose an extended version of ELECTRA called phone-attentive ELECTRA (P-ELECTRA). In the pre-training of P-ELECTRA, each word is replaced by a phone-to-word conversion model, which leverages phone information to generate acoustically similar words. Since our rescoring method is optimized for detecting errors, it can also be used for word-level confidence estimation. Experimental evaluations on the Librispeech and TED-LIUM2 corpora show that our rescoring method with ELECTRA is competitive with conventional rescoring methods with faster inference. ELECTRA also performs better in confidence estimation than BERT because it can learn to detect inappropriate words not only in fine-tuning but also in pre-training.

</details>

### [Fast Contextual Adaptation with Neural Associative Memory for On-Device Personalized Speech Recognition](2110.02220.md)
**Tsendsuren Munkhdalai, Khe Chai Sim, Angad Chandorkar, Fan Gao et al.** · 2021-10-05

<details>
<summary>Abstract</summary>

Fast contextual adaptation has shown to be effective in improving Automatic Speech Recognition (ASR) of rare words and when combined with an on-device personalized training, it can yield an even better recognition result. However, the traditional re-scoring approaches based on an external language model is prone to diverge during the personalized training. In this work, we introduce a model-based end-to-end contextual adaptation approach that is decoder-agnostic and amenable to on-device personalization. Our on-device simulation experiments demonstrate that the proposed approach outperforms the traditional re-scoring technique by 12% relative WER and 15.7% entity mention specific F1-score in a continues personalization scenario.

</details>

### [Towards efficient end-to-end speech recognition with biologically-inspired neural networks](2110.02743.md)
**Thomas Bohnstingl, Ayush Garg, Stanisław Woźniak, George Saon et al.** · 2021-10-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is a capability which enables a program to process human speech into a written form. Recent developments in artificial intelligence (AI) have led to high-accuracy ASR systems based on deep neural networks, such as the recurrent neural network transducer (RNN-T). However, the core components and the performed operations of these approaches depart from the powerful biological counterpart, i.e., the human brain. On the other hand, the current developments in biologically-inspired ASR models, based on spiking neural networks (SNNs), lag behind in terms of accuracy and focus primarily on small scale applications. In this work, we revisit the incorporation of biologically-plausible models into deep learning and we substantially enhance their capabilities, by taking inspiration from the diverse neural and synaptic dynamics found in the brain. In particular, we introduce neural connectivity concepts emulating the axo-somatic and the axo-axonic synapses. Based on this, we propose novel deep learning units with enriched neuro-synaptic dynamics and integrate them into the RNN-T architecture. We demonstrate for the first time, that a biologically realistic implementation of a large-scale ASR model can yield competitive performance levels compared to the existing deep learning models. Specifically, we show that such an implementation bears several advantages, such as a reduced computational cost and a lower latency, which are critical for speech recognition applications.

</details>

### [Building a Noisy Audio Dataset to Evaluate Machine Learning Approaches for Automatic Speech Recognition Systems](2110.01425.md)
**Julio Cesar Duarte, Sérgio Colcher** · 2021-10-04

<details>
<summary>Abstract</summary>

Automatic speech recognition systems are part of people's daily lives, embedded in personal assistants and mobile phones, helping as a facilitator for human-machine interaction while allowing access to information in a practically intuitive way. Such systems are usually implemented using machine learning techniques, especially with deep neural networks. Even with its high performance in the task of transcribing text from speech, few works address the issue of its recognition in noisy environments and, usually, the datasets used do not contain noisy audio examples, while only mitigating this issue using data augmentation techniques. This work aims to present the process of building a dataset of noisy audios, in a specific case of degenerated audios due to interference, commonly present in radio transmissions. Additionally, we present initial results of a classifier that uses such data for evaluation, indicating the benefits of using this dataset in the recognizer's training process. Such recognizer achieves an average result of 0.4116 in terms of character error rate in the noisy set (SNR = 30).

</details>

### [Speech Technology for Everyone: Automatic Speech Recognition for Non-Native English with Transfer Learning](2110.00678.md)
**Toshiko Shibano, Xinyi Zhang, Mia Taige Li, Haejin Cho et al.** · 2021-10-01

<details>
<summary>Abstract</summary>

To address the performance gap of English ASR models on L2 English speakers, we evaluate fine-tuning of pretrained wav2vec 2.0 models (Baevski et al., 2020; Xu et al., 2021) on L2-ARCTIC, a non-native English speech corpus (Zhao et al., 2018) under different training settings. We compare \textbf{(a)} models trained with a combination of diverse accents to ones trained with only specific accents and \textbf{(b)} results from different single-accent models. Our experiments demonstrate the promise of developing ASR models for non-native English speakers, even with small amounts of L2 training data and even without a language model. Our models also excel in the zero-shot setting where we train on multiple L2 datasets and test on a blind L2 test set.

</details>

### [Improving Punctuation Restoration for Speech Transcripts via External Data](2110.00560.md)
**Xue-Yong Fu, Cheng Chen, Md Tahmid Rahman Laskar, Shashi Bhushan TN et al.** · 2021-10-01

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems generally do not produce punctuated transcripts. To make transcripts more readable and follow the expected input format for downstream language models, it is necessary to add punctuation marks. In this paper, we tackle the punctuation restoration problem specifically for the noisy text (e.g., phone conversation scenarios). To leverage the available written text datasets, we introduce a data sampling technique based on an n-gram language model to sample more training data that are similar to our in-domain data. Moreover, we propose a two-stage fine-tuning approach that utilizes the sampled external data as well as our in-domain dataset for models based on BERT. Extensive experiments show that the proposed approach outperforms the baseline with an improvement of 1:12% F1 score.

</details>

### [Incremental Layer-wise Self-Supervised Learning for Efficient Speech Domain Adaptation On Device](2110.00155.md)
**Zhouyuan Huo, Dongseong Hwang, Khe Chai Sim, Shefali Garg et al.** · 2021-10-01

<details>
<summary>Abstract</summary>

Streaming end-to-end speech recognition models have been widely applied to mobile devices and show significant improvement in efficiency. These models are typically trained on the server using transcribed speech data. However, the server data distribution can be very different from the data distribution on user devices, which could affect the model performance. There are two main challenges for on device training, limited reliable labels and limited training memory. While self-supervised learning algorithms can mitigate the mismatch between domains using unlabeled data, they are not applicable on mobile devices directly because of the memory constraint. In this paper, we propose an incremental layer-wise self-supervised learning algorithm for efficient speech domain adaptation on mobile devices, in which only one layer is updated at a time. Extensive experimental results demonstrate that the proposed algorithm obtains a Word Error Rate (WER) on the target domain $24.2\%$ better than supervised baseline and costs $89.7\%$ less training memory than the end-to-end self-supervised learning algorithm.

</details>

### [SpliceOut: A Simple and Efficient Audio Augmentation Method](2110.00046.md)
**Arjit Jain, Pranay Reddy Samala, Deepak Mittal, Preethi Jyoti et al.** · 2021-09-30

<details>
<summary>Abstract</summary>

Time masking has become a de facto augmentation technique for speech and audio tasks, including automatic speech recognition (ASR) and audio classification, most notably as a part of SpecAugment. In this work, we propose SpliceOut, a simple modification to time masking which makes it computationally more efficient. SpliceOut performs comparably to (and sometimes outperforms) SpecAugment on a wide variety of speech and audio tasks, including ASR for seven different languages using varying amounts of training data, as well as on speech translation, sound and music classification, thus establishing itself as a broadly applicable audio augmentation method. SpliceOut also provides additional gains when used in conjunction with other augmentation techniques. Apart from the fully-supervised setting, we also demonstrate that SpliceOut can complement unsupervised representation learning with performance gains in the semi-supervised and self-supervised settings.

</details>

### [Federated Learning in ASR: Not as Easy as You Think](2109.15108.md)
**Wentao Yu, Jan Freiwald, Sören Tewes, Fabien Huennemeyer et al.** · 2021-09-30

<details>
<summary>Abstract</summary>

With the growing availability of smart devices and cloud services, personal speech assistance systems are increasingly used on a daily basis. Most devices redirect the voice recordings to a central server, which uses them for upgrading the recognizer model. This leads to major privacy concerns, since private data could be misused by the server or third parties. Federated learning is a decentralized optimization strategy that has been proposed to address such concerns. Utilizing this approach, private data is used for on-device training. Afterwards, updated model parameters are sent to the server to improve the global model, which is redistributed to the clients. In this work, we implement federated learning for speech recognition in a hybrid and an end-to-end model. We discuss the outcomes of these systems, which both show great similarities and only small improvements, pointing to a need for a deeper understanding of federated learning for speech recognition.

</details>

### [Fine-tuning wav2vec2 for speaker recognition](2109.15053.md)
**Nik Vaessen, David A. van Leeuwen** · 2021-09-30

<details>
<summary>Abstract</summary>

This paper explores applying the wav2vec2 framework to speaker recognition instead of speech recognition. We study the effectiveness of the pre-trained weights on the speaker recognition task, and how to pool the wav2vec2 output sequence into a fixed-length speaker embedding. To adapt the framework to speaker recognition, we propose a single-utterance classification variant with CE or AAM softmax loss, and an utterance-pair classification variant with BCE loss. Our best performing variant, w2v2-aam, achieves a 1.88% EER on the extended voxceleb1 test set compared to 1.69% EER with an ECAPA-TDNN baseline. Code is available at https://github.com/nikvaessen/w2v2-speaker.

</details>

### [FastCorrect 2: Fast Error Correction on Multiple Candidates for Automatic Speech Recognition](2109.14420.md)
**Yichong Leng, Xu Tan, Rui Wang, Linchen Zhu et al.** · 2021-09-29

<details>
<summary>Abstract</summary>

Error correction is widely used in automatic speech recognition (ASR) to post-process the generated sentence, and can further reduce the word error rate (WER). Although multiple candidates are generated by an ASR system through beam search, current error correction approaches can only correct one sentence at a time, failing to leverage the voting effect from multiple candidates to better detect and correct error tokens. In this work, we propose FastCorrect 2, an error correction model that takes multiple ASR candidates as input for better correction accuracy. FastCorrect 2 adopts non-autoregressive generation for fast inference, which consists of an encoder that processes multiple source sentences and a decoder that generates the target sentence in parallel from the adjusted source sentence, where the adjustment is based on the predicted duration of each source token. However, there are some issues when handling multiple source sentences. First, it is non-trivial to leverage the voting effect from multiple source sentences since they usually vary in length. Thus, we propose a novel alignment algorithm to maximize the degree of token alignment among multiple sentences in terms of token and pronunciation similarity. Second, the decoder can only take one adjusted source sentence as input, while there are multiple source sentences. Thus, we develop a candidate predictor to detect the most suitable candidate for the decoder. Experiments on our inhouse dataset and AISHELL-1 show that FastCorrect 2 can further reduce the WER over the previous correction model with single candidate by 3.2% and 2.6%, demonstrating the effectiveness of leveraging multiple candidates in ASR error correction. FastCorrect 2 achieves better performance than the cascaded re-scoring and correction pipeline and can serve as a unified post-processing module for ASR.

</details>

### [Comparison of Self-Supervised Speech Pre-Training Methods on Flemish Dutch](2109.14357.md)
**Jakob Poncelet, Hugo Van hamme** · 2021-09-29

<details>
<summary>Abstract</summary>

Recent research in speech processing exhibits a growing interest in unsupervised and self-supervised representation learning from unlabelled data to alleviate the need for large amounts of annotated data. We investigate several popular pre-training methods and apply them to Flemish Dutch. We compare off-the-shelf English pre-trained models to models trained on an increasing amount of Flemish data. We find that the most important factors for positive transfer to downstream speech recognition tasks include a substantial amount of data and a matching pre-training domain. Ideally, we also finetune on an annotated subset in the target language. All pre-trained models improve linear phone separability in Flemish, but not all methods improve Automatic Speech Recognition. We experience superior performance with wav2vec 2.0 and we obtain a 30% WER improvement by finetuning the multilingually pre-trained XLSR-53 model on Flemish Dutch, after integration into an HMM-DNN acoustic model.

</details>

### [Google Neural Network Models for Edge Devices: Analyzing and Mitigating Machine Learning Inference Bottlenecks](2109.14320.md)
**Amirali Boroumand, Saugata Ghose, Berkin Akin, Ravi Narayanaswami et al.** · 2021-09-29

<details>
<summary>Abstract</summary>

Emerging edge computing platforms often contain machine learning (ML) accelerators that can accelerate inference for a wide range of neural network (NN) models. These models are designed to fit within the limited area and energy constraints of the edge computing platforms, each targeting various applications (e.g., face detection, speech recognition, translation, image captioning, video analytics). To understand how edge ML accelerators perform, we characterize the performance of a commercial Google Edge TPU, using 24 Google edge NN models (which span a wide range of NN model types) and analyzing each NN layer within each model. We find that the Edge TPU suffers from three major shortcomings: (1) it operates significantly below peak computational throughput, (2) it operates significantly below its theoretical energy efficiency, and (3) its memory system is a large energy and performance bottleneck. Our characterization reveals that the one-size-fits-all, monolithic design of the Edge TPU ignores the high degree of heterogeneity both across different NN models and across different NN layers within the same NN model, leading to the shortcomings we observe. We propose a new acceleration framework called Mensa. Mensa incorporates multiple heterogeneous edge ML accelerators (including both on-chip and near-data accelerators), each of which caters to the characteristics of a particular subset of NN models and layers. During NN inference, for each NN layer, Mensa decides which accelerator to schedule the layer on, taking into account both the optimality of each accelerator for the layer and layer-to-layer communication costs. Averaged across all 24 Google edge NN models, Mensa improves energy efficiency and throughput by 3.0x and 3.1x over the Edge TPU, and by 2.4x and 4.3x over Eyeriss~v2, a state-of-the-art accelerator.

</details>

### [Word-level confidence estimation for RNN transducers](2110.15222.md)
**Mingqiu Wang, Hagen Soltau, Laurent El Shafey, Izhak Shafran** · 2021-09-28

<details>
<summary>Abstract</summary>

Confidence estimate is an often requested feature in applications such as medical transcription where errors can impact patient care and the confidence estimate could be used to alert medical professionals to verify potential errors in recognition. In this paper, we present a lightweight neural confidence model tailored for Automatic Speech Recognition (ASR) system with Recurrent Neural Network Transducers (RNN-T). Compared to other existing approaches, our model utilizes: (a) the time information associated with recognized words, which reduces the computational complexity, and (b) a simple and elegant trick for mapping between sub-word and word sequences. The mapping addresses the non-unique tokenization and token deletion problems while amplifying differences between confusable words. Through extensive empirical evaluations on two different long-form test sets, we demonstrate that the model achieves a performance of 0.4 Normalized Cross Entropy (NCE) and 0.05 Expected Calibration Error (ECE). It is robust across different ASR configurations, including target types (graphemes vs. morphemes), traffic conditions (streaming vs. non-streaming), and encoder types. We further discuss the importance of evaluation metrics to reflect practical applications and highlight the need for further work in improving Area Under the Curve (AUC) for Negative Precision Rate (NPV) and True Negative Rate (TNR).

</details>

### [Neural Dependency Coding inspired Multimodal Fusion](2110.00385.md)
**Shiv Shankar** · 2021-09-28

<details>
<summary>Abstract</summary>

Information integration from different modalities is an active area of research. Human beings and, in general, biological neural systems are quite adept at using a multitude of signals from different sensory perceptive fields to interact with the environment and each other. Recent work in deep fusion models via neural networks has led to substantial improvements over unimodal approaches in areas like speech recognition, emotion recognition and analysis, captioning and image description. However, such research has mostly focused on architectural changes allowing for fusion of different modalities while keeping the model complexity manageable. Inspired by recent neuroscience ideas about multisensory integration and processing, we investigate the effect of synergy maximizing loss functions. Experiments on multimodal sentiment analysis tasks: CMU-MOSI and CMU-MOSEI with different models show that our approach provides a consistent performance boost.

</details>

### [Private Language Model Adaptation for Speech Recognition](2110.10026.md)
**Zhe Liu, Ke Li, Shreyan Bakshi, Fuchun Peng** · 2021-09-28

<details>
<summary>Abstract</summary>

Speech model adaptation is crucial to handle the discrepancy between server-side proxy training data and actual data received on local devices of users. With the use of federated learning (FL), we introduce an efficient approach on continuously adapting neural network language models (NNLMs) on private devices with applications on automatic speech recognition (ASR). To address the potential speech transcription errors in the on-device training corpus, we perform empirical studies on comparing various strategies of leveraging token-level confidence scores to improve the NNLM quality in the FL settings. Experiments show that compared with no model adaptation, the proposed method achieves relative 2.6% and 10.8% word error rate (WER) reductions on two speech evaluation datasets, respectively. We also provide analysis in evaluating privacy guarantees of our presented procedure.

</details>

### [BigSSL: Exploring the Frontier of Large-Scale Semi-Supervised Learning for Automatic Speech Recognition](2109.13226.md)
**Yu Zhang, Daniel S. Park, Wei Han, James Qin et al.** · 2021-09-27

<details>
<summary>Abstract</summary>

We summarize the results of a host of efforts using giant automatic speech recognition (ASR) models pre-trained using large, diverse unlabeled datasets containing approximately a million hours of audio. We find that the combination of pre-training, self-training and scaling up model size greatly increases data efficiency, even for extremely large tasks with tens of thousands of hours of labeled data. In particular, on an ASR task with 34k hours of labeled data, by fine-tuning an 8 billion parameter pre-trained Conformer model we can match state-of-the-art (SoTA) performance with only 3% of the training data and significantly improve SoTA with the full training set. We also report on the universal benefits gained from using big pre-trained and self-trained models for a large set of downstream tasks that cover a wide range of speech domains and span multiple orders of magnitudes of dataset sizes, including obtaining SoTA performance on many public benchmarks. In addition, we utilize the learned representation of pre-trained networks to achieve SoTA results on non-ASR tasks.

</details>

### [Factorized Neural Transducer for Efficient Language Model Adaptation](2110.01500.md)
**Xie Chen, Zhong Meng, Sarangarajan Parthasarathy, Jinyu Li** · 2021-09-27

<details>
<summary>Abstract</summary>

In recent years, end-to-end (E2E) based automatic speech recognition (ASR) systems have achieved great success due to their simplicity and promising performance. Neural Transducer based models are increasingly popular in streaming E2E based ASR systems and have been reported to outperform the traditional hybrid system in some scenarios. However, the joint optimization of acoustic model, lexicon and language model in neural Transducer also brings about challenges to utilize pure text for language model adaptation. This drawback might prevent their potential applications in practice. In order to address this issue, in this paper, we propose a novel model, factorized neural Transducer, by factorizing the blank and vocabulary prediction, and adopting a standalone language model for the vocabulary prediction. It is expected that this factorization can transfer the improvement of the standalone language model to the Transducer for speech recognition, which allows various language model adaptation techniques to be applied. We demonstrate that the proposed factorized neural Transducer yields 15% to 20% WER improvements when out-of-domain text data is used for language model adaptation, at the cost of a minor degradation in WER on a general test set.

</details>

### [Fast-MD: Fast Multi-Decoder End-to-End Speech Translation with Non-Autoregressive Hidden Intermediates](2109.12804.md)
**Hirofumi Inaguma, Siddharth Dalmia, Brian Yan, Shinji Watanabe** · 2021-09-27

<details>
<summary>Abstract</summary>

The multi-decoder (MD) end-to-end speech translation model has demonstrated high translation quality by searching for better intermediate automatic speech recognition (ASR) decoder states as hidden intermediates (HI). It is a two-pass decoding model decomposing the overall task into ASR and machine translation sub-tasks. However, the decoding speed is not fast enough for real-world applications because it conducts beam search for both sub-tasks during inference. We propose Fast-MD, a fast MD model that generates HI by non-autoregressive (NAR) decoding based on connectionist temporal classification (CTC) outputs followed by an ASR decoder. We investigated two types of NAR HI: (1) parallel HI by using an autoregressive Transformer ASR decoder and (2) masked HI by using Mask-CTC, which combines CTC and the conditional masked language model. To reduce a mismatch in the ASR decoder between teacher-forcing during training and conditioning on CTC outputs during testing, we also propose sampling CTC outputs during training. Experimental evaluations on three corpora show that Fast-MD achieved about 2x and 4x faster decoding speed than that of the naïve MD model on GPU and CPU with comparable translation quality. Adopting the Conformer encoder and intermediate CTC loss further boosts its quality without sacrificing decoding speed.

</details>

### [Simple and Effective Zero-shot Cross-lingual Phoneme Recognition](2109.11680.md)
**Qiantong Xu, Alexei Baevski, Michael Auli** · 2021-09-23

<details>
<summary>Abstract</summary>

Recent progress in self-training, self-supervised pretraining and unsupervised learning enabled well performing speech recognition systems without any labeled data. However, in many cases there is labeled data available for related languages which is not utilized by these methods. This paper extends previous work on zero-shot cross-lingual transfer learning by fine-tuning a multilingually pretrained wav2vec 2.0 model to transcribe unseen languages. This is done by mapping phonemes of the training languages to the target language using articulatory features. Experiments show that this simple method significantly outperforms prior work which introduced task-specific architectures and used only part of a monolingually pretrained model.

</details>

### [Scenario Aware Speech Recognition: Advancements for Apollo Fearless Steps & CHiME-4 Corpora](2109.11086.md)
**Szu-Jui Chen, Wei Xia, John H. L. Hansen** · 2021-09-23

<details>
<summary>Abstract</summary>

In this study, we propose to investigate triplet loss for the purpose of an alternative feature representation for ASR. We consider a general non-semantic speech representation, which is trained with a self-supervised criteria based on triplet loss called TRILL, for acoustic modeling to represent the acoustic characteristics of each audio. This strategy is then applied to the CHiME-4 corpus and CRSS-UTDallas Fearless Steps Corpus, with emphasis on the 100-hour challenge corpus which consists of 5 selected NASA Apollo-11 channels. An analysis of the extracted embeddings provides the foundation needed to characterize training utterances into distinct groups based on acoustic distinguishing properties. Moreover, we also demonstrate that triplet-loss based embedding performs better than i-Vector in acoustic modeling, confirming that the triplet loss is more effective than a speaker feature. With additional techniques such as pronunciation and silence probability modeling, plus multi-style training, we achieve a +5.42% and +3.18% relative WER improvement for the development and evaluation sets of the Fearless Steps Corpus. To explore generalization, we further test the same technique on the 1 channel track of CHiME-4 and observe a +11.90% relative WER improvement for real test data.

</details>

### [Animal inspired Application of a Variant of Mel Spectrogram for Seismic Data Processing](2109.10733.md)
**Samayan Bhattacharya, Sk Shahnawaz** · 2021-09-22

<details>
<summary>Abstract</summary>

Predicting disaster events from seismic data is of paramount importance and can save thousands of lives, especially in earthquake-prone areas and habitations around volcanic craters. The drastic rise in the number of seismic monitoring stations in recent years has allowed the collection of a huge quantity of data, outpacing the capacity of seismologists. Due to the complex nature of the seismological data, it is often difficult for seismologists to detect subtle patterns with major implications. Machine learning algorithms have been demonstrated to be effective in classification and prediction tasks for seismic data. It has been widely known that some animals can sense disasters like earthquakes from seismic signals well before the disaster strikes. Mel spectrogram has been widely used for speech recognition as it scales the actual frequencies according to human hearing. In this paper, we propose a variant of the Mel spectrogram to scale the raw frequencies of seismic data to the hearing of such animals that can sense disasters from seismic signals. We are using a Computer vision algorithm along with clustering that allows for the classification of unlabelled seismic data.

</details>

### [On the Difficulty of Segmenting Words with Attention](2109.10107.md)
**Ramon Sanabria, Hao Tang, Sharon Goldwater** · 2021-09-21

<details>
<summary>Abstract</summary>

Word segmentation, the problem of finding word boundaries in speech, is of interest for a range of tasks. Previous papers have suggested that for sequence-to-sequence models trained on tasks such as speech translation or speech recognition, attention can be used to locate and segment the words. We show, however, that even on monolingual data this approach is brittle. In our experiments with different input types, data sizes, and segmentation algorithms, only models trained to predict phones from words succeed in the task. Models trained to predict words from either phones or speech (i.e., the opposite direction needed to generalize to new data), yield much worse results, suggesting that attention-based segmentation is only useful in limited scenarios.

</details>

### [Learning Domain Specific Language Models for Automatic Speech Recognition through Machine Translation](2110.10261.md)
**Saurav Jha** · 2021-09-21

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have been gaining popularity in the recent years for their widespread usage in smart phones and speakers. Building ASR systems for task-specific scenarios is subject to the availability of utterances that adhere to the style of the task as well as the language in question. In our work, we target such a scenario wherein task-specific text data is available in a language that is different from the target language in which an ASR Language Model (LM) is expected. We use Neural Machine Translation (NMT) as an intermediate step to first obtain translations of the task-specific text data. We then train LMs on the 1-best and N-best translations and study ways to improve on such a baseline LM. We develop a procedure to derive word confusion networks from NMT beam search graphs and evaluate LMs trained on these confusion networks. With experiments on the WMT20 chat translation task dataset, we demonstrate that NMT confusion networks can help to reduce the perplexity of both n-gram and recurrent neural network LMs compared to those trained only on N-best translations.

</details>

### [Audio Interval Retrieval using Convolutional Neural Networks](2109.09906.md)
**Ievgeniia Kuzminykh, Dan Shevchuk, Stavros Shiaeles, Bogdan Ghita** · 2021-09-21

<details>
<summary>Abstract</summary>

Modern streaming services are increasingly labeling videos based on their visual or audio content. This typically augments the use of technologies such as AI and ML by allowing to use natural speech for searching by keywords and video descriptions. Prior research has successfully provided a number of solutions for speech to text, in the case of a human speech, but this article aims to investigate possible solutions to retrieve sound events based on a natural language query, and estimate how effective and accurate they are. In this study, we specifically focus on the YamNet, AlexNet, and ResNet-50 pre-trained models to automatically classify audio samples using their respective melspectrograms into a number of predefined classes. The predefined classes can represent sounds associated with actions within a video fragment. Two tests are conducted to evaluate the performance of the models on two separate problems: audio classification and intervals retrieval based on a natural language query. Results show that the benchmarked models are comparable in terms of performance, with YamNet slightly outperforming the other two models. YamNet was able to classify single fixed-size audio samples with 92.7% accuracy and 68.75% precision while its average accuracy on intervals retrieval was 71.62% and precision was 41.95%. The investigated method may be embedded into an automated event marking architecture for streaming services.

</details>

### [Robustness Analysis of Deep Learning Frameworks on Mobile Platforms](2109.09869.md)
**Amin Eslami Abyane, Hadi Hemmati** · 2021-09-20

<details>
<summary>Abstract</summary>

With the recent increase in the computational power of modern mobile devices, machine learning-based heavy tasks such as face detection and speech recognition are now integral parts of such devices. This requires frameworks to execute machine learning models (e.g., Deep Neural Networks) on mobile devices. Although there exist studies on the accuracy and performance of these frameworks, the quality of on-device deep learning frameworks, in terms of their robustness, has not been systematically studied yet. In this paper, we empirically compare two on-device deep learning frameworks with three adversarial attacks on three different model architectures. We also use both the quantized and unquantized variants for each architecture. The results show that, in general, neither of the deep learning frameworks is better than the other in terms of robustness, and there is not a significant difference between the PC and mobile frameworks either. However, in cases like Boundary attack, mobile version is more robust than PC. In addition, quantization improves robustness in all cases when moving from PC to mobile.

</details>

### [iRNN: Integer-only Recurrent Neural Network](2109.09828.md)
**Eyyüb Sari, Vanessa Courville, Vahid Partovi Nia** · 2021-09-20

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNN) are used in many real-world text and speech applications. They include complex modules such as recurrence, exponential-based activation, gate interaction, unfoldable normalization, bi-directional dependence, and attention. The interaction between these elements prevents running them on integer-only operations without a significant performance drop. Deploying RNNs that include layer normalization and attention on integer-only arithmetic is still an open problem. We present a quantization-aware training method for obtaining a highly accurate integer-only recurrent neural network (iRNN). Our approach supports layer normalization, attention, and an adaptive piecewise linear approximation of activations (PWL), to serve a wide range of RNNs on various applications. The proposed method is proven to work on RNN-based language models and challenging automatic speech recognition, enabling AI applications on the edge. Our iRNN maintains similar performance as its full-precision counterpart, their deployment on smartphones improves the runtime performance by $2\times$, and reduces the model size by $4\times$.

</details>

### [MeetDot: Videoconferencing with Live Translation Captions](2109.09577.md)
**Arkady Arkhangorodsky, Christopher Chu, Scot Fang, Yiqi Huang et al.** · 2021-09-20

<details>
<summary>Abstract</summary>

We present MeetDot, a videoconferencing system with live translation captions overlaid on screen. The system aims to facilitate conversation between people who speak different languages, thereby reducing communication barriers between multilingual participants. Currently, our system supports speech and captions in 4 languages and combines automatic speech recognition (ASR) and machine translation (MT) in a cascade. We use the re-translation strategy to translate the streamed speech, resulting in caption flicker. Additionally, our system has very strict latency requirements to have acceptable call quality. We implement several features to enhance user experience and reduce their cognitive load, such as smooth scrolling captions and reducing caption flicker. The modular architecture allows us to integrate different ASR and MT services in our backend. Our system provides an integrated evaluation suite to optimize key intrinsic evaluation metrics such as accuracy, latency and erasure. Finally, we present an innovative cross-lingual word-guessing game as an extrinsic evaluation metric to measure end-to-end system performance. We plan to make our system open-source for research purposes.

</details>

### [Audio-Visual Speech Recognition is Worth 32$\times$32$\times$8 Voxels](2109.09536.md)
**Dmitriy Serdyuk, Otavio Braga, Olivier Siohan** · 2021-09-20

<details>
<summary>Abstract</summary>

Audio-visual automatic speech recognition (AV-ASR) introduces the video modality into the speech recognition process, often by relying on information conveyed by the motion of the speaker's mouth. The use of the video signal requires extracting visual features, which are then combined with the acoustic features to build an AV-ASR system [1]. This is traditionally done with some form of 3D convolutional network (e.g. VGG) as widely used in the computer vision community. Recently, image transformers [2] have been introduced to extract visual features useful for image classification tasks. In this work, we propose to replace the 3D convolutional visual front-end with a video transformer front-end. We train our systems on a large-scale dataset composed of YouTube videos and evaluate performance on the publicly available LRS3-TED set, as well as on a large set of YouTube videos. On a lip-reading task, the transformer-based front-end shows superior performance compared to a strong convolutional baseline. On an AV-ASR task, the transformer front-end performs as well as (or better than) the convolutional baseline. Fine-tuning our model on the LRS3-TED training set matches previous state of the art. Thus, we experimentally show the viability of the convolution-free model for AV-ASR.

</details>

### [Wav-BERT: Cooperative Acoustic and Linguistic Representation Learning for Low-Resource Speech Recognition](2109.09161.md)
**Guolin Zheng, Yubei Xiao, Ke Gong, Pan Zhou et al.** · 2021-09-19

<details>
<summary>Abstract</summary>

Unifying acoustic and linguistic representation learning has become increasingly crucial to transfer the knowledge learned on the abundance of high-resource language data for low-resource speech recognition. Existing approaches simply cascade pre-trained acoustic and language models to learn the transfer from speech to text. However, how to solve the representation discrepancy of speech and text is unexplored, which hinders the utilization of acoustic and linguistic information. Moreover, previous works simply replace the embedding layer of the pre-trained language model with the acoustic features, which may cause the catastrophic forgetting problem. In this work, we introduce Wav-BERT, a cooperative acoustic and linguistic representation learning method to fuse and utilize the contextual information of speech and text. Specifically, we unify a pre-trained acoustic model (wav2vec 2.0) and a language model (BERT) into an end-to-end trainable framework. A Representation Aggregation Module is designed to aggregate acoustic and linguistic representation, and an Embedding Attention Module is introduced to incorporate acoustic information into BERT, which can effectively facilitate the cooperation of two pre-trained models and thus boost the representation learning. Extensive experiments show that our Wav-BERT significantly outperforms the existing approaches and achieves state-of-the-art performance on low-resource speech recognition.

</details>

### [AI Accelerator Survey and Trends](2109.08957.md)
**Albert Reuther, Peter Michaleas, Michael Jones, Vijay Gadepally et al.** · 2021-09-18

<details>
<summary>Abstract</summary>

Over the past several years, new machine learning accelerators were being announced and released every month for a variety of applications from speech recognition, video object detection, assisted driving, and many data center applications. This paper updates the survey of AI accelerators and processors from past two years. This paper collects and summarizes the current commercial accelerators that have been publicly announced with peak performance and power consumption numbers. The performance and power values are plotted on a scatter graph, and a number of dimensions and observations from the trends on this plot are again discussed and analyzed. This year, we also compile a list of benchmarking performance results and compute the computational efficiency with respect to peak performance.

</details>

### [Dual-Encoder Architecture with Encoder Selection for Joint Close-Talk and Far-Talk Speech Recognition](2109.08744.md)
**Felix Weninger, Marco Gaudesi, Ralf Leibold, Roberto Gemello et al.** · 2021-09-17

<details>
<summary>Abstract</summary>

In this paper, we propose a dual-encoder ASR architecture for joint modeling of close-talk (CT) and far-talk (FT) speech, in order to combine the advantages of CT and FT devices for better accuracy. The key idea is to add an encoder selection network to choose the optimal input source (CT or FT) and the corresponding encoder. We use a single-channel encoder for CT speech and a multi-channel encoder with Spatial Filtering neural beamforming for FT speech, which are jointly trained with the encoder selection. We validate our approach on both attention-based and RNN Transducer end-to-end ASR systems. The experiments are done with conversational speech from a medical use case, which is recorded simultaneously with a CT device and a microphone array. Our results show that the proposed dual-encoder architecture obtains up to 9% relative WER reduction when using both CT and FT input, compared to the best single-encoder system trained and tested in matched condition.

</details>

### [Continuous Streaming Multi-Talker ASR with Dual-path Transducers](2109.08555.md)
**Desh Raj, Liang Lu, Zhuo Chen, Yashesh Gaur et al.** · 2021-09-17

<details>
<summary>Abstract</summary>

Streaming recognition of multi-talker conversations has so far been evaluated only for 2-speaker single-turn sessions. In this paper, we investigate it for multi-turn meetings containing multiple speakers using the Streaming Unmixing and Recognition Transducer (SURT) model, and show that naively extending the single-turn model to this harder setting incurs a performance penalty. As a solution, we propose the dual-path (DP) modeling strategy first used for time-domain speech separation. We experiment with LSTM and Transformer based DP models, and show that they improve word error rate (WER) performance while yielding faster convergence. We also explore training strategies such as chunk width randomization and curriculum learning for these models, and demonstrate their importance through ablation studies. Finally, we evaluate our models on the LibriCSS meeting data, where they perform competitively with offline separation-based methods.

</details>

### [Utterance-level neural confidence measure for end-to-end children speech recognition](2109.07750.md)
**Wei Liu, Tan Lee** · 2021-09-16

<details>
<summary>Abstract</summary>

Confidence measure is a performance index of particular importance for automatic speech recognition (ASR) systems deployed in real-world scenarios. In the present study, utterance-level neural confidence measure (NCM) in end-to-end automatic speech recognition (E2E ASR) is investigated. The E2E system adopts the joint CTC-attention Transformer architecture. The prediction of NCM is formulated as a task of binary classification, i.e., accept/reject the input utterance, based on a set of predictor features acquired during the ASR decoding process. The investigation is focused on evaluating and comparing the efficacies of predictor features that are derived from different internal and external modules of the E2E system. Experiments are carried out on children speech, for which state-of-the-art ASR systems show less than satisfactory performance and robust confidence measure is particularly useful. It is noted that predictor features related to acoustic information of speech play a more important role in estimating confidence measure than those related to linguistic information. N-best score features show significantly better performance than single-best ones. It has also been shown that the metrics of EER and AUC are not appropriate to evaluate the NCM of a mismatched ASR with significant performance gap.

</details>

### [Improving Accent Identification and Accented Speech Recognition Under a Framework of Self-supervised Learning](2109.07349.md)
**Keqi Deng, Songjun Cao, Long Ma** · 2021-09-15

<details>
<summary>Abstract</summary>

Recently, self-supervised pre-training has gained success in automatic speech recognition (ASR). However, considering the difference between speech accents in real scenarios, how to identify accents and use accent features to improve ASR is still challenging. In this paper, we employ the self-supervised pre-training method for both accent identification and accented speech recognition tasks. For the former task, a standard deviation constraint loss (SDC-loss) based end-to-end (E2E) architecture is proposed to identify accents under the same language. As for accented speech recognition task, we design an accent-dependent ASR system, which can utilize additional accent input features. Furthermore, we propose a frame-level accent feature, which is extracted based on the proposed accent identification model and can be dynamically adjusted. We pre-train our models using 960 hours unlabeled LibriSpeech dataset and fine-tune them on AESRC2020 speech dataset. The experimental results show that our proposed accent-dependent ASR system is significantly ahead of the AESRC2020 baseline and achieves $6.5\%$ relative word error rate (WER) reduction compared with our accent-independent ASR system.

</details>

### [Improving Streaming Transformer Based ASR Under a Framework of Self-supervised Learning](2109.07327.md)
**Songjun Cao, Yueteng Kang, Yanzhe Fu, Xiaoshuo Xu et al.** · 2021-09-15

<details>
<summary>Abstract</summary>

Recently self-supervised learning has emerged as an effective approach to improve the performance of automatic speech recognition (ASR). Under such a framework, the neural network is usually pre-trained with massive unlabeled data and then fine-tuned with limited labeled data. However, the non-streaming architecture like bidirectional transformer is usually adopted by the neural network to achieve competitive results, which can not be used in streaming scenarios. In this paper, we mainly focus on improving the performance of streaming transformer under the self-supervised learning framework. Specifically, we propose a novel two-stage training method during fine-tuning, which combines knowledge distilling and self-training. The proposed training method achieves 16.3% relative word error rate (WER) reduction on Librispeech noisy test set. Finally, by only using the 100h clean subset of Librispeech as the labeled data and the rest (860h) as the unlabeled data, our streaming transformer based model obtains competitive WERs 3.5/8.7 on Librispeech clean/noisy test sets.

</details>

### [Tied & Reduced RNN-T Decoder](2109.07513.md)
**Rami Botros, Tara N. Sainath, Robert David, Emmanuel Guzman et al.** · 2021-09-15

<details>
<summary>Abstract</summary>

Previous works on the Recurrent Neural Network-Transducer (RNN-T) models have shown that, under some conditions, it is possible to simplify its prediction network with little or no loss in recognition accuracy (arXiv:2003.07705 [eess.AS], [2], arXiv:2012.06749 [cs.CL]). This is done by limiting the context size of previous labels and/or using a simpler architecture for its layers instead of LSTMs. The benefits of such changes include reduction in model size, faster inference and power savings, which are all useful for on-device applications. In this work, we study ways to make the RNN-T decoder (prediction network + joint network) smaller and faster without degradation in recognition performance. Our prediction network performs a simple weighted averaging of the input embeddings, and shares its embedding matrix weights with the joint network's output layer (a.k.a. weight tying, commonly used in language modeling arXiv:1611.01462 [cs.LG]). This simple design, when used in conjunction with additional Edit-based Minimum Bayes Risk (EMBR) training, reduces the RNN-T Decoder from 23M parameters to just 2M, without affecting word-error rate (WER).

</details>

### [Residual Adapters for Parameter-Efficient ASR Adaptation to Atypical and Accented Speech](2109.06952.md)
**Katrin Tomanek, Vicky Zayats, Dirk Padfield, Kara Vaillancourt et al.** · 2021-09-14

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems are often optimized to work best for speakers with canonical speech patterns. Unfortunately, these systems perform poorly when tested on atypical speech and heavily accented speech. It has previously been shown that personalization through model fine-tuning substantially improves performance. However, maintaining such large models per speaker is costly and difficult to scale. We show that by adding a relatively small number of extra parameters to the encoder layers via so-called residual adapter, we can achieve similar adaptation gains compared to model fine-tuning, while only updating a tiny fraction (less than 0.5%) of the model parameters. We demonstrate this on two speech adaptation tasks (atypical and accented speech) and for two state-of-the-art ASR architectures.

</details>

### [Performance-Efficiency Trade-offs in Unsupervised Pre-training for Speech Recognition](2109.06870.md)
**Felix Wu, Kwangyoun Kim, Jing Pan, Kyu Han et al.** · 2021-09-14

<details>
<summary>Abstract</summary>

This paper is a study of performance-efficiency trade-offs in pre-trained models for automatic speech recognition (ASR). We focus on wav2vec 2.0, and formalize several architecture designs that influence both the model performance and its efficiency. Putting together all our observations, we introduce SEW (Squeezed and Efficient Wav2vec), a pre-trained model architecture with significant improvements along both performance and efficiency dimensions across a variety of training setups. For example, under the 100h-960h semi-supervised setup on LibriSpeech, SEW achieves a 1.9x inference speedup compared to wav2vec 2.0, with a 13.5% relative reduction in word error rate. With a similar inference time, SEW reduces word error rate by 25-50% across different model sizes.

</details>

### [Non-autoregressive Transformer with Unified Bidirectional Decoder for Automatic Speech Recognition](2109.06684.md)
**Chuan-Fei Zhang, Yan Liu, Tian-Hao Zhang, Song-Lu Chen et al.** · 2021-09-14

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) transformer models have been studied intensively in automatic speech recognition (ASR), and a substantial part of NAR transformer models is to use the casual mask to limit token dependencies. However, the casual mask is designed for the left-to-right decoding process of the non-parallel autoregressive (AR) transformer, which is inappropriate for the parallel NAR transformer since it ignores the right-to-left contexts. Some models are proposed to utilize right-to-left contexts with an extra decoder, but these methods increase the model complexity. To tackle the above problems, we propose a new non-autoregressive transformer with a unified bidirectional decoder (NAT-UBD), which can simultaneously utilize left-to-right and right-to-left contexts. However, direct use of bidirectional contexts will cause information leakage, which means the decoder output can be affected by the character information from the input of the same position. To avoid information leakage, we propose a novel attention mask and modify vanilla queries, keys, and values matrices for NAT-UBD. Experimental results verify that NAT-UBD can achieve character error rates (CERs) of 5.0%/5.5% on the Aishell1 dev/test sets, outperforming all previous NAR transformer models. Moreover, NAT-UBD can run 49.8x faster than the AR transformer baseline when decoding in a single step.

</details>

### [Multi-Sentence Resampling: A Simple Approach to Alleviate Dataset Length Bias and Beam-Search Degradation](2109.06253.md)
**Ivan Provilkov, Andrey Malinin** · 2021-09-13

<details>
<summary>Abstract</summary>

Neural Machine Translation (NMT) is known to suffer from a beam-search problem: after a certain point, increasing beam size causes an overall drop in translation quality. This effect is especially pronounced for long sentences. While much work was done analyzing this phenomenon, primarily for autoregressive NMT models, there is still no consensus on its underlying cause. In this work, we analyze errors that cause major quality degradation with large beams in NMT and Automatic Speech Recognition (ASR). We show that a factor that strongly contributes to the quality degradation with large beams is \textit{dataset length-bias} - \textit{NMT datasets are strongly biased towards short sentences}. To mitigate this issue, we propose a new data augmentation technique -- \textit{Multi-Sentence Resampling (MSR)}. This technique extends the training examples by concatenating several sentences from the original dataset to make a long training example. We demonstrate that MSR significantly reduces degradation with growing beam size and improves final translation quality on the IWSTL$15$ En-Vi, IWSTL$17$ En-Fr, and WMT$14$ En-De datasets.

</details>

### [Applications of Recurrent Neural Network for Biometric Authentication & Anomaly Detection](2109.05701.md)
**Joseph M. Ackerson, Dave Rushit, Seliya Jim** · 2021-09-13

<details>
<summary>Abstract</summary>

Recurrent Neural Networks are powerful machine learning frameworks that allow for data to be saved and referenced in a temporal sequence. This opens many new possibilities in fields such as handwriting analysis and speech recognition. This paper seeks to explore current research being conducted on RNNs in four very important areas, being biometric authentication, expression recognition, anomaly detection, and applications to aircraft. This paper reviews the methodologies, purpose, results, and the benefits and drawbacks of each proposed method below. These various methodologies all focus on how they can leverage distinct RNN architectures such as the popular Long Short-Term Memory (LSTM) RNN or a Deep-Residual RNN. This paper also examines which frameworks work best in certain situations, and the advantages and disadvantages of each pro-posed model.

</details>

### [A Decidability-Based Loss Function](2109.05524.md)
**Pedro Silva, Gladston Moreira, Vander Freitas, Rodrigo Silva et al.** · 2021-09-12

<details>
<summary>Abstract</summary>

Nowadays, deep learning is the standard approach for a wide range of problems, including biometrics, such as face recognition and speech recognition, etc. Biometric problems often use deep learning models to extract features from images, also known as embeddings. Moreover, the loss function used during training strongly influences the quality of the generated embeddings. In this work, a loss function based on the decidability index is proposed to improve the quality of embeddings for the verification routine. Our proposal, the D-loss, avoids some Triplet-based loss disadvantages such as the use of hard samples and tricky parameter tuning, which can lead to slow convergence. The proposed approach is compared against the Softmax (cross-entropy), Triplets Soft-Hard, and the Multi Similarity losses in four different benchmarks: MNIST, Fashion-MNIST, CIFAR10 and CASIA-IrisV4. The achieved results show the efficacy of the proposal when compared to other popular metrics in the literature. The D-loss computation, besides being simple, non-parametric and easy to implement, favors both the inter-class and intra-class scenarios.

</details>

### [Unsupervised Domain Adaptation Schemes for Building ASR in Low-resource Languages](2109.05494.md)
**Anoop C S, Prathosh A P, A G Ramakrishnan** · 2021-09-12

<details>
<summary>Abstract</summary>

Building an automatic speech recognition (ASR) system from scratch requires a large amount of annotated speech data, which is difficult to collect in many languages. However, there are cases where the low-resource language shares a common acoustic space with a high-resource language having enough annotated data to build an ASR. In such cases, we show that the domain-independent acoustic models learned from the high-resource language through unsupervised domain adaptation (UDA) schemes can enhance the performance of the ASR in the low-resource language. We use the specific example of Hindi in the source domain and Sanskrit in the target domain. We explore two architectures: i) domain adversarial training using gradient reversal layer (GRL) and ii) domain separation networks (DSN). The GRL and DSN architectures give absolute improvements of 6.71% and 7.32%, respectively, in word error rate over the baseline deep neural network model when trained on just 5.5 hours of data in the target domain. We also show that choosing a proper language (Telugu) in the source domain can bring further improvement. The results suggest that UDA schemes can be helpful in the development of ASR systems for low-resource languages, mitigating the hassle of collecting large amounts of annotated speech data.

</details>

### [Remember the context! ASR slot error correction through memorization](2109.05092.md)
**Dhanush Bekal, Ashish Shenoy, Monica Sunkara, Sravan Bodapati et al.** · 2021-09-10

<details>
<summary>Abstract</summary>

Accurate recognition of slot values such as domain specific words or named entities by automatic speech recognition (ASR) systems forms the core of the Goal-oriented Dialogue Systems. Although it is a critical step with direct impact on downstream tasks such as language understanding, many domain agnostic ASR systems tend to perform poorly on domain specific or long tail words. They are often supplemented with slot error correcting systems but it is often hard for any neural model to directly output such rare entity words. To address this problem, we propose k-nearest neighbor (k-NN) search that outputs domain-specific entities from an explicit datastore. We improve error correction rate by conveniently augmenting a pretrained joint phoneme and text based transformer sequence to sequence model with k-NN search during inference. We evaluate our proposed approach on five different domains containing long tail slot entities such as full names, airports, street names, cities, states. Our best performing error correction model shows a relative improvement of 7.4% in word error rate (WER) on rare word entities over the baseline and also achieves a relative WER improvement of 9.8% on an out of vocabulary (OOV) test set.

</details>

### [Physics-AI Symbiosis](2109.05959.md)
**Bahram Jalali, Achuta Kadambi, Vwani Roychowdhury** · 2021-09-10

<details>
<summary>Abstract</summary>

The phenomenal success of physics in explaining nature and designing hardware is predicated on efficient computational models. A universal codebook of physical laws defines the computational rules and a physical system is an interacting ensemble governed by these rules. Led by deep neural networks, artificial intelligence (AI) has introduced an alternate end-to-end data-driven computational framework, with astonishing performance gains in image classification and speech recognition and fueling hopes for a novel approach to discovering physics itself. These gains, however, come at the expense of interpretability and also computational efficiency; a trend that is on a collision course with the expected end of semiconductor scaling known as the Moore's Law. With focus on photonic applications, this paper argues how an emerging symbiosis of physics and artificial intelligence can overcome such formidable challenges, thereby not only extending the latter's spectacular rise but also transforming the direction of physical science.

</details>

### [Large-vocabulary Audio-visual Speech Recognition in Noisy Environments](2109.04894.md)
**Wentao Yu, Steffen Zeiler, Dorothea Kolossa** · 2021-09-10

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) can effectively and significantly improve the recognition rates of small-vocabulary systems, compared to their audio-only counterparts. For large-vocabulary systems, however, there are still many difficulties, such as unsatisfactory video recognition accuracies, that make it hard to improve over audio-only baselines. In this paper, we specifically consider such scenarios, focusing on the large-vocabulary task of the LRS2 database, where audio-only performance is far superior to video-only accuracies, making this an interesting and challenging setup for multi-modal integration. To address the inherent difficulties, we propose a new fusion strategy: a recurrent integration network is trained to fuse the state posteriors of multiple single-modality models, guided by a set of model-based and signal-based stream reliability measures. During decoding, this network is used for stream integration within a hybrid recognizer, where it can thus cope with the time-variant reliability and information content of its multiple feature inputs. We compare the results with end-to-end AVSR systems as well as with competitive hybrid baseline models, finding that the new fusion strategy shows superior results, on average even outperforming oracle dynamic stream weighting, which has so far marked the -- realistically unachievable -- upper bound for standard stream weighting. Even though the pure lipreading performance is low, audio-visual integration is helpful under all -- clean, noisy, and reverberant -- conditions. On average, the new system achieves a relative word error rate reduction of 42.18\% compared to the audio-only model, pointing at a high effectiveness of the proposed integration approach.

</details>

### [Self-Attention Channel Combinator Frontend for End-to-End Multichannel Far-field Speech Recognition](2109.04783.md)
**Rong Gong, Carl Quillen, Dushyant Sharma, Andrew Goderre et al.** · 2021-09-10

<details>
<summary>Abstract</summary>

When a sufficiently large far-field training data is presented, jointly optimizing a multichannel frontend and an end-to-end (E2E) Automatic Speech Recognition (ASR) backend shows promising results. Recent literature has shown traditional beamformer designs, such as MVDR (Minimum Variance Distortionless Response) or fixed beamformers can be successfully integrated as the frontend into an E2E ASR system with learnable parameters. In this work, we propose the self-attention channel combinator (SACC) ASR frontend, which leverages the self-attention mechanism to combine multichannel audio signals in the magnitude spectral domain. Experiments conducted on a multichannel playback test data shows that the SACC achieved a 9.3% WERR compared to a state-of-the-art fixed beamformer-based frontend, both jointly optimized with a ContextNet-based ASR backend. We also demonstrate the connection between the SACC and the traditional beamformers, and analyze the intermediate outputs of the SACC.

</details>

### [Infusing Future Information into Monotonic Attention Through Language Models](2109.03121.md)
**Mohd Abbas Zaidi, Sathish Indurthi, Beomseok Lee, Nikhil Kumar Lakumarapu et al.** · 2021-09-07

<details>
<summary>Abstract</summary>

Simultaneous neural machine translation(SNMT) models start emitting the target sequence before they have processed the source sequence. The recent adaptive policies for SNMT use monotonic attention to perform read/write decisions based on the partial source and target sequences. The lack of sufficient information might cause the monotonic attention to take poor read/write decisions, which in turn negatively affects the performance of the SNMT model. On the other hand, human translators make better read/write decisions since they can anticipate the immediate future words using linguistic information and domain knowledge.Motivated by human translators, in this work, we propose a framework to aid monotonic attention with an external language model to improve its decisions.We conduct experiments on the MuST-C English-German and English-French speech-to-text translation tasks to show the effectiveness of the proposed framework.The proposed SNMT method improves the quality-latency trade-off over the state-of-the-art monotonic multihead attention.

</details>

### [Complementing Handcrafted Features with Raw Waveform Using a Light-weight Auxiliary Model](2109.02773.md)
**Zhongwei Teng, Quchen Fu, Jules White, Maria Powell et al.** · 2021-09-06

<details>
<summary>Abstract</summary>

An emerging trend in audio processing is capturing low-level speech representations from raw waveforms. These representations have shown promising results on a variety of tasks, such as speech recognition and speech separation. Compared to handcrafted features, learning speech features via backpropagation provides the model greater flexibility in how it represents data for different tasks theoretically. However, results from empirical study shows that, in some tasks, such as voice spoof detection, handcrafted features are more competitive than learned features. Instead of evaluating handcrafted features and raw waveforms independently, this paper proposes an Auxiliary Rawnet model to complement handcrafted features with features learned from raw waveforms. A key benefit of the approach is that it can improve accuracy at a relatively low computational cost. The proposed Auxiliary Rawnet model is tested using the ASVspoof 2019 dataset and the results from this dataset indicate that a light-weight waveform encoder can potentially boost the performance of handcrafted-features-based encoders in exchange for a small amount of additional computational work.

</details>

### [ISyNet: Convolutional Neural Networks design for AI accelerator](2109.01932.md)
**Alexey Letunovskiy, Vladimir Korviakov, Vladimir Polovnikov, Anastasiia Kargapoltseva et al.** · 2021-09-04

<details>
<summary>Abstract</summary>

In recent years Deep Learning reached significant results in many practical problems, such as computer vision, natural language processing, speech recognition and many others. For many years the main goal of the research was to improve the quality of models, even if the complexity was impractically high. However, for the production solutions, which often require real-time work, the latency of the model plays a very important role. Current state-of-the-art architectures are found with neural architecture search (NAS) taking model complexity into account. However, designing of the search space suitable for specific hardware is still a challenging task. To address this problem we propose a measure of hardware efficiency of neural architecture search space - matrix efficiency measure (MEM); a search space comprising of hardware-efficient operations; a latency-aware scaling method; and ISyNet - a set of architectures designed to be fast on the specialized neural processing unit (NPU) hardware and accurate at the same time. We show the advantage of the designed architectures for the NPU devices on ImageNet and the generalization ability for the downstream classification and detection tasks.

</details>

### [Using Topological Framework for the Design of Activation Function and Model Pruning in Deep Neural Networks](2109.01572.md)
**Yogesh Kochar, Sunil Kumar Vengalil, Neelam Sinha** · 2021-09-03

<details>
<summary>Abstract</summary>

Success of deep neural networks in diverse tasks across domains of computer vision, speech recognition and natural language processing, has necessitated understanding the dynamics of training process and also working of trained models. Two independent contributions of this paper are 1) Novel activation function for faster training convergence 2) Systematic pruning of filters of models trained irrespective of activation function. We analyze the topological transformation of the space of training samples as it gets transformed by each successive layer during training, by changing the activation function. The impact of changing activation function on the convergence during training is reported for the task of binary classification. A novel activation function aimed at faster convergence for classification tasks is proposed. Here, Betti numbers are used to quantify topological complexity of data. Results of experiments on popular synthetic binary classification datasets with large Betti numbers(>150) using MLPs are reported. Results show that the proposed activation function results in faster convergence requiring fewer epochs by a factor of 1.5 to 2, since Betti numbers reduce faster across layers with the proposed activation function. The proposed methodology was verified on benchmark image datasets: fashion MNIST, CIFAR-10 and cat-vs-dog images, using CNNs. Based on empirical results, we propose a novel method for pruning a trained model. The trained model was pruned by eliminating filters that transform data to a topological space with large Betti numbers. All filters with Betti numbers greater than 300 were removed from each layer without significant reduction in accuracy. This resulted in faster prediction time and reduced memory size of the model.

</details>

### [CrypTen: Secure Multi-Party Computation Meets Machine Learning](2109.00984.md)
**Brian Knott, Shobha Venkataraman, Awni Hannun, Shubho Sengupta et al.** · 2021-09-02

<details>
<summary>Abstract</summary>

Secure multi-party computation (MPC) allows parties to perform computations on data while keeping that data private. This capability has great potential for machine-learning applications: it facilitates training of machine-learning models on private data sets owned by different parties, evaluation of one party's private model using another party's private data, etc. Although a range of studies implement machine-learning models via secure MPC, such implementations are not yet mainstream. Adoption of secure MPC is hampered by the absence of flexible software frameworks that "speak the language" of machine-learning researchers and engineers. To foster adoption of secure MPC in machine learning, we present CrypTen: a software framework that exposes popular secure MPC primitives via abstractions that are common in modern machine-learning frameworks, such as tensor computations, automatic differentiation, and modular neural networks. This paper describes the design of CrypTen and measure its performance on state-of-the-art models for text classification, speech recognition, and image classification. Our benchmarks show that CrypTen's GPU support and high-performance communication between (an arbitrary number of) parties allows it to perform efficient private evaluation of modern machine-learning models under a semi-honest threat model. For example, two parties using CrypTen can securely predict phonemes in speech recordings using Wav2Letter faster than real-time. We hope that CrypTen will spur adoption of secure MPC in the machine-learning community.

</details>

### [Coarse-To-Fine And Cross-Lingual ASR Transfer](2109.00916.md)
**Peter Polák, Ondřej Bojar** · 2021-09-02

<details>
<summary>Abstract</summary>

End-to-end neural automatic speech recognition systems achieved recently state-of-the-art results, but they require large datasets and extensive computing resources. Transfer learning has been proposed to overcome these difficulties even across languages, e.g., German ASR trained from an English model. We experiment with much less related languages, reusing an English model for Czech ASR. To simplify the transfer, we propose to use an intermediate alphabet, Czech without accents, and document that it is a highly effective strategy. The technique is also useful on Czech data alone, in the style of coarse-to-fine training. We achieve substantial eductions in training time as well as word error rate (WER).

</details>

### [Tree-constrained Pointer Generator for End-to-end Contextual Speech Recognition](2109.00627.md)
**Guangzhi Sun, Chao Zhang, Philip C. Woodland** · 2021-09-01

<details>
<summary>Abstract</summary>

Contextual knowledge is important for real-world automatic speech recognition (ASR) applications. In this paper, a novel tree-constrained pointer generator (TCPGen) component is proposed that incorporates such knowledge as a list of biasing words into both attention-based encoder-decoder and transducer end-to-end ASR models in a neural-symbolic way. TCPGen structures the biasing words into an efficient prefix tree to serve as its symbolic input and creates a neural shortcut between the tree and the final ASR output distribution to facilitate recognising biasing words during decoding. Systems were trained and evaluated on the Librispeech corpus where biasing words were extracted at the scales of an utterance, a chapter, or a book to simulate different application scenarios. Experimental results showed that TCPGen consistently improved word error rates (WERs) compared to the baselines, and in particular, achieved significant WER reductions on the biasing words. TCPGen is highly efficient: it can handle 5,000 biasing words and distractors and only add a small overhead to memory use and computation cost.

</details>

### [You Only Hear Once: A YOLO-like Algorithm for Audio Segmentation and Sound Event Detection](2109.00962.md)
**Satvik Venkatesh, David Moffat, Eduardo Reck Miranda** · 2021-09-01

<details>
<summary>Abstract</summary>

Audio segmentation and sound event detection are crucial topics in machine listening that aim to detect acoustic classes and their respective boundaries. It is useful for audio-content analysis, speech recognition, audio-indexing, and music information retrieval. In recent years, most research articles adopt segmentation-by-classification. This technique divides audio into small frames and individually performs classification on these frames. In this paper, we present a novel approach called You Only Hear Once (YOHO), which is inspired by the YOLO algorithm popularly adopted in Computer Vision. We convert the detection of acoustic boundaries into a regression problem instead of frame-based classification. This is done by having separate output neurons to detect the presence of an audio class and predict its start and end points. The relative improvement for F-measure of YOHO, compared to the state-of-the-art Convolutional Recurrent Neural Network, ranged from 1% to 6% across multiple datasets for audio segmentation and sound event detection. As the output of YOHO is more end-to-end and has fewer neurons to predict, the speed of inference is at least 6 times faster than segmentation-by-classification. In addition, as this approach predicts acoustic boundaries directly, the post-processing and smoothing is about 7 times faster.

</details>

### [Efficient conformer: Progressive downsampling and grouped attention for automatic speech recognition](2109.01163.md)
**Maxime Burchi, Valentin Vielzeuf** · 2021-08-31

<details>
<summary>Abstract</summary>

The recently proposed Conformer architecture has shown state-of-the-art performances in Automatic Speech Recognition by combining convolution with attention to model both local and global dependencies. In this paper, we study how to reduce the Conformer architecture complexity with a limited computing budget, leading to a more efficient architecture design that we call Efficient Conformer. We introduce progressive downsampling to the Conformer encoder and propose a novel attention mechanism named grouped attention, allowing us to reduce attention complexity from $O(n^{2}d)$ to $O(n^{2}d / g)$ for sequence length $n$, hidden dimension $d$ and group size parameter $g$. We also experiment the use of strided multi-head self-attention as a global downsampling operation. Our experiments are performed on the LibriSpeech dataset with CTC and RNN-Transducer losses. We show that within the same computing budget, the proposed architecture achieves better performances with faster training and decoding compared to the Conformer. Our 13M parameters CTC model achieves competitive WERs of 3.6%/9.0% without using a language model and 2.7%/6.7% with an external n-gram language model on the test-clean/test-other sets while being 29% faster than our CTC Conformer baseline at inference and 36% faster to train.

</details>

### [Adversarial Example Devastation and Detection on Speech Recognition System by Adding Random Noise](2108.13562.md)
**Mingyu Dong, Diqun Yan, Yongkang Gong, Rangding Wang** · 2021-08-31

<details>
<summary>Abstract</summary>

An automatic speech recognition (ASR) system based on a deep neural network is vulnerable to attack by an adversarial example, especially if the command-dependent ASR fails. A defense method against adversarial examples is proposed to improve the robustness and security of the ASR system. We propose an algorithm of devastation and detection on adversarial examples that can attack current advanced ASR systems. We choose an advanced text- and command-dependent ASR system as our target, generating adversarial examples by an optimization-based attack on text-dependent ASR and the GA-based algorithm on command-dependent ASR. The method is based on input transformation of adversarial examples. Different random intensities and kinds of noise are added to adversarial examples to devastate the perturbation previously added to normal examples. Experimental results show that the method performs well. For the devastation of examples, the original speech similarity after adding noise can reach 99.68%, the similarity of adversarial examples can reach zero, and the detection rate of adversarial examples can reach 94%.

</details>

### [Maximum F1-score training for end-to-end mispronunciation detection and diagnosis of L2 English speech](2108.13816.md)
**Bi-Cheng Yan, Shao-Wei Fan Jiang, Fu-An Chao, Berlin Chen** · 2021-08-31

<details>
<summary>Abstract</summary>

End-to-end (E2E) neural models are increasingly attracting attention as a promising modeling approach for mispronunciation detection and diagnosis (MDD). Typically, these models are trained by optimizing a cross-entropy criterion, which corresponds to improving the log-likelihood of the training data. However, there is a discrepancy between the objectives of model training and the MDD evaluation, since the performance of an MDD model is commonly evaluated in terms of F1-score instead of phone or word error rate (PER/WER). In view of this, we in this paper explore the use of a discriminative objective function for training E2E MDD models, which aims to maximize the expected F1-score directly. A series of experiments conducted on the L2-ARCTIC dataset show that our proposed method can yield considerable performance improvements in relation to some state-of-the-art E2E MDD approaches and the celebrated GOP method.

</details>

### [ASR-GLUE: A New Multi-task Benchmark for ASR-Robust Natural Language Understanding](2108.13048.md)
**Lingyun Feng, Jianwei Yu, Deng Cai, Songxiang Liu et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

Language understanding in speech-based systems have attracted much attention in recent years with the growing demand for voice interface applications. However, the robustness of natural language understanding (NLU) systems to errors introduced by automatic speech recognition (ASR) is under-examined. %To facilitate the research on ASR-robust general language understanding, In this paper, we propose ASR-GLUE benchmark, a new collection of 6 different NLU tasks for evaluating the performance of models under ASR error across 3 different levels of background noise and 6 speakers with various voice characteristics. Based on the proposed benchmark, we systematically investigate the effect of ASR error on NLU tasks in terms of noise intensity, error type and speaker variants. We further purpose two ways, correction-based method and data augmentation-based method to improve robustness of the NLU systems. Extensive experimental results and analysises show that the proposed methods are effective to some extent, but still far from human performance, demonstrating that NLU under ASR error is still very challenging and requires further research.

</details>

### [Multi-Channel Transformer Transducer for Speech Recognition](2108.12953.md)
**Feng-Ju Chang, Martin Radfar, Athanasios Mouchtaris, Maurizio Omologo** · 2021-08-30

<details>
<summary>Abstract</summary>

Multi-channel inputs offer several advantages over single-channel, to improve the robustness of on-device speech recognition systems. Recent work on multi-channel transformer, has proposed a way to incorporate such inputs into end-to-end ASR for improved accuracy. However, this approach is characterized by a high computational complexity, which prevents it from being deployed in on-device systems. In this paper, we present a novel speech recognition model, Multi-Channel Transformer Transducer (MCTT), which features end-to-end multi-channel training, low computation cost, and low latency so that it is suitable for streaming decoding in on-device speech recognition. In a far-field in-house dataset, our MCTT outperforms stagewise multi-channel models with transformer-transducer up to 6.01% relative WER improvement (WERR). In addition, MCTT outperforms the multi-channel transformer up to 11.62% WERR, and is 15.8 times faster in terms of inference speed. We further show that we can improve the computational cost of MCTT by constraining the future and previous context in attention computations.

</details>

### [Europarl-ASR: A Large Corpus of Parliamentary Debates for Streaming ASR Benchmarking and Speech Data Filtering/Verbatimization](s2:26da0b420c12d06f15af0a0f15b826c96a193beb.md)
**Gonçal V. Garcés Díaz-Munío, J. Silvestre-Cerdà, Javier Jorge, Adrián Giménez Pastor et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

We introduce Europarl-ASR, a large speech and text corpus of parliamentary debates including 1 300 hours of transcribed speeches and 70 million tokens of text in English extracted from European Parliament sessions. The training set is labelled with the Parliament’s non-fully-verbatim official transcripts, timealigned. As verbatimness is critical for acoustic model training, we also provide automatically noise-filtered and automatically verbatimized transcripts of all speeches based on speech data filtering and verbatimization techniques. Additionally, 18 hours of transcribed speeches were manually verbatimized to build reliable speaker-dependent and speaker-independent development/test sets for streaming ASR benchmarking. The availability of manual non-verbatim and verbatim transcripts for dev/test speeches makes this corpus useful for the assessment of automatic filtering and verbatimization techniques. This paper describes the corpus and its creation, and provides off-line and streaming ASR baselines for both the speaker-dependent and speaker-independent tasks using the three training transcription sets. The corpus is publicly released under an open licence.

</details>

### [Multiple Softmax Architecture for Streaming Multilingual End-to-End ASR Systems](s2:95a2bbe105558b5f2056f862e153090fb6239a62.md)
**Vikas Joshi, Amit Das, Eric Sun, Rupeshkumar Mehta et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

Improving multilingual end-to-end (E2E) automatic speech recognition (ASR) systems have manifold advantages. They simplify the training strategy, are easier to scale and exhibit better performance over monolingual models. However, it is still challenging to use a single multilingual model to recognize multiple languages without knowing the input language, as most multilingual models assume the availability of the input language. In this paper, we introduce multi-softmax model to improve the multilingual recurrent neural network transducer (RNN-T) models, by having language speciﬁc softmax, joint and embedding layers, while sharing rest of the parameters. We extend the multi-softmax model to work without knowing the input language, by integrating a language identiﬁcation (LID) model, that estimates the LID on-the-ﬂy and also does the recognition at the same time. The multi-softmax model outperforms monolingual models with an average word error rate relative (WERR) reduction of 4 . 65% on Indian languages. Finetun-ing further improves the WERR reduction to 12 . 2% . The multi-softmax model with on-the-ﬂy LID estimation, shows WERR reduction of 13 . 86% compared to the multilingual baseline.

</details>

### [Mixture Model Attention: Flexible Streaming and Non-Streaming Automatic Speech Recognition](s2:3933c9336ca4a3935fc2c74d44177239edac2f13.md)
**Kartik Audhkhasi, Tongzhou Chen, B. Ramabhadran, Pedro J. Moreno** · 2021-08-30

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) hypothesizes words as soon as the input audio arrives, whereas non-streaming ASR can potentially wait for the completion of the entire ut-terance to hypothesize words. Streaming and non-streaming ASR systems have typically used different acoustic encoders. Recent work has attempted to unify them by either jointly training a ﬁxed stack of streaming and non-streaming layers or using knowledge distillation during training to ensure consistency between the streaming and non-streaming predictions. We propose mixture model (MiMo) attention as a simpler and theoretically-motivated alternative that replaces only the attention mechanism, requires no change to the training loss, and allows greater ﬂexibility of switching between streaming and non-streaming mode during inference. Our experiments on the public Librispeech data set and a few Indic language data sets show that MiMo attention endows a single ASR model with the ability to operate in both streaming and non-streaming modes without any overhead and without signiﬁcant loss in accuracy compared to separately-trained streaming and non-streaming models. We also illustrate this beneﬁt of MiMo attention in a second-pass rescoring setting.

</details>

### [Streaming End-to-End Speech Recognition for Hybrid RNN-T/Attention Architecture](s2:4db2063a3bd0ae621a1b8d177d098e84c0a45844.md)
**Takafumi Moriya, Tomohiro Tanaka, Takanori Ashihara, Tsubasa Ochiai et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

We present a novel architecture with its decoding approach for improving recurrent neural network-transducer (RNN-T) performance. RNN-T is promising for building time-synchronous automatic speech recognition (ASR) systems and thus enhancing streaming ASR applications. We note that encoder-decoder-based sequence-to-sequence models (S2S) have been also used successfully by the ASR community. In this paper, we integrate these popular models in the RNN-T+S2S approach; higher recognition performance than either is achieved due to their integration. However, it is generally deemed to be complicated to use S2S in streaming systems, because the attention mechanism can use arbitrarily long past and future contexts during decoding. Our RNN-T+S2S is composed of the shared encoder, an RNN-T decoder and a triggered attention-based decoder which uses time restricted encoder outputs for attention weight computation. By using the trigger points generated from RNN-T outputs, the S2S branch of RNN-T+S2S activates only when the triggers are detected, which makes streaming ASR practical. Experiments on public and private datasets created to research various tasks demonstrate that our proposal can yield superior recognition performance.

</details>

### [The CSTR System for Multilingual and Code-Switching ASR Challenges for Low Resource Indian Languages](s2:1a81d6466c05244ee6f2c2610702603f07caace9.md)
**Ondrej Klejch, E. Wallington, P. Bell** · 2021-08-30

<details>
<summary>Abstract</summary>

This paper describes the CSTR submission to the Multilingual and Code-Switching ASR Challenges at Interspeech 2021. For the multilingual track of the challenge, we trained a multilingual CNN-TDNN acoustic model for Gujarati, Hindi, Marathi, Odia, Tamil and Telugu and subsequently ﬁne-tuned the model on monolingual training data. A language model built on a mixture of training and CommonCrawl data was used for decoding. We also demonstrate that crawled data from YouTube can be successfully used to improve the performance of the acoustic model with semi-supervised training. These models together with conﬁdence based language identiﬁcation achieve the average WER of 18.1%, a 41% relative improvement compared to the provided multilingual baseline model. For the code-switching track of the challenge we again train a multilingual model on Bengali and Hindi technical lectures and we employ a language model trained on CommonCrawl Bengali and Hindi data mixed with in-domain English data, using a novel transliteration method to generate pronunciations for the English terms. The ﬁnal model improves by 18% and 34% relative compared to our multilingual baseline. Both our systems were among the top-ranked entries to the challenge.

</details>

### [Improving RNN-T for Domain Scaling Using Semi-Supervised Training with Neural TTS](s2:9e8b8d25c94aa67025a441d8fb838749d4c79dba.md)
**Yan Deng, Rui Zhao, Zhong Meng, Xie Chen et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

Recurrent neural network transducer (RNN-T) has shown to be comparable with conventional hybrid model for speech recognition. However, there is still a challenge in out-of-domain scenarios with context or words different from training data. In this paper, we explore the semi-supervised training which optimizes RNN-T jointly with neural text-to-speech (TTS) to better generalize to new domains using domain-speciﬁc text data. We apply the method to two tasks: one with out-of-domain context and the other with signiﬁcant out-of-vocabulary (OOV) words. The results show that the proposed method signiﬁcantly improves the recognition accuracy in both tasks, resulting in 61.4% and 53.8% relative word error rate (WER) reductions respectively, from a well-trained RNN-T with 65 thousand hours of training data. We do further study on the semi-supervised training methodology: 1) which modules of RNN-T model to be updated; 2) the impact of using different neural TTS models; 3) the performance of using text with different relevancy to target domain. Finally, we compare several RNN-T customization methods, and conclude that semi-supervised training with neural TTS is comparable and complementary with Internal Language Model Estimation (ILME) or biasing.

</details>

### [Rapid Speaker Adaptation for Conformer Transducer: Attention and Bias Are All You Need](s2:39108c8127b90392a5338d64c8cd5d179a3f1723.md)
**Yan Huang, Guoli Ye, Jinyu Li, Y. Gong** · 2021-08-30

<details>
<summary>Abstract</summary>

Conformer transducer achieves new state-of-the-art end-to-end (E2E) system performance and has become increasingly appealing for production. In this paper, we study how to effectively perform rapid speaker adaptation in a conformer transducer and how it compares with the RNN transducer. We hi-erarchically decompose the conformer transducer and compare adapting each component through ﬁne-tuning. Among various interesting observations, there are three distinct ﬁndings: First, adapting the self-attention can achieve more than 80% gain of the full network adaptation. When the adaptation data is extremely scarce, attention is all you need to adapt. Second, within the self-attention, adapting the value projection outperforms adapting the key or the query projection. Lastly, bias adaptation, despite of its compact parameter space, is surpris-ingly effective. We conduct experiments on a state-of-the-art conformer transducer for an email dictation task. With 3 to 5 min source speech and 200 minute personalized TTS speech, the best performing encoder and joint network adaptation yields 38.37% and 19.90% relative word error rate (WER) reduction. Combining the attention and bias adaptation can achieve 90% of the gain with signiﬁcantly smaller footprint. Further comparison with the RNN-T suggests the new state-of-the-art conformer transducer can beneﬁt as much as if not more from personalization.

</details>

### [Investigations on Speech Recognition Systems for Low-Resource Dialectal Arabic-English Code-Switching Speech](2108.12881.md)
**Injy Hamed, Pavel Denisov, Chia-Yu Li, Mohamed Elmahdy et al.** · 2021-08-29

<details>
<summary>Abstract</summary>

Code-switching (CS), defined as the mixing of languages in conversations, has become a worldwide phenomenon. The prevalence of CS has been recently met with a growing demand and interest to build CS ASR systems. In this paper, we present our work on code-switched Egyptian Arabic-English automatic speech recognition (ASR). We first contribute in filling the huge gap in resources by collecting, analyzing and publishing our spontaneous CS Egyptian Arabic-English speech corpus. We build our ASR systems using DNN-based hybrid and Transformer-based end-to-end models. In this paper, we present a thorough comparison between both approaches under the setting of a low-resource, orthographically unstandardized, and morphologically rich language pair. We show that while both systems give comparable overall recognition results, each system provides complementary sets of strength points. We show that recognition can be improved by combining the outputs of both systems. We propose several effective system combination approaches, where hypotheses of both systems are merged on sentence- and word-levels. Our approaches result in overall WER relative improvement of 4.7%, over a baseline performance of 32.1% WER. In the case of intra-sentential CS sentences, we achieve WER relative improvement of 4.8%. Our best performing system achieves 30.6% WER on ArzEn test set.

</details>

### [A Multimodal Framework for Video Ads Understanding](2108.12868.md)
**Zejia Weng, Lingchen Meng, Rui Wang, Zuxuan Wu et al.** · 2021-08-29

<details>
<summary>Abstract</summary>

There is a growing trend in placing video advertisements on social platforms for online marketing, which demands automatic approaches to understand the contents of advertisements effectively. Taking the 2021 TAAC competition as an opportunity, we developed a multimodal system to improve the ability of structured analysis of advertising video content. In our framework, we break down the video structuring analysis problem into two tasks, i.e., scene segmentation and multi-modal tagging. In scene segmentation, we build upon a temporal convolution module for temporal modeling to predict whether adjacent frames belong to the same scene. In multi-modal tagging, we first compute clip-level visual features by aggregating frame-level features with NeXt-SoftDBoF. The visual features are further complemented with textual features that are derived using a global-local attention mechanism to extract useful information from OCR (Optical Character Recognition) and ASR (Audio Speech Recognition) outputs. Our solution achieved a score of 0.2470 measured in consideration of localization and prediction accuracy, ranking fourth in the 2021 TAAC final leaderboard.

</details>

### [Goal-driven text descriptions for images](2108.12575.md)
**Ruotian Luo** · 2021-08-28

<details>
<summary>Abstract</summary>

A big part of achieving Artificial General Intelligence(AGI) is to build a machine that can see and listen like humans. Much work has focused on designing models for image classification, video classification, object detection, pose estimation, speech recognition, etc., and has achieved significant progress in recent years thanks to deep learning. However, understanding the world is not enough. An AI agent also needs to know how to talk, especially how to communicate with a human. While perception (vision, for example) is more common across animal species, the use of complicated language is unique to humans and is one of the most important aspects of intelligence. In this thesis, we focus on generating textual output given visual input. In Chapter 3, we focus on generating the referring expression, a text description for an object in the image so that a receiver can infer which object is being described. We use a comprehension machine to directly guide the generated referring expressions to be more discriminative. In Chapter 4, we introduce a method that encourages discriminability in image caption generation. We show that more discriminative captioning models generate more descriptive captions. In Chapter 5, we study how training objectives and sampling methods affect the models' ability to generate diverse captions. We find that a popular captioning training strategy will be detrimental to the diversity of generated captions. In Chapter 6, we propose a model that can control the length of generated captions. By changing the desired length, one can influence the style and descriptiveness of the captions. Finally, in Chapter 7, we rank/generate informative image tags according to their information utility. The proposed method better matches what humans think are the most important tags for the images.

</details>

### [Injecting Text in Self-Supervised Speech Pretraining](2108.12226.md)
**Zhehuai Chen, Yu Zhang, Andrew Rosenberg, Bhuvana Ramabhadran et al.** · 2021-08-27

<details>
<summary>Abstract</summary>

Self-supervised pretraining for Automated Speech Recognition (ASR) has shown varied degrees of success. In this paper, we propose to jointly learn representations during pretraining from two different modalities: speech and text. The proposed method, tts4pretrain complements the power of contrastive learning in self-supervision with linguistic/lexical representations derived from synthesized speech, effectively learning from untranscribed speech and unspoken text. Lexical learning in the speech encoder is enforced through an additional sequence loss term that is coupled with contrastive loss during pretraining. We demonstrate that this novel pretraining method yields Word Error Rate (WER) reductions of 10% relative on the well-benchmarked, Librispeech task over a state-of-the-art baseline pretrained with wav2vec2.0 only. The proposed method also serves as an effective strategy to compensate for the lack of transcribed speech, effectively matching the performance of 5000 hours of transcribed speech with just 100 hours of transcribed speech on the AMI meeting transcription task. Finally, we demonstrate WER reductions of up to 15% on an in-house Voice Search task over traditional pretraining. Incorporating text into encoder pretraining is complimentary to rescoring with a larger or in-domain language model, resulting in additional 6% relative reduction in WER.

</details>

### [Grammar Based Speaker Role Identification for Air Traffic Control Speech Recognition](2108.12175.md)
**Amrutha Prasad, Juan Zuluaga-Gomez, Petr Motlicek, Saeed Sarfjoo et al.** · 2021-08-27

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) for air traffic control is generally trained by pooling Air Traffic Controller (ATCO) and pilot data into one set. This is motivated by the fact that pilot's voice communications are more scarce than ATCOs. Due to this data imbalance and other reasons (e.g., varying acoustic conditions), the speech from ATCOs is usually recognized more accurately than from pilots. Automatically identifying the speaker roles is a challenging task, especially in the case of the noisy voice recordings collected using Very High Frequency (VHF) receivers or due to the unavailability of the push-to-talk (PTT) signal, i.e., both audio channels are mixed. In this work, we propose to (1) automatically segment the ATCO and pilot data based on an intuitive approach exploiting ASR transcripts and (2) subsequently consider an automatic recognition of ATCOs' and pilots' voice as two separate tasks. Our work is performed on VHF audio data with high noise levels, i.e., signal-to-noise (SNR) ratios below 15 dB, as this data is recognized to be helpful for various speech-based machine-learning tasks. Specifically, for the speaker role identification task, the module is represented by a simple yet efficient knowledge-based system exploiting a grammar defined by the International Civil Aviation Organization (ICAO). The system accepts text as the input, either manually verified annotations or automatically generated transcripts. The developed approach provides an average accuracy in speaker role identification of about 83%. Finally, we show that training an acoustic model for ASR tasks separately (i.e., separate models for ATCOs and pilots) or using a multitask approach is well suited for the noisy data and outperforms the traditional ASR system where all data is pooled together.

</details>

### [Improving callsign recognition with air-surveillance data in air-traffic communication](2108.12156.md)
**Iuliia Nigmatulina, Rudolf Braun, Juan Zuluaga-Gomez, Petr Motlicek** · 2021-08-27

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) can be used as the assistance of speech communication between pilots and air-traffic controllers. Its application can significantly reduce the complexity of the task and increase the reliability of transmitted information. Evidently, high accuracy predictions are needed to minimize the risk of errors. Especially, high accuracy is required in recognition of key information, such as commands and callsigns, used to navigate pilots. Our results prove that the surveillance data containing callsigns can help to considerably improve the recognition of a callsign in an utterance when the weights of probable callsign n-grams are reduced per utterance. In this paper, we investigate two approaches: (1) G-boosting, when callsigns weights are adjusted at language model level (G) and followed by the dynamic decoder with an on-the-fly composition, and (2) lattice rescoring when callsign information is introduced on top of lattices generated using a conventional decoder. Boosting callsign n-grams with the combination of two methods allowed us to gain 28.4% of absolute improvement in callsign recognition accuracy and up to 74.2% of relative improvement in WER of callsign recognition.

</details>

### [Full Attention Bidirectional Deep Learning Structure for Single Channel Speech Enhancement](2108.12105.md)
**Yuzi Yan, Wei-Qiang Zhang, Michael T. Johnson** · 2021-08-27

<details>
<summary>Abstract</summary>

As the cornerstone of other important technologies, such as speech recognition and speech synthesis, speech enhancement is a critical area in audio signal processing. In this paper, a new deep learning structure for speech enhancement is demonstrated. The model introduces a "full" attention mechanism to a bidirectional sequence-to-sequence method to make use of latent information after each focal frame. This is an extension of the previous attention-based RNN method. The proposed bidirectional attention-based architecture achieves better performance in terms of speech quality (PESQ), compared with OM-LSA, CNN-LSTM, T-GSA and the unidirectional attention-based LSTM baseline.

</details>

### [4-bit Quantization of LSTM-based Speech Recognition Models](2108.12074.md)
**Andrea Fasoli, Chia-Yu Chen, Mauricio Serrano, Xiao Sun et al.** · 2021-08-27

<details>
<summary>Abstract</summary>

We investigate the impact of aggressive low-precision representations of weights and activations in two families of large LSTM-based architectures for Automatic Speech Recognition (ASR): hybrid Deep Bidirectional LSTM - Hidden Markov Models (DBLSTM-HMMs) and Recurrent Neural Network - Transducers (RNN-Ts). Using a 4-bit integer representation, a naïve quantization approach applied to the LSTM portion of these models results in significant Word Error Rate (WER) degradation. On the other hand, we show that minimal accuracy loss is achievable with an appropriate choice of quantizers and initializations. In particular, we customize quantization schemes depending on the local properties of the network, improving recognition performance while limiting computational time. We demonstrate our solution on the Switchboard (SWB) and CallHome (CH) test sets of the NIST Hub5-2000 evaluation. DBLSTM-HMMs trained with 300 or 2000 hours of SWB data achieves $<$0.5% and $<$1% average WER degradation, respectively. On the more challenging RNN-T models, our quantization strategy limits degradation in 4-bit inference to 1.3%.

</details>

### [Position-Invariant Truecasing with a Word-and-Character Hierarchical Recurrent Neural Network](2108.11943.md)
**Hao Zhang, You-Chi Cheng, Shankar Kumar, Mingqing Chen et al.** · 2021-08-26

<details>
<summary>Abstract</summary>

Truecasing is the task of restoring the correct case (uppercase or lowercase) of noisy text generated either by an automatic system for speech recognition or machine translation or by humans. It improves the performance of downstream NLP tasks such as named entity recognition and language modeling. We propose a fast, accurate and compact two-level hierarchical word-and-character-based recurrent neural network model, the first of its kind for this problem. Using sequence distillation, we also address the problem of truecasing while ignoring token positions in the sentence, i.e. in a position-invariant manner.

</details>

### [Reducing Exposure Bias in Training Recurrent Neural Network Transducers](2108.10803.md)
**Xiaodong Cui, Brian Kingsbury, George Saon, David Haws et al.** · 2021-08-24

<details>
<summary>Abstract</summary>

When recurrent neural network transducers (RNNTs) are trained using the typical maximum likelihood criterion, the prediction network is trained only on ground truth label sequences. This leads to a mismatch during inference, known as exposure bias, when the model must deal with label sequences containing errors. In this paper we investigate approaches to reducing exposure bias in training to improve the generalization of RNNT models for automatic speech recognition (ASR). A label-preserving input perturbation to the prediction network is introduced. The input token sequences are perturbed using SwitchOut and scheduled sampling based on an additional token language model. Experiments conducted on the 300-hour Switchboard dataset demonstrate their effectiveness. By reducing the exposure bias, we show that we can further improve the accuracy of a high-performance RNNT ASR model and obtain state-of-the-art results on the 300-hour Switchboard dataset.

</details>

### [Graph Neural Networks: Methods, Applications, and Opportunities](2108.10733.md)
**Lilapati Waikhom, Ripon Patgiri** · 2021-08-24

<details>
<summary>Abstract</summary>

In the last decade or so, we have witnessed deep learning reinvigorating the machine learning field. It has solved many problems in the domains of computer vision, speech recognition, natural language processing, and various other tasks with state-of-the-art performance. The data is generally represented in the Euclidean space in these domains. Various other domains conform to non-Euclidean space, for which graph is an ideal representation. Graphs are suitable for representing the dependencies and interrelationships between various entities. Traditionally, handcrafted features for graphs are incapable of providing the necessary inference for various tasks from this complex data representation. Recently, there is an emergence of employing various advances in deep learning to graph data-based tasks. This article provides a comprehensive survey of graph neural networks (GNNs) in each learning setting: supervised, unsupervised, semi-supervised, and self-supervised learning. Taxonomy of each graph based learning setting is provided with logical divisions of methods falling in the given learning setting. The approaches for each learning task are analyzed from both theoretical as well as empirical standpoints. Further, we provide general architecture guidelines for building GNNs. Various applications and benchmark datasets are also provided, along with open challenges still plaguing the general applicability of GNNs.

</details>

### [A Unified Transformer-based Framework for Duplex Text Normalization](2108.09889.md)
**Tuan Manh Lai, Yang Zhang, Evelina Bakhturina, Boris Ginsburg et al.** · 2021-08-23

<details>
<summary>Abstract</summary>

Text normalization (TN) and inverse text normalization (ITN) are essential preprocessing and postprocessing steps for text-to-speech synthesis and automatic speech recognition, respectively. Many methods have been proposed for either TN or ITN, ranging from weighted finite-state transducers to neural networks. Despite their impressive performance, these methods aim to tackle only one of the two tasks but not both. As a result, in a complete spoken dialog system, two separate models for TN and ITN need to be built. This heterogeneity increases the technical complexity of the system, which in turn increases the cost of maintenance in a production setting. Motivated by this observation, we propose a unified framework for building a single neural duplex system that can simultaneously handle TN and ITN. Combined with a simple but effective data augmentation method, our systems achieve state-of-the-art results on the Google TN dataset for English and Russian. They can also reach over 95% sentence-level accuracy on an internal English TN dataset without any additional fine-tuning. In addition, we also create a cleaned dataset from the Spoken Wikipedia Corpora for German and report the performance of our systems on the dataset. Overall, experimental results demonstrate the proposed duplex text normalization framework is highly effective and applicable to a range of domains and languages

</details>

### [One TTS Alignment To Rule Them All](2108.10447.md)
**Rohan Badlani, Adrian Łancucki, Kevin J. Shih, Rafael Valle et al.** · 2021-08-23

<details>
<summary>Abstract</summary>

Speech-to-text alignment is a critical component of neural textto-speech (TTS) models. Autoregressive TTS models typically use an attention mechanism to learn these alignments on-line. However, these alignments tend to be brittle and often fail to generalize to long utterances and out-of-domain text, leading to missing or repeating words. Most non-autoregressive endto-end TTS models rely on durations extracted from external sources. In this paper we leverage the alignment mechanism proposed in RAD-TTS as a generic alignment learning framework, easily applicable to a variety of neural TTS models. The framework combines forward-sum algorithm, the Viterbi algorithm, and a simple and efficient static prior. In our experiments, the alignment learning framework improves all tested TTS architectures, both autoregressive (Flowtron, Tacotron 2) and non-autoregressive (FastPitch, FastSpeech 2, RAD-TTS). Specifically, it improves alignment convergence speed of existing attention-based mechanisms, simplifies the training pipeline, and makes the models more robust to errors on long utterances. Most importantly, the framework improves the perceived speech synthesis quality, as judged by human evaluators.

</details>

### [Multilingual Speech Recognition for Low-Resource Indian Languages using Multi-Task conformer](2109.03969.md)
**Krishna D N** · 2021-08-22

<details>
<summary>Abstract</summary>

Transformers have recently become very popular for sequence-to-sequence applications such as machine translation and speech recognition. In this work, we propose a multi-task learning-based transformer model for low-resource multilingual speech recognition for Indian languages. Our proposed model consists of a conformer [1] encoder and two parallel transformer decoders. We use a phoneme decoder (PHN-DEC) for the phoneme recognition task and a grapheme decoder (GRP-DEC) to predict grapheme sequence. We consider the phoneme recognition task as an auxiliary task for our multi-task learning framework. We jointly optimize the network for both phoneme and grapheme recognition tasks using Joint CTC-Attention [2] training. We use a conditional decoding scheme to inject the language information into the model before predicting the grapheme sequence. Our experiments show that our proposed approach can obtain significant improvement over previous approaches [4]. We also show that our conformer-based dual-decoder approach outperforms both the transformer-based dual-decoder approach and single decoder approach. Finally, We compare monolingual ASR models with our proposed multilingual ASR approach.

</details>

### [A Dual-Decoder Conformer for Multilingual Speech Recognition](2109.03277.md)
**Krishna D N** · 2021-08-22

<details>
<summary>Abstract</summary>

Transformer-based models have recently become very popular for sequence-to-sequence applications such as machine translation and speech recognition. This work proposes a dual-decoder transformer model for low-resource multilingual speech recognition for Indian languages. Our proposed model consists of a Conformer [1] encoder, two parallel transformer decoders, and a language classifier. We use a phoneme decoder (PHN-DEC) for the phoneme recognition task and a grapheme decoder (GRP-DEC) to predict grapheme sequence along with language information. We consider phoneme recognition and language identification as auxiliary tasks in the multi-task learning framework. We jointly optimize the network for phoneme recognition, grapheme recognition, and language identification tasks with Joint CTC-Attention [2] training. Our experiments show that we can obtain a significant reduction in WER over the baseline approaches. We also show that our dual-decoder approach obtains significant improvement over the single decoder approach.

</details>

### [Generalizing RNN-Transducer to Out-Domain Audio via Sparse Self-Attention Layers](2108.10752.md)
**Juntae Kim, Jeehye Lee** · 2021-08-22

<details>
<summary>Abstract</summary>

Recurrent neural network transducer (RNN-T) is an end-to-end speech recognition framework converting input acoustic frames into a character sequence. The state-of-the-art encoder network for RNN-T is the Conformer, which can effectively model the local-global context information via its convolution and self-attention layers. Although Conformer RNN-T has shown outstanding performance, most studies have been verified in the setting where the train and test data are drawn from the same domain. The domain mismatch problem for Conformer RNN-T has not been intensively investigated yet, which is an important issue for the product-level speech recognition system. In this study, we identified that fully connected self-attention layers in the Conformer caused high deletion errors, specifically in the long-form out-domain utterances. To address this problem, we introduce sparse self-attention layers for Conformer-based encoder networks, which can exploit local and generalized global information by pruning most of the in-domain fitted global connections. Also, we propose a state reset method for the generalization of the prediction network to cope with long-form utterances. Applying proposed methods to an out-domain test, we obtained 27.6% relative character error rate (CER) reduction compared to the fully connected self-attention layer-based Conformers.

</details>

### [A Multi-level Acoustic Feature Extraction Framework for Transformer Based End-to-End Speech Recognition](2108.07980.md)
**Jin Li, Rongfeng Su, Xurong Xie, Nan Yan et al.** · 2021-08-18

<details>
<summary>Abstract</summary>

Transformer based end-to-end modelling approaches with multiple stream inputs have been achieved great success in various automatic speech recognition (ASR) tasks. An important issue associated with such approaches is that the intermediate features derived from each stream might have similar representations and thus it is lacking of feature diversity, such as the descriptions related to speaker characteristics. To address this issue, this paper proposed a novel multi-level acoustic feature extraction framework that can be easily combined with Transformer based ASR models. The framework consists of two input streams: a shallow stream with high-resolution spectrograms and a deep stream with low-resolution spectrograms. The shallow stream is used to acquire traditional shallow features that is beneficial for the classification of phones or words while the deep stream is used to obtain utterance-level speaker-invariant deep features for improving the feature diversity. A feature correlation based fusion strategy is used to aggregate both features across the frequency and time domains and then fed into the Transformer encoder-decoder module. By using the proposed multi-level acoustic feature extraction framework, state-of-the-art word error rate of 21.7% and 2.5% were obtained on the HKUST Mandarin telephone and Librispeech speech recognition tasks respectively.

</details>

### [Integrating Dialog History into End-to-End Spoken Language Understanding Systems](2108.08405.md)
**Jatin Ganhotra, Samuel Thomas, Hong-Kwang J. Kuo, Sachindra Joshi et al.** · 2021-08-18

<details>
<summary>Abstract</summary>

End-to-end spoken language understanding (SLU) systems that process human-human or human-computer interactions are often context independent and process each turn of a conversation independently. Spoken conversations on the other hand, are very much context dependent, and dialog history contains useful information that can improve the processing of each conversational turn. In this paper, we investigate the importance of dialog history and how it can be effectively integrated into end-to-end SLU systems. While processing a spoken utterance, our proposed RNN transducer (RNN-T) based SLU model has access to its dialog history in the form of decoded transcripts and SLU labels of previous turns. We encode the dialog history as BERT embeddings, and use them as an additional input to the SLU model along with the speech features for the current utterance. We evaluate our approach on a recently released spoken dialog data set, the HarperValleyBank corpus. We observe significant improvements: 8% for dialog action and 30% for caller intent recognition tasks, in comparison to a competitive context independent end-to-end baseline system.

</details>

### [A Light-weight contextual spelling correction model for customizing transducer-based speech recognition systems](2108.07493.md)
**Xiaoqiang Wang, Yanqing Liu, Sheng Zhao, Jinyu Li** · 2021-08-17

<details>
<summary>Abstract</summary>

It's challenging to customize transducer-based automatic speech recognition (ASR) system with context information which is dynamic and unavailable during model training. In this work, we introduce a light-weight contextual spelling correction model to correct context-related recognition errors in transducer-based ASR systems. We incorporate the context information into the spelling correction model with a shared context encoder and use a filtering algorithm to handle large-size context lists. Experiments show that the model improves baseline ASR model performance with about 50% relative word error rate reduction, which also significantly outperforms the baseline method such as contextual LM biasing. The model also shows excellent performance for out-of-vocabulary terms not seen during training.

</details>

### [Dereverberation of Autoregressive Envelopes for Far-field Speech Recognition](2108.05520.md)
**Anurenjan Purushothaman, Anirudh Sreeram, Rohit Kumar, Sriram Ganapathy** · 2021-08-12

<details>
<summary>Abstract</summary>

The task of speech recognition in far-field environments is adversely affected by the reverberant artifacts that elicit as the temporal smearing of the sub-band envelopes. In this paper, we develop a neural model for speech dereverberation using the long-term sub-band envelopes of speech. The sub-band envelopes are derived using frequency domain linear prediction (FDLP) which performs an autoregressive estimation of the Hilbert envelopes. The neural dereverberation model estimates the envelope gain which when applied to reverberant signals suppresses the late reflection components in the far-field signal. The dereverberated envelopes are used for feature extraction in speech recognition. Further, the sequence of steps involved in envelope dereverberation, feature extraction and acoustic modeling for ASR can be implemented as a single neural processing pipeline which allows the joint learning of the dereverberation network and the acoustic model. Several experiments are performed on the REVERB challenge dataset, CHiME-3 dataset and VOiCES dataset. In these experiments, the joint learning of envelope dereverberation and acoustic model yields significant performance improvements over the baseline ASR system based on log-mel spectrogram as well as other past approaches for dereverberation (average relative improvements of 10-24% over the baseline system). A detailed analysis on the choice of hyper-parameters and the cost function involved in envelope dereverberation is also provided.

</details>

### [On The Compensation Between Magnitude and Phase in Speech Separation](2108.05470.md)
**Zhong-Qiu Wang, Gordon Wichern, Jonathan Le Roux** · 2021-08-11

<details>
<summary>Abstract</summary>

Deep neural network (DNN) based end-to-end optimization in the complex time-frequency (T-F) domain or time domain has shown considerable potential in monaural speech separation. Many recent studies optimize loss functions defined solely in the time or complex domain, without including a loss on magnitude. Although such loss functions typically produce better scores if the evaluation metrics are objective time-domain metrics, they however produce worse scores on speech quality and intelligibility metrics and usually lead to worse speech recognition performance, compared with including a loss on magnitude. While this phenomenon has been experimentally observed by many studies, it is often not accurately explained and there lacks a thorough understanding on its fundamental cause. This paper provides a novel view from the perspective of the implicit compensation between estimated magnitude and phase. Analytical results based on monaural speech separation and robust automatic speech recognition (ASR) tasks in noisy-reverberant conditions support the validity of our view.

</details>

### [End-to-End Speech Recognition With Joint Dereverberation Of Sub-Band Autoregressive Envelopes](2108.03975.md)
**Rohit Kumar, Anurenjan Purushothaman, Anirudh Sreeram, Sriram Ganapathy** · 2021-08-09

<details>
<summary>Abstract</summary>

The end-to-end (E2E) automatic speech recognition (ASR) systems are often required to operate in reverberant conditions, where the long-term sub-band envelopes of the speech are temporally smeared. In this paper, we develop a feature enhancement approach using a neural model operating on sub-band temporal envelopes. The temporal envelopes are modeled using the framework of frequency domain linear prediction (FDLP). The neural enhancement model proposed in this paper performs an envelope gain based enhancement of temporal envelopes. The model architecture consists of a combination of convolutional and long short term memory (LSTM) neural network layers. Further, the envelope dereverberation, feature extraction and acoustic modeling using transformer based E2E ASR can all be jointly optimized for the speech recognition task. The joint optimization ensures that the dereverberation model targets the ASR cost function. We perform E2E speech recognition experiments on the REVERB challenge dataset as well as on the VOiCES dataset. In these experiments, the proposed joint modeling approach yields significant improvements compared to the baseline E2E ASR system (average relative improvements of 21% on the REVERB challenge dataset and about 10% on the VOiCES dataset).

</details>

### [The HW-TSC's Offline Speech Translation Systems for IWSLT 2021 Evaluation](2108.03845.md)
**Minghan Wang, Yuxia Wang, Chang Su, Jiaxin Guo et al.** · 2021-08-09

<details>
<summary>Abstract</summary>

This paper describes our work in participation of the IWSLT-2021 offline speech translation task. Our system was built in a cascade form, including a speaker diarization module, an Automatic Speech Recognition (ASR) module and a Machine Translation (MT) module. We directly use the LIUM SpkDiarization tool as the diarization module. The ASR module is trained with three ASR datasets from different sources, by multi-source training, using a modified Transformer encoder. The MT module is pretrained on the large-scale WMT news translation dataset and fine-tuned on the TED corpus. Our method achieves 24.6 BLEU score on the 2021 test set.

</details>

### [Time-Frequency Localization Using Deep Convolutional Maxout Neural Network in Persian Speech Recognition](2108.03818.md)
**Arash Dehghani, Seyyed Ali Seyyedsalehi** · 2021-08-09

<details>
<summary>Abstract</summary>

In this paper, a CNN-based structure for the time-frequency localization of information is proposed for Persian speech recognition. Research has shown that the receptive fields' spectrotemporal plasticity of some neurons in mammals' primary auditory cortex and midbrain makes localization facilities improve recognition performance. Over the past few years, much work has been done to localize time-frequency information in ASR systems, using the spatial or temporal immutability properties of methods such as HMMs, TDNNs, CNNs, and LSTM-RNNs. However, most of these models have large parameter volumes and are challenging to train. For this purpose, we have presented a structure called Time-Frequency Convolutional Maxout Neural Network (TFCMNN) in which parallel time-domain and frequency-domain 1D-CMNNs are applied simultaneously and independently to the spectrogram, and then their outputs are concatenated and applied jointly to a fully connected Maxout network for classification. To improve the performance of this structure, we have used newly developed methods and models such as Dropout, maxout, and weight normalization. Two sets of experiments were designed and implemented on the FARSDAT dataset to evaluate the performance of this model compared to conventional 1D-CMNN models. According to the experimental results, the average recognition score of TFCMNN models is about 1.6% higher than the average of conventional 1D-CMNN models. In addition, the average training time of the TFCMNN models is about 17 hours lower than the average training time of traditional models. Therefore, as proven in other sources, time-frequency localization in ASR systems increases system accuracy and speeds up the training process.

</details>

### [Spatio-Temporal Attention Mechanism and Knowledge Distillation for Lip Reading](2108.03543.md)
**Shahd Elashmawy, Marian Ramsis, Hesham M. Eraqi, Farah Eldeshnawy et al.** · 2021-08-07

<details>
<summary>Abstract</summary>

Despite the advancement in the domain of audio and audio-visual speech recognition, visual speech recognition systems are still quite under-explored due to the visual ambiguity of some phonemes. In this work, we propose a new lip-reading model that combines three contributions. First, the model front-end adopts a spatio-temporal attention mechanism to help extract the informative data from the input visual frames. Second, the model back-end utilizes a sequence-level and frame-level Knowledge Distillation (KD) techniques that allow leveraging audio data during the visual model training. Third, a data preprocessing pipeline is adopted that includes facial landmarks detection-based lip-alignment. On LRW lip-reading dataset benchmark, a noticeable accuracy improvement is demonstrated; the spatio-temporal attention, Knowledge Distillation, and lip-alignment contributions achieved 88.43%, 88.64%, and 88.37% respectively.

</details>

### [An empirical assessment of deep learning approaches to task-oriented dialog management](2108.03478.md)
**Lukáš Matějů, David Griol, Zoraida Callejas, José Manuel Molina et al.** · 2021-08-07

<details>
<summary>Abstract</summary>

Deep learning is providing very positive results in areas related to conversational interfaces, such as speech recognition, but its potential benefit for dialog management has still not been fully studied. In this paper, we perform an assessment of different configurations for deep-learned dialog management with three dialog corpora from different application domains and varying in size, dimensionality and possible system responses. Our results have allowed us to identify several aspects that can have an impact on accuracy, including the approaches used for feature extraction, input representation, context consideration and the hyper-parameters of the deep neural networks employed.

</details>

### [Knowledge Distillation from BERT Transformer to Speech Transformer for Intent Classification](2108.02598.md)
**Yidi Jiang, Bidisha Sharma, Maulik Madhavi, Haizhou Li** · 2021-08-05

<details>
<summary>Abstract</summary>

End-to-end intent classification using speech has numerous advantages compared to the conventional pipeline approach using automatic speech recognition (ASR), followed by natural language processing modules. It attempts to predict intent from speech without using an intermediate ASR module. However, such end-to-end framework suffers from the unavailability of large speech resources with higher acoustic variation in spoken language understanding. In this work, we exploit the scope of the transformer distillation method that is specifically designed for knowledge distillation from a transformer based language model to a transformer based speech model. In this regard, we leverage the reliable and widely used bidirectional encoder representations from transformers (BERT) model as a language model and transfer the knowledge to build an acoustic model for intent classification using the speech. In particular, a multilevel transformer based teacher-student model is designed, and knowledge distillation is performed across attention and hidden sub-layers of different transformer layers of the student and teacher models. We achieve an intent classification accuracy of 99.10% and 88.79% for Fluent speech corpus and ATIS database, respectively. Further, the proposed method demonstrates better performance and robustness in acoustically degraded condition compared to the baseline method.

</details>

### [From Textual to Verbal Communication: Towards Applying Sentiment Analysis to a Software Project Meeting](2108.01985.md)
**Marc Herrmann, Jil Klünder** · 2021-08-04

<details>
<summary>Abstract</summary>

Sentiment analysis gets increasing attention in software engineering with new tools emerging from new insights provided by researchers. Existing use cases and tools are meant to be used for textual communication such as comments on collaborative version control systems. While this can already provide useful feedback for development teams, a lot of communication takes place in meetings and is not suited for present tool designs and concepts. In this paper, we present a concept that is capable of processing live meeting audio and classifying transcribed statements into sentiment polarity classes. We combine the latest advances in open source speech recognition with previous research in sentiment analysis. We tested our approach on a student software project meeting to gain proof of concept, showing moderate agreement between the classifications of our tool and a human observer on the meeting audio. Despite the preliminary character of our study, we see promising results motivating future research in sentiment analysis on meetings. For example, the polarity classification can be extended to detect destructive behaviour that can endanger project success.

</details>

### [Blind and neural network-guided convolutional beamformer for joint denoising, dereverberation, and source separation](2108.01836.md)
**Tomohiro Nakatani, Rintaro Ikeshita, Keisuke Kinoshita, Hiroshi Sawada et al.** · 2021-08-04

<details>
<summary>Abstract</summary>

This paper proposes an approach for optimizing a Convolutional BeamFormer (CBF) that can jointly perform denoising (DN), dereverberation (DR), and source separation (SS). First, we develop a blind CBF optimization algorithm that requires no prior information on the sources or the room acoustics, by extending a conventional joint DR and SS method. For making the optimization computationally tractable, we incorporate two techniques into the approach: the Source-Wise Factorization (SW-Fact) of a CBF and the Independent Vector Extraction (IVE). To further improve the performance, we develop a method that integrates a neural network(NN) based source power spectra estimation with CBF optimization by an inverse-Gamma prior. Experiments using noisy reverberant mixtures reveal that our proposed method with both blind and NN-guided scenarios greatly outperforms the conventional state-of-the-art NN-supported mask-based CBF in terms of the improvement in automatic speech recognition and signal distortion reduction performance.

</details>

### [Improving Distinction between ASR Errors and Speech Disfluencies with Feature Space Interpolation](2108.01812.md)
**Seongmin Park, Dongchan Shin, Sangyoun Paik, Subong Choi et al.** · 2021-08-04

<details>
<summary>Abstract</summary>

Fine-tuning pretrained language models (LMs) is a popular approach to automatic speech recognition (ASR) error detection during post-processing. While error detection systems often take advantage of statistical language archetypes captured by LMs, at times the pretrained knowledge can hinder error detection performance. For instance, presence of speech disfluencies might confuse the post-processing system into tagging disfluent but accurate transcriptions as ASR errors. Such confusion occurs because both error detection and disfluency detection tasks attempt to identify tokens at statistically unlikely positions. This paper proposes a scheme to improve existing LM-based ASR error detection systems, both in terms of detection scores and resilience to such distracting auxiliary tasks. Our approach adopts the popular mixup method in text feature space and can be utilized with any black-box ASR output. To demonstrate the effectiveness of our method, we conduct post-processing experiments with both traditional and end-to-end ASR systems (both for English and Korean languages) with 5 different speech corpora. We find that our method improves both ASR error detection F 1 scores and reduces the number of correctly transcribed disfluencies wrongly detected as ASR errors. Finally, we suggest methods to utilize resulting LMs directly in semi-supervised ASR training.

</details>

### [With One Voice: Composing a Travel Voice Assistant from Re-purposed Models](2108.11463.md)
**Shachaf Poran, Gil Amsalem, Amit Beka, Dmitri Goldenberg** · 2021-08-04

<details>
<summary>Abstract</summary>

Voice assistants provide users a new way of interacting with digital products, allowing them to retrieve information and complete tasks with an increased sense of control and flexibility. Such products are comprised of several machine learning models, like Speech-to-Text transcription, Named Entity Recognition and Resolution, and Text Classification. Building a voice assistant from scratch takes the prolonged efforts of several teams constructing numerous models and orchestrating between components. Alternatives such as using third-party vendors or re-purposing existing models may be considered to shorten time-to-market and development costs. However, each option has its benefits and drawbacks. We present key insights from building a voice search assistant for Booking.com search and recommendation system. Our paper compares the achieved performance and development efforts in dedicated tailor-made solutions against existing re-purposed models. We share and discuss our data-driven decisions about implementation trade-offs and their estimated outcomes in hindsight, showing that a fully functional machine learning product can be built from existing models.

</details>

### [Information Sieve: Content Leakage Reduction in End-to-End Prosody For Expressive Speech Synthesis](2108.01831.md)
**Xudong Dai, Cheng Gong, Longbiao Wang, Kaili Zhang** · 2021-08-04

<details>
<summary>Abstract</summary>

Expressive neural text-to-speech (TTS) systems incorporate a style encoder to learn a latent embedding as the style information. However, this embedding process may encode redundant textual information. This phenomenon is called content leakage. Researchers have attempted to resolve this problem by adding an ASR or other auxiliary supervision loss functions. In this study, we propose an unsupervised method called the "information sieve" to reduce the effect of content leakage in prosody transfer. The rationale of this approach is that the style encoder can be forced to focus on style information rather than on textual information contained in the reference speech by a well-designed downsample-upsample filter, i.e., the extracted style embeddings can be downsampled at a certain interval and then upsampled by duplication. Furthermore, we used instance normalization in convolution layers to help the system learn a better latent style space. Objective metrics such as the significantly lower word error rate (WER) demonstrate the effectiveness of this model in mitigating content leakage. Listening tests indicate that the model retains its prosody transferability compared with the baseline models such as the original GST-Tacotron and ASR-guided Tacotron.

</details>

### [Bifocal Neural ASR: Exploiting Keyword Spotting for Inference Optimization](2108.01704.md)
**Jonathan Macoskey, Grant P. Strimel, Ariya Rastrow** · 2021-08-03

<details>
<summary>Abstract</summary>

We present Bifocal RNN-T, a new variant of the Recurrent Neural Network Transducer (RNN-T) architecture designed for improved inference time latency on speech recognition tasks. The architecture enables a dynamic pivot for its runtime compute pathway, namely taking advantage of keyword spotting to select which component of the network to execute for a given audio frame. To accomplish this, we leverage a recurrent cell we call the Bifocal LSTM (BFLSTM), which we detail in the paper. The architecture is compatible with other optimization strategies such as quantization, sparsification, and applying time-reduction layers, making it especially applicable for deployed, real-time speech recognition settings. We present the architecture and report comparative experimental results on voice-assistant speech recognition tasks. Specifically, we show our proposed Bifocal RNN-T can improve inference cost by 29.1% with matching word error rates and only a minor increase in memory size.

</details>

### [Learning a Neural Diff for Speech Models](2108.01561.md)
**Jonathan Macoskey, Grant P. Strimel, Ariya Rastrow** · 2021-08-03

<details>
<summary>Abstract</summary>

As more speech processing applications execute locally on edge devices, a set of resource constraints must be considered. In this work we address one of these constraints, namely over-the-network data budgets for transferring models from server to device. We present neural update approaches for release of subsequent speech model generations abiding by a data budget. We detail two architecture-agnostic methods which learn compact representations for transmission to devices. We experimentally validate our techniques with results on two tasks (automatic speech recognition and spoken language understanding) on open source data sets by demonstrating when applied in succession, our budgeted updates outperform comparable model compression baselines by significant margins.

</details>

### [Amortized Neural Networks for Low-Latency Speech Recognition](2108.01553.md)
**Jonathan Macoskey, Grant P. Strimel, Jinru Su, Ariya Rastrow** · 2021-08-03

<details>
<summary>Abstract</summary>

We introduce Amortized Neural Networks (AmNets), a compute cost- and latency-aware network architecture particularly well-suited for sequence modeling tasks. We apply AmNets to the Recurrent Neural Network Transducer (RNN-T) to reduce compute cost and latency for an automatic speech recognition (ASR) task. The AmNets RNN-T architecture enables the network to dynamically switch between encoder branches on a frame-by-frame basis. Branches are constructed with variable levels of compute cost and model capacity. Here, we achieve variable compute for two well-known candidate techniques: one using sparse pruning and the other using matrix factorization. Frame-by-frame switching is determined by an arbitrator network that requires negligible compute overhead. We present results using both architectures on LibriSpeech data and show that our proposed architecture can reduce inference cost by up to 45\% and latency to nearly real-time without incurring a loss in accuracy.

</details>

### [A Study of Multilingual End-to-End Speech Recognition for Kazakh, Russian, and English](2108.01280.md)
**Saida Mussakhojayeva, Yerbolat Khassanov, Huseyin Atakan Varol** · 2021-08-03

<details>
<summary>Abstract</summary>

We study training a single end-to-end (E2E) automatic speech recognition (ASR) model for three languages used in Kazakhstan: Kazakh, Russian, and English. We first describe the development of multilingual E2E ASR based on Transformer networks and then perform an extensive assessment on the aforementioned languages. We also compare two variants of output grapheme set construction: combined and independent. Furthermore, we evaluate the impact of LMs and data augmentation techniques on the recognition performance of the multilingual E2E ASR. In addition, we present several datasets for training and evaluation purposes. Experiment results show that the multilingual models achieve comparable performances to the monolingual baselines with a similar number of parameters. Our best monolingual and multilingual models achieved 20.9% and 20.5% average word error rates on the combined test set, respectively. To ensure the reproducibility of our experiments and results, we share our training recipes, datasets, and pre-trained models.

</details>

### [User-Initiated Repetition-Based Recovery in Multi-Utterance Dialogue Systems](2108.01208.md)
**Hoang Long Nguyen, Vincent Renkens, Joris Pelemans, Srividya Pranavi Potharaju et al.** · 2021-08-02

<details>
<summary>Abstract</summary>

Recognition errors are common in human communication. Similar errors often lead to unwanted behaviour in dialogue systems or virtual assistants. In human communication, we can recover from them by repeating misrecognized words or phrases; however in human-machine communication this recovery mechanism is not available. In this paper, we attempt to bridge this gap and present a system that allows a user to correct speech recognition errors in a virtual assistant by repeating misunderstood words. When a user repeats part of the phrase the system rewrites the original query to incorporate the correction. This rewrite allows the virtual assistant to understand the original query successfully. We present an end-to-end 2-step attention pointer network that can generate the the rewritten query by merging together the incorrectly understood utterance with the correction follow-up. We evaluate the model on data collected for this task and compare the proposed model to a rule-based baseline and a standard pointer network. We show that rewriting the original query is an effective way to handle repetition-based recovery and that the proposed model outperforms the rule based baseline, reducing Word Error Rate by 19% relative at 2% False Alarm Rate on annotated data.

</details>

### [MOHAQ: Multi-Objective Hardware-Aware Quantization of Recurrent Neural Networks](2108.01192.md)
**Nesma M. Rezk, Tomas Nordström, Dimitrios Stathis, Zain Ul-Abdin et al.** · 2021-08-02

<details>
<summary>Abstract</summary>

The compression of deep learning models is of fundamental importance in deploying such models to edge devices. The selection of compression parameters can be automated to meet changes in the hardware platform and application using optimization algorithms. This article introduces a Multi-Objective Hardware-Aware Quantization (MOHAQ) method, which considers hardware efficiency and inference error as objectives for mixed-precision quantization. The proposed method feasibly evaluates candidate solutions in a large search space by relying on two steps. First, post-training quantization is applied for fast solution evaluation (inference-only search). Second, we propose the "beacon-based search" to retrain selected solutions only and use them as beacons to know the effect of retraining on other solutions. We use a speech recognition model based on Simple Recurrent Unit (SRU) using the TIMIT dataset and apply our method to run on SiLago and Bitfusion platforms. We provide experimental evaluations showing that SRU can be compressed up to 8x by post-training quantization without any significant error increase. On SiLago, we found solutions that achieve 97\% and 86\% of the maximum possible speedup and energy saving, with a minor increase in error. On Bitfusion, beacon-based search reduced the error gain of inference-only search by up to 4.9 percentage points.

</details>

### [Decoupling recognition and transcription in Mandarin ASR](2108.01129.md)
**Jiahong Yuan, Xingyu Cai, Dongji Gao, Renjie Zheng et al.** · 2021-08-02

<details>
<summary>Abstract</summary>

Much of the recent literature on automatic speech recognition (ASR) is taking an end-to-end approach. Unlike English where the writing system is closely related to sound, Chinese characters (Hanzi) represent meaning, not sound. We propose factoring audio -> Hanzi into two sub-tasks: (1) audio -> Pinyin and (2) Pinyin -> Hanzi, where Pinyin is a system of phonetic transcription of standard Chinese. Factoring the audio -> Hanzi task in this way achieves 3.9% CER (character error rate) on the Aishell-1 corpus, the best result reported on this dataset so far.

</details>

### [Automatic recognition of suprasegmentals in speech](2108.01122.md)
**Jiahong Yuan, Neville Ryant, Xingyu Cai, Kenneth Church et al.** · 2021-08-02

<details>
<summary>Abstract</summary>

This study reports our efforts to improve automatic recognition of suprasegmentals by fine-tuning wav2vec 2.0 with CTC, a method that has been successful in automatic speech recognition. We demonstrate that the method can improve the state-of-the-art on automatic recognition of syllables, tones, and pitch accents. Utilizing segmental information, by employing tonal finals or tonal syllables as recognition units, can significantly improve Mandarin tone recognition. Language models are helpful when tonal syllables are used as recognition units, but not helpful when tones are recognition units. Finally, Mandarin tone recognition can benefit from English phoneme recognition by combining the two tasks in fine-tuning wav2vec 2.0.

</details>

### [Adversarial Data Augmentation for Disordered Speech Recognition](2108.00899.md)
**Zengrui Jin, Mengzhe Geng, Xurong Xie, Jianwei Yu et al.** · 2021-08-02

<details>
<summary>Abstract</summary>

Automatic recognition of disordered speech remains a highly challenging task to date. The underlying neuro-motor conditions, often compounded with co-occurring physical disabilities, lead to the difficulty in collecting large quantities of impaired speech required for ASR system development. To this end, data augmentation techniques play a vital role in current disordered speech recognition systems. In contrast to existing data augmentation techniques only modifying the speaking rate or overall shape of spectral contour, fine-grained spectro-temporal differences between disordered and normal speech are modelled using deep convolutional generative adversarial networks (DCGAN) during data augmentation to modify normal speech spectra into those closer to disordered speech. Experiments conducted on the UASpeech corpus suggest the proposed adversarial data augmentation approach consistently outperformed the baseline augmentation methods using tempo or speed perturbation on a state-of-the-art hybrid DNN system. An overall word error rate (WER) reduction up to 3.05\% (9.7\% relative) was obtained over the baseline system using no data augmentation. The final learning hidden unit contribution (LHUC) speaker adapted system using the best adversarial augmentation approach gives an overall WER of 25.89% on the UASpeech test set of 16 dysarthric speakers.

</details>

### [Online quantum time series processing with random oscillator networks](2108.00698.md)
**Johannes Nokkala** · 2021-08-02

<details>
<summary>Abstract</summary>

Reservoir computing is a powerful machine learning paradigm for online time series processing. It has reached state-of-the-art performance in tasks such as chaotic time series prediction and continuous speech recognition thanks to its unique combination of high computational power and low training cost which sets it aside from alternatives such as traditionally trained recurrent neural networks, and furthermore is amenable to implementations in dedicated hardware, potentially leading to extremely compact and efficient reservoir computers. Recently the use of random quantum systems has been proposed, leveraging the complexity of quantum dynamics for classical time series processing. Extracting the output from a quantum system without disturbing its state too much is problematic however, and can be expected to become a bottleneck in such approaches. Here we propose a reservoir computing inspired approach to online processing of time series consisting of quantum information, sidestepping the measurement problem. We illustrate its power by generalizing two paradigmatic benchmark tasks from classical reservoir computing to quantum information and introducing a task without a classical analogue where a random system is trained to both create and distribute entanglement between systems that never directly interact. Finally, we discuss partial generalizations where only the input or only the output time series is quantum.

</details>

### [Adversarial Robustness of Deep Code Comment Generation](2108.00213.md)
**Yu Zhou, Xiaoqing Zhang, Juanjuan Shen, Tingting Han et al.** · 2021-07-31

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have shown remarkable performance in a variety of domains such as computer vision, speech recognition, or natural language processing. Recently they also have been applied to various software engineering tasks, typically involving processing source code. DNNs are well-known to be vulnerable to adversarial examples, i.e., fabricated inputs that could lead to various misbehaviors of the DNN model while being perceived as benign by humans. In this paper, we focus on the code comment generation task in software engineering and study the robustness issue of the DNNs when they are applied to this task. We propose ACCENT, an identifier substitution approach to craft adversarial code snippets, which are syntactically correct and semantically close to the original code snippet, but may mislead the DNNs to produce completely irrelevant code comments. In order to improve the robustness, ACCENT also incorporates a novel training method, which can be applied to existing code comment generation models. We conduct comprehensive experiments to evaluate our approach by attacking the mainstream encoder-decoder architectures on two large-scale publicly available datasets. The results show that ACCENT efficiently produces stable attacks with functionality-preserving adversarial examples, and the generated examples have better transferability compared with baselines. We also confirm, via experiments, the effectiveness in improving model robustness with our training method.

</details>

### [Can You Hear It? Backdoor Attacks via Ultrasonic Triggers](2107.14569.md)
**Stefanos Koffas, Jing Xu, Mauro Conti, Stjepan Picek** · 2021-07-30

<details>
<summary>Abstract</summary>

This work explores backdoor attacks for automatic speech recognition systems where we inject inaudible triggers. By doing so, we make the backdoor attack challenging to detect for legitimate users, and thus, potentially more dangerous. We conduct experiments on two versions of a speech dataset and three neural networks and explore the performance of our attack concerning the duration, position, and type of the trigger. Our results indicate that less than 1% of poisoned data is sufficient to deploy a backdoor attack and reach a 100% attack success rate. We observed that short, non-continuous triggers result in highly successful attacks. However, since our trigger is inaudible, it can be as long as possible without raising any suspicions making the attack more effective. Finally, we conducted our attack in actual hardware and saw that an adversary could manipulate inference in an Android application by playing the inaudible trigger over the air.

</details>

### [USC: An Open-Source Uzbek Speech Corpus and Initial Speech Recognition Experiments](2107.14419.md)
**Muhammadjon Musaev, Saida Mussakhojayeva, Ilyos Khujayorov, Yerbolat Khassanov et al.** · 2021-07-30

<details>
<summary>Abstract</summary>

We present a freely available speech corpus for the Uzbek language and report preliminary automatic speech recognition (ASR) results using both the deep neural network hidden Markov model (DNN-HMM) and end-to-end (E2E) architectures. The Uzbek speech corpus (USC) comprises 958 different speakers with a total of 105 hours of transcribed audio recordings. To the best of our knowledge, this is the first open-source Uzbek speech corpus dedicated to the ASR task. To ensure high quality, the USC has been manually checked by native speakers. We first describe the design and development procedures of the USC, and then explain the conducted ASR experiments in detail. The experimental results demonstrate promising results for the applicability of the USC for ASR. Specifically, 18.1% and 17.4% word error rates were achieved on the validation and test sets, respectively. To enable experiment reproducibility, we share the USC dataset, pre-trained models, and training recipes in our GitHub repository.

</details>

### [Adapting GPT, GPT-2 and BERT Language Models for Speech Recognition](2108.07789.md)
**Xianrui Zheng, Chao Zhang, Philip C. Woodland** · 2021-07-29

<details>
<summary>Abstract</summary>

Language models (LMs) pre-trained on massive amounts of text, in particular bidirectional encoder representations from Transformers (BERT), generative pre-training (GPT), and GPT-2, have become a key technology for many natural language processing tasks. In this paper, we present results using fine-tuned GPT, GPT-2, and their combination for automatic speech recognition (ASR). Unlike unidirectional LM GPT and GPT-2, BERT is bidirectional whose direct product of the output probabilities is no longer a valid language prior probability. A conversion method is proposed to compute the correct language prior probability based on bidirectional LM outputs in a mathematically exact way. Experimental results on the widely used AMI and Switchboard ASR tasks showed that the combination of the fine-tuned GPT and GPT-2 outperformed the combination of three neural LMs with different architectures trained from scratch on the in-domain text by up to a 12% relative word error rate reduction (WERR). Furthermore, on the AMI corpus, the proposed conversion for language prior probabilities enables BERT to obtain an extra 3% relative WERR, and the combination of BERT, GPT and GPT-2 results in further improvements.

</details>

### [An Adapter Based Pre-Training for Efficient and Scalable Self-Supervised Speech Representation Learning](2107.13530.md)
**Samuel Kessler, Bethan Thomas, Salah Karout** · 2021-07-26

<details>
<summary>Abstract</summary>

We present a method for transferring pre-trained self-supervised (SSL) speech representations to multiple languages. There is an abundance of unannotated speech, so creating self-supervised representations from raw audio and fine-tuning on small annotated datasets is a promising direction to build speech recognition systems. SSL models generally perform SSL on raw audio in a pre-training phase and then fine-tune on a small fraction of annotated data. Such models have produced state of the art results for ASR. However, these models are very expensive to pre-train. We use an existing wav2vec 2.0 model and tackle the problem of learning new language representations while utilizing existing model knowledge. Crucially we do so without catastrophic forgetting of the existing language representation. We use adapter modules to speed up pre-training a new language task. Our model can decrease pre-training times by 32% when learning a new language task, and learn this new audio-language representation without forgetting previous language representation. We evaluate by applying these language representations to automatic speech recognition.

</details>

### [Facetron: A Multi-speaker Face-to-Speech Model based on Cross-modal Latent Representations](2107.12003.md)
**Se-Yun Um, Jihyun Kim, Jihyun Lee, Hong-Goo Kang** · 2021-07-26

<details>
<summary>Abstract</summary>

In this paper, we propose a multi-speaker face-to-speech waveform generation model that also works for unseen speaker conditions. Using a generative adversarial network (GAN) with linguistic and speaker characteristic features as auxiliary conditions, our method directly converts face images into speech waveforms under an end-to-end training framework. The linguistic features are extracted from lip movements using a lip-reading model, and the speaker characteristic features are predicted from face images using cross-modal learning with a pre-trained acoustic model. Since these two features are uncorrelated and controlled independently, we can flexibly synthesize speech waveforms whose speaker characteristics vary depending on the input face images. We show the superiority of our proposed model over conventional methods in terms of objective and subjective evaluation results. Specifically, we evaluate the performances of linguistic features by measuring their accuracy on an automatic speech recognition task. In addition, we estimate speaker and gender similarity for multi-speaker and unseen conditions, respectively. We also evaluate the aturalness of the synthesized speech waveforms using a mean opinion score (MOS) test and non-intrusive objective speech quality assessment (NISQA).The demo samples of the proposed and other models are available at https://sam-0927.github.io/

</details>

### [Brazilian Portuguese Speech Recognition Using Wav2vec 2.0](2107.11414.md)
**Lucas Rafael Stefanel Gris, Edresson Casanova, Frederico Santos de Oliveira, Anderson da Silva Soares et al.** · 2021-07-23

<details>
<summary>Abstract</summary>

Deep learning techniques have been shown to be efficient in various tasks, especially in the development of speech recognition systems, that is, systems that aim to transcribe an audio sentence in a sequence of written words. Despite the progress in the area, speech recognition can still be considered difficult, especially for languages lacking available data, such as Brazilian Portuguese (BP). In this sense, this work presents the development of an public Automatic Speech Recognition (ASR) system using only open available audio data, from the fine-tuning of the Wav2vec 2.0 XLSR-53 model pre-trained in many languages, over BP data. The final model presents an average word error rate of 12.4% over 7 different datasets (10.5% when applying a language model). According to our knowledge, the obtained error is the lowest among open end-to-end (E2E) ASR models for BP.

</details>

### [Using Deep Learning Techniques and Inferential Speech Statistics for AI Synthesised Speech Recognition](2107.11412.md)
**Arun Kumar Singh, Priyanka Singh, Karan Nathwani** · 2021-07-23

<details>
<summary>Abstract</summary>

The recent developments in technology have re-warded us with amazing audio synthesis models like TACOTRON and WAVENETS. On the other side, it poses greater threats such as speech clones and deep fakes, that may go undetected. To tackle these alarming situations, there is an urgent need to propose models that can help discriminate a synthesized speech from an actual human speech and also identify the source of such a synthesis. Here, we propose a model based on Convolutional Neural Network (CNN) and Bidirectional Recurrent Neural Network (BiRNN) that helps to achieve both the aforementioned objectives. The temporal dependencies present in AI synthesized speech are exploited using Bidirectional RNN and CNN. The model outperforms the state-of-the-art approaches by classifying the AI synthesized audio from real human speech with an error rate of 1.9% and detecting the underlying architecture with an accuracy of 97%.

</details>

### [OLR 2021 Challenge: Datasets, Rules and Baselines](2107.11113.md)
**Binling Wang, Wenxuan Hu, Jing Li, Yiming Zhi et al.** · 2021-07-23

<details>
<summary>Abstract</summary>

This paper introduces the sixth Oriental Language Recognition (OLR) 2021 Challenge, which intends to improve the performance of language recognition systems and speech recognition systems within multilingual scenarios. The data profile, four tasks, two baselines, and the evaluation principles are introduced in this paper. In addition to the Language Identification (LID) tasks, multilingual Automatic Speech Recognition (ASR) tasks are introduced to OLR 2021 Challenge for the first time. The challenge this year focuses on more practical and challenging problems, with four tasks: (1) constrained LID, (2) unconstrained LID, (3) constrained multilingual ASR, (4) unconstrained multilingual ASR. Baselines for LID tasks and multilingual ASR tasks are provided, respectively. The LID baseline system is an extended TDNN x-vector model constructed with Pytorch. A transformer-based end-to-end model is provided as the multilingual ASR baseline system. These recipes will be online published, and available for participants to construct their own LID or ASR systems. The baseline results demonstrate that those tasks are rather challenging and deserve more effort to achieve better performance.

</details>

### [CarneliNet: Neural Mixture Model for Automatic Speech Recognition](2107.10708.md)
**Aleksei Kalinov, Somshubra Majumdar, Jagadeesh Balam, Boris Ginsburg** · 2021-07-22

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition systems have achieved great accuracy by using deeper and deeper models. However, the increased depth comes with a larger receptive field that can negatively impact model performance in streaming scenarios. We propose an alternative approach that we call Neural Mixture Model. The basic idea is to introduce a parallel mixture of shallow networks instead of a very deep network. To validate this idea we design CarneliNet -- a CTC-based neural network composed of three mega-blocks. Each mega-block consists of multiple parallel shallow sub-networks based on 1D depthwise-separable convolutions. We evaluate the model on LibriSpeech, MLS and AISHELL-2 datasets and achieved close to state-of-the-art results for CTC-based models. Finally, we demonstrate that one can dynamically reconfigure the number of parallel sub-networks to accommodate the computational requirements without retraining.

</details>

### [Multitask-Based Joint Learning Approach To Robust ASR For Radio Communication Speech](2107.10701.md)
**Duo Ma, Nana Hou, Van Tung Pham, Haihua Xu et al.** · 2021-07-22

<details>
<summary>Abstract</summary>

To realize robust end-to-end Automatic Speech Recognition(E2E ASR) under radio communication condition, we propose a multitask-based method to joint train a Speech Enhancement (SE) module as the front-end and an E2E ASR model as the back-end in this paper. One of the advantage of the proposed method is that the entire system can be trained from scratch. Different from prior works, either component here doesn't need to perform pre-training and fine-tuning processes separately. Through analysis, we found that the success of the proposed method lies in the following aspects. Firstly, multitask learning is essential, that is the SE network is not only learning to produce more Intelligent speech, it is also aimed to generate speech that is beneficial to recognition. Secondly, we also found speech phase preserved from noisy speech is critical for improving ASR performance. Thirdly, we propose a dual channel data augmentation training method to obtain further improvement.Specifically, we combine the clean and enhanced speech to train the whole system. We evaluate the proposed method on the RATS English data set, achieving a relative WER reduction of 4.6% with the joint training method, and up to a relative WER reduction of 11.2% with the proposed data augmentation method.

</details>

### [Semantic Communications for Speech Recognition](2107.11190.md)
**Zhenzi Weng, Zhijin Qin, Geoffrey Ye Li** · 2021-07-22

<details>
<summary>Abstract</summary>

The traditional communications transmit all the source data represented by bits, regardless of the content of source and the semantic information required by the receiver. However, in some applications, the receiver only needs part of the source data that represents critical semantic information, which prompts to transmit the application-related information, especially when bandwidth resources are limited. In this paper, we consider a semantic communication system for speech recognition by designing the transceiver as an end-to-end (E2E) system. Particularly, a deep learning (DL)-enabled semantic communication system, named DeepSC-SR, is developed to learn and extract text-related semantic features at the transmitter, which motivates the system to transmit much less than the source speech data without performance degradation. Moreover, in order to facilitate the proposed DeepSC-SR for dynamic channel environments, we investigate a robust model to cope with various channel environments without requiring retraining. The simulation results demonstrate that our proposed DeepSC-SR outperforms the traditional communication systems in terms of the speech recognition metrics, such as character-error-rate and word-error-rate, and is more robust to channel variations, especially in the low signal-to-noise (SNR) regime.

</details>

### [Seed Words Based Data Selection for Language Model Adaptation](2107.09433.md)
**Roberto Gretter, Marco Matassoni, Daniele Falavigna** · 2021-07-20

<details>
<summary>Abstract</summary>

We address the problem of language model customization in applications where the ASR component needs to manage domain-specific terminology; although current state-of-the-art speech recognition technology provides excellent results for generic domains, the adaptation to specialized dictionaries or glossaries is still an open issue. In this work we present an approach for automatically selecting sentences, from a text corpus, that match, both semantically and morphologically, a glossary of terms (words or composite words) furnished by the user. The final goal is to rapidly adapt the language model of an hybrid ASR system with a limited amount of in-domain text data in order to successfully cope with the linguistic domain at hand; the vocabulary of the baseline model is expanded and tailored, reducing the resulting OOV rate. Data selection strategies based on shallow morphological seeds and semantic similarity viaword2vec are introduced and discussed; the experimental setting consists in a simultaneous interpreting scenario, where ASRs in three languages are designed to recognize the domain-specific terms (i.e. dentistry). Results using different metrics (OOV rate, WER, precision and recall) show the effectiveness of the proposed techniques.

</details>

### [Streaming End-to-End ASR based on Blockwise Non-Autoregressive Models](2107.09428.md)
**Tianzi Wang, Yuya Fujita, Xuankai Chang, Shinji Watanabe** · 2021-07-20

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) modeling has gained more and more attention in speech processing. With recent state-of-the-art attention-based automatic speech recognition (ASR) structure, NAR can realize promising real-time factor (RTF) improvement with only small degradation of accuracy compared to the autoregressive (AR) models. However, the recognition inference needs to wait for the completion of a full speech utterance, which limits their applications on low latency scenarios. To address this issue, we propose a novel end-to-end streaming NAR speech recognition system by combining blockwise-attention and connectionist temporal classification with mask-predict (Mask-CTC) NAR. During inference, the input audio is separated into small blocks and then processed in a blockwise streaming way. To address the insertion and deletion error at the edge of the output of each block, we apply an overlapping decoding strategy with a dynamic mapping trick that can produce more coherent sentences. Experimental results show that the proposed method improves online ASR recognition in low latency conditions compared to vanilla Mask-CTC. Moreover, it can achieve a much faster inference speed compared to the AR attention-based models. All of our codes will be publicly available at https://github.com/espnet/espnet.

</details>

### [A baseline model for computationally inexpensive speech recognition for Kazakh using the Coqui STT framework](2107.10637.md)
**Ilnar Salimzianov** · 2021-07-19

<details>
<summary>Abstract</summary>

Mobile devices are transforming the way people interact with computers, and speech interfaces to applications are ever more important. Automatic Speech Recognition systems recently published are very accurate, but often require powerful machinery (specialised Graphical Processing Units) for inference, which makes them impractical to run on commodity devices, especially in streaming mode. Impressed by the accuracy of, but dissatisfied with the inference times of the baseline Kazakh ASR model of (Khassanov et al.,2021) when not using a GPU, we trained a new baseline acoustic model (on the same dataset as the aforementioned paper) and three language models for use with the Coqui STT framework. Results look promising, but further epochs of training and parameter sweeping or, alternatively, limiting the vocabulary that the ASR system must support, is needed to reach a production-level accuracy.

</details>

### [End-to-end speech recognition with Alignment RNN-Transducer](s2:262ee8316bf0a733a36542f6884a749d32f1e9dc.md)
**Ying Tian, Zerui Li, Min Liu, Kazushige Ouchi et al.** · 2021-07-18

<details>
<summary>Abstract</summary>

The Recurrent Neural Network Transducer (RNN-T) extends Connectionist Temporal Classification (CTC) by jointly modeling both input-output and output-output dependencies, and it has been successfully applied in end-to-end speech recognition. RNN-T adds language information by expanding its dimensions in this way, but the model training is difficult. And some paths of the model are unreasonable when decoding. Therefore, we present the Alignment RNN Transducer (ART) algorithm, which uses the forward-backward algorithm in CTC to find the best path alignment information as context-related information for training. We not only reduce the training dimensions but also adds context information to the model. And we still use CTC as the loss function to avoid decoding the impossible path in the RNN-T. We verify the algorithm on a Mandarin speech corpus AIShell-1, and it achieves a 13.65% CER, compared with the 16.79% CER given by the RNN-T model.

</details>

### [A Comparison of Methods for OOV-word Recognition on a New Public Dataset](2107.08091.md)
**Rudolf A. Braun, Srikanth Madikeri, Petr Motlicek** · 2021-07-16

<details>
<summary>Abstract</summary>

A common problem for automatic speech recognition systems is how to recognize words that they did not see during training. Currently there is no established method of evaluating different techniques for tackling this problem. We propose using the CommonVoice dataset to create test sets for multiple languages which have a high out-of-vocabulary (OOV) ratio relative to a training set and release a new tool for calculating relevant performance metrics. We then evaluate, within the context of a hybrid ASR system, how much better subword models are at recognizing OOVs, and how much benefit one can get from incorporating OOV-word information into an existing system by modifying WFSTs. Additionally, we propose a new method for modifying a subword-based language model so as to better recognize OOV-words. We showcase very large improvements in OOV-word recognition and make both the data and code available.

</details>

### [Multi-task Learning with Cross Attention for Keyword Spotting](2107.07634.md)
**Takuya Higuchi, Anmol Gupta, Chandra Dhir** · 2021-07-15

<details>
<summary>Abstract</summary>

Keyword spotting (KWS) is an important technique for speech applications, which enables users to activate devices by speaking a keyword phrase. Although a phoneme classifier can be used for KWS, exploiting a large amount of transcribed data for automatic speech recognition (ASR), there is a mismatch between the training criterion (phoneme recognition) and the target task (KWS). Recently, multi-task learning has been applied to KWS to exploit both ASR and KWS training data. In this approach, an output of an acoustic model is split into two branches for the two tasks, one for phoneme transcription trained with the ASR data and one for keyword classification trained with the KWS data. In this paper, we introduce a cross attention decoder in the multi-task learning framework. Unlike the conventional multi-task learning approach with the simple split of the output layer, the cross attention decoder summarizes information from a phonetic encoder by performing cross attention between the encoder outputs and a trainable query sequence to predict a confidence score for the KWS task. Experimental results on KWS tasks show that the proposed approach achieves a 12% relative reduction in the false reject ratios compared to the conventional multi-task learning with split branches and a bi-directional long short-team memory decoder.

</details>

### [VAD-free Streaming Hybrid CTC/Attention ASR for Unsegmented Recording](2107.07509.md)
**Hirofumi Inaguma, Tatsuya Kawahara** · 2021-07-15

<details>
<summary>Abstract</summary>

In this work, we propose novel decoding algorithms to enable streaming automatic speech recognition (ASR) on unsegmented long-form recordings without voice activity detection (VAD), based on monotonic chunkwise attention (MoChA) with an auxiliary connectionist temporal classification (CTC) objective. We propose a block-synchronous beam search decoding to take advantage of efficient batched output-synchronous and low-latency input-synchronous searches. We also propose a VAD-free inference algorithm that leverages CTC probabilities to determine a suitable timing to reset the model states to tackle the vulnerability to long-form data. Experimental evaluations demonstrate that the block-synchronous decoding achieves comparable accuracy to the label-synchronous one. Moreover, the VAD-free inference can recognize long-form speech robustly for up to a few hours.

</details>

### [CLSRIL-23: Cross Lingual Speech Representations for Indic Languages](2107.07402.md)
**Anirudh Gupta, Harveen Singh Chadha, Priyanshi Shah, Neeraj Chhimwal et al.** · 2021-07-15

<details>
<summary>Abstract</summary>

We present a CLSRIL-23, a self supervised learning based audio pre-trained model which learns cross lingual speech representations from raw audio across 23 Indic languages. It is built on top of wav2vec 2.0 which is solved by training a contrastive task over masked latent speech representations and jointly learns the quantization of latents shared across all languages. We compare the language wise loss during pretraining to compare effects of monolingual and multilingual pretraining. Performance on some downstream fine-tuning tasks for speech recognition is also compared and our experiments show that multilingual pretraining outperforms monolingual training, in terms of learning speech representations which encodes phonetic similarity of languages and also in terms of performance on down stream tasks. A decrease of 5% is observed in WER and 9.5% in CER when a multilingual pretrained model is used for finetuning in Hindi. All the code models are also open sourced. CLSRIL-23 is a model trained on $23$ languages and almost 10,000 hours of audio data to facilitate research in speech recognition for Indic languages. We hope that new state of the art systems will be created using the self supervised approach, especially for low resources Indic languages.

</details>

### [The IWSLT 2021 BUT Speech Translation Systems](2107.06155.md)
**Hari Krishna Vydana, Martin Karafi'at, Luk'as Burget, "Honza" Cernock'y** · 2021-07-13

<details>
<summary>Abstract</summary>

The paper describes BUT's English to German offline speech translation(ST) systems developed for IWSLT2021. They are based on jointly trained Automatic Speech Recognition-Machine Translation models. Their performances is evaluated on MustC-Common test set. In this work, we study their efficiency from the perspective of having a large amount of separate ASR training data and MT training data, and a smaller amount of speech-translation training data. Large amounts of ASR and MT training data are utilized for pre-training the ASR and MT models. Speech-translation data is used to jointly optimize ASR-MT models by defining an end-to-end differentiable path from speech to translations. For this purpose, we use the internal continuous representations from the ASR-decoder as the input to MT module. We show that speech translation can be further improved by training the ASR-decoder jointly with the MT-module using large amount of text-only MT training data. We also show significant improvements by training an ASR module capable of generating punctuated text, rather than leaving the punctuation task to the MT module.

</details>

### [Zero-shot Speech Translation](2107.06010.md)
**Tu Anh Dinh** · 2021-07-13

<details>
<summary>Abstract</summary>

Speech Translation (ST) is the task of translating speech in one language into text in another language. Traditional cascaded approaches for ST, using Automatic Speech Recognition (ASR) and Machine Translation (MT) systems, are prone to error propagation. End-to-end approaches use only one system to avoid propagating error, yet are difficult to employ due to data scarcity. We explore zero-shot translation, which enables translating a pair of languages that is unseen during training, thus avoid the use of end-to-end ST data. Zero-shot translation has been shown to work for multilingual machine translation, yet has not been studied for speech translation. We attempt to build zero-shot ST models that are trained only on ASR and MT tasks but can do ST task during inference. The challenge is that the representation of text and audio is significantly different, thus the models learn ASR and MT tasks in different ways, making it non-trivial to perform zero-shot. These models tend to output the wrong language when performing zero-shot ST. We tackle the issues by including additional training data and an auxiliary loss function that minimizes the text-audio difference. Our experiment results and analysis show that the methods are promising for zero-shot ST. Moreover, our methods are particularly useful in the few-shot settings where a limited amount of ST data is available, with improvements of up to +11.8 BLEU points compared to direct end-to-end ST models and +3.9 BLEU points compared to ST models fine-tuned from pre-trained ASR model.

</details>

### [Conformer-based End-to-end Speech Recognition With Rotary Position Embedding](2107.05907.md)
**Shengqiang Li, Menglong Xu, Xiao-Lei Zhang** · 2021-07-13

<details>
<summary>Abstract</summary>

Transformer-based end-to-end speech recognition models have received considerable attention in recent years due to their high training speed and ability to model a long-range global context. Position embedding in the transformer architecture is indispensable because it provides supervision for dependency modeling between elements at different positions in the input sequence. To make use of the time order of the input sequence, many works inject some information about the relative or absolute position of the element into the input sequence. In this work, we investigate various position embedding methods in the convolution-augmented transformer (conformer) and adopt a novel implementation named rotary position embedding (RoPE). RoPE encodes absolute positional information into the input sequence by a rotation matrix, and then naturally incorporates explicit relative position information into a self-attention module. To evaluate the effectiveness of the RoPE method, we conducted experiments on AISHELL-1 and LibriSpeech corpora. Results show that the conformer enhanced with RoPE achieves superior performance in the speech recognition task. Specifically, our model achieves a relative word error rate reduction of 8.70% and 7.27% over the conformer on test-clean and test-other sets of the LibriSpeech corpus respectively.

</details>

### [UniSpeech at scale: An Empirical Study of Pre-training Method on Large-Scale Speech Recognition Dataset](2107.05233.md)
**Chengyi Wang, Yu Wu, Shujie Liu, Jinyu Li et al.** · 2021-07-12

<details>
<summary>Abstract</summary>

Recently, there has been a vast interest in self-supervised learning (SSL) where the model is pre-trained on large scale unlabeled data and then fine-tuned on a small labeled dataset. The common wisdom is that SSL helps resource-limited tasks in which only a limited amount of labeled data is available. The benefit of SSL keeps diminishing when the labeled training data amount increases. To our best knowledge, at most a few thousand hours of labeled data was used in the study of SSL. In contrast, the industry usually uses tens of thousands of hours of labeled data to build high-accuracy speech recognition (ASR) systems for resource-rich languages. In this study, we take the challenge to investigate whether and how SSL can improve the ASR accuracy of a state-of-the-art production-scale Transformer-Transducer model, which was built with 65 thousand hours of anonymized labeled EN-US data.

</details>

### [Perceptual-based deep-learning denoiser as a defense against adversarial attacks on ASR systems](2107.05222.md)
**Anirudh Sreeram, Nicholas Mehlman, Raghuveer Peri, Dillon Knox et al.** · 2021-07-12

<details>
<summary>Abstract</summary>

In this paper we investigate speech denoising as a defense against adversarial attacks on automatic speech recognition (ASR) systems. Adversarial attacks attempt to force misclassification by adding small perturbations to the original speech signal. We propose to counteract this by employing a neural-network based denoiser as a pre-processor in the ASR pipeline. The denoiser is independent of the downstream ASR model, and thus can be rapidly deployed in existing systems. We found that training the denoisier using a perceptually motivated loss function resulted in increased adversarial robustness without compromising ASR performance on benign samples. Our defense was evaluated (as a part of the DARPA GARD program) on the 'Kenansville' attack strategy across a range of attack strengths and speech samples. An average improvement in Word Error Rate (WER) of about 7.7% was observed over the undefended model at 20 dB signal-to-noise-ratio (SNR) attack strength.

</details>

### [Improving Speech Translation by Understanding and Learning from the Auxiliary Text Translation Task](2107.05782.md)
**Yun Tang, Juan Pino, Xian Li, Changhan Wang et al.** · 2021-07-12

<details>
<summary>Abstract</summary>

Pretraining and multitask learning are widely used to improve the speech to text translation performance. In this study, we are interested in training a speech to text translation model along with an auxiliary text to text translation task. We conduct a detailed analysis to understand the impact of the auxiliary task on the primary task within the multitask learning framework. Our analysis confirms that multitask learning tends to generate similar decoder representations from different modalities and preserve more information from the pretrained text translation modules. We observe minimal negative transfer effect between the two tasks and sharing more parameters is helpful to transfer knowledge from the text task to the speech task. The analysis also reveals that the modality representation difference at the top decoder layers is still not negligible, and those layers are critical for the translation quality. Inspired by these findings, we propose three methods to improve translation quality. First, a parameter sharing and initialization strategy is proposed to enhance information sharing between the tasks. Second, a novel attention-based regularization is proposed for the encoders and pulls the representations from different modalities closer. Third, an online knowledge distillation is proposed to enhance the knowledge transfer from the text to the speech task. Our experiments show that the proposed approach improves translation performance by more than 2 BLEU over a strong baseline and achieves state-of-the-art results on the \textsc{MuST-C} English-German, English-French and English-Spanish language pairs.

</details>

### [Multilingual and crosslingual speech recognition using phonological-vector based phone embeddings](2107.05038.md)
**Chengrui Zhu, Keyu An, Huahuan Zheng, Zhijian Ou** · 2021-07-11

<details>
<summary>Abstract</summary>

The use of phonological features (PFs) potentially allows language-specific phones to remain linked in training, which is highly desirable for information sharing for multilingual and crosslingual speech recognition methods for low-resourced languages. A drawback suffered by previous methods in using phonological features is that the acoustic-to-PF extraction in a bottom-up way is itself difficult. In this paper, we propose to join phonology driven phone embedding (top-down) and deep neural network (DNN) based acoustic feature extraction (bottom-up) to calculate phone probabilities. The new method is called JoinAP (Joining of Acoustics and Phonology). Remarkably, no inversion from acoustics to phonological features is required for speech recognition. For each phone in the IPA (International Phonetic Alphabet) table, we encode its phonological features to a phonological-vector, and then apply linear or nonlinear transformation of the phonological-vector to obtain the phone embedding. A series of multilingual and crosslingual (both zero-shot and few-shot) speech recognition experiments are conducted on the CommonVoice dataset (German, French, Spanish and Italian) and the AISHLL-1 dataset (Mandarin), and demonstrate the superiority of JoinAP with nonlinear phone embeddings over both JoinAP with linear phone embeddings and the traditional method with flat phone embeddings.

</details>

### [Layer-wise Analysis of a Self-supervised Speech Representation Model](2107.04734.md)
**Ankita Pasad, Ju-Chieh Chou, Karen Livescu** · 2021-07-10

<details>
<summary>Abstract</summary>

Recently proposed self-supervised learning approaches have been successful for pre-training speech representation models. The utility of these learned representations has been observed empirically, but not much has been studied about the type or extent of information encoded in the pre-trained representations themselves. Developing such insights can help understand the capabilities and limits of these models and enable the research community to more efficiently develop their usage for downstream applications. In this work, we begin to fill this gap by examining one recent and successful pre-trained model (wav2vec 2.0), via its intermediate representation vectors, using a suite of analysis tools. We use the metrics of canonical correlation, mutual information, and performance on simple downstream tasks with non-parametric probes, in order to (i) query for acoustic and linguistic information content, (ii) characterize the evolution of information across model layers, and (iii) understand how fine-tuning the model for automatic speech recognition (ASR) affects these observations. Our findings motivate modifying the fine-tuning protocol for ASR, which produces improved word error rates in a low-resource setting.

</details>

### [Noisy Training Improves E2E ASR for the Edge](2107.04677.md)
**Dilin Wang, Yuan Shangguan, Haichuan Yang, Pierce Chuang et al.** · 2021-07-09

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has become increasingly ubiquitous on modern edge devices. Past work developed streaming End-to-End (E2E) all-neural speech recognizers that can run compactly on edge devices. However, E2E ASR models are prone to overfitting and have difficulties in generalizing to unseen testing data. Various techniques have been proposed to regularize the training of ASR models, including layer normalization, dropout, spectrum data augmentation and speed distortions in the inputs. In this work, we present a simple yet effective noisy training strategy to further improve the E2E ASR model training. By introducing random noise to the parameter space during training, our method can produce smoother models at convergence that generalize better. We apply noisy training to improve both dense and sparse state-of-the-art Emformer models and observe consistent WER reduction. Specifically, when training Emformers with 90% sparsity, we achieve 12% and 14% WER improvements on the LibriSpeech Test-other and Test-clean data set, respectively.

</details>

### [Loss Prediction: End-to-End Active Learning Approach For Speech Recognition](2107.04289.md)
**Jian Luo, Jianzong Wang, Ning Cheng, Jing Xiao** · 2021-07-09

<details>
<summary>Abstract</summary>

End-to-end speech recognition systems usually require huge amounts of labeling resource, while annotating the speech data is complicated and expensive. Active learning is the solution by selecting the most valuable samples for annotation. In this paper, we proposed to use a predicted loss that estimates the uncertainty of the sample. The CTC (Connectionist Temporal Classification) and attention loss are informative for speech recognition since they are computed based on all decoding paths and alignments. We defined an end-to-end active learning pipeline, training an ASR/LP (Automatic Speech Recognition/Loss Prediction) joint model. The proposed approach was validated on an English and a Chinese speech recognition task. The experiments show that our approach achieves competitive results, outperforming random selection, least confidence, and estimated loss method.

</details>

### [On lattice-free boosted MMI training of HMM and CTC-based full-context ASR models](2107.04154.md)
**Xiaohui Zhang, Vimal Manohar, David Zhang, Frank Zhang et al.** · 2021-07-09

<details>
<summary>Abstract</summary>

Hybrid automatic speech recognition (ASR) models are typically sequentially trained with CTC or LF-MMI criteria. However, they have vastly different legacies and are usually implemented in different frameworks. In this paper, by decoupling the concepts of modeling units and label topologies and building proper numerator/denominator graphs accordingly, we establish a generalized framework for hybrid acoustic modeling (AM). In this framework, we show that LF-MMI is a powerful training criterion applicable to both limited-context and full-context models, for wordpiece/mono-char/bi-char/chenone units, with both HMM/CTC topologies. From this framework, we propose three novel training schemes: chenone(ch)/wordpiece(wp)-CTC-bMMI, and wordpiece(wp)-HMM-bMMI with different advantages in training performance, decoding efficiency and decoding time-stamp accuracy. The advantages of different training schemes are evaluated comprehensively on Librispeech, and wp-CTC-bMMI and ch-CTC-bMMI are evaluated on two real world ASR tasks to show their effectiveness. Besides, we also show bi-char(bc) HMM-MMI models can serve as better alignment models than traditional non-neural GMM-HMMs.

</details>

### [Improved Language Identification Through Cross-Lingual Self-Supervised Learning](2107.04082.md)
**Andros Tjandra, Diptanu Gon Choudhury, Frank Zhang, Kritika Singh et al.** · 2021-07-08

<details>
<summary>Abstract</summary>

Language identification greatly impacts the success of downstream tasks such as automatic speech recognition. Recently, self-supervised speech representations learned by wav2vec 2.0 have been shown to be very effective for a range of speech tasks. We extend previous self-supervised work on language identification by experimenting with pre-trained models which were learned on real-world unconstrained speech in multiple languages and not just on English. We show that models pre-trained on many languages perform better and enable language identification systems that require very little labeled data to perform well. Results on a 26 languages setup show that with only 10 minutes of labeled data per language, a cross-lingually pre-trained model can achieve over 89.2% accuracy.

</details>

### [End-to-End Rich Transcription-Style Automatic Speech Recognition with Semi-Supervised Learning](2107.05382.md)
**Tomohiro Tanaka, Ryo Masumura, Mana Ihori, Akihiko Takashima et al.** · 2021-07-07

<details>
<summary>Abstract</summary>

We propose a semi-supervised learning method for building end-to-end rich transcription-style automatic speech recognition (RT-ASR) systems from small-scale rich transcription-style and large-scale common transcription-style datasets. In spontaneous speech tasks, various speech phenomena such as fillers, word fragments, laughter and coughs, etc. are often included. While common transcriptions do not give special awareness to these phenomena, rich transcriptions explicitly convert them into special phenomenon tokens as well as textual tokens. In previous studies, the textual and phenomenon tokens were simultaneously estimated in an end-to-end manner. However, it is difficult to build accurate RT-ASR systems because large-scale rich transcription-style datasets are often unavailable. To solve this problem, our training method uses a limited rich transcription-style dataset and common transcription-style dataset simultaneously. The Key process in our semi-supervised learning is to convert the common transcription-style dataset into a pseudo-rich transcription-style dataset. To this end, we introduce style tokens which control phenomenon tokens are generated or not into transformer-based autoregressive modeling. We use this modeling for generating the pseudo-rich transcription-style datasets and for building RT-ASR system from the pseudo and original datasets. Our experiments on spontaneous ASR tasks showed the effectiveness of the proposed method.

</details>

### [Improving Speech Recognition Accuracy of Local POI Using Geographical Models](2107.03165.md)
**Songjun Cao, Yike Zhang, Xiaobing Feng, Long Ma** · 2021-07-07

<details>
<summary>Abstract</summary>

Nowadays voice search for points of interest (POI) is becoming increasingly popular. However, speech recognition for local POI has remained to be a challenge due to multi-dialect and massive POI. This paper improves speech recognition accuracy for local POI from two aspects. Firstly, a geographic acoustic model (Geo-AM) is proposed. The Geo-AM deals with multi-dialect problem using dialect-specific input feature and dialect-specific top layer. Secondly, a group of geo-specific language models (Geo-LMs) are integrated into our speech recognition system to improve recognition accuracy of long tail and homophone POI. During decoding, specific language models are selected on demand according to users' geographic location. Experiments show that the proposed Geo-AM achieves 6.5%$\sim$10.1% relative character error rate (CER) reduction on an accent testset and the proposed Geo-AM and Geo-LM totally achieve over 18.7% relative CER reduction on Tencent Map task.

</details>

### [Advancing CTC-CRF Based End-to-End Speech Recognition with Wordpieces and Conformers](2107.03007.md)
**Huahuan Zheng, Wenjie Peng, Zhijian Ou, Jinsong Zhang** · 2021-07-07

<details>
<summary>Abstract</summary>

Automatic speech recognition systems have been largely improved in the past few decades and current systems are mainly hybrid-based and end-to-end-based. The recently proposed CTC-CRF framework inherits the data-efficiency of the hybrid approach and the simplicity of the end-to-end approach. In this paper, we further advance CTC-CRF based ASR technique with explorations on modeling units and neural architectures. Specifically, we investigate techniques to enable the recently developed wordpiece modeling units and Conformer neural networks to be succesfully applied in CTC-CRFs. Experiments are conducted on two English datasets (Switchboard, Librispeech) and a German dataset from CommonVoice. Experimental results suggest that (i) Conformer can improve the recognition performance significantly; (ii) Wordpiece-based systems perform slightly worse compared with phone-based systems for the target language with a low degree of grapheme-phoneme correspondence (e.g. English), while the two systems can perform equally strong when such degree of correspondence is high for the target language (e.g. German).

</details>

### [Kosp2e: Korean Speech to English Translation Corpus](2107.02875.md)
**Won Ik Cho, Seok Min Kim, Hyunchang Cho, Nam Soo Kim** · 2021-07-06

<details>
<summary>Abstract</summary>

Most speech-to-text (S2T) translation studies use English speech as a source, which makes it difficult for non-English speakers to take advantage of the S2T technologies. For some languages, this problem was tackled through corpus construction, but the farther linguistically from English or the more under-resourced, this deficiency and underrepresentedness becomes more significant. In this paper, we introduce kosp2e (read as `kospi'), a corpus that allows Korean speech to be translated into English text in an end-to-end manner. We adopt open license speech recognition corpus, translation corpus, and spoken language corpora to make our dataset freely available to the public, and check the performance through the pipeline and training-based approaches. Using pipeline and various end-to-end schemes, we obtain the highest BLEU of 21.3 and 18.0 for each based on the English hypothesis, validating the feasibility of our data. We plan to supplement annotations for other target languages through community contributions in the future.

</details>

### [A Comparative Study of Modular and Joint Approaches for Speaker-Attributed ASR on Monaural Long-Form Audio](2107.02852.md)
**Naoyuki Kanda, Xiong Xiao, Jian Wu, Tianyan Zhou et al.** · 2021-07-06

<details>
<summary>Abstract</summary>

Speaker-attributed automatic speech recognition (SA-ASR) is a task to recognize "who spoke what" from multi-talker recordings. An SA-ASR system usually consists of multiple modules such as speech separation, speaker diarization and ASR. On the other hand, considering the joint optimization, an end-to-end (E2E) SA-ASR model has recently been proposed with promising results on simulation data. In this paper, we present our recent study on the comparison of such modular and joint approaches towards SA-ASR on real monaural recordings. We develop state-of-the-art SA-ASR systems for both modular and joint approaches by leveraging large-scale training data, including 75 thousand hours of ASR training data and the VoxCeleb corpus for speaker representation learning. We also propose a new pipeline that performs the E2E SA-ASR model after speaker clustering. Our evaluation on the AMI meeting corpus reveals that after fine-tuning with a small real data, the joint system performs 8.9--29.9% better in accuracy compared to the best modular system while the modular system performs better before such fine-tuning. We also conduct various error analyses to show the remaining issues for the monaural SA-ASR.

</details>

### [Exploiting Single-Channel Speech For Multi-channel End-to-end Speech Recognition](2107.02670.md)
**Keyu An, Zhijian Ou** · 2021-07-06

<details>
<summary>Abstract</summary>

Recently, the end-to-end training approach for neural beamformer-supported multi-channel ASR has shown its effectiveness in multi-channel speech recognition. However, the integration of multiple modules makes it more difficult to perform end-to-end training, particularly given that the multi-channel speech corpus recorded in real environments with a sizeable data scale is relatively limited. This paper explores the usage of single-channel data to improve the multi-channel end-to-end speech recognition system. Specifically, we design three schemes to exploit the single-channel data, namely pre-training, data scheduling, and data simulation. Extensive experiments on CHiME4 and AISHELL-4 datasets demonstrate that all three methods improve the multi-channel end-to-end training stability and speech recognition performance, while the data scheduling approach keeps a much simpler pipeline (vs. pre-training) and less computation cost (vs. data simulation). Moreover, we give a thorough analysis of our systems, including how the performance is affected by the choice of front-end, the data augmentation, training strategy, and single-channel data size.

</details>

### [Instant One-Shot Word-Learning for Context-Specific Neural Sequence-to-Sequence Speech Recognition](2107.02268.md)
**Christian Huber, Juan Hussain, Sebastian Stüker, Alexander Waibel** · 2021-07-05

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence systems deliver state-of-the-art performance for automatic speech recognition (ASR). When using appropriate modeling units, e.g., byte-pair encoded characters, these systems are in principal open vocabulary systems. In practice, however, they often fail to recognize words not seen during training, e.g., named entities, numbers or technical terms. To alleviate this problem we supplement an end-to-end ASR system with a word/phrase memory and a mechanism to access this memory to recognize the words and phrases correctly. After the training of the ASR system, and when it has already been deployed, a relevant word can be added or subtracted instantly without the need for further training. In this paper we demonstrate that through this mechanism our system is able to recognize more than 85% of newly added words that it previously failed to recognize compared to a strong baseline.

</details>

### [Improving a neural network model by explanation-guided training for glioma classification based on MRI data](2107.02008.md)
**Frantisek Sefcik, Wanda Benesova** · 2021-07-05

<details>
<summary>Abstract</summary>

In recent years, artificial intelligence (AI) systems have come to the forefront. These systems, mostly based on Deep learning (DL), achieve excellent results in areas such as image processing, natural language processing, or speech recognition. Despite the statistically high accuracy of deep learning models, their output is often a decision of "black box". Thus, Interpretability methods have become a popular way to gain insight into the decision-making process of deep learning models. Explanation of a deep learning model is desirable in the medical domain since the experts have to justify their judgments to the patient. In this work, we proposed a method for explanation-guided training that uses a Layer-wise relevance propagation (LRP) technique to force the model to focus only on the relevant part of the image. We experimentally verified our method on a convolutional neural network (CNN) model for low-grade and high-grade glioma classification problems. Our experiments show promising results in a way to use interpretation techniques in the model training process.

</details>

### [Investigation of Practical Aspects of Single Channel Speech Separation for ASR](2107.01922.md)
**Jian Wu, Zhuo Chen, Sanyuan Chen, Yu Wu et al.** · 2021-07-05

<details>
<summary>Abstract</summary>

Speech separation has been successfully applied as a frontend processing module of conversation transcription systems thanks to its ability to handle overlapped speech and its flexibility to combine with downstream tasks such as automatic speech recognition (ASR). However, a speech separation model often introduces target speech distortion, resulting in a sub-optimum word error rate (WER). In this paper, we describe our efforts to improve the performance of a single channel speech separation system. Specifically, we investigate a two-stage training scheme that firstly applies a feature level optimization criterion for pretraining, followed by an ASR-oriented optimization criterion using an end-to-end (E2E) speech recognition model. Meanwhile, to keep the model light-weight, we introduce a modified teacher-student learning technique for model compression. By combining those approaches, we achieve a absolute average WER improvement of 2.70% and 0.77% using models with less than 10M parameters compared with the previous state-of-the-art results on the LibriCSS dataset for utterance-wise evaluation and continuous evaluation, respectively

</details>

### [Arabic Code-Switching Speech Recognition using Monolingual Data](2107.01573.md)
**Ahmed Ali, Shammur Chowdhury, Amir Hussein, Yasser Hifny** · 2021-07-04

<details>
<summary>Abstract</summary>

Code-switching in automatic speech recognition (ASR) is an important challenge due to globalization. Recent research in multilingual ASR shows potential improvement over monolingual systems. We study key issues related to multilingual modeling for ASR through a series of large-scale ASR experiments. Our innovative framework deploys a multi-graph approach in the weighted finite state transducers (WFST) framework. We compare our WFST decoding strategies with a transformer sequence to sequence system trained on the same data. Given a code-switching scenario between Arabic and English languages, our results show that the WFST decoding approaches were more suitable for the intersentential code-switching datasets. In addition, the transformer system performed better for intrasentential code-switching task. With this study, we release an artificially generated development and test sets, along with ecological code-switching test set, to benchmark the ASR performance.

</details>

### [Cross-Modal Transformer-Based Neural Correction Models for Automatic Speech Recognition](2107.01569.md)
**Tomohiro Tanaka, Ryo Masumura, Mana Ihori, Akihiko Takashima et al.** · 2021-07-04

<details>
<summary>Abstract</summary>

We propose a cross-modal transformer-based neural correction models that refines the output of an automatic speech recognition (ASR) system so as to exclude ASR errors. Generally, neural correction models are composed of encoder-decoder networks, which can directly model sequence-to-sequence mapping problems. The most successful method is to use both input speech and its ASR output text as the input contexts for the encoder-decoder networks. However, the conventional method cannot take into account the relationships between these two different modal inputs because the input contexts are separately encoded for each modal. To effectively leverage the correlated information between the two different modal inputs, our proposed models encode two different contexts jointly on the basis of cross-modal self-attention using a transformer. We expect that cross-modal self-attention can effectively capture the relationships between two different modals for refining ASR hypotheses. We also introduce a shallow fusion technique to efficiently integrate the first-pass ASR model and our proposed neural correction model. Experiments on Japanese natural language ASR tasks demonstrated that our proposed models achieve better ASR performance than conventional neural correction models.

</details>

### [Unified Autoregressive Modeling for Joint End-to-End Multi-Talker Overlapped Speech Recognition and Speaker Attribute Estimation](2107.01549.md)
**Ryo Masumura, Daiki Okamura, Naoki Makishima, Mana Ihori et al.** · 2021-07-04

<details>
<summary>Abstract</summary>

In this paper, we present a novel modeling method for single-channel multi-talker overlapped automatic speech recognition (ASR) systems. Fully neural network based end-to-end models have dramatically improved the performance of multi-taker overlapped ASR tasks. One promising approach for end-to-end modeling is autoregressive modeling with serialized output training in which transcriptions of multiple speakers are recursively generated one after another. This enables us to naturally capture relationships between speakers. However, the conventional modeling method cannot explicitly take into account the speaker attributes of individual utterances such as gender and age information. In fact, the performance deteriorates when each speaker is the same gender or is close in age. To address this problem, we propose unified autoregressive modeling for joint end-to-end multi-talker overlapped ASR and speaker attribute estimation. Our key idea is to handle gender and age estimation tasks within the unified autoregressive modeling. In the proposed method, transformer-based autoregressive model recursively generates not only textual tokens but also attribute tokens of each speaker. This enables us to effectively utilize speaker attributes for improving multi-talker overlapped ASR. Experiments on Japanese multi-talker overlapped ASR tasks demonstrate the effectiveness of the proposed method.

</details>

### [TENET: A Time-reversal Enhancement Network for Noise-robust ASR](2107.01531.md)
**Fu-An Chao, Shao-Wei Fan Jiang, Bi-Cheng Yan, Jeih-weih Hung et al.** · 2021-07-04

<details>
<summary>Abstract</summary>

Due to the unprecedented breakthroughs brought about by deep learning, speech enhancement (SE) techniques have been developed rapidly and play an important role prior to acoustic modeling to mitigate noise effects on speech. To increase the perceptual quality of speech, current state-of-the-art in the SE field adopts adversarial training by connecting an objective metric to the discriminator. However, there is no guarantee that optimizing the perceptual quality of speech will necessarily lead to improved automatic speech recognition (ASR) performance. In this study, we present TENET, a novel Time-reversal Enhancement NETwork, which leverages the transformation of an input noisy signal itself, i.e., the time-reversed version, in conjunction with the siamese network and complex dual-path transformer to promote SE performance for noise-robust ASR. Extensive experiments conducted on the Voicebank-DEMAND dataset show that TENET can achieve state-of-the-art results compared to a few top-of-the-line methods in terms of both SE and ASR evaluation metrics. To demonstrate the model generalization ability, we further evaluate TENET on the test set of scenarios contaminated with unseen noise, and the results also confirm the superiority of this promising method.

</details>

### [Relaxed Attention: A Simple Method to Boost Performance of End-to-End Automatic Speech Recognition](2107.01275.md)
**Timo Lohrenz, Patrick Schwarz, Zhengyang Li, Tim Fingscheidt** · 2021-07-02

<details>
<summary>Abstract</summary>

Recently, attention-based encoder-decoder (AED) models have shown high performance for end-to-end automatic speech recognition (ASR) across several tasks. Addressing overconfidence in such models, in this paper we introduce the concept of relaxed attention, which is a simple gradual injection of a uniform distribution to the encoder-decoder attention weights during training that is easily implemented with two lines of code. We investigate the effect of relaxed attention across different AED model architectures and two prominent ASR tasks, Wall Street Journal (WSJ) and Librispeech. We found that transformers trained with relaxed attention outperform the standard baseline models consistently during decoding with external language models. On WSJ, we set a new benchmark for transformer-based end-to-end speech recognition with a word error rate of 3.65%, outperforming state of the art (4.20%) by 13.1% relative, while introducing only a single hyperparameter.

</details>

### [Dual Causal/Non-Causal Self-Attention for Streaming End-to-End Speech Recognition](2107.01269.md)
**Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2021-07-02

<details>
<summary>Abstract</summary>

Attention-based end-to-end automatic speech recognition (ASR) systems have recently demonstrated state-of-the-art results for numerous tasks. However, the application of self-attention and attention-based encoder-decoder models remains challenging for streaming ASR, where each word must be recognized shortly after it was spoken. In this work, we present the dual causal/non-causal self-attention (DCN) architecture, which in contrast to restricted self-attention prevents the overall context to grow beyond the look-ahead of a single layer when used in a deep architecture. DCN is compared to chunk-based and restricted self-attention using streaming transformer and conformer architectures, showing improved ASR performance over restricted self-attention and competitive ASR results compared to chunk-based self-attention, while providing the advantage of frame-synchronous processing. Combined with triggered attention, the proposed streaming end-to-end ASR systems obtained state-of-the-art results on the LibriSpeech, HKUST, and Switchboard ASR tasks.

</details>

### [CrowdSpeech and VoxDIY: Benchmark Datasets for Crowdsourced Audio Transcription](2107.01091.md)
**Nikita Pavlichenko, Ivan Stelmakh, Dmitry Ustalov** · 2021-07-02

<details>
<summary>Abstract</summary>

Domain-specific data is the crux of the successful transfer of machine learning systems from benchmarks to real life. In simple problems such as image classification, crowdsourcing has become one of the standard tools for cheap and time-efficient data collection: thanks in large part to advances in research on aggregation methods. However, the applicability of crowdsourcing to more complex tasks (e.g., speech recognition) remains limited due to the lack of principled aggregation methods for these modalities. The main obstacle towards designing aggregation methods for more advanced applications is the absence of training data, and in this work, we focus on bridging this gap in speech recognition. For this, we collect and release CrowdSpeech -- the first publicly available large-scale dataset of crowdsourced audio transcriptions. Evaluation of existing and novel aggregation methods on our data shows room for improvement, suggesting that our work may entail the design of better algorithms. At a higher level, we also contribute to the more general challenge of developing the methodology for reliable data collection via crowdsourcing. In that, we design a principled pipeline for constructing datasets of crowdsourced audio transcriptions in any novel domain. We show its applicability on an under-resourced language by constructing VoxDIY -- a counterpart of CrowdSpeech for the Russian language. We also release the code that allows a full replication of our data collection pipeline and share various insights on best practices of data collection via crowdsourcing.

</details>

### [Supervised Contrastive Learning for Accented Speech Recognition](2107.00921.md)
**Tao Han, Hantao Huang, Ziang Yang, Wei Han** · 2021-07-02

<details>
<summary>Abstract</summary>

Neural network based speech recognition systems suffer from performance degradation due to accented speech, especially unfamiliar accents. In this paper, we study the supervised contrastive learning framework for accented speech recognition. To build different views (similar "positive" data samples) for contrastive learning, three data augmentation techniques including noise injection, spectrogram augmentation and TTS-same-sentence generation are further investigated. From the experiments on the Common Voice dataset, we have shown that contrastive learning helps to build data-augmentation invariant and pronunciation invariant representations, which significantly outperforms traditional joint training methods in both zero-shot and full-shot settings. Experiments show that contrastive learning can improve accuracy by 3.66% (zero-shot) and 3.78% (full-shot) on average, comparing to the joint training method.

</details>

### [Combining Frame-Synchronous and Label-Synchronous Systems for Speech Recognition](2107.00764.md)
**Qiujia Li, Chao Zhang, Philip C. Woodland** · 2021-07-01

<details>
<summary>Abstract</summary>

Commonly used automatic speech recognition (ASR) systems can be classified into frame-synchronous and label-synchronous categories, based on whether the speech is decoded on a per-frame or per-label basis. Frame-synchronous systems, such as traditional hidden Markov model systems, can easily incorporate existing knowledge and can support streaming ASR applications. Label-synchronous systems, based on attention-based encoder-decoder models, can jointly learn the acoustic and language information with a single model, which can be regarded as audio-grounded language models. In this paper, we propose rescoring the N-best hypotheses or lattices produced by a first-pass frame-synchronous system with a label-synchronous system in a second-pass. By exploiting the complementary modelling of the different approaches, the combined two-pass systems achieve competitive performance without using any extra speech or text data on two standard ASR tasks. For the 80-hour AMI IHM dataset, the combined system has a 13.7% word error rate (WER) on the evaluation set, which is up to a 29% relative WER reduction over the individual systems. For the 300-hour Switchboard dataset, the WERs of the combined system are 5.7% and 12.1% on Switchboard and CallHome subsets of Hub5'00, and 13.2% and 7.6% on Switchboard Cellular and Fisher subsets of RT03, up to a 33% relative reduction in WER over the individual systems.

</details>

### [ESPnet-ST IWSLT 2021 Offline Speech Translation System](2107.00636.md)
**Hirofumi Inaguma, Brian Yan, Siddharth Dalmia, Pengcheng Guo et al.** · 2021-07-01

<details>
<summary>Abstract</summary>

This paper describes the ESPnet-ST group's IWSLT 2021 submission in the offline speech translation track. This year we made various efforts on training data, architecture, and audio segmentation. On the data side, we investigated sequence-level knowledge distillation (SeqKD) for end-to-end (E2E) speech translation. Specifically, we used multi-referenced SeqKD from multiple teachers trained on different amounts of bitext. On the architecture side, we adopted the Conformer encoder and the Multi-Decoder architecture, which equips dedicated decoders for speech recognition and translation tasks in a unified encoder-decoder model and enables search in both source and target language spaces during inference. We also significantly improved audio segmentation by using the pyannote.audio toolkit and merging multiple short segments for long context modeling. Experimental evaluations showed that each of them contributed to large improvements in translation performance. Our best E2E system combined all the above techniques with model ensembling and achieved 31.4 BLEU on the 2-ref of tst2021 and 21.2 BLEU and 19.3 BLEU on the two single references of tst2021.

</details>

### [StableEmit: Selection Probability Discount for Reducing Emission Latency of Streaming Monotonic Attention ASR](2107.00635.md)
**Hirofumi Inaguma, Tatsuya Kawahara** · 2021-07-01

<details>
<summary>Abstract</summary>

While attention-based encoder-decoder (AED) models have been successfully extended to the online variants for streaming automatic speech recognition (ASR), such as monotonic chunkwise attention (MoChA), the models still have a large label emission latency because of the unconstrained end-to-end training objective. Previous works tackled this problem by leveraging alignment information to control the timing to emit tokens during training. In this work, we propose a simple alignment-free regularization method, StableEmit, to encourage MoChA to emit tokens earlier. StableEmit discounts the selection probabilities in hard monotonic attention for token boundary detection by a constant factor and regularizes them to recover the total attention mass during training. As a result, the scale of the selection probabilities is increased, and the values can reach a threshold for token emission earlier, leading to a reduction of emission latency and deletion errors. Moreover, StableEmit can be combined with methods that constraint alignments to further improve the accuracy and latency. Experimental evaluations with LSTM and Conformer encoders demonstrate that StableEmit significantly reduces the recognition errors and the emission latency simultaneously. We also show that the use of alignment information is complementary in both metrics.

</details>

### [Pretext Tasks selection for multitask self-supervised speech representation learning](2107.00594.md)
**Salah Zaiem, Titouan Parcollet, Slim Essid, Abdel Heba** · 2021-07-01

<details>
<summary>Abstract</summary>

Through solving pretext tasks, self-supervised learning leverages unlabeled data to extract useful latent representations replacing traditional input features in the downstream task. In audio/speech signal processing, a wide range of features where engineered through decades of research efforts. As it turns out, learning to predict such features (a.k.a pseudo-labels) has proven to be a particularly relevant pretext task, leading to useful self-supervised representations which prove to be effective for downstream tasks. However, methods and common practices for combining such pretext tasks for better performance on the downstream task have not been explored and understood properly. In fact, the process relies almost exclusively on a computationally heavy experimental procedure, which becomes intractable with the increase of the number of pretext tasks. This paper introduces a method to select a group of pretext tasks among a set of candidates. The method we propose estimates calibrated weights for the partial losses corresponding to the considered pretext tasks during the self-supervised training process. The experiments conducted on automatic speech recognition, speaker and emotion recognition validate our approach, as the groups selected and weighted with our method perform better than classic baselines, thus facilitating the selection and combination of relevant pseudo-labels for self-supervised representation learning.

</details>

### [Word-Free Spoken Language Understanding for Mandarin-Chinese](2107.00186.md)
**Zhiyuan Guo, Yuexin Li, Guo Chen, Xingyu Chen et al.** · 2021-07-01

<details>
<summary>Abstract</summary>

Spoken dialogue systems such as Siri and Alexa provide great convenience to people's everyday life. However, current spoken language understanding (SLU) pipelines largely depend on automatic speech recognition (ASR) modules, which require a large amount of language-specific training data. In this paper, we propose a Transformer-based SLU system that works directly on phones. This acoustic-based SLU system consists of only two blocks and does not require the presence of ASR module. The first block is a universal phone recognition system, and the second block is a Transformer-based language model for phones. We verify the effectiveness of the system on an intent classification dataset in Mandarin Chinese.

</details>

### [The USTC-NELSLIP Systems for Simultaneous Speech Translation Task at IWSLT 2021](2107.00279.md)
**Dan Liu, Mengge Du, Xiaoxi Li, Yuchen Hu et al.** · 2021-07-01

<details>
<summary>Abstract</summary>

This paper describes USTC-NELSLIP's submissions to the IWSLT2021 Simultaneous Speech Translation task. We proposed a novel simultaneous translation model, Cross Attention Augmented Transducer (CAAT), which extends conventional RNN-T to sequence-to-sequence tasks without monotonic constraints, e.g., simultaneous translation. Experiments on speech-to-text (S2T) and text-to-text (T2T) simultaneous translation tasks shows CAAT achieves better quality-latency trade-offs compared to \textit{wait-k}, one of the previous state-of-the-art approaches. Based on CAAT architecture and data augmentation, we build S2T and T2T simultaneous translation systems in this evaluation campaign. Compared to last year's optimal systems, our S2T simultaneous translation system improves by an average of 11.3 BLEU for all latency regimes, and our T2T simultaneous translation system improves by an average of 4.6 BLEU.

</details>

### [Sequence-level Confidence Classifier for ASR Utterance Accuracy and Application to Acoustic Models](2107.00099.md)
**Amber Afshan, Kshitiz Kumar, Jian Wu** · 2021-06-30

<details>
<summary>Abstract</summary>

Scores from traditional confidence classifiers (CCs) in automatic speech recognition (ASR) systems lack universal interpretation and vary with updates to the underlying confidence or acoustic models (AMs). In this work, we build interpretable confidence scores with an objective to closely align with ASR accuracy. We propose a new sequence-level CC with a richer context providing CC scores highly correlated with ASR accuracy and scores stable across CC updates. Hence, expanding CC applications. Recently, AM customization has gained traction with the widespread use of unified models. Conventional adaptation strategies that customize AM expect well-matched data for the target domain with gold-standard transcriptions. We propose a cost-effective method of using CC scores to select an optimal adaptation data set, where we maximize ASR gains from minimal data. We study data in various confidence ranges and optimally choose data for AM adaptation with KL-Divergence regularization. On the Microsoft voice search task, data selection for supervised adaptation using the sequence-level confidence scores achieves word error rate reduction (WERR) of 8.5% for row-convolution LSTM (RC-LSTM) and 5.2% for latency-controlled bidirectional LSTM (LC-BLSTM). In the semi-supervised case, with ASR hypotheses as labels, our method provides WERR of 5.9% and 2.8% for RC-LSTM and LC-BLSTM, respectively.

</details>

### [IMS' Systems for the IWSLT 2021 Low-Resource Speech Translation Task](2106.16055.md)
**Pavel Denisov, Manuel Mager, Ngoc Thang Vu** · 2021-06-30

<details>
<summary>Abstract</summary>

This paper describes the submission to the IWSLT 2021 Low-Resource Speech Translation Shared Task by IMS team. We utilize state-of-the-art models combined with several data augmentation, multi-task and transfer learning approaches for the automatic speech recognition (ASR) and machine translation (MT) steps of our cascaded system. Moreover, we also explore the feasibility of a full end-to-end speech translation (ST) model in the case of very constrained amount of ground truth labeled data. Our best system achieves the best performance among all submitted systems for Congolese Swahili to English and French with BLEU scores 7.7 and 13.7 respectively, and the second best result for Coastal Swahili to English with BLEU score 14.9.

</details>

### [On joint training with interfaces for spoken language understanding](2106.15919.md)
**Anirudh Raju, Milind Rao, Gautam Tiwari, Pranav Dheram et al.** · 2021-06-30

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) systems extract both text transcripts and semantics associated with intents and slots from input speech utterances. SLU systems usually consist of (1) an automatic speech recognition (ASR) module, (2) an interface module that exposes relevant outputs from ASR, and (3) a natural language understanding (NLU) module. Interfaces in SLU systems carry information on text transcriptions or richer information like neural embeddings from ASR to NLU. In this paper, we study how interfaces affect joint-training for spoken language understanding. Most notably, we obtain the state-of-the-art results on the publicly available 50-hr SLURP dataset. We first leverage large-size pretrained ASR and NLU models that are connected by a text interface, and then jointly train both models via a sequence loss function. For scenarios where pretrained models are not utilized, the best results are obtained through a joint sequence loss training using richer neural interfaces. Finally, we show the overall diminishing impact of leveraging pretrained models with increased training data size.

</details>

### [Rethinking End-to-End Evaluation of Decomposable Tasks: A Case Study on Spoken Language Understanding](2106.15065.md)
**Siddhant Arora, Alissa Ostapenko, Vijay Viswanathan, Siddharth Dalmia et al.** · 2021-06-29

<details>
<summary>Abstract</summary>

Decomposable tasks are complex and comprise of a hierarchy of sub-tasks. Spoken intent prediction, for example, combines automatic speech recognition and natural language understanding. Existing benchmarks, however, typically hold out examples for only the surface-level sub-task. As a result, models with similar performance on these benchmarks may have unobserved performance differences on the other sub-tasks. To allow insightful comparisons between competitive end-to-end architectures, we propose a framework to construct robust test sets using coordinate ascent over sub-task specific utility functions. Given a dataset for a decomposable task, our method optimally creates a test set for each sub-task to individually assess sub-components of the end-to-end model. Using spoken language understanding as a case study, we generate new splits for the Fluent Speech Commands and Snips SmartLights datasets. Each split has two test sets: one with held-out utterances assessing natural language understanding abilities, and one with held-out speakers to test speech processing skills. Our splits identify performance gaps up to 10% between end-to-end systems that were within 1% of each other on the original test sets. These performance gaps allow more realistic and actionable comparisons between different architectures, driving future model development. We release our splits and tools for the community.

</details>

### [Use of Machine Learning Technique to maximize the signal over background for $H \rightarrow ττ$](2106.14257.md)
**Kanhaiya Gupta** · 2021-06-27

<details>
<summary>Abstract</summary>

In recent years, artificial neural networks (ANNs) have won numerous contests in pattern recognition and machine learning. ANNS have been applied to problems ranging from speech recognition to prediction of protein secondary structure, classification of cancers, and gene prediction. Here, we intend to maximize the chances of finding the Higgs boson decays to two $τ$ leptons in the pseudo dataset using a Machine Learning technique to classify the recorded events as signal or background.

</details>

### [Open, Sesame! Introducing Access Control to Voice Services](2106.14191.md)
**Dominika Woszczyk, Alvin Lee, Soteris Demetriou** · 2021-06-27

<details>
<summary>Abstract</summary>

Personal voice assistants (VAs) are shown to be vulnerable against record-and-replay, and other acoustic attacks which allow an adversary to gain unauthorized control of connected devices within a smart home. Existing defenses either lack detection and management capabilities or are too coarse-grained to enable flexible policies on par with other computing interfaces. In this work, we present Sesame, a lightweight framework for edge devices which is the first to enable fine-grained access control of smart-home voice commands. Sesame combines three components: Automatic Speech Recognition, Natural Language Understanding (NLU) and a Policy module. We implemented Sesame on Android devices and demonstrate that our system can enforce security policies for both Alexa and Google Home in real-time (362ms end-to-end inference time), with a lightweight (<25MB) NLU model which exhibits minimal accuracy loss compared to its non-compact equivalent.

</details>

### [On a novel training algorithm for sequence-to-sequence predictive recurrent networks](2106.14120.md)
**Boris Rubinstein** · 2021-06-27

<details>
<summary>Abstract</summary>

Neural networks mapping sequences to sequences (seq2seq) lead to significant progress in machine translation and speech recognition. Their traditional architecture includes two recurrent networks (RNs) followed by a linear predictor. In this manuscript we perform analysis of a corresponding algorithm and show that the parameters of the RNs of the well trained predictive network are not independent of each other. Their dependence can be used to significantly improve the network effectiveness. The traditional seq2seq algorithms require short term memory of a size proportional to the predicted sequence length. This requirement is quite difficult to implement in a neuroscience context. We present a novel memoryless algorithm for seq2seq predictive networks and compare it to the traditional one in the context of time series prediction. We show that the new algorithm is more robust and makes predictions with higher accuracy than the traditional one.

</details>

### [Cross-Modal Knowledge Distillation Method for Automatic Cued Speech Recognition](2106.13686.md)
**Jianrong Wang, Ziyue Tang, Xuewei Li, Mei Yu et al.** · 2021-06-25

<details>
<summary>Abstract</summary>

Cued Speech (CS) is a visual communication system for the deaf or hearing impaired people. It combines lip movements with hand cues to obtain a complete phonetic repertoire. Current deep learning based methods on automatic CS recognition suffer from a common problem, which is the data scarcity. Until now, there are only two public single speaker datasets for French (238 sentences) and British English (97 sentences). In this work, we propose a cross-modal knowledge distillation method with teacher-student structure, which transfers audio speech information to CS to overcome the limited data problem. Firstly, we pretrain a teacher model for CS recognition with a large amount of open source audio speech data, and simultaneously pretrain the feature extractors for lips and hands using CS data. Then, we distill the knowledge from teacher model to the student model with frame-level and sequence-level distillation strategies. Importantly, for frame-level, we exploit multi-task learning to weigh losses automatically, to obtain the balance coefficient. Besides, we establish a five-speaker British English CS dataset for the first time. The proposed method is evaluated on French and British English CS datasets, showing superior CS recognition performance to the state-of-the-art (SOTA) by a large margin.

</details>

### [Building Intelligent Autonomous Navigation Agents](2106.13415.md)
**Devendra Singh Chaplot** · 2021-06-25

<details>
<summary>Abstract</summary>

Breakthroughs in machine learning in the last decade have led to `digital intelligence', i.e. machine learning models capable of learning from vast amounts of labeled data to perform several digital tasks such as speech recognition, face recognition, machine translation and so on. The goal of this thesis is to make progress towards designing algorithms capable of `physical intelligence', i.e. building intelligent autonomous navigation agents capable of learning to perform complex navigation tasks in the physical world involving visual perception, natural language understanding, reasoning, planning, and sequential decision making. Despite several advances in classical navigation methods in the last few decades, current navigation agents struggle at long-term semantic navigation tasks. In the first part of the thesis, we discuss our work on short-term navigation using end-to-end reinforcement learning to tackle challenges such as obstacle avoidance, semantic perception, language grounding, and reasoning. In the second part, we present a new class of navigation methods based on modular learning and structured explicit map representations, which leverage the strengths of both classical and end-to-end learning methods, to tackle long-term navigation tasks. We show that these methods are able to effectively tackle challenges such as localization, mapping, long-term planning, exploration and learning semantic priors. These modular learning methods are capable of long-term spatial and semantic understanding and achieve state-of-the-art results on various navigation tasks.

</details>

### [Where are we in semantic concept extraction for Spoken Language Understanding?](2106.13045.md)
**Sahar Ghannay, Antoine Caubrière, Salima Mdhaffar, Gaëlle Laperrière et al.** · 2021-06-24

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) topic has seen a lot of progress these last three years, with the emergence of end-to-end neural approaches. Spoken language understanding refers to natural language processing tasks related to semantic extraction from speech signal, like named entity recognition from speech or slot filling task in a context of human-machine dialogue. Classically, SLU tasks were processed through a cascade approach that consists in applying, firstly, an automatic speech recognition process, followed by a natural language processing module applied to the automatic transcriptions. These three last years, end-to-end neural approaches, based on deep neural networks, have been proposed in order to directly extract the semantics from speech signal, by using a single neural model. More recent works on self-supervised training with unlabeled data open new perspectives in term of performance for automatic speech recognition and natural language processing. In this paper, we present a brief overview of the recent advances on the French MEDIA benchmark dataset for SLU, with or without the use of additional data. We also present our last results that significantly outperform the current state-of-the-art with a Concept Error Rate (CER) of 11.2%, instead of 13.6% for the last state-of-the-art system presented this year.

</details>

### [Mixtures of Deep Neural Experts for Automated Speech Scoring](2106.12475.md)
**Sara Papi, Edmondo Trentin, Roberto Gretter, Marco Matassoni et al.** · 2021-06-23

<details>
<summary>Abstract</summary>

The paper copes with the task of automatic assessment of second language proficiency from the language learners' spoken responses to test prompts. The task has significant relevance to the field of computer assisted language learning. The approach presented in the paper relies on two separate modules: (1) an automatic speech recognition system that yields text transcripts of the spoken interactions involved, and (2) a multiple classifier system based on deep learners that ranks the transcripts into proficiency classes. Different deep neural network architectures (both feed-forward and recurrent) are specialized over diverse representations of the texts in terms of: a reference grammar, the outcome of probabilistic language models, several word embeddings, and two bag-of-word models. Combination of the individual classifiers is realized either via a probabilistic pseudo-joint model, or via a neural mixture of experts. Using the data of the third Spoken CALL Shared Task challenge, the highest values to date were obtained in terms of three popular evaluation metrics.

</details>

### [A Discriminative Entity-Aware Language Model for Virtual Assistants](2106.11292.md)
**Mandana Saebi, Ernest Pusateri, Aaksha Meghawat, Christophe Van Gysel** · 2021-06-21

<details>
<summary>Abstract</summary>

High-quality automatic speech recognition (ASR) is essential for virtual assistants (VAs) to work well. However, ASR often performs poorly on VA requests containing named entities. In this work, we start from the observation that many ASR errors on named entities are inconsistent with real-world knowledge. We extend previous discriminative n-gram language modeling approaches to incorporate real-world knowledge from a Knowledge Graph (KG), using features that capture entity type-entity and entity-entity relationships. We apply our model through an efficient lattice rescoring process, achieving relative sentence error rate reductions of more than 25% on some synthesized test sets covering less popular entities, with minimal degradation on a uniformly sampled VA test set.

</details>

### [How to Reach Real-Time AI on Consumer Devices? Solutions for Programmable and Custom Architectures](2106.15021.md)
**Stylianos I. Venieris, Ioannis Panopoulos, Ilias Leontiadis, Iakovos S. Venieris** · 2021-06-21

<details>
<summary>Abstract</summary>

The unprecedented performance of deep neural networks (DNNs) has led to large strides in various Artificial Intelligence (AI) inference tasks, such as object and speech recognition. Nevertheless, deploying such AI models across commodity devices faces significant challenges: large computational cost, multiple performance objectives, hardware heterogeneity and a common need for high accuracy, together pose critical problems to the deployment of DNNs across the various embedded and mobile devices in the wild. As such, we have yet to witness the mainstream usage of state-of-the-art deep learning algorithms across consumer devices. In this paper, we provide preliminary answers to this potentially game-changing question by presenting an array of design techniques for efficient AI systems. We start by examining the major roadblocks when targeting both programmable processors and custom accelerators. Then, we present diverse methods for achieving real-time performance following a cross-stack approach. These span model-, system- and hardware-level techniques, and their combination. Our findings provide illustrative examples of AI systems that do not overburden mobile hardware, while also indicating how they can improve inference accuracy. Moreover, we showcase how custom ASIC- and FPGA-based accelerators can be an enabling factor for next-generation AI applications, such as multi-DNN systems. Collectively, these results highlight the critical need for further exploration as to how the various cross-stack solutions can be best combined in order to bring the latest advances in deep learning close to users, in a robust and efficient manner.

</details>

### [Pay Better Attention to Attention: Head Selection in Multilingual and Multi-Domain Sequence Modeling](2106.10840.md)
**Hongyu Gong, Yun Tang, Juan Pino, Xian Li** · 2021-06-21

<details>
<summary>Abstract</summary>

Multi-head attention has each of the attention heads collect salient information from different parts of an input sequence, making it a powerful mechanism for sequence modeling. Multilingual and multi-domain learning are common scenarios for sequence modeling, where the key challenge is to maximize positive transfer and mitigate negative transfer across languages and domains. In this paper, we find that non-selective attention sharing is sub-optimal for achieving good generalization across all languages and domains. We further propose attention sharing strategies to facilitate parameter sharing and specialization in multilingual and multi-domain sequence modeling. Our approach automatically learns shared and specialized attention heads for different languages and domains to mitigate their interference. Evaluated in various tasks including speech recognition, text-to-text and speech-to-text translation, the proposed attention sharing strategies consistently bring gains to sequence models built upon multi-head attention. For speech-to-text translation, our approach yields an average of $+2.0$ BLEU over $13$ language directions in multilingual setting and $+2.0$ BLEU over $3$ domains in multi-domain setting.

</details>

### [Low Resource German ASR with Untranscribed Data Spoken by Non-native Children -- INTERSPEECH 2021 Shared Task SPAPL System](2106.09963.md)
**Jinhan Wang, Yunzheng Zhu, Ruchao Fan, Wei Chu et al.** · 2021-06-18

<details>
<summary>Abstract</summary>

This paper describes the SPAPL system for the INTERSPEECH 2021 Challenge: Shared Task on Automatic Speech Recognition for Non-Native Children's Speech in German. ~ 5 hours of transcribed data and ~ 60 hours of untranscribed data are provided to develop a German ASR system for children. For the training of the transcribed data, we propose a non-speech state discriminative loss (NSDL) to mitigate the influence of long-duration non-speech segments within speech utterances. In order to explore the use of the untranscribed data, various approaches are implemented and combined together to incrementally improve the system performance. First, bidirectional autoregressive predictive coding (Bi-APC) is used to learn initial parameters for acoustic modelling using the provided untranscribed data. Second, incremental semi-supervised learning is further used to iteratively generate pseudo-transcribed data. Third, different data augmentation schemes are used at different training stages to increase the variability and size of the training data. Finally, a recurrent neural network language model (RNNLM) is used for rescoring. Our system achieves a word error rate (WER) of 39.68% on the evaluation data, an approximately 12% relative improvement over the official baseline (45.21%).

</details>

### [An Improved Single Step Non-autoregressive Transformer for Automatic Speech Recognition](2106.09885.md)
**Ruchao Fan, Wei Chu, Peng Chang, Jing Xiao et al.** · 2021-06-18

<details>
<summary>Abstract</summary>

Non-autoregressive mechanisms can significantly decrease inference time for speech transformers, especially when the single step variant is applied. Previous work on CTC alignment-based single step non-autoregressive transformer (CASS-NAT) has shown a large real time factor (RTF) improvement over autoregressive transformers (AT). In this work, we propose several methods to improve the accuracy of the end-to-end CASS-NAT, followed by performance analyses. First, convolution augmented self-attention blocks are applied to both the encoder and decoder modules. Second, we propose to expand the trigger mask (acoustic boundary) for each token to increase the robustness of CTC alignments. In addition, iterated loss functions are used to enhance the gradient update of low-layer parameters. Without using an external language model, the WERs of the improved CASS-NAT, when using the three methods, are 3.1%/7.2% on Librispeech test clean/other sets and the CER is 5.4% on the Aishell1 test set, achieving a 7%~21% relative WER/CER improvement. For the analyses, we plot attention weight distributions in the decoders to visualize the relationships between token-level acoustic embeddings. When the acoustic embeddings are visualized, we find that they have a similar behavior to word embeddings, which explains why the improved CASS-NAT performs similarly to AT.

</details>

### [Golos: Russian Dataset for Speech Research](2106.10161.md)
**Nikolay Karpov, Alexander Denisenko, Fedor Minkin** · 2021-06-18

<details>
<summary>Abstract</summary>

This paper introduces a novel Russian speech dataset called Golos, a large corpus suitable for speech research. The dataset mainly consists of recorded audio files manually annotated on the crowd-sourcing platform. The total duration of the audio is about 1240 hours. We have made the corpus freely available to download, along with the acoustic model with CTC loss prepared on this corpus. Additionally, transfer learning was applied to improve the performance of the acoustic model. In order to evaluate the quality of the dataset with the beam-search algorithm, we have built a 3-gram language model on the open Common Crawl dataset. The total word error rate (WER) metrics turned out to be about 3.3% and 11.5%.

</details>

### [Multi-mode Transformer Transducer with Stochastic Future Context](2106.09760.md)
**Kwangyoun Kim, Felix Wu, Prashant Sridhar, Kyu J. Han et al.** · 2021-06-17

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) models make fewer errors when more surrounding speech information is presented as context. Unfortunately, acquiring a larger future context leads to higher latency. There exists an inevitable trade-off between speed and accuracy. Naively, to fit different latency requirements, people have to store multiple models and pick the best one under the constraints. Instead, a more desirable approach is to have a single model that can dynamically adjust its latency based on different constraints, which we refer to as Multi-mode ASR. A Multi-mode ASR model can fulfill various latency requirements during inference -- when a larger latency becomes acceptable, the model can process longer future context to achieve higher accuracy and when a latency budget is not flexible, the model can be less dependent on future context but still achieve reliable accuracy. In pursuit of Multi-mode ASR, we propose Stochastic Future Context, a simple training procedure that samples one streaming configuration in each iteration. Through extensive experiments on AISHELL-1 and LibriSpeech datasets, we show that a Multi-mode ASR model rivals, if not surpasses, a set of competitive streaming baselines trained with different latency budgets.

</details>

### [Efficient Conformer with Prob-Sparse Attention Mechanism for End-to-EndSpeech Recognition](2106.09236.md)
**Xiong Wang, Sining Sun, Lei Xie, Long Ma** · 2021-06-17

<details>
<summary>Abstract</summary>

End-to-end models are favored in automatic speech recognition (ASR) because of their simplified system structure and superior performance. Among these models, Transformer and Conformer have achieved state-of-the-art recognition accuracy in which self-attention plays a vital role in capturing important global information. However, the time and memory complexity of self-attention increases squarely with the length of the sentence. In this paper, a prob-sparse self-attention mechanism is introduced into Conformer to sparse the computing process of self-attention in order to accelerate inference speed and reduce space consumption. Specifically, we adopt a Kullback-Leibler divergence based sparsity measurement for each query to decide whether we compute the attention function on this query. By using the prob-sparse attention mechanism, we achieve impressively 8% to 45% inference speed-up and 15% to 45% memory usage reduction of the self-attention module of Conformer Transducer while maintaining the same level of error rate.

</details>

### [Layer Pruning on Demand with Intermediate CTC](2106.09216.md)
**Jaesong Lee, Jingu Kang, Shinji Watanabe** · 2021-06-17

<details>
<summary>Abstract</summary>

Deploying an end-to-end automatic speech recognition (ASR) model on mobile/embedded devices is a challenging task, since the device computational power and energy consumption requirements are dynamically changed in practice. To overcome the issue, we present a training and pruning method for ASR based on the connectionist temporal classification (CTC) which allows reduction of model depth at run-time without any extra fine-tuning. To achieve the goal, we adopt two regularization methods, intermediate CTC and stochastic depth, to train a model whose performance does not degrade much after pruning. We present an in-depth analysis of layer behaviors using singular vector canonical correlation analysis (SVCCA), and efficient strategies for finding layers which are safe to prune. Using the proposed method, we show that a Transformer-CTC model can be pruned in various depth on demand, improving real-time factor from 0.005 to 0.002 on GPU, while each pruned sub-model maintains the accuracy of individually trained model of the same depth.

</details>

### [Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better](2106.08962.md)
**Gaurav Menghani** · 2021-06-16

<details>
<summary>Abstract</summary>

Deep Learning has revolutionized the fields of computer vision, natural language understanding, speech recognition, information retrieval and more. However, with the progressive improvements in deep learning models, their number of parameters, latency, resources required to train, etc. have all have increased significantly. Consequently, it has become important to pay attention to these footprint metrics of a model as well, not just its quality. We present and motivate the problem of efficiency in deep learning, followed by a thorough survey of the five core areas of model efficiency (spanning modeling techniques, infrastructure, and hardware) and the seminal work there. We also present an experiment-based guide along with code, for practitioners to optimize their model training and deployment. We believe this is the first comprehensive survey in the efficient deep learning space that covers the landscape of model efficiency from modeling techniques to hardware support. Our hope is that this survey would provide the reader with the mental model and the necessary understanding of the field to apply generic efficiency techniques to immediately get significant improvements, and also equip them with ideas for further research and experimentation to achieve additional gains.

</details>

### [Momentum Pseudo-Labeling for Semi-Supervised Speech Recognition](2106.08922.md)
**Yosuke Higuchi, Niko Moritz, Jonathan Le Roux, Takaaki Hori** · 2021-06-16

<details>
<summary>Abstract</summary>

Pseudo-labeling (PL) has been shown to be effective in semi-supervised automatic speech recognition (ASR), where a base model is self-trained with pseudo-labels generated from unlabeled data. While PL can be further improved by iteratively updating pseudo-labels as the model evolves, most of the previous approaches involve inefficient retraining of the model or intricate control of the label update. We present momentum pseudo-labeling (MPL), a simple yet effective strategy for semi-supervised ASR. MPL consists of a pair of online and offline models that interact and learn from each other, inspired by the mean teacher method. The online model is trained to predict pseudo-labels generated on the fly by the offline model. The offline model maintains a momentum-based moving average of the online model. MPL is performed in a single training process and the interaction between the two models effectively helps them reinforce each other to improve the ASR performance. We apply MPL to an end-to-end ASR model based on the connectionist temporal classification. The experimental results demonstrate that MPL effectively improves over the base model and is scalable to different semi-supervised scenarios with varying amounts of data or domain mismatch.

</details>

### [Topic Classification on Spoken Documents Using Deep Acoustic and Linguistic Features](2106.08637.md)
**Tan Liu, Wu Guo, Bin Gu** · 2021-06-16

<details>
<summary>Abstract</summary>

Topic classification systems on spoken documents usually consist of two modules: an automatic speech recognition (ASR) module to convert speech into text and a text topic classification (TTC) module to predict the topic class from the decoded text. In this paper, instead of using the ASR transcripts, the fusion of deep acoustic and linguistic features is used for topic classification on spoken documents. More specifically, a conventional CTC-based acoustic model (AM) using phonemes as output units is first trained, and the outputs of the layer before the linear phoneme classifier in the trained AM are used as the deep acoustic features of spoken documents. Furthermore, these deep acoustic features are fed to a phoneme-to-word (P2W) module to obtain deep linguistic features. Finally, a local multi-head attention module is proposed to fuse these two types of deep features for topic classification. Experiments conducted on a subset selected from Switchboard corpus show that our proposed framework outperforms the conventional ASR+TTC systems and achieves a 3.13% improvement in ACC.

</details>

### [Multi-Speaker ASR Combining Non-Autoregressive Conformer CTC and Conditional Speaker Chain](2106.08595.md)
**Pengcheng Guo, Xuankai Chang, Shinji Watanabe, Lei Xie** · 2021-06-16

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) models have achieved a large inference computation reduction and comparable results with autoregressive (AR) models on various sequence to sequence tasks. However, there has been limited research aiming to explore the NAR approaches on sequence to multi-sequence problems, like multi-speaker automatic speech recognition (ASR). In this study, we extend our proposed conditional chain model to NAR multi-speaker ASR. Specifically, the output of each speaker is inferred one-by-one using both the input mixture speech and previously-estimated conditional speaker features. In each step, a NAR connectionist temporal classification (CTC) encoder is used to perform parallel computation. With this design, the total inference steps will be restricted to the number of mixed speakers. Besides, we also adopt the Conformer and incorporate an intermediate CTC loss to improve the performance. Experiments on WSJ0-Mix and LibriMix corpora show that our model outperforms other NAR models with only a slight increase of latency, achieving WERs of 22.3% and 24.9%, respectively. Moreover, by including the data of variable numbers of speakers, our model can even better than the PIT-Conformer AR model with only 1/7 latency, obtaining WERs of 19.9% and 34.3% on WSJ0-2mix and WSJ0-3mix sets. All of our codes are publicly available at https://github.com/pengchengguo/espnet/tree/conditional-multispk.

</details>

### [A Study into Pre-training Strategies for Spoken Language Understanding on Dysarthric Speech](2106.08313.md)
**Pu Wang, Bagher BabaAli, Hugo Van hamme** · 2021-06-15

<details>
<summary>Abstract</summary>

End-to-end (E2E) spoken language understanding (SLU) systems avoid an intermediate textual representation by mapping speech directly into intents with slot values. This approach requires considerable domain-specific training data. In low-resource scenarios this is a major concern, e.g., in the present study dealing with SLU for dysarthric speech. Pretraining part of the SLU model for automatic speech recognition targets helps but no research has shown to which extent SLU on dysarthric speech benefits from knowledge transferred from other dysarthric speech tasks. This paper investigates the efficiency of pre-training strategies for SLU tasks on dysarthric speech. The designed SLU system consists of a TDNN acoustic model for feature encoding and a capsule network for intent and slot decoding. The acoustic model is pre-trained in two stages: initialization with a corpus of normal speech and finetuning on a mixture of dysarthric and normal speech. By introducing the intelligibility score as a metric of the impairment severity, this paper quantitatively analyzes the relation between generalization and pathology severity for dysarthric speech.

</details>

### [E2E-based Multi-task Learning Approach to Joint Speech and Accent Recognition](2106.08211.md)
**Jicheng Zhang, Yizhou Peng, Pham Van Tung, Haihua Xu et al.** · 2021-06-15

<details>
<summary>Abstract</summary>

In this paper, we propose a single multi-task learning framework to perform End-to-End (E2E) speech recognition (ASR) and accent recognition (AR) simultaneously. The proposed framework is not only more compact but can also yield comparable or even better results than standalone systems. Specifically, we found that the overall performance is predominantly determined by the ASR task, and the E2E-based ASR pretraining is essential to achieve improved performance, particularly for the AR task. Additionally, we conduct several analyses of the proposed method. First, though the objective loss for the AR task is much smaller compared with its counterpart of ASR task, a smaller weighting factor with the AR task in the joint objective function is necessary to yield better results for each task. Second, we found that sharing only a few layers of the encoder yields better AR results than sharing the overall encoder. Experimentally, the proposed method produces WER results close to the best standalone E2E ASR ones, while it achieves 7.7% and 4.2% relative improvement over standalone and single-task-based joint recognition methods on test set for accent recognition respectively.

</details>

### [Dialectal Speech Recognition and Translation of Swiss German Speech to Standard German Text: Microsoft's Submission to SwissText 2021](2106.08126.md)
**Yuriy Arabskyy, Aashish Agarwal, Subhadeep Dey, Oscar Koller** · 2021-06-15

<details>
<summary>Abstract</summary>

This paper describes the winning approach in the Shared Task 3 at SwissText 2021 on Swiss German Speech to Standard German Text, a public competition on dialect recognition and translation. Swiss German refers to the multitude of Alemannic dialects spoken in the German-speaking parts of Switzerland. Swiss German differs significantly from standard German in pronunciation, word inventory and grammar. It is mostly incomprehensible to native German speakers. Moreover, it lacks a standardized written script. To solve the challenging task, we propose a hybrid automatic speech recognition system with a lexicon that incorporates translations, a 1st pass language model that deals with Swiss German particularities, a transfer-learned acoustic model and a strong neural language model for 2nd pass rescoring. Our submission reaches 46.04% BLEU on a blind conversational test set and outperforms the second best competitor by a 12% relative margin.

</details>

### [SynthASR: Unlocking Synthetic Data for Speech Recognition](2106.07803.md)
**Amin Fazel, Wei Yang, Yulan Liu, Roberto Barra-Chicote et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) models have recently demonstrated superior performance over the traditional hybrid ASR models. Training an E2E ASR model requires a large amount of data which is not only expensive but may also raise dependency on production data. At the same time, synthetic speech generated by the state-of-the-art text-to-speech (TTS) engines has advanced to near-human naturalness. In this work, we propose to utilize synthetic speech for ASR training (SynthASR) in applications where data is sparse or hard to get for ASR model training. In addition, we apply continual learning with a novel multi-stage training strategy to address catastrophic forgetting, achieved by a mix of weighted multi-style training, data augmentation, encoder freezing, and parameter regularization. In our experiments conducted on in-house datasets for a new application of recognizing medication names, training ASR RNN-T models with synthetic audio via the proposed multi-stage training improved the recognition performance on new application by more than 65% relative, without degradation on existing general applications. Our observations show that SynthASR holds great promise in training the state-of-the-art large-scale E2E ASR models for new applications while reducing the costs and dependency on production data.

</details>

### [Assessing the Use of Prosody in Constituency Parsing of Imperfect Transcripts](2106.07794.md)
**Trang Tran, Mari Ostendorf** · 2021-06-14

<details>
<summary>Abstract</summary>

This work explores constituency parsing on automatically recognized transcripts of conversational speech. The neural parser is based on a sentence encoder that leverages word vectors contextualized with prosodic features, jointly learning prosodic feature extraction with parsing. We assess the utility of the prosody in parsing on imperfect transcripts, i.e. transcripts with automatic speech recognition (ASR) errors, by applying the parser in an N-best reranking framework. In experiments on Switchboard, we obtain 13-15% of the oracle N-best gain relative to parsing the 1-best ASR output, with insignificant impact on word recognition error rate. Prosody provides a significant part of the gain, and analyses suggest that it leads to more grammatical utterances via recovering function words.

</details>

### [Kaizen: Continuously improving teacher using Exponential Moving Average for semi-supervised speech recognition](2106.07759.md)
**Vimal Manohar, Tatiana Likhomanenko, Qiantong Xu, Wei-Ning Hsu et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

In this paper, we introduce the Kaizen framework that uses a continuously improving teacher to generate pseudo-labels for semi-supervised speech recognition (ASR). The proposed approach uses a teacher model which is updated as the exponential moving average (EMA) of the student model parameters. We demonstrate that it is critical for EMA to be accumulated with full-precision floating point. The Kaizen framework can be seen as a continuous version of the iterative pseudo-labeling approach for semi-supervised training. It is applicable for different training criteria, and in this paper we demonstrate its effectiveness for frame-level hybrid hidden Markov model-deep neural network (HMM-DNN) systems as well as sequence-level Connectionist Temporal Classification (CTC) based models. For large scale real-world unsupervised public videos in UK English and Italian languages the proposed approach i) shows more than 10% relative word error rate (WER) reduction over standard teacher-student training; ii) using just 10 hours of supervised data and a large amount of unsupervised data closes the gap to the upper-bound supervised ASR system that uses 650h or 2700h respectively.

</details>

### [CoDERT: Distilling Encoder Representations with Co-learning for Transducer-based Speech Recognition](2106.07734.md)
**Rupak Vignesh Swaminathan, Brian King, Grant P. Strimel, Jasha Droppo et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

We propose a simple yet effective method to compress an RNN-Transducer (RNN-T) through the well-known knowledge distillation paradigm. We show that the transducer's encoder outputs naturally have a high entropy and contain rich information about acoustically similar word-piece confusions. This rich information is suppressed when combined with the lower entropy decoder outputs to produce the joint network logits. Consequently, we introduce an auxiliary loss to distill the encoder logits from a teacher transducer's encoder, and explore training strategies where this encoder distillation works effectively. We find that tandem training of teacher and student encoders with an inplace encoder distillation outperforms the use of a pre-trained and static teacher transducer. We also report an interesting phenomenon we refer to as implicit distillation, that occurs when the teacher and student encoders share the same decoder. Our experiments show 5.37-8.4% relative word error rate reductions (WERR) on in-house test sets, and 5.05-6.18% relative WERRs on LibriSpeech test sets.

</details>

### [Overcoming Domain Mismatch in Low Resource Sequence-to-Sequence ASR Models using Hybrid Generated Pseudotranscripts](2106.07716.md)
**Chak-Fai Li, Francis Keith, William Hartmann, Matthew Snover et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

Sequence-to-sequence (seq2seq) models are competitive with hybrid models for automatic speech recognition (ASR) tasks when large amounts of training data are available. However, data sparsity and domain adaptation are more problematic for seq2seq models than their hybrid counterparts. We examine corpora of five languages from the IARPA MATERIAL program where the transcribed data is conversational telephone speech (CTS) and evaluation data is broadcast news (BN). We show that there is a sizable initial gap in such a data condition between hybrid and seq2seq models, and the hybrid model is able to further improve through the use of additional language model (LM) data. We use an additional set of untranscribed data primarily in the BN domain for semisupervised training. In semisupervised training, a seed model trained on transcribed data generates hypothesized transcripts for unlabeled domain-matched data for further training. By using a hybrid model with an expanded language model for pseudotranscription, we are able to improve our seq2seq model from an average word error rate (WER) of 66.7% across all five languages to 29.0% WER. While this puts the seq2seq model at a competitive operating point, hybrid models are still able to use additional LM data to maintain an advantage.

</details>

### [Using heterogeneity in semi-supervised transcription hypotheses to improve code-switched speech recognition](2106.07699.md)
**Andrew Slottje, Shannon Wotherspoon, William Hartmann, Matthew Snover et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

Modeling code-switched speech is an important problem in automatic speech recognition (ASR). Labeled code-switched data are rare, so monolingual data are often used to model code-switched speech. These monolingual data may be more closely matched to one of the languages in the code-switch pair. We show that such asymmetry can bias prediction toward the better-matched language and degrade overall model performance. To address this issue, we propose a semi-supervised approach for code-switched ASR. We consider the case of English-Mandarin code-switching, and the problem of using monolingual data to build bilingual "transcription models'' for annotation of unlabeled code-switched data. We first build multiple transcription models so that their individual predictions are variously biased toward either English or Mandarin. We then combine these biased transcriptions using confidence-based selection. This strategy generates a superior transcript for semi-supervised training, and obtains a 19% relative improvement compared to a semi-supervised system that relies on a transcription model built with only the best-matched monolingual data.

</details>

### [Audio Attacks and Defenses against AED Systems -- A Practical Study](2106.07428.md)
**Rodrigo dos Santos, Shirin Nilizadeh** · 2021-06-14

<details>
<summary>Abstract</summary>

In this paper, we evaluate deep learning-enabled AED systems against evasion attacks based on adversarial examples. We test the robustness of multiple security critical AED tasks, implemented as CNNs classifiers, as well as existing third-party Nest devices, manufactured by Google, which run their own black-box deep learning models. Our adversarial examples use audio perturbations made of white and background noises. Such disturbances are easy to create, to perform and to reproduce, and can be accessible to a large number of potential attackers, even non-technically savvy ones. We show that an adversary can focus on audio adversarial inputs to cause AED systems to misclassify, achieving high success rates, even when we use small levels of a given type of noisy disturbance. For instance, on the case of the gunshot sound class, we achieve nearly 100% success rate when employing as little as 0.05 white noise level. Similarly to what has been previously done by works focusing on adversarial examples from the image domain as well as on the speech recognition domain. We then, seek to improve classifiers' robustness through countermeasures. We employ adversarial training and audio denoising. We show that these countermeasures, when applied to audio input, can be successful, either in isolation or in combination, generating relevant increases of nearly fifty percent in the performance of the classifiers when these are under attack.

</details>

### [Cross-utterance Reranking Models with BERT and Graph Convolutional Networks for Conversational Speech Recognition](2106.06922.md)
**Shih-Hsuan Chiu, Tien-Hong Lo, Fu-An Chao, Berlin Chen** · 2021-06-13

<details>
<summary>Abstract</summary>

How to effectively incorporate cross-utterance information cues into a neural language model (LM) has emerged as one of the intriguing issues for automatic speech recognition (ASR). Existing research efforts on improving contextualization of an LM typically regard previous utterances as a sequence of additional input and may fail to capture complex global structural dependencies among these utterances. In view of this, we in this paper seek to represent the historical context information of an utterance as graph-structured data so as to distill cross-utterances, global word interaction relationships. To this end, we apply a graph convolutional network (GCN) on the resulting graph to obtain the corresponding GCN embeddings of historical words. GCN has recently found its versatile applications on social-network analysis, text summarization, and among others due mainly to its ability of effectively capturing rich relational information among elements. However, GCN remains largely underexplored in the context of ASR, especially for dealing with conversational speech. In addition, we frame ASR N-best reranking as a prediction problem, leveraging bidirectional encoder representations from transformers (BERT) as the vehicle to not only seize the local intrinsic word regularity patterns inherent in a candidate hypothesis but also incorporate the cross-utterance, historical word interaction cues distilled by GCN for promoting performance. Extensive experiments conducted on the AMI benchmark dataset seem to confirm the pragmatic utility of our methods, in relation to some current top-of-the-line methods.

</details>

### [GigaSpeech: An Evolving, Multi-domain ASR Corpus with 10,000 Hours of Transcribed Audio](2106.06909.md)
**Guoguo Chen, Shuzhou Chai, Guanbo Wang, Jiayu Du et al.** · 2021-06-13

<details>
<summary>Abstract</summary>

This paper introduces GigaSpeech, an evolving, multi-domain English speech recognition corpus with 10,000 hours of high quality labeled audio suitable for supervised training, and 40,000 hours of total audio suitable for semi-supervised and unsupervised training. Around 40,000 hours of transcribed audio is first collected from audiobooks, podcasts and YouTube, covering both read and spontaneous speaking styles, and a variety of topics, such as arts, science, sports, etc. A new forced alignment and segmentation pipeline is proposed to create sentence segments suitable for speech recognition training, and to filter out segments with low-quality transcription. For system training, GigaSpeech provides five subsets of different sizes, 10h, 250h, 1000h, 2500h, and 10000h. For our 10,000-hour XL training subset, we cap the word error rate at 4% during the filtering/validation stage, and for all our other smaller training subsets, we cap it at 0%. The DEV and TEST evaluation sets, on the other hand, are re-processed by professional human transcribers to ensure high transcription quality. Baseline systems are provided for popular speech recognition toolkits, namely Athena, ESPnet, Kaldi and Pika.

</details>

### [Incorporating External POS Tagger for Punctuation Restoration](2106.06731.md)
**Ning Shi, Wei Wang, Boxin Wang, Jinfeng Li et al.** · 2021-06-12

<details>
<summary>Abstract</summary>

Punctuation restoration is an important post-processing step in automatic speech recognition. Among other kinds of external information, part-of-speech (POS) taggers provide informative tags, suggesting each input token's syntactic role, which has been shown to be beneficial for the punctuation restoration task. In this work, we incorporate an external POS tagger and fuse its predicted labels into the existing language model to provide syntactic information. Besides, we propose sequence boundary sampling (SBS) to learn punctuation positions more efficiently as a sequence tagging task. Experimental results show that our methods can consistently obtain performance gains and achieve a new state-of-the-art on the common IWSLT benchmark. Further ablation studies illustrate that both large pre-trained language models and the external POS tagger take essential parts to improve the model's performance.

</details>

### [Leveraging Pre-trained Language Model for Speech Sentiment Analysis](2106.06598.md)
**Suwon Shon, Pablo Brusco, Jing Pan, Kyu J. Han et al.** · 2021-06-11

<details>
<summary>Abstract</summary>

In this paper, we explore the use of pre-trained language models to learn sentiment information of written texts for speech sentiment analysis. First, we investigate how useful a pre-trained language model would be in a 2-step pipeline approach employing Automatic Speech Recognition (ASR) and transcripts-based sentiment analysis separately. Second, we propose a pseudo label-based semi-supervised training strategy using a language model on an end-to-end speech sentiment approach to take advantage of a large, but unlabeled speech dataset for training. Although spoken and written texts have different linguistic characteristics, they can complement each other in understanding sentiment. Therefore, the proposed system can not only model acoustic characteristics to bear sentiment-specific information in speech signals, but learn latent information to carry sentiments in the text representation. In these experiments, we demonstrate the proposed approaches improve F1 scores consistently compared to systems without a language model. Moreover, we also show that the proposed framework can reduce 65% of human supervision by leveraging a large amount of data without human sentiment annotation and boost performance in a low-resource condition where the human sentiment annotation is not available enough.

</details>

### [Improving RNN-T ASR Performance with Date-Time and Location Awareness](2106.06183.md)
**Swayambhu Nath Ray, Soumyajit Mitra, Raghavendra Bilgi, Sri Garimella** · 2021-06-11

<details>
<summary>Abstract</summary>

In this paper, we explore the benefits of incorporating context into a Recurrent Neural Network (RNN-T) based Automatic Speech Recognition (ASR) model to improve the speech recognition for virtual assistants. Specifically, we use meta information extracted from the time at which the utterance is spoken and the approximate location information to make ASR context aware. We show that these contextual information, when used individually, improves overall performance by as much as 3.48% relative to the baseline and when the contexts are combined, the model learns complementary features and the recognition improves by 4.62%. On specific domains, these contextual signals show improvements as high as 11.5%, without any significant degradation on others. We ran experiments with models trained on data of sizes 30K hours and 10K hours. We show that the scale of improvement with the 10K hours dataset is much higher than the one obtained with 30K hours dataset. Our results indicate that with limited data to train the ASR model, contextual signals can improve the performance significantly.

</details>

### [Direct Simultaneous Speech-to-Text Translation Assisted by Synchronized Streaming ASR](2106.06636.md)
**Junkun Chen, Mingbo Ma, Renjie Zheng, Liang Huang** · 2021-06-11

<details>
<summary>Abstract</summary>

Simultaneous speech-to-text translation is widely useful in many scenarios. The conventional cascaded approach uses a pipeline of streaming ASR followed by simultaneous MT, but suffers from error propagation and extra latency. To alleviate these issues, recent efforts attempt to directly translate the source speech into target text simultaneously, but this is much harder due to the combination of two separate tasks. We instead propose a new paradigm with the advantages of both cascaded and end-to-end approaches. The key idea is to use two separate, but synchronized, decoders on streaming ASR and direct speech-to-text translation (ST), respectively, and the intermediate results of ASR guide the decoding policy of (but is not fed as input to) ST. During training time, we use multitask learning to jointly learn these two tasks with a shared encoder. En-to-De and En-to-Es experiments on the MuSTC dataset demonstrate that our proposed technique achieves substantially better translation quality at similar levels of latency.

</details>

### [Exploiting Large-scale Teacher-Student Training for On-device Acoustic Models](2106.06126.md)
**Jing Liu, Rupak Vignesh Swaminathan, Sree Hari Krishnan Parthasarathi, Chunchuan Lyu et al.** · 2021-06-11

<details>
<summary>Abstract</summary>

We present results from Alexa speech teams on semi-supervised learning (SSL) of acoustic models (AM) with experiments spanning over 3000 hours of GPU time, making our study one of the largest of its kind. We discuss SSL for AMs in a small footprint setting, showing that a smaller capacity model trained with 1 million hours of unsupervised data can outperform a baseline supervised system by 14.3% word error rate reduction (WERR). When increasing the supervised data to seven-fold, our gains diminish to 7.1% WERR; to improve SSL efficiency at larger supervised data regimes, we employ a step-wise distillation into a smaller model, obtaining a WERR of 14.4%. We then switch to SSL using larger student models in low data regimes; while learning efficiency with unsupervised data is higher, student models may outperform teacher models in such a setting. We develop a theoretical sketch to explain this behavior.

</details>

### [PARP: Prune, Adjust and Re-Prune for Self-Supervised Speech Recognition](2106.05933.md)
**Cheng-I Jeff Lai, Yang Zhang, Alexander H. Liu, Shiyu Chang et al.** · 2021-06-10

<details>
<summary>Abstract</summary>

Self-supervised speech representation learning (speech SSL) has demonstrated the benefit of scale in learning rich representations for Automatic Speech Recognition (ASR) with limited paired data, such as wav2vec 2.0. We investigate the existence of sparse subnetworks in pre-trained speech SSL models that achieve even better low-resource ASR results. However, directly applying widely adopted pruning methods such as the Lottery Ticket Hypothesis (LTH) is suboptimal in the computational cost needed. Moreover, we show that the discovered subnetworks yield minimal performance gain compared to the original dense network. We present Prune-Adjust-Re-Prune (PARP), which discovers and finetunes subnetworks for much better performance, while only requiring a single downstream ASR finetuning run. PARP is inspired by our surprising observation that subnetworks pruned for pre-training tasks need merely a slight adjustment to achieve a sizeable performance boost in downstream ASR tasks. Extensive experiments on low-resource ASR verify (1) sparse subnetworks exist in mono-lingual/multi-lingual pre-trained speech SSL, and (2) the computational advantage and performance gain of PARP over baseline pruning methods. In particular, on the 10min Librispeech split without LM decoding, PARP discovers subnetworks from wav2vec 2.0 with an absolute 10.9%/12.6% WER decrease compared to the full model. We further demonstrate the effectiveness of PARP via: cross-lingual pruning without any phone recognition degradation, the discovery of a multi-lingual subnetwork for 10 spoken languages in 1 finetuning run, and its applicability to pre-trained BERT/XLNet for natural language tasks.

</details>

### [Balanced End-to-End Monolingual pre-training for Low-Resourced Indic Languages Code-Switching Speech Recognition](2106.05885.md)
**Amir Hussein, Shammur Chowdhury, Najim Dehak, Ahmed Ali** · 2021-06-10

<details>
<summary>Abstract</summary>

The success in designing Code-Switching (CS) ASR often depends on the availability of the transcribed CS resources. Such dependency harms the development of ASR in low-resourced languages such as Bengali and Hindi. In this paper, we exploit the transfer learning approach to design End-to-End (E2E) CS ASR systems for the two low-resourced language pairs using different monolingual speech data and a small set of noisy CS data. We trained the CS-ASR, following two steps: (i) building a robust bilingual ASR system using a convolution-augmented transformer (Conformer) based acoustic model and n-gram language model, and (ii) fine-tuned the entire E2E ASR with limited noisy CS data. We tested our method on MUCS 2021 challenge and achieved 3rd place in the CS track. We then tested the proposed method using noisy CS data released for Hindi-English and Bengali-English pairs in Multilingual and Code-Switching ASR Challenges for Low Resource Indian Languages (MUCS 2021) and achieved 3rd place in the CS track. Unlike, the leading two systems that benefited from crawling YouTube and learning transliteration pairs, our proposed transfer learning approach focused on using only the limited CS data with no data-cleaning or data re-segmentation. Our approach achieved 14.1% relative gain in word error rate (WER) in Hindi-English and 27.1% in Bengali-English. We provide detailed guidelines on the steps to finetune the self-attention based model for limited data for ASR. Moreover, we release the code and recipe used in this paper.

</details>

### [A Wearable Virtual Touch System for Cars](2106.05700.md)
**Gowdham Prabhakar, Priyam Rajkhowa, Pradipta Biswas** · 2021-06-10

<details>
<summary>Abstract</summary>

In automotive domain, operation of secondary tasks like accessing infotainment system, adjusting air conditioning vents, and side mirrors distract drivers from driving. Though existing modalities like gesture and speech recognition systems facilitate undertaking secondary tasks by reducing duration of eyes off the road, those often require remembering a set of gestures or screen sequences. In this paper, we have proposed two different modalities for drivers to virtually touch the dashboard display using a laser tracker with a mechanical switch and an eye gaze switch. We compared performances of our proposed modalities against conventional touch modality in automotive environment by comparing pointing and selection times of representative secondary task and also analysed effect on driving performance in terms of deviation from lane, average speed, variation in perceived workload and system usability. We did not find significant difference in driving and pointing performance between laser tracking system and existing touchscreen system. Our result also showed that the driving and pointing performance of the virtual touch system with eye gaze switch was significantly better than the same with mechanical switch. We evaluated the efficacy of the proposed virtual touch system with eye gaze switch inside a real car and investigated acceptance of the system by professional drivers using qualitative research. The quantitative and qualitative studies indicated importance of using multimodal system inside car and highlighted several criteria for acceptance of new automotive user interface.

</details>

### [U2++: Unified Two-pass Bidirectional End-to-end Model for Speech Recognition](2106.05642.md)
**Di Wu, Binbin Zhang, Chao Yang, Zhendong Peng et al.** · 2021-06-10

<details>
<summary>Abstract</summary>

The unified streaming and non-streaming two-pass (U2) end-to-end model for speech recognition has shown great performance in terms of streaming capability, accuracy, real-time factor (RTF), and latency. In this paper, we present U2++, an enhanced version of U2 to further improve the accuracy. The core idea of U2++ is to use the forward and the backward information of the labeling sequences at the same time at training to learn richer information, and combine the forward and backward prediction at decoding to give more accurate recognition results. We also proposed a new data augmentation method called SpecSub to help the U2++ model to be more accurate and robust. Our experiments show that, compared with U2, U2++ shows faster convergence at training, better robustness to the decoding method, as well as consistent 5\% - 8\% word error rate reduction gain over U2. On the experiment of AISHELL-1, we achieve a 4.63\% character error rate (CER) with a non-streaming setup and 5.05\% with a streaming setup with 320ms latency by U2++. To the best of our knowledge, 5.05\% is the best-published streaming result on the AISHELL-1 test set.

</details>

### [A Comparative Study on Neural Architectures and Training Methods for Japanese Speech Recognition](2106.05111.md)
**Shigeki Karita, Yotaro Kubo, Michiel Adriaan Unico Bacchiani, Llion Jones** · 2021-06-09

<details>
<summary>Abstract</summary>

End-to-end (E2E) modeling is advantageous for automatic speech recognition (ASR) especially for Japanese since word-based tokenization of Japanese is not trivial, and E2E modeling is able to model character sequences directly. This paper focuses on the latest E2E modeling techniques, and investigates their performances on character-based Japanese ASR by conducting comparative experiments. The results are analyzed and discussed in order to understand the relative advantages of long short-term memory (LSTM), and Conformer models in combination with connectionist temporal classification, transducer, and attention-based loss functions. Furthermore, the paper investigates on effectivity of the recent training techniques such as data augmentation (SpecAugment), variational noise injection, and exponential moving average. The best configuration found in the paper achieved the state-of-the-art character error rates of 4.1%, 3.2%, and 3.5% for Corpus of Spontaneous Japanese (CSJ) eval1, eval2, and eval3 tasks, respectively. The system is also shown to be computationally efficient thanks to the efficiency of Conformer transducers.

</details>

### [Unsupervised Automatic Speech Recognition: A Review](2106.04897.md)
**Hanan Aldarmaki, Asad Ullah, Nazar Zaki** · 2021-06-09

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems can be trained to achieve remarkable performance given large amounts of manually transcribed speech, but large labeled data sets can be difficult or expensive to acquire for all languages of interest. In this paper, we review the research literature to identify models and ideas that could lead to fully unsupervised ASR, including unsupervised segmentation of the speech signal, unsupervised mapping from speech segments to text, and semi-supervised models with nominal amounts of labeled examples. The objective of the study is to identify the limitations of what can be learned from speech data alone and to understand the minimum requirements for speech recognition. Identifying these limitations would help optimize the resources and efforts in ASR development for low-resource languages.

</details>

### [Sequential End-to-End Intent and Slot Label Classification and Localization](2106.04660.md)
**Yiran Cao, Nihal Potdar, Anderson R. Avila** · 2021-06-08

<details>
<summary>Abstract</summary>

Human-computer interaction (HCI) is significantly impacted by delayed responses from a spoken dialogue system. Hence, end-to-end (e2e) spoken language understanding (SLU) solutions have recently been proposed to decrease latency. Such approaches allow for the extraction of semantic information directly from the speech signal, thus bypassing the need for a transcript from an automatic speech recognition (ASR) system. In this paper, we propose a compact e2e SLU architecture for streaming scenarios, where chunks of the speech signal are processed continuously to predict intent and slot values. Our model is based on a 3D convolutional neural network (3D-CNN) and a unidirectional long short-term memory (LSTM). We compare the performance of two alignment-free losses: the connectionist temporal classification (CTC) method and its adapted version, namely connectionist temporal localization (CTL). The latter performs not only the classification but also localization of sequential audio events. The proposed solution is evaluated on the Fluent Speech Command dataset and results show our model ability to process incoming speech signal, reaching accuracy as high as 98.97 % for CTC and 98.78 % for CTL on single-label classification, and as high as 95.69 % for CTC and 95.28 % for CTL on two-label prediction.

</details>

### [Muddling Label Regularization: Deep Learning for Tabular Datasets](2106.04462.md)
**Karim Lounici, Katia Meziani, Benjamin Riu** · 2021-06-08

<details>
<summary>Abstract</summary>

Deep Learning (DL) is considered the state-of-the-art in computer vision, speech recognition and natural language processing. Until recently, it was also widely accepted that DL is irrelevant for learning tasks on tabular data, especially in the small sample regime where ensemble methods are acknowledged as the gold standard. We present a new end-to-end differentiable method to train a standard FFNN. Our method, \textbf{Muddling labels for Regularization} (\texttt{MLR}), penalizes memorization through the generation of uninformative labels and the application of a differentiable close-form regularization scheme on the last hidden layer during training. \texttt{MLR} outperforms classical NN and the gold standard (GBDT, RF) for regression and classification tasks on several datasets from the UCI database and Kaggle covering a large range of sample sizes and feature to sample ratios. Researchers and practitioners can use \texttt{MLR} on its own as an off-the-shelf \DL{} solution or integrate it into the most advanced ML pipelines.

</details>

### [Raw Waveform Encoder with Multi-Scale Globally Attentive Locally Recurrent Networks for End-to-End Speech Recognition](2106.04275.md)
**Max W. Y. Lam, Jun Wang, Chao Weng, Dan Su et al.** · 2021-06-08

<details>
<summary>Abstract</summary>

End-to-end speech recognition generally uses hand-engineered acoustic features as input and excludes the feature extraction module from its joint optimization. To extract learnable and adaptive features and mitigate information loss, we propose a new encoder that adopts globally attentive locally recurrent (GALR) networks and directly takes raw waveform as input. We observe improved ASR performance and robustness by applying GALR on different window lengths to aggregate fine-grain temporal information into multi-scale acoustic features. Experiments are conducted on a benchmark dataset AISHELL-2 and two large-scale Mandarin speech corpus of 5,000 hours and 21,000 hours. With faster speed and comparable model size, our proposed multi-scale GALR waveform encoder achieved consistent character error rate reductions (CERRs) from 7.9% to 28.1% relative over strong baselines, including Conformer and TDNN-Conformer. In particular, our approach demonstrated notable robustness than the traditional handcrafted features and outperformed the baseline MFCC-based TDNN-Conformer model by a 15.2% CERR on a music-mixed real-world speech test set.

</details>

### [Data Augmentation Methods for End-to-end Speech Recognition on Distant-Talk Scenarios](2106.03419.md)
**Emiru Tsunoo, Kentaro Shibata, Chaitanya Narisetty, Yosuke Kashiwagi et al.** · 2021-06-07

<details>
<summary>Abstract</summary>

Although end-to-end automatic speech recognition (E2E ASR) has achieved great performance in tasks that have numerous paired data, it is still challenging to make E2E ASR robust against noisy and low-resource conditions. In this study, we investigated data augmentation methods for E2E ASR in distant-talk scenarios. E2E ASR models are trained on the series of CHiME challenge datasets, which are suitable tasks for studying robustness against noisy and spontaneous speech. We propose to use three augmentation methods and thier combinations: 1) data augmentation using text-to-speech (TTS) data, 2) cycle-consistent generative adversarial network (Cycle-GAN) augmentation trained to map two different audio characteristics, the one of clean speech and of noisy recordings, to match the testing condition, and 3) pseudo-label augmentation provided by the pretrained ASR module for smoothing label distributions. Experimental results using the CHiME-6/CHiME-4 datasets show that each augmentation method individually improves the accuracy on top of the conventional SpecAugment; further improvements are obtained by combining these approaches. We achieved 4.3\% word error rate (WER) reduction, which was more significant than that of the SpecAugment, when we combine all three augmentations for the CHiME-6 task.

</details>

### [CAPE: Encoding Relative Positions with Continuous Augmented Positional Embeddings](2106.03143.md)
**Tatiana Likhomanenko, Qiantong Xu, Gabriel Synnaeve, Ronan Collobert et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

Without positional information, attention-based Transformer neural networks are permutation-invariant. Absolute or relative positional embeddings are the most popular ways to feed Transformer models with positional information. Absolute positional embeddings are simple to implement, but suffer from generalization issues when evaluating on sequences longer than seen at training time. Relative positions are more robust to input length change, but are more complex to implement and yield inferior model throughput due to extra computational and memory costs. In this paper, we propose an augmentation-based approach (CAPE) for absolute positional embeddings, which keeps the advantages of both absolute (simplicity and speed) and relative positional embeddings (better generalization). In addition, our empirical evaluation on state-of-the-art models in machine translation, image and speech recognition demonstrates that CAPE leads to better generalization performance as well as increased stability with respect to training hyper-parameters.

</details>

### [Joint ASR and Language Identification Using RNN-T: An Efficient Approach to Dynamic Language Switching](s2:618e05ab0c5e51c6d22e760cfa9bb1f3366bdfd0.md)
**Surabhi Punjabi, Harish Arsikere, Zeynab Raeesy, Chander Chandak et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

Conventional dynamic language switching enables seamless multilingual interactions by running several monolingual ASR systems in parallel and triggering the appropriate downstream components using a standalone language identification (LID) service. Since this solution is neither scalable nor cost- and memory-efficient, especially for on-device applications, we propose end-to-end, streaming, joint ASR-LID architectures based on the recurrent neural network transducer framework. Two key formulations are explored: (1) joint training using a unified output space for ASR and LID vocabularies, and (2) joint training viewed as multi-task optimization. We also evaluate the benefit of using auxiliary language information obtained on-the-fly from an acoustic LID classifier. Experiments with the English-Hindi language pair show that: (a) multi-task architectures perform better overall, and (b) the best joint architecture surpasses monolingual ASR (6.4–9.2% word error rate reduction) and acoustic LID (53.9–56.1% error rate reduction) baselines while reducing the overall memory footprint by up to 46%.

</details>

### [Improving RNN Transducer Modeling for Small-Footprint Keyword Spotting](s2:60e99521f3133344870886da1ca14ef707b10f34.md)
**Yao Tian, Haitao Yao, Meng Cai, Yaming Liu et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

The recurrent neural network transducer (RNN-T) model has been proved effective for keyword spotting (KWS) recently. However, compared with cross-entropy (CE) or connectionist temporal classification (CTC) based models, the additional prediction network in the RNN-T model increases the model size and computational cost. Besides, since the keyword training data usually only contain the keyword sequence, the prediction network might has over-fitting problems. In this paper, we improve the RNN-T modeling for small-footprint keyword spotting in three aspects. First, to address the over-fitting issue, we explore multi-task training where a CTC loss is added to the encoder. The CTC loss is calculated with both KWS data and ASR data, while the RNN-T loss is calculated with ASR data so that only the encoder is augmented with KWS data. Second, we use the feed-forward neural network to replace the LSTM for prediction network modeling. Thus all possible prediction network outputs could be pre-computed for decoding. Third, we further improve the model with transfer learning, where a model trained with 160 thousand hours of ASR data is used to initialize the KWS model. On a self-collected far-field wake-word testset, the proposed RNN-T system greatly improves the performance comparing with a strong "keyword-filler" baseline.

</details>

### [Simpleflat: A Simple Whole-Network Pre-Training Approach for RNN Transducer-Based End-to-End Speech Recognition](s2:5802d0d99ef9404fc0c63e8d0497d8527f34b9ee.md)
**Takafumi Moriya, Takanori Ashihara, Tomohiro Tanaka, Tsubasa Ochiai et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

Recurrent neural network-transducer (RNN-T) is promising for building time-synchronous end-to-end automatic speech recognition (ASR) systems, in part because it does not need frame-wise alignment between input features and target labels in the training step. Although training without alignment is beneficial, it makes it difficult to discern the relation between input features and output token sequences. This, in effect, degrades RNN-T performance. Our solution is SimpleFlat (SF), a novel and simple whole-network pretraining approach for RNN-T. SF extracts frame-wise alignments on-the-fly from the training dataset, and does not require any external resources. We distribute equal numbers of target tokens to each frame following RNN-T encoder output lengths by repeating each token. The frame-wise tokens so created are shifted, and also used as the prediction network inputs. Therefore, SF can be implemented by cross entropy loss computation as in autoregressive model training. Experiments on Japanese and English ASR tasks demonstrate that SF can effectively improve various RNN-T architectures.

</details>

### [RNN-T Based Open-Vocabulary Keyword Spotting in Mandarin with Multi-Level Detection](s2:1dc20db4eb6e4cc5d3085bcd5dd21c202e17c682.md)
**Zuozhen Liu, Ta Li, Pengyuan Zhang** · 2021-06-06

<details>
<summary>Abstract</summary>

Despite the recent prevalence of keyword spotting (KWS) in smart-home, open-vocabulary KWS remains a keen but unmet need among the users. In this paper, we propose an RNN Transducer (RNN-T) based keyword spotting system with a constrained attention mechanism biasing module that biases the RNN-T model towards a specific keyword of interest. The atonal syllables are adopted as the modeling units, which addresses the out-of-vocabulary (OOV) problem. A multi-level detection is applied to the posterior probabilities for the judgement. Evaluating on the AISHELL-2 dataset shows our proposed method outperforms the RNN-T-based approach by 2.70% in false reject rate (FRR) at 1 false alarm (FA) per hour. We further provide insights into the role of each stage of the detection cascade, where most negative samples are filtered out by the first stage with high computational efficiency.

</details>

### [Neural Utterance Confidence Measure for RNN-Transducers and Two Pass Models](s2:9d0653557a460d22443b77489f3b8c0d9858e51f.md)
**Ashutosh Gupta, Ankur Kumar, Dhananjaya N. Gowda, Kwangyoun Kim et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

In this paper, we propose methods to compute confidence score on the predictions made by an end-to-end speech recognition model in a 2-pass framework. We use RNN-Transducer for a streaming model, and an attention-based decoder for the second pass model. We use neural technique to compute the confidence score, and experiment with various combinations of features from RNN-Transducer and second pass models. The neural confidence score model is trained as a binary classification task to accept or reject a prediction made by speech recognition model. The model is evaluated in a distributed speech recognition environment, and performs significantly better when features from second pass model are used as compared to the features from streaming model.

</details>

### [Minimum Word Error Rate Training with Language Model Fusion for End-to-End Speech Recognition](2106.02302.md)
**Zhong Meng, Yu Wu, Naoyuki Kanda, Liang Lu et al.** · 2021-06-04

<details>
<summary>Abstract</summary>

Integrating external language models (LMs) into end-to-end (E2E) models remains a challenging task for domain-adaptive speech recognition. Recently, internal language model estimation (ILME)-based LM fusion has shown significant word error rate (WER) reduction from Shallow Fusion by subtracting a weighted internal LM score from an interpolation of E2E model and external LM scores during beam search. However, on different test sets, the optimal LM interpolation weights vary over a wide range and have to be tuned extensively on well-matched validation sets. In this work, we perform LM fusion in the minimum WER (MWER) training of an E2E model to obviate the need for LM weights tuning during inference. Besides MWER training with Shallow Fusion (MWER-SF), we propose a novel MWER training with ILME (MWER-ILME) where the ILME-based fusion is conducted to generate N-best hypotheses and their posteriors. Additional gradient is induced when internal LM is engaged in MWER-ILME loss computation. During inference, LM weights pre-determined in MWER training enable robust LM integrations on test sets from different domains. Experimented with 30K-hour trained transformer transducers, MWER-ILME achieves on average 8.8% and 5.8% relative WER reductions from MWER and MWER-SF training, respectively, on 6 different test sets

</details>

### [Semantic-WER: A Unified Metric for the Evaluation of ASR Transcript for End Usability](2106.02016.md)
**Somnath Roy** · 2021-06-03

<details>
<summary>Abstract</summary>

Recent advances in supervised, semi-supervised and self-supervised deep learning algorithms have shown significant improvement in the performance of automatic speech recognition(ASR) systems. The state-of-the-art systems have achieved a word error rate (WER) less than 5%. However, in the past, researchers have argued the non-suitability of the WER metric for the evaluation of ASR systems for downstream tasks such as spoken language understanding (SLU) and information retrieval. The reason is that the WER works at the surface level and does not include any syntactic and semantic knowledge.The current work proposes Semantic-WER (SWER), a metric to evaluate the ASR transcripts for downstream applications in general. The SWER can be easily customized for any down-stream task.

</details>

### [A Discussion On the Validity of Manifold Learning](2106.01608.md)
**Dai Shi, Andi Han, Yi Guo, Junbin Gao** · 2021-06-03

<details>
<summary>Abstract</summary>

Dimensionality reduction (DR) and manifold learning (ManL) have been applied extensively in many machine learning tasks, including signal processing, speech recognition, and neuroinformatics. However, the understanding of whether DR and ManL models can generate valid learning results remains unclear. In this work, we investigate the validity of learning results of some widely used DR and ManL methods through the chart mapping function of a manifold. We identify a fundamental problem of these methods: the mapping functions induced by these methods violate the basic settings of manifolds, and hence they are not learning manifold in the mathematical sense. To address this problem, we provide a provably correct algorithm called fixed points Laplacian mapping (FPLM), that has the geometric guarantee to find a valid manifold representation (up to a homeomorphism). Combining one additional condition(orientation preserving), we discuss a sufficient condition for an algorithm to be bijective for any d-simplex decomposition result on a d-manifold. However, constructing such a mapping function and its computational method satisfying these conditions is still an open problem in mathematics.

</details>

### [Lightweight Adapter Tuning for Multilingual Speech Translation](2106.01463.md)
**Hang Le, Juan Pino, Changhan Wang, Jiatao Gu et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

Adapter modules were recently introduced as an efficient alternative to fine-tuning in NLP. Adapter tuning consists in freezing pretrained parameters of a model and injecting lightweight modules between layers, resulting in the addition of only a small number of task-specific trainable parameters. While adapter tuning was investigated for multilingual neural machine translation, this paper proposes a comprehensive analysis of adapters for multilingual speech translation (ST). Starting from different pre-trained models (a multilingual ST trained on parallel data or a multilingual BART (mBART) trained on non-parallel multilingual data), we show that adapters can be used to: (a) efficiently specialize ST to specific language pairs with a low extra cost in terms of parameters, and (b) transfer from an automatic speech recognition (ASR) task and an mBART pre-trained model to a multilingual ST task. Experiments show that adapter tuning offer competitive results to full fine-tuning, while being much more parameter-efficient.

</details>

### [Attention-based Contextual Language Model Adaptation for Speech Recognition](2106.01451.md)
**Richard Diehl Martinez, Scott Novotney, Ivan Bulyko, Ariya Rastrow et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

Language modeling (LM) for automatic speech recognition (ASR) does not usually incorporate utterance level contextual information. For some domains like voice assistants, however, additional context, such as the time at which an utterance was spoken, provides a rich input signal. We introduce an attention mechanism for training neural speech recognition language models on both text and non-linguistic contextual data. When applied to a large de-identified dataset of utterances collected by a popular voice assistant platform, our method reduces perplexity by 7.0% relative over a standard LM that does not incorporate contextual information. When evaluated on utterances extracted from the long tail of the dataset, our method improves perplexity by 9.0% relative over a standard LM and by over 2.8% relative when compared to a state-of-the-art model for contextual LM.

</details>

### [Dual Script E2E framework for Multilingual and Code-Switching ASR](2106.01400.md)
**Mari Ganesh Kumar, Jom Kuriakose, Anand Thyagachandran, Arun Kumar A et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

India is home to multiple languages, and training automatic speech recognition (ASR) systems for languages is challenging. Over time, each language has adopted words from other languages, such as English, leading to code-mixing. Most Indian languages also have their own unique scripts, which poses a major limitation in training multilingual and code-switching ASR systems. Inspired by results in text-to-speech synthesis, in this work, we use an in-house rule-based phoneme-level common label set (CLS) representation to train multilingual and code-switching ASR for Indian languages. We propose two end-to-end (E2E) ASR systems. In the first system, the E2E model is trained on the CLS representation, and we use a novel data-driven back-end to recover the native language script. In the second system, we propose a modification to the E2E model, wherein the CLS representation and the native language characters are used simultaneously for training. We show our results on the multilingual and code-switching tasks of the Indic ASR Challenge 2021. Our best results achieve 6% and 5% improvement (approx) in word error rate over the baseline system for the multilingual and code-switching tasks, respectively, on the challenge development data.

</details>

### [Automatic Speech Recognition in Sanskrit: A New Speech Corpus and Modelling Insights](2106.05852.md)
**Devaraja Adiga, Rishabh Kumar, Amrith Krishna, Preethi Jyothi et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) in Sanskrit is interesting, owing to the various linguistic peculiarities present in the language. The Sanskrit language is lexically productive, undergoes euphonic assimilation of phones at the word boundaries and exhibits variations in spelling conventions and in pronunciations. In this work, we propose the first large scale study of automatic speech recognition (ASR) in Sanskrit, with an emphasis on the impact of unit selection in Sanskrit ASR. In this work, we release a 78 hour ASR dataset for Sanskrit, which faithfully captures several of the linguistic characteristics expressed by the language. We investigate the role of different acoustic model and language model units in ASR systems for Sanskrit. We also propose a new modelling unit, inspired by the syllable level unit selection, that captures character sequences from one vowel in the word to the next vowel. We also highlight the importance of choosing graphemic representations for Sanskrit and show the impact of this choice on word error rates (WER). Finally, we extend these insights from Sanskrit ASR for building ASR systems in two other Indic languages, Gujarati and Telugu. For both these languages, our experimental results show that the use of phonetic based graphemic representations in ASR results in performance improvements as compared to ASR systems that use native scripts.

</details>

### [Improving low-resource ASR performance with untranscribed out-of-domain data](2106.01227.md)
**Jayadev Billa** · 2021-06-02

<details>
<summary>Abstract</summary>

Semi-supervised training (SST) is a common approach to leverage untranscribed/unlabeled speech data to improve automatic speech recognition performance in low-resource languages. However, if the available unlabeled speech is mismatched to the target domain, SST is not as effective, and in many cases performs worse than the original system. In this paper, we address the issue of low-resource ASR when only untranscribed out-of-domain speech data is readily available in the target language. Specifically, we look to improve performance on conversational/telephony speech (target domain) using web resources, in particular YouTube data, which more closely resembles news/topical broadcast data. Leveraging SST, we show that while in some cases simply pooling the out-of-domain data with the training data lowers word error rate (WER), in all cases, we see improvements if we train first with the out-of-domain data and then fine-tune the resulting model with the original training data. Using 2000 hours of speed perturbed YouTube audio in each target language, with semi-supervised transcripts, we show improvements on multiple languages/data sets, of up to 16.3% relative improvement in WER over the baseline systems and up to 7.4% relative improvement in WER over a system that simply pools the out-of-domain data with the training data.

</details>

### [Should We Always Separate?: Switching Between Enhanced and Observed Signals for Overlapping Speech Recognition](2106.00949.md)
**Hiroshi Sato, Tsubasa Ochiai, Marc Delcroix, Keisuke Kinoshita et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

Although recent advances in deep learning technology improved automatic speech recognition (ASR), it remains difficult to recognize speech when it overlaps other people's voices. Speech separation or extraction is often used as a front-end to ASR to handle such overlapping speech. However, deep neural network-based speech enhancement can generate `processing artifacts' as a side effect of the enhancement, which degrades ASR performance. For example, it is well known that single-channel noise reduction for non-speech noise (non-overlapping speech) often does not improve ASR. Likewise, the processing artifacts may also be detrimental to ASR in some conditions when processing overlapping speech with a separation/extraction method, although it is usually believed that separation/extraction improves ASR. In order to answer the question `Do we always have to separate/extract speech from mixtures?', we analyze ASR performance on observed and enhanced speech at various noise and interference conditions, and show that speech enhancement degrades ASR under some conditions even for overlapping speech. Based on these findings, we propose a simple switching algorithm between observed and enhanced speech based on the estimated signal-to-interference ratio and signal-to-noise ratio. We demonstrated experimentally that such a simple switching mechanism can improve recognition performance when processing artifacts are detrimental to ASR.

</details>

### [A Neural Acoustic Echo Canceller Optimized Using An Automatic Speech Recognizer And Large Scale Synthetic Data](2106.00856.md)
**Nathan Howard, Alex Park, Turaj Zakizadeh Shabestary, Alexander Gruenstein et al.** · 2021-06-01

<details>
<summary>Abstract</summary>

We consider the problem of recognizing speech utterances spoken to a device which is generating a known sound waveform; for example, recognizing queries issued to a digital assistant which is generating responses to previous user inputs. Previous work has proposed building acoustic echo cancellation (AEC) models for this task that optimize speech enhancement metrics using both neural network as well as signal processing approaches. Since our goal is to recognize the input speech, we consider enhancements which improve word error rates (WERs) when the predicted speech signal is passed to an automatic speech recognition (ASR) model. First, we augment the loss function with a term that produces outputs useful to a pre-trained ASR model and show that this augmented loss function improves WER metrics. Second, we demonstrate that augmenting our training dataset of real world examples with a large synthetic dataset improves performance. Crucially, applying SpecAugment style masks to the reference channel during training aids the model in adapting from synthetic to real domains. In experimental evaluations, we find the proposed approaches improve performance, on average, by 57% over a signal processing baseline and 45% over the neural AEC model without the proposed changes.

</details>

### [Multilingual Speech Translation with Unified Transformer: Huawei Noah's Ark Lab at IWSLT 2021](2106.00197.md)
**Xingshan Zeng, Liangyou Li, Qun Liu** · 2021-06-01

<details>
<summary>Abstract</summary>

This paper describes the system submitted to the IWSLT 2021 Multilingual Speech Translation (MultiST) task from Huawei Noah's Ark Lab. We use a unified transformer architecture for our MultiST model, so that the data from different modalities (i.e., speech and text) and different tasks (i.e., Speech Recognition, Machine Translation, and Speech Translation) can be exploited to enhance the model's ability. Specifically, speech and text inputs are firstly fed to different feature extractors to extract acoustic and textual features, respectively. Then, these features are processed by a shared encoder--decoder architecture. We apply several training techniques to improve the performance, including multi-task learning, task-level curriculum learning, data augmentation, etc. Our final system achieves significantly better results than bilingual baselines on supervised language pairs and yields reasonable results on zero-shot language pairs.

</details>

### [Fine-grained Generalization Analysis of Structured Output Prediction](2106.00115.md)
**Waleed Mustafa, Yunwen Lei, Antoine Ledent, Marius Kloft** · 2021-05-31

<details>
<summary>Abstract</summary>

In machine learning we often encounter structured output prediction problems (SOPPs), i.e. problems where the output space admits a rich internal structure. Application domains where SOPPs naturally occur include natural language processing, speech recognition, and computer vision. Typical SOPPs have an extremely large label set, which grows exponentially as a function of the size of the output. Existing generalization analysis implies generalization bounds with at least a square-root dependency on the cardinality $d$ of the label set, which can be vacuous in practice. In this paper, we significantly improve the state of the art by developing novel high-probability bounds with a logarithmic dependency on $d$. Moreover, we leverage the lens of algorithmic stability to develop generalization bounds in expectation without any dependency on $d$. Our results therefore build a solid theoretical foundation for learning in large-scale SOPPs. Furthermore, we extend our results to learning with weakly dependent data.

</details>

### [Byakto Speech: Real-time long speech synthesis with convolutional neural network: Transfer learning from English to Bangla](2106.03937.md)
**Zabir Al Nazi, Sayed Mohammed Tasmimul Huda** · 2021-05-31

<details>
<summary>Abstract</summary>

Speech synthesis is one of the challenging tasks to automate by deep learning, also being a low-resource language there are very few attempts at Bangla speech synthesis. Most of the existing works can't work with anything other than simple Bangla characters script, very short sentences, etc. This work attempts to solve these problems by introducing Byakta, the first-ever open-source deep learning-based bilingual (Bangla and English) text to a speech synthesis system. A speech recognition model-based automated scoring metric was also proposed to evaluate the performance of a TTS model. We also introduce a test benchmark dataset for Bangla speech synthesis models for evaluating speech quality. The TTS is available at https://github.com/zabir-nabil/bangla-tts

</details>

### [Low-Resource Spoken Language Identification Using Self-Attentive Pooling and Deep 1D Time-Channel Separable Convolutions](2106.00052.md)
**Roman Bedyakin, Nikolay Mikhaylovskiy** · 2021-05-31

<details>
<summary>Abstract</summary>

This memo describes NTR/TSU winning submission for Low Resource ASR challenge at Dialog2021 conference, language identification track. Spoken Language Identification (LID) is an important step in a multilingual Automated Speech Recognition (ASR) system pipeline. Traditionally, the ASR task requires large volumes of labeled data that are unattainable for most of the world's languages, including most of the languages of Russia. In this memo, we show that a convolutional neural network with a Self-Attentive Pooling layer shows promising results in low-resource setting for the language identification task and set up a SOTA for the Low Resource ASR challenge dataset. Additionally, we compare the structure of confusion matrices for this and significantly more diverse VoxForge dataset and state and substantiate the hypothesis that whenever the dataset is diverse enough so that the other classification factors, like gender, age etc. are well-averaged, the confusion matrix for LID system bears the language similarity measure.

</details>

### [Bangla Natural Language Processing: A Comprehensive Analysis of Classical, Machine Learning, and Deep Learning Based Methods](2105.14875.md)
**Ovishake Sen, Mohtasim Fuad, MD. Nazrul Islam, Jakaria Rabbi et al.** · 2021-05-31

<details>
<summary>Abstract</summary>

The Bangla language is the seventh most spoken language, with 265 million native and non-native speakers worldwide. However, English is the predominant language for online resources and technical knowledge, journals, and documentation. Consequently, many Bangla-speaking people, who have limited command of English, face hurdles to utilize English resources. To bridge the gap between limited support and increasing demand, researchers conducted many experiments and developed valuable tools and techniques to create and process Bangla language materials. Many efforts are also ongoing to make it easy to use the Bangla language in the online and technical domains. There are some review papers to understand the past, previous, and future Bangla Natural Language Processing (BNLP) trends. The studies are mainly concentrated on the specific domains of BNLP, such as sentiment analysis, speech recognition, optical character recognition, and text summarization. There is an apparent scarcity of resources that contain a comprehensive review of the recent BNLP tools and methods. Therefore, in this paper, we present a thorough analysis of 75 BNLP research papers and categorize them into 11 categories, namely Information Extraction, Machine Translation, Named Entity Recognition, Parsing, Parts of Speech Tagging, Question Answering System, Sentiment Analysis, Spam and Fake Detection, Text Summarization, Word Sense Disambiguation, and Speech Processing and Recognition. We study articles published between 1999 to 2021, and 50% of the papers were published after 2015. Furthermore, we discuss Classical, Machine Learning and Deep Learning approaches with different datasets while addressing the limitations and current and future trends of the BNLP.

</details>

### [Towards One Model to Rule All: Multilingual Strategy for Dialectal Code-Switching Arabic ASR](2105.14779.md)
**Shammur Absar Chowdhury, Amir Hussein, Ahmed Abdelali, Ahmed Ali** · 2021-05-31

<details>
<summary>Abstract</summary>

With the advent of globalization, there is an increasing demand for multilingual automatic speech recognition (ASR), handling language and dialectal variation of spoken content. Recent studies show its efficacy over monolingual systems. In this study, we design a large multilingual end-to-end ASR using self-attention based conformer architecture. We trained the system using Arabic (Ar), English (En) and French (Fr) languages. We evaluate the system performance handling: (i) monolingual (Ar, En and Fr); (ii) multi-dialectal (Modern Standard Arabic, along with dialectal variation such as Egyptian and Moroccan); (iii) code-switching -- cross-lingual (Ar-En/Fr) and dialectal (MSA-Egyptian dialect) test cases, and compare with current state-of-the-art systems. Furthermore, we investigate the influence of different embedding/character representations including character vs word-piece; shared vs distinct input symbol per language. Our findings demonstrate the strength of such a model by outperforming state-of-the-art monolingual dialectal Arabic and code-switching Arabic ASR.

</details>

### [Multi-Scale Temporal Convolution Network for Classroom Voice Detection](2105.14717.md)
**Lu Ma, Xintian Wang, Song Yang, Yaguang Gong et al.** · 2021-05-31

<details>
<summary>Abstract</summary>

Teaching with the cooperation of expert teacher and assistant teacher, which is the so-called "double-teachers classroom", i.e., the course is giving by the expert online and presented through projection screen at the classroom, and the teacher at the classroom performs as an assistant for guiding the students in learning, is becoming more prevalent in today's teaching method for K-12 education. For monitoring the teaching quality, a microphone clipped on the assistant's neckline is always used for voice recording, then fed to the downstream tasks of automatic speech recognition (ASR) and neural language processing (NLP). However, besides its voice, there would be some other interfering voices, including the expert's one and the student's one. Here, we propose to extract the assistant' voices from the perspective of sound event detection, i.e., the voices are classified into four categories, namely the expert, the teacher, the mixture of them, and the background. To make frame-level identification, which is important for grabbing sensitive words for the downstream tasks, a multi-scale temporal convolution neural network is constructed with stacked dilated convolutions for considering both local and global properties. These features are concatenated and fed to a classification network constructed by three linear layers. The framework is evaluated on simulated data and real-world recordings, giving considerable performance in terms of precision and recall, compared with some classical classification methods.

</details>

### [Creating and Implementing a Smart Speaker](2106.13675.md)
**Sanskar Jethi, Avinash Kumar Choudhary, Yash Gupta, Abhishek Chaudhary** · 2021-05-30

<details>
<summary>Abstract</summary>

We have seen significant advancements in Artificial Intelligence and Machine Learning in the 21st century. It has enabled a new technology where we can have a human-like conversation with the machines. The most significant use of this speech recognition and contextual understanding technology exists in the form of a Smart Speaker. We have a wide variety of Smart Speaker products available to us. This paper aims to decode its creation and explain the technology that makes these Speakers, "Smart."

</details>

### [Quantization and Deployment of Deep Neural Networks on Microcontrollers](2105.13331.md)
**Pierre-Emmanuel Novac, Ghouthi Boukli Hacene, Alain Pegatoquet, Benoît Miramond et al.** · 2021-05-27

<details>
<summary>Abstract</summary>

Embedding Artificial Intelligence onto low-power devices is a challenging task that has been partly overcome with recent advances in machine learning and hardware design. Presently, deep neural networks can be deployed on embedded targets to perform different tasks such as speech recognition,object detection or Human Activity Recognition. However, there is still room for optimization of deep neural networks onto embedded devices. These optimizations mainly address power consumption,memory and real-time constraints, but also an easier deployment at the edge. Moreover, there is still a need for a better understanding of what can be achieved for different use cases. This work focuses on quantization and deployment of deep neural networks onto low-power 32-bit microcontrollers. The quantization methods, relevant in the context of an embedded execution onto a microcontroller, are first outlined. Then, a new framework for end-to-end deep neural networks training, quantization and deployment is presented. This framework, called MicroAI, is designed as an alternative to existing inference engines (TensorFlow Lite for Microcontrollers and STM32CubeAI). Our framework can indeed be easily adjusted and/or extended for specific use cases. Execution using single precision 32-bit floating-point as well as fixed-point on 8- and 16-bit integers are supported. The proposed quantization method is evaluated with three different datasets (UCI-HAR, Spoken MNIST and GTSRB). Finally, a comparison study between MicroAI and both existing embedded inference engines is provided in terms of memory and power efficiency. On-device evaluation is done using ARM Cortex-M4F-based microcontrollers (Ambiq Apollo3 and STM32L452RE).

</details>

### [Multitask Learning for Grapheme-to-Phoneme Conversion of Anglicisms in German Speech Recognition](2105.12708.md)
**Julia Pritzen, Michael Gref, Dietlind Zühlke, Christoph Schmidt** · 2021-05-26

<details>
<summary>Abstract</summary>

Anglicisms are a challenge in German speech recognition. Due to their irregular pronunciation compared to native German words, automatically generated pronunciation dictionaries often include faulty phoneme sequences for Anglicisms. In this work, we propose a multitask sequence-to-sequence approach for grapheme-to-phoneme conversion to improve the phonetization of Anglicisms. We extended a grapheme-to-phoneme model with a classifier to distinguish Anglicisms from native German words. With this approach, the model learns to generate pronunciations differently depending on the classification result. We used our model to create supplementary Anglicism pronunciation dictionaries that are added to an existing German speech recognition model. Tested on a dedicated Anglicism evaluation set, we improved the recognition of Anglicisms compared to a baseline model, reducing the word error rate by 1 % and the Anglicism error rate by 3 %. We show that multitask learning can help solving the challenge of Anglicisms in German speech recognition.

</details>

### [Training Speech Enhancement Systems with Noisy Speech Datasets](2105.12315.md)
**Koichi Saito, Stefan Uhlich, Giorgio Fabbro, Yuki Mitsufuji** · 2021-05-26

<details>
<summary>Abstract</summary>

Recently, deep neural network (DNN)-based speech enhancement (SE) systems have been used with great success. During training, such systems require clean speech data - ideally, in large quantity with a variety of acoustic conditions, many different speaker characteristics and for a given sampling rate (e.g., 48kHz for fullband SE). However, obtaining such clean speech data is not straightforward - especially, if only considering publicly available datasets. At the same time, a lot of material for automatic speech recognition (ASR) with the desired acoustic/speaker/sampling rate characteristics is publicly available except being clean, i.e., it also contains background noise as this is even often desired in order to have ASR systems that are noise-robust. Hence, using such data to train SE systems is not straightforward. In this paper, we propose two improvements to train SE systems on noisy speech data. First, we propose several modifications of the loss functions, which make them robust against noisy speech targets. In particular, computing the median over the sample axis before averaging over time-frequency bins allows to use such data. Furthermore, we propose a noise augmentation scheme for mixture-invariant training (MixIT), which allows using it also in such scenarios. For our experiments, we use the Mozilla Common Voice dataset and we show that using our robust loss function improves PESQ by up to 0.19 compared to a system trained in the traditional way. Similarly, for MixIT we can see an improvement of up to 0.27 in PESQ when using our proposed noise augmentation.

</details>

### [Unsupervised Speech Recognition](2105.11084.md)
**Alexei Baevski, Wei-Ning Hsu, Alexis Conneau, Michael Auli** · 2021-05-24

<details>
<summary>Abstract</summary>

Despite rapid progress in the recent past, current speech recognition systems still require labeled training data which limits this technology to a small fraction of the languages spoken around the globe. This paper describes wav2vec-U, short for wav2vec Unsupervised, a method to train speech recognition models without any labeled data. We leverage self-supervised speech representations to segment unlabeled audio and learn a mapping from these representations to phonemes via adversarial training. The right representations are key to the success of our method. Compared to the best previous unsupervised work, wav2vec-U reduces the phoneme error rate on the TIMIT benchmark from 26.1 to 11.3. On the larger English Librispeech benchmark, wav2vec-U achieves a word error rate of 5.9 on test-other, rivaling some of the best published systems trained on 960 hours of labeled data from only two years ago. We also experiment on nine other languages, including low-resource languages such as Kyrgyz, Swahili and Tatar.

</details>

### [A Streaming End-to-End Framework For Spoken Language Understanding](2105.10042.md)
**Nihal Potdar, Anderson R. Avila, Chao Xing, Dong Wang et al.** · 2021-05-20

<details>
<summary>Abstract</summary>

End-to-end spoken language understanding (SLU) has recently attracted increasing interest. Compared to the conventional tandem-based approach that combines speech recognition and language understanding as separate modules, the new approach extracts users' intentions directly from the speech signals, resulting in joint optimization and low latency. Such an approach, however, is typically designed to process one intention at a time, which leads users to take multiple rounds to fulfill their requirements while interacting with a dialogue system. In this paper, we propose a streaming end-to-end framework that can process multiple intentions in an online and incremental way. The backbone of our framework is a unidirectional RNN trained with the connectionist temporal classification (CTC) criterion. By this design, an intention can be identified when sufficient evidence has been accumulated, and multiple intentions can be identified sequentially. We evaluate our solution on the Fluent Speech Commands (FSC) dataset and the intent detection accuracy is about 97 % on all multi-intent settings. This result is comparable to the performance of the state-of-the-art non-streaming models, but is achieved in an online and incremental way. We also employ our model to a keyword spotting task using the Google Speech Commands dataset and the results are also highly promising.

</details>

### [Exploiting Adapters for Cross-lingual Low-resource Speech Recognition](2105.11905.md)
**Wenxin Hou, Han Zhu, Yidong Wang, Jindong Wang et al.** · 2021-05-18

<details>
<summary>Abstract</summary>

Cross-lingual speech adaptation aims to solve the problem of leveraging multiple rich-resource languages to build models for a low-resource target language. Since the low-resource language has limited training data, speech recognition models can easily overfit. In this paper, we propose to use adapters to investigate the performance of multiple adapters for parameter-efficient cross-lingual speech adaptation. Based on our previous MetaAdapter that implicitly leverages adapters, we propose a novel algorithms called SimAdapter for explicitly learning knowledge from adapters. Our algorithm leverages adapters which can be easily integrated into the Transformer structure.MetaAdapter leverages meta-learning to transfer the general knowledge from training data to the test language. SimAdapter aims to learn the similarities between the source and target languages during fine-tuning using the adapters. We conduct extensive experiments on five-low-resource languages in Common Voice dataset. Results demonstrate that our MetaAdapter and SimAdapter methods can reduce WER by 2.98% and 2.55% with only 2.5% and 15.5% of trainable parameters compared to the strong full-model fine-tuning baseline. Moreover, we also show that these two novel algorithms can be integrated for better performance with up to 3.55% relative WER reduction.

</details>

### [Streaming cascade-based speech translation leveraged by a direct segmentation model](s2:172bea5507c71bd2777cca4249946f2bdf5df31c.md)
**Adrià Giménez, Alfons Juan** · 2021-05-17

<details>
<summary>Abstract</summary>

The cascade approach to Speech Translation (ST) is based on a pipeline that concatenates an Automatic Speech Recognition (ASR) system followed by a Machine Translation (MT) system. Nowadays, state-of-the-art ST systems are populated with deep neural networks that are conceived to work in an offline setup in which the audio input to be translated is fully available in advance. However, a streaming setup defines a completely different picture, in which an unbounded audio input gradually becomes available and at the same time the translation needs to be generated under real-time constraints. In this work, we present a state-of-the-art streaming ST system in which neural-based models integrated in the ASR and MT components are carefully adapted in terms of their training and decoding procedures in order to run under a streaming setup. In addition, a direct segmentation model that adapts the continuous ASR output to the capacity of simultaneous MT systems trained at the sentence level is introduced to guarantee low latency while preserving the translation quality of the complete ST system. The resulting ST system is thoroughly evaluated on the real-life streaming Europarl-ST benchmark to gauge the trade-off between quality and latency for each component individually as well as for the complete ST system.

</details>

### [Streaming cascade-based speech translation leveraged by a direct segmentation model](s2:5104ac08384a6c370060b5c4d1b933274e739771.md)
**Javier Iranzo-Sánchez, Javier Jorge, Pau Baquero-Arnal, J. Silvestre-Cerdà et al.** · 2021-05-17

<details>
<summary>Abstract</summary>

The cascade approach to Speech Translation (ST) is based on a pipeline that concatenates an Automatic Speech Recognition (ASR) system followed by a Machine Translation (MT) system. Nowadays, state-of-the-art ST systems are populated with deep neural networks that are conceived to work in an offline setup in which the audio input to be translated is fully available in advance. However, a streaming setup defines a completely different picture, in which an unbounded audio input gradually becomes available and at the same time the translation needs to be generated under real-time constraints. In this work, we present a state-of-the-art streaming ST system in which neural-based models integrated in the ASR and MT components are carefully adapted in terms of their training and decoding procedures in order to run under a streaming setup. In addition, a direct segmentation model that adapts the continuous ASR output to the capacity of simultaneous MT systems trained at the sentence level is introduced to guarantee low latency while preserving the translation quality of the complete ST system. The resulting ST system is thoroughly evaluated on the real-life streaming Europarl-ST benchmark to gauge the trade-off between quality and latency for each component individually as well as for the complete ST system.

</details>

### [Hardware Synthesis of State-Space Equations; Application to FPGA Implementation of Shallow and Deep Neural Networks](2105.07131.md)
**Amir-Hossein Kiamarzi, Pezhman Torabi, Reza Sameni** · 2021-05-15

<details>
<summary>Abstract</summary>

Nowadays, shallow and deep Neural Networks (NNs) have vast applications including biomedical engineering, image processing, computer vision, and speech recognition. Many researchers have developed hardware accelerators including field-programmable gate arrays (FPGAs) for implementing high-performance and energy efficient NNs. Apparently, the hardware architecture design process is specific and time-consuming for each NN. Therefore, a systematic way to design, implement and optimize NNs is highly demanded. The paper presents a systematic approach to implement state-space models in register transfer level (RTL), with special interest for NN implementation. The proposed design flow is based on the iterative nature of state-space models and the analogy between state-space formulations and finite-state machines. The method can be used in linear/nonlinear and time-varying/time-invariant systems. It can also be used to implement either intrinsically iterative systems (widely used in various domains such as signal processing, numerical analysis, computer arithmetic, and control engineering), or systems that could be rewritten in equivalent iterative forms. The implementation of recurrent NNs such as long short-term memory (LSTM) NNs, which have intrinsic state-space forms, are another major applications for this framework. As a case study, it is shown that state-space systems can be used for the systematic implementation and optimization of NNs (as nonlinear and time-varying dynamic systems). An RTL code generating software is also provided online, which simplifies the automatic generation of NNs of arbitrary size.

</details>

### [Listen with Intent: Improving Speech Recognition with Audio-to-Intent Front-End](2105.07071.md)
**Swayambhu Nath Ray, Minhua Wu, Anirudh Raju, Pegah Ghahremani et al.** · 2021-05-14

<details>
<summary>Abstract</summary>

Comprehending the overall intent of an utterance helps a listener recognize the individual words spoken. Inspired by this fact, we perform a novel study of the impact of explicitly incorporating intent representations as additional information to improve a recurrent neural network-transducer (RNN-T) based automatic speech recognition (ASR) system. An audio-to-intent (A2I) model encodes the intent of the utterance in the form of embeddings or posteriors, and these are used as auxiliary inputs for RNN-T training and inference. Experimenting with a 50k-hour far-field English speech corpus, this study shows that when running the system in non-streaming mode, where intent representation is extracted from the entire utterance and then used to bias streaming RNN-T search from the start, it provides a 5.56% relative word error rate reduction (WERR). On the other hand, a streaming system using per-frame intent posteriors as extra inputs for the RNN-T ASR system yields a 3.33% relative WERR. A further detailed analysis of the streaming system indicates that our proposed method brings especially good gain on media-playing related intents (e.g. 9.12% relative WERR on PlayMusicIntent).

</details>

### [Streaming Transformer for Hardware Efficient Voice Trigger Detection and False Trigger Mitigation](2105.06598.md)
**Vineet Garg, Wonil Chang, Siddharth Sigtia, Saurabh Adya et al.** · 2021-05-14

<details>
<summary>Abstract</summary>

We present a unified and hardware efficient architecture for two stage voice trigger detection (VTD) and false trigger mitigation (FTM) tasks. Two stage VTD systems of voice assistants can get falsely activated to audio segments acoustically similar to the trigger phrase of interest. FTM systems cancel such activations by using post trigger audio context. Traditional FTM systems rely on automatic speech recognition lattices which are computationally expensive to obtain on device. We propose a streaming transformer (TF) encoder architecture, which progressively processes incoming audio chunks and maintains audio context to perform both VTD and FTM tasks using only acoustic features. The proposed joint model yields an average 18% relative reduction in false reject rate (FRR) for the VTD task at a given false alarm rate. Moreover, our model suppresses 95% of the false triggers with an additional one second of post-trigger audio. Finally, on-device measurements show 32% reduction in runtime memory and 56% reduction in inference time compared to non-streaming version of the model.

</details>

### [Exploring CTC Based End-to-End Techniques for Myanmar Speech Recognition](2105.06253.md)
**Khin Me Me Chit, Laet Laet Lin** · 2021-05-13

<details>
<summary>Abstract</summary>

In this work, we explore a Connectionist Temporal Classification (CTC) based end-to-end Automatic Speech Recognition (ASR) model for the Myanmar language. A series of experiments is presented on the topology of the model in which the convolutional layers are added and dropped, different depths of bidirectional long short-term memory (BLSTM) layers are used and different label encoding methods are investigated. The experiments are carried out in low-resource scenarios using our recorded Myanmar speech corpus of nearly 26 hours. The best model achieves character error rate (CER) of 4.72% and syllable error rate (SER) of 12.38% on the test set.

</details>

### [Attention-based Neural Beamforming Layers for Multi-channel Speech Recognition](2105.05920.md)
**Bhargav Pulugundla, Yang Gao, Brian King, Gokce Keskin et al.** · 2021-05-12

<details>
<summary>Abstract</summary>

Attention-based beamformers have recently been shown to be effective for multi-channel speech recognition. However, they are less capable at capturing local information. In this work, we propose a 2D Conv-Attention module which combines convolution neural networks with attention for beamforming. We apply self- and cross-attention to explicitly model the correlations within and between the input channels. The end-to-end 2D Conv-Attention model is compared with a multi-head self-attention and superdirective-based neural beamformers. We train and evaluate on an in-house multi-channel dataset. The results show a relative improvement of 3.8% in WER by the proposed model over the baseline neural beamformer.

</details>

### [Stacked Acoustic-and-Textual Encoding: Integrating the Pre-trained Models into Speech Translation Encoders](2105.05752.md)
**Chen Xu, Bojie Hu, Yanyang Li, Yuhao Zhang et al.** · 2021-05-12

<details>
<summary>Abstract</summary>

Encoder pre-training is promising in end-to-end Speech Translation (ST), given the fact that speech-to-translation data is scarce. But ST encoders are not simple instances of Automatic Speech Recognition (ASR) or Machine Translation (MT) encoders. For example, we find that ASR encoders lack the global context representation, which is necessary for translation, whereas MT encoders are not designed to deal with long but locally attentive acoustic sequences. In this work, we propose a Stacked Acoustic-and-Textual Encoding (SATE) method for speech translation. Our encoder begins with processing the acoustic sequence as usual, but later behaves more like an MT encoder for a global representation of the input sequence. In this way, it is straightforward to incorporate the pre-trained models into the system. Also, we develop an adaptor module to alleviate the representation inconsistency between the pre-trained ASR encoder and MT encoder, and develop a multi-teacher knowledge distillation method to preserve the pre-training knowledge. Experimental results on the LibriSpeech En-Fr and MuST-C En-De ST tasks show that our method achieves state-of-the-art BLEU scores of 18.3 and 25.2. To our knowledge, we are the first to develop an end-to-end ST system that achieves comparable or even better BLEU performance than the cascaded ST counterpart when large-scale ASR and MT data is available.

</details>

### [StutterNet: Stuttering Detection Using Time Delay Neural Network](2105.05599.md)
**Shakeel A. Sheikh, Md Sahidullah, Fabrice Hirsch, Slim Ouni** · 2021-05-12

<details>
<summary>Abstract</summary>

This paper introduces StutterNet, a novel deep learning based stuttering detection capable of detecting and identifying various types of disfluencies. Most of the existing work in this domain uses automatic speech recognition (ASR) combined with language models for stuttering detection. Compared to the existing work, which depends on the ASR module, our method relies solely on the acoustic signal. We use a time-delay neural network (TDNN) suitable for capturing contextual aspects of the disfluent utterances. We evaluate our system on the UCLASS stuttering dataset consisting of more than 100 speakers. Our method achieves promising results and outperforms the state-of-the-art residual neural network based method. The number of trainable parameters of the proposed method is also substantially less due to the parameter sharing scheme of TDNN.

</details>

### [Optical neuromorphic processing at Tera-OP/s speeds based on Kerr soliton crystal microcombs](2105.06296.md)
**Mengxi Tan, Xingyuan Xu, David J. Moss** · 2021-05-12

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs), inspired by biological visual cortex systems, are a powerful category of artificial neural networks that can extract the hierarchical features of raw data to greatly reduce the network parametric complexity and enhance the predicting accuracy. They are of significant interest for machine learning tasks such as computer vision, speech recognition, playing board games and medical diagnosis. Optical neural networks offer the promise of dramatically accelerating computing speed to overcome the inherent bandwidth bottleneck of electronics. Here, we demonstrate a universal optical vector convolutional accelerator operating beyond 10 TeraOPS (TOPS: operations per second), generating convolutions of images of 250,000 pixels with 8 bit resolution for 10 kernels simultaneously, enough for facial image recognition. We then use the same hardware to sequentially form a deep optical CNN with ten output neurons, achieving successful recognition of full 10 digits with 900 pixel handwritten digit images with 88% accuracy. Our results are based on simultaneously interleaving temporal, wavelength and spatial dimensions enabled by an integrated microcomb source. This approach is scalable and trainable to much more complex networks for demanding applications such as unmanned vehicle and real time video recognition.

</details>

### [Investigating the Reordering Capability in CTC-based Non-Autoregressive End-to-End Speech Translation](2105.04840.md)
**Shun-Po Chuang, Yung-Sung Chuang, Chih-Chiang Chang, Hung-yi Lee** · 2021-05-11

<details>
<summary>Abstract</summary>

We study the possibilities of building a non-autoregressive speech-to-text translation model using connectionist temporal classification (CTC), and use CTC-based automatic speech recognition as an auxiliary task to improve the performance. CTC's success on translation is counter-intuitive due to its monotonicity assumption, so we analyze its reordering capability. Kendall's tau distance is introduced as the quantitative metric, and gradient-based visualization provides an intuitive way to take a closer look into the model. Our analysis shows that transformer encoders have the ability to change the word order and points out the future research direction that worth being explored more on non-autoregressive speech translation.

</details>

### [What shall we do with an hour of data? Speech recognition for the un- and under-served languages of Common Voice](2105.04674.md)
**Francis M. Tyers, Josh Meyer** · 2021-05-10

<details>
<summary>Abstract</summary>

This technical report describes the methods and results of a three-week sprint to produce deployable speech recognition models for 31 under-served languages of the Common Voice project. We outline the preprocessing steps, hyperparameter selection, and resulting accuracy on official testing sets. In addition to this we evaluate the models on multiple tasks: closed-vocabulary speech recognition, pre-transcription, forced alignment, and key-word spotting. The following experiments use Coqui STT, a toolkit for training and deployment of neural Speech-to-Text models.

</details>

### [Speech2Slot: An End-to-End Knowledge-based Slot Filling from Speech](2105.04719.md)
**Pengwei Wang, Xin Ye, Xiaohuan Zhou, Jinghui Xie et al.** · 2021-05-10

<details>
<summary>Abstract</summary>

In contrast to conventional pipeline Spoken Language Understanding (SLU) which consists of automatic speech recognition (ASR) and natural language understanding (NLU), end-to-end SLU infers the semantic meaning directly from speech and overcomes the error propagation caused by ASR. End-to-end slot filling (SF) from speech is an essential component of end-to-end SLU, and is usually regarded as a sequence-to-sequence generation problem, heavily relied on the performance of language model of ASR. However, it is hard to generate a correct slot when the slot is out-of-vovabulary (OOV) in training data, especially when a slot is an anti-linguistic entity without grammatical rule. Inspired by object detection in computer vision that is to detect the object from an image, we consider SF as the task of slot detection from speech. In this paper, we formulate the SF task as a matching task and propose an end-to-end knowledge-based SF model, named Speech-to-Slot (Speech2Slot), to leverage knowledge to detect the boundary of a slot from the speech. We also release a large-scale dataset of Chinese speech for slot filling, containing more than 830,000 samples. The experiments show that our approach is markedly superior to the conventional pipeline SLU approach, and outperforms the state-of-the-art end-to-end SF approach with 12.51% accuracy improvement.

</details>

### [English Accent Accuracy Analysis in a State-of-the-Art Automatic Speech Recognition System](2105.05041.md)
**Guillermo Cámbara, Alex Peiró-Lilja, Mireia Farrús, Jordi Luque** · 2021-05-09

<details>
<summary>Abstract</summary>

Nowadays, research in speech technologies has gotten a lot out thanks to recently created public domain corpora that contain thousands of recording hours. These large amounts of data are very helpful for training the new complex models based on deep learning technologies. However, the lack of dialectal diversity in a corpus is known to cause performance biases in speech systems, mainly for underrepresented dialects. In this work, we propose to evaluate a state-of-the-art automatic speech recognition (ASR) deep learning-based model, using unseen data from a corpus with a wide variety of labeled English accents from different countries around the world. The model has been trained with 44.5K hours of English speech from an open access corpus called Multilingual LibriSpeech, showing remarkable results in popular benchmarks. We test the accuracy of such ASR against samples extracted from another public corpus that is continuously growing, the Common Voice dataset. Then, we present graphically the accuracy in terms of Word Error Rate of each of the different English included accents, showing that there is indeed an accuracy bias in terms of accentual variety, favoring the accents most prevalent in the training corpus.

</details>

### [FastCorrect: Fast Error Correction with Edit Alignment for Automatic Speech Recognition](2105.03842.md)
**Yichong Leng, Xu Tan, Linchen Zhu, Jin Xu et al.** · 2021-05-09

<details>
<summary>Abstract</summary>

Error correction techniques have been used to refine the output sentences from automatic speech recognition (ASR) models and achieve a lower word error rate (WER) than original ASR outputs. Previous works usually use a sequence-to-sequence model to correct an ASR output sentence autoregressively, which causes large latency and cannot be deployed in online ASR services. A straightforward solution to reduce latency, inspired by non-autoregressive (NAR) neural machine translation, is to use an NAR sequence generation model for ASR error correction, which, however, comes at the cost of significantly increased ASR error rate. In this paper, observing distinctive error patterns and correction operations (i.e., insertion, deletion, and substitution) in ASR, we propose FastCorrect, a novel NAR error correction model based on edit alignment. In training, FastCorrect aligns each source token from an ASR output sentence to the target tokens from the corresponding ground-truth sentence based on the edit distance between the source and target sentences, and extracts the number of target tokens corresponding to each source token during edition/correction, which is then used to train a length predictor and to adjust the source tokens to match the length of the target sentence for parallel generation. In inference, the token number predicted by the length predictor is used to adjust the source tokens for target sequence generation. Experiments on the public AISHELL-1 dataset and an internal industrial-scale ASR dataset show the effectiveness of FastCorrect for ASR error correction: 1) it speeds up the inference by 6-9 times and maintains the accuracy (8-14% WER reduction) compared with the autoregressive correction model; and 2) it outperforms the popular NAR models adopted in neural machine translation and text edition by a large margin.

</details>

### [End-to-End Optical Character Recognition for Bengali Handwritten Words](2105.04020.md)
**Farisa Benta Safir, Abu Quwsar Ohi, M. F. Mridha, Muhammad Mostafa Monowar et al.** · 2021-05-09

<details>
<summary>Abstract</summary>

Optical character recognition (OCR) is a process of converting analogue documents into digital using document images. Currently, many commercial and non-commercial OCR systems exist for both handwritten and printed copies for different languages. Despite this, very few works are available in case of recognising Bengali words. Among them, most of the works focused on OCR of printed Bengali characters. This paper introduces an end-to-end OCR system for Bengali language. The proposed architecture implements an end to end strategy that recognises handwritten Bengali words from handwritten word images. We experiment with popular convolutional neural network (CNN) architectures, including DenseNet, Xception, NASNet, and MobileNet to build the OCR architecture. Further, we experiment with two different recurrent neural networks (RNN) methods, LSTM and GRU. We evaluate the proposed architecture using BanglaWritting dataset, which is a peer-reviewed Bengali handwritten image dataset. The proposed method achieves 0.091 character error rate and 0.273 word error rate performed using DenseNet121 model with GRU recurrent layer.

</details>

### [Robustness of end-to-end Automatic Speech Recognition Models -- A Case Study using Mozilla DeepSpeech](2105.09742.md)
**Aashish Agarwal, Torsten Zesch** · 2021-05-08

<details>
<summary>Abstract</summary>

When evaluating the performance of automatic speech recognition models, usually word error rate within a certain dataset is used. Special care must be taken in understanding the dataset in order to report realistic performance numbers. We argue that many performance numbers reported probably underestimate the expected error rate. We conduct experiments controlling for selection bias, gender as well as overlap (between training and test data) in content, voices, and recording conditions. We find that content overlap has the biggest impact, but other factors like gender also play a role.

</details>

### [Latency-Controlled Neural Architecture Search for Streaming Speech Recognition](2105.03643.md)
**Liqiang He, Shulin Feng, Dan Su, Dong Yu** · 2021-05-08

<details>
<summary>Abstract</summary>

Neural architecture search (NAS) has attracted much attention and has been explored for automatic speech recognition (ASR). In this work, we focus on streaming ASR scenarios and propose the latency-controlled NAS for acoustic modeling. First, based on the vanilla neural architecture, normal cells are altered to causal cells to control the total latency of the architecture. Second, a revised operation space with a smaller receptive field is proposed to generate the final architecture with low latency. Extensive experiments show that: 1) Based on the proposed neural architecture, the neural networks with a medium latency of 550ms (millisecond) and a low latency of 190ms can be learned in the vanilla and revised operation space respectively. 2) For the low latency setting, the evaluation network can achieve more than 19\% (average on the four test sets) relative improvements compared with the hybrid CLDNN baseline, on a 10k-hour large-scale dataset.

</details>

### [Energy-Efficient AI over a Virtualized Cloud Fog Network](2105.03221.md)
**Barzan A. Yosuf, Sanaa H. Mohamed, Mohamed Alenazi, Taisir E. H. El-Gorashi et al.** · 2021-05-07

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) have served as a catalyst in introducing a plethora of next-generation services in the era of Internet of Things (IoT), thanks to the availability of massive amounts of data collected by the objects on the edge. Currently, DNN models are used to deliver many Artificial Intelligence (AI) services that include image and natural language processing, speech recognition, and robotics. Accordingly, such services utilize various DNN models that make it computationally intensive for deployment on the edge devices alone. Thus, most AI models are offloaded to distant cloud data centers (CDCs), which tend to consolidate large amounts of computing and storage resources into one or more CDCs. Deploying services in the CDC will inevitably lead to excessive latencies and overall increase in power consumption. Instead, fog computing allows for cloud services to be extended to the edge of the network, which allows for data processing to be performed closer to the end-user device. However, different from cloud data centers, fog nodes have limited computational power and are highly distributed in the network. In this paper, using Mixed Integer Linear Programming (MILP), we formulate the placement of DNN inference models, which is abstracted as a network embedding problem in a Cloud Fog Network (CFN) architecture, where power savings are introduced through trade-offs between processing and networking. We study the performance of the CFN architecture by comparing the energy savings when compared to the baseline approach which is the CDC.

</details>

### [SpeechMoE: Scaling to Large Acoustic Models with Dynamic Routing Mixture of Experts](2105.03036.md)
**Zhao You, Shulin Feng, Dan Su, Dong Yu** · 2021-05-07

<details>
<summary>Abstract</summary>

Recently, Mixture of Experts (MoE) based Transformer has shown promising results in many domains. This is largely due to the following advantages of this architecture: firstly, MoE based Transformer can increase model capacity without computational cost increasing both at training and inference time. Besides, MoE based Transformer is a dynamic network which can adapt to the varying complexity of input instances in realworld applications. In this work, we explore the MoE based model for speech recognition, named SpeechMoE. To further control the sparsity of router activation and improve the diversity of gate values, we propose a sparsity L1 loss and a mean importance loss respectively. In addition, a new router architecture is used in SpeechMoE which can simultaneously utilize the information from a shared embedding network and the hierarchical representation of different MoE layers. Experimental results show that SpeechMoE can achieve lower character error rate (CER) with comparable computation cost than traditional static networks, providing 7.0%-23.0% relative CER improvements on four evaluation datasets.

</details>

### [Efficient Weight factorization for Multilingual Speech Recognition](2105.03010.md)
**Ngoc-Quan Pham, Tuan-Nam Nguyen, Sebastian Stueker, Alexander Waibel** · 2021-05-07

<details>
<summary>Abstract</summary>

End-to-end multilingual speech recognition involves using a single model training on a compositional speech corpus including many languages, resulting in a single neural network to handle transcribing different languages. Due to the fact that each language in the training data has different characteristics, the shared network may struggle to optimize for all various languages simultaneously. In this paper we propose a novel multilingual architecture that targets the core operation in neural networks: linear transformation functions. The key idea of the method is to assign fast weight matrices for each language by decomposing each weight matrix into a shared component and a language dependent component. The latter is then factorized into vectors using rank-1 assumptions to reduce the number of parameters per language. This efficient factorization scheme is proved to be effective in two multilingual settings with $7$ and $27$ languages, reducing the word error rates by $26\%$ and $27\%$ rel. for two popular architectures LSTM and Transformer, respectively.

</details>

### [Learning Shared Semantic Space for Speech-to-Text Translation](2105.03095.md)
**Chi Han, Mingxuan Wang, Heng Ji, Lei Li** · 2021-05-07

<details>
<summary>Abstract</summary>

Having numerous potential applications and great impact, end-to-end speech translation (ST) has long been treated as an independent task, failing to fully draw strength from the rapid advances of its sibling - text machine translation (MT). With text and audio inputs represented differently, the modality gap has rendered MT data and its end-to-end models incompatible with their ST counterparts. In observation of this obstacle, we propose to bridge this representation gap with Chimera. By projecting audio and text features to a common semantic representation, Chimera unifies MT and ST tasks and boosts the performance on ST benchmarks, MuST-C and Augmented Librispeech, to a new state-of-the-art. Specifically, Chimera obtains 27.1 BLEU on MuST-C EN-DE, improving the SOTA by a +1.9 BLEU margin. Further experimental analyses demonstrate that the shared semantic space indeed conveys common knowledge between these two tasks and thus paves a new way for augmenting training resources across modalities. Code, data, and resources are available at https://github.com/Glaciohound/Chimera-ST.

</details>

### [Challenges and Obstacles Towards Deploying Deep Learning Models on Mobile Devices](2105.02613.md)
**Hamid Tabani, Ajay Balasubramaniam, Elahe Arani, Bahram Zonooz** · 2021-05-06

<details>
<summary>Abstract</summary>

From computer vision and speech recognition to forecasting trajectories in autonomous vehicles, deep learning approaches are at the forefront of so many domains. Deep learning models are developed using plethora of high-level, generic frameworks and libraries. Running those models on the mobile devices require hardware-aware optimizations and in most cases converting the models to other formats or using a third-party framework. In reality, most of the developed models need to undergo a process of conversion, adaptation, and, in some cases, full retraining to match the requirements and features of the framework that is deploying the model on the target platform. Variety of hardware platforms with heterogeneous computing elements, from wearable devices to high-performance GPU clusters are used to run deep learning models. In this paper, we present the existing challenges, obstacles, and practical solutions towards deploying deep learning models on mobile devices.

</details>

### [Reducing Streaming ASR Model Delay with Self Alignment](2105.05005.md)
**Jaeyoung Kim, Han Lu, Anshuman Tripathi, Qian Zhang et al.** · 2021-05-06

<details>
<summary>Abstract</summary>

Reducing prediction delay for streaming end-to-end ASR models with minimal performance regression is a challenging problem. Constrained alignment is a well-known existing approach that penalizes predicted word boundaries using external low-latency acoustic models. On the contrary, recently proposed FastEmit is a sequence-level delay regularization scheme encouraging vocabulary tokens over blanks without any reference alignments. Although all these schemes are successful in reducing delay, ASR word error rate (WER) often severely degrades after applying these delay constraining schemes. In this paper, we propose a novel delay constraining method, named self alignment. Self alignment does not require external alignment models. Instead, it utilizes Viterbi forced-alignments from the trained model to find the lower latency alignment direction. From LibriSpeech evaluation, self alignment outperformed existing schemes: 25% and 56% less delay compared to FastEmit and constrained alignment at the similar word error rate. For Voice Search evaluation,12% and 25% delay reductions were achieved compared to FastEmit and constrained alignment with more than 2% WER improvements.

</details>

### [Accent Recognition with Hybrid Phonetic Features](2105.01920.md)
**Zhan Zhang, Xi Chen, Yuehai Wang, Jianyi Yang** · 2021-05-05

<details>
<summary>Abstract</summary>

The performance of voice-controlled systems is usually influenced by accented speech. To make these systems more robust, the frontend accent recognition (AR) technologies have received increased attention in recent years. As accent is a high-level abstract feature that has a profound relationship with the language knowledge, AR is more challenging than other language-agnostic audio classification tasks. In this paper, we use an auxiliary automatic speech recognition (ASR) task to extract language-related phonetic features. Furthermore, we propose a hybrid structure that incorporates the embeddings of both a fixed acoustic model and a trainable acoustic model, making the language-related acoustic feature more robust. We conduct several experiments on the Accented English Speech Recognition Challenge (AESRC) 2020 dataset. The results demonstrate that our approach can obtain a 6.57% relative improvement on the validation set. We also get a 7.28% relative improvement on the final test set for this competition, showing the merits of the proposed method.

</details>

### [Performance Evaluation of Deep Convolutional Maxout Neural Network in Speech Recognition](2105.01399.md)
**Arash Dehghani, Seyyed Ali Seyyedsalehi** · 2021-05-04

<details>
<summary>Abstract</summary>

In this paper, various structures and methods of Deep Artificial Neural Networks (DNN) will be evaluated and compared for the purpose of continuous Persian speech recognition. One of the first models of neural networks used in speech recognition applications were fully connected Neural Networks (FCNNs) and, consequently, Deep Neural Networks (DNNs). Although these models have better performance compared to GMM / HMM models, they do not have the proper structure to model local speech information. Convolutional Neural Network (CNN) is a good option for modeling the local structure of biological signals, including speech signals. Another issue that Deep Artificial Neural Networks face, is the convergence of networks on training data. The main inhibitor of convergence is the presence of local minima in the process of training. Deep Neural Network Pre-training methods, despite a large amount of computing, are powerful tools for crossing the local minima. But the use of appropriate neuronal models in the network structure seems to be a better solution to this problem. The Rectified Linear Unit neuronal model and the Maxout model are the most suitable neuronal models presented to this date. Several experiments were carried out to evaluate the performance of the methods and structures mentioned. After verifying the proper functioning of these methods, a combination of all models was implemented on FARSDAT speech database for continuous speech recognition. The results obtained from the experiments show that the combined model (CMDNN) improves the performance of ANNs in speech recognition versus the pre-trained fully connected NNs with sigmoid neurons by about 3%.

</details>

### [Streaming end-to-end speech recognition with jointly trained neural feature enhancement](2105.01254.md)
**Chanwoo Kim, Abhinav Garg, Dhananjaya Gowda, Seongkyu Mun et al.** · 2021-05-04

<details>
<summary>Abstract</summary>

In this paper, we present a streaming end-to-end speech recognition model based on Monotonic Chunkwise Attention (MoCha) jointly trained with enhancement layers. Even though the MoCha attention enables streaming speech recognition with recognition accuracy comparable to a full attention-based approach, training this model is sensitive to various factors such as the difficulty of training examples, hyper-parameters, and so on. Because of these issues, speech recognition accuracy of a MoCha-based model for clean speech drops significantly when a multi-style training approach is applied. Inspired by Curriculum Learning [1], we introduce two training strategies: Gradual Application of Enhanced Features (GAEF) and Gradual Reduction of Enhanced Loss (GREL). With GAEF, the model is initially trained using clean features. Subsequently, the portion of outputs from the enhancement layers gradually increases. With GREL, the portion of the Mean Squared Error (MSE) loss for the enhanced output gradually reduces as training proceeds. In experimental results on the LibriSpeech corpus and noisy far-field test sets, the proposed model with GAEF-GREL training strategies shows significantly better results than the conventional multi-style training approach.

</details>

### [Quantifying and Maximizing the Benefits of Back-End Noise Adaption on Attention-Based Speech Recognition Models](2105.01134.md)
**Coleman Hooper, Thierry Tambe, Gu-Yeon Wei** · 2021-05-03

<details>
<summary>Abstract</summary>

This work analyzes how attention-based Bidirectional Long Short-Term Memory (BLSTM) models adapt to noise-augmented speech. We identify crucial components for noise adaptation in BLSTM models by freezing model components during fine-tuning. We first freeze larger model subnetworks and then pursue a fine-grained freezing approach in the encoder after identifying its importance for noise adaptation. The first encoder layer is shown to be crucial for noise adaptation, and the weights are shown to be more important than the other layers. Appreciable accuracy benefits are identified when fine-tuning on a target noisy environment from a model pretrained with noisy speech relative to fine-tuning from a model pretrained with only clean speech when tested on the target noisy environment. For this analysis, we produce our own dataset augmentation tool and it is open-sourced to encourage future efforts in exploring noise adaptation in ASR.

</details>

### [On the limit of English conversational speech recognition](2105.00982.md)
**Zoltán Tüske, George Saon, Brian Kingsbury** · 2021-05-03

<details>
<summary>Abstract</summary>

In our previous work we demonstrated that a single headed attention encoder-decoder model is able to reach state-of-the-art results in conversational speech recognition. In this paper, we further improve the results for both Switchboard 300 and 2000. Through use of an improved optimizer, speaker vector embeddings, and alternative speech representations we reduce the recognition errors of our LSTM system on Switchboard-300 by 4% relative. Compensation of the decoder model with the probability ratio approach allows more efficient integration of an external language model, and we report 5.9% and 11.5% WER on the SWB and CHM parts of Hub5'00 with very simple LSTM models. Our study also considers the recently proposed conformer, and more advanced self-attention based language models. Overall, the conformer shows similar performance to the LSTM; nevertheless, their combination and decoding with an improved LM reaches a new record on Switchboard-300, 5.0% and 10.0% WER on SWB and CHM. Our findings are also confirmed on Switchboard-2000, and a new state of the art is reported, practically reaching the limit of the benchmark.

</details>

### [Searchable Hidden Intermediates for End-to-End Models of Decomposable Sequence Tasks](2105.00573.md)
**Siddharth Dalmia, Brian Yan, Vikas Raunak, Florian Metze et al.** · 2021-05-02

<details>
<summary>Abstract</summary>

End-to-end approaches for sequence tasks are becoming increasingly popular. Yet for complex sequence tasks, like speech translation, systems that cascade several models trained on sub-tasks have shown to be superior, suggesting that the compositionality of cascaded systems simplifies learning and enables sophisticated search capabilities. In this work, we present an end-to-end framework that exploits compositionality to learn searchable hidden representations at intermediate stages of a sequence model using decomposed sub-tasks. These hidden intermediates can be improved using beam search to enhance the overall performance and can also incorporate external models at intermediate stages of the network to re-score or adapt towards out-of-domain data. One instance of the proposed framework is a Multi-Decoder model for speech translation that extracts the searchable hidden intermediates from a speech recognition sub-task. The model demonstrates the aforementioned benefits and outperforms the previous state-of-the-art by around +6 and +3 BLEU on the two test sets of Fisher-CallHome and by around +3 and +4 BLEU on the English-German and English-French test sets of MuST-C.

</details>

### [Deformable TDNN with adaptive receptive fields for speech recognition](2104.14791.md)
**Keyu An, Yi Zhang, Zhijian Ou** · 2021-04-30

<details>
<summary>Abstract</summary>

Time Delay Neural Networks (TDNNs) are widely used in both DNN-HMM based hybrid speech recognition systems and recent end-to-end systems. Nevertheless, the receptive fields of TDNNs are limited and fixed, which is not desirable for tasks like speech recognition, where the temporal dynamics of speech are varied and affected by many factors. This paper proposes to use deformable TDNNs for adaptive temporal dynamics modeling in end-to-end speech recognition. Inspired by deformable ConvNets, deformable TDNNs augment the temporal sampling locations with additional offsets and learn the offsets automatically based on the ASR criterion, without additional supervision. Experiments show that deformable TDNNs obtain state-of-the-art results on WSJ benchmarks (1.42\%/3.45\% WER on WSJ eval92/dev93 respectively), outperforming standard TDNNs significantly. Furthermore, we propose the latency control mechanism for deformable TDNNs, which enables deformable TDNNs to do streaming ASR without accuracy degradation.

</details>

### [Scaling End-to-End Models for Large-Scale Multilingual ASR](2104.14830.md)
**Bo Li, Ruoming Pang, Tara N. Sainath, Anmol Gulati et al.** · 2021-04-30

<details>
<summary>Abstract</summary>

Building ASR models across many languages is a challenging multi-task learning problem due to large variations and heavily unbalanced data. Existing work has shown positive transfer from high resource to low resource languages. However, degradations on high resource languages are commonly observed due to interference from the heterogeneous multilingual data and reduction in per-language capacity. We conduct a capacity study on a 15-language task, with the amount of data per language varying from 7.6K to 53.5K hours. We adopt GShard [1] to efficiently scale up to 10B parameters. Empirically, we find that (1) scaling the number of model parameters is an effective way to solve the capacity bottleneck - our 500M-param model already outperforms monolingual baselines and scaling it to 1B and 10B brought further quality gains; (2) larger models are not only more data efficient, but also more efficient in terms of training cost as measured in TPU days - the 1B-param model reaches the same accuracy at 34% of training time as the 500M-param model; (3) given a fixed capacity budget, adding depth works better than width and large encoders do better than large decoders; (4) with continuous training, they can be adapted to new languages and domains.

</details>

### [Speech Vision: An End-to-End Deep Learning-Based Dysarthric Automatic Speech Recognition System](s2:bc1b1caeafc1181bf8d8557eb7388b55e3e5a0b1.md)
**S. R. Shahamiri** · 2021-04-30

<details>
<summary>Abstract</summary>

Dysarthria is a disorder that affects an individual’s speech intelligibility due to the paralysis of muscles and organs involved in the articulation process. As the condition is often associated with physically debilitating disabilities, not only do such individuals face communication problems, but also interactions with digital devices can become a burden. For these individuals, automatic speech recognition (ASR) technologies can make a significant difference in their lives as computing and portable digital devices can become an interaction medium, enabling them to communicate with others and computers. However, ASR technologies have performed poorly in recognizing dysarthric speech, especially for severe dysarthria, due to multiple challenges facing dysarthric ASR systems. We identified these challenges are due to the alternation and inaccuracy of dysarthric phonemes, the scarcity of dysarthric speech data, and the phoneme labeling imprecision. This paper reports on our second dysarthric-specific ASR system, called Speech Vision (SV) that tackles these challenges by adopting a novel approach towards dysarthric ASR in which speech features are extracted visually, then SV learns to see the shape of the words pronounced by dysarthric individuals. This visual acoustic modeling feature of SV eliminates phoneme-related challenges. To address the data scarcity problem, SV adopts visual data augmentation techniques, generates synthetic dysarthric acoustic visuals, and leverages transfer learning. Benchmarking with other state-of-the-art dysarthric ASR considered in this study, SV outperformed them by improving recognition accuracies for 67% of UA-Speech speakers, where the biggest improvements were achieved for severe dysarthria.

</details>

### [Using Transformers to Provide Teachers with Personalized Feedback on their Classroom Discourse: The TalkMoves Application](2105.07949.md)
**Abhijit Suresh, Jennifer Jacobs, Vivian Lai, Chenhao Tan et al.** · 2021-04-29

<details>
<summary>Abstract</summary>

TalkMoves is an innovative application designed to support K-12 mathematics teachers to reflect on, and continuously improve their instructional practices. This application combines state-of-the-art natural language processing capabilities with automated speech recognition to automatically analyze classroom recordings and provide teachers with personalized feedback on their use of specific types of discourse aimed at broadening and deepening classroom conversations about mathematics. These specific discourse strategies are referred to as "talk moves" within the mathematics education community and prior research has documented the ways in which systematic use of these discourse strategies can positively impact student engagement and learning. In this article, we describe the TalkMoves application's cloud-based infrastructure for managing and processing classroom recordings, and its interface for providing teachers with feedback on their use of talk moves during individual teaching episodes. We present the series of model architectures we developed, and the studies we conducted, to develop our best-performing, transformer-based model (F1 = 79.3%). We also discuss several technical challenges that need to be addressed when working with real-world speech and language data from noisy K-12 classrooms.

</details>

### [End-to-End Speech Recognition from Federated Acoustic Models](2104.14297.md)
**Yan Gao, Titouan Parcollet, Salah Zaiem, Javier Fernandez-Marques et al.** · 2021-04-29

<details>
<summary>Abstract</summary>

Training Automatic Speech Recognition (ASR) models under federated learning (FL) settings has attracted a lot of attention recently. However, the FL scenarios often presented in the literature are artificial and fail to capture the complexity of real FL systems. In this paper, we construct a challenging and realistic ASR federated experimental setup consisting of clients with heterogeneous data distributions using the French and Italian sets of the CommonVoice dataset, a large heterogeneous dataset containing thousands of different speakers, acoustic environments and noises. We present the first empirical study on attention-based sequence-to-sequence End-to-End (E2E) ASR model with three aggregation weighting strategies -- standard FedAvg, loss-based aggregation and a novel word error rate (WER)-based aggregation, compared in two realistic FL scenarios: cross-silo with 10 clients and cross-device with 2K and 4K clients. Our analysis on E2E ASR from heterogeneous and realistic federated acoustic models provides the foundations for future research and development of realistic FL-based ASR applications.

</details>

### [On Addressing Practical Challenges for RNN-Transducer](2105.00858.md)
**Rui Zhao, Jian Xue, Jinyu Li, Wenning Wei et al.** · 2021-04-27

<details>
<summary>Abstract</summary>

In this paper, several works are proposed to address practical challenges for deploying RNN Transducer (RNN-T) based speech recognition system. These challenges are adapting a well-trained RNN-T model to a new domain without collecting the audio data, obtaining time stamps and confidence scores at word level. The first challenge is solved with a splicing data method which concatenates the speech segments extracted from the source domain data. To get the time stamp, a phone prediction branch is added to the RNN-T model by sharing the encoder for the purpose of force alignment. Finally, we obtain word-level confidence scores by utilizing several types of features calculated during decoding and from confusion network. Evaluated with Microsoft production data, the splicing data adaptation method improves the baseline and adaptation with the text to speech method by 58.03% and 15.25% relative word error rate reduction, respectively. The proposed time stamping method can get less than 50ms word timing difference from the ground truth alignment on average while maintaining the recognition accuracy of the RNN-T model. We also obtain high confidence annotation performance with limited computation cost.

</details>

### [Using Radio Archives for Low-Resource Speech Recognition: Towards an Intelligent Virtual Assistant for Illiterate Users](2104.13083.md)
**Moussa Doumbouya, Lisa Einstein, Chris Piech** · 2021-04-27

<details>
<summary>Abstract</summary>

For many of the 700 million illiterate people around the world, speech recognition technology could provide a bridge to valuable information and services. Yet, those most in need of this technology are often the most underserved by it. In many countries, illiterate people tend to speak only low-resource languages, for which the datasets necessary for speech technology development are scarce. In this paper, we investigate the effectiveness of unsupervised speech representation learning on noisy radio broadcasting archives, which are abundant even in low-resource languages. We make three core contributions. First, we release two datasets to the research community. The first, West African Radio Corpus, contains 142 hours of audio in more than 10 languages with a labeled validation subset. The second, West African Virtual Assistant Speech Recognition Corpus, consists of 10K labeled audio clips in four languages. Next, we share West African wav2vec, a speech encoder trained on the noisy radio corpus, and compare it with the baseline Facebook speech encoder trained on six times more data of higher quality. We show that West African wav2vec performs similarly to the baseline on a multilingual speech recognition task, and significantly outperforms the baseline on a West African language identification task. Finally, we share the first-ever speech recognition models for Maninka, Pular and Susu, languages spoken by a combined 10 million people in over seven countries, including six where the majority of the adult population is illiterate. Our contributions offer a path forward for ethical AI research to serve the needs of those most disadvantaged by the digital divide.

</details>

### [Multi-Task Learning for End-to-End ASR Word and Utterance Confidence with Deletion Prediction](2104.12870.md)
**David Qiu, Yanzhang He, Qiujia Li, Yu Zhang et al.** · 2021-04-26

<details>
<summary>Abstract</summary>

Confidence scores are very useful for downstream applications of automatic speech recognition (ASR) systems. Recent works have proposed using neural networks to learn word or utterance confidence scores for end-to-end ASR. In those studies, word confidence by itself does not model deletions, and utterance confidence does not take advantage of word-level training signals. This paper proposes to jointly learn word confidence, word deletion, and utterance confidence. Empirical results show that multi-task learning with all three objectives improves confidence metrics (NCE, AUC, RMSE) without the need for increasing the model size of the confidence estimation module. Using the utterance-level confidence for rescoring also decreases the word error rates on Google's Voice Search and Long-tail Maps datasets by 3-5% relative, without needing a dedicated neural rescorer.

</details>

### [Head-synchronous Decoding for Transformer-based Streaming ASR](2104.12631.md)
**Mohan Li, Catalin Zorila, Rama Doddipatla** · 2021-04-26

<details>
<summary>Abstract</summary>

Online Transformer-based automatic speech recognition (ASR) systems have been extensively studied due to the increasing demand for streaming applications. Recently proposed Decoder-end Adaptive Computation Steps (DACS) algorithm for online Transformer ASR was shown to achieve state-of-the-art performance and outperform other existing methods. However, like any other online approach, the DACS-based attention heads in each of the Transformer decoder layers operate independently (or asynchronously) and lead to diverged attending positions. Since DACS employs a truncation threshold to determine the halting position, some of the attention weights are cut off untimely and might impact the stability and precision of decoding. To overcome these issues, here we propose a head-synchronous (HS) version of the DACS algorithm, where the boundary of attention is jointly detected by all the DACS heads in each decoder layer. ASR experiments on Wall Street Journal (WSJ), AIShell-1 and Librispeech show that the proposed method consistently outperforms vanilla DACS and achieves state-of-the-art performance. We will also demonstrate that HS-DACS has reduced decoding cost when compared to vanilla DACS.

</details>

### [Semantic Data Augmentation for End-to-End Mandarin Speech Recognition](2104.12521.md)
**Jianwei Sun, Zhiyuan Tang, Hengxin Yin, Wei Wang et al.** · 2021-04-26

<details>
<summary>Abstract</summary>

End-to-end models have gradually become the preferred option for automatic speech recognition (ASR) applications. During the training of end-to-end ASR, data augmentation is a quite effective technique for regularizing the neural networks. This paper proposes a novel data augmentation technique based on semantic transposition of the transcriptions via syntax rules for end-to-end Mandarin ASR. Specifically, we first segment the transcriptions based on part-of-speech tags. Then transposition strategies, such as placing the object in front of the subject or swapping the subject and the object, are applied on the segmented sentences. Finally, the acoustic features corresponding to the transposed transcription are reassembled based on the audio-to-text forced-alignment produced by a pre-trained ASR system. The combination of original data and augmented one is used for training a new ASR system. The experiments are conducted on the Transformer[2] and Conformer[3] based ASR. The results show that the proposed method can give consistent performance gain to the system. Augmentation related issues, such as comparison of different strategies and ratios for data combination are also investigated.

</details>

### [Complex Neural Spatial Filter: Enhancing Multi-channel Target Speech Separation in Complex Domain](2104.12359.md)
**Rongzhi Gu, Shi-Xiong Zhang, Yuexian Zou, Dong Yu** · 2021-04-26

<details>
<summary>Abstract</summary>

To date, mainstream target speech separation (TSS) approaches are formulated to estimate the complex ratio mask (cRM) of the target speech in time-frequency domain under supervised deep learning framework. However, the existing deep models for estimating cRM are designed in the way that the real and imaginary parts of the cRM are separately modeled using real-valued training data pairs. The research motivation of this study is to design a deep model that fully exploits the temporal-spectral-spatial information of multi-channel signals for estimating cRM directly and efficiently in complex domain. As a result, a novel TSS network is designed consisting of two modules, a complex neural spatial filter (cNSF) and an MVDR. Essentially, cNSF is a cRM estimation model and an MVDR module is cascaded to the cNSF module to reduce the nonlinear speech distortions introduced by neural network. Specifically, to fit the cRM target, all input features of cNSF are reformulated into complex-valued representations following the supervised learning paradigm. Then, to achieve good hierarchical feature abstraction, a complex deep neural network (cDNN) is delicately designed with U-Net structure. Experiments conducted on simulated multi-channel speech data demonstrate the proposed cNSF outperforms the baseline NSF by 12.1% scale-invariant signal-to-distortion ratio and 33.1% word error rate.

</details>

### [Bridging the gap between streaming and non-streaming ASR systems bydistilling ensembles of CTC and RNN-T models](2104.14346.md)
**Thibault Doutre, Wei Han, Chung-Cheng Chiu, Ruoming Pang et al.** · 2021-04-25

<details>
<summary>Abstract</summary>

Streaming end-to-end automatic speech recognition (ASR) systems are widely used in everyday applications that require transcribing speech to text in real-time. Their minimal latency makes them suitable for such tasks. Unlike their non-streaming counterparts, streaming models are constrained to be causal with no future context and suffer from higher word error rates (WER). To improve streaming models, a recent study [1] proposed to distill a non-streaming teacher model on unsupervised utterances, and then train a streaming student using the teachers' predictions. However, the performance gap between teacher and student WERs remains high. In this paper, we aim to close this gap by using a diversified set of non-streaming teacher models and combining them using Recognizer Output Voting Error Reduction (ROVER). In particular, we show that, despite being weaker than RNN-T models, CTC models are remarkable teachers. Further, by fusing RNN-T and CTC models together, we build the strongest teachers. The resulting student models drastically improve upon streaming models of previous work [1]: the WER decreases by 41% on Spanish, 27% on Portuguese, and 13% on French.

</details>

### [Scalable End-to-End RF Classification: A Case Study on Undersized Dataset Regularization by Convolutional-MST](2104.12103.md)
**Khalid Youssef, Greg Schuette, Yubin Cai, Daisong Zhang et al.** · 2021-04-25

<details>
<summary>Abstract</summary>

Unlike areas such as computer vision and speech recognition where convolutional and recurrent neural networks-based approaches have proven effective to the nature of the respective areas of application, deep learning (DL) still lacks a general approach suitable for the unique nature and challenges of RF systems such as radar, signals intelligence, electronic warfare, and communications. Existing approaches face problems in robustness, consistency, efficiency, repeatability and scalability. One of the main challenges in RF sensing such as radar target identification is the difficulty and cost of obtaining data. Hundreds to thousands of samples per class are typically used when training for classifying signals into 2 to 12 classes with reported accuracy ranging from 87% to 99%, where accuracy generally decreases with more classes added. In this paper, we present a new DL approach based on multistage training and demonstrate it on RF sensing signal classification. We consistently achieve over 99% accuracy for up to 17 diverse classes using only 11 samples per class for training, yielding up to 35% improvement in accuracy over standard DL approaches.

</details>

### [Quantization of Deep Neural Networks for Accurate Edge Computing](2104.12046.md)
**Wentao Chen, Hailong Qiu, Jian Zhuang, Chutong Zhang et al.** · 2021-04-25

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have demonstrated their great potential in recent years, exceeding the per-formance of human experts in a wide range of applications. Due to their large sizes, however, compressiontechniques such as weight quantization and pruning are usually applied before they can be accommodated onthe edge. It is generally believed that quantization leads to performance degradation, and plenty of existingworks have explored quantization strategies aiming at minimum accuracy loss. In this paper, we argue thatquantization, which essentially imposes regularization on weight representations, can sometimes help toimprove accuracy. We conduct comprehensive experiments on three widely used applications: fully con-nected network (FCN) for biomedical image segmentation, convolutional neural network (CNN) for imageclassification on ImageNet, and recurrent neural network (RNN) for automatic speech recognition, and experi-mental results show that quantization can improve the accuracy by 1%, 1.95%, 4.23% on the three applicationsrespectively with 3.5x-6.4x memory reduction.

</details>

### [Language ID Prediction from Speech Using Self-Attentive Pooling and 1D-Convolutions](2104.11985.md)
**Roman Bedyakin, Nikolay Mikhaylovskiy** · 2021-04-24

<details>
<summary>Abstract</summary>

This memo describes NTR-TSU submission for SIGTYP 2021 Shared Task on predicting language IDs from speech. Spoken Language Identification (LID) is an important step in a multilingual Automated Speech Recognition (ASR) system pipeline. For many low-resource and endangered languages, only single-speaker recordings may be available, demanding a need for domain and speaker-invariant language ID systems. In this memo, we show that a convolutional neural network with a Self-Attentive Pooling layer shows promising results for the language identification task.

</details>

### [LeBenchmark: A Reproducible Framework for Assessing Self-Supervised Representation Learning from Speech](2104.11462.md)
**Solene Evain, Ha Nguyen, Hang Le, Marcely Zanon Boito et al.** · 2021-04-23

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) using huge unlabeled data has been successfully explored for image and natural language processing. Recent works also investigated SSL from speech. They were notably successful to improve performance on downstream tasks such as automatic speech recognition (ASR). While these works suggest it is possible to reduce dependence on labeled data for building efficient speech systems, their evaluation was mostly made on ASR and using multiple and heterogeneous experimental settings (most of them for English). This questions the objective comparison of SSL approaches and the evaluation of their impact on building speech systems. In this paper, we propose LeBenchmark: a reproducible framework for assessing SSL from speech. It not only includes ASR (high and low resource) tasks but also spoken language understanding, speech translation and emotion recognition. We also focus on speech technologies in a language different than English: French. SSL models of different sizes are trained from carefully sourced and documented datasets. Experiments show that SSL is beneficial for most but not all tasks which confirms the need for exhaustive and reliable benchmarks to evaluate its real impact. LeBenchmark is shared with the scientific community for reproducible research in SSL from speech.

</details>

### [Fast Text-Only Domain Adaptation of RNN-Transducer Prediction Network](2104.11127.md)
**Janne Pylkkönen, Antti Ukkonen, Juho Kilpikoski, Samu Tamminen et al.** · 2021-04-22

<details>
<summary>Abstract</summary>

Adaption of end-to-end speech recognition systems to new tasks is known to be challenging. A number of solutions have been proposed which apply external language models with various fusion methods, possibly with a combination of two-pass decoding. Also TTS systems have been used to generate adaptation data for the end-to-end models. In this paper we show that RNN-transducer models can be effectively adapted to new domains using only small amounts of textual data. By taking advantage of model's inherent structure, where the prediction network is interpreted as a language model, we can apply fast adaptation to the model. Adapting the model avoids the need for complicated decoding time fusions and external language models. Using appropriate regularization, the prediction network can be adapted to new domains while still retaining good generalization capabilities. We show with multiple ASR evaluation tasks how this method can provide relative gains of 10-45% in target task WER. We also share insights how RNN-transducer prediction network performs as a language model.

</details>

### [Scene-aware Far-field Automatic Speech Recognition](2104.10757.md)
**Zhenyu Tang, Dinesh Manocha** · 2021-04-21

<details>
<summary>Abstract</summary>

We propose a novel method for generating scene-aware training data for far-field automatic speech recognition. We use a deep learning-based estimator to non-intrusively compute the sub-band reverberation time of an environment from its speech samples. We model the acoustic characteristics of a scene with its reverberation time and represent it using a multivariate Gaussian distribution. We use this distribution to select acoustic impulse responses from a large real-world dataset for augmenting speech data. The speech recognition system trained on our scene-aware data consistently outperforms the system trained using many more random acoustic impulse responses on the REVERB and the AMI far-field benchmarks. In practice, we obtain 2.64% absolute improvement in word error rate compared with using training data of the same size with uniformly distributed reverberation times.

</details>

### [On Sampling-Based Training Criteria for Neural Language Modeling](2104.10507.md)
**Yingbo Gao, David Thulke, Alexander Gerstenberger, Khoa Viet Tran et al.** · 2021-04-21

<details>
<summary>Abstract</summary>

As the vocabulary size of modern word-based language models becomes ever larger, many sampling-based training criteria are proposed and investigated. The essence of these sampling methods is that the softmax-related traversal over the entire vocabulary can be simplified, giving speedups compared to the baseline. A problem we notice about the current landscape of such sampling methods is the lack of a systematic comparison and some myths about preferring one over another. In this work, we consider Monte Carlo sampling, importance sampling, a novel method we call compensated partial summation, and noise contrastive estimation. Linking back to the three traditional criteria, namely mean squared error, binary cross-entropy, and cross-entropy, we derive the theoretical solutions to the training problems. Contrary to some common belief, we show that all these sampling methods can perform equally well, as long as we correct for the intended class posterior probabilities. Experimental results in language modeling and automatic speech recognition on Switchboard and LibriSpeech support our claim, with all sampling-based methods showing similar perplexities and word error rates while giving the expected speedups.

</details>

### [Pre-training for Spoken Language Understanding with Joint Textual and Phonetic Representation Learning](2104.10357.md)
**Qian Chen, Wen Wang, Qinglin Zhang** · 2021-04-21

<details>
<summary>Abstract</summary>

In the traditional cascading architecture for spoken language understanding (SLU), it has been observed that automatic speech recognition errors could be detrimental to the performance of natural language understanding. End-to-end (E2E) SLU models have been proposed to directly map speech input to desired semantic frame with a single model, hence mitigating ASR error propagation. Recently, pre-training technologies have been explored for these E2E models. In this paper, we propose a novel joint textual-phonetic pre-training approach for learning spoken language representations, aiming at exploring the full potentials of phonetic information to improve SLU robustness to ASR errors. We explore phoneme labels as high-level speech features, and design and compare pre-training tasks based on conditional masked language model objectives and inter-sentence relation objectives. We also investigate the efficacy of combining textual and phonetic information during fine-tuning. Experimental results on spoken language understanding benchmarks, Fluent Speech Commands and SNIPS, show that the proposed approach significantly outperforms strong baseline models and improves robustness of spoken language understanding to ASR errors.

</details>

### [Label-Synchronous Speech-to-Text Alignment for ASR Using Forward and Backward Transformers](2104.10328.md)
**Yusuke Kida, Tatsuya Komatsu, Masahito Togami** · 2021-04-21

<details>
<summary>Abstract</summary>

This paper proposes a novel label-synchronous speech-to-text alignment technique for automatic speech recognition (ASR). The speech-to-text alignment is a problem of splitting long audio recordings with un-aligned transcripts into utterance-wise pairs of speech and text. Unlike conventional methods based on frame-synchronous prediction, the proposed method re-defines the speech-to-text alignment as a label-synchronous text mapping problem. This enables an accurate alignment benefiting from the strong inference ability of the state-of-the-art attention-based encoder-decoder models, which cannot be applied to the conventional methods. Two different Transformer models named forward Transformer and backward Transformer are respectively used for estimating an initial and final tokens of a given speech segment based on end-of-sentence prediction with teacher-forcing. Experiments using the corpus of spontaneous Japanese (CSJ) demonstrate that the proposed method provides an accurate utterance-wise alignment, that matches the manually annotated alignment with as few as 0.2% errors. It is also confirmed that a Transformer-based hybrid CTC/Attention ASR model using the aligned speech and text pairs as an additional training data reduces character error rates relatively up to 59.0%, which is significantly better than 39.0% reduction by a conventional alignment method based on connectionist temporal classification model.

</details>

### [End-to-end Speech Translation via Cross-modal Progressive Training](2104.10380.md)
**Rong Ye, Mingxuan Wang, Lei Li** · 2021-04-21

<details>
<summary>Abstract</summary>

End-to-end speech translation models have become a new trend in research due to their potential of reducing error propagation. However, these models still suffer from the challenge of data scarcity. How to effectively use unlabeled or other parallel corpora from machine translation is promising but still an open problem. In this paper, we propose Cross Speech-Text Network (XSTNet), an end-to-end model for speech-to-text translation. XSTNet takes both speech and text as input and outputs both transcription and translation text. The model benefits from its three key design aspects: a self-supervised pre-trained sub-network as the audio encoder, a multi-task training objective to exploit additional parallel bilingual text, and a progressive training procedure. We evaluate the performance of XSTNet and baselines on the MuST-C En-X and LibriSpeech En-Fr datasets. In particular, XSTNet achieves state-of-the-art results on all language directions with an average BLEU of 28.8, outperforming the previous best method by 3.2 BLEU. Code, models, cases, and more detailed analysis are available at https://github.com/ReneeYe/XSTNet.

</details>

### [Fusing information streams in end-to-end audio-visual speech recognition](2104.09482.md)
**Wentao Yu, Steffen Zeiler, Dorothea Kolossa** · 2021-04-19

<details>
<summary>Abstract</summary>

End-to-end acoustic speech recognition has quickly gained widespread popularity and shows promising results in many studies. Specifically the joint transformer/CTC model provides very good performance in many tasks. However, under noisy and distorted conditions, the performance still degrades notably. While audio-visual speech recognition can significantly improve the recognition rate of end-to-end models in such poor conditions, it is not obvious how to best utilize any available information on acoustic and visual signal quality and reliability in these models. We thus consider the question of how to optimally inform the transformer/CTC model of any time-variant reliability of the acoustic and visual information streams. We propose a new fusion strategy, incorporating reliability information in a decision fusion net that considers the temporal effects of the attention mechanism. This approach yields significant improvements compared to a state-of-the-art baseline model on the Lip Reading Sentences 2 and 3 (LRS2 and LRS3) corpus. On average, the new system achieves a relative word error rate reduction of 43% compared to the audio-only setup and 31% compared to the audiovisual end-to-end baseline.

</details>

### [Advanced Long-context End-to-end Speech Recognition Using Context-expanded Transformers](2104.09426.md)
**Takaaki Hori, Niko Moritz, Chiori Hori, Jonathan Le Roux** · 2021-04-19

<details>
<summary>Abstract</summary>

This paper addresses end-to-end automatic speech recognition (ASR) for long audio recordings such as lecture and conversational speeches. Most end-to-end ASR models are designed to recognize independent utterances, but contextual information (e.g., speaker or topic) over multiple utterances is known to be useful for ASR. In our prior work, we proposed a context-expanded Transformer that accepts multiple consecutive utterances at the same time and predicts an output sequence for the last utterance, achieving 5-15% relative error reduction from utterance-based baselines in lecture and conversational ASR benchmarks. Although the results have shown remarkable performance gain, there is still potential to further improve the model architecture and the decoding process. In this paper, we extend our prior work by (1) introducing the Conformer architecture to further improve the accuracy, (2) accelerating the decoding process with a novel activation recycling technique, and (3) enabling streaming decoding with triggered attention. We demonstrate that the extended Transformer provides state-of-the-art end-to-end ASR performance, obtaining a 17.3% character error rate for the HKUST dataset and 12.0%/6.3% word error rates for the Switchboard-300 Eval2000 CallHome/Switchboard test sets. The new decoding method reduces decoding time by more than 50% and further enables streaming ASR with limited accuracy degradation.

</details>

### [Learning on Hardware: A Tutorial on Neural Network Accelerators and Co-Processors](2104.09252.md)
**Lukas Baischer, Matthias Wess, Nima TaheriNejad** · 2021-04-19

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have the advantage that they can take into account a large number of parameters, which enables them to solve complex tasks. In computer vision and speech recognition, they have a better accuracy than common algorithms, and in some tasks, they boast an even higher accuracy than human experts. With the progress of DNNs in recent years, many other fields of application such as diagnosis of diseases and autonomous driving are taking advantage of them. The trend at DNNs is clear: The network size is growing exponentially, which leads to an exponential increase in computational effort and required memory size. For this reason, optimized hardware accelerators are used to increase the performance of the inference of neuronal networks. However, there are various neural network hardware accelerator platforms, such as graphics processing units (GPUs), application specific integrated circuits (ASICs) and field programmable gate arrays (FPGAs). Each of these platforms offer certain advantages and disadvantages. Also, there are various methods for reducing the computational effort of DNNs, which are differently suitable for each hardware accelerator. In this article an overview of existing neural network hardware accelerators and acceleration methods is given. Their strengths and weaknesses are shown and a recommendation of suitable applications is given. In particular, we focus on acceleration of the inference of convolutional neural networks (CNNs) used for image recognition tasks. Given that there exist many different hardware architectures. FPGA-based implementations are well-suited to show the effect of DNN optimization methods on accuracy and throughput. For this reason, the focus of this work is more on FPGA-based implementations.

</details>

### [Acoustic Data-Driven Subword Modeling for End-to-End Speech Recognition](2104.09106.md)
**Wei Zhou, Mohammad Zeineldeen, Zuoyun Zheng, Ralf Schlüter et al.** · 2021-04-19

<details>
<summary>Abstract</summary>

Subword units are commonly used for end-to-end automatic speech recognition (ASR), while a fully acoustic-oriented subword modeling approach is somewhat missing. We propose an acoustic data-driven subword modeling (ADSM) approach that adapts the advantages of several text-based and acoustic-based subword methods into one pipeline. With a fully acoustic-oriented label design and learning process, ADSM produces acoustic-structured subword units and acoustic-matched target sequence for further ASR training. The obtained ADSM labels are evaluated with different end-to-end ASR approaches including CTC, RNN-Transducer and attention models. Experiments on the LibriSpeech corpus show that ADSM clearly outperforms both byte pair encoding (BPE) and pronunciation-assisted subword modeling (PASM) in all cases. Detailed analysis shows that ADSM achieves acoustically more logical word segmentation and more balanced sequence length, and thus, is suitable for both time-synchronous and label-synchronous models. We also briefly describe how to apply acoustic-based subword regularization and unseen text segmentation using ADSM.

</details>

### [MIMO Self-attentive RNN Beamformer for Multi-speaker Speech Separation](2104.08450.md)
**Xiyun Li, Yong Xu, Meng Yu, Shi-Xiong Zhang et al.** · 2021-04-17

<details>
<summary>Abstract</summary>

Recently, our proposed recurrent neural network (RNN) based all deep learning minimum variance distortionless response (ADL-MVDR) beamformer method yielded superior performance over the conventional MVDR by replacing the matrix inversion and eigenvalue decomposition with two recurrent neural networks. In this work, we present a self-attentive RNN beamformer to further improve our previous RNN-based beamformer by leveraging on the powerful modeling capability of self-attention. Temporal-spatial self-attention module is proposed to better learn the beamforming weights from the speech and noise spatial covariance matrices. The temporal self-attention module could help RNN to learn global statistics of covariance matrices. The spatial self-attention module is designed to attend on the cross-channel correlation in the covariance matrices. Furthermore, a multi-channel input with multi-speaker directional features and multi-speaker speech separation outputs (MIMO) model is developed to improve the inference efficiency. The evaluations demonstrate that our proposed MIMO self-attentive RNN beamformer improves both the automatic speech recognition (ASR) accuracy and the perceptual estimation of speech quality (PESQ) against prior arts.

</details>

### [Efficient Keyword Spotting by capturing long-range interactions with Temporal Lambda Networks](2104.08086.md)
**Biel Tura, Santiago Escuder, Ferran Diego, Carlos Segura et al.** · 2021-04-16

<details>
<summary>Abstract</summary>

Models based on attention mechanisms have shown unprecedented speech recognition performance. However, they are computationally expensive and unnecessarily complex for keyword spotting, a task targeted to small-footprint devices. This work explores the application of Lambda networks, an alternative framework for capturing long-range interactions without attention, for the keyword spotting task. We propose a novel \textit{ResNet}-based model by swapping the residual blocks by temporal Lambda layers. Furthermore, the proposed architecture is built upon uni-dimensional temporal convolutions that further reduce its complexity. The presented model does not only reach state-of-the-art accuracies on the Google Speech Commands dataset, but it is 85% and 65% lighter than its Transformer-based (KWT) and convolutional (Res15) counterparts while being up to 100 times faster. To the best of our knowledge, this is the first attempt to explore the Lambda framework within the speech domain and therefore, we unravel further research of new interfaces based on this architecture.

</details>

### [Efficient and Generic 1D Dilated Convolution Layer for Deep Learning](2104.08002.md)
**Narendra Chaudhary, Sanchit Misra, Dhiraj Kalamkar, Alexander Heinecke et al.** · 2021-04-16

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs) have found many applications in tasks involving two-dimensional (2D) data, such as image classification and image processing. Therefore, 2D convolution layers have been heavily optimized on CPUs and GPUs. However, in many applications - for example genomics and speech recognition, the data can be one-dimensional (1D). Such applications can benefit from optimized 1D convolution layers. In this work, we introduce our efficient implementation of a generic 1D convolution layer covering a wide range of parameters. It is optimized for x86 CPU architectures, in particular, for architectures containing Intel AVX-512 and AVX-512 BFloat16 instructions. We use the LIBXSMM library's batch-reduce General Matrix Multiplication (BRGEMM) kernel for FP32 and BFloat16 precision. We demonstrate that our implementation can achieve up to 80% efficiency on Intel Xeon Cascade Lake and Cooper Lake CPUs. Additionally, we show the generalization capability of our BRGEMM based approach by achieving high efficiency across a range of parameters. We consistently achieve higher efficiency than the 1D convolution layer with Intel oneDNN library backend for varying input tensor widths, filter widths, number of channels, filters, and dilation parameters. Finally, we demonstrate the performance of our optimized 1D convolution layer by utilizing it in the end-to-end neural network training with real genomics datasets and achieve up to 6.86x speedup over the oneDNN library-based implementation on Cascade Lake CPUs. We also demonstrate the scaling with 16 sockets of Cascade/Cooper Lake CPUs and achieve significant speedup over eight V100 GPUs using a similar power envelop. In the end-to-end training, we get a speedup of 1.41x on Cascade Lake with FP32, 1.57x on Cooper Lake with FP32, and 2.27x on Cooper Lake with BFloat16 over eight V100 GPUs with FP32.

</details>

### [A Method to Reveal Speaker Identity in Distributed ASR Training, and How to Counter It](2104.07815.md)
**Trung Dang, Om Thakkar, Swaroop Ramaswamy, Rajiv Mathews et al.** · 2021-04-15

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) models are commonly trained over spoken utterances using optimization methods like Stochastic Gradient Descent (SGD). In distributed settings like Federated Learning, model training requires transmission of gradients over a network. In this work, we design the first method for revealing the identity of the speaker of a training utterance with access only to a gradient. We propose Hessian-Free Gradients Matching, an input reconstruction technique that operates without second derivatives of the loss function (required in prior works), which can be expensive to compute. We show the effectiveness of our method using the DeepSpeech model architecture, demonstrating that it is possible to reveal the speaker's identity with 34% top-1 accuracy (51% top-5 accuracy) on the LibriSpeech dataset. Further, we study the effect of two well-known techniques, Differentially Private SGD and Dropout, on the success of our method. We show that a dropout rate of 0.2 can reduce the speaker identity accuracy to 0% top-1 (0.5% top-5).

</details>

### [Cross-domain Speech Recognition with Unsupervised Character-level Distribution Matching](2104.07491.md)
**Wenxin Hou, Jindong Wang, Xu Tan, Tao Qin et al.** · 2021-04-15

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) can achieve promising performance with large-scale training data. However, it is known that domain mismatch between training and testing data often leads to a degradation of recognition accuracy. In this work, we focus on the unsupervised domain adaptation for ASR and propose CMatch, a Character-level distribution matching method to perform fine-grained adaptation between each character in two domains. First, to obtain labels for the features belonging to each character, we achieve frame-level label assignment using the Connectionist Temporal Classification (CTC) pseudo labels. Then, we match the character-level distributions using Maximum Mean Discrepancy. We train our algorithm using the self-training technique. Experiments on the Libri-Adapt dataset show that our proposed approach achieves 14.39% and 16.50% relative Word Error Rate (WER) reduction on both cross-device and cross-environment ASR. We also comprehensively analyze the different strategies for frame-level label assignment and Transformer adaptations.

</details>

### [Conditional independence for pretext task selection in Self-supervised speech representation learning](2104.07388.md)
**Salah Zaiem, Titouan Parcollet, Slim Essid** · 2021-04-15

<details>
<summary>Abstract</summary>

Through solving pretext tasks, self-supervised learning (SSL) leverages unlabeled data to extract useful latent representations replacing traditional input features in the downstream task. A common pretext task consists in pretraining a SSL model on pseudo-labels derived from the original signal. This technique is particularly relevant for speech data where various meaningful signal processing features may serve as pseudo-labels. However, the process of selecting pseudo-labels, for speech or other types of data, remains mostly unexplored and currently relies on observing the results on the final downstream task. Nevertheless, this methodology is not sustainable at scale due to substantial computational (hence carbon) costs. Thus, this paper introduces a practical and theoretical framework to select relevant pseudo-labels with respect to a given downstream task. More precisely, we propose a functional estimator of the pseudo-label utility grounded in the conditional independence theory, which does not require any training. The experiments conducted on speaker recognition and automatic speech recognition validate our estimator, showing a significant correlation between the performance observed on the downstream task and the utility estimates obtained with our approach, facilitating the prospection of relevant pseudo-labels for self-supervised speech representation learning.

</details>

### [Efficient conformer-based speech recognition with linear attention](2104.06865.md)
**Shengqiang Li, Menglong Xu, Xiao-Lei Zhang** · 2021-04-14

<details>
<summary>Abstract</summary>

Recently, conformer-based end-to-end automatic speech recognition, which outperforms recurrent neural network based ones, has received much attention. Although the parallel computing of conformer is more efficient than recurrent neural networks, the computational complexity of its dot-product self-attention is quadratic with respect to the length of the input feature. To reduce the computational complexity of the self-attention layer, we propose multi-head linear self-attention for the self-attention layer, which reduces its computational complexity to linear order. In addition, we propose to factorize the feed forward module of the conformer by low-rank matrix factorization, which successfully reduces the number of the parameters by approximate 50% with little performance loss. The proposed model, named linear attention based conformer (LAC), can be trained and inferenced jointly with the connectionist temporal classification objective, which further improves the performance of LAC. To evaluate the effectiveness of LAC, we conduct experiments on the AISHELL-1 and LibriSpeech corpora. Results show that the proposed LAC achieves better performance than 7 recently proposed speech recognition models, and is competitive with the state-of-the-art conformer. Meanwhile, the proposed LAC has a number of parameters of only 50% over the conformer with faster training speed than the latter.

</details>

### [EAT: Enhanced ASR-TTS for Self-supervised Speech Recognition](2104.07474.md)
**Murali Karthick Baskar, Lukáš Burget, Shinji Watanabe, Ramon Fernandez Astudillo et al.** · 2021-04-13

<details>
<summary>Abstract</summary>

Self-supervised ASR-TTS models suffer in out-of-domain data conditions. Here we propose an enhanced ASR-TTS (EAT) model that incorporates two main features: 1) The ASR$\rightarrow$TTS direction is equipped with a language model reward to penalize the ASR hypotheses before forwarding it to TTS. 2) In the TTS$\rightarrow$ASR direction, a hyper-parameter is introduced to scale the attention context from synthesized speech before sending it to ASR to handle out-of-domain data. Training strategies and the effectiveness of the EAT model are explored under out-of-domain data conditions. The results show that EAT reduces the performance gap between supervised and self-supervised training significantly by absolute 2.6\% and 2.7\% on Librispeech and BABEL respectively.

</details>

### [Source and Target Bidirectional Knowledge Distillation for End-to-end Speech Translation](2104.06457.md)
**Hirofumi Inaguma, Tatsuya Kawahara, Shinji Watanabe** · 2021-04-13

<details>
<summary>Abstract</summary>

A conventional approach to improving the performance of end-to-end speech translation (E2E-ST) models is to leverage the source transcription via pre-training and joint training with automatic speech recognition (ASR) and neural machine translation (NMT) tasks. However, since the input modalities are different, it is difficult to leverage source language text successfully. In this work, we focus on sequence-level knowledge distillation (SeqKD) from external text-based NMT models. To leverage the full potential of the source language information, we propose backward SeqKD, SeqKD from a target-to-source backward NMT model. To this end, we train a bilingual E2E-ST model to predict paraphrased transcriptions as an auxiliary task with a single decoder. The paraphrases are generated from the translations in bitext via back-translation. We further propose bidirectional SeqKD in which SeqKD from both forward and backward NMT models is combined. Experimental evaluations on both autoregressive and non-autoregressive models show that SeqKD in each direction consistently improves the translation performance, and the effectiveness is complementary regardless of the model capacity.

</details>

### [Equivalence of Segmental and Neural Transducer Modeling: A Proof of Concept](2104.06104.md)
**Wei Zhou, Albert Zeyer, André Merboldt, Ralf Schlüter et al.** · 2021-04-13

<details>
<summary>Abstract</summary>

With the advent of direct models in automatic speech recognition (ASR), the formerly prevalent frame-wise acoustic modeling based on hidden Markov models (HMM) diversified into a number of modeling architectures like encoder-decoder attention models, transducer models and segmental models (direct HMM). While transducer models stay with a frame-level model definition, segmental models are defined on the level of label segments directly. While (soft-)attention-based models avoid explicit alignment, transducer and segmental approach internally do model alignment, either by segment hypotheses or, more implicitly, by emitting so-called blank symbols. In this work, we prove that the widely used class of RNN-Transducer models and segmental models (direct HMM) are equivalent and therefore show equal modeling power. It is shown that blank probabilities translate into segment length probabilities and vice versa. In addition, we provide initial experiments investigating decoding and beam-pruning, comparing time-synchronous and label-/segment-synchronous search strategies and their properties using the same underlying model.

</details>

### [Experiments of ASR-based mispronunciation detection for children and adult English learners](2104.05980.md)
**Nina Hosseini-Kivanani, Roberto Gretter, Marco Matassoni, Giuseppe Daniele Falavigna** · 2021-04-13

<details>
<summary>Abstract</summary>

Pronunciation is one of the fundamentals of language learning, and it is considered a primary factor of spoken language when it comes to an understanding and being understood by others. The persistent presence of high error rates in speech recognition domains resulting from mispronunciations motivates us to find alternative techniques for handling mispronunciations. In this study, we develop a mispronunciation assessment system that checks the pronunciation of non-native English speakers, identifies the commonly mispronounced phonemes of Italian learners of English, and presents an evaluation of the non-native pronunciation observed in phonetically annotated speech corpora. In this work, to detect mispronunciations, we used a phone-based ASR implemented using Kaldi. We used two non-native English labeled corpora; (i) a corpus of Italian adults contains 5,867 utterances from 46 speakers, and (ii) a corpus of Italian children consists of 5,268 utterances from 78 children. Our results show that the selected error model can discriminate correct sounds from incorrect sounds in both native and nonnative speech, and therefore can be used to detect pronunciation errors in non-native speech. The phone error rates show improvement in using the error language model. The ASR system shows better accuracy after applying the error model on our selected corpora.

</details>

### [Improved Conformer-based End-to-End Speech Recognition Using Neural Architecture Search](2104.05390.md)
**Yukun Liu, Ta Li, Pengyuan Zhang, Yonghong Yan** · 2021-04-12

<details>
<summary>Abstract</summary>

Recently neural architecture search(NAS) has been successfully used in image classification, natural language processing, and automatic speech recognition(ASR) tasks for finding the state-of-the-art(SOTA) architectures than those human-designed architectures. NAS can derive a SOTA and data-specific architecture over validation data from a pre-defined search space with a search algorithm. Inspired by the success of NAS in ASR tasks, we propose a NAS-based ASR framework containing one search space and one differentiable search algorithm called Differentiable Architecture Search(DARTS). Our search space follows the convolution-augmented transformer(Conformer) backbone, which is a more expressive ASR architecture than those used in existing NAS-based ASR frameworks. To improve the performance of our method, a regulation method called Dynamic Search Schedule(DSS) is employed. On a widely used Mandarin benchmark AISHELL-1, our best-searched architecture outperforms the baseline Conform model significantly with about 11% CER relative improvement, and our method is proved to be pretty efficient by the search cost comparisons.

</details>

### [Comparing the Benefit of Synthetic Training Data for Various Automatic Speech Recognition Architectures](2104.05379.md)
**Nick Rossenbach, Mohammad Zeineldeen, Benedikt Hilmes, Ralf Schlüter et al.** · 2021-04-12

<details>
<summary>Abstract</summary>

Recent publications on automatic-speech-recognition (ASR) have a strong focus on attention encoder-decoder (AED) architectures which tend to suffer from over-fitting in low resource scenarios. One solution to tackle this issue is to generate synthetic data with a trained text-to-speech system (TTS) if additional text is available. This was successfully applied in many publications with AED systems, but only very limited in the context of other ASR architectures. We investigate the effect of varying pre-processing, the speaker embedding and input encoding of the TTS system w.r.t. the effectiveness of the synthesized data for AED-ASR training. Additionally, we also consider internal language model subtraction for the first time, resulting in up to 38% relative improvement. We compare the AED results to a state-of-the-art hybrid ASR system, a monophone based system using connectionist-temporal-classification (CTC) and a monotonic transducer based system. We show that for the later systems the addition of synthetic data has no relevant effect, but they still outperform the AED systems on LibriSpeech-100h. We achieve a final word-error-rate of 3.3%/10.0% with a hybrid system on the clean/noisy test-sets, surpassing any previous state-of-the-art systems on Librispeech-100h that do not include unlabeled audio data.

</details>

### [Innovative Bert-based Reranking Language Models for Speech Recognition](2104.04950.md)
**Shih-Hsuan Chiu, Berlin Chen** · 2021-04-11

<details>
<summary>Abstract</summary>

More recently, Bidirectional Encoder Representations from Transformers (BERT) was proposed and has achieved impressive success on many natural language processing (NLP) tasks such as question answering and language understanding, due mainly to its effective pre-training then fine-tuning paradigm as well as strong local contextual modeling ability. In view of the above, this paper presents a novel instantiation of the BERT-based contextualized language models (LMs) for use in reranking of N-best hypotheses produced by automatic speech recognition (ASR). To this end, we frame N-best hypothesis reranking with BERT as a prediction problem, which aims to predict the oracle hypothesis that has the lowest word error rate (WER) given the N-best hypotheses (denoted by PBERT). In particular, we also explore to capitalize on task-specific global topic information in an unsupervised manner to assist PBERT in N-best hypothesis reranking (denoted by TPBERT). Extensive experiments conducted on the AMI benchmark corpus demonstrate the effectiveness and feasibility of our methods in comparison to the conventional autoregressive models like the recurrent neural network (RNN) and a recently proposed method that employed BERT to compute pseudo-log-likelihood (PLL) scores for N-best hypothesis reranking.

</details>

### [Non-autoregressive Transformer-based End-to-end ASR using BERT](2104.04805.md)
**Fu-Hao Yu, Kuan-Yu Chen** · 2021-04-10

<details>
<summary>Abstract</summary>

Transformer-based models have led to significant innovation in classical and practical subjects as varied as speech processing, natural language processing, and computer vision. On top of the Transformer, attention-based end-to-end automatic speech recognition (ASR) models have recently become popular. Specifically, non-autoregressive modeling, which boasts fast inference and performance comparable to conventional autoregressive methods, is an emerging research topic. In the context of natural language processing, the bidirectional encoder representations from Transformers (BERT) model has received widespread attention, partially due to its ability to infer contextualized word representations and to enable superior performance for downstream tasks while needing only simple fine-tuning. Motivated by the success, we intend to view speech recognition as a downstream task of BERT, thus an ASR system is expected to be deduced by performing fine-tuning. Consequently, to not only inherit the advantages of non-autoregressive ASR models but also enjoy the benefits of a pre-trained language model (e.g., BERT), we propose a non-autoregressive Transformer-based end-to-end ASR model based on BERT. We conduct a series of experiments on the AISHELL-1 dataset that demonstrate competitive or superior results for the model when compared to state-of-the-art ASR systems.

</details>

### [Boundary and Context Aware Training for CIF-based Non-Autoregressive End-to-end ASR](2104.04702.md)
**Fan Yu, Haoneng Luo, Pengcheng Guo, Yuhao Liang et al.** · 2021-04-10

<details>
<summary>Abstract</summary>

Continuous integrate-and-fire (CIF) based models, which use a soft and monotonic alignment mechanism, have been well applied in non-autoregressive (NAR) speech recognition with competitive performance compared with other NAR methods. However, such an alignment learning strategy may suffer from an erroneous acoustic boundary estimation, severely hindering the convergence speed as well as the system performance. In this paper, we propose a boundary and context aware training approach for CIF based NAR models. Firstly, the connectionist temporal classification (CTC) spike information is utilized to guide the learning of acoustic boundaries in the CIF. Besides, an additional contextual decoder is introduced behind the CIF decoder, aiming to capture the linguistic dependencies within a sentence. Finally, we adopt a recently proposed Conformer architecture to improve the capacity of acoustic modeling. Experiments on the open-source Mandarin AISHELL-1 corpus show that the proposed method achieves a comparable character error rates (CERs) of 4.9% with only 1/24 latency compared with a state-of-the-art autoregressive (AR) Conformer model. Futhermore, when evaluating on an internal 7500 hours Mandarin corpus, our model still outperforms other NAR methods and even reaches the AR Conformer model on a challenging real-world noisy test set.

</details>

### [Accented Speech Recognition Inspired by Human Perception](2104.04627.md)
**Xiangyun Chu, Elizabeth Combs, Amber Wang, Michael Picheny** · 2021-04-09

<details>
<summary>Abstract</summary>

While improvements have been made in automatic speech recognition performance over the last several years, machines continue to have significantly lower performance on accented speech than humans. In addition, the most significant improvements on accented speech primarily arise by overwhelming the problem with hundreds or even thousands of hours of data. Humans typically require much less data to adapt to a new accent. This paper explores methods that are inspired by human perception to evaluate possible performance improvements for recognition of accented speech, with a specific focus on recognizing speech with a novel accent relative to that of the training data. Our experiments are run on small, accessible datasets that are available to the research community. We explore four methodologies: pre-exposure to multiple accents, grapheme and phoneme-based pronunciations, dropout (to improve generalization to a novel accent), and the identification of the layers in the neural network that can specifically be associated with accent modeling. Our results indicate that methods based on human perception are promising in reducing WER and understanding how accented speech is modeled in neural networks for novel accents.

</details>

### [Lookup-Table Recurrent Language Models for Long Tail Speech Recognition](2104.04552.md)
**W. Ronny Huang, Tara N. Sainath, Cal Peyser, Shankar Kumar et al.** · 2021-04-09

<details>
<summary>Abstract</summary>

We introduce Lookup-Table Language Models (LookupLM), a method for scaling up the size of RNN language models with only a constant increase in the floating point operations, by increasing the expressivity of the embedding table. In particular, we instantiate an (additional) embedding table which embeds the previous n-gram token sequence, rather than a single token. This allows the embedding table to be scaled up arbitrarily -- with a commensurate increase in performance -- without changing the token vocabulary. Since embeddings are sparsely retrieved from the table via a lookup; increasing the size of the table adds neither extra operations to each forward pass nor extra parameters that need to be stored on limited GPU/TPU memory. We explore scaling n-gram embedding tables up to nearly a billion parameters. When trained on a 3-billion sentence corpus, we find that LookupLM improves long tail log perplexity by 2.44 and long tail WER by 23.4% on a downstream speech recognition task over a standard RNN language model baseline, an improvement comparable to a scaling up the baseline by 6.2x the number of floating point operations.

</details>

### [Language model fusion for streaming end to end speech recognition](2104.04487.md)
**Rodrigo Cabrera, Xiaofeng Liu, Mohammadreza Ghodsi, Zebulun Matteson et al.** · 2021-04-09

<details>
<summary>Abstract</summary>

Streaming processing of speech audio is required for many contemporary practical speech recognition tasks. Even with the large corpora of manually transcribed speech data available today, it is impossible for such corpora to cover adequately the long tail of linguistic content that's important for tasks such as open-ended dictation and voice search. We seek to address both the streaming and the tail recognition challenges by using a language model (LM) trained on unpaired text data to enhance the end-to-end (E2E) model. We extend shallow fusion and cold fusion approaches to streaming Recurrent Neural Network Transducer (RNNT), and also propose two new competitive fusion approaches that further enhance the RNNT architecture. Our results on multiple languages with varying training set sizes show that these fusion methods improve streaming RNNT performance through introducing extra linguistic features. Cold fusion works consistently better on streaming RNNT with up to a 8.5% WER improvement.

</details>

### [On Architectures and Training for Raw Waveform Feature Extraction in ASR](2104.04298.md)
**Peter Vieting, Christoph Lüscher, Wilfried Michel, Ralf Schlüter et al.** · 2021-04-09

<details>
<summary>Abstract</summary>

With the success of neural network based modeling in automatic speech recognition (ASR), many studies investigated acoustic modeling and learning of feature extractors directly based on the raw waveform. Recently, one line of research has focused on unsupervised pre-training of feature extractors on audio-only data to improve downstream ASR performance. In this work, we investigate the usefulness of one of these front-end frameworks, namely wav2vec, in a setting without additional untranscribed data for hybrid ASR systems. We compare this framework both to the manually defined standard Gammatone feature set, as well as to features extracted as part of the acoustic model of an ASR system trained supervised. We study the benefits of using the pre-trained feature extractor and explore how to additionally exploit an existing acoustic model trained with different features. Finally, we systematically examine combinations of the described features in order to further advance the performance.

</details>

### [The NTNU Taiwanese ASR System for Formosa Speech Recognition Challenge 2020](2104.04221.md)
**Fu-An Chao, Tien-Hong Lo, Shi-Yan Weng, Shih-Hsuan Chiu et al.** · 2021-04-09

<details>
<summary>Abstract</summary>

This paper describes the NTNU ASR system participating in the Formosa Speech Recognition Challenge 2020 (FSR-2020) supported by the Formosa Speech in the Wild project (FSW). FSR-2020 aims at fostering the development of Taiwanese speech recognition. Apart from the issues on tonal and dialectical variations of the Taiwanese language, speech artificially contaminated with different types of real-world noise also has to be dealt with in the final test stage; all of these make FSR-2020 much more challenging than before. To work around the under-resourced issue, the main technical aspects of our ASR system include various deep learning techniques, such as transfer learning, semi-supervised learning, front-end speech enhancement and model ensemble, as well as data cleansing and data augmentation conducted on the training data. With the best configuration, our system obtains 13.1 % syllable error rate (SER) on the final-test set, achieving the first place among all participating systems on Track 3.

</details>

### [RNN Transducer Models For Spoken Language Understanding](2104.03842.md)
**Samuel Thomas, Hong-Kwang J. Kuo, George Saon, Zoltán Tüske et al.** · 2021-04-08

<details>
<summary>Abstract</summary>

We present a comprehensive study on building and adapting RNN transducer (RNN-T) models for spoken language understanding(SLU). These end-to-end (E2E) models are constructed in three practical settings: a case where verbatim transcripts are available, a constrained case where the only available annotations are SLU labels and their values, and a more restrictive case where transcripts are available but not corresponding audio. We show how RNN-T SLU models can be developed starting from pre-trained automatic speech recognition (ASR) systems, followed by an SLU adaptation step. In settings where real audio data is not available, artificially synthesized speech is used to successfully adapt various SLU models. When evaluated on two SLU data sets, the ATIS corpus and a customer call center data set, the proposed models closely track the performance of other E2E models and achieve state-of-the-art results.

</details>

### [Exploring Machine Speech Chain for Domain Adaptation and Few-Shot Speaker Adaptation](2104.03815.md)
**Fengpeng Yue, Yan Deng, Lei He, Tom Ko** · 2021-04-08

<details>
<summary>Abstract</summary>

Machine Speech Chain, which integrates both end-to-end (E2E) automatic speech recognition (ASR) and text-to-speech (TTS) into one circle for joint training, has been proven to be effective in data augmentation by leveraging large amounts of unpaired data. In this paper, we explore the TTS->ASR pipeline in speech chain to do domain adaptation for both neural TTS and E2E ASR models, with only text data from target domain. We conduct experiments by adapting from audiobook domain (LibriSpeech) to presentation domain (TED-LIUM), there is a relative word error rate (WER) reduction of 10% for the E2E ASR model on the TED-LIUM test set, and a relative WER reduction of 51.5% in synthetic speech generated by neural TTS in the presentation domain. Further, we apply few-shot speaker adaptation for the E2E ASR by using a few utterances from target speakers in an unsupervised way, results in additional gains.

</details>

### [Contextual Semi-Supervised Learning: An Approach To Leverage Air-Surveillance and Untranscribed ATC Data in ASR Systems](2104.03643.md)
**Juan Zuluaga-Gomez, Iuliia Nigmatulina, Amrutha Prasad, Petr Motlicek et al.** · 2021-04-08

<details>
<summary>Abstract</summary>

Air traffic management and specifically air-traffic control (ATC) rely mostly on voice communications between Air Traffic Controllers (ATCos) and pilots. In most cases, these voice communications follow a well-defined grammar that could be leveraged in Automatic Speech Recognition (ASR) technologies. The callsign used to address an airplane is an essential part of all ATCo-pilot communications. We propose a two-steps approach to add contextual knowledge during semi-supervised training to reduce the ASR system error rates at recognizing the part of the utterance that contains the callsign. Initially, we represent in a WFST the contextual knowledge (i.e. air-surveillance data) of an ATCo-pilot communication. Then, during Semi-Supervised Learning (SSL) the contextual knowledge is added by second-pass decoding (i.e. lattice re-scoring). Results show that `unseen domains' (e.g. data from airports not present in the supervised training data) are further aided by contextual SSL when compared to standalone SSL. For this task, we introduce the Callsign Word Error Rate (CA-WER) as an evaluation metric, which only assesses ASR performance of the spoken callsign in an utterance. We obtained a 32.1% CA-WER relative improvement applying SSL with an additional 17.5% CA-WER improvement by adding contextual knowledge during SSL on a challenging ATC-based test set gathered from LiveATC.

</details>

### [Layer Reduction: Accelerating Conformer-Based Self-Supervised Model via Layer Consistency](2105.00812.md)
**Jinchuan Tian, Rongzhi Gu, Helin Wang, Yuexian Zou** · 2021-04-08

<details>
<summary>Abstract</summary>

Transformer-based self-supervised models are trained as feature extractors and have empowered many downstream speech tasks to achieve state-of-the-art performance. However, both the training and inference process of these models may encounter prohibitively high computational cost and large parameter budget. Although Parameter Sharing Strategy (PSS) proposed in ALBERT paves the way for parameter reduction, the computation required remains the same. Interestingly, we found in experiments that distributions of feature embeddings from different Transformer layers are similar when PSS is integrated: a property termed as Layer Consistency (LC) in this paper. Given this similarity of feature distributions, we assume that feature embeddings from different layers would have similar representing power. In this work, Layer Consistency enables us to adopt Transformer-based models in a more efficient manner: the number of Conformer layers in each training iteration could be uniformly sampled and Shallow Layer Inference (SLI) could be applied to reduce the number of layers in inference stage. In experiments, our models are trained with LibriSpeech dataset and then evaluated on both phone classification and Speech Recognition tasks. We experimentally achieve 7.8X parameter reduction, 41.9% training speedup and 37.7% inference speedup while maintaining comparable performance with conventional BERT-like self-supervised methods.

</details>

### [WNARS: WFST based Non-autoregressive Streaming End-to-End Speech Recognition](2104.03587.md)
**Zhichao Wang, Wenwen Yang, Pan Zhou, Wei Chen** · 2021-04-08

<details>
<summary>Abstract</summary>

Recently, attention-based encoder-decoder (AED) end-to-end (E2E) models have drawn more and more attention in the field of automatic speech recognition (ASR). AED models, however, still have drawbacks when deploying in commercial applications. Autoregressive beam search decoding makes it inefficient for high-concurrency applications. It is also inconvenient to integrate external word-level language models. The most important thing is that AED models are difficult for streaming recognition due to global attention mechanism. In this paper, we propose a novel framework, namely WNARS, using hybrid CTC-attention AED models and weighted finite-state transducers (WFST) to solve these problems together. We switch from autoregressive beam search to CTC branch decoding, which performs first-pass decoding with WFST in chunk-wise streaming way. The decoder branch then performs second-pass rescoring on the generated hypotheses non-autoregressively. On the AISHELL-1 task, our WNARS achieves a character error rate of 5.22% with 640ms latency, to the best of our knowledge, which is the state-of-the-art performance for online ASR. Further experiments on our 10,000-hour Mandarin task show the proposed method achieves more than 20% improvements with 50% latency compared to a strong TDNN-BLSTM lattice-free MMI baseline.

</details>

### [Pushing the Limits of Non-Autoregressive Speech Recognition](2104.03416.md)
**Edwin G. Ng, Chung-Cheng Chiu, Yu Zhang, William Chan** · 2021-04-07

<details>
<summary>Abstract</summary>

We combine recent advancements in end-to-end speech recognition to non-autoregressive automatic speech recognition. We push the limits of non-autoregressive state-of-the-art results for multiple datasets: LibriSpeech, Fisher+Switchboard and Wall Street Journal. Key to our recipe, we leverage CTC on giant Conformer neural network architectures with SpecAugment and wav2vec2 pre-training. We achieve 1.8%/3.6% WER on LibriSpeech test/test-other sets, 5.1%/9.8% WER on Switchboard, and 3.4% on the Wall Street Journal, all without a language model.

</details>

### [Speak or Chat with Me: End-to-End Spoken Language Understanding System with Flexible Inputs](2104.05752.md)
**Sujeong Cha, Wangrui Hou, Hyun Jung, My Phung et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

A major focus of recent research in spoken language understanding (SLU) has been on the end-to-end approach where a single model can predict intents directly from speech inputs without intermediate transcripts. However, this approach presents some challenges. First, since speech can be considered as personally identifiable information, in some cases only automatic speech recognition (ASR) transcripts are accessible. Second, intent-labeled speech data is scarce. To address the first challenge, we propose a novel system that can predict intents from flexible types of inputs: speech, ASR transcripts, or both. We demonstrate strong performance for either modality separately, and when both speech and ASR transcripts are available, through system combination, we achieve better results than using a single input modality. To address the second challenge, we leverage a semantically robust pre-trained BERT model and adopt a cross-modal system that co-trains text embeddings and acoustic embeddings in a shared latent space. We further enhance this system by utilizing an acoustic module pre-trained on LibriSpeech and domain-adapting the text module on our target datasets. Our experiments show significant advantages for these pre-training and fine-tuning strategies, resulting in a system that achieves competitive intent-classification performance on Snips SLU and Fluent Speech Commands datasets.

</details>

### [FSR: Accelerating the Inference Process of Transducer-Based Models by Applying Fast-Skip Regularization](2104.02882.md)
**Zhengkun Tian, Jiangyan Yi, Ye Bai, Jianhua Tao et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

Transducer-based models, such as RNN-Transducer and transformer-transducer, have achieved great success in speech recognition. A typical transducer model decodes the output sequence conditioned on the current acoustic state and previously predicted tokens step by step. Statistically, The number of blank tokens in the prediction results accounts for nearly 90\% of all tokens. It takes a lot of computation and time to predict the blank tokens, but only the non-blank tokens will appear in the final output sequence. Therefore, we propose a method named fast-skip regularization, which tries to align the blank position predicted by a transducer with that predicted by a CTC model. During the inference, the transducer model can predict the blank tokens in advance by a simple CTC project layer without many complicated forward calculations of the transducer decoder and then skip them, which will reduce the computation and improve the inference speed greatly. All experiments are conducted on a public Chinese mandarin dataset AISHELL-1. The results show that the fast-skip regularization can indeed help the transducer model learn the blank position alignments. Besides, the inference with fast-skip can be speeded up nearly 4 times with only a little performance degradation.

</details>

### [Capturing Multi-Resolution Context by Dilated Self-Attention](2104.02858.md)
**Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2021-04-07

<details>
<summary>Abstract</summary>

Self-attention has become an important and widely used neural network component that helped to establish new state-of-the-art results for various applications, such as machine translation and automatic speech recognition (ASR). However, the computational complexity of self-attention grows quadratically with the input sequence length. This can be particularly problematic for applications such as ASR, where an input sequence generated from an utterance can be relatively long. In this work, we propose a combination of restricted self-attention and a dilation mechanism, which we refer to as dilated self-attention. The restricted self-attention allows attention to neighboring frames of the query at a high resolution, and the dilation mechanism summarizes distant information to allow attending to it with a lower resolution. Different methods for summarizing distant frames are studied, such as subsampling, mean-pooling, and attention-based pooling. ASR results demonstrate substantial improvements compared to restricted self-attention alone, achieving similar results compared to full-sequence based self-attention with a fraction of the computational costs.

</details>

### [Darts-Conformer: Towards Efficient Gradient-Based Neural Architecture Search For End-to-End ASR](2104.02868.md)
**Xian Shi, Pan Zhou, Wei Chen, Lei Xie** · 2021-04-07

<details>
<summary>Abstract</summary>

Neural architecture search (NAS) has been successfully applied to tasks like image classification and language modeling for finding efficient high-performance network architectures. In ASR field especially end-to-end ASR, the related research is still in its infancy. In this work, we focus on applying NAS on the most popular manually designed model: Conformer, and then propose an efficient ASR model searching method that benefits from the natural advantage of differentiable architecture search (Darts) in reducing computational overheads. We fuse Darts mutator and Conformer blocks to form a complete search space, within which a modified architecture called Darts-Conformer cell is found automatically. The entire searching process on AISHELL-1 dataset costs only 0.7 GPU days. Replacing the Conformer encoder by stacking searched cell, we get an end-to-end ASR model (named as Darts-Conformner) that outperforms the Conformer baseline by 4.7\% on the open-source AISHELL-1 dataset. Besides, we verify the transferability of the architecture searched on a small dataset to a larger 2k-hour dataset. To the best of our knowledge, this is the first successful attempt to apply gradient-based architecture search in the attention-based encoder-decoder ASR model.

</details>

### [Interpreting A Pre-trained Model Is A Key For Model Architecture Optimization: A Case Study On Wav2Vec 2.0](2104.02851.md)
**Liu Chen, Meysam Asgari** · 2021-04-07

<details>
<summary>Abstract</summary>

A deep Transformer model with good evaluation score does not mean each subnetwork (a.k.a transformer block) learns reasonable representation. Diagnosing abnormal representation and avoiding it can contribute to achieving a better evaluation score. We propose an innovative perspective for analyzing attention patterns: summarize block-level patterns and assume abnormal patterns contribute negative influence. We leverage Wav2Vec 2.0 as a research target and analyze a pre-trained model's pattern. All experiments leverage Librispeech-100-clean as training data. Through avoiding diagnosed abnormal ones, our custom Wav2Vec 2.0 outperforms the original version about 4.8% absolute word error rate (WER) on test-clean with viterbi decoding. Our version is still 0.9% better when decoding with a 4-gram language model. Moreover, we identify that avoiding abnormal patterns is the main contributor for performance boosting.

</details>

### [Learning to Rank Microphones for Distant Speech Recognition](2104.02819.md)
**Samuele Cornell, Alessio Brutti, Marco Matassoni, Stefano Squartini** · 2021-04-06

<details>
<summary>Abstract</summary>

Fully exploiting ad-hoc microphone networks for distant speech recognition is still an open issue. Empirical evidence shows that being able to select the best microphone leads to significant improvements in recognition without any additional effort on front-end processing. Current channel selection techniques either rely on signal, decoder or posterior-based features. Signal-based features are inexpensive to compute but do not always correlate with recognition performance. Instead decoder and posterior-based features exhibit better correlation but require substantial computational resources. In this work, we tackle the channel selection problem by proposing MicRank, a learning to rank framework where a neural network is trained to rank the available channels using directly the recognition performance on the training set. The proposed approach is agnostic with respect to the array geometry and type of recognition back-end. We investigate different learning to rank strategies using a synthetic dataset developed on purpose and the CHiME-6 data. Results show that the proposed approach is able to considerably improve over previous selection techniques, reaching comparable and in some instances better performance than oracle signal-based measures.

</details>

### [Exploring Targeted Universal Adversarial Perturbations to End-to-end ASR Models](2104.02757.md)
**Zhiyun Lu, Wei Han, Yu Zhang, Liangliang Cao** · 2021-04-06

<details>
<summary>Abstract</summary>

Although end-to-end automatic speech recognition (e2e ASR) models are widely deployed in many applications, there have been very few studies to understand models' robustness against adversarial perturbations. In this paper, we explore whether a targeted universal perturbation vector exists for e2e ASR models. Our goal is to find perturbations that can mislead the models to predict the given targeted transcript such as "thank you" or empty string on any input utterance. We study two different attacks, namely additive and prepending perturbations, and their performances on the state-of-the-art LAS, CTC and RNN-T models. We find that LAS is the most vulnerable to perturbations among the three models. RNN-T is more robust against additive perturbations, especially on long utterances. And CTC is robust against both additive and prepending perturbations. To attack RNN-T, we find prepending perturbation is more effective than the additive perturbation, and can mislead the models to predict the same short target on utterances of arbitrary length.

</details>

### [Comparing CTC and LFMMI for out-of-domain adaptation of wav2vec 2.0 acoustic model](2104.02558.md)
**Apoorv Vyas, Srikanth Madikeri, Hervé Bourlard** · 2021-04-06

<details>
<summary>Abstract</summary>

In this work, we investigate if the wav2vec 2.0 self-supervised pretraining helps mitigate the overfitting issues with connectionist temporal classification (CTC) training to reduce its performance gap with flat-start lattice-free MMI (E2E-LFMMI) for automatic speech recognition with limited training data. Towards that objective, we use the pretrained wav2vec 2.0 BASE model and fine-tune it on three different datasets including out-of-domain (Switchboard) and cross-lingual (Babel) scenarios. Our results show that for supervised adaptation of the wav2vec 2.0 model, both E2E-LFMMI and CTC achieve similar results; significantly outperforming the baselines trained only with supervised data. Fine-tuning the wav2vec 2.0 model with E2E-LFMMI and CTC we obtain the following relative WER improvements over the supervised baseline trained with E2E-LFMMI. We get relative improvements of 40% and 44% on the clean-set and 64% and 58% on the test set of Librispeech (100h) respectively. On Switchboard (300h) we obtain relative improvements of 33% and 35% respectively. Finally, for Babel languages, we obtain relative improvements of 26% and 23% on Swahili (38h) and 18% and 17% on Tagalog (84h) respectively.

</details>

### [Optimal Transport-based Adaptation in Dysarthric Speech Tasks](2104.02535.md)
**Rosanna Turrisi, Leonardo Badino** · 2021-04-06

<details>
<summary>Abstract</summary>

In many real-world applications, the mismatch between distributions of training data (source) and test data (target) significantly degrades the performance of machine learning algorithms. In speech data, causes of this mismatch include different acoustic environments or speaker characteristics. In this paper, we address this issue in the challenging context of dysarthric speech, by multi-source domain/speaker adaptation (MSDA/MSSA). Specifically, we propose the use of an optimal-transport based approach, called MSDA via Weighted Joint Optimal Transport (MSDA-WDJOT). We confront the mismatch problem in dysarthria detection for which the proposed approach outperforms both the Baseline and the state-of-the-art MSDA models, improving the detection accuracy of 0.9% over the best competitor method. We then employ MSDA-WJDOT for dysarthric speaker adaptation in command speech recognition. This provides a Command Error Rate relative reduction of 16% and 7% over the baseline and the best competitor model, respectively. Interestingly, MSDA-WJDOT provides a similarity score between the source and the target, i.e. between speakers in this case. We leverage this similarity measure to define a Dysarthric and Healthy score of the target speaker and diagnose the dysarthria with an accuracy of 95%.

</details>

### [LT-LM: a novel non-autoregressive language model for single-shot lattice rescoring](2104.02526.md)
**Anton Mitrofanov, Mariya Korenevskaya, Ivan Podluzhny, Yuri Khokhlov et al.** · 2021-04-06

<details>
<summary>Abstract</summary>

Neural network-based language models are commonly used in rescoring approaches to improve the quality of modern automatic speech recognition (ASR) systems. Most of the existing methods are computationally expensive since they use autoregressive language models. We propose a novel rescoring approach, which processes the entire lattice in a single call to the model. The key feature of our rescoring policy is a novel non-autoregressive Lattice Transformer Language Model (LT-LM). This model takes the whole lattice as an input and predicts a new language score for each arc. Additionally, we propose the artificial lattices generation approach to incorporate a large amount of text data in the LT-LM training process. Our single-shot rescoring performs orders of magnitude faster than other rescoring methods in our experiments. It is more than 300 times faster than pruned RNNLM lattice rescoring and N-best rescoring while slightly inferior in terms of WER.

</details>

### [AI4D -- African Language Program](2104.02516.md)
**Kathleen Siminyu, Godson Kalipe, Davor Orlic, Jade Abbott et al.** · 2021-04-06

<details>
<summary>Abstract</summary>

Advances in speech and language technologies enable tools such as voice-search, text-to-speech, speech recognition and machine translation. These are however only available for high resource languages like English, French or Chinese. Without foundational digital resources for African languages, which are considered low-resource in the digital context, these advanced tools remain out of reach. This work details the AI4D - African Language Program, a 3-part project that 1) incentivised the crowd-sourcing, collection and curation of language datasets through an online quantitative and qualitative challenge, 2) supported research fellows for a period of 3-4 months to create datasets annotated for NLP tasks, and 3) hosted competitive Machine Learning challenges on the basis of these datasets. Key outcomes of the work so far include 1) the creation of 9+ open source, African language datasets annotated for a variety of ML tasks, and 2) the creation of baseline models for these datasets through hosting of competitive ML challenges.

</details>

### [Extremely Low Footprint End-to-End ASR System for Smart Device](2104.05784.md)
**Zhifu Gao, Yiwu Yao, Shiliang Zhang, Jun Yang et al.** · 2021-04-06

<details>
<summary>Abstract</summary>

Recently, end-to-end (E2E) speech recognition has become popular, since it can integrate the acoustic, pronunciation and language models into a single neural network, which outperforms conventional models. Among E2E approaches, attention-based models, e.g. Transformer, have emerged as being superior. Such models have opened the door to deployment of ASR on smart devices, however they still suffer from requiring a large number of model parameters. We propose an extremely low footprint E2E ASR system for smart devices, to achieve the goal of satisfying resource constraints without sacrificing recognition accuracy. We design cross-layer weight sharing to improve parameter efficiency and further exploit model compression methods including sparsification and quantization, to reduce memory storage and boost decoding efficiency. We evaluate our approaches on the public AISHELL-1 and AISHELL-2 benchmarks. On the AISHELL-2 task, the proposed method achieves more than 10x compression (model size reduces from 248 to 24MB), at the cost of only minor performance loss (CER reduces from 6.49% to 6.92%).

</details>

### [Non-autoregressive Mandarin-English Code-switching Speech Recognition](2104.02258.md)
**Shun-Po Chuang, Heng-Jui Chang, Sung-Feng Huang, Hung-yi Lee** · 2021-04-06

<details>
<summary>Abstract</summary>

Mandarin-English code-switching (CS) is frequently used among East and Southeast Asian people. However, the intra-sentence language switching of the two very different languages makes recognizing CS speech challenging. Meanwhile, the recent successful non-autoregressive (NAR) ASR models remove the need for left-to-right beam decoding in autoregressive (AR) models and achieved outstanding performance and fast inference speed, but it has not been applied to Mandarin-English CS speech recognition. This paper takes advantage of the Mask-CTC NAR ASR framework to tackle the CS speech recognition issue. We further propose to change the Mandarin output target of the encoder to Pinyin for faster encoder training and introduce the Pinyin-to-Mandarin decoder to learn contextualized information. Moreover, we use word embedding label smoothing to regularize the decoder with contextualized information and projection matrix regularization to bridge that gap between the encoder and decoder. We evaluate these methods on the SEAME corpus and achieved exciting results.

</details>

### [Flexi-Transducer: Optimizing Latency, Accuracy and Compute forMulti-Domain On-Device Scenarios](2104.02232.md)
**Jay Mahadeokar, Yangyang Shi, Yuan Shangguan, Chunyang Wu et al.** · 2021-04-06

<details>
<summary>Abstract</summary>

Often, the storage and computational constraints of embeddeddevices demand that a single on-device ASR model serve multiple use-cases / domains. In this paper, we propose aFlexibleTransducer(FlexiT) for on-device automatic speech recognition to flexibly deal with multiple use-cases / domains with different accuracy and latency requirements. Specifically, using a single compact model, FlexiT provides a fast response for voice commands, and accurate transcription but with more latency for dictation. In order to achieve flexible and better accuracy and latency trade-offs, the following techniques are used. Firstly, we propose using domain-specific altering of segment size for Emformer encoder that enables FlexiT to achieve flexible de-coding. Secondly, we use Alignment Restricted RNNT loss to achieve flexible fine-grained control on token emission latency for different domains. Finally, we add a domain indicator vector as an additional input to the FlexiT model. Using the combination of techniques, we show that a single model can be used to improve WERs and real time factor for dictation scenarios while maintaining optimal latency for voice commands use-cases

</details>

### [Dissecting User-Perceived Latency of On-Device E2E Speech Recognition](2104.02207.md)
**Yuan Shangguan, Rohit Prabhavalkar, Hang Su, Jay Mahadeokar et al.** · 2021-04-06

<details>
<summary>Abstract</summary>

As speech-enabled devices such as smartphones and smart speakers become increasingly ubiquitous, there is growing interest in building automatic speech recognition (ASR) systems that can run directly on-device; end-to-end (E2E) speech recognition models such as recurrent neural network transducers and their variants have recently emerged as prime candidates for this task. Apart from being accurate and compact, such systems need to decode speech with low user-perceived latency (UPL), producing words as soon as they are spoken. This work examines the impact of various techniques - model architectures, training criteria, decoding hyperparameters, and endpointer parameters - on UPL. Our analyses suggest that measures of model size (parameters, input chunk sizes), or measures of computation (e.g., FLOPS, RTF) that reflect the model's ability to process input frames are not always strongly correlated with observed UPL. Thus, conventional algorithmic latency measurements might be inadequate in accurately capturing latency observed when models are deployed on embedded devices. Instead, we find that factors affecting token emission latency, and endpointing behavior have a larger impact on UPL. We achieve the best trade-off between latency and word error rate when performing ASR jointly with endpointing, while utilizing the recently proposed alignment regularization mechanism.

</details>

### [Contextualized Streaming End-to-End Speech Recognition with Trie-Based Deep Biasing and Shallow Fusion](2104.02194.md)
**Duc Le, Mahaveer Jain, Gil Keren, Suyoun Kim et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

How to leverage dynamic contextual information in end-to-end speech recognition has remained an active research area. Previous solutions to this problem were either designed for specialized use cases that did not generalize well to open-domain scenarios, did not scale to large biasing lists, or underperformed on rare long-tail words. We address these limitations by proposing a novel solution that combines shallow fusion, trie-based deep biasing, and neural network language model contextualization. These techniques result in significant 19.5% relative Word Error Rate improvement over existing contextual biasing approaches and 5.4%-9.3% improvement compared to a strong hybrid baseline on both open-domain and constrained contextualization tasks, where the targets consist of mostly rare long-tail words. Our final system remains lightweight and modular, allowing for quick modification without model re-training.

</details>

### [Dynamic Encoder Transducer: A Flexible Solution For Trading Off Accuracy For Latency](2104.02176.md)
**Yangyang Shi, Varun Nagaraja, Chunyang Wu, Jay Mahadeokar et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

We propose a dynamic encoder transducer (DET) for on-device speech recognition. One DET model scales to multiple devices with different computation capacities without retraining or finetuning. To trading off accuracy and latency, DET assigns different encoders to decode different parts of an utterance. We apply and compare the layer dropout and the collaborative learning for DET training. The layer dropout method that randomly drops out encoder layers in the training phase, can do on-demand layer dropout in decoding. Collaborative learning jointly trains multiple encoders with different depths in one single model. Experiment results on Librispeech and in-house data show that DET provides a flexible accuracy and latency trade-off. Results on Librispeech show that the full-size encoder in DET relatively reduces the word error rate of the same size baseline by over 8%. The lightweight encoder in DET trained with collaborative learning reduces the model size by 25% but still gets similar WER as the full-size baseline. DET gets similar accuracy as a baseline model with better latency on a large in-house data set by assigning a lightweight encoder for the beginning part of one utterance and a full-size encoder for the rest.

</details>

### [Semantic Distance: A New Metric for ASR Performance Analysis Towards Spoken Language Understanding](2104.02138.md)
**Suyoun Kim, Abhinav Arora, Duc Le, Ching-Feng Yeh et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

Word Error Rate (WER) has been the predominant metric used to evaluate the performance of automatic speech recognition (ASR) systems. However, WER is sometimes not a good indicator for downstream Natural Language Understanding (NLU) tasks, such as intent recognition, slot filling, and semantic parsing in task-oriented dialog systems. This is because WER takes into consideration only literal correctness instead of semantic correctness, the latter of which is typically more important for these downstream tasks. In this study, we propose a novel Semantic Distance (SemDist) measure as an alternative evaluation metric for ASR systems to address this issue. We define SemDist as the distance between a reference and hypothesis pair in a sentence-level embedding space. To represent the reference and hypothesis as a sentence embedding, we exploit RoBERTa, a state-of-the-art pre-trained deep contextualized language model based on the transformer architecture. We demonstrate the effectiveness of our proposed metric on various downstream tasks, including intent recognition, semantic parsing, and named entity recognition.

</details>

### [SpeechStew: Simply Mix All Available Speech Recognition Data to Train One Large Neural Network](2104.02133.md)
**William Chan, Daniel Park, Chris Lee, Yu Zhang et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

We present SpeechStew, a speech recognition model that is trained on a combination of various publicly available speech recognition datasets: AMI, Broadcast News, Common Voice, LibriSpeech, Switchboard/Fisher, Tedlium, and Wall Street Journal. SpeechStew simply mixes all of these datasets together, without any special re-weighting or re-balancing of the datasets. SpeechStew achieves SoTA or near SoTA results across a variety of tasks, without the use of an external language model. Our results include 9.0\% WER on AMI-IHM, 4.7\% WER on Switchboard, 8.3\% WER on CallHome, and 1.3\% on WSJ, which significantly outperforms prior work with strong external language models. We also demonstrate that SpeechStew learns powerful transfer learning representations. We fine-tune SpeechStew on a noisy low resource speech dataset, CHiME-6. We achieve 38.9\% WER without a language model, which compares to 38.6\% WER to a strong HMM baseline with a language model.

</details>

### [SPGISpeech: 5,000 hours of transcribed financial audio for fully formatted end-to-end speech recognition](2104.02014.md)
**Patrick K. O'Neill, Vitaly Lavrukhin, Somshubra Majumdar, Vahid Noroozi et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

In the English speech-to-text (STT) machine learning task, acoustic models are conventionally trained on uncased Latin characters, and any necessary orthography (such as capitalization, punctuation, and denormalization of non-standard words) is imputed by separate post-processing models. This adds complexity and limits performance, as many formatting tasks benefit from semantic information present in the acoustic signal but absent in transcription. Here we propose a new STT task: end-to-end neural transcription with fully formatted text for target labels. We present baseline Conformer-based models trained on a corpus of 5,000 hours of professionally transcribed earnings calls, achieving a CER of 1.7. As a contribution to the STT research community, we release the corpus free for non-commercial use at https://datasets.kensho.com/datasets/scribe.

</details>

### [Talk, Don't Write: A Study of Direct Speech-Based Image Retrieval](2104.01894.md)
**Ramon Sanabria, Austin Waters, Jason Baldridge** · 2021-04-05

<details>
<summary>Abstract</summary>

Speech-based image retrieval has been studied as a proxy for joint representation learning, usually without emphasis on retrieval itself. As such, it is unclear how well speech-based retrieval can work in practice -- both in an absolute sense and versus alternative strategies that combine automatic speech recognition (ASR) with strong text encoders. In this work, we extensively study and expand choices of encoder architectures, training methodology (including unimodal and multimodal pretraining), and other factors. Our experiments cover different types of speech in three datasets: Flickr Audio, Places Audio, and Localized Narratives. Our best model configuration achieves large gains over state of the art, e.g., pushing recall-at-one from 21.8% to 33.2% for Flickr Audio and 27.6% to 53.4% for Places Audio. We also show our best speech-based models can match or exceed cascaded ASR-to-text encoding when speech is spontaneous, accented, or otherwise hard to automatically transcribe.

</details>

### [Speaker conditioned acoustic modeling for multi-speaker conversational ASR](2104.01882.md)
**Srikanth Raj Chetupalli, Sriram Ganapathy** · 2021-04-05

<details>
<summary>Abstract</summary>

In this paper, we propose a novel approach for the transcription of speech conversations with natural speaker overlap, from single channel speech recordings. The proposed model is a combination of a speaker diarization system and a hybrid automatic speech recognition (ASR) system. The speaker conditioned acoustic model (SCAM) in the ASR system consists of a series of embedding layers which use the speaker activity inputs from the diarization system to derive speaker specific embeddings. The output of the SCAM are speaker specific senones that are used for decoding the transcripts for each speaker in the conversation. In this work, we experiment with the automatic speaker activity decisions generated using an end-to-end speaker diarization system. A joint learning approach is also proposed where the diarization model and the ASR acoustic model are jointly optimized. The experiments are performed on the mixed-channel two speaker recordings from the Switchboard corpus of telephone conversations. In these experiments, we show that the proposed acoustic model, incorporating speaker activity decisions and joint optimization, improves significantly over the ASR system with explicit source filtering (relative improvements of 12% in word error rate (WER) over the baseline system).

</details>

### [Citrinet: Closing the Gap between Non-Autoregressive and Autoregressive End-to-End Models for Automatic Speech Recognition](2104.01721.md)
**Somshubra Majumdar, Jagadeesh Balam, Oleksii Hrinchuk, Vitaly Lavrukhin et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

We propose Citrinet - a new end-to-end convolutional Connectionist Temporal Classification (CTC) based automatic speech recognition (ASR) model. Citrinet is deep residual neural model which uses 1D time-channel separable convolutions combined with sub-word encoding and squeeze-and-excitation. The resulting architecture significantly reduces the gap between non-autoregressive and sequence-to-sequence and transducer models. We evaluate Citrinet on LibriSpeech, TED-LIUM2, AISHELL-1 and Multilingual LibriSpeech (MLS) English speech datasets. Citrinet accuracy on these datasets is close to the best autoregressive Transducer models.

</details>

### [Phoneme Recognition through Fine Tuning of Phonetic Representations: a Case Study on Luhya Language Varieties](2104.01624.md)
**Kathleen Siminyu, Xinjian Li, Antonios Anastasopoulos, David Mortensen et al.** · 2021-04-04

<details>
<summary>Abstract</summary>

Models pre-trained on multiple languages have shown significant promise for improving speech recognition, particularly for low-resource languages. In this work, we focus on phoneme recognition using Allosaurus, a method for multilingual recognition based on phonetic annotation, which incorporates phonological knowledge through a language-dependent allophone layer that associates a universal narrow phone-set with the phonemes that appear in each language. To evaluate in a challenging real-world scenario, we curate phone recognition datasets for Bukusu and Saamia, two varieties of the Luhya language cluster of western Kenya and eastern Uganda. To our knowledge, these datasets are the first of their kind. We carry out similar experiments on the dataset of an endangered Tangkhulic language, East Tusom, a Tibeto-Burman language variety spoken mostly in India. We explore both zero-shot and few-shot recognition by fine-tuning using datasets of varying sizes (10 to 1000 utterances). We find that fine-tuning of Allosaurus, even with just 100 utterances, leads to significant improvements in phone error rates.

</details>

### [Towards Lifelong Learning of End-to-end ASR](2104.01616.md)
**Heng-Jui Chang, Hung-yi Lee, Lin-shan Lee** · 2021-04-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) technologies today are primarily optimized for given datasets; thus, any changes in the application environment (e.g., acoustic conditions or topic domains) may inevitably degrade the performance. We can collect new data describing the new environment and fine-tune the system, but this naturally leads to higher error rates for the earlier datasets, referred to as catastrophic forgetting. The concept of lifelong learning (LLL) aiming to enable a machine to sequentially learn new tasks from new datasets describing the changing real world without forgetting the previously learned knowledge is thus brought to attention. This paper reports, to our knowledge, the first effort to extensively consider and analyze the use of various approaches of LLL in end-to-end (E2E) ASR, including proposing novel methods in saving data for past domains to mitigate the catastrophic forgetting problem. An overall relative reduction of 28.7% in WER was achieved compared to the fine-tuning baseline when sequentially learning on three very different benchmark corpora. This can be the first step toward the highly desired ASR technologies capable of synchronizing with the continuously changing real world.

</details>

### [TransfoRNN: Capturing the Sequential Information in Self-Attention Representations for Language Modeling](2104.01572.md)
**Tze Yuang Chong, Xuyang Wang, Lin Yang, Junjie Wang** · 2021-04-04

<details>
<summary>Abstract</summary>

In this paper, we describe the use of recurrent neural networks to capture sequential information from the self-attention representations to improve the Transformers. Although self-attention mechanism provides a means to exploit long context, the sequential information, i.e. the arrangement of tokens, is not explicitly captured. We propose to cascade the recurrent neural networks to the Transformers, which referred to as the TransfoRNN model, to capture the sequential information. We found that the TransfoRNN models which consists of only shallow Transformers stack is suffice to give comparable, if not better, performance than a deeper Transformer model. Evaluated on the Penn Treebank and WikiText-2 corpora, the proposed TransfoRNN model has shown lower model perplexities with fewer number of model parameters. On the Penn Treebank corpus, the model perplexities were reduced up to 5.5% with the model size reduced up to 10.5%. On the WikiText-2 corpus, the model perplexity was reduced up to 2.2% with a 27.7% smaller model. Also, the TransfoRNN model was applied on the LibriSpeech speech recognition task and has shown comparable results with the Transformer models.

</details>

### [TSNAT: Two-Step Non-Autoregressvie Transformer Models for Speech Recognition](2104.01522.md)
**Zhengkun Tian, Jiangyan Yi, Jianhua Tao, Ye Bai et al.** · 2021-04-04

<details>
<summary>Abstract</summary>

The autoregressive (AR) models, such as attention-based encoder-decoder models and RNN-Transducer, have achieved great success in speech recognition. They predict the output sequence conditioned on the previous tokens and acoustic encoded states, which is inefficient on GPUs. The non-autoregressive (NAR) models can get rid of the temporal dependency between the output tokens and predict the entire output tokens in at least one step. However, the NAR model still faces two major problems. On the one hand, there is still a great gap in performance between the NAR models and the advanced AR models. On the other hand, it's difficult for most of the NAR models to train and converge. To address these two problems, we propose a new model named the two-step non-autoregressive transformer(TSNAT), which improves the performance and accelerating the convergence of the NAR model by learning prior knowledge from a parameters-sharing AR model. Furthermore, we introduce the two-stage method into the inference process, which improves the model performance greatly. All the experiments are conducted on a public Chinese mandarin dataset ASIEHLL-1. The results show that the TSNAT can achieve a competitive performance with the AR model and outperform many complicated NAR models.

</details>

### [Adversarial Joint Training with Self-Attention Mechanism for Robust End-to-End Speech Recognition](2104.01471.md)
**Lujun Li, Yikai Kang, Yuchen Shi, Ludwig Kürzinger et al.** · 2021-04-03

<details>
<summary>Abstract</summary>

Lately, the self-attention mechanism has marked a new milestone in the field of automatic speech recognition (ASR). Nevertheless, its performance is susceptible to environmental intrusions as the system predicts the next output symbol depending on the full input sequence and the previous predictions. Inspired by the extensive applications of the generative adversarial networks (GANs) in speech enhancement and ASR tasks, we propose an adversarial joint training framework with the self-attention mechanism to boost the noise robustness of the ASR system. Generally, it consists of a self-attention speech enhancement GAN and a self-attention end-to-end ASR model. There are two highlights which are worth noting in this proposed framework. One is that it benefits from the advancement of both self-attention mechanism and GANs; while the other is that the discriminator of GAN plays the role of the global discriminant network in the stage of the adversarial joint training, which guides the enhancement front-end to capture more compatible structures for the subsequent ASR module and thereby offsets the limitation of the separate training and handcrafted loss functions. With the adversarial joint optimization, the proposed framework is expected to learn more robust representations suitable for the ASR task. We execute systematic experiments on the corpus AISHELL-1, and the experimental results show that on the artificial noisy test set, the proposed framework achieves the relative improvements of 66% compared to the ASR model trained by clean data solely, 35.1% compared to the speech enhancement & ASR scheme without joint training, and 5.3% compared to multi-condition training.

</details>

### [On-the-Fly Aligned Data Augmentation for Sequence-to-Sequence ASR](2104.01393.md)
**Tsz Kin Lam, Mayumi Ohta, Shigehiko Schamoni, Stefan Riezler** · 2021-04-03

<details>
<summary>Abstract</summary>

We propose an on-the-fly data augmentation method for automatic speech recognition (ASR) that uses alignment information to generate effective training samples. Our method, called Aligned Data Augmentation (ADA) for ASR, replaces transcribed tokens and the speech representations in an aligned manner to generate previously unseen training pairs. The speech representations are sampled from an audio dictionary that has been extracted from the training corpus and inject speaker variations into the training examples. The transcribed tokens are either predicted by a language model such that the augmented data pairs are semantically close to the original data, or randomly sampled. Both strategies result in training pairs that improve robustness in ASR training. Our experiments on a Seq-to-Seq architecture show that ADA can be applied on top of SpecAugment, and achieves about 9-23% and 4-15% relative improvements in WER over SpecAugment alone on LibriSpeech 100h and LibriSpeech 960h test datasets, respectively.

</details>

### [ExKaldi-RT: A Real-Time Automatic Speech Recognition Extension Toolkit of Kaldi](2104.01384.md)
**Yu Wang, Chee Siang Leow, Akio Kobayashi, Takehito Utsuro et al.** · 2021-04-03

<details>
<summary>Abstract</summary>

This paper describes the ExKaldi-RT online automatic speech recognition (ASR) toolkit that is implemented based on the Kaldi ASR toolkit and Python language. ExKaldi-RT provides tools for building online recognition pipelines. While similar tools are available built on Kaldi, a key feature of ExKaldi-RT that it works on Python, which has an easy-to-use interface that allows online ASR system developers to develop original research, such as by applying neural network-based signal processing and by decoding model trained with deep learning frameworks. We performed benchmark experiments on the minimum LibriSpeech corpus, and it showed that ExKaldi-RT could achieve competitive ASR performance in real-time recognition.

</details>

### [HMM-Free Encoder Pre-Training for Streaming RNN Transducer](2104.10764.md)
**Lu Huang, Jingyu Sun, Yufeng Tang, Junfeng Hou et al.** · 2021-04-02

<details>
<summary>Abstract</summary>

This work describes an encoder pre-training procedure using frame-wise label to improve the training of streaming recurrent neural network transducer (RNN-T) model. Streaming RNN-T trained from scratch usually performs worse than non-streaming RNN-T. Although it is common to address this issue through pre-training components of RNN-T with other criteria or frame-wise alignment guidance, the alignment is not easily available in end-to-end manner. In this work, frame-wise alignment, used to pre-train streaming RNN-T's encoder, is generated without using a HMM-based system. Therefore an all-neural framework equipping HMM-free encoder pre-training is constructed. This is achieved by expanding the spikes of CTC model to their left/right blank frames, and two expanding strategies are proposed. To our best knowledge, this is the first work to simulate HMM-based frame-wise label using CTC model for pre-training. Experiments conducted on LibriSpeech and MLS English tasks show the proposed pre-training procedure, compared with random initialization, reduces the WER by relatively 5%~11% and the emission latency by 60 ms. Besides, the method is lexicon-free, so it is friendly to new languages without manually designed lexicon.

</details>

### [Keyword Transformer: A Self-Attention Model for Keyword Spotting](2104.00769.md)
**Axel Berg, Mark O'Connor, Miguel Tairum Cruz** · 2021-04-01

<details>
<summary>Abstract</summary>

The Transformer architecture has been successful across many domains, including natural language processing, computer vision and speech recognition. In keyword spotting, self-attention has primarily been used on top of convolutional or recurrent encoders. We investigate a range of ways to adapt the Transformer architecture to keyword spotting and introduce the Keyword Transformer (KWT), a fully self-attentional architecture that exceeds state-of-the-art performance across multiple tasks without any pre-training or additional data. Surprisingly, this simple architecture outperforms more complex models that mix convolutional, recurrent and attentive layers. KWT can be used as a drop-in replacement for these models, setting two new benchmark records on the Google Speech Commands dataset with 98.6% and 97.7% accuracy on the 12 and 35-command tasks respectively.

</details>

### [Multi-Encoder Learning and Stream Fusion for Transformer-Based End-to-End Automatic Speech Recognition](2104.00120.md)
**Timo Lohrenz, Zhengyang Li, Tim Fingscheidt** · 2021-03-31

<details>
<summary>Abstract</summary>

Stream fusion, also known as system combination, is a common technique in automatic speech recognition for traditional hybrid hidden Markov model approaches, yet mostly unexplored for modern deep neural network end-to-end model architectures. Here, we investigate various fusion techniques for the all-attention-based encoder-decoder architecture known as the transformer, striving to achieve optimal fusion by investigating different fusion levels in an example single-microphone setting with fusion of standard magnitude and phase features. We introduce a novel multi-encoder learning method that performs a weighted combination of two encoder-decoder multi-head attention outputs only during training. Employing then only the magnitude feature encoder in inference, we are able to show consistent improvement on Wall Street Journal (WSJ) with language model and on Librispeech, without increase in runtime or parameters. Combining two such multi-encoder trained models by a simple late fusion in inference, we achieve state-of-the-art performance for transformer-based models on WSJ with a significant WER reduction of 19% relative compared to the current benchmark approach.

</details>

### [XY Neural Networks](2103.17244.md)
**Nikita Stroev, Natalia G. Berloff** · 2021-03-31

<details>
<summary>Abstract</summary>

The classical XY model is a lattice model of statistical mechanics notable for its universality in the rich hierarchy of the optical, laser and condensed matter systems. We show how to build complex structures for machine learning based on the XY model's nonlinear blocks. The final target is to reproduce the deep learning architectures, which can perform complicated tasks usually attributed to such architectures: speech recognition, visual processing, or other complex classification types with high quality. We developed the robust and transparent approach for the construction of such models, which has universal applicability (i.e. does not strongly connect to any particular physical system), allows many possible extensions while at the same time preserving the simplicity of the methodology.

</details>

### [Adversarial Attacks and Defenses for Speech Recognition Systems](2103.17122.md)
**Piotr Żelasko, Sonal Joshi, Yiwen Shao, Jesus Villalba et al.** · 2021-03-31

<details>
<summary>Abstract</summary>

The ubiquitous presence of machine learning systems in our lives necessitates research into their vulnerabilities and appropriate countermeasures. In particular, we investigate the effectiveness of adversarial attacks and defenses against automatic speech recognition (ASR) systems. We select two ASR models - a thoroughly studied DeepSpeech model and a more recent Espresso framework Transformer encoder-decoder model. We investigate two threat models: a denial-of-service scenario where fast gradient-sign method (FGSM) or weak projected gradient descent (PGD) attacks are used to degrade the model's word error rate (WER); and a targeted scenario where a more potent imperceptible attack forces the system to recognize a specific phrase. We find that the attack transferability across the investigated ASR systems is limited. To defend the model, we use two preprocessing defenses: randomized smoothing and WaveGAN-based vocoder, and find that they significantly improve the model's adversarial robustness. We show that a WaveGAN vocoder can be a useful countermeasure to adversarial attacks on ASR systems - even when it is jointly attacked with the ASR, the target phrases' word error rate is high.

</details>

### [PhyAug: Physics-Directed Data Augmentation for Deep Sensing Model Transfer in Cyber-Physical Systems](2104.01160.md)
**Wenjie Luo, Zhenyu Yan, Qun Song, Rui Tan** · 2021-03-31

<details>
<summary>Abstract</summary>

Run-time domain shifts from training-phase domains are common in sensing systems designed with deep learning. The shifts can be caused by sensor characteristic variations and/or discrepancies between the design-phase model and the actual model of the sensed physical process. To address these issues, existing transfer learning techniques require substantial target-domain data and thus incur high post-deployment overhead. This paper proposes to exploit the first principle governing the domain shift to reduce the demand on target-domain data. Specifically, our proposed approach called PhyAug uses the first principle fitted with few labeled or unlabeled source/target-domain data pairs to transform the existing source-domain training data into augmented data for updating the deep neural networks. In two case studies of keyword spotting and DeepSpeech2-based automatic speech recognition, with 5-second unlabeled data collected from the target microphones, PhyAug recovers the recognition accuracy losses due to microphone characteristic variations by 37% to 72%. In a case study of seismic source localization with TDoA fngerprints, by exploiting the frst principle of signal propagation in uneven media, PhyAug only requires 3% to 8% of labeled TDoA measurements required by the vanilla fingerprinting approach in achieving the same localization accuracy.

</details>

### [Integer-only Zero-shot Quantization for Efficient Speech Recognition](2103.16827.md)
**Sehoon Kim, Amir Gholami, Zhewei Yao, Nicholas Lee et al.** · 2021-03-31

<details>
<summary>Abstract</summary>

End-to-end neural network models achieve improved performance on various automatic speech recognition (ASR) tasks. However, these models perform poorly on edge hardware due to large memory and computation requirements. While quantizing model weights and/or activations to low-precision can be a promising solution, previous research on quantizing ASR models is limited. In particular, the previous approaches use floating-point arithmetic during inference and thus they cannot fully exploit efficient integer processing units. Moreover, they require training and/or validation data during quantization, which may not be available due to security or privacy concerns. To address these limitations, we propose an integer-only, zero-shot quantization scheme for ASR models. In particular, we generate synthetic data whose runtime statistics resemble the real data, and we use it to calibrate models during quantization. We apply our method to quantize QuartzNet, Jasper, and Conformer and show negligible WER degradation as compared to the full-precision baseline models, even without using any data. Moreover, we achieve up to 2.35x speedup on a T4 GPU and 4x compression rate, with a modest WER degradation of <1% with INT8 quantization.

</details>

### [Large-Scale Pre-Training of End-to-End Multi-Talker ASR for Meeting Transcription with Single Distant Microphone](2103.16776.md)
**Naoyuki Kanda, Guoli Ye, Yu Wu, Yashesh Gaur et al.** · 2021-03-31

<details>
<summary>Abstract</summary>

Transcribing meetings containing overlapped speech with only a single distant microphone (SDM) has been one of the most challenging problems for automatic speech recognition (ASR). While various approaches have been proposed, all previous studies on the monaural overlapped speech recognition problem were based on either simulation data or small-scale real data. In this paper, we extensively investigate a two-step approach where we first pre-train a serialized output training (SOT)-based multi-talker ASR by using large-scale simulation data and then fine-tune the model with a small amount of real meeting data. Experiments are conducted by utilizing 75 thousand (K) hours of our internal single-talker recording to simulate a total of 900K hours of multi-talker audio segments for supervised pre-training. With fine-tuning on the 70 hours of the AMI-SDM training data, our SOT ASR model achieves a word error rate (WER) of 21.2% for the AMI-SDM evaluation set while automatically counting speakers in each test segment. This result is not only significantly better than the previous state-of-the-art WER of 36.4% with oracle utterance boundary information but also better than a result by a similarly fine-tuned single-talker ASR model applied to beamformed audio.

</details>

### [A study of latent monotonic attention variants](2103.16710.md)
**Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2021-03-30

<details>
<summary>Abstract</summary>

End-to-end models reach state-of-the-art performance for speech recognition, but global soft attention is not monotonic, which might lead to convergence problems, to instability, to bad generalisation, cannot be used for online streaming, and is also inefficient in calculation. Monotonicity can potentially fix all of this. There are several ad-hoc solutions or heuristics to introduce monotonicity, but a principled introduction is rarely found in literature so far. In this paper, we present a mathematically clean solution to introduce monotonicity, by introducing a new latent variable which represents the audio position or segment boundaries. We compare several monotonic latent models to our global soft attention baseline such as a hard attention model, a local windowed soft attention model, and a segmental soft attention model. We can show that our monotonic models perform as good as the global soft attention model. We perform our experiments on Switchboard 300h. We carefully outline the details of our training and release our code and configs.

</details>

### [Pre-training for low resource speech-to-intent applications](2103.16674.md)
**Pu Wang, Hugo Van hamme** · 2021-03-30

<details>
<summary>Abstract</summary>

Designing a speech-to-intent (S2I) agent which maps the users' spoken commands to the agents' desired task actions can be challenging due to the diverse grammatical and lexical preference of different users. As a remedy, we discuss a user-taught S2I system in this paper. The user-taught system learns from scratch from the users' spoken input with action demonstration, which ensure it is fully matched to the users' way of formulating intents and their articulation habits. The main issue is the scarce training data due to the user effort involved. Existing state-of-art approaches in this setting are based on non-negative matrix factorization (NMF) and capsule networks. In this paper we combine the encoder of an end-to-end ASR system with the prior NMF/capsule network-based user-taught decoder, and investigate whether pre-training methodology can reduce training data requirements for the NMF and capsule network. Experimental results show the pre-trained ASR-NMF framework significantly outperforms other models, and also, we discuss limitations of pre-training with different types of command-and-control(C&C) applications.

</details>

### [Transformer-based end-to-end speech recognition with residual Gaussian-based self-attention](2103.15722.md)
**Chengdong Liang, Menglong Xu, Xiao-Lei Zhang** · 2021-03-29

<details>
<summary>Abstract</summary>

Self-attention (SA), which encodes vector sequences according to their pairwise similarity, is widely used in speech recognition due to its strong context modeling ability. However, when applied to long sequence data, its accuracy is reduced. This is caused by the fact that its weighted average operator may lead to the dispersion of the attention distribution, which results in the relationship between adjacent signals ignored. To address this issue, in this paper, we introduce relative-position-awareness self-attention (RPSA). It not only maintains the global-range dependency modeling ability of self-attention, but also improves the localness modeling ability. Because the local window length of the original RPSA is fixed and sensitive to different test data, here we propose Gaussian-based self-attention (GSA) whose window length is learnable and adaptive to the test data automatically. We further generalize GSA to a new residual Gaussian self-attention (resGSA) for the performance improvement. We apply RPSA, GSA, and resGSA to Transformer-based speech recognition respectively. Experimental results on the AISHELL-1 Mandarin speech recognition corpus demonstrate the effectiveness of the proposed methods. For example, the resGSA-Transformer achieves a character error rate (CER) of 5.86% on the test set, which is relative 7.8% lower than that of the SA-Transformer. Although the performance of the proposed resGSA-Transformer is only slightly better than that of the RPSA-Transformer, it does not have to tune the window length manually.

</details>

### [Multiple-hypothesis CTC-based semi-supervised adaptation of end-to-end speech recognition](2103.15515.md)
**Cong-Thanh Do, Rama Doddipatla, Thomas Hain** · 2021-03-29

<details>
<summary>Abstract</summary>

This paper proposes an adaptation method for end-to-end speech recognition. In this method, multiple automatic speech recognition (ASR) 1-best hypotheses are integrated in the computation of the connectionist temporal classification (CTC) loss function. The integration of multiple ASR hypotheses helps alleviating the impact of errors in the ASR hypotheses to the computation of the CTC loss when ASR hypotheses are used. When being applied in semi-supervised adaptation scenarios where part of the adaptation data do not have labels, the CTC loss of the proposed method is computed from different ASR 1-best hypotheses obtained by decoding the unlabeled adaptation data. Experiments are performed in clean and multi-condition training scenarios where the CTC-based end-to-end ASR systems are trained on Wall Street Journal (WSJ) clean training data and CHiME-4 multi-condition training data, respectively, and tested on Aurora-4 test data. The proposed adaptation method yields 6.6% and 5.8% relative word error rate (WER) reductions in clean and multi-condition training scenarios, respectively, compared to a baseline system which is adapted with part of the adaptation data having manual transcriptions using back-propagation fine-tuning.

</details>

### [Scaling sparsemax based channel selection for speech recognition with ad-hoc microphone arrays](2103.15305.md)
**Junqi Chen, Xiao-Lei Zhang** · 2021-03-29

<details>
<summary>Abstract</summary>

Recently, speech recognition with ad-hoc microphone arrays has received much attention. It is known that channel selection is an important problem of ad-hoc microphone arrays, however, this topic seems far from explored in speech recognition yet, particularly with a large-scale ad-hoc microphone array. To address this problem, we propose a Scaling Sparsemax algorithm for the channel selection problem of the speech recognition with large-scale ad-hoc microphone arrays. Specifically, we first replace the conventional Softmax operator in the stream attention mechanism of a multichannel end-to-end speech recognition system with Sparsemax, which conducts channel selection by forcing the channel weights of noisy channels to zero. Because Sparsemax punishes the weights of many channels to zero harshly, we propose Scaling Sparsemax which punishes the channels mildly by setting the weights of very noisy channels to zero only. Experimental results with ad-hoc microphone arrays of over 30 channels under the conformer speech recognition architecture show that the proposed Scaling Sparsemax yields a word error rate of over 30% lower than Softmax on simulation data sets, and over 20% lower on semi-real data sets, in test scenarios with both matched and mismatched channel numbers.

</details>

### [Leveraging pre-trained representations to improve access to untranscribed speech from endangered languages](2103.14583.md)
**Nay San, Martijn Bartelds, Mitchell Browne, Lily Clifford et al.** · 2021-03-26

<details>
<summary>Abstract</summary>

Pre-trained speech representations like wav2vec 2.0 are a powerful tool for automatic speech recognition (ASR). Yet many endangered languages lack sufficient data for pre-training such models, or are predominantly oral vernaculars without a standardised writing system, precluding fine-tuning. Query-by-example spoken term detection (QbE-STD) offers an alternative for iteratively indexing untranscribed speech corpora by locating spoken query terms. Using data from 7 Australian Aboriginal languages and a regional variety of Dutch, all of which are endangered or vulnerable, we show that QbE-STD can be improved by leveraging representations developed for ASR (wav2vec 2.0: the English monolingual model and XLSR53 multilingual model). Surprisingly, the English model outperformed the multilingual model on 4 Australian language datasets, raising questions around how to optimally leverage self-supervised speech representations for QbE-STD. Nevertheless, we find that wav2vec 2.0 representations (either English or XLSR53) offer large improvements (56-86% relative) over state-of-the-art approaches on our endangered language datasets.

</details>

### [Mutually-Constrained Monotonic Multihead Attention for Online ASR](2103.14302.md)
**Jaeyun Song, Hajin Shim, Eunho Yang** · 2021-03-26

<details>
<summary>Abstract</summary>

Despite the feature of real-time decoding, Monotonic Multihead Attention (MMA) shows comparable performance to the state-of-the-art offline methods in machine translation and automatic speech recognition (ASR) tasks. However, the latency of MMA is still a major issue in ASR and should be combined with a technique that can reduce the test latency at inference time, such as head-synchronous beam search decoding, which forces all non-activated heads to activate after a small fixed delay from the first head activation. In this paper, we remove the discrepancy between training and test phases by considering, in the training of MMA, the interactions across multiple heads that will occur in the test time. Specifically, we derive the expected alignments from monotonic attention by considering the boundaries of other heads and reflect them in the learning process. We validate our proposed method on the two standard benchmark datasets for ASR and show that our approach, MMA with the mutually-constrained heads from the training stage, provides better performance than baselines.

</details>

### [BART based semantic correction for Mandarin automatic speech recognition system](2104.05507.md)
**Yun Zhao, Xuerui Yang, Jinchao Wang, Yongyu Gao et al.** · 2021-03-26

<details>
<summary>Abstract</summary>

Although automatic speech recognition (ASR) systems achieved significantly improvements in recent years, spoken language recognition error occurs which can be easily spotted by human beings. Various language modeling techniques have been developed on post recognition tasks like semantic correction. In this paper, we propose a Transformer based semantic correction method with pretrained BART initialization, Experiments on 10000 hours Mandarin speech dataset show that character error rate (CER) can be effectively reduced by 21.7% relatively compared to our baseline ASR system. Expert evaluation demonstrates that actual improvement of our model surpasses what CER indicates.

</details>

### [Cyclic Defense GAN Against Speech Adversarial Attacks](2103.14717.md)
**Mohammad Esmaeilpour, Patrick Cardinal, Alessandro Lameiras Koerich** · 2021-03-26

<details>
<summary>Abstract</summary>

This paper proposes a new defense approach for counteracting state-of-the-art white and black-box adversarial attack algorithms. Our approach fits into the implicit reactive defense algorithm category since it does not directly manipulate the potentially malicious input signals. Instead, it reconstructs a similar signal with a synthesized spectrogram using a cyclic generative adversarial network. This cyclic framework helps to yield a stable generative model. Finally, we feed the reconstructed signal into the speech-to-text model for transcription. The conducted experiments on targeted and non-targeted adversarial attacks developed for attacking DeepSpeech, Kaldi, and Lingvo models demonstrate the proposed defense's effectiveness in adverse scenarios.

</details>

### [Correcting Automated and Manual Speech Transcription Errors using Warped Language Models](2103.14580.md)
**Mahdi Namazifar, John Malik, Li Erran Li, Gokhan Tur et al.** · 2021-03-26

<details>
<summary>Abstract</summary>

Masked language models have revolutionized natural language processing systems in the past few years. A recently introduced generalization of masked language models called warped language models are trained to be more robust to the types of errors that appear in automatic or manual transcriptions of spoken language by exposing the language model to the same types of errors during training. In this work we propose a novel approach that takes advantage of the robustness of warped language models to transcription noise for correcting transcriptions of spoken language. We show that our proposed approach is able to achieve up to 10% reduction in word error rates of both automatic and manual transcriptions of spoken language.

</details>

### [Residual Energy-Based Models for End-to-End Speech Recognition](2103.14152.md)
**Qiujia Li, Yu Zhang, Bo Li, Liangliang Cao et al.** · 2021-03-25

<details>
<summary>Abstract</summary>

End-to-end models with auto-regressive decoders have shown impressive results for automatic speech recognition (ASR). These models formulate the sequence-level probability as a product of the conditional probabilities of all individual tokens given their histories. However, the performance of locally normalised models can be sub-optimal because of factors such as exposure bias. Consequently, the model distribution differs from the underlying data distribution. In this paper, the residual energy-based model (R-EBM) is proposed to complement the auto-regressive ASR model to close the gap between the two distributions. Meanwhile, R-EBMs can also be regarded as utterance-level confidence estimators, which may benefit many downstream tasks. Experiments on a 100hr LibriSpeech dataset show that R-EBMs can reduce the word error rates (WERs) by 8.2%/6.7% while improving areas under precision-recall curves of confidence scores by 12.6%/28.4% on test-clean/test-other sets. Furthermore, on a state-of-the-art model using self-supervised learning (wav2vec 2.0), R-EBMs still significantly improves both the WER and confidence estimation performance.

</details>

### [Radically Old Way of Computing Spectra: Applications in End-to-End ASR](2103.14129.md)
**Samik Sadhu, Hynek Hermansky** · 2021-03-25

<details>
<summary>Abstract</summary>

We propose a technique to compute spectrograms using Frequency Domain Linear Prediction (FDLP) that uses all-pole models to fit the squared Hilbert envelope of speech in different frequency sub-bands. The spectrogram of a complete speech utterance is computed by overlap-add of contiguous all-pole model responses. A long context window of 1.5 seconds allows us to capture the low frequency temporal modulations of speech in the spectrogram. For an end-to-end automatic speech recognition task, the FDLP spectrogram performs on par with the standard mel spectrogram features for clean read speech training and test data. For more realistic speech data with train-test domain mismatches or reverberations, FDLP spectrogram shows up to 25% and 22% relative WER improvements over mel spectrogram respectively.

</details>

### [Real-time low-resource phoneme recognition on edge devices](2103.13997.md)
**Yonatan Alon** · 2021-03-25

<details>
<summary>Abstract</summary>

While speech recognition has seen a surge in interest and research over the last decade, most machine learning models for speech recognition either require large training datasets or lots of storage and memory. Combined with the prominence of English as the number one language in which audio data is available, this means most other languages currently lack good speech recognition models. The method presented in this paper shows how to create and train models for speech recognition in any language which are not only highly accurate, but also require very little storage, memory and training data when compared with traditional models. This allows training models to recognize any language and deploying them on edge devices such as mobile phones or car displays for fast real-time speech recognition.

</details>

### [An Approach to Improve Robustness of NLP Systems against ASR Errors](2103.13610.md)
**Tong Cui, Jinghui Xiao, Liangyou Li, Xin Jiang et al.** · 2021-03-25

<details>
<summary>Abstract</summary>

Speech-enabled systems typically first convert audio to text through an automatic speech recognition (ASR) model and then feed the text to downstream natural language processing (NLP) modules. The errors of the ASR system can seriously downgrade the performance of the NLP modules. Therefore, it is essential to make them robust to the ASR errors. Previous work has shown it is effective to employ data augmentation methods to solve this problem by injecting ASR noise during the training process. In this paper, we utilize the prevalent pre-trained language model to generate training samples with ASR-plausible noise. Compare to the previous methods, our approach generates ASR noise that better fits the real-world error distribution. Experimental results on spoken language translation(SLT) and spoken language understanding (SLU) show that our approach effectively improves the system robustness against the ASR errors and achieves state-of-the-art results on both tasks.

</details>

### [MLLP-VRAIN Spanish ASR Systems for the Albayzin-RTVE 2020 Speech-To-Text Challenge](s2:82241d2062ffef8e99f4d5e22b5ce690c8f6a122.md)
**Javier Jorge, Adrià Giménez, Pau Baquero-Arnal, Javier Iranzo-Sánchez et al.** · 2021-03-24

<details>
<summary>Abstract</summary>

This paper describes the automatic speech recognition (ASR) systems built by the MLLP-VRAIN research group of Universitat Polit`ecnica de Val`encia for the Albayzin-RTVE 2020 Speech-to-Text Challenge. The primary system ( p-streaming 1500ms nlt ) was a hybrid BLSTM-HMM ASR system using streaming one-pass decoding with a context window of 1.5 seconds and a linear combination of an n-gram, a LSTM, and a Transformer language model (LM). The acoustic model was trained on nearly 4,000 hours of speech data from different sources, using the MLLP’s transLectures-UPV toolkit (TLK) and TensorFlow; whilst LMs were trained using SRILM (n-gram), CUED-RNNLM (LSTM), and Fairseq (Transformer), with up to 102G tokens. This system achieved 11.6% and 16.0% WER on the test-2018 and test-2020 sets, respectively. As it is streaming-enabled, it could be put into production environments for automatic captioning of live media streams, with a theoretical delay of 1.5 seconds. Along with the primary system, we also submitted three contrastive systems. From these, we highlight the system c2-streaming 600ms t that, following the same conﬁguration of the primary one, but using a smaller context window of 0.6 seconds and a Transformer LM, scored 12.3% and 16.9% WER points respectively on the same test sets, with a measured empirical latency of 0.81 ± 0.09 seconds (mean ± stdev). This is, we ob- tained state-of-the-art latencies for high-quality automatic live captioning with a small WER degradation of 6% relative.

</details>

### [Evolving Learning Rate Optimizers for Deep Neural Networks](2103.12623.md)
**Pedro Carvalho, Nuno Lourenço, Penousal Machado** · 2021-03-23

<details>
<summary>Abstract</summary>

Artificial Neural Networks (ANNs) became popular due to their successful application difficult problems such image and speech recognition. However, when practitioners want to design an ANN they need to undergo laborious process of selecting a set of parameters and topology. Currently, there are several state-of-the art methods that allow for the automatic selection of some of these aspects. Learning Rate optimizers are a set of such techniques that search for good values of learning rates. Whilst these techniques are effective and have yielded good results over the years, they are general solution i.e. they do not consider the characteristics of a specific network. We propose a framework called AutoLR to automatically design Learning Rate Optimizers. Two versions of the system are detailed. The first one, Dynamic AutoLR, evolves static and dynamic learning rate optimizers based on the current epoch and the previous learning rate. The second version, Adaptive AutoLR, evolves adaptive optimizers that can fine tune the learning rate for each network eeight which makes them generally more effective. The results are competitive with the best state of the art methods, even outperforming them in some scenarios. Furthermore, the system evolved a classifier, ADES, that appears to be novel and innovative since, to the best of our knowledge, it has a structure that differs from state of the art methods.

</details>

### [Hallucination of speech recognition errors with sequence to sequence learning](2103.12258.md)
**Prashant Serai, Vishal Sunder, Eric Fosler-Lussier** · 2021-03-23

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is an imperfect process that results in certain mismatches in ASR output text when compared to plain written text or transcriptions. When plain text data is to be used to train systems for spoken language understanding or ASR, a proven strategy to reduce said mismatch and prevent degradations, is to hallucinate what the ASR outputs would be given a gold transcription. Prior work in this domain has focused on modeling errors at the phonetic level, while using a lexicon to convert the phones to words, usually accompanied by an FST Language model. We present novel end-to-end models to directly predict hallucinated ASR word sequence outputs, conditioning on an input word sequence as well as a corresponding phoneme sequence. This improves prior published results for recall of errors from an in-domain ASR system's transcription of unseen data, as well as an out-of-domain ASR system's transcriptions of audio from an unrelated task, while additionally exploring an in-between scenario when limited characterization data from the test ASR system is obtainable. To verify the extrinsic validity of the method, we also use our hallucinated ASR errors to augment training for a spoken question classifier, finding that they enable robustness to real ASR errors in a downstream task, when scarce or even zero task-specific audio was available at train-time.

</details>

### [Contextual Biasing of Language Models for Speech Recognition in Goal-Oriented Conversational Agents](2103.10325.md)
**Ashish Shenoy, Sravan Bodapati, Katrin Kirchhoff** · 2021-03-18

<details>
<summary>Abstract</summary>

Goal-oriented conversational interfaces are designed to accomplish specific tasks and typically have interactions that tend to span multiple turns adhering to a pre-defined structure and a goal. However, conventional neural language models (NLM) in Automatic Speech Recognition (ASR) systems are mostly trained sentence-wise with limited context. In this paper, we explore different ways to incorporate context into a LSTM based NLM in order to model long range dependencies and improve speech recognition. Specifically, we use context carry over across multiple turns and use lexical contextual cues such as system dialog act from Natural Language Understanding (NLU) models and the user provided structure of the chatbot. We also propose a new architecture that utilizes context embeddings derived from BERT on sample utterances provided during inference time. Our experiments show a word error rate (WER) relative reduction of 7% over non-contextual utterance-level NLM rescorers on goal-oriented audio datasets.

</details>

### [Advancing RNN Transducer Technology for Speech Recognition](2103.09935.md)
**George Saon, Zoltan Tueske, Daniel Bolanos, Brian Kingsbury** · 2021-03-17

<details>
<summary>Abstract</summary>

We investigate a set of techniques for RNN Transducers (RNN-Ts) that were instrumental in lowering the word error rate on three different tasks (Switchboard 300 hours, conversational Spanish 780 hours and conversational Italian 900 hours). The techniques pertain to architectural changes, speaker adaptation, language model fusion, model combination and general training recipe. First, we introduce a novel multiplicative integration of the encoder and prediction network vectors in the joint network (as opposed to additive). Second, we discuss the applicability of i-vector speaker adaptation to RNN-Ts in conjunction with data perturbation. Third, we explore the effectiveness of the recently proposed density ratio language model fusion for these tasks. Last but not least, we describe the other components of our training recipe and their effect on recognition performance. We report a 5.9% and 12.5% word error rate on the Switchboard and CallHome test sets of the NIST Hub5 2000 evaluation and a 12.7% WER on the Mozilla CommonVoice Italian test set.

</details>

### [Transformer-based ASR Incorporating Time-reduction Layer and Fine-tuning with Self-Knowledge Distillation](2103.09903.md)
**Md Akmal Haidar, Chao Xing, Mehdi Rezagholizadeh** · 2021-03-17

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR), unlike conventional ASR, does not have modules to learn the semantic representation from speech encoder. Moreover, the higher frame-rate of speech representation prevents the model to learn the semantic representation properly. Therefore, the models that are constructed by the lower frame-rate of speech encoder lead to better performance. For Transformer-based ASR, the lower frame-rate is not only important for learning better semantic representation but also for reducing the computational complexity due to the self-attention mechanism which has O(n^2) order of complexity in both training and inference. In this paper, we propose a Transformer-based ASR model with the time reduction layer, in which we incorporate time reduction layer inside transformer encoder layers in addition to traditional sub-sampling methods to input features that further reduce the frame-rate. This can help in reducing the computational cost of the self-attention process for training and inference with performance improvement. Moreover, we introduce a fine-tuning approach for pre-trained ASR models using self-knowledge distillation (S-KD) which further improves the performance of our ASR model. Experiments on LibriSpeech datasets show that our proposed methods outperform all other Transformer-based ASR systems. Furthermore, with language model (LM) fusion, we achieve new state-of-the-art word error rate (WER) results for Transformer-based ASR models with just 30 million parameters trained without any external data.

</details>

### [An Asynchronous WFST-Based Decoder For Automatic Speech Recognition](2103.09063.md)
**Hang Lv, Zhehuai Chen, Hainan Xu, Daniel Povey et al.** · 2021-03-16

<details>
<summary>Abstract</summary>

We introduce asynchronous dynamic decoder, which adopts an efficient A* algorithm to incorporate big language models in the one-pass decoding for large vocabulary continuous speech recognition. Unlike standard one-pass decoding with on-the-fly composition decoder which might induce a significant computation overhead, the asynchronous dynamic decoder has a novel design where it has two fronts, with one performing "exploration" and the other "backfill". The computation of the two fronts alternates in the decoding process, resulting in more effective pruning than the standard one-pass decoding with an on-the-fly composition decoder. Experiments show that the proposed decoder works notably faster than the standard one-pass decoding with on-the-fly composition decoder, while the acceleration will be more obvious with the increment of data complexity.

</details>

### [Fast Development of ASR in African Languages using Self Supervised Speech Representation Learning](2103.08993.md)
**Jama Hussein Mohamud, Lloyd Acquaye Thompson, Aissatou Ndoye, Laurent Besacier** · 2021-03-16

<details>
<summary>Abstract</summary>

This paper describes the results of an informal collaboration launched during the African Master of Machine Intelligence (AMMI) in June 2020. After a series of lectures and labs on speech data collection using mobile applications and on self-supervised representation learning from speech, a small group of students and the lecturer continued working on automatic speech recognition (ASR) project for three languages: Wolof, Ga, and Somali. This paper describes how data was collected and ASR systems developed with a small amount (1h) of transcribed speech as training data. In these low resource conditions, pre-training a model on large amounts of raw speech was fundamental for the efficiency of ASR systems developed.

</details>

### [Distributed Deep Learning Using Volunteer Computing-Like Paradigm](2103.08894.md)
**Medha Atre, Birendra Jha, Ashwini Rao** · 2021-03-16

<details>
<summary>Abstract</summary>

Use of Deep Learning (DL) in commercial applications such as image classification, sentiment analysis and speech recognition is increasing. When training DL models with large number of parameters and/or large datasets, cost and speed of training can become prohibitive. Distributed DL training solutions that split a training job into subtasks and execute them over multiple nodes can decrease training time. However, the cost of current solutions, built predominantly for cluster computing systems, can still be an issue. In contrast to cluster computing systems, Volunteer Computing (VC) systems can lower the cost of computing, but applications running on VC systems have to handle fault tolerance, variable network latency and heterogeneity of compute nodes, and the current solutions are not designed to do so. We design a distributed solution that can run DL training on a VC system by using a data parallel approach. We implement a novel asynchronous SGD scheme called VC-ASGD suited for VC systems. In contrast to traditional VC systems that lower cost by using untrustworthy volunteer devices, we lower cost by leveraging preemptible computing instances on commercial cloud platforms. By using preemptible instances that require applications to be fault tolerant, we lower cost by 70-90% and improve data security.

</details>

### [XLST: Cross-lingual Self-training to Learn Multilingual Representation for Low Resource Speech Recognition](2103.08207.md)
**Zi-Qiang Zhang, Yan Song, Ming-Hui Wu, Xin Fang et al.** · 2021-03-15

<details>
<summary>Abstract</summary>

In this paper, we propose a weakly supervised multilingual representation learning framework, called cross-lingual self-training (XLST). XLST is able to utilize a small amount of annotated data from high-resource languages to improve the representation learning on multilingual un-annotated data. Specifically, XLST uses a supervised trained model to produce initial representations and another model to learn from them, by maximizing the similarity between output embeddings of these two models. Furthermore, the moving average mechanism and multi-view data augmentation are employed, which are experimentally shown to be crucial to XLST. Comprehensive experiments have been conducted on the CommonVoice corpus to evaluate the effectiveness of XLST. Results on 5 downstream low-resource ASR tasks shows that our multilingual pretrained model achieves relatively 18.6% PER reduction over the state-of-the-art self-supervised method, with leveraging additional 100 hours of annotated English data.

</details>

### [Multi-Discriminator Sobolev Defense-GAN Against Adversarial Attacks for End-to-End Speech Systems](2103.08086.md)
**Mohammad Esmaeilpour, Patrick Cardinal, Alessandro Lameiras Koerich** · 2021-03-15

<details>
<summary>Abstract</summary>

This paper introduces a defense approach against end-to-end adversarial attacks developed for cutting-edge speech-to-text systems. The proposed defense algorithm has four major steps. First, we represent speech signals with 2D spectrograms using the short-time Fourier transform. Second, we iteratively find a safe vector using a spectrogram subspace projection operation. This operation minimizes the chordal distance adjustment between spectrograms with an additional regularization term. Third, we synthesize a spectrogram with such a safe vector using a novel GAN architecture trained with Sobolev integral probability metric. To improve the model's performance in terms of stability and the total number of learned modes, we impose an additional constraint on the generator network. Finally, we reconstruct the signal from the synthesized spectrogram and the Griffin-Lim phase approximation technique. We evaluate the proposed defense approach against six strong white and black-box adversarial attacks benchmarked on DeepSpeech, Kaldi, and Lingvo models. Our experimental results show that our algorithm outperforms other state-of-the-art defense algorithms both in terms of accuracy and signal quality.

</details>

### [OkwuGbé: End-to-End Speech Recognition for Fon and Igbo](2103.07762.md)
**Bonaventure F. P. Dossou, Chris C. Emezue** · 2021-03-13

<details>
<summary>Abstract</summary>

Language is inherent and compulsory for human communication. Whether expressed in a written or spoken way, it ensures understanding between people of the same and different regions. With the growing awareness and effort to include more low-resourced languages in NLP research, African languages have recently been a major subject of research in machine translation, and other text-based areas of NLP. However, there is still very little comparable research in speech recognition for African languages. Interestingly, some of the unique properties of African languages affecting NLP, like their diacritical and tonal complexities, have a major root in their speech, suggesting that careful speech interpretation could provide more intuition on how to deal with the linguistic complexities of African languages for text-based NLP. OkwuGbé is a step towards building speech recognition systems for African low-resourced languages. Using Fon and Igbo as our case study, we conduct a comprehensive linguistic analysis of each language and describe the creation of end-to-end, deep neural network-based speech recognition models for both languages. We present a state-of-art ASR model for Fon, as well as benchmark ASR model results for Igbo. Our linguistic analyses (for Fon and Igbo) provide valuable insights and guidance into the creation of speech recognition models for other African low-resourced languages, as well as guide future NLP research for Fon and Igbo. The Fon and Igbo models source code have been made publicly available.

</details>

### [A Distributed Optimisation Framework Combining Natural Gradient with Hessian-Free for Discriminative Sequence Training](2103.07554.md)
**Adnan Haider, Chao Zhang, Florian L. Kreyssig, Philip C. Woodland** · 2021-03-12

<details>
<summary>Abstract</summary>

This paper presents a novel natural gradient and Hessian-free (NGHF) optimisation framework for neural network training that can operate efficiently in a distributed manner. It relies on the linear conjugate gradient (CG) algorithm to combine the natural gradient (NG) method with local curvature information from Hessian-free (HF) or other second-order methods. A solution to a numerical issue in CG allows effective parameter updates to be generated with far fewer CG iterations than usually used (e.g. 5-8 instead of 200). This work also presents a novel preconditioning approach to improve the progress made by individual CG iterations for models with shared parameters. Although applicable to other training losses and model structures, NGHF is investigated in this paper for lattice-based discriminative sequence training for hybrid hidden Markov model acoustic models using a standard recurrent neural network, long short-term memory, and time delay neural network models for output probability calculation. Automatic speech recognition experiments are reported on the multi-genre broadcast data set for a range of different acoustic model types. These experiments show that NGHF achieves larger word error rate reductions than standard stochastic gradient descent or Adam, while requiring orders of magnitude fewer parameter updates.

</details>

### [Dynamic Acoustic Unit Augmentation With BPE-Dropout for Low-Resource End-to-End Speech Recognition](2103.07186.md)
**Aleksandr Laptev, Andrei Andrusenko, Ivan Podluzhny, Anton Mitrofanov et al.** · 2021-03-12

<details>
<summary>Abstract</summary>

With the rapid development of speech assistants, adapting server-intended automatic speech recognition (ASR) solutions to a direct device has become crucial. Researchers and industry prefer to use end-to-end ASR systems for on-device speech recognition tasks. This is because end-to-end systems can be made resource-efficient while maintaining a higher quality compared to hybrid systems. However, building end-to-end models requires a significant amount of speech data. Another challenging task associated with speech assistants is personalization, which mainly lies in handling out-of-vocabulary (OOV) words. In this work, we consider building an effective end-to-end ASR system in low-resource setups with a high OOV rate, embodied in Babel Turkish and Babel Georgian tasks. To address the aforementioned problems, we propose a method of dynamic acoustic unit augmentation based on the BPE-dropout technique. It non-deterministically tokenizes utterances to extend the token's contexts and to regularize their distribution for the model's recognition of unseen words. It also reduces the need for optimal subword vocabulary size search. The technique provides a steady improvement in regular and personalized (OOV-oriented) speech recognition tasks (at least 6% relative WER and 25% relative F-score) at no additional computational cost. Owing to the use of BPE-dropout, our monolingual Turkish Conformer established a competitive result with 22.2% character error rate (CER) and 38.9% word error rate (WER), which is close to the best published multilingual system.

</details>

### [Learning Word-Level Confidence For Subword End-to-End ASR](2103.06716.md)
**David Qiu, Qiujia Li, Yanzhang He, Yu Zhang et al.** · 2021-03-11

<details>
<summary>Abstract</summary>

We study the problem of word-level confidence estimation in subword-based end-to-end (E2E) models for automatic speech recognition (ASR). Although prior works have proposed training auxiliary confidence models for ASR systems, they do not extend naturally to systems that operate on word-pieces (WP) as their vocabulary. In particular, ground truth WP correctness labels are needed for training confidence models, but the non-unique tokenization from word to WP causes inaccurate labels to be generated. This paper proposes and studies two confidence models of increasing complexity to solve this problem. The final model uses self-attention to directly learn word-level confidence without needing subword tokenization, and exploits full context features from multiple hypotheses to improve confidence accuracy. Experiments on Voice Search and long-tail test sets show standard metrics (e.g., NCE, AUC, RMSE) improving substantially. The proposed confidence module also enables a model selection approach to combine an on-device E2E model with a hybrid model on the server to address the rare word recognition problem for the E2E model.

</details>

### [Fine-tuning of Pre-trained End-to-end Speech Recognition with Generative Adversarial Networks](2103.13329.md)
**Md Akmal Haidar, Mehdi Rezagholizadeh** · 2021-03-10

<details>
<summary>Abstract</summary>

Adversarial training of end-to-end (E2E) ASR systems using generative adversarial networks (GAN) has recently been explored for low-resource ASR corpora. GANs help to learn the true data representation through a two-player min-max game. However, training an E2E ASR model using a large ASR corpus with a GAN framework has never been explored, because it might take excessively long time due to high-variance gradient updates and face convergence issues. In this paper, we introduce a novel framework for fine-tuning a pre-trained ASR model using the GAN objective where the ASR model acts as a generator and a discriminator tries to distinguish the ASR output from the real data. Since the ASR model is pre-trained, we hypothesize that the ASR model output (soft distribution vectors) helps to get higher scores from the discriminator and makes the task of the discriminator harder within our GAN framework, which in turn improves the performance of the ASR model in the fine-tuning stage. Here, the pre-trained ASR model is fine-tuned adversarially against the discriminator using an additional adversarial loss. Experiments on full LibriSpeech dataset show that our proposed approach outperforms baselines and conventional GAN-based adversarial models.

</details>

### [Best of Both Worlds: Robust Accented Speech Recognition with Adversarial Transfer Learning](2103.05834.md)
**Nilaksh Das, Sravan Bodapati, Monica Sunkara, Sundararajan Srinivasan et al.** · 2021-03-10

<details>
<summary>Abstract</summary>

Training deep neural networks for automatic speech recognition (ASR) requires large amounts of transcribed speech. This becomes a bottleneck for training robust models for accented speech which typically contains high variability in pronunciation and other semantics, since obtaining large amounts of annotated accented data is both tedious and costly. Often, we only have access to large amounts of unannotated speech from different accents. In this work, we leverage this unannotated data to provide semantic regularization to an ASR model that has been trained only on one accent, to improve its performance for multiple accents. We propose Accent Pre-Training (Acc-PT), a semi-supervised training strategy that combines transfer learning and adversarial training. Our approach improves the performance of a state-of-the-art ASR model by 33% on average over the baseline across multiple accents, training only on annotated samples from one standard accent, and as little as 105 minutes of unannotated speech from a target accent.

</details>

### [Contrastive Semi-supervised Learning for ASR](2103.05149.md)
**Alex Xiao, Christian Fuegen, Abdelrahman Mohamed** · 2021-03-09

<details>
<summary>Abstract</summary>

Pseudo-labeling is the most adopted method for pre-training automatic speech recognition (ASR) models. However, its performance suffers from the supervised teacher model's degrading quality in low-resource setups and under domain transfer. Inspired by the successes of contrastive representation learning for computer vision and speech applications, and more recently for supervised learning of visual objects, we propose Contrastive Semi-supervised Learning (CSL). CSL eschews directly predicting teacher-generated pseudo-labels in favor of utilizing them to select positive and negative examples. In the challenging task of transcribing public social media videos, using CSL reduces the WER by 8% compared to the standard Cross-Entropy pseudo-labeling (CE-PL) when 10hr of supervised data is used to annotate 75,000hr of videos. The WER reduction jumps to 19% under the ultra low-resource condition of using 1hr labels for teacher supervision. CSL generalizes much better in out-of-domain conditions, showing up to 17% WER reduction compared to the best CE-PL pre-trained model.

</details>

### [A Parallelizable Lattice Rescoring Strategy with Neural Language Models](2103.05081.md)
**Ke Li, Daniel Povey, Sanjeev Khudanpur** · 2021-03-08

<details>
<summary>Abstract</summary>

This paper proposes a parallel computation strategy and a posterior-based lattice expansion algorithm for efficient lattice rescoring with neural language models (LMs) for automatic speech recognition. First, lattices from first-pass decoding are expanded by the proposed posterior-based lattice expansion algorithm. Second, each expanded lattice is converted into a minimal list of hypotheses that covers every arc. Each hypothesis is constrained to be the best path for at least one arc it includes. For each lattice, the neural LM scores of the minimal list are computed in parallel and are then integrated back to the lattice in the rescoring stage. Experiments on the Switchboard dataset show that the proposed rescoring strategy obtains comparable recognition performance and generates more compact lattices than a competitive baseline method. Furthermore, the parallel rescoring method offers more flexibility by simplifying the integration of PyTorch-trained neural LMs for lattice rescoring with Kaldi.

</details>

### [Split Computing and Early Exiting for Deep Learning Applications: Survey and Research Challenges](2103.04505.md)
**Yoshitomo Matsubara, Marco Levorato, Francesco Restuccia** · 2021-03-08

<details>
<summary>Abstract</summary>

Mobile devices such as smartphones and autonomous vehicles increasingly rely on deep neural networks (DNNs) to execute complex inference tasks such as image classification and speech recognition, among others. However, continuously executing the entire DNN on mobile devices can quickly deplete their battery. Although task offloading to cloud/edge servers may decrease the mobile device's computational burden, erratic patterns in channel quality, network, and edge server load can lead to a significant delay in task execution. Recently, approaches based on split computing (SC) have been proposed, where the DNN is split into a head and a tail model, executed respectively on the mobile device and on the edge server. Ultimately, this may reduce bandwidth usage as well as energy consumption. Another approach, called early exiting (EE), trains models to embed multiple "exits" earlier in the architecture, each providing increasingly higher target accuracy. Therefore, the trade-off between accuracy and delay can be tuned according to the current conditions or application demands. In this paper, we provide a comprehensive survey of the state of the art in SC and EE strategies by presenting a comparison of the most relevant approaches. We conclude the paper by providing a set of compelling research challenges.

</details>

### [Neural model robustness for skill routing in large-scale conversational AI systems: A design choice exploration](2103.03373.md)
**Han Li, Sunghyun Park, Aswarth Dara, Jinseok Nam et al.** · 2021-03-04

<details>
<summary>Abstract</summary>

Current state-of-the-art large-scale conversational AI or intelligent digital assistant systems in industry comprises a set of components such as Automatic Speech Recognition (ASR) and Natural Language Understanding (NLU). For some of these systems that leverage a shared NLU ontology (e.g., a centralized intent/slot schema), there exists a separate skill routing component to correctly route a request to an appropriate skill, which is either a first-party or third-party application that actually executes on a user request. The skill routing component is needed as there are thousands of skills that can either subscribe to the same intent and/or subscribe to an intent under specific contextual conditions (e.g., device has a screen). Ensuring model robustness or resilience in the skill routing component is an important problem since skills may dynamically change their subscription in the ontology after the skill routing model has been deployed to production. We show how different modeling design choices impact the model robustness in the context of skill routing on a state-of-the-art commercial conversational AI system, specifically on the choices around data augmentation, model architecture, and optimization method. We show that applying data augmentation can be a very effective and practical way to drastically improve model robustness.

</details>

### [WaveGuard: Understanding and Mitigating Audio Adversarial Examples](2103.03344.md)
**Shehzeen Hussain, Paarth Neekhara, Shlomo Dubnov, Julian McAuley et al.** · 2021-03-04

<details>
<summary>Abstract</summary>

There has been a recent surge in adversarial attacks on deep learning based automatic speech recognition (ASR) systems. These attacks pose new challenges to deep learning security and have raised significant concerns in deploying ASR systems in safety-critical applications. In this work, we introduce WaveGuard: a framework for detecting adversarial inputs that are crafted to attack ASR systems. Our framework incorporates audio transformation functions and analyses the ASR transcriptions of the original and transformed audio to detect adversarial inputs. We demonstrate that our defense framework is able to reliably detect adversarial examples constructed by four recent audio adversarial attacks, with a variety of audio transformation functions. With careful regard for best practices in defense evaluations, we analyze our proposed defense and its strength to withstand adaptive and robust attacks in the audio domain. We empirically demonstrate that audio transformations that recover audio from perceptually informed representations can lead to a strong defense that is robust against an adaptive adversary even in a complete white-box setting. Furthermore, WaveGuard can be used out-of-the box and integrated directly with any ASR model to efficiently detect audio adversarial examples, without the need for model retraining.

</details>

### [Continuous Speech Separation with Ad Hoc Microphone Arrays](2103.02378.md)
**Dongmei Wang, Takuya Yoshioka, Zhuo Chen, Xiaofei Wang et al.** · 2021-03-03

<details>
<summary>Abstract</summary>

Speech separation has been shown effective for multi-talker speech recognition. Under the ad hoc microphone array setup where the array consists of spatially distributed asynchronous microphones, additional challenges must be overcome as the geometry and number of microphones are unknown beforehand. Prior studies show, with a spatial-temporalinterleaving structure, neural networks can efficiently utilize the multi-channel signals of the ad hoc array. In this paper, we further extend this approach to continuous speech separation. Several techniques are introduced to enable speech separation for real continuous recordings. First, we apply a transformer-based network for spatio-temporal modeling of the ad hoc array signals. In addition, two methods are proposed to mitigate a speech duplication problem during single talker segments, which seems more severe in the ad hoc array scenarios. One method is device distortion simulation for reducing the acoustic mismatch between simulated training data and real recordings. The other is speaker counting to detect the single speaker segments and merge the output signal channels. Experimental results for AdHoc-LibiCSS, a new dataset consisting of continuous recordings of concatenated LibriSpeech utterances obtained by multiple different devices, show the proposed separation method can significantly improve the ASR accuracy for overlapped speech with little performance degradation for single talker segments.

</details>

### [Incorporating VAD into ASR System by Multi-task Learning](2103.01661.md)
**Meng Li, Xia Yan, Feng Lin** · 2021-03-02

<details>
<summary>Abstract</summary>

When we use End-to-end automatic speech recognition (E2E-ASR) system for real-world applications, a voice activity detection (VAD) system is usually needed to improve the performance and to reduce the computational cost by discarding non-speech parts in the audio. Usually ASR and VAD systems are trained and utilized independently to each other. In this paper, we present a novel multi-task learning (MTL) framework that incorporates VAD into the ASR system. The proposed system learns ASR and VAD jointly in the training stage. With the assistance of VAD, the ASR performance improves as its connectionist temporal classification (CTC) loss function can leverage the VAD alignment information. In the inference stage, the proposed system removes non-speech parts at low computational cost and recognizes speech parts with high robustness. Experimental results on segmented speech data show that by utilizing VAD information, the proposed method outperforms the baseline ASR system on both English and Chinese datasets. On unsegmented speech data, we find that the system outperforms the ASR systems that build an extra GMM-based or DNN-based voice activity detector.

</details>

### [Alignment Knowledge Distillation for Online Streaming Attention-based Speech Recognition](2103.00422.md)
**Hirofumi Inaguma, Tatsuya Kawahara** · 2021-02-28

<details>
<summary>Abstract</summary>

This article describes an efficient training method for online streaming attention-based encoder-decoder (AED) automatic speech recognition (ASR) systems. AED models have achieved competitive performance in offline scenarios by jointly optimizing all components. They have recently been extended to an online streaming framework via models such as monotonic chunkwise attention (MoChA). However, the elaborate attention calculation process is not robust for long-form speech utterances. Moreover, the sequence-level training objective and time-restricted streaming encoder cause a nonnegligible delay in token emission during inference. To address these problems, we propose CTC synchronous training (CTC-ST), in which CTC alignments are leveraged as a reference for token boundaries to enable a MoChA model to learn optimal monotonic input-output alignments. We formulate a purely end-to-end training objective to synchronize the boundaries of MoChA to those of CTC. The CTC model shares an encoder with the MoChA model to enhance the encoder representation. Moreover, the proposed method provides alignment information learned in the CTC branch to the attention-based decoder. Therefore, CTC-ST can be regarded as self-distillation of alignment knowledge from CTC to MoChA. Experimental evaluations on a variety of benchmark datasets show that the proposed method significantly reduces recognition errors and emission latency simultaneously. The robustness to long-form and noisy speech is also demonstrated. We compare CTC-ST with several methods that distill alignment knowledge from a hybrid ASR system and show that the CTC-ST can achieve a comparable tradeoff of accuracy and latency without relying on external alignment information. The best MoChA system shows recognition accuracy comparable to that of RNN-transducer (RNN-T) while achieving lower emission latency.

</details>

### [Exploiting Attention-based Sequence-to-Sequence Architectures for Sound Event Localization](2103.00417.md)
**Christopher Schymura, Tsubasa Ochiai, Marc Delcroix, Keisuke Kinoshita et al.** · 2021-02-28

<details>
<summary>Abstract</summary>

Sound event localization frameworks based on deep neural networks have shown increased robustness with respect to reverberation and noise in comparison to classical parametric approaches. In particular, recurrent architectures that incorporate temporal context into the estimation process seem to be well-suited for this task. This paper proposes a novel approach to sound event localization by utilizing an attention-based sequence-to-sequence model. These types of models have been successfully applied to problems in natural language processing and automatic speech recognition. In this work, a multi-channel audio signal is encoded to a latent representation, which is subsequently decoded to a sequence of estimated directions-of-arrival. Herein, attentions allow for capturing temporal dependencies in the audio signal by focusing on specific frames that are relevant for estimating the activity and direction-of-arrival of sound events at the current time-step. The framework is evaluated on three publicly available datasets for sound event localization. It yields superior localization performance compared to state-of-the-art methods in both anechoic and reverberant conditions.

</details>

### [MixSpeech: Data Augmentation for Low-resource Automatic Speech Recognition](2102.12664.md)
**Linghui Meng, Jin Xu, Xu Tan, Jindong Wang et al.** · 2021-02-25

<details>
<summary>Abstract</summary>

In this paper, we propose MixSpeech, a simple yet effective data augmentation method based on mixup for automatic speech recognition (ASR). MixSpeech trains an ASR model by taking a weighted combination of two different speech features (e.g., mel-spectrograms or MFCC) as the input, and recognizing both text sequences, where the two recognition losses use the same combination weight. We apply MixSpeech on two popular end-to-end speech recognition models including LAS (Listen, Attend and Spell) and Transformer, and conduct experiments on several low-resource datasets including TIMIT, WSJ, and HKUST. Experimental results show that MixSpeech achieves better accuracy than the baseline models without data augmentation, and outperforms a strong data augmentation method SpecAugment on these recognition tasks. Specifically, MixSpeech outperforms SpecAugment with a relative PER improvement of 10.6$\%$ on TIMIT dataset, and achieves a strong WER of 4.7$\%$ on WSJ dataset.

</details>

### [Meta-Learning for improving rare word recognition in end-to-end ASR](2102.12624.md)
**Florian Lux, Ngoc Thang Vu** · 2021-02-25

<details>
<summary>Abstract</summary>

We propose a new method of generating meaningful embeddings for speech, changes to four commonly used meta learning approaches to enable them to perform keyword spotting in continuous signals and an approach of combining their outcomes into an end-to-end automatic speech recognition system to improve rare word recognition. We verify the functionality of each of our three contributions in two experiments exploring their performance for different amounts of classes (N-way) and examples per class (k-shot) in a few-shot setting. We find that the speech embeddings work well and the changes to the meta learning approaches also clearly enable them to perform continuous signal spotting. Despite the interface between keyword spotting and speech recognition being very simple, we are able to consistently improve word error rate by up to 5%.

</details>

### [Speech Enhancement Using Multi-Stage Self-Attentive Temporal Convolutional Networks](2102.12078.md)
**Ju Lin, Adriaan J. van Wijngaarden, Kuang-Ching Wang, Melissa C. Smith** · 2021-02-24

<details>
<summary>Abstract</summary>

Multi-stage learning is an effective technique to invoke multiple deep-learning modules sequentially. This paper applies multi-stage learning to speech enhancement by using a multi-stage structure, where each stage comprises a self-attention (SA) block followed by stacks of temporal convolutional network (TCN) blocks with doubling dilation factors. Each stage generates a prediction that is refined in a subsequent stage. A fusion block is inserted at the input of later stages to re-inject original information. The resulting multi-stage speech enhancement system, in short, multi-stage SA-TCN, is compared with state-of-the-art deep-learning speech enhancement methods using the LibriSpeech and VCTK data sets. The multi-stage SA-TCN system's hyper-parameters are fine-tuned, and the impact of the SA block, the fusion block and the number of stages are determined. The use of a multi-stage SA-TCN system as a front-end for automatic speech recognition systems is investigated as well. It is shown that the multi-stage SA-TCN systems perform well relative to other state-of-the-art systems in terms of speech enhancement and speech recognition scores.

</details>

### [Unidirectional Memory-Self-Attention Transducer for Online Speech Recognition](2102.11594.md)
**Jian Luo, Jianzong Wang, Ning Cheng, Jing Xiao** · 2021-02-23

<details>
<summary>Abstract</summary>

Self-attention models have been successfully applied in end-to-end speech recognition systems, which greatly improve the performance of recognition accuracy. However, such attention-based models cannot be used in online speech recognition, because these models usually have to utilize a whole acoustic sequences as inputs. A common method is restricting the field of attention sights by a fixed left and right window, which makes the computation costs manageable yet also introduces performance degradation. In this paper, we propose Memory-Self-Attention (MSA), which adds history information into the Restricted-Self-Attention unit. MSA only needs localtime features as inputs, and efficiently models long temporal contexts by attending memory states. Meanwhile, recurrent neural network transducer (RNN-T) has proved to be a great approach for online ASR tasks, because the alignments of RNN-T are local and monotonic. We propose a novel network structure, called Memory-Self-Attention (MSA) Transducer. Both encoder and decoder of the MSA Transducer contain the proposed MSA unit. The experiments demonstrate that our proposed models improve WER results than Restricted-Self-Attention models by $13.5 on WSJ and $7.1 on SWBD datasets relatively, and without much computation costs increase.

</details>

### [Data Fusion for Audiovisual Speaker Localization: Extending Dynamic Stream Weights to the Spatial Domain](2102.11588.md)
**Julio Wissing, Benedikt Boenninghoff, Dorothea Kolossa, Tsubasa Ochiai et al.** · 2021-02-23

<details>
<summary>Abstract</summary>

Estimating the positions of multiple speakers can be helpful for tasks like automatic speech recognition or speaker diarization. Both applications benefit from a known speaker position when, for instance, applying beamforming or assigning unique speaker identities. Recently, several approaches utilizing acoustic signals augmented with visual data have been proposed for this task. However, both the acoustic and the visual modality may be corrupted in specific spatial regions, for instance due to poor lighting conditions or to the presence of background noise. This paper proposes a novel audiovisual data fusion framework for speaker localization by assigning individual dynamic stream weights to specific regions in the localization space. This fusion is achieved via a neural network, which combines the predictions of individual audio and video trackers based on their time- and location-dependent reliability. A performance evaluation using audiovisual recordings yields promising results, with the proposed fusion approach outperforming all baseline models.

</details>

### [End-to-End Dereverberation, Beamforming, and Speech Recognition with Improved Numerical Stability and Advanced Frontend](2102.11525.md)
**Wangyou Zhang, Christoph Boeddeker, Shinji Watanabe, Tomohiro Nakatani et al.** · 2021-02-23

<details>
<summary>Abstract</summary>

Recently, the end-to-end approach has been successfully applied to multi-speaker speech separation and recognition in both single-channel and multichannel conditions. However, severe performance degradation is still observed in the reverberant and noisy scenarios, and there is still a large performance gap between anechoic and reverberant conditions. In this work, we focus on the multichannel multi-speaker reverberant condition, and propose to extend our previous framework for end-to-end dereverberation, beamforming, and speech recognition with improved numerical stability and advanced frontend subnetworks including voice activity detection like masks. The techniques significantly stabilize the end-to-end training process. The experiments on the spatialized wsj1-2mix corpus show that the proposed system achieves about 35% WER relative reduction compared to our conventional multi-channel E2E ASR system, and also obtains decent speech dereverberation and separation performance (SDR=12.5 dB) in the reverberant multi-speaker condition while trained only with the ASR criterion.

</details>

### [Evolutionary optimization of contexts for phonetic correction in speech recognition systems](2102.11480.md)
**Rafael Viana-Cámara, Diego Campos-Sobrino, Mario Campos-Soberanis** · 2021-02-23

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is an area of growing academic and commercial interest due to the high demand for applications that use it to provide a natural communication method. It is common for general purpose ASR systems to fail in applications that use a domain-specific language. Various strategies have been used to reduce the error, such as providing a context that modifies the language model and post-processing correction methods. This article explores the use of an evolutionary process to generate an optimized context for a specific application domain, as well as different correction techniques based on phonetic distance metrics. The results show the viability of a genetic algorithm as a tool for context optimization, which, added to a post-processing correction based on phonetic representations, can reduce the errors on the recognized speech.

</details>

### [Generating Human Readable Transcript for Automatic Speech Recognition with Pre-trained Language Model](2102.11114.md)
**Junwei Liao, Yu Shi, Ming Gong, Linjun Shou et al.** · 2021-02-22

<details>
<summary>Abstract</summary>

Modern Automatic Speech Recognition (ASR) systems can achieve high performance in terms of recognition accuracy. However, a perfectly accurate transcript still can be challenging to read due to disfluency, filter words, and other errata common in spoken communication. Many downstream tasks and human readers rely on the output of the ASR system; therefore, errors introduced by the speaker and ASR system alike will be propagated to the next task in the pipeline. In this work, we propose an ASR post-processing model that aims to transform the incorrect and noisy ASR output into a readable text for humans and downstream tasks. We leverage the Metadata Extraction (MDE) corpus to construct a task-specific dataset for our study. Since the dataset is small, we propose a novel data augmentation method and use a two-stage training strategy to fine-tune the RoBERTa pre-trained model. On the constructed test set, our model outperforms a production two-step pipeline-based post-processing method by a large margin of 13.26 on readability-aware WER (RA-WER) and 17.53 on BLEU metrics. Human evaluation also demonstrates that our method can generate more human-readable transcripts than the baseline method.

</details>

### [The Use of Voice Source Features for Sung Speech Recognition](2102.10376.md)
**Gerardo Roa Dabike, Jon Barker** · 2021-02-20

<details>
<summary>Abstract</summary>

In this paper, we ask whether vocal source features (pitch, shimmer, jitter, etc) can improve the performance of automatic sung speech recognition, arguing that conclusions previously drawn from spoken speech studies may not be valid in the sung speech domain. We first use a parallel singing/speaking corpus (NUS-48E) to illustrate differences in sung vs spoken voicing characteristics including pitch range, syllables duration, vibrato, jitter and shimmer. We then use this analysis to inform speech recognition experiments on the sung speech DSing corpus, using a state of the art acoustic model and augmenting conventional features with various voice source parameters. Experiments are run with three standard (increasingly large) training sets, DSing1 (15.1 hours), DSing3 (44.7 hours) and DSing30 (149.1 hours). Pitch combined with degree of voicing produces a significant decrease in WER from 38.1% to 36.7% when training with DSing1 however smaller decreases in WER observed when training with the larger more varied DSing3 and DSing30 sets were not seen to be statistically significant. Voicing quality characteristics did not improve recognition performance although analysis suggests that they do contribute to an improved discrimination between voiced/unvoiced phoneme pairs.

</details>

### [End-to-End Neural Systems for Automatic Children Speech Recognition: An Empirical Study](2102.09918.md)
**Prashanth Gurunath Shivakumar, Shrikanth Narayanan** · 2021-02-19

<details>
<summary>Abstract</summary>

A key desiderata for inclusive and accessible speech recognition technology is ensuring its robust performance to children's speech. Notably, this includes the rapidly advancing neural network based end-to-end speech recognition systems. Children speech recognition is more challenging due to the larger intra-inter speaker variability in terms of acoustic and linguistic characteristics compared to adult speech. Furthermore, the lack of adequate and appropriate children speech resources adds to the challenge of designing robust end-to-end neural architectures. This study provides a critical assessment of automatic children speech recognition through an empirical study of contemporary state-of-the-art end-to-end speech recognition systems. Insights are provided on the aspects of training data requirements, adaptation on children data, and the effect of children age, utterance lengths, different architectures and loss functions for end-to-end systems and role of language models on the speech recognition performance.

</details>

### [Fixing Errors of the Google Voice Recognizer through Phonetic Distance Metrics](2102.09680.md)
**Diego Campos-Sobrino, Mario Campos-Soberanis, Iván Martínez-Chin, Víctor Uc-Cetina** · 2021-02-18

<details>
<summary>Abstract</summary>

Speech recognition systems for the Spanish language, such as Google's, produce errors quite frequently when used in applications of a specific domain. These errors mostly occur when recognizing words new to the recognizer's language model or ad hoc to the domain. This article presents an algorithm that uses Levenshtein distance on phonemes to reduce the speech recognizer's errors. The preliminary results show that it is possible to correct the recognizer's errors significantly by using this metric and using a dictionary of specific phrases from the domain of the application. Despite being designed for particular domains, the algorithm proposed here is of general application. The phrases that must be recognized can be explicitly defined for each application, without the algorithm having to be modified. It is enough to indicate to the algorithm the set of sentences on which it must work. The algorithm's complexity is $O(tn)$, where $t$ is the number of words in the transcript to be corrected, and $n$ is the number of phrases specific to the domain.

</details>

### [All-optical spiking neurosynaptic networks with self-learning capabilities](2102.09360.md)
**J. Feldmann, N. Youngblood, C. D. Wright, H. Bhaskaran et al.** · 2021-02-18

<details>
<summary>Abstract</summary>

Software-implementation, via neural networks, of brain-inspired computing approaches underlie many important modern-day computational tasks, from image processing to speech recognition, artificial intelligence and deep learning applications. Yet, differing from real neural tissue, traditional computing architectures physically separate the core computing functions of memory and processing, making fast, efficient and low-energy brain-like computing difficult to achieve. To overcome such limitations, an attractive and alternative goal is to design direct hardware mimics of brain neurons and synapses which, when connected in appropriate networks (or neuromorphic systems), process information in a way more fundamentally analogous to that of real brains. Here we present an all-optical approach to achieving such a goal. Specifically, we demonstrate an all-optical spiking neuron device and connect it, via an integrated photonics network, to photonic synapses to deliver a small-scale all-optical neurosynaptic system capable of supervised and unsupervised learning. Moreover, we exploit wavelength division multiplexing techniques to implement a scalable circuit architecture for photonic neural networks, successfully demonstrating pattern recognition directly in the optical domain using a photonic system comprising 140 elements. Such optical implementations of neurosynaptic networks promise access to the high speed and bandwidth inherent to optical systems, which would be very attractive for the direct processing of telecommunication and visual data in the optical domain.

</details>

### [Gaussian Kernelized Self-Attention for Long Sequence Data and Its Application to CTC-based Speech Recognition](2102.09168.md)
**Yosuke Kashiwagi, Emiru Tsunoo, Shinji Watanabe** · 2021-02-18

<details>
<summary>Abstract</summary>

Self-attention (SA) based models have recently achieved significant performance improvements in hybrid and end-to-end automatic speech recognition (ASR) systems owing to their flexible context modeling capability. However, it is also known that the accuracy degrades when applying SA to long sequence data. This is mainly due to the length mismatch between the inference and training data because the training data are usually divided into short segments for efficient training. To mitigate this mismatch, we propose a new architecture, which is a variant of the Gaussian kernel, which itself is a shift-invariant kernel. First, we mathematically demonstrate that self-attention with shared weight parameters for queries and keys is equivalent to a normalized kernel function. By replacing this kernel function with the proposed Gaussian kernel, the architecture becomes completely shift-invariant with the relative position information embedded using a frame indexing technique. The proposed Gaussian kernelized SA was applied to connectionist temporal classification (CTC) based ASR. An experimental evaluation with the Corpus of Spontaneous Japanese (CSJ) and TEDLIUM 3 benchmarks shows that the proposed SA achieves a significant improvement in accuracy (e.g., from 24.0% WER to 6.0% in CSJ) in long sequence data without any windowing techniques.

</details>

### [Echo State Speech Recognition](2102.09114.md)
**Harsh Shrivastava, Ankush Garg, Yuan Cao, Yu Zhang et al.** · 2021-02-18

<details>
<summary>Abstract</summary>

We propose automatic speech recognition (ASR) models inspired by echo state network (ESN), in which a subset of recurrent neural networks (RNN) layers in the models are randomly initialized and untrained. Our study focuses on RNN-T and Conformer models, and we show that model quality does not drop even when the decoder is fully randomized. Furthermore, such models can be trained more efficiently as the decoders do not require to be updated. By contrast, randomizing encoders hurts model quality, indicating that optimizing encoders and learn proper representations for acoustic inputs are more vital for speech recognition. Overall, we challenge the common practice of training ASR models for all components, and demonstrate that ESN-based models can perform equally well but enable more efficient training and storage than fully-trainable counterparts.

</details>

### [Fundamental Frequency Feature Normalization and Data Augmentation for Child Speech Recognition](2102.09106.md)
**Gary Yeung, Ruchao Fan, Abeer Alwan** · 2021-02-18

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems for young children are needed due to the importance of age-appropriate educational technology. Because of the lack of publicly available young child speech data, feature extraction strategies such as feature normalization and data augmentation must be considered to successfully train child ASR systems. This study proposes a novel technique for child ASR using both feature normalization and data augmentation methods based on the relationship between formants and fundamental frequency ($f_o$). Both the $f_o$ feature normalization and data augmentation techniques are implemented as a frequency shift in the Mel domain. These techniques are evaluated on a child read speech ASR task. Child ASR systems are trained by adapting a BLSTM-based acoustic model trained on adult speech. Using both $f_o$ normalization and data augmentation results in a relative word error rate (WER) improvement of 19.3% over the baseline when tested on the OGI Kids' Speech Corpus, and the resulting child ASR system achieves the best WER currently reported on this corpus.

</details>

### [Do End-to-End Speech Recognition Models Care About Context?](2102.09928.md)
**Lasse Borgholt, Jakob Drachmann Havtorn, Željko Agić, Anders Søgaard et al.** · 2021-02-17

<details>
<summary>Abstract</summary>

The two most common paradigms for end-to-end speech recognition are connectionist temporal classification (CTC) and attention-based encoder-decoder (AED) models. It has been argued that the latter is better suited for learning an implicit language model. We test this hypothesis by measuring temporal context sensitivity and evaluate how the models perform when we constrain the amount of contextual information in the audio input. We find that the AED model is indeed more context sensitive, but that the gap can be closed by adding self-attention to the CTC model. Furthermore, the two models perform similarly when contextual information is constrained. Finally, in contrast to previous research, our results show that the CTC model is highly competitive on WSJ and LibriSpeech without the help of an external language model.

</details>

### [ATCSpeechNet: A multilingual end-to-end speech recognition framework for air traffic control systems](2102.08535.md)
**Yi Lin, Bo Yang, Linchao Li, Dongyue Guo et al.** · 2021-02-17

<details>
<summary>Abstract</summary>

In this paper, a multilingual end-to-end framework, called as ATCSpeechNet, is proposed to tackle the issue of translating communication speech into human-readable text in air traffic control (ATC) systems. In the proposed framework, we focus on integrating the multilingual automatic speech recognition (ASR) into one model, in which an end-to-end paradigm is developed to convert speech waveform into text directly, without any feature engineering or lexicon. In order to make up for the deficiency of the handcrafted feature engineering caused by ATC challenges, a speech representation learning (SRL) network is proposed to capture robust and discriminative speech representations from the raw wave. The self-supervised training strategy is adopted to optimize the SRL network from unlabeled data, and further to predict the speech features, i.e., wave-to-feature. An end-to-end architecture is improved to complete the ASR task, in which a grapheme-based modeling unit is applied to address the multilingual ASR issue. Facing the problem of small transcribed samples in the ATC domain, an unsupervised approach with mask prediction is applied to pre-train the backbone network of the ASR model on unlabeled data by a feature-to-feature process. Finally, by integrating the SRL with ASR, an end-to-end multilingual ASR framework is formulated in a supervised manner, which is able to translate the raw wave into text in one model, i.e., wave-to-text. Experimental results on the ATCSpeech corpus demonstrate that the proposed approach achieves a high performance with a very small labeled corpus and less resource consumption, only 4.20% label error rate on the 58-hour transcribed corpus. Compared to the baseline model, the proposed approach obtains over 100% relative performance improvement which can be further enhanced with the increasing of the size of the transcribed samples.

</details>

### [End-to-End Automatic Speech Recognition with Deep Mutual Learning](2102.08154.md)
**Ryo Masumura, Mana Ihori, Akihiko Takashima, Tomohiro Tanaka et al.** · 2021-02-16

<details>
<summary>Abstract</summary>

This paper is the first study to apply deep mutual learning (DML) to end-to-end ASR models. In DML, multiple models are trained simultaneously and collaboratively by mimicking each other throughout the training process, which helps to attain the global optimum and prevent models from making over-confident predictions. While previous studies applied DML to simple multi-class classification problems, there are no studies that have used it on more complex sequence-to-sequence mapping problems. For this reason, this paper presents a method to apply DML to state-of-the-art Transformer-based end-to-end ASR models. In particular, we propose to combine DML with recent representative training techniques. i.e., label smoothing, scheduled sampling, and SpecAugment, each of which are essential for powerful end-to-end ASR models. We expect that these training techniques work well with DML because DML has complementary characteristics. We experimented with two setups for Japanese ASR tasks: large-scale modeling and compact modeling. We demonstrate that DML improves the ASR performance of both modeling setups compared with conventional learning methods including knowledge distillation. We also show that combining DML with the existing training techniques effectively improves ASR performance.

</details>

### [Improving speech recognition models with small samples for air traffic control systems](2102.08015.md)
**Yi Lin, Qin Li, Bo Yang, Zhen Yan et al.** · 2021-02-16

<details>
<summary>Abstract</summary>

In the domain of air traffic control (ATC) systems, efforts to train a practical automatic speech recognition (ASR) model always faces the problem of small training samples since the collection and annotation of speech samples are expert- and domain-dependent task. In this work, a novel training approach based on pretraining and transfer learning is proposed to address this issue, and an improved end-to-end deep learning model is developed to address the specific challenges of ASR in the ATC domain. An unsupervised pretraining strategy is first proposed to learn speech representations from unlabeled samples for a certain dataset. Specifically, a masking strategy is applied to improve the diversity of the sample without losing their general patterns. Subsequently, transfer learning is applied to fine-tune a pretrained or other optimized baseline models to finally achieves the supervised ASR task. By virtue of the common terminology used in the ATC domain, the transfer learning task can be regarded as a sub-domain adaption task, in which the transferred model is optimized using a joint corpus consisting of baseline samples and new transcribed samples from the target dataset. This joint corpus construction strategy enriches the size and diversity of the training samples, which is important for addressing the issue of the small transcribed corpus. In addition, speed perturbation is applied to augment the new transcribed samples to further improve the quality of the speech corpus. Three real ATC datasets are used to validate the proposed ASR model and training strategies. The experimental results demonstrate that the ASR performance is significantly improved on all three datasets, with an absolute character error rate only one-third of that achieved through the supervised training. The applicability of the proposed strategies to other ASR approaches is also validated.

</details>

### [Deep Learning based Multi-Source Localization with Source Splitting and its Effectiveness in Multi-Talker Speech Recognition](2102.07955.md)
**Aswin Shanmugam Subramanian, Chao Weng, Shinji Watanabe, Meng Yu et al.** · 2021-02-16

<details>
<summary>Abstract</summary>

Multi-source localization is an important and challenging technique for multi-talker conversation analysis. This paper proposes a novel supervised learning method using deep neural networks to estimate the direction of arrival (DOA) of all the speakers simultaneously from the audio mixture. At the heart of the proposal is a source splitting mechanism that creates source-specific intermediate representations inside the network. This allows our model to give source-specific posteriors as the output unlike the traditional multi-label classification approach. Existing deep learning methods perform a frame level prediction, whereas our approach performs an utterance level prediction by incorporating temporal selection and averaging inside the network to avoid post-processing. We also experiment with various loss functions and show that a variant of earth mover distance (EMD) is very effective in classifying DOA at a very high resolution by modeling inter-class relationships. In addition to using the prediction error as a metric for evaluating our localization model, we also establish its potency as a frontend with automatic speech recognition (ASR) as the downstream task. We convert the estimated DOAs into a feature suitable for ASR and pass it as an additional input feature to a strong multi-channel and multi-talker speech recognition baseline. This added input feature drastically improves the ASR performance and gives a word error rate (WER) of 6.3% on the evaluation data of our simulated noisy two speaker mixtures, while the baseline which doesn't use explicit localization input has a WER of 11.5%. We also perform ASR evaluation on real recordings with the overlapped set of the MC-WSJ-AV corpus in addition to simulated mixtures.

</details>

### [Hierarchical Transformer-based Large-Context End-to-end ASR with Large-Context Knowledge Distillation](2102.07935.md)
**Ryo Masumura, Naoki Makishima, Mana Ihori, Akihiko Takashima et al.** · 2021-02-16

<details>
<summary>Abstract</summary>

We present a novel large-context end-to-end automatic speech recognition (E2E-ASR) model and its effective training method based on knowledge distillation. Common E2E-ASR models have mainly focused on utterance-level processing in which each utterance is independently transcribed. On the other hand, large-context E2E-ASR models, which take into account long-range sequential contexts beyond utterance boundaries, well handle a sequence of utterances such as discourses and conversations. However, the transformer architecture, which has recently achieved state-of-the-art ASR performance among utterance-level ASR systems, has not yet been introduced into the large-context ASR systems. We can expect that the transformer architecture can be leveraged for effectively capturing not only input speech contexts but also long-range sequential contexts beyond utterance boundaries. Therefore, this paper proposes a hierarchical transformer-based large-context E2E-ASR model that combines the transformer architecture with hierarchical encoder-decoder based large-context modeling. In addition, in order to enable the proposed model to use long-range sequential contexts, we also propose a large-context knowledge distillation that distills the knowledge from a pre-trained large-context language model in the training phase. We evaluate the effectiveness of the proposed model and proposed training method on Japanese discourse ASR tasks.

</details>

### [Personalization Strategies for End-to-End Speech Recognition Systems](2102.07739.md)
**Aditya Gourav, Linda Liu, Ankur Gandhe, Yile Gu et al.** · 2021-02-15

<details>
<summary>Abstract</summary>

The recognition of personalized content, such as contact names, remains a challenging problem for end-to-end speech recognition systems. In this work, we demonstrate how first and second-pass rescoring strategies can be leveraged together to improve the recognition of such words. Following previous work, we use a shallow fusion approach to bias towards recognition of personalized content in the first-pass decoding. We show that such an approach can improve personalized content recognition by up to 16% with minimum degradation on the general use case. We describe a fast and scalable algorithm that enables our biasing models to remain at the word-level, while applying the biasing at the subword level. This has the advantage of not requiring the biasing models to be dependent on any subword symbol table. We also describe a novel second-pass de-biasing approach: used in conjunction with a first-pass shallow fusion that optimizes on oracle WER, we can achieve an additional 14% improvement on personalized content recognition, and even improve accuracy for the general use case by up to 2.5%.

</details>

### [Fast End-to-End Speech Recognition via Non-Autoregressive Models and Cross-Modal Knowledge Transferring from BERT](2102.07594.md)
**Ye Bai, Jiangyan Yi, Jianhua Tao, Zhengkun Tian et al.** · 2021-02-15

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder (AED) models have achieved promising performance in speech recognition. However, because the decoder predicts text tokens (such as characters or words) in an autoregressive manner, it is difficult for an AED model to predict all tokens in parallel. This makes the inference speed relatively slow. We believe that because the encoder already captures the whole speech utterance, which has the token-level relationship implicitly, we can predict a token without explicitly autoregressive language modeling. When the prediction of a token does not rely on other tokens, the parallel prediction of all tokens in the sequence is realizable. Based on this idea, we propose a non-autoregressive speech recognition model called LASO (Listen Attentively, and Spell Once). The model consists of an encoder, a decoder, and a position dependent summarizer (PDS). The three modules are based on basic attention blocks. The encoder extracts high-level representations from the speech. The PDS uses positional encodings corresponding to tokens to convert the acoustic representations into token-level representations. The decoder further captures token-level relationships with the self-attention mechanism. At last, the probability distribution on the vocabulary is computed for each token position. Therefore, speech recognition is re-formulated as a position-wise classification problem. Further, we propose a cross-modal transfer learning method to refine semantics from a large-scale pre-trained language model BERT for improving the performance.

</details>

### [Jira: a Kurdish Speech Recognition System Designing and Building Speech Corpus and Pronunciation Lexicon](2102.07412.md)
**Hadi Veisi, Hawre Hosseini, Mohammad Mohammadamini, Wirya Fathy et al.** · 2021-02-15

<details>
<summary>Abstract</summary>

In this paper, we introduce the first large vocabulary speech recognition system (LVSR) for the Central Kurdish language, named Jira. The Kurdish language is an Indo-European language spoken by more than 30 million people in several countries, but due to the lack of speech and text resources, there is no speech recognition system for this language. To fill this gap, we introduce the first speech corpus and pronunciation lexicon for the Kurdish language. Regarding speech corpus, we designed a sentence collection in which the ratio of di-phones in the collection resembles the real data of the Central Kurdish language. The designed sentences are uttered by 576 speakers in a controlled environment with noise-free microphones (called AsoSoft Speech-Office) and in Telegram social network environment using mobile phones (denoted as AsoSoft Speech-Crowdsourcing), resulted in 43.68 hours of speech. Besides, a test set including 11 different document topics is designed and recorded in two corresponding speech conditions (i.e., Office and Crowdsourcing). Furthermore, a 60K pronunciation lexicon is prepared in this research in which we faced several challenges and proposed solutions for them. The Kurdish language has several dialects and sub-dialects that results in many lexical variations. Our methods for script standardization of lexical variations and automatic pronunciation of the lexicon tokens are presented in detail. To setup the recognition engine, we used the Kaldi toolkit. A statistical tri-gram language model that is extracted from the AsoSoft text corpus is used in the system. Several standard recipes including HMM-based models (i.e., mono, tri1, tr2, tri2, tri3), SGMM, and DNN methods are used to generate the acoustic model. These methods are trained with AsoSoft Speech-Office and AsoSoft Speech-Crowdsourcing and a combination of them. The best performance achieved by the SGMM acoustic model which results in 13.9% of the average word error rate (on different document topics) and 4.9% for the general topic.

</details>

### [Leveraging Acoustic and Linguistic Embeddings from Pretrained speech and language Models for Intent Classification](2102.07370.md)
**Bidisha Sharma, Maulik Madhavi, Haizhou Li** · 2021-02-15

<details>
<summary>Abstract</summary>

Intent classification is a task in spoken language understanding. An intent classification system is usually implemented as a pipeline process, with a speech recognition module followed by text processing that classifies the intents. There are also studies of end-to-end system that takes acoustic features as input and classifies the intents directly. Such systems don't take advantage of relevant linguistic information, and suffer from limited training data. In this work, we propose a novel intent classification framework that employs acoustic features extracted from a pretrained speech recognition system and linguistic features learned from a pretrained language model. We use knowledge distillation technique to map the acoustic embeddings towards linguistic embeddings. We perform fusion of both acoustic and linguistic embeddings through cross-attention approach to classify intents. With the proposed method, we achieve 90.86% and 99.07% accuracy on ATIS and Fluent speech corpus, respectively.

</details>

### [Robust Classification using Hidden Markov Models and Mixtures of Normalizing Flows](2102.07284.md)
**Anubhab Ghosh, Antoine Honoré, Dong Liu, Gustav Eje Henter et al.** · 2021-02-15

<details>
<summary>Abstract</summary>

We test the robustness of a maximum-likelihood (ML) based classifier where sequential data as observation is corrupted by noise. The hypothesis is that a generative model, that combines the state transitions of a hidden Markov model (HMM) and the neural network based probability distributions for the hidden states of the HMM, can provide a robust classification performance. The combined model is called normalizing-flow mixture model based HMM (NMM-HMM). It can be trained using a combination of expectation-maximization (EM) and backpropagation. We verify the improved robustness of NMM-HMM classifiers in an application to speech recognition.

</details>

### [Thank you for Attention: A survey on Attention-based Artificial Neural Networks for Automatic Speech Recognition](2102.07259.md)
**Priyabrata Karmakar, Shyh Wei Teng, Guojun Lu** · 2021-02-14

<details>
<summary>Abstract</summary>

Attention is a very popular and effective mechanism in artificial neural network-based sequence-to-sequence models. In this survey paper, a comprehensive review of the different attention models used in developing automatic speech recognition systems is provided. The paper focuses on the development and evolution of attention models for offline and streaming speech recognition within recurrent neural network- and Transformer- based architectures.

</details>

### [Multimodal Punctuation Prediction with Contextual Dropout](2102.11012.md)
**Andrew Silva, Barry-John Theobald, Nicholas Apostoloff** · 2021-02-12

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is widely used in consumer electronics. ASR greatly improves the utility and accessibility of technology, but usually the output is only word sequences without punctuation. This can result in ambiguity in inferring user-intent. We first present a transformer-based approach for punctuation prediction that achieves 8% improvement on the IWSLT 2012 TED Task, beating the previous state of the art [1]. We next describe our multimodal model that learns from both text and audio, which achieves 8% improvement over the text-only algorithm on an internal dataset for which we have both the audio and transcriptions. Finally, we present an approach to learning a model using contextual dropout that allows us to handle variable amounts of future context at test time.

</details>

### [Hybrid phonetic-neural model for correction in speech recognition systems](2102.06744.md)
**Rafael Viana-Cámara, Mario Campos-Soberanis, Diego Campos-Sobrino** · 2021-02-12

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is a relevant area in multiple settings because it provides a natural communication mechanism between applications and users. ASRs often fail in environments that use language specific to particular application domains. Some strategies have been explored to reduce errors in closed ASRs through post-processing, particularly automatic spell checking, and deep learning approaches. In this article, we explore using a deep neural network to refine the results of a phonetic correction algorithm applied to a telesales audio database. The results exhibit a reduction in the word error rate (WER), both in the original transcription and in the phonetic correction, which shows the viability of deep learning models together with post-processing correction strategies to reduce errors made by closed ASRs in specific language domains.

</details>

### [End-to-end Audio-visual Speech Recognition with Conformers](2102.06657.md)
**Pingchuan Ma, Stavros Petridis, Maja Pantic** · 2021-02-12

<details>
<summary>Abstract</summary>

In this work, we present a hybrid CTC/Attention model based on a ResNet-18 and Convolution-augmented transformer (Conformer), that can be trained in an end-to-end manner. In particular, the audio and visual encoders learn to extract features directly from raw pixels and audio waveforms, respectively, which are then fed to conformers and then fusion takes place via a Multi-Layer Perceptron (MLP). The model learns to recognise characters using a combination of CTC and an attention mechanism. We show that end-to-end training, instead of using pre-computed visual features which is common in the literature, the use of a conformer, instead of a recurrent network, and the use of a transformer-based language model, significantly improve the performance of our model. We present results on the largest publicly available datasets for sentence-level speech recognition, Lip Reading Sentences 2 (LRS2) and Lip Reading Sentences 3 (LRS3), respectively. The results show that our proposed models raise the state-of-the-art performance by a large margin in audio-only, visual-only, and audio-visual experiments.

</details>

### [Transformer Language Models with LSTM-based Cross-utterance Information Representation](2102.06474.md)
**G. Sun, C. Zhang, P. C. Woodland** · 2021-02-12

<details>
<summary>Abstract</summary>

The effective incorporation of cross-utterance information has the potential to improve language models (LMs) for automatic speech recognition (ASR). To extract more powerful and robust cross-utterance representations for the Transformer LM (TLM), this paper proposes the R-TLM which uses hidden states in a long short-term memory (LSTM) LM. To encode the cross-utterance information, the R-TLM incorporates an LSTM module together with a segment-wise recurrence in some of the Transformer blocks. In addition to the LSTM module output, a shortcut connection using a fusion layer that bypasses the LSTM module is also investigated. The proposed system was evaluated on the AMI meeting corpus, the Eval2000 and the RT03 telephone conversation evaluation sets. The best R-TLM achieved 0.9%, 0.6%, and 0.8% absolute WER reductions over the single-utterance TLM baseline, and 0.5%, 0.3%, 0.2% absolute WER reductions over a strong cross-utterance TLM baseline on the AMI evaluation set, Eval2000 and RT03 respectively. Improvements on Eval2000 and RT03 were further supported by significance tests. R-TLMs were found to have better LM scores on words where recognition errors are more likely to occur. The R-TLM WER can be further reduced by interpolation with an LSTM-LM.

</details>

### [An Investigation of End-to-End Models for Robust Speech Recognition](2102.06237.md)
**Archiki Prasad, Preethi Jyothi, Rajbabu Velmurugan** · 2021-02-11

<details>
<summary>Abstract</summary>

End-to-end models for robust automatic speech recognition (ASR) have not been sufficiently well-explored in prior work. With end-to-end models, one could choose to preprocess the input speech using speech enhancement techniques and train the model using enhanced speech. Another alternative is to pass the noisy speech as input and modify the model architecture to adapt to noisy speech. A systematic comparison of these two approaches for end-to-end robust ASR has not been attempted before. We address this gap and present a detailed comparison of speech enhancement-based techniques and three different model-based adaptation techniques covering data augmentation, multi-task learning, and adversarial learning for robust ASR. While adversarial learning is the best-performing technique on certain noise types, it comes at the cost of degrading clean speech WER. On other relatively stationary noise types, a new speech enhancement technique outperformed all the model-based adaptation techniques. This suggests that knowledge of the underlying noise type can meaningfully inform the choice of adaptation technique.

</details>

### [Fused Acoustic and Text Encoding for Multimodal Bilingual Pretraining and Speech Translation](2102.05766.md)
**Renjie Zheng, Junkun Chen, Mingbo Ma, Liang Huang** · 2021-02-10

<details>
<summary>Abstract</summary>

Recently, representation learning for text and speech has successfully improved many language related tasks. However, all existing methods suffer from two limitations: (a) they only learn from one input modality, while a unified representation for both speech and text is needed by tasks such as end-to-end speech translation, and as a result,(b) they can not exploit various large-scale text and speech data and their performance is limited by the scarcity of parallel speech translation data.To address these problems, we propose a Fused Acoustic and Text Masked Language Model (FAT-MLM) which jointly learns a unified representation for both acoustic and text input from various types of corpora including parallel data for speech recognition and machine translation, and even pure speech and text data. Within this cross-modal representation learning framework, we further present an end-to-end model for Fused Acoustic and Text Speech Translation (FAT-ST). Experiments on three translation directions show that by fine-tuning from FAT-MLM, our proposed speech translation models substantially improve translation quality by up to +5.9 BLEU.

</details>

### [Fast Classification Learning with Neural Networks and Conceptors for Speech Recognition and Car Driving Maneuvers](2102.05588.md)
**Stefanie Krause, Oliver Otto, Frieder Stolzenburg** · 2021-02-10

<details>
<summary>Abstract</summary>

Recurrent neural networks are a powerful means in diverse applications. We show that, together with so-called conceptors, they also allow fast learning, in contrast to other deep learning methods. In addition, a relatively small number of examples suffices to train neural networks with high accuracy. We demonstrate this with two applications, namely speech recognition and detecting car driving maneuvers. We improve the state of the art by application-specific preparation techniques: For speech recognition, we use mel frequency cepstral coefficients leading to a compact representation of the frequency spectra, and detecting car driving maneuvers can be done without the commonly used polynomial interpolation, as our evaluation suggests.

</details>

### [Dompteur: Taming Audio Adversarial Examples](2102.05431.md)
**Thorsten Eisenhofer, Lea Schönherr, Joel Frank, Lars Speckemeier et al.** · 2021-02-10

<details>
<summary>Abstract</summary>

Adversarial examples seem to be inevitable. These specifically crafted inputs allow attackers to arbitrarily manipulate machine learning systems. Even worse, they often seem harmless to human observers. In our digital society, this poses a significant threat. For example, Automatic Speech Recognition (ASR) systems, which serve as hands-free interfaces to many kinds of systems, can be attacked with inputs incomprehensible for human listeners. The research community has unsuccessfully tried several approaches to tackle this problem. In this paper we propose a different perspective: We accept the presence of adversarial examples against ASR systems, but we require them to be perceivable by human listeners. By applying the principles of psychoacoustics, we can remove semantically irrelevant information from the ASR input and train a model that resembles human perception more closely. We implement our idea in a tool named DOMPTEUR and demonstrate that our augmented system, in contrast to an unmodified baseline, successfully focuses on perceptible ranges of the input signal. This change forces adversarial examples into the audible range, while using minimal computational overhead and preserving benign performance. To evaluate our approach, we construct an adaptive attacker that actively tries to avoid our augmentations and demonstrate that adversarial examples from this attacker remain clearly perceivable. Finally, we substantiate our claims by performing a hearing test with crowd-sourced human listeners.

</details>

### [NUVA: A Naming Utterance Verifier for Aphasia Treatment](2102.05408.md)
**David Sabate Barbera, Mark Huckvale, Victoria Fleming, Emily Upton et al.** · 2021-02-10

<details>
<summary>Abstract</summary>

Anomia (word-finding difficulties) is the hallmark of aphasia, an acquired language disorder most commonly caused by stroke. Assessment of speech performance using picture naming tasks is a key method for both diagnosis and monitoring of responses to treatment interventions by people with aphasia (PWA). Currently, this assessment is conducted manually by speech and language therapists (SLT). Surprisingly, despite advancements in automatic speech recognition (ASR) and artificial intelligence with technologies like deep learning, research on developing automated systems for this task has been scarce. Here we present NUVA, an utterance verification system incorporating a deep learning element that classifies 'correct' versus' incorrect' naming attempts from aphasic stroke patients. When tested on eight native British-English speaking PWA the system's performance accuracy ranged between 83.6% to 93.6%, with a 10-fold cross-validation mean of 89.5%. This performance was not only significantly better than a baseline created for this study using one of the leading commercially available ASRs (Google speech-to-text service) but also comparable in some instances with two independent SLT ratings for the same dataset.

</details>

### [Sparsification via Compressed Sensing for Automatic Speech Recognition](2102.04932.md)
**Kai Zhen, Hieu Duy Nguyen, Feng-Ju Chang, Athanasios Mouchtaris et al.** · 2021-02-09

<details>
<summary>Abstract</summary>

In order to achieve high accuracy for machine learning (ML) applications, it is essential to employ models with a large number of parameters. Certain applications, such as Automatic Speech Recognition (ASR), however, require real-time interactions with users, hence compelling the model to have as low latency as possible. Deploying large scale ML applications thus necessitates model quantization and compression, especially when running ML models on resource constrained devices. For example, by forcing some of the model weight values into zero, it is possible to apply zero-weight compression, which reduces both the model size and model reading time from the memory. In the literature, such methods are referred to as sparse pruning. The fundamental questions are when and which weights should be forced to zero, i.e. be pruned. In this work, we propose a compressed sensing based pruning (CSP) approach to effectively address those questions. By reformulating sparse pruning as a sparsity inducing and compression-error reduction dual problem, we introduce the classic compressed sensing process into the ML model training process. Using ASR task as an example, we show that CSP consistently outperforms existing approaches in the literature.

</details>

### [BembaSpeech: A Speech Recognition Corpus for the Bemba Language](2102.04889.md)
**Claytone Sikasote, Antonios Anastasopoulos** · 2021-02-09

<details>
<summary>Abstract</summary>

We present a preprocessed, ready-to-use automatic speech recognition corpus, BembaSpeech, consisting over 24 hours of read speech in the Bemba language, a written but low-resourced language spoken by over 30% of the population in Zambia. To assess its usefulness for training and testing ASR systems for Bemba, we train an end-to-end Bemba ASR system by fine-tuning a pre-trained DeepSpeech English model on the training portion of the BembaSpeech corpus. Our best model achieves a word error rate (WER) of 54.78%. The results show that the corpus can be used for building ASR systems for Bemba. The corpus and models are publicly released at https://github.com/csikasote/BembaSpeech.

</details>

### [Bayesian Transformer Language Models for Speech Recognition](2102.04754.md)
**Boyang Xue, Jianwei Yu, Junhao Xu, Shansong Liu et al.** · 2021-02-09

<details>
<summary>Abstract</summary>

State-of-the-art neural language models (LMs) represented by Transformers are highly complex. Their use of fixed, deterministic parameter estimates fail to account for model uncertainty and lead to over-fitting and poor generalization when given limited training data. In order to address these issues, this paper proposes a full Bayesian learning framework for Transformer LM estimation. Efficient variational inference based approaches are used to estimate the latent parameter posterior distributions associated with different parts of the Transformer model architecture including multi-head self-attention, feed forward and embedding layers. Statistically significant word error rate (WER) reductions up to 0.5\% absolute (3.18\% relative) and consistent perplexity gains were obtained over the baseline Transformer LMs on state-of-the-art Switchboard corpus trained LF-MMI factored TDNN systems with i-Vector speaker adaptation. Performance improvements were also obtained on a cross domain LM adaptation task requiring porting a Transformer LM trained on the Switchboard and Fisher data to a low-resource DementiaBank elderly speech corpus.

</details>

### [Train your classifier first: Cascade Neural Networks Training from upper layers to lower layers](2102.04697.md)
**Shucong Zhang, Cong-Thanh Do, Rama Doddipatla, Erfan Loweimi et al.** · 2021-02-09

<details>
<summary>Abstract</summary>

Although the lower layers of a deep neural network learn features which are transferable across datasets, these layers are not transferable within the same dataset. That is, in general, freezing the trained feature extractor (the lower layers) and retraining the classifier (the upper layers) on the same dataset leads to worse performance. In this paper, for the first time, we show that the frozen classifier is transferable within the same dataset. We develop a novel top-down training method which can be viewed as an algorithm for searching for high-quality classifiers. We tested this method on automatic speech recognition (ASR) tasks and language modelling tasks. The proposed method consistently improves recurrent neural network ASR models on Wall Street Journal, self-attention ASR models on Switchboard, and AWD-LSTM language models on WikiText-2.

</details>

### [Federated Acoustic Modeling For Automatic Speech Recognition](2102.04429.md)
**Xiaodong Cui, Songtao Lu, Brian Kingsbury** · 2021-02-08

<details>
<summary>Abstract</summary>

Data privacy and protection is a crucial issue for any automatic speech recognition (ASR) service provider when dealing with clients. In this paper, we investigate federated acoustic modeling using data from multiple clients. A client's data is stored on a local data server and the clients communicate only model parameters with a central server, and not their data. The communication happens infrequently to reduce the communication cost. To mitigate the non-iid issue, client adaptive federated training (CAFT) is proposed to canonicalize data across clients. The experiments are carried out on 1,150 hours of speech data from multiple domains. Hybrid LSTM acoustic models are trained via federated learning and their performance is compared to traditional centralized acoustic model training. The experimental results demonstrate the effectiveness of the proposed federated acoustic modeling strategy. We also show that CAFT can further improve the performance of the federated acoustic model.

</details>

### [End-to-End Multi-Channel Transformer for Speech Recognition](2102.03951.md)
**Feng-Ju Chang, Martin Radfar, Athanasios Mouchtaris, Brian King et al.** · 2021-02-08

<details>
<summary>Abstract</summary>

Transformers are powerful neural architectures that allow integrating different modalities using attention mechanisms. In this paper, we leverage the neural transformer architectures for multi-channel speech recognition systems, where the spectral and spatial information collected from different microphones are integrated using attention layers. Our multi-channel transformer network mainly consists of three parts: channel-wise self attention layers (CSA), cross-channel attention layers (CCA), and multi-channel encoder-decoder attention layers (EDA). The CSA and CCA layers encode the contextual relationship within and between channels and across time, respectively. The channel-attended outputs from CSA and CCA are then fed into the EDA layers to help decode the next token given the preceding ones. The experiments show that in a far-field in-house dataset, our method outperforms the baseline single-channel transformer, as well as the super-directive and neural beamformers cascaded with the transformers.

</details>

### [Multi-Task Self-Supervised Pre-Training for Music Classification](2102.03229.md)
**Ho-Hsiang Wu, Chieh-Chi Kao, Qingming Tang, Ming Sun et al.** · 2021-02-05

<details>
<summary>Abstract</summary>

Deep learning is very data hungry, and supervised learning especially requires massive labeled data to work well. Machine listening research often suffers from limited labeled data problem, as human annotations are costly to acquire, and annotations for audio are time consuming and less intuitive. Besides, models learned from labeled dataset often embed biases specific to that particular dataset. Therefore, unsupervised learning techniques become popular approaches in solving machine listening problems. Particularly, a self-supervised learning technique utilizing reconstructions of multiple hand-crafted audio features has shown promising results when it is applied to speech domain such as emotion recognition and automatic speech recognition (ASR). In this paper, we apply self-supervised and multi-task learning methods for pre-training music encoders, and explore various design choices including encoder architectures, weighting mechanisms to combine losses from multiple tasks, and worker selections of pretext tasks. We investigate how these design choices interact with various downstream music classification tasks. We find that using various music specific workers altogether with weighting mechanisms to balance the losses during pre-training helps improve and generalize to the downstream tasks.

</details>

### [Intermediate Loss Regularization for CTC-based Speech Recognition](2102.03216.md)
**Jaesong Lee, Shinji Watanabe** · 2021-02-05

<details>
<summary>Abstract</summary>

We present a simple and efficient auxiliary loss function for automatic speech recognition (ASR) based on the connectionist temporal classification (CTC) objective. The proposed objective, an intermediate CTC loss, is attached to an intermediate layer in the CTC encoder network. This intermediate CTC loss well regularizes CTC training and improves the performance requiring only small modification of the code and small and no overhead during training and inference, respectively. In addition, we propose to combine this intermediate CTC loss with stochastic depth training, and apply this combination to a recently proposed Conformer network. We evaluate the proposed method on various corpora, reaching word error rate (WER) 9.9% on the WSJ corpus and character error rate (CER) 5.2% on the AISHELL-1 corpus respectively, based on CTC greedy search without a language model. Especially, the AISHELL-1 task is comparable to other state-of-the-art ASR systems based on auto-regressive decoder with beam search.

</details>

### [Two-Stage Augmentation and Adaptive CTC Fusion for Improved Robustness of Multi-Stream End-to-End ASR](2102.03055.md)
**Ruizhi Li, Gregory Sell, Hynek Hermansky** · 2021-02-05

<details>
<summary>Abstract</summary>

Performance degradation of an Automatic Speech Recognition (ASR) system is commonly observed when the test acoustic condition is different from training. Hence, it is essential to make ASR systems robust against various environmental distortions, such as background noises and reverberations. In a multi-stream paradigm, improving robustness takes account of handling a variety of unseen single-stream conditions and inter-stream dynamics. Previously, a practical two-stage training strategy was proposed within multi-stream end-to-end ASR, where Stage-2 formulates the multi-stream model with features from Stage-1 Universal Feature Extractor (UFE). In this paper, as an extension, we introduce a two-stage augmentation scheme focusing on mismatch scenarios: Stage-1 Augmentation aims to address single-stream input varieties with data augmentation techniques; Stage-2 Time Masking applies temporal masks on UFE features of randomly selected streams to simulate diverse stream combinations. During inference, we also present adaptive Connectionist Temporal Classification (CTC) fusion with the help of hierarchical attention mechanisms. Experiments have been conducted on two datasets, DIRHA and AMI, as a multi-stream scenario. Compared with the previous training strategy, substantial improvements are reported with relative word error rate reductions of 29.7-59.3% across several unseen stream combinations.

</details>

### [Effects of Number of Filters of Convolutional Layers on Speech Recognition Model Accuracy](2102.02326.md)
**James Mou, Jun Li** · 2021-02-03

<details>
<summary>Abstract</summary>

Inspired by the progress of the End-to-End approach [1], this paper systematically studies the effects of Number of Filters of convolutional layers on the model prediction accuracy of CNN+RNN (Convolutional Neural Networks adding to Recurrent Neural Networks) for ASR Models (Automatic Speech Recognition). Experimental results show that only when the CNN Number of Filters exceeds a certain threshold value is adding CNN to RNN able to improve the performance of the CNN+RNN speech recognition model, otherwise some parameter ranges of CNN can render it useless to add the CNN to the RNN model. Our results show a strong dependency of word accuracy on the Number of Filters of convolutional layers. Based on the experimental results, the paper suggests a possible hypothesis of Sound-2-Vector Embedding (Convolutional Embedding) to explain the above observations. Based on this Embedding hypothesis and the optimization of parameters, the paper develops an End-to-End speech recognition system which has a high word accuracy but also has a light model-weight. The developed LVCSR (Large Vocabulary Continuous Speech Recognition) model has achieved quite a high word accuracy of 90.2% only by its Acoustic Model alone, without any assistance from intermediate phonetic representation and any Language Model. Its acoustic model contains only 4.4 million weight parameters, compared to the 35~68 million acoustic-model weight parameters in DeepSpeech2 [2] (one of the top state-of-the-art LVCSR models) which can achieve a word accuracy of 91.5%. The light-weighted model is good for improving the transcribing computing efficiency and also useful for mobile devices, Driverless Vehicles, etc. Our model weight is reduced to ~10% the size of DeepSpeech2, but our model accuracy remains close to that of DeepSpeech2. If combined with a Language Model, our LVCSR system is able to achieve 91.5% word accuracy.

</details>

### [General-Purpose Speech Representation Learning through a Self-Supervised Multi-Granularity Framework](2102.01930.md)
**Yucheng Zhao, Dacheng Yin, Chong Luo, Zhiyuan Zhao et al.** · 2021-02-03

<details>
<summary>Abstract</summary>

This paper presents a self-supervised learning framework, named MGF, for general-purpose speech representation learning. In the design of MGF, speech hierarchy is taken into consideration. Specifically, we propose to use generative learning approaches to capture fine-grained information at small time scales and use discriminative learning approaches to distill coarse-grained or semantic information at large time scales. For phoneme-scale learning, we borrow idea from the masked language model but tailor it for the continuous speech signal by replacing classification loss with a contrastive loss. We corroborate our design by evaluating MGF representation on various downstream tasks, including phoneme classification, speaker classification, speech recognition, and emotion classification. Experiments verify that training at different time scales needs different training targets and loss functions, which in general complement each other and lead to a better performance.

</details>

### [WeNet: Production oriented Streaming and Non-streaming End-to-End Speech Recognition Toolkit](2102.01547.md)
**Zhuoyuan Yao, Di Wu, Xiong Wang, Binbin Zhang et al.** · 2021-02-02

<details>
<summary>Abstract</summary>

In this paper, we propose an open source, production first, and production ready speech recognition toolkit called WeNet in which a new two-pass approach is implemented to unify streaming and non-streaming end-to-end (E2E) speech recognition in a single model. The main motivation of WeNet is to close the gap between the research and the production of E2E speechrecognition models. WeNet provides an efficient way to ship ASR applications in several real-world scenarios, which is the main difference and advantage to other open source E2E speech recognition toolkits. In our toolkit, a new two-pass method is implemented. Our method propose a dynamic chunk-based attention strategy of the the transformer layers to allow arbitrary right context length modifies in hybrid CTC/attention architecture. The inference latency could be easily controlled by only changing the chunk size. The CTC hypotheses are then rescored by the attention decoder to get the final result. Our experiments on the AISHELL-1 dataset using WeNet show that, our model achieves 5.03\% relative character error rate (CER) reduction in non-streaming ASR compared to a standard non-streaming transformer. After model quantification, our model perform reasonable RTF and latency.

</details>

### [Internal Language Model Training for Domain-Adaptive End-to-End Speech Recognition](2102.01380.md)
**Zhong Meng, Naoyuki Kanda, Yashesh Gaur, Sarangarajan Parthasarathy et al.** · 2021-02-02

<details>
<summary>Abstract</summary>

The efficacy of external language model (LM) integration with existing end-to-end (E2E) automatic speech recognition (ASR) systems can be improved significantly using the internal language model estimation (ILME) method. In this method, the internal LM score is subtracted from the score obtained by interpolating the E2E score with the external LM score, during inference. To improve the ILME-based inference, we propose an internal LM training (ILMT) method to minimize an additional internal LM loss by updating only the E2E model components that affect the internal LM estimation. ILMT encourages the E2E model to form a standalone LM inside its existing components, without sacrificing ASR accuracy. After ILMT, the more modular E2E model with matched training and inference criteria enables a more thorough elimination of the source-domain internal LM, and therefore leads to a more effective integration of the target-domain external LM. Experimented with 30K-hour trained recurrent neural network transducer and attention-based encoder-decoder models, ILMT with ILME-based inference achieves up to 31.5% and 11.4% relative word error rate reductions from standard E2E training with Shallow Fusion on out-of-domain LibriSpeech and in-domain Microsoft production test sets, respectively.

</details>

### [On Scaling Contrastive Representations for Low-Resource Speech Recognition](2102.00850.md)
**Lasse Borgholt, Tycho Max Sylvester Tax, Jakob Drachmann Havtorn, Lars Maaløe et al.** · 2021-02-01

<details>
<summary>Abstract</summary>

Recent advances in self-supervised learning through contrastive training have shown that it is possible to learn a competitive speech recognition system with as little as 10 minutes of labeled data. However, these systems are computationally expensive since they require pre-training followed by fine-tuning in a large parameter space. We explore the performance of such systems without fine-tuning by training a state-of-the-art speech recognizer on the fixed representations from the computationally demanding wav2vec 2.0 framework. We find performance to decrease without fine-tuning and, in the extreme low-resource setting, wav2vec 2.0 is inferior to its predecessor. In addition, we find that wav2vec 2.0 representations live in a low dimensional subspace and that decorrelating the features of the representations can stabilize training of the automatic speech recognizer. Finally, we propose a bidirectional extension to the original wav2vec framework that consistently improves performance.

</details>

### [Neural OCR Post-Hoc Correction of Historical Corpora](2102.00583.md)
**Lijun Lyu, Maria Koutraki, Martin Krickl, Besnik Fetahu** · 2021-02-01

<details>
<summary>Abstract</summary>

Optical character recognition (OCR) is crucial for a deeper access to historical collections. OCR needs to account for orthographic variations, typefaces, or language evolution (i.e., new letters, word spellings), as the main source of character, word, or word segmentation transcription errors. For digital corpora of historical prints, the errors are further exacerbated due to low scan quality and lack of language standardization. For the task of OCR post-hoc correction, we propose a neural approach based on a combination of recurrent (RNN) and deep convolutional network (ConvNet) to correct OCR transcription errors. At character level we flexibly capture errors, and decode the corrected output based on a novel attention mechanism. Accounting for the input and output similarity, we propose a new loss function that rewards the model's correcting behavior. Evaluation on a historical book corpus in German language shows that our models are robust in capturing diverse OCR transcription errors and reduce the word error rate of 32.3% by more than 89%.

</details>

### [Graph Neural Networks to Predict Customer Satisfaction Following Interactions with a Corporate Call Center](2102.00420.md)
**Teja Kanchinadam, Zihang Meng, Joseph Bockhorst, Vikas Singh et al.** · 2021-01-31

<details>
<summary>Abstract</summary>

Customer satisfaction is an important factor in creating and maintaining long-term relationships with customers. Near real-time identification of potentially dissatisfied customers following phone calls can provide organizations the opportunity to take meaningful interventions and to foster ongoing customer satisfaction and loyalty. This work describes a fully operational system we have developed at a large US company for predicting customer satisfaction following incoming phone calls. The system takes as an input speech-to-text transcriptions of calls and predicts call satisfaction reported by customers on post-call surveys (scale from 1 to 10). Because of its ordinal, subjective, and often highly-skewed nature, predicting survey scores is not a trivial task and presents several modeling challenges. We introduce a graph neural network (GNN) approach that takes into account the comparative nature of the problem by considering the relative scores among batches, instead of only pairs of calls when training. This approach produces more accurate predictions than previous approaches including standard regression and classification models that directly fit the survey scores with call data. Our proposed approach can be easily generalized to other customer satisfaction prediction problems.

</details>

### [Speech Recognition by Simply Fine-tuning BERT](2102.00291.md)
**Wen-Chin Huang, Chia-Hua Wu, Shang-Bao Luo, Kuan-Yu Chen et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

We propose a simple method for automatic speech recognition (ASR) by fine-tuning BERT, which is a language model (LM) trained on large-scale unlabeled text data and can generate rich contextual representations. Our assumption is that given a history context sequence, a powerful LM can narrow the range of possible choices and the speech signal can be used as a simple clue. Hence, comparing to conventional ASR systems that train a powerful acoustic model (AM) from scratch, we believe that speech recognition is possible by simply fine-tuning a BERT model. As an initial study, we demonstrate the effectiveness of the proposed idea on the AISHELL dataset and show that stacking a very simple AM on top of BERT can yield reasonable performance.

</details>

### [Robust Attack Detection Approach for IIoT Using Ensemble Classifier](2102.01515.md)
**V. Priya, I. Sumaiya Thaseen, Thippa Reddy Gadekallu, Mohamed K. Aboudaif et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

Generally, the risks associated with malicious threats are increasing for the IIoT and its related applications due to dependency on the Internet and the minimal resource availability of IoT devices. Thus, anomaly-based intrusion detection models for IoT networks are vital. Distinct detection methodologies need to be developed for the IIoT network as threat detection is a significant expectation of stakeholders. Machine learning approaches are considered to be evolving techniques that learn with experience, and such approaches have resulted in superior performance in various applications, such as pattern recognition, outlier analysis, and speech recognition. Traditional techniques and tools are not adequate to secure IIoT networks due to the use of various protocols in industrial systems and restricted possibilities of upgradation. In this paper, the objective is to develop a two-phase anomaly detection model to enhance the reliability of an IIoT network. In the first phase, SVM and Naive Bayes are integrated using an ensemble blending technique. K-fold cross-validation is performed while training the data with different training and testing ratios to obtain optimized training and test sets. Ensemble blending uses a random forest technique to predict class labels. An Artificial Neural Network (ANN) classifier that uses the Adam optimizer to achieve better accuracy is also used for prediction. In the second phase, both the ANN and random forest results are fed to the model's classification unit, and the highest accuracy value is considered the final result. The proposed model is tested on standard IoT attack datasets, such as WUSTL_IIOT-2018, N_BaIoT, and Bot_IoT. The highest accuracy obtained is 99%. The results also demonstrate that the proposed model outperforms traditional techniques and thus improves the reliability of an IIoT network.

</details>

### [Triple M: A Practical Text-to-speech Synthesis System With Multi-guidance Attention And Multi-band Multi-time LPCNet](2102.00247.md)
**Shilun Lin, Fenglong Xie, Li Meng, Xinhui Li et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

In this work, a robust and efficient text-to-speech (TTS) synthesis system named Triple M is proposed for large-scale online application. The key components of Triple M are: 1) A sequence-to-sequence model adopts a novel multi-guidance attention to transfer complementary advantages from guiding attention mechanisms to the basic attention mechanism without in-domain performance loss and online service modification. Compared with single attention mechanism, multi-guidance attention not only brings better naturalness to long sentence synthesis, but also reduces the word error rate by 26.8%. 2) A new efficient multi-band multi-time vocoder framework, which reduces the computational complexity from 2.8 to 1.0 GFLOP and speeds up LPCNet by 2.75x on a single CPU.

</details>

### [BCN2BRNO: ASR System Fusion for Albayzin 2020 Speech to Text Challenge](2101.12729.md)
**Martin Kocour, Guillermo Cámbara, Jordi Luque, David Bonet et al.** · 2021-01-29

<details>
<summary>Abstract</summary>

This paper describes joint effort of BUT and Telefónica Research on development of Automatic Speech Recognition systems for Albayzin 2020 Challenge. We compare approaches based on either hybrid or end-to-end models. In hybrid modelling, we explore the impact of SpecAugment layer on performance. For end-to-end modelling, we used a convolutional neural network with gated linear units (GLUs). The performance of such model is also evaluated with an additional n-gram language model to improve word error rates. We further inspect source separation methods to extract speech from noisy environment (i.e. TV shows). More precisely, we assess the effect of using a neural-based music separator named Demucs. A fusion of our best systems achieved 23.33% WER in official Albayzin 2020 evaluations. Aside from techniques used in our final submitted systems, we also describe our efforts in retrieving high quality transcripts for training.

</details>

### [Transformer Based Deliberation for Two-Pass Speech Recognition](2101.11577.md)
**Ke Hu, Ruoming Pang, Tara N. Sainath, Trevor Strohman** · 2021-01-27

<details>
<summary>Abstract</summary>

Interactive speech recognition systems must generate words quickly while also producing accurate results. Two-pass models excel at these requirements by employing a first-pass decoder that quickly emits words, and a second-pass decoder that requires more context but is more accurate. Previous work has established that a deliberation network can be an effective second-pass model. The model attends to two kinds of inputs at once: encoded audio frames and the hypothesis text from the first-pass model. In this work, we explore using transformer layers instead of long-short term memory (LSTM) layers for deliberation rescoring. In transformer layers, we generalize the "encoder-decoder" attention to attend to both encoded audio and first-pass text hypotheses. The output context vectors are then combined by a merger layer. Compared to LSTM-based deliberation, our best transformer deliberation achieves 7% relative word error rate improvements along with a 38% reduction in computation. We also compare against non-deliberation transformer rescoring, and find a 9% relative improvement.

</details>

### [Leveraging End-to-End ASR for Endangered Language Documentation: An Empirical Study on Yoloxóchitl Mixtec](2101.10877.md)
**Jiatong Shi, Jonathan D. Amith, Rey Castillo García, Esteban Guadalupe Sierra et al.** · 2021-01-26

<details>
<summary>Abstract</summary>

"Transcription bottlenecks", created by a shortage of effective human transcribers are one of the main challenges to endangered language (EL) documentation. Automatic speech recognition (ASR) has been suggested as a tool to overcome such bottlenecks. Following this suggestion, we investigated the effectiveness for EL documentation of end-to-end ASR, which unlike Hidden Markov Model ASR systems, eschews linguistic resources but is instead more dependent on large-data settings. We open source a Yoloxóchitl Mixtec EL corpus. First, we review our method in building an end-to-end ASR system in a way that would be reproducible by the ASR community. We then propose a novice transcription correction task and demonstrate how ASR systems and novice transcribers can work together to improve EL documentation. We believe this combinatory methodology would mitigate the transcription bottleneck and transcriber shortage that hinders EL documentation.

</details>

### [A Review of Speaker Diarization: Recent Advances with Deep Learning](2101.09624.md)
**Tae Jin Park, Naoyuki Kanda, Dimitrios Dimitriadis, Kyu J. Han et al.** · 2021-01-24

<details>
<summary>Abstract</summary>

Speaker diarization is a task to label audio or video recordings with classes that correspond to speaker identity, or in short, a task to identify "who spoke when". In the early years, speaker diarization algorithms were developed for speech recognition on multispeaker audio recordings to enable speaker adaptive processing. These algorithms also gained their own value as a standalone application over time to provide speaker-specific metainformation for downstream tasks such as audio retrieval. More recently, with the emergence of deep learning technology, which has driven revolutionary changes in research and practices across speech application domains, rapid advancements have been made for speaker diarization. In this paper, we review not only the historical development of speaker diarization technology but also the recent advancements in neural speaker diarization approaches. Furthermore, we discuss how speaker diarization systems have been integrated with speech recognition applications and how the recent surge of deep learning is leading the way of jointly modeling these two components to be complementary to each other. By considering such exciting technical trends, we believe that this paper is a valuable contribution to the community to provide a survey work by consolidating the recent developments with neural methods and thus facilitating further progress toward a more efficient speaker diarization.

</details>

### [Streaming Models for Joint Speech Recognition and Translation](2101.09149.md)
**Orion Weller, Matthias Sperber, Christian Gollan, Joris Kluivers** · 2021-01-22

<details>
<summary>Abstract</summary>

Using end-to-end models for speech translation (ST) has increasingly been the focus of the ST community. These models condense the previously cascaded systems by directly converting sound waves into translated text. However, cascaded models have the advantage of including automatic speech recognition output, useful for a variety of practical ST systems that often display transcripts to the user alongside the translations. To bridge this gap, recent work has shown initial progress into the feasibility for end-to-end models to produce both of these outputs. However, all previous work has only looked at this problem from the consecutive perspective, leaving uncertainty on whether these approaches are effective in the more challenging streaming setting. We develop an end-to-end streaming ST model based on a re-translation approach and compare against standard cascading approaches. We also introduce a novel inference method for the joint case, interleaving both transcript and translation in generation and removing the need to use separate decoders. Our evaluation across a range of metrics capturing accuracy, latency, and consistency shows that our end-to-end models are statistically similar to cascading models, while having half the number of parameters. We also find that both systems provide strong translation quality at low latency, keeping 99% of consecutive quality at a lag of just under a second.

</details>

### [Exploiting Beam Search Confidence for Energy-Efficient Speech Recognition](2101.09083.md)
**Dennis Pinto, Jose-María Arnau, Antonio González** · 2021-01-22

<details>
<summary>Abstract</summary>

With computers getting more and more powerful and integrated in our daily lives, the focus is increasingly shifting towards more human-friendly interfaces, making Automatic Speech Recognition (ASR) a central player as the ideal means of interaction with machines. Consequently, interest in speech technology has grown in the last few years, with more systems being proposed and higher accuracy levels being achieved, even surpassing \textit{Human Accuracy}. While ASR systems become increasingly powerful, the computational complexity also increases, and the hardware support have to keep pace. In this paper, we propose a technique to improve the energy-efficiency and performance of ASR systems, focusing on low-power hardware for edge devices. We focus on optimizing the DNN-based Acoustic Model evaluation, as we have observed it to be the main bottleneck in state-of-the-art ASR systems, by leveraging run-time information from the Beam Search. By doing so, we reduce energy and execution time of the acoustic model evaluation by 25.6% and 25.9%, respectively, with negligible accuracy loss.

</details>

### [Noisy-target Training: A Training Strategy for DNN-based Speech Enhancement without Clean Speech](2101.08625.md)
**Takuya Fujimura, Yuma Koizumi, Kohei Yatabe, Ryoichi Miyazaki** · 2021-01-21

<details>
<summary>Abstract</summary>

Deep neural network (DNN)-based speech enhancement ordinarily requires clean speech signals as the training target. However, collecting clean signals is very costly because they must be recorded in a studio. This requirement currently restricts the amount of training data for speech enhancement to less than 1/1000 of that of speech recognition which does not need clean signals. Increasing the amount of training data is important for improving the performance, and hence the requirement of clean signals should be relaxed. In this paper, we propose a training strategy that does not require clean signals. The proposed method only utilizes noisy signals for training, which enables us to use a variety of speech signals in the wild. Our experimental results showed that the proposed method can achieve the performance similar to that of a DNN trained with clean signals.

</details>

### [Arabic Speech Recognition by End-to-End, Modular Systems and Human](2101.08454.md)
**Amir Hussein, Shinji Watanabe, Ahmed Ali** · 2021-01-21

<details>
<summary>Abstract</summary>

Recent advances in automatic speech recognition (ASR) have achieved accuracy levels comparable to human transcribers, which led researchers to debate if the machine has reached human performance. Previous work focused on the English language and modular hidden Markov model-deep neural network (HMM-DNN) systems. In this paper, we perform a comprehensive benchmarking for end-to-end transformer ASR, modular HMM-DNN ASR, and human speech recognition (HSR) on the Arabic language and its dialects. For the HSR, we evaluate linguist performance and lay-native speaker performance on a new dataset collected as a part of this study. For ASR the end-to-end work led to 12.5%, 27.5%, 33.8% WER; a new performance milestone for the MGB2, MGB3, and MGB5 challenges respectively. Our results suggest that human performance in the Arabic language is still considerably better than the machine with an absolute WER gap of 3.5% on average.

</details>

### [UniSpeech: Unified Speech Representation Learning with Labeled and Unlabeled Data](2101.07597.md)
**Chengyi Wang, Yu Wu, Yao Qian, Kenichi Kumatani et al.** · 2021-01-19

<details>
<summary>Abstract</summary>

In this paper, we propose a unified pre-training approach called UniSpeech to learn speech representations with both unlabeled and labeled data, in which supervised phonetic CTC learning and phonetically-aware contrastive self-supervised learning are conducted in a multi-task learning manner. The resultant representations can capture information more correlated with phonetic structures and improve the generalization across languages and domains. We evaluate the effectiveness of UniSpeech for cross-lingual representation learning on public CommonVoice corpus. The results show that UniSpeech outperforms self-supervised pretraining and supervised transfer learning for speech recognition by a maximum of 13.4% and 17.8% relative phone error rate reductions respectively (averaged over all testing languages). The transferability of UniSpeech is also demonstrated on a domain-shift speech recognition task, i.e., a relative word error rate reduction of 6% against the previous approach.

</details>

### [Convolution-Based Attention Model With Positional Encoding For Streaming Speech Recognition On Embedded Devices](s2:7167cf25eb343b7ba4e07c59580c5fb40b789d77.md)
**Jinhwan Park, Chanwoo Kim, Wonyong Sung** · 2021-01-19

<details>
<summary>Abstract</summary>

On-device automatic speech recognition (ASR) is much more preferred over server-based implementations owing to its low latency and privacy protection. Many server-based ASRs employ recurrent neural networks (RNNs) to exploit their ability to recognize long sequences with a limited number of states; however, they are inefficient for single-stream implementations in embedded devices. In this study, a highly efficient convolutional model-based ASR with monotonic chunkwise attention is developed. Although temporal convolution-based models allow more efficient implementations, they demand a long filter-length to avoid looping or skipping problems. To remedy this problem, we add positional encoding, while shortening the filter length, to a convolution-based ASR encoder. It is demonstrated that the accuracy of the short filter-length convolutional model is significantly improved. In addition, the effect of positional encoding is analyzed by visualizing the attention energy and encoder outputs. The proposed model achieves the word error rate of 11.20% on TED-LIUMv2 for an end-to-end speech recognition task.

</details>

### [Tiny Transducer: A Highly-efficient Speech Recognition Model on Edge Devices](2101.06856.md)
**Yuekai Zhang, Sining Sun, Long Ma** · 2021-01-18

<details>
<summary>Abstract</summary>

This paper proposes an extremely lightweight phone-based transducer model with a tiny decoding graph on edge devices. First, a phone synchronous decoding (PSD) algorithm based on blank label skipping is first used to speed up the transducer decoding process. Then, to decrease the deletion errors introduced by the high blank score, a blank label deweighting approach is proposed. To reduce parameters and computation, deep feedforward sequential memory network (DFSMN) layers are used in the transducer encoder, and a CNN-based stateless predictor is adopted. SVD technology compresses the model further. WFST-based decoding graph takes the context-independent (CI) phone posteriors as input and allows us to flexibly bias user-specific information. Finally, with only 0.9M parameters after SVD, our system could give a relative 9.1% - 20.5% improvement compared with a bigger conventional hybrid system on edge devices.

</details>

### [Efficiently Fusing Pretrained Acoustic and Linguistic Encoders for Low-resource Speech Recognition](2101.06699.md)
**Cheng Yi, Shiyu Zhou, Bo Xu** · 2021-01-17

<details>
<summary>Abstract</summary>

End-to-end models have achieved impressive results on the task of automatic speech recognition (ASR). For low-resource ASR tasks, however, labeled data can hardly satisfy the demand of end-to-end models. Self-supervised acoustic pre-training has already shown its amazing ASR performance, while the transcription is still inadequate for language modeling in end-to-end models. In this work, we fuse a pre-trained acoustic encoder (wav2vec2.0) and a pre-trained linguistic encoder (BERT) into an end-to-end ASR model. The fused model only needs to learn the transfer from speech to language during fine-tuning on limited labeled data. The length of the two modalities is matched by a monotonic attention mechanism without additional parameters. Besides, a fully connected layer is introduced for the hidden mapping between modalities. We further propose a scheduled fine-tuning strategy to preserve and utilize the text context modeling ability of the pre-trained linguistic encoder. Experiments show our effective utilizing of pre-trained modules. Our model achieves better recognition performance on CALLHOME corpus (15 hours) than other end-to-end models.

</details>

### [A Novel Approach for Earthquake Early Warning System Design using Deep Learning Techniques](2101.06517.md)
**Tonumoy Mukherjee, Chandrani Singh, Prabir Kumar Biswas** · 2021-01-16

<details>
<summary>Abstract</summary>

Earthquake signals are non-stationary in nature and thus in real-time, it is difficult to identify and classify events based on classical approaches like peak ground displacement, peak ground velocity. Even the popular algorithm of STA/LTA requires extensive research to determine basic thresholding parameters so as to trigger an alarm. Also, many times due to human error or other unavoidable natural factors such as thunder strikes or landslides, the algorithm may end up raising a false alarm. This work focuses on detecting earthquakes by converting seismograph recorded data into corresponding audio signals for better perception and then uses popular Speech Recognition techniques of Filter bank coefficients and Mel Frequency Cepstral Coefficients (MFCC) to extract the features. These features were then used to train a Convolutional Neural Network(CNN) and a Long Short Term Memory(LSTM) network. The proposed method can overcome the above-mentioned problems and help in detecting earthquakes automatically from the waveforms without much human intervention. For the 1000Hz audio data set the CNN model showed a testing accuracy of 91.1% for 0.2-second sample window length while the LSTM model showed 93.99% for the same. A total of 610 sounds consisting of 310 earthquake sounds and 300 non-earthquake sounds were used to train the models. While testing, the total time required for generating the alarm was approximately 2 seconds which included individual times for data collection, processing, and prediction taking into consideration the processing and prediction delays. This shows the effectiveness of the proposed method for Earthquake Early Warning (EEW) applications. Since the input of the method is only the waveform, it is suitable for real-time processing, thus the models can also be used as an onsite EEW system requiring a minimum amount of preparation time and workload.

</details>

### [Fast offline Transformer-based end-to-end automatic speech recognition for real-world applications](2101.05600.md)
**Yoo Rhee Oh, Kiyoung Park, Jeon Gyu Park** · 2021-01-14

<details>
<summary>Abstract</summary>

With the recent advances in technology, automatic speech recognition (ASR) has been widely used in real-world applications. The efficiency of converting large amounts of speech into text accurately with limited resources has become more important than ever. This paper proposes a method to rapidly recognize a large speech database via a Transformer-based end-to-end model. Transformers have improved the state-of-the-art performance in many fields. However, they are not easy to use for long sequences. In this paper, various techniques to speed up the recognition of real-world speeches are proposed and tested, including decoding via multiple-utterance batched beam search, detecting end-of-speech based on a connectionist temporal classification (CTC), restricting the CTC prefix score, and splitting long speeches into short segments. Experiments are conducted with the Librispeech English and the real-world Korean ASR tasks to verify the proposed methods. From the experiments, the proposed system can convert 8 hours of speeches spoken at real-world meetings into text in less than 3 minutes with a 10.73% character error rate, which is 27.1% relatively lower than that of conventional systems.

</details>

### [An evaluation of word-level confidence estimation for end-to-end automatic speech recognition](2101.05525.md)
**Dan Oneata, Alexandru Caranica, Adriana Stan, Horia Cucu** · 2021-01-14

<details>
<summary>Abstract</summary>

Quantifying the confidence (or conversely the uncertainty) of a prediction is a highly desirable trait of an automatic system, as it improves the robustness and usefulness in downstream tasks. In this paper we investigate confidence estimation for end-to-end automatic speech recognition (ASR). Previous work has addressed confidence measures for lattice-based ASR, while current machine learning research mostly focuses on confidence measures for unstructured deep learning. However, as the ASR systems are increasingly being built upon deep end-to-end methods, there is little work that tries to develop confidence measures in this context. We fill this gap by providing an extensive benchmark of popular confidence methods on four well-known speech datasets. There are two challenges we overcome in adapting existing methods: working on structured data (sequences) and obtaining confidences at a coarser level than the predictions (words instead of tokens). Our results suggest that a strong baseline can be obtained by scaling the logits by a learnt temperature, followed by estimating the confidence as the negative entropy of the predictive distribution and, finally, sum pooling to aggregate at word level.

</details>

### [Speaker activity driven neural speech extraction](2101.05516.md)
**Marc Delcroix, Katerina Zmolikova, Tsubasa Ochiai, Keisuke Kinoshita et al.** · 2021-01-14

<details>
<summary>Abstract</summary>

Target speech extraction, which extracts the speech of a target speaker in a mixture given auxiliary speaker clues, has recently received increased interest. Various clues have been investigated such as pre-recorded enrollment utterances, direction information, or video of the target speaker. In this paper, we explore the use of speaker activity information as an auxiliary clue for single-channel neural network-based speech extraction. We propose a speaker activity driven speech extraction neural network (ADEnet) and show that it can achieve performance levels competitive with enrollment-based approaches, without the need for pre-recordings. We further demonstrate the potential of the proposed approach for processing meeting-like recordings, where the speaker activity is obtained from a diarization system. We show that this simple yet practical approach can successfully extract speakers after diarization, which results in improved ASR performance, especially in high overlapping conditions, with a relative word error rate reduction of up to 25%.

</details>

### [Robustness of on-device Models: Adversarial Attack to Deep Learning Models on Android Apps](2101.04401.md)
**Yujin Huang, Han Hu, Chunyang Chen** · 2021-01-12

<details>
<summary>Abstract</summary>

Deep learning has shown its power in many applications, including object detection in images, natural-language understanding, and speech recognition. To make it more accessible to end users, many deep learning models are now embedded in mobile apps. Compared to offloading deep learning from smartphones to the cloud, performing machine learning on-device can help improve latency, connectivity, and power consumption. However, most deep learning models within Android apps can easily be obtained via mature reverse engineering, while the models' exposure may invite adversarial attacks. In this study, we propose a simple but effective approach to hacking deep learning models using adversarial attacks by identifying highly similar pre-trained models from TensorFlow Hub. All 10 real-world Android apps in the experiment are successfully attacked by our approach. Apart from the feasibility of the model attack, we also carry out an empirical study that investigates the characteristics of deep learning models used by hundreds of Android apps on Google Play. The results show that many of them are similar to each other and widely use fine-tuning techniques to pre-trained models on the Internet.

</details>

### [BRDS: An FPGA-based LSTM Accelerator with Row-Balanced Dual-Ratio Sparsification](2101.02667.md)
**Seyed Abolfazl Ghasemzadeh, Erfan Bank Tavakoli, Mehdi Kamal, Ali Afzali-Kusha et al.** · 2021-01-07

<details>
<summary>Abstract</summary>

In this paper, first, a hardware-friendly pruning algorithm for reducing energy consumption and improving the speed of Long Short-Term Memory (LSTM) neural network accelerators is presented. Next, an FPGA-based platform for efficient execution of the pruned networks based on the proposed algorithm is introduced. By considering the sensitivity of two weight matrices of the LSTM models in pruning, different sparsity ratios (i.e., dual-ratio sparsity) are applied to these weight matrices. To reduce memory accesses, a row-wise sparsity pattern is adopted. The proposed hardware architecture makes use of computation overlapping and pipelining to achieve low-power and high-speed. The effectiveness of the proposed pruning algorithm and accelerator is assessed under some benchmarks for natural language processing, binary sentiment classification, and speech recognition. Results show that, e.g., compared to a recently published work in this field, the proposed accelerator could provide up to 272% higher effective GOPS/W and the perplexity error is reduced by up to 1.4% for the PTB dataset.

</details>

### [Data Quality Measures and Efficient Evaluation Algorithms for Large-Scale High-Dimensional Data](2101.01441.md)
**Hyeongmin Cho, Sangkyun Lee** · 2021-01-05

<details>
<summary>Abstract</summary>

Machine learning has been proven to be effective in various application areas, such as object and speech recognition on mobile systems. Since a critical key to machine learning success is the availability of large training data, many datasets are being disclosed and published online. From a data consumer or manager point of view, measuring data quality is an important first step in the learning process. We need to determine which datasets to use, update, and maintain. However, not many practical ways to measure data quality are available today, especially when it comes to large-scale high-dimensional data, such as images and videos. This paper proposes two data quality measures that can compute class separability and in-class variability, the two important aspects of data quality, for a given dataset. Classical data quality measures tend to focus only on class separability; however, we suggest that in-class variability is another important data quality factor. We provide efficient algorithms to compute our quality measures based on random projections and bootstrapping with statistical benefits on large-scale high-dimensional data. In experiments, we show that our measures are compatible with classical measures on small-scale data and can be computed much more efficiently on large-scale high-dimensional datasets.

</details>

### [Domain-aware Neural Language Models for Speech Recognition](2101.03229.md)
**Linda Liu, Yile Gu, Aditya Gourav, Ankur Gandhe et al.** · 2021-01-05

<details>
<summary>Abstract</summary>

As voice assistants become more ubiquitous, they are increasingly expected to support and perform well on a wide variety of use-cases across different domains. We present a domain-aware rescoring framework suitable for achieving domain-adaptation during second-pass rescoring in production settings. In our framework, we fine-tune a domain-general neural language model on several domains, and use an LSTM-based domain classification model to select the appropriate domain-adapted model to use for second-pass rescoring. This domain-aware rescoring improves the word error rate by up to 2.4% and slot word error rate by up to 4.1% on three individual domains -- shopping, navigation, and music -- compared to domain general rescoring. These improvements are obtained while maintaining accuracy for the general use case.

</details>

### [Generalized Spatio-Temporal RNN Beamformer for Target Speech Separation](2101.01280.md)
**Yong Xu, Zhuohuang Zhang, Meng Yu, Shi-Xiong Zhang et al.** · 2021-01-04

<details>
<summary>Abstract</summary>

Although the conventional mask-based minimum variance distortionless response (MVDR) could reduce the non-linear distortion, the residual noise level of the MVDR separated speech is still high. In this paper, we propose a spatio-temporal recurrent neural network based beamformer (RNN-BF) for target speech separation. This new beamforming framework directly learns the beamforming weights from the estimated speech and noise spatial covariance matrices. Leveraging on the temporal modeling capability of RNNs, the RNN-BF could automatically accumulate the statistics of the speech and noise covariance matrices to learn the frame-level beamforming weights in a recursive way. An RNN-based generalized eigenvalue (RNN-GEV) beamformer and a more generalized RNN beamformer (GRNN-BF) are proposed. We further improve the RNN-GEV and the GRNN-BF by using layer normalization to replace the commonly used mask normalization on the covariance matrices. The proposed GRNN-BF obtains better performance against prior arts in terms of speech quality (PESQ), speech-to-noise ratio (SNR) and word error rate (WER).

</details>

### [DEVI: Open-source Human-Robot Interface for Interactive Receptionist Systems](2101.00479.md)
**Ramesha Karunasena, Piumi Sandarenu, Madushi Pinto, Achala Athukorala et al.** · 2021-01-02

<details>
<summary>Abstract</summary>

Humanoid robots that act as human-robot interfaces equipped with social skills can assist people in many of their daily activities. Receptionist robots are one such application where social skills and appearance are of utmost importance. Many existing robot receptionist systems suffer from high cost and they do not disclose internal architectures for further development for robot researchers. Moreover, there does not exist customizable open-source robot receptionist frameworks to be deployed for any given application. In this paper we present an open-source robot receptionist intelligence core -- "DEVI"(means 'lady' in Sinhala), that provides researchers with ease of creating customized robot receptionists according to the requirements (cost, external appearance, and required processing power). Moreover, this paper also presents details on a prototype implementation of a physical robot using the DEVI system. The robot can give directional guidance with physical gestures, answer basic queries using a speech recognition and synthesis system, recognize and greet known people using face recognition and register new people in its database, using a self-learning neural network. Experiments conducted with DEVI show the effectiveness of the proposed system.

</details>

### [VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation Learning, Semi-Supervised Learning and Interpretation](2101.00390.md)
**Changhan Wang, Morgane Rivière, Ann Lee, Anne Wu et al.** · 2021-01-02

<details>
<summary>Abstract</summary>

We introduce VoxPopuli, a large-scale multilingual corpus providing 100K hours of unlabelled speech data in 23 languages. It is the largest open data to date for unsupervised representation learning as well as semi-supervised learning. VoxPopuli also contains 1.8K hours of transcribed speeches in 16 languages and their aligned oral interpretations into 5 other languages totaling 5.1K hours. We provide speech recognition baselines and validate the versatility of VoxPopuli unlabelled data in semi-supervised learning under challenging out-of-domain settings. We will release the corpus at https://github.com/facebookresearch/voxpopuli under an open license.

</details>

### [Adaptation Algorithms for Neural Network-Based Speech Recognition: An Overview](s2:178906286af4b31b45b2dbc267b3d51189a02181.md)
**P. Bell, Joachim Fainberg, Ondrej Klejch, Jinyu Li et al.** · 2021-01-01

<details>
<summary>Abstract</summary>

We present a structured overview of adaptation algorithms for neural network-based speech recognition, considering both hybrid hidden Markov model / neural network systems and end-to-end neural network systems, with a focus on speaker adaptation, domain adaptation, and accent adaptation. The overview characterizes adaptation algorithms as based on embeddings, model parameter adaptation, or data augmentation. We present a meta-analysis of the performance of speech recognition adaptation algorithms, based on relative error rate reductions as reported in the literature.

</details>

### [End-to-End Spoken Language Understanding using RNN-Transducer ASR](s2:0ff92a606b18eeade9b662c6a97ae8264a25e0d7.md)
**A. Raju, Gautam Tiwari, Milind Rao, Pranav Dheram et al.** · 2021-01-01

### [Cross Attention Augmented Transducer Networks for Simultaneous Translation](s2:df4f0c97d4ee2e28bb8a88fcc9a1c865a861fc69.md)
**Dan Liu, Mengge Du, Xiaoxi Li, Ya Li et al.** · 2021-01-01

<details>
<summary>Abstract</summary>

This paper proposes a novel architecture, Cross Attention Augmented Transducer (CAAT), for simultaneous translation. The framework aims to jointly optimize the policy and translation models. To effectively consider all possible READ-WRITE simultaneous translation action paths, we adapt the online automatic speech recognition (ASR) model, RNN-T, but remove the strong monotonic constraint, which is critical for the translation task to consider reordering. To make CAAT work, we introduce a novel latency loss whose expectation can be optimized by a forward-backward algorithm. We implement CAAT with Transformer while the general CAAT architecture can also be implemented with other attention-based encoder-decoder frameworks. Experiments on both speech-to-text (S2T) and text-to-text (T2T) simultaneous translation tasks show that CAAT achieves significantly better latency-quality trade-offs compared to the state-of-the-art simultaneous translation approaches.

</details>

