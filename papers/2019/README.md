# 2019

387 papers in this year.

### [Attention-based gated scaling adaptative acoustic model for ctc-based speech recognition](1912.13307.md)
**Fenglin Ding, Wu Guo, Lirong Dai, Jun Du** · 2019-12-31

<details>
<summary>Abstract</summary>

In this paper, we propose a novel adaptive technique that uses an attention-based gated scaling (AGS) scheme to improve deep feature learning for connectionist temporal classification (CTC) acoustic modeling. In AGS, the outputs of each hidden layer of the main network are scaled by an auxiliary gate matrix extracted from the lower layer by using attention mechanisms. Furthermore, the auxiliary AGS layer and the main network are jointly trained without requiring second-pass model training or additional speaker information, such as speaker code. On the Mandarin AISHELL-1 datasets, the proposed AGS yields a 7.94% character error rate (CER). To the best of our knowledge, this result is the best recognition accuracy achieved on this dataset by using an end-to-end framework.

</details>

### [Improved Multi-Stage Training of Online Attention-based Encoder-Decoder Models](1912.12384.md)
**Abhinav Garg, Dhananjaya Gowda, Ankur Kumar, Kwangyoun Kim et al.** · 2019-12-28

<details>
<summary>Abstract</summary>

In this paper, we propose a refined multi-stage multi-task training strategy to improve the performance of online attention-based encoder-decoder (AED) models. A three-stage training based on three levels of architectural granularity namely, character encoder, byte pair encoding (BPE) based encoder, and attention decoder, is proposed. Also, multi-task learning based on two-levels of linguistic granularity namely, character and BPE, is used. We explore different pre-training strategies for the encoders including transfer learning from a bidirectional encoder. Our encoder-decoder models with online attention show 35% and 10% relative improvement over their baselines for smaller and bigger models, respectively. Our models achieve a word error rate (WER) of 5.04% and 4.48% on the Librispeech test-clean data for the smaller and bigger models respectively after fusion with long short-term memory (LSTM) based external language model (LM).

</details>

### [Attention-based ASR with Lightweight and Dynamic Convolutions](1912.11793.md)
**Yuya Fujita, Aswin Shanmugam Subramanian, Motoi Omachi, Shinji Watanabe** · 2019-12-26

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) with sequence-to-sequence models has gained attention because of its simple model training compared with conventional hidden Markov model based ASR. Recently, several studies report the state-of-the-art E2E ASR results obtained by Transformer. Compared to recurrent neural network (RNN) based E2E models, training of Transformer is more efficient and also achieves better performance on various tasks. However, self-attention used in Transformer requires computation quadratic in its input length. In this paper, we propose to apply lightweight and dynamic convolution to E2E ASR as an alternative architecture to the self-attention to make the computational order linear. We also propose joint training with connectionist temporal classification, convolution on the frequency axis, and combination with self-attention. With these techniques, the proposed architectures achieve better performance than RNN-based E2E model and performance competitive to state-of-the-art Transformer on various ASR benchmarks including noisy/reverberant tasks.

</details>

### [Harnessing Evolution of Multi-Turn Conversations for Effective Answer Retrieval](1912.10554.md)
**Mohammad Aliannejadi, Manajit Chakraborty, Esteban Andrés Ríssola, Fabio Crestani** · 2019-12-22

<details>
<summary>Abstract</summary>

With the improvements in speech recognition and voice generation technologies over the last years, a lot of companies have sought to develop conversation understanding systems that run on mobile phones or smart home devices through natural language interfaces. Conversational assistants, such as Google Assistant and Microsoft Cortana, can help users to complete various types of tasks. This requires an accurate understanding of the user's information need as the conversation evolves into multiple turns. Finding relevant context in a conversation's history is challenging because of the complexity of natural language and the evolution of a user's information need. In this work, we present an extensive analysis of language, relevance, dependency of user utterances in a multi-turn information-seeking conversation. To this aim, we have annotated relevant utterances in the conversations released by the TREC CaST 2019 track. The annotation labels determine which of the previous utterances in a conversation can be used to improve the current one. Furthermore, we propose a neural utterance relevance model based on BERT fine-tuning, outperforming competitive baselines. We study and compare the performance of multiple retrieval models, utilizing different strategies to incorporate the user's context. The experimental results on both classification and retrieval tasks show that our proposed approach can effectively identify and incorporate the conversation context. We show that processing the current utterance using the predicted relevant utterance leads to a 38% relative improvement in terms of nDCG@20. Finally, to foster research in this area, we have released the dataset of the annotations.

</details>

### [power-law nonlinearity with maximally uniform distribution criterion for improved neural network training in automatic speech recognition](1912.11041.md)
**Chanwoo Kim, Mehul Kumar, Kwangyoun Kim, Dhananjaya Gowda** · 2019-12-22

<details>
<summary>Abstract</summary>

In this paper, we describe the Maximum Uniformity of Distribution (MUD) algorithm with the power-law nonlinearity. In this approach, we hypothesize that neural network training will become more stable if feature distribution is not too much skewed. We propose two different types of MUD approaches: power function-based MUD and histogram-based MUD. In these approaches, we first obtain the mel filterbank coefficients and apply nonlinearity functions for each filterbank channel. With the power function-based MUD, we apply a power-function based nonlinearity where power function coefficients are chosen to maximize the likelihood assuming that nonlinearity outputs follow the uniform distribution. With the histogram-based MUD, the empirical Cumulative Density Function (CDF) from the training database is employed to transform the original distribution into a uniform distribution. In MUD processing, we do not use any prior knowledge (e.g. logarithmic relation) about the energy of the incoming signal and the perceived intensity by a human. Experimental results using an end-to-end speech recognition system demonstrate that power-function based MUD shows better result than the conventional Mel Filterbank Cepstral Coefficients (MFCCs). On the LibriSpeech database, we could achieve 4.02 % WER on test-clean and 13.34 % WER on test-other without using any Language Models (LMs). The major contribution of this work is that we developed a new algorithm for designing the compressive nonlinearity in a data-driven way, which is much more flexible than the previous approaches and may be extended to other domains as well.

</details>

### [end-to-end training of a large vocabulary end-to-end speech recognition system](1912.11040.md)
**Chanwoo Kim, Sungsoo Kim, Kwangyoun Kim, Mehul Kumar et al.** · 2019-12-22

<details>
<summary>Abstract</summary>

In this paper, we present an end-to-end training framework for building state-of-the-art end-to-end speech recognition systems. Our training system utilizes a cluster of Central Processing Units(CPUs) and Graphics Processing Units (GPUs). The entire data reading, large scale data augmentation, neural network parameter updates are all performed "on-the-fly". We use vocal tract length perturbation [1] and an acoustic simulator [2] for data augmentation. The processed features and labels are sent to the GPU cluster. The Horovod allreduce approach is employed to train neural network parameters. We evaluated the effectiveness of our system on the standard Librispeech corpus [3] and the 10,000-hr anonymized Bixby English dataset. Our end-to-end speech recognition system built using this training infrastructure showed a 2.44 % WER on test-clean of the LibriSpeech test set after applying shallow fusion with a Transformer language model (LM). For the proprietary English Bixby open domain test set, we obtained a WER of 7.92 % using a Bidirectional Full Attention (BFA) end-to-end model after applying shallow fusion with an RNN-LM. When the monotonic chunckwise attention (MoCha) based approach is employed for streaming speech recognition, we obtained a WER of 9.95 % on the same Bixby open domain test set.

</details>

### [Theory-training deep neural networks for an alloy solidification benchmark problem](1912.09800.md)
**M. Torabi Rad, A. Viardin, G. J. Schmitz, M. Apel** · 2019-12-20

<details>
<summary>Abstract</summary>

Deep neural networks are machine learning tools that are transforming fields ranging from speech recognition to computational medicine. In this study, we extend their application to the field of alloy solidification modeling. To that end, and for the first time in the field, theory-trained deep neural networks (TTNs) for solidification are introduced. These networks are trained using the framework founded by Raissi et al.[1-3] and a theory that consists of a mathematical macroscale solidification model and the boundary and initial conditions of a well-known solidification benchmark problem. One of the main advantages of TTNs is that they do not need any prior knowledge of the solution of the governing equations or any external data for training. Using the built-in capabilities in TensorFlow, networks with different widths and depths are trained, and their predictions are examined in detail to verify that they satisfy both the model equations and the initial and boundary conditions of the benchmark problem. Issues that are critical in theory-training are identified, and guidelines that can be used in the future for successful and efficient training of similar networks are proposed. Through this study, theory-trained deep neural networks are shown to be a viable tool to simulate alloy solidification problems.

</details>

### [Generating Synthetic Audio Data for Attention-Based Speech Recognition Systems](1912.09257.md)
**Nick Rossenbach, Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2019-12-19

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) led to the development of flexible multi-speaker end-to-end TTS systems. We extend state-of-the-art attention-based automatic speech recognition (ASR) systems with synthetic audio generated by a TTS system trained only on the ASR corpora itself. ASR and TTS systems are built separately to show that text-only data can be used to enhance existing end-to-end ASR systems without the necessity of parameter or architecture changes. We compare our method with language model integration of the same text data and with simple data augmentation methods like SpecAugment and show that performance improvements are mostly independent. We achieve improvements of up to 33% relative in word-error-rate (WER) over a strong baseline with data-augmentation in a low-resource environment (LibriSpeech-100h), closing the gap to a comparable oracle experiment by more than 50\%. We also show improvements of up to 5% relative WER over our most recent ASR baseline on LibriSpeech-960h.

</details>

### [Detecting Adversarial Attacks On Audiovisual Speech Recognition](1912.08639.md)
**Pingchuan Ma, Stavros Petridis, Maja Pantic** · 2019-12-18

<details>
<summary>Abstract</summary>

Adversarial attacks pose a threat to deep learning models. However, research on adversarial detection methods, especially in the multi-modal domain, is very limited. In this work, we propose an efficient and straightforward detection method based on the temporal correlation between audio and video streams. The main idea is that the correlation between audio and video in adversarial examples will be lower than benign examples due to added adversarial noise. We use the synchronisation confidence score as a proxy for audiovisual correlation and based on it we can detect adversarial attacks. To the best of our knowledge, this is the first work on detection of adversarial attacks on audiovisual speech recognition models. We apply recent adversarial attacks on two audiovisual speech recognition models trained on the GRID and LRW datasets. The experimental results demonstrate that the proposed approach is an effective way for detecting such attacks.

</details>

### [A Cycle-GAN Approach to Model Natural Perturbations in Speech for ASR Applications](1912.11151.md)
**Sri Harsha Dumpala, Imran Sheikh, Rupayan Chakraborty, Sunil Kumar Kopparapu** · 2019-12-18

<details>
<summary>Abstract</summary>

Naturally introduced perturbations in audio signal, caused by emotional and physical states of the speaker, can significantly degrade the performance of Automatic Speech Recognition (ASR) systems. In this paper, we propose a front-end based on Cycle-Consistent Generative Adversarial Network (CycleGAN) which transforms naturally perturbed speech into normal speech, and hence improves the robustness of an ASR system. The CycleGAN model is trained on non-parallel examples of perturbed and normal speech. Experiments on spontaneous laughter-speech and creaky-speech datasets show that the performance of four different ASR systems improve by using speech obtained from CycleGAN based front-end, as compared to directly using the original perturbed speech. Visualization of the features of the laughter perturbed speech and those generated by the proposed front-end further demonstrates the effectiveness of our approach.

</details>

### [End-to-end training of time domain audio separation and recognition](1912.08462.md)
**Thilo von Neumann, Keisuke Kinoshita, Lukas Drude, Christoph Boeddeker et al.** · 2019-12-18

<details>
<summary>Abstract</summary>

The rising interest in single-channel multi-speaker speech separation sparked development of End-to-End (E2E) approaches to multi-speaker speech recognition. However, up until now, state-of-the-art neural network-based time domain source separation has not yet been combined with E2E speech recognition. We here demonstrate how to combine a separation module based on a Convolutional Time domain Audio Separation Network (Conv-TasNet) with an E2E speech recognizer and how to train such a model jointly by distributing it over multiple GPUs or by approximating truncated back-propagation for the convolutional front-end. To put this work into perspective and illustrate the complexity of the design space, we provide a compact overview of single-channel multi-speaker recognition systems. Our experiments show a word error rate of 11.0% on WSJ0-2mix and indicate that our joint time domain model can yield substantial improvements over cascade DNN-HMM and monolithic E2E frequency domain systems proposed so far.

</details>

### [Application of Word2vec in Phoneme Recognition](1912.08011.md)
**Xin Feng, Lei Wang** · 2019-12-17

<details>
<summary>Abstract</summary>

In this paper, we present how to hybridize a Word2vec model and an attention-based end-to-end speech recognition model. We build a phoneme recognition system based on Listen, Attend and Spell model. And the phoneme recognition model uses a word2vec model to initialize the embedding matrix for the improvement of the performance, which can increase the distance among the phoneme vectors. At the same time, in order to solve the problem of overfitting in the 61 phoneme recognition model on TIMIT dataset, we propose a new training method. A 61-39 phoneme mapping comparison table is used to inverse map the phonemes of the dataset to generate more 61 phoneme training data. At the end of training, replace the dataset with a standard dataset for corrective training. Our model can achieve the best result under the TIMIT dataset which is 16.5% PER (Phoneme Error Rate).

</details>

### [Libri-Light: A Benchmark for ASR with Limited or No Supervision](1912.07875.md)
**Jacob Kahn, Morgane Rivière, Weiyi Zheng, Evgeny Kharitonov et al.** · 2019-12-17

<details>
<summary>Abstract</summary>

We introduce a new collection of spoken English audio suitable for training speech recognition systems under limited or no supervision. It is derived from open-source audio books from the LibriVox project. It contains over 60K hours of audio, which is, to our knowledge, the largest freely-available corpus of speech. The audio has been segmented using voice activity detection and is tagged with SNR, speaker ID and genre descriptions. Additionally, we provide baseline systems and evaluation metrics working under three settings: (1) the zero resource/unsupervised setting (ABX), (2) the semi-supervised setting (PER, CER) and (3) the distant supervision setting (WER). Settings (2) and (3) use limited textual resources (10 minutes to 10 hours) aligned with the speech. Setting (3) uses large amounts of unaligned text. They are evaluated on the standard LibriSpeech dev and test sets for comparison with the supervised state-of-the-art.

</details>

### [Synchronous Speech Recognition and Speech-to-Text Translation with Interactive Decoding](1912.07240.md)
**Yuchen Liu, Jiajun Zhang, Hao Xiong, Long Zhou et al.** · 2019-12-16

<details>
<summary>Abstract</summary>

Speech-to-text translation (ST), which translates source language speech into target language text, has attracted intensive attention in recent years. Compared to the traditional pipeline system, the end-to-end ST model has potential benefits of lower latency, smaller model size, and less error propagation. However, it is notoriously difficult to implement such a model without transcriptions as intermediate. Existing works generally apply multi-task learning to improve translation quality by jointly training end-to-end ST along with automatic speech recognition (ASR). However, different tasks in this method cannot utilize information from each other, which limits the improvement. Other works propose a two-stage model where the second model can use the hidden state from the first one, but its cascade manner greatly affects the efficiency of training and inference process. In this paper, we propose a novel interactive attention mechanism which enables ASR and ST to perform synchronously and interactively in a single model. Specifically, the generation of transcriptions and translations not only relies on its previous outputs but also the outputs predicted in the other task. Experiments on TED speech translation corpora have shown that our proposed model can outperform strong baselines on the quality of speech translation and achieve better speech recognition performances as well.

</details>

### [Personalization of End-to-end Speech Recognition On Mobile Devices For Named Entities](1912.09251.md)
**Khe Chai Sim, Françoise Beaufays, Arnaud Benard, Dhruv Guliani et al.** · 2019-12-14

<details>
<summary>Abstract</summary>

We study the effectiveness of several techniques to personalize end-to-end speech models and improve the recognition of proper names relevant to the user. These techniques differ in the amounts of user effort required to provide supervision, and are evaluated on how they impact speech recognition performance. We propose using keyword-dependent precision and recall metrics to measure vocabulary acquisition performance. We evaluate the algorithms on a dataset that we designed to contain names of persons that are difficult to recognize. Therefore, the baseline recall rate for proper names in this dataset is very low: 2.4%. A data synthesis approach we developed brings it to 48.6%, with no need for speech input from the user. With speech input, if the user corrects only the names, the name recall rate improves to 64.4%. If the user corrects all the recognition errors, we achieve the best recall of 73.5%. To eliminate the need to upload user data and store personalized models on a server, we focus on performing the entire personalization workflow on a mobile device.

</details>

### [Common Voice: A Massively-Multilingual Speech Corpus](1912.06670.md)
**Rosana Ardila, Megan Branson, Kelly Davis, Michael Henretty et al.** · 2019-12-13

<details>
<summary>Abstract</summary>

The Common Voice corpus is a massively-multilingual collection of transcribed speech intended for speech technology research and development. Common Voice is designed for Automatic Speech Recognition purposes but can be useful in other domains (e.g. language identification). To achieve scale and sustainability, the Common Voice project employs crowdsourcing for both data collection and data validation. The most recent release includes 29 languages, and as of November 2019 there are a total of 38 languages collecting data. Over 50,000 individuals have participated so far, resulting in 2,500 hours of collected audio. To our knowledge this is the largest audio corpus in the public domain for speech recognition, both in terms of number of hours and number of languages. As an example use case for Common Voice, we present speech recognition experiments using Mozilla's DeepSpeech Speech-to-Text toolkit. By applying transfer learning from a source English model, we find an average Character Error Rate improvement of 5.99 +/- 5.48 for twelve target languages (German, French, Italian, Turkish, Catalan, Slovenian, Welsh, Irish, Breton, Tatar, Chuvash, and Kabyle). For most of these languages, these are the first ever published results on end-to-end Automatic Speech Recognition.

</details>

### [SpecAugment on Large Scale Datasets](1912.05533.md)
**Daniel S. Park, Yu Zhang, Chung-Cheng Chiu, Youzheng Chen et al.** · 2019-12-11

<details>
<summary>Abstract</summary>

Recently, SpecAugment, an augmentation scheme for automatic speech recognition that acts directly on the spectrogram of input utterances, has shown to be highly effective in enhancing the performance of end-to-end networks on public datasets. In this paper, we demonstrate its effectiveness on tasks with large scale datasets by investigating its application to the Google Multidomain Dataset (Narayanan et al., 2018). We achieve improvement across all test domains by mixing raw training data augmented with SpecAugment and noise-perturbed training data when training the acoustic model. We also introduce a modification of SpecAugment that adapts the time mask size and/or multiplicity depending on the length of the utterance, which can potentially benefit large scale tasks. By using adaptive masking, we are able to further improve the performance of the Listen, Attend and Spell model on LibriSpeech to 2.2% WER on test-clean and 5.2% WER on test-other.

</details>

### [Leveraging End-to-End Speech Recognition with Neural Architecture Search](1912.05946.md)
**Ahmed Baruwa, Mojeed Abisiga, Ibrahim Gbadegesin, Afeez Fakunle** · 2019-12-11

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been demonstrated to outperform many traditional machine learning algorithms in Automatic Speech Recognition (ASR). In this paper, we show that a large improvement in the accuracy of deep speech models can be achieved with effective Neural Architecture Optimization at a very low computational cost. Phone recognition tests with the popular LibriSpeech and TIMIT benchmarks proved this fact by displaying the ability to discover and train novel candidate models within a few hours (less than a day) many times faster than the attention-based seq2seq models. Our method achieves test error of 7% Word Error Rate (WER) on the LibriSpeech corpus and 13% Phone Error Rate (PER) on the TIMIT corpus, on par with state-of-the-art results.

</details>

### [A Novel Topology for End-to-end Temporal Classification and Segmentation with Recurrent Neural Network](1912.04784.md)
**Taiyang Zhao** · 2019-12-10

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) has matured as an alignment free to sequence transduction and shows competitive for end-to-end speech recognition. In the CTC topology, the blank symbol occupies more than half of the state trellis, which results the spike phenomenon of the non-blank symbols. For classification task, the spikes work quite well, but as to the segmentation task it does not provide boundaries information. In this paper, a novel topology is introduced to combine the temporal classification and segmentation ability in one framework.

</details>

### [Audio-attention discriminative language model for ASR rescoring](1912.03363.md)
**Ankur Gandhe, Ariya Rastrow** · 2019-12-06

<details>
<summary>Abstract</summary>

End-to-end approaches for automatic speech recognition (ASR) benefit from directly modeling the probability of the word sequence given the input audio stream in a single neural network. However, compared to conventional ASR systems, these models typically require more data to achieve comparable results. Well-known model adaptation techniques, to account for domain and style adaptation, are not easily applicable to end-to-end systems. Conventional HMM-based systems, on the other hand, have been optimized for various production environments and use cases. In this work, we propose to combine the benefits of end-to-end approaches with a conventional system using an attention-based discriminative language model that learns to rescore the output of a first-pass ASR system. We show that learning to rescore a list of potential ASR outputs is much simpler than learning to generate the hypothesis. The proposed model results in 8% improvement in word error rate even when the amount of training data is a fraction of data used for training the first-pass system.

</details>

### [Visualizing Deep Neural Networks for Speech Recognition with Learned Topographic Filter Maps](1912.04067.md)
**Andreas Krug, Sebastian Stober** · 2019-12-06

<details>
<summary>Abstract</summary>

The uninformative ordering of artificial neurons in Deep Neural Networks complicates visualizing activations in deeper layers. This is one reason why the internal structure of such models is very unintuitive. In neuroscience, activity of real brains can be visualized by highlighting active regions. Inspired by those techniques, we train a convolutional speech recognition model, where filters are arranged in a 2D grid and neighboring filters are similar to each other. We show, how those topographic filter maps visualize artificial neuron activations more intuitively. Moreover, we investigate, whether this causes phoneme-responsive neurons to be grouped in certain regions of the topographic map.

</details>

### [Semantic Mask for Transformer based End-to-End Speech Recognition](1912.03010.md)
**Chengyi Wang, Yu Wu, Yujiao Du, Jinyu Li et al.** · 2019-12-06

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder model has achieved impressive results for both automatic speech recognition (ASR) and text-to-speech (TTS) tasks. This approach takes advantage of the memorization capacity of neural networks to learn the mapping from the input sequence to the output sequence from scratch, without the assumption of prior knowledge such as the alignments. However, this model is prone to overfitting, especially when the amount of training data is limited. Inspired by SpecAugment and BERT, in this paper, we propose a semantic mask based regularization for training such kind of end-to-end (E2E) model. The idea is to mask the input features corresponding to a particular output token, e.g., a word or a word-piece, in order to encourage the model to fill the token based on the contextual information. While this approach is applicable to the encoder-decoder framework with any type of neural network architecture, we study the transformer-based model for ASR in this work. We perform experiments on Librispeech 960h and TedLium2 data sets, and achieve the state-of-the-art performance on the test set in the scope of E2E models.

</details>

### [Synchronous Transformers for End-to-End Speech Recognition](1912.02958.md)
**Zhengkun Tian, Jiangyan Yi, Ye Bai, Jianhua Tao et al.** · 2019-12-06

<details>
<summary>Abstract</summary>

For most of the attention-based sequence-to-sequence models, the decoder predicts the output sequence conditioned on the entire input sequence processed by the encoder. The asynchronous problem between the encoding and decoding makes these models difficult to be applied for online speech recognition. In this paper, we propose a model named synchronous transformer to address this problem, which can predict the output sequence chunk by chunk. Once a fixed-length chunk of the input sequence is processed by the encoder, the decoder begins to predict symbols immediately. During training, a forward-backward algorithm is introduced to optimize all the possible alignment paths. Our model is evaluated on a Mandarin dataset AISHELL-1. The experiments show that the synchronous transformer is able to perform encoding and decoding synchronously, and achieves a character error rate of 8.91% on the test set.

</details>

### [Integrating Knowledge into End-to-End Speech Recognition from External Text-Only Data](1912.01777.md)
**Ye Bai, Jiangyan Yi, Jianhua Tao, Zhengqi Wen et al.** · 2019-12-04

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder (AED) models have achieved promising performance in speech recognition. However, because of the end-to-end training, an AED model is usually trained with speech-text paired data. It is challenging to incorporate external text-only data into AED models. Another issue of the AED model is that it does not use the right context of a text token while predicting the token. To alleviate the above two issues, we propose a unified method called LST (Learn Spelling from Teachers) to integrate knowledge into an AED model from the external text-only data and leverage the whole context in a sentence. The method is divided into two stages. First, in the representation stage, a language model is trained on the text. It can be seen as that the knowledge in the text is compressed into the LM. Then, at the transferring stage, the knowledge is transferred to the AED model via teacher-student learning. To further use the whole context of the text sentence, we propose an LM called causal cloze completer (COR), which estimates the probability of a token, given both the left context and the right context of it. Therefore, with LST training, the AED model can leverage the whole context in the sentence. Different from fusion based methods, which use LM during decoding, the proposed method does not increase any extra complexity at the inference stage. We conduct experiments on two scales of public Chinese datasets AISHELL-1 and AISHELL-2. The experimental results demonstrate the effectiveness of leveraging external text-only data and the whole context in a sentence with our proposed method, compared with baseline hybrid systems and AED model based systems.

</details>

### [Deep Contextualized Acoustic Representations For Semi-Supervised Speech Recognition](1912.01679.md)
**Shaoshi Ling, Yuzong Liu, Julian Salazar, Katrin Kirchhoff** · 2019-12-03

<details>
<summary>Abstract</summary>

We propose a novel approach to semi-supervised automatic speech recognition (ASR). We first exploit a large amount of unlabeled audio data via representation learning, where we reconstruct a temporal slice of filterbank features from past and future context frames. The resulting deep contextualized acoustic representations (DeCoAR) are then used to train a CTC-based end-to-end ASR system using a smaller amount of labeled audio data. In our experiments, we show that systems trained on DeCoAR consistently outperform ones trained on conventional filterbank features, giving 42% and 19% relative improvement over the baseline on WSJ eval92 and LibriSpeech test-clean, respectively. Our approach can drastically reduce the amount of labeled data required; unsupervised training on LibriSpeech then supervision with 100 hours of labeled data achieves performance on par with training on all 960 hours directly. Pre-trained models and code will be released online.

</details>

### [Language Model Bootstrapping Using Neural Machine Translation For Conversational Speech Recognition](1912.00958.md)
**Surabhi Punjabi, Harish Arsikere, Sri Garimella** · 2019-12-02

<details>
<summary>Abstract</summary>

Building conversational speech recognition systems for new languages is constrained by the availability of utterances that capture user-device interactions. Data collection is both expensive and limited by the speed of manual transcription. In order to address this, we advocate the use of neural machine translation as a data augmentation technique for bootstrapping language models. Machine translation (MT) offers a systematic way of incorporating collections from mature, resource-rich conversational systems that may be available for a different language. However, ingesting raw translations from a general purpose MT system may not be effective owing to the presence of named entities, intra sentential code-switching and the domain mismatch between the conversational data being translated and the parallel text used for MT training. To circumvent this, we explore the following domain adaptation techniques: (a) sentence embedding based data selection for MT training, (b) model finetuning, and (c) rescoring and filtering translated hypotheses. Using Hindi as the experimental testbed, we translate US English utterances to supplement the transcribed collections. We observe a relative word error rate reduction of 7.8-15.6%, depending on the bootstrapping phase. Fine grained analysis reveals that translation particularly aids the interaction scenarios which are underrepresented in the transcribed data.

</details>

### [Streaming End-to-End Speech Recognition with Joint CTC-Attention Based Models](s2:15342c138f57c736a54d97b11a363857651730e3.md)
**Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2019-12-01

<details>
<summary>Abstract</summary>

In this paper, we present a one-pass decoding algorithm for streaming recognition with joint connectionist temporal classification (CTC) and attention-based end-to-end automatic speech recognition (ASR) models. The decoding scheme is based on a frame-synchronous CTC prefix beam search algorithm and the recently proposed triggered attention concept. To achieve a fully streaming end-to-end ASR system, the CTC-triggered attention decoder is combined with a unidirectional encoder neural network based on parallel time-delayed long short-term memory (PTDLSTM) streams, which has demonstrated superior performance compared to various other streaming encoder architectures in earlier work. A new type of pre-training method is studied to further improve our streaming ASR models by adding residual connections to the encoder neural network and layer-wise removing them during the training process. The proposed joint CTC-triggered attention decoding algorithm, which enables streaming recognition of attention-based ASR systems, achieves similar ASR results compared to offline CTC-attention decoding and significantly better results compared to CTC prefix beam search decoding alone.

</details>

### [Real-Time Voice Transmission over Wireless Sensor Network (VoWSN) based Automatic Speech Recognition (ASR) Technique](s2:78ab4305a9bb4cd0b43356c207ed19ffdfba5aac.md)
**Ina'am Fathi, Qutaiba Ibrahim, J. Abdul-Jabbar** · 2019-12-01

<details>
<summary>Abstract</summary>

The speech recognition process under the embedded system with constrained resources represents a challenge in terms of processing capability, storage memory, and B.W (or data rate). So, in this paper an efficient Real-Time Voice over Wireless sensor network (VoWSN) platform based on Automatic Speech Recognition (ASR) system to be used in emergency scenarios is proposed, implemented and evaluated. The workflow principle of the proposed system is depending on a Category Transformation Protocol (CTP) that transforms system category gradually from network dependent ASR system with a full dictionary and language model (i.e. large vocabulary) to fully embedded ASR system with customized dictionary and language model (i.e. small vocabulary ). Moreover, a comparison study has been performed between our proposed VoWSN based ASR system and a VoWSN based streaming system. This comparison is performed to elaborate the gains achieved when sending the text of the voice signal instead of sending the voice signal. Additionally, the Voice over IoTs (VoIoTs) system has been evaluated utilizing Voice streaming or ASR system to evaluate the system performance when connecting to the Internet. The comparison evaluation process is achieved by means of experimental platform and simulation.

</details>

### [Zero-Shot Code-Switching ASR and TTS with Multilingual Machine Speech Chain](s2:4445177e6990ce853c3d5a2f46feb835405bb2cf.md)
**Sahoko Nakayama, Andros Tjandra, S. Sakti, Satoshi Nakamura** · 2019-12-01

<details>
<summary>Abstract</summary>

Constructing automatic speech recognition (ASR) and text-to-speech (TTS) for code-switching in a supervised fashion poses a challenge since a large amount of code-switching speech and the corresponding transcription are usually unavailable. The machine speech chain mechanism can be utilized to achieve semi-supervised learning. The framework enables ASR and TTS to assist each other when they receive unpaired data since it allows them to infer the missing pair and optimize the models with reconstruction loss. In this study, we handle multiple language pairs of code-switching by integrating language embeddings into the machine speech chain and investigate whether the model can perform with code-switching language pairs that are never explicitly seen during training. Experimental results reveal that the proposed approach improves the performance of the multilingual code-switching language pairs with which the model was trained and can also perform with unknown code-switching language pairs without directly learning on it.

</details>

### [Biometrics Recognition Using Deep Learning: A Survey](1912.00271.md)
**Shervin Minaee, Amirali Abdolrashidi, Hang Su, Mohammed Bennamoun et al.** · 2019-11-30

<details>
<summary>Abstract</summary>

Deep learning-based models have been very successful in achieving state-of-the-art results in many of the computer vision, speech recognition, and natural language processing tasks in the last few years. These models seem a natural fit for handling the ever-increasing scale of biometric recognition problems, from cellphone authentication to airport security systems. Deep learning-based models have increasingly been leveraged to improve the accuracy of different biometric recognition systems in recent years. In this work, we provide a comprehensive survey of more than 120 promising works on biometric recognition (including face, fingerprint, iris, palmprint, ear, voice, signature, and gait recognition), which deploy deep learning models, and show their strengths and potentials in different applications. For each biometric, we first introduce the available datasets that are widely used in the literature and their characteristics. We will then talk about several promising deep learning works developed for that biometric, and show their performance on popular public benchmarks. We will also discuss some of the main challenges while using these models for biometric recognition, and possible future directions to which research in this area is headed.

</details>

### [Improving Voice Separation by Incorporating End-to-end Speech Recognition](1911.12928.md)
**Naoya Takahashi, Mayank Kumar Singh, Sakya Basak, Parthasaarathy Sudarsanam et al.** · 2019-11-29

<details>
<summary>Abstract</summary>

Despite recent advances in voice separation methods, many challenges remain in realistic scenarios such as noisy recording and the limits of available data. In this work, we propose to explicitly incorporate the phonetic and linguistic nature of speech by taking a transfer learning approach using an end-to-end automatic speech recognition (E2EASR) system. The voice separation is conditioned on deep features extracted from E2EASR to cover the long-term dependence of phonetic aspects. Experimental results on speech separation and enhancement task on the AVSpeech dataset show that the proposed method significantly improves the signal-to-distortion ratio over the baseline model and even outperforms an audio visual model, that utilizes visual information of lip movements.

</details>

### [Multimodal Machine Translation through Visuals and Speech](1911.12798.md)
**Umut Sulubacak, Ozan Caglayan, Stig-Arne Grönroos, Aku Rouhe et al.** · 2019-11-28

<details>
<summary>Abstract</summary>

Multimodal machine translation involves drawing information from more than one modality, based on the assumption that the additional modalities will contain useful alternative views of the input data. The most prominent tasks in this area are spoken language translation, image-guided translation, and video-guided translation, which exploit audio and visual modalities, respectively. These tasks are distinguished from their monolingual counterparts of speech recognition, image captioning, and video captioning by the requirement of models to generate outputs in a different language. This survey reviews the major data resources for these tasks, the evaluation campaigns concentrated around them, the state of the art in end-to-end and pipeline approaches, and also the challenges in performance evaluation. The paper concludes with a discussion of directions for future research in these areas: the need for more expansive and challenging datasets, for targeted evaluations of model performance, and for multimodality in both the input and output space.

</details>

### [Minimum Bayes Risk Training of RNN-Transducer for End-to-End Speech Recognition](1911.12487.md)
**Chao Weng, Chengzhu Yu, Jia Cui, Chunlei Zhang et al.** · 2019-11-28

<details>
<summary>Abstract</summary>

In this work, we propose minimum Bayes risk (MBR) training of RNN-Transducer (RNN-T) for end-to-end speech recognition. Specifically, initialized with a RNN-T trained model, MBR training is conducted via minimizing the expected edit distance between the reference label sequence and on-the-fly generated N-best hypothesis. We also introduce a heuristic to incorporate an external neural network language model (NNLM) in RNN-T beam search decoding and explore MBR training with the external NNLM. Experimental results demonstrate an MBR trained model outperforms a RNN-T trained model substantially and further improvements can be achieved if trained with an external NNLM. Our best MBR trained system achieves absolute character error rate (CER) reductions of 1.2% and 0.5% on read and spontaneous Mandarin speech respectively over a strong convolution and transformer based RNN-T baseline trained on ~21,000 hours of speech.

</details>

### [Designing the Next Generation of Intelligent Personal Robotic Assistants for the Physically Impaired](1911.12482.md)
**Basit Ayantunde, Jane Odum, Fadlullah Olawumi, Joshua Olalekan** · 2019-11-28

<details>
<summary>Abstract</summary>

The physically impaired commonly have difficulties performing simple routine tasks without relying on other individuals who are not always readily available and thus make them strive for independence. While their impaired abilities can in many cases be augmented (to certain degrees) with the use of assistive technologies, there has been little attention to their applications in embodied AI with assistive technologies. This paper presents the modular framework, architecture, and design of the mid-fidelity prototype of MARVIN: an artificial-intelligence-powered robotic assistant designed to help the physically impaired in performing simple day-to-day tasks. The prototype features a trivial locomotion unit and also utilizes various state-of-the-art neural network architectures for specific modular components of the system. These components perform specialized functions, such as automatic speech recognition, object detection, natural language understanding, speech synthesis, etc. We also discuss the constraints, challenges encountered, potential future applications and improvements towards succeeding prototypes.

</details>

### [AIPNet: Generative Adversarial Pre-training of Accent-invariant Networks for End-to-end Speech Recognition](1911.11935.md)
**Yi-Chen Chen, Zhaojun Yang, Ching-Feng Yeh, Mahaveer Jain et al.** · 2019-11-27

<details>
<summary>Abstract</summary>

As one of the major sources in speech variability, accents have posed a grand challenge to the robustness of speech recognition systems. In this paper, our goal is to build a unified end-to-end speech recognition system that generalizes well across accents. For this purpose, we propose a novel pre-training framework AIPNet based on generative adversarial nets (GAN) for accent-invariant representation learning: Accent Invariant Pre-training Networks. We pre-train AIPNet to disentangle accent-invariant and accent-specific characteristics from acoustic features through adversarial training on accented data for which transcriptions are not necessarily available. We further fine-tune AIPNet by connecting the accent-invariant module with an attention-based encoder-decoder model for multi-accent speech recognition. In the experiments, our approach is compared against four baselines including both accent-dependent and accent-independent models. Experimental results on 9 English accents show that the proposed approach outperforms all the baselines by 2.3 \sim 4.5% relative reduction on average WER when transcriptions are available in all accents and by 1.6 \sim 6.1% relative reduction when transcriptions are only available in US accent.

</details>

### [Automatic prediction of suicidal risk in military couples using multimodal interaction cues from couples conversations](1911.11927.md)
**Sandeep Nallan Chakravarthula, Md Nasir, Shao-Yen Tseng, Haoqi Li et al.** · 2019-11-27

<details>
<summary>Abstract</summary>

Suicide is a major societal challenge globally, with a wide range of risk factors, from individual health, psychological and behavioral elements to socio-economic aspects. Military personnel, in particular, are at especially high risk. Crisis resources, while helpful, are often constrained by access to clinical visits or therapist availability, especially when needed in a timely manner. There have hence been efforts on identifying whether communication patterns between couples at home can provide preliminary information about potential suicidal behaviors, prior to intervention. In this work, we investigate whether acoustic, lexical, behavior and turn-taking cues from military couples' conversations can provide meaningful markers of suicidal risk. We test their effectiveness in real-world noisy conditions by extracting these cues through an automatic diarization and speech recognition front-end. Evaluation is performed by classifying 3 degrees of suicidal risk: none, ideation, attempt. Our automatic system performs significantly better than chance in all classification scenarios and we find that behavior and turn-taking cues are the most informative ones. We also observe that conditioning on factors such as speaker gender and topic of discussion tends to improve classification performance.

</details>

### [Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers](1911.11502.md)
**Ya Zhao, Rui Xu, Xinchao Wang, Peng Hou et al.** · 2019-11-26

<details>
<summary>Abstract</summary>

Lip reading has witnessed unparalleled development in recent years thanks to deep learning and the availability of large-scale datasets. Despite the encouraging results achieved, the performance of lip reading, unfortunately, remains inferior to the one of its counterpart speech recognition, due to the ambiguous nature of its actuations that makes it challenging to extract discriminant features from the lip movement videos. In this paper, we propose a new method, termed as Lip by Speech (LIBS), of which the goal is to strengthen lip reading by learning from speech recognizers. The rationale behind our approach is that the features extracted from speech recognizers may provide complementary and discriminant clues, which are formidable to be obtained from the subtle movements of the lips, and consequently facilitate the training of lip readers. This is achieved, specifically, by distilling multi-granularity knowledge from speech recognizers to lip readers. To conduct this cross-modal knowledge distillation, we utilize an efficacious alignment scheme to handle the inconsistent lengths of the audios and videos, as well as an innovative filtering strategy to refine the speech recognizer's prediction. The proposed method achieves the new state-of-the-art performance on the CMLR and LRS2 datasets, outperforming the baseline by a margin of 7.66% and 2.75% in character error rate, respectively.

</details>

### [Independent language modeling architecture for end-to-end ASR](1912.00863.md)
**Van Tung Pham, Haihua Xu, Yerbolat Khassanov, Zhiping Zeng et al.** · 2019-11-25

<details>
<summary>Abstract</summary>

The attention-based end-to-end (E2E) automatic speech recognition (ASR) architecture allows for joint optimization of acoustic and language models within a single network. However, in a vanilla E2E ASR architecture, the decoder sub-network (subnet), which incorporates the role of the language model (LM), is conditioned on the encoder output. This means that the acoustic encoder and the language model are entangled that doesn't allow language model to be trained separately from external text data. To address this problem, in this work, we propose a new architecture that separates the decoder subnet from the encoder output. In this way, the decoupled subnet becomes an independently trainable LM subnet, which can easily be updated using the external text data. We study two strategies for updating the new architecture. Experimental results show that, 1) the independent LM architecture benefits from external text data, achieving 9.3% and 22.8% relative character and word error rate reduction on Mandarin HKUST and English NSC datasets respectively; 2)the proposed architecture works well with external LM and can be generalized to different amount of labelled data.

</details>

### [Recurrent Neural Networks (RNNs): A gentle Introduction and Overview](1912.05911.md)
**Robin M. Schmidt** · 2019-11-23

<details>
<summary>Abstract</summary>

State-of-the-art solutions in the areas of "Language Modelling & Generating Text", "Speech Recognition", "Generating Image Descriptions" or "Video Tagging" have been using Recurrent Neural Networks as the foundation for their approaches. Understanding the underlying concepts is therefore of tremendous importance if we want to keep up with recent or upcoming publications in those areas. In this work we give a short overview over some of the most important concepts in the realm of Recurrent Neural Networks which enables readers to easily understand the fundamentals such as but not limited to "Backpropagation through Time" or "Long Short-Term Memory Units" as well as some of the more recent advances like the "Attention Mechanism" or "Pointer Networks". We also give recommendations for further reading regarding more complex topics where it is necessary.

</details>

### [Improving N-gram Language Models with Pre-trained Deep Transformer](1911.10235.md)
**Yiren Wang, Hongzhao Huang, Zhe Liu, Yutong Pang et al.** · 2019-11-22

<details>
<summary>Abstract</summary>

Although n-gram language models (LMs) have been outperformed by the state-of-the-art neural LMs, they are still widely used in speech recognition due to its high efficiency in inference. In this paper, we demonstrate that n-gram LM can be improved by neural LMs through a text generation based data augmentation method. In contrast to previous approaches, we employ a large-scale general domain pre-training followed by in-domain fine-tuning strategy to construct deep Transformer based neural LMs. Large amount of in-domain text data is generated with the well trained deep Transformer to construct new n-gram LMs, which are then interpolated with baseline n-gram systems. Empirical studies on different speech recognition tasks show that the proposed approach can effectively improve recognition accuracy. In particular, our proposed approach brings significant relative word error rate reduction up to 6.0% for domains with limited in-domain data.

</details>

### [Cantonese Automatic Speech Recognition Using Transfer Learning from Mandarin](1911.09271.md)
**Bryan Li, Xinyue Wang, Homayoon Beigi** · 2019-11-21

<details>
<summary>Abstract</summary>

We propose a system to develop a basic automatic speech recognizer(ASR) for Cantonese, a low-resource language, through transfer learning of Mandarin, a high-resource language. We take a time-delayed neural network trained on Mandarin, and perform weight transfer of several layers to a newly initialized model for Cantonese. We experiment with the number of layers transferred, their learning rates, and pretraining i-vectors. Key findings are that this approach allows for quicker training time with less data. We find that for every epoch, log-probability is smaller for transfer learning models compared to a Cantonese-only model. The transfer learning models show slight improvement in CER.

</details>

### [Speech Sentiment Analysis via Pre-trained Features from End-to-end ASR Models](1911.09762.md)
**Zhiyun Lu, Liangliang Cao, Yu Zhang, Chung-Cheng Chiu et al.** · 2019-11-21

<details>
<summary>Abstract</summary>

In this paper, we propose to use pre-trained features from end-to-end ASR models to solve speech sentiment analysis as a down-stream task. We show that end-to-end ASR features, which integrate both acoustic and text information from speech, achieve promising results. We use RNN with self-attention as the sentiment classifier, which also provides an easy visualization through attention weights to help interpret model predictions. We use well benchmarked IEMOCAP dataset and a new large-scale speech sentiment dataset SWBD-sentiment for evaluation. Our approach improves the-state-of-the-art accuracy on IEMOCAP from 66.6% to 71.7%, and achieves an accuracy of 70.10% on SWBD-sentiment with more than 49,500 utterances.

</details>

### [On using 2D sequence-to-sequence models for speech recognition](1911.08888.md)
**Parnia Bahar, Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2019-11-20

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence models have shown promising results in automatic speech recognition. Using these architectures, one-dimensional input and output sequences are related by an attention approach, thereby replacing more explicit alignment processes, like in classical HMM-based modeling. In contrast, here we apply a novel two-dimensional long short-term memory (2DLSTM) architecture to directly model the input/output relation between audio/feature vector sequences and word sequences. The proposed model is an alternative model such that instead of using any type of attention components, we apply a 2DLSTM layer to assimilate the context from both input observations and output transcriptions. The experimental evaluation on the Switchboard 300h automatic speech recognition task shows word error rates for the 2DLSTM model that are competitive to end-to-end attention-based model.

</details>

### [CAT: CRF-based ASR Toolkit](1911.08747.md)
**Keyu An, Hongyu Xiang, Zhijian Ou** · 2019-11-20

<details>
<summary>Abstract</summary>

In this paper, we present a new open source toolkit for automatic speech recognition (ASR), named CAT (CRF-based ASR Toolkit). A key feature of CAT is discriminative training in the framework of conditional random field (CRF), particularly with connectionist temporal classification (CTC) inspired state topology. CAT contains a full-fledged implementation of CTC-CRF and provides a complete workflow for CRF-based end-to-end speech recognition. Evaluation results on Chinese and English benchmarks such as Switchboard and Aishell show that CAT obtains the state-of-the-art results among existing end-to-end models with less parameters, and is competitive compared with the hybrid DNN-HMM models. Towards flexibility, we show that i-vector based speaker-adapted recognition and latency control mechanism can be explored easily and effectively in CAT. We hope CAT, especially the CRF-based framework and software, will be of broad interest to the community, and can be further explored and improved.

</details>

### [A Comparative Study on End-to-end Speech to Text Translation](1911.08870.md)
**Parnia Bahar, Tobias Bieschke, Hermann Ney** · 2019-11-20

<details>
<summary>Abstract</summary>

Recent advances in deep learning show that end-to-end speech to text translation model is a promising approach to direct the speech translation field. In this work, we provide an overview of different end-to-end architectures, as well as the usage of an auxiliary connectionist temporal classification (CTC) loss for better convergence. We also investigate on pre-training variants such as initializing different components of a model using pre-trained models, and their impact on the final performance, which gives boosts up to 4% in BLEU and 5% in TER. Our experiments are performed on 270h IWSLT TED-talks En->De, and 100h LibriSpeech Audiobooks En->Fr. We also show improvements over the current end-to-end state-of-the-art systems on both tasks.

</details>

### [End-to-end ASR: from Supervised to Semi-Supervised Learning with Modern Architectures](1911.08460.md)
**Gabriel Synnaeve, Qiantong Xu, Jacob Kahn, Tatiana Likhomanenko et al.** · 2019-11-19

<details>
<summary>Abstract</summary>

We study pseudo-labeling for the semi-supervised training of ResNet, Time-Depth Separable ConvNets, and Transformers for speech recognition, with either CTC or Seq2Seq loss functions. We perform experiments on the standard LibriSpeech dataset, and leverage additional unlabeled data from LibriVox through pseudo-labeling. We show that while Transformer-based acoustic models have superior performance with the supervised dataset alone, semi-supervision improves all models across architectures and loss functions and bridges much of the performance gaps between them. In doing so, we reach a new state-of-the-art for end-to-end acoustic models decoded with an external language model in the standard supervised learning setting, and a new absolute state-of-the-art with semi-supervised training. Finally, we study the effect of leveraging different amounts of unlabeled audio, propose several ways of evaluating the characteristics of unlabeled audio which improve acoustic modeling, and show that acoustic models trained with more audio rely less on external language models.

</details>

### [Deep Spiking Neural Networks for Large Vocabulary Automatic Speech Recognition](1911.08373.md)
**Jibin Wu, Emre Yilmaz, Malu Zhang, Haizhou Li et al.** · 2019-11-19

<details>
<summary>Abstract</summary>

Artificial neural networks (ANN) have become the mainstream acoustic modeling technique for large vocabulary automatic speech recognition (ASR). A conventional ANN features a multi-layer architecture that requires massive amounts of computation. The brain-inspired spiking neural networks (SNN) closely mimic the biological neural networks and can operate on low-power neuromorphic hardware with spike-based computation. Motivated by their unprecedented energyefficiency and rapid information processing capability, we explore the use of SNNs for speech recognition. In this work, we use SNNs for acoustic modeling and evaluate their performance on several large vocabulary recognition scenarios. The experimental results demonstrate competitive ASR accuracies to their ANN counterparts, while require significantly reduced computational cost and inference time. Integrating the algorithmic power of deep SNNs with energy-efficient neuromorphic hardware, therefore, offer an attractive solution for ASR applications running locally on mobile and embedded devices.

</details>

### [Sequential Multi-Frame Neural Beamforming for Speech Separation and Enhancement](1911.07953.md)
**Zhong-Qiu Wang, Hakan Erdogan, Scott Wisdom, Kevin Wilson et al.** · 2019-11-18

<details>
<summary>Abstract</summary>

This work introduces sequential neural beamforming, which alternates between neural network based spectral separation and beamforming based spatial separation. Our neural networks for separation use an advanced convolutional architecture trained with a novel stabilized signal-to-noise ratio loss function. For beamforming, we explore multiple ways of computing time-varying covariance matrices, including factorizing the spatial covariance into a time-varying amplitude component and a time-invariant spatial component, as well as using block-based techniques. In addition, we introduce a multi-frame beamforming method which improves the results significantly by adding contextual frames to the beamforming formulations. We extensively evaluate and analyze the effects of window size, block size, and multi-frame context size for these methods. Our best method utilizes a sequence of three neural separation and multi-frame time-invariant spatial beamforming stages, and demonstrates an average improvement of 2.75 dB in scale-invariant signal-to-noise ratio and 14.2% absolute reduction in a comparative speech recognition metric across four challenging reverberant speech enhancement and separation tasks. We also use our three-speaker separation model to separate real recordings in the LibriCSS evaluation set into non-overlapping tracks, and achieve a better word error rate as compared to a baseline mask based beamformer.

</details>

### [Improving Non-Intrusive Load Disaggregation through an Attention-Based Deep Neural Network](1912.00759.md)
**Veronica Piccialli, Antonio M. Sudoso** · 2019-11-15

<details>
<summary>Abstract</summary>

Energy disaggregation, known in the literature as Non-Intrusive Load Monitoring (NILM), is the task of inferring the power demand of the individual appliances given the aggregate power demand recorded by a single smart meter which monitors multiple appliances. In this paper, we propose a deep neural network that combines a regression subnetwork with a classification subnetwork for solving the NILM problem. Specifically, we improve the generalization capability of the overall architecture by including an encoder-decoder with a tailored attention mechanism in the regression subnetwork. The attention mechanism is inspired by the temporal attention that has been successfully applied in neural machine translation, text summarization, and speech recognition. The experiments conducted on two publicly available datasets--REDD and UK-DALE--show that our proposed deep neural network outperforms the state-of-the-art in all the considered experimental conditions. We also show that modeling attention translates into the network's ability to correctly detect the turning on or off an appliance and to locate signal sections with high power consumption, which are of extreme interest in the field of energy disaggregation.

</details>

### [Sample Drop Detection for Distant-speech Recognition with Asynchronous Devices Distributed in Space](1911.06713.md)
**Tina Raissi, Santiago Pascual, Maurizio Omologo** · 2019-11-15

<details>
<summary>Abstract</summary>

In many applications of multi-microphone multi-device processing, the synchronization among different input channels can be affected by the lack of a common clock and isolated drops of samples. In this work, we address the issue of sample drop detection in the context of a conversational speech scenario, recorded by a set of microphones distributed in space. The goal is to design a neural-based model that given a short window in the time domain, detects whether one or more devices have been subjected to a sample drop event. The candidate time windows are selected from a set of large time intervals, possibly including a sample drop, and by using a preprocessing step. The latter is based on the application of normalized cross-correlation between signals acquired by different devices. The architecture of the neural network relies on a CNN-LSTM encoder, followed by multi-head attention. The experiments are conducted using both artificial and real data. Our proposed approach obtained F1 score of 88% on an evaluation set extracted from the CHiME-5 corpus. A comparable performance was found in a larger set of experiments conducted on a set of multi-channel artificial scenes.

</details>

### [3-D Feature and Acoustic Modeling for Far-Field Speech Recognition](1911.05504.md)
**Anurenjan Purushothaman, Anirudh Sreeram, Sriram Ganapathy** · 2019-11-13

<details>
<summary>Abstract</summary>

Automatic speech recognition in multi-channel reverberant conditions is a challenging task. The conventional way of suppressing the reverberation artifacts involves a beamforming based enhancement of the multi-channel speech signal, which is used to extract spectrogram based features for a neural network acoustic model. In this paper, we propose to extract features directly from the multi-channel speech signal using a multi variate autoregressive (MAR) modeling approach, where the correlations among all the three dimensions of time, frequency and channel are exploited. The MAR features are fed to a convolutional neural network (CNN) architecture which performs the joint acoustic modeling on the three dimensions. The 3-D CNN architecture allows the combination of multi-channel features that optimize the speech recognition cost compared to the traditional beamforming models that focus on the enhancement task. Experiments are conducted on the CHiME-3 and REVERB Challenge dataset using multi-channel reverberant speech. In these experiments, the proposed 3-D feature and acoustic modeling approach provides significant improvements over an ASR system trained with beamformed audio (average relative improvements of 10 % and 9 % in word error rates for CHiME-3 and REVERB Challenge datasets respectively.

</details>

### [The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design](1911.05289.md)
**Jeffrey Dean** · 2019-11-13

<details>
<summary>Abstract</summary>

The past decade has seen a remarkable series of advances in machine learning, and in particular deep learning approaches based on artificial neural networks, to improve our abilities to build more accurate systems across a broad range of areas, including computer vision, speech recognition, language translation, and natural language understanding tasks. This paper is a companion paper to a keynote talk at the 2020 International Solid-State Circuits Conference (ISSCC) discussing some of the advances in machine learning, and their implications on the kinds of computational devices we need to build, especially in the post-Moore's Law-era. It also discusses some of the ways that machine learning may also be able to help with some aspects of the circuit design process. Finally, it provides a sketch of at least one interesting direction towards much larger-scale multi-task models that are sparsely activated and employ much more dynamic, example- and task-based routing than the machine learning models of today.

</details>

### [Long-span language modeling for speech recognition](1911.04571.md)
**Sarangarajan Parthasarathy, William Gale, Xie Chen, George Polovets et al.** · 2019-11-11

<details>
<summary>Abstract</summary>

We explore neural language modeling for speech recognition where the context spans multiple sentences. Rather than encode history beyond the current sentence using a cache of words or document-level features, we focus our study on the ability of LSTM and Transformer language models to implicitly learn to carry over context across sentence boundaries. We introduce a new architecture that incorporates an attention mechanism into LSTM to combine the benefits of recurrent and attention architectures. We conduct language modeling and speech recognition experiments on the publicly available LibriSpeech corpus. We show that conventional training on a paragraph-level corpus results in significant reductions in perplexity compared to training on a sentence-level corpus. We also describe speech recognition experiments using long-span language models in second-pass re-ranking, and provide insights into the ability of such models to take advantage of context beyond the current sentence.

</details>

### [Data Efficient Direct Speech-to-Text Translation with Modality Agnostic Meta-Learning](1911.04283.md)
**Sathish Indurthi, Houjeung Han, Nikhil Kumar Lakumarapu, Beomseok Lee et al.** · 2019-11-11

<details>
<summary>Abstract</summary>

End-to-end Speech Translation (ST) models have several advantages such as lower latency, smaller model size, and less error compounding over conventional pipelines that combine Automatic Speech Recognition (ASR) and text Machine Translation (MT) models. However, collecting large amounts of parallel data for ST task is more difficult compared to the ASR and MT tasks. Previous studies have proposed the use of transfer learning approaches to overcome the above difficulty. These approaches benefit from weakly supervised training data, such as ASR speech-to-transcript or MT text-to-text translation pairs. However, the parameters in these models are updated independently of each task, which may lead to sub-optimal solutions. In this work, we adopt a meta-learning algorithm to train a modality agnostic multi-task model that transfers knowledge from source tasks=ASR+MT to target task=ST where ST task severely lacks data. In the meta-learning phase, the parameters of the model are exposed to vast amounts of speech transcripts (e.g., English ASR) and text translations (e.g., English-German MT). During this phase, parameters are updated in such a way to understand speech, text representations, the relation between them, as well as act as a good initialization point for the target ST task. We evaluate the proposed meta-learning approach for ST tasks on English-German (En-De) and English-French (En-Fr) language pairs from the Multilingual Speech Translation Corpus (MuST-C). Our method outperforms the previous transfer learning approaches and sets new state-of-the-art results for En-De and En-Fr ST tasks by obtaining 9.18, and 11.76 BLEU point improvements, respectively.

</details>

### [Multimodal Intelligence: Representation Learning, Information Fusion, and Applications](1911.03977.md)
**Chao Zhang, Zichao Yang, Xiaodong He, Li Deng** · 2019-11-10

<details>
<summary>Abstract</summary>

Deep learning methods have revolutionized speech recognition, image recognition, and natural language processing since 2010. Each of these tasks involves a single modality in their input signals. However, many applications in the artificial intelligence field involve multiple modalities. Therefore, it is of broad interest to study the more difficult and complex problem of modeling and learning across multiple modalities. In this paper, we provide a technical review of available models and learning methods for multimodal intelligence. The main focus of this review is the combination of vision and natural language modalities, which has become an important topic in both the computer vision and natural language processing research communities. This review provides a comprehensive analysis of recent works on multimodal deep learning from three perspectives: learning multimodal representations, fusing multimodal signals at various levels, and multimodal applications. Regarding multimodal representation learning, we review the key concepts of embedding, which unify multimodal signals into a single vector space and thereby enable cross-modality signal processing. We also review the properties of many types of embeddings that are constructed and learned for general downstream tasks. Regarding multimodal fusion, this review focuses on special architectures for the integration of representations of unimodal signals for a particular task. Regarding applications, selected areas of a broad interest in the current literature are covered, including image-to-text caption generation, text-to-image generation, and visual question answering. We believe that this review will facilitate future studies in the emerging field of multimodal intelligence for related communities.

</details>

### [Effectiveness of self-supervised pre-training for speech recognition](1911.03912.md)
**Alexei Baevski, Michael Auli, Abdelrahman Mohamed** · 2019-11-10

<details>
<summary>Abstract</summary>

We compare self-supervised representation learning algorithms which either explicitly quantize the audio data or learn representations without quantization. We find the former to be more accurate since it builds a good vocabulary of the data through vq-wav2vec [1] to enable learning of effective representations in subsequent BERT training. Different to previous work, we directly fine-tune the pre-trained BERT models on transcribed speech using a Connectionist Temporal Classification (CTC) loss instead of feeding the representations into a task-specific model. We also propose a BERT-style model learning directly from the continuous audio data and compare pre-training on raw audio to spectral features. Fine-tuning a BERT model on 10 hour of labeled Librispeech data with a vq-wav2vec vocabulary is almost as good as the best known reported system trained on 100 hours of labeled data on testclean, while achieving a 25% WER reduction on test-other. When using only 10 minutes of labeled data, WER is 25.2 on test-other and 16.3 on test-clean. This demonstrates that self-supervision can enable speech recognition systems trained on a near-zero amount of transcribed data.

</details>

### [Listen and Fill in the Missing Letters: Non-Autoregressive Transformer for Speech Recognition](1911.04908.md)
**Nanxin Chen, Shinji Watanabe, Jesús Villalba, Najim Dehak** · 2019-11-10

<details>
<summary>Abstract</summary>

Recently very deep transformers have outperformed conventional bi-directional long short-term memory networks by a large margin in speech recognition. However, to put it into production usage, inference computation cost is still a serious concern in real scenarios. In this paper, we study two different non-autoregressive transformer structure for automatic speech recognition (ASR): A-CMLM and A-FMLM. During training, for both frameworks, input tokens fed to the decoder are randomly replaced by special mask tokens. The network is required to predict the tokens corresponding to those mask tokens by taking both unmasked context and input speech into consideration. During inference, we start from all mask tokens and the network iteratively predicts missing tokens based on partial results. We show that this framework can support different decoding strategies, including traditional left-to-right. A new decoding strategy is proposed as an example, which starts from the easiest predictions to the most difficult ones. Results on Mandarin (Aishell) and Japanese (CSJ) ASR benchmarks show the possibility to train such a non-autoregressive network for ASR. Especially in Aishell, the proposed method outperformed the Kaldi ASR system and it matches the performance of the state-of-the-art autoregressive transformer with 7x speedup. Pretrained models and code will be made available after publication.

</details>

### [Speaker Adaptation for Attention-Based End-to-End Speech Recognition](1911.03762.md)
**Zhong Meng, Yashesh Gaur, Jinyu Li, Yifan Gong** · 2019-11-09

<details>
<summary>Abstract</summary>

We propose three regularization-based speaker adaptation approaches to adapt the attention-based encoder-decoder (AED) model with very limited adaptation data from target speakers for end-to-end automatic speech recognition. The first method is Kullback-Leibler divergence (KLD) regularization, in which the output distribution of a speaker-dependent (SD) AED is forced to be close to that of the speaker-independent (SI) model by adding a KLD regularization to the adaptation criterion. To compensate for the asymmetric deficiency in KLD regularization, an adversarial speaker adaptation (ASA) method is proposed to regularize the deep-feature distribution of the SD AED through the adversarial learning of an auxiliary discriminator and the SD AED. The third approach is the multi-task learning, in which an SD AED is trained to jointly perform the primary task of predicting a large number of output units and an auxiliary task of predicting a small number of output units to alleviate the target sparsity issue. Evaluated on a Microsoft short message dictation task, all three methods are highly effective in adapting the AED model, achieving up to 12.2% and 3.0% word error rate improvement over an SI AED trained from 3400 hours data for supervised and unsupervised adaptation, respectively.

</details>

### [A Simplified Fully Quantized Transformer for End-to-end Speech Recognition](1911.03604.md)
**Alex Bie, Bharat Venkitesh, Joao Monteiro, Md. Akmal Haidar et al.** · 2019-11-09

<details>
<summary>Abstract</summary>

While significant improvements have been made in recent years in terms of end-to-end automatic speech recognition (ASR) performance, such improvements were obtained through the use of very large neural networks, unfit for embedded use on edge devices. That being said, in this paper, we work on simplifying and compressing Transformer-based encoder-decoder architectures for the end-to-end ASR task. We empirically introduce a more compact Speech-Transformer by investigating the impact of discarding particular modules on the performance of the model. Moreover, we evaluate reducing the numerical precision of our network's weights and activations while maintaining the performance of the full-precision model. Our experiments show that we can reduce the number of parameters of the full-precision model and then further compress the model 4x by fully quantizing to 8-bit fixed point precision.

</details>

### [Recurrent Neural Network Transducer for Audio-Visual Speech Recognition](1911.04890.md)
**Takaki Makino, Hank Liao, Yannis Assael, Brendan Shillingford et al.** · 2019-11-08

<details>
<summary>Abstract</summary>

This work presents a large-scale audio-visual speech recognition system based on a recurrent neural network transducer (RNN-T) architecture. To support the development of such a system, we built a large audio-visual (A/V) dataset of segmented utterances extracted from YouTube public videos, leading to 31k hours of audio-visual training content. The performance of an audio-only, visual-only, and audio-visual system are compared on two large-vocabulary test sets: a set of utterance segments from public YouTube videos called YTDEV18 and the publicly available LRS3-TED set. To highlight the contribution of the visual modality, we also evaluated the performance of our system on the YTDEV18 set artificially corrupted with background noise and overlapping speech. To the best of our knowledge, our system significantly improves the state-of-the-art on the LRS3-TED set.

</details>

### [Boosting LSTM Performance Through Dynamic Precision Selection](1911.04244.md)
**Franyell Silfa, Jose-Maria Arnau, Antonio Gonzàlez** · 2019-11-07

<details>
<summary>Abstract</summary>

The use of low numerical precision is a fundamental optimization included in modern accelerators for Deep Neural Networks (DNNs). The number of bits of the numerical representation is set to the minimum precision that is able to retain accuracy based on an offline profiling, and it is kept constant for DNN inference. In this work, we explore the use of dynamic precision selection during DNN inference. We focus on Long Short Term Memory (LSTM) networks, which represent the state-of-the-art networks for applications such as machine translation and speech recognition. Unlike conventional DNNs, LSTM networks remember information from previous evaluations by storing data in the LSTM cell state. Our key observation is that the cell state determines the amount of precision required: time steps where the cell state changes significantly require higher precision, whereas time steps where the cell state is stable can be computed with lower precision without any loss in accuracy. Based on this observation, we implement a novel hardware scheme that tracks the evolution of the elements in the LSTM cell state and dynamically selects the appropriate precision in each time step. For a set of popular LSTM networks, our scheme selects the lowest precision for more than 66% of the time, outperforming systems that fix the precision statically. We evaluate our proposal on top of a modern accelerator highly optimized for LSTM computation, and show that it provides 1.56x speedup and 23% energy savings on average without any loss in accuracy. The extra hardware to determine the appropriate precision represents a small area overhead of 8.8%.

</details>

### [A comparison of end-to-end models for long-form speech recognition](1911.02242.md)
**Chung-Cheng Chiu, Wei Han, Yu Zhang, Ruoming Pang et al.** · 2019-11-06

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) models, including both attention-based models and the recurrent neural network transducer (RNN-T), have shown superior performance compared to conventional systems. However, previous studies have focused primarily on short utterances that typically last for just a few seconds or, at most, a few tens of seconds. Whether such architectures are practical on long utterances that last from minutes to hours remains an open question. In this paper, we both investigate and improve the performance of end-to-end models on long-form transcription. We first present an empirical comparison of different end-to-end models on a real world long-form task and demonstrate that the RNN-T model is much more robust than attention-based systems in this regime. We next explore two improvements to attention-based systems that significantly improve its performance: restricting the attention to be monotonic, and applying a novel decoding algorithm that breaks long utterances into shorter overlapping segments. Combining these two improvements, we show that attention-based end-to-end models can be very competitive to RNN-T on long-form speech recognition.

</details>

### [Spatial Attention for Far-field Speech Recognition with Deep Beamforming Neural Networks](1911.02115.md)
**Weipeng He, Lu Lu, Biqiao Zhang, Jay Mahadeokar et al.** · 2019-11-05

<details>
<summary>Abstract</summary>

In this paper, we introduce spatial attention for refining the information in multi-direction neural beamformer for far-field automatic speech recognition. Previous approaches of neural beamformers with multiple look directions, such as the factored complex linear projection, have shown promising results. However, the features extracted by such methods contain redundant information, as only the direction of the target speech is relevant. We propose using a spatial attention subnet to weigh the features from different directions, so that the subsequent acoustic model could focus on the most relevant features for the speech recognition. Our experimental results show that spatial attention achieves up to 9% relative word error rate improvement over methods without the attention.

</details>

### [RNN-T For Latency Controlled ASR With Improved Beam Search](1911.01629.md)
**Mahaveer Jain, Kjell Schubert, Jay Mahadeokar, Ching-Feng Yeh et al.** · 2019-11-05

<details>
<summary>Abstract</summary>

Neural transducer-based systems such as RNN Transducers (RNN-T) for automatic speech recognition (ASR) blend the individual components of a traditional hybrid ASR systems (acoustic model, language model, punctuation model, inverse text normalization) into one single model. This greatly simplifies training and inference and hence makes RNN-T a desirable choice for ASR systems. In this work, we investigate use of RNN-T in applications that require a tune-able latency budget during inference time. We also improved the decoding speed of the originally proposed RNN-T beam search algorithm. We evaluated our proposed system on English videos ASR dataset and show that neural RNN-T models can achieve comparable WER and better computational efficiency compared to a well tuned hybrid ASR baseline.

</details>

### [SHARP: An Adaptable, Energy-Efficient Accelerator for Recurrent Neural Network](1911.01258.md)
**Reza Yazdani, Olatunji Ruwase, Minjia Zhang, Yuxiong He et al.** · 2019-11-04

<details>
<summary>Abstract</summary>

The effectiveness of Recurrent Neural Networks (RNNs) for tasks such as Automatic Speech Recognition has fostered interest in RNN inference acceleration. Due to the recurrent nature and data dependencies of RNN computations, prior work has designed customized architectures specifically tailored to the computation pattern of RNN, getting high computation efficiency for certain chosen model sizes. However, given that the dimensionality of RNNs varies a lot for different tasks, it is crucial to generalize this efficiency to diverse configurations. In this work, we identify adaptiveness as a key feature that is missing from today's RNN accelerators. In particular, we first show the problem of low resource-utilization and low adaptiveness for the state-of-the-art RNN implementations on GPU, FPGA and ASIC architectures. To solve these issues, we propose an intelligent tiled-based dispatching mechanism for increasing the adaptiveness of RNN computation, in order to efficiently handle the data dependencies. To do so, we propose Sharp as a hardware accelerator, which pipelines RNN computation using an effective scheduling scheme to hide most of the dependent serialization. Furthermore, Sharp employs dynamic reconfigurable architecture to adapt to the model's characteristics. Sharp achieves 2x, 2.8x, and 82x speedups on average, considering different RNN models and resource budgets, compared to the state-of-the-art ASIC, FPGA, and GPU implementations, respectively. Furthermore, we provide significant energy-reduction with respect to the previous solutions, due to the low power dissipation of Sharp (321 GFLOPS/Watt).

</details>

### [Supervised level-wise pretraining for recurrent neural network initialization in multi-class classification](1911.01071.md)
**Dino Ienco, Roberto Interdonato, Raffaele Gaetano** · 2019-11-04

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) can be seriously impacted by the initial parameters assignment, which may result in poor generalization performances on new unseen data. With the objective to tackle this crucial issue, in the context of RNN based classification, we propose a new supervised layer-wise pretraining strategy to initialize network parameters. The proposed approach leverages a data-aware strategy that sets up a taxonomy of classification problems automatically derived by the model behavior. To the best of our knowledge, despite the great interest in RNN-based classification, this is the first data-aware strategy dealing with the initialization of such models. The proposed strategy has been tested on four benchmarks coming from two different domains, i.e., Speech Recognition and Remote Sensing. Results underline the significance of our approach and point out that data-aware strategies positively support the initialization of Recurrent Neural Network based classification models.

</details>

### [Onssen: an open-source speech separation and enhancement library](1911.00982.md)
**Zhaoheng Ni, Michael I Mandel** · 2019-11-03

<details>
<summary>Abstract</summary>

Speech separation is an essential task for multi-talker speech recognition. Recently many deep learning approaches are proposed and have been constantly refreshing the state-of-the-art performances. The lack of algorithm implementations limits researchers to use the same dataset for comparison. Building a generic platform can benefit researchers by easily implementing novel separation algorithms and comparing them with the existing ones on customized datasets. We introduce "onssen": an open-source speech separation and enhancement library. onssen is a library mainly for deep learning separation and enhancement algorithms. It uses LibRosa and NumPy libraries for the feature extraction and PyTorch as the back-end for model training. onssen supports most of the Time-Frequency mask-based separation algorithms (e.g. deep clustering, chimera net, chimera++, and so on) and also supports customized datasets. In this paper, we describe the functionality of modules in onssen and show the algorithms implemented by onssen achieve the same performances as reported in the original papers.

</details>

### [Predicting word error rate for reverberant speech](1911.00566.md)
**Hannes Gamper, Dimitra Emmanouilidou, Sebastian Braun, Ivan J. Tashev** · 2019-11-01

<details>
<summary>Abstract</summary>

Reverberation negatively impacts the performance of automatic speech recognition (ASR). Prior work on quantifying the effect of reverberation has shown that clarity (C50), a parameter that can be estimated from the acoustic impulse response, is correlated with ASR performance. In this paper we propose predicting ASR performance in terms of the word error rate (WER) directly from acoustic parameters via a polynomial, sigmoidal, or neural network fit, as well as blindly from reverberant speech samples using a convolutional neural network (CNN). We carry out experiments on two state-of-the-art ASR models and a large set of acoustic impulse responses (AIRs). The results confirm C50 and C80 to be highly correlated with WER, allowing WER to be predicted with the proposed fitting approaches. The proposed non-intrusive CNN model outperforms C50-based WER prediction, indicating that WER can be estimated blindly, i.e., directly from the reverberant speech samples without knowledge of the acoustic parameters.

</details>

### [Improving Generalization of Transformer for Speech Recognition with Parallel Schedule Sampling and Relative Positional Embedding](1911.00203.md)
**Pan Zhou, Ruchao Fan, Wei Chen, Jia Jia** · 2019-11-01

<details>
<summary>Abstract</summary>

Transformer has shown promising results in many sequence to sequence transformation tasks recently. It utilizes a number of feed-forward self-attention layers to replace the recurrent neural networks (RNN) in attention-based encoder decoder (AED) architecture. Self-attention layer learns temporal dependence by incorporating sinusoidal positional embedding of tokens in a sequence for parallel computing. Quicker iteration speed in training than sequential operation of RNN can be obtained. Deeper layers of the transformer also make it perform better than RNN-based AED. However, this parallelization ability is lost when applying scheduled sampling training. Self-attention with sinusoidal positional embedding may cause performance degradations for longer sequences that have similar acoustic or semantic information at different positions as well. To address these problems, we propose to use parallel scheduled sampling (PSS) and relative positional embedding (RPE) to help the transformer generalize to unseen data. Our proposed methods achieve a 7% relative improvement for short utterances and a 70% relative gain for long utterances on a 10,000-hour Mandarin ASR task.

</details>

### [Novel Defense Method against Audio Adversarial Example for Speech-to-Text Transcription Neural Networks](s2:fe84cd7a846ca26e9e588327ef7031650d10b093.md)
**K. Tamura, Akitada Omagari, Shuichi Hashida** · 2019-11-01

<details>
<summary>Abstract</summary>

With the developments in deep learning, the security of neural networks against vulnerabilities has become one of the most urgent research topics in deep learning. There are many types of security countermeasures. Adversarial examples and their defense methods, in particular, have been well-studied in recent years. An adversarial example is designed to make neural networks misclassify or produce inaccurate output. Audio adversarial examples are a type of adversarial example where the main target of attack is a speech-to-text transcription neural network. In this study, we propose a new defense method against audio adversarial examples for the speech-to-text transcription neural networks. It is difficult to determine whether an input waveform data representing the sound of voice is an audio adversarial example. Therefore, the main framework of the proposed defense method is based on a sandbox approach. To evaluate the proposed defense method, we used actual audio adversarial examples that were created on Deep Speech, which is a speech-to-text transcription neural network. We confirmed that our defense method can identify audio adversarial examples to protect speech-to-text systems.

</details>

### [A Multilingual ASR of Sepedi-English Code-Switched Speech for Automatic Language Identification](s2:fa55fdc0e2c18e3d25b359de5f1724c595b62495.md)
**K. Mabokela** · 2019-11-01

<details>
<summary>Abstract</summary>

This paper presents an integration of multilingual speech recognition into language identification (LID) for code-switched speech using phonotatic features as language information. A multilingual speech recognition system converts the spoken utterances into occurrences of phone sequences. The hidden Markov models (HMMs) are employed to build a multilingual acoustic models that can handle multiple languages within an utterance. We propose two phoneme clustering methods to determine the phoneme similarities among the target languages. A supervised machine learning technique is employed to learn the language transition of the phonotactic information given the phoneme sequences. The classification decision is made by support vector machines (SVM) technique which classifies language identity given the likelihood scores based on the phoneme occurrence segments. We experiments were performed using a mixed language speech corpus for Sepedi and English. We evaluate the ASR-LID system measuring the performance of the phone error rate (PER) and the LID classification accuracy portions separately. We obtained a lower PER on a system that employed data-driven phoneme clustering method which was modelled with 32-Gaussian mixtures per state. The proposed multilingual ASR-LID framework has achieved an acceptable recognition and classification accuracy on code-switched and monolingual speech respectively.

</details>

### [A neural document language modeling framework for spoken document retrieval](1910.14286.md)
**Li-Phen Yen, Zhen-Yu Wu, Kuan-Yu Chen** · 2019-10-31

<details>
<summary>Abstract</summary>

Recent developments in deep learning have led to a significant innovation in various classic and practical subjects, including speech recognition, computer vision, question answering, information retrieval and so on. In the context of natural language processing (NLP), language representations have shown giant successes in many downstream tasks, so the school of studies have become a major stream of research recently. Because the immenseness of multimedia data along with speech have spread around the world in our daily life, spoken document retrieval (SDR) has become an important research subject in the past decades. Targeting on enhancing the SDR performance, the paper concentrates on proposing a neural retrieval framework, which assembles the merits of using language modeling (LM) mechanism in SDR and leveraging the abstractive information learned by the language representation models. Consequently, to our knowledge, this is a pioneer study on supervised training of a neural LM-based SDR framework, especially combined with the pretrained language representation methods.

</details>

### [Lightweight and Efficient End-to-End Speech Recognition Using Low-Rank Transformer](1910.13923.md)
**Genta Indra Winata, Samuel Cahyawijaya, Zhaojiang Lin, Zihan Liu et al.** · 2019-10-30

<details>
<summary>Abstract</summary>

Highly performing deep neural networks come at the cost of computational complexity that limits their practicality for deployment on portable devices. We propose the low-rank transformer (LRT), a memory-efficient and fast neural architecture that significantly reduces the parameters and boosts the speed of training and inference for end-to-end speech recognition. Our approach reduces the number of parameters of the network by more than 50% and speeds up the inference time by around 1.35x compared to the baseline transformer model. The experiments show that our LRT model generalizes better and yields lower error rates on both validation and test sets compared to an uncompressed transformer model. The LRT model outperforms those from existing works on several datasets in an end-to-end setting without using an external language model or acoustic data.

</details>

### [Overlapped speech recognition from a jointly learned multi-channel neural speech extraction and representation](1910.13825.md)
**Bo Wu, Meng Yu, Lianwu Chen, Chao Weng et al.** · 2019-10-30

<details>
<summary>Abstract</summary>

We propose an end-to-end joint optimization framework of a multi-channel neural speech extraction and deep acoustic model without mel-filterbank (FBANK) extraction for overlapped speech recognition. First, based on a multi-channel convolutional TasNet with STFT kernel, we unify the multi-channel target speech enhancement front-end network and a convolutional, long short-term memory and fully connected deep neural network (CLDNN) based acoustic model (AM) with the FBANK extraction layer to build a hybrid neural network, which is thus jointly updated only by the recognition loss. The proposed framework achieves 28% word error rate reduction (WERR) over a separately optimized system on AISHELL-1 and shows consistent robustness to signal to interference ratio (SIR) and angle difference between overlapping speakers. Next, a further exploration shows that the speech recognition is improved with a simplified structure by replacing the FBANK extraction layer in the joint model with a learnable feature projection. Finally, we also perform the objective measurement of speech quality on the reconstructed waveform from the enhancement network in the joint model.

</details>

### [Learning Deterministic Weighted Automata with Queries and Counterexamples](1910.13895.md)
**Gail Weiss, Yoav Goldberg, Eran Yahav** · 2019-10-30

<details>
<summary>Abstract</summary>

We present an algorithm for extraction of a probabilistic deterministic finite automaton (PDFA) from a given black-box language model, such as a recurrent neural network (RNN). The algorithm is a variant of the exact-learning algorithm L*, adapted to a probabilistic setting with noise. The key insight is the use of conditional probabilities for observations, and the introduction of a local tolerance when comparing them. When applied to RNNs, our algorithm often achieves better word error rate (WER) and normalised distributed cumulative gain (NDCG) than that achieved by spectral extraction of weighted finite automata (WFA) from the same networks. PDFAs are substantially more expressive than n-grams, and are guaranteed to be stochastic and deterministic - unlike spectrally extracted WFAs.

</details>

### [Improving sequence-to-sequence speech recognition training with on-the-fly data augmentation](1910.13296.md)
**Thai-Son Nguyen, Sebastian Stueker, Jan Niehues, Alex Waibel** · 2019-10-29

<details>
<summary>Abstract</summary>

Sequence-to-Sequence (S2S) models recently started to show state-of-the-art performance for automatic speech recognition (ASR). With these large and deep models overfitting remains the largest problem, outweighing performance improvements that can be obtained from better architectures. One solution to the overfitting problem is increasing the amount of available training data and the variety exhibited by the training data with the help of data augmentation. In this paper we examine the influence of three data augmentation methods on the performance of two S2S model architectures. One of the data augmentation method comes from literature, while two other methods are our own development - a time perturbation in the frequency domain and sub-sequence sampling. Our experiments on Switchboard and Fisher data show state-of-the-art performance for S2S models that are trained solely on the speech training data and do not use additional text data.

</details>

### [Transformer-based Cascaded Multimodal Speech Translation](1910.13215.md)
**Zixiu Wu, Ozan Caglayan, Julia Ive, Josiah Wang et al.** · 2019-10-29

<details>
<summary>Abstract</summary>

This paper describes the cascaded multimodal speech translation systems developed by Imperial College London for the IWSLT 2019 evaluation campaign. The architecture consists of an automatic speech recognition (ASR) system followed by a Transformer-based multimodal machine translation (MMT) system. While the ASR component is identical across the experiments, the MMT model varies in terms of the way of integrating the visual context (simple conditioning vs. attention), the type of visual features exploited (pooled, convolutional, action categories) and the underlying architecture. For the latter, we explore both the canonical transformer and its deliberation version with additive and cascade variants which differ in how they integrate the textual attention. Upon conducting extensive experiments, we found that (i) the explored visual integration schemes often harm the translation performance for the transformer and additive deliberation, but considerably improve the cascade deliberation; (ii) the transformer and cascade deliberation integrate the visual modality better than the additive deliberation, as shown by the incongruence analysis.

</details>

### [LeanConvNets: Low-cost Yet Effective Convolutional Neural Networks](1910.13157.md)
**Jonathan Ephrath, Moshe Eliasof, Lars Ruthotto, Eldad Haber et al.** · 2019-10-29

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNNs) have become indispensable for solving machine learning tasks in speech recognition, computer vision, and other areas that involve high-dimensional data. A CNN filters the input feature using a network containing spatial convolution operators with compactly supported stencils. In practice, the input data and the hidden features consist of a large number of channels, which in most CNNs are fully coupled by the convolution operators. This coupling leads to immense computational cost in the training and prediction phase. In this paper, we introduce LeanConvNets that are derived by sparsifying fully-coupled operators in existing CNNs. Our goal is to improve the efficiency of CNNs by reducing the number of weights, floating point operations and latency times, with minimal loss of accuracy. Our lean convolution operators involve tuning parameters that controls the trade-off between the network's accuracy and computational costs. These convolutions can be used in a wide range of existing networks, and we exemplify their use in residual networks (ResNets). Using a range of benchmark problems from image classification and semantic segmentation, we demonstrate that the resulting LeanConvNet's accuracy is close to state-of-the-art networks while being computationally less expensive. In our tests, the lean versions of ResNet in most cases outperform comparable reduced architectures such as MobileNets and ShuffleNets.

</details>

### [Transformer-Transducer: End-to-End Speech Recognition with Self-Attention](1910.12977.md)
**Ching-Feng Yeh, Jay Mahadeokar, Kaustubh Kalgaonkar, Yongqiang Wang et al.** · 2019-10-28

<details>
<summary>Abstract</summary>

We explore options to use Transformer networks in neural transducer for end-to-end speech recognition. Transformer networks use self-attention for sequence modeling and comes with advantages in parallel computation and capturing contexts. We propose 1) using VGGNet with causal convolution to incorporate positional information and reduce frame rate for efficient inference 2) using truncated self-attention to enable streaming for Transformer and reduce computational complexity. All experiments are conducted on the public LibriSpeech corpus. The proposed Transformer-Transducer outperforms neural transducer with LSTM/BLSTM networks and achieved word error rates of 6.37 % on the test-clean set and 15.30 % on the test-other set, while remaining streamable, compact with 45.7M parameters for the entire system, and computationally efficient with complexity of O(T), where T is input sequence length.

</details>

### [Sequence-to-sequence Automatic Speech Recognition with Word Embedding Regularization and Fused Decoding](1910.12740.md)
**Alexander H. Liu, Tzu-Wei Sung, Shun-Po Chuang, Hung-yi Lee et al.** · 2019-10-28

<details>
<summary>Abstract</summary>

In this paper, we investigate the benefit that off-the-shelf word embedding can bring to the sequence-to-sequence (seq-to-seq) automatic speech recognition (ASR). We first introduced the word embedding regularization by maximizing the cosine similarity between a transformed decoder feature and the target word embedding. Based on the regularized decoder, we further proposed the fused decoding mechanism. This allows the decoder to consider the semantic consistency during decoding by absorbing the information carried by the transformed decoder feature, which is learned to be close to the target word embedding. Initial results on LibriSpeech demonstrated that pre-trained word embedding can significantly lower ASR recognition error with a negligible cost, and the choice of word embedding algorithms among Skip-gram, CBOW and BERT is important.

</details>

### [DFSMN-SAN with Persistent Memory Model for Automatic Speech Recognition](1910.13282.md)
**Zhao You, Dan Su, Jie Chen, Chao Weng et al.** · 2019-10-28

<details>
<summary>Abstract</summary>

Self-attention networks (SAN) have been introduced into automatic speech recognition (ASR) and achieved state-of-the-art performance owing to its superior ability in capturing long term dependency. One of the key ingredients is the self-attention mechanism which can be effectively performed on the whole utterance level. In this paper, we try to investigate whether even more information beyond the whole utterance level can be exploited and beneficial. We propose to apply self-attention layer with augmented memory to ASR. Specifically, we first propose a variant model architecture which combines deep feed-forward sequential memory network (DFSMN) with self-attention layers to form a better baseline model compared with a purely self-attention network. Then, we propose and compare two kinds of additional memory structures added into self-attention layers. Experiments on large-scale LVCSR tasks show that on four individual test sets, the DFSMN-SAN architecture outperforms vanilla SAN encoder by 5% relatively in character error rate (CER). More importantly, the additional memory structure provides further 5% to 11% relative improvement in CER.

</details>

### [Unsupervised pre-training for sequence to sequence speech recognition](1910.12418.md)
**Zhiyun Fan, Shiyu Zhou, Bo Xu** · 2019-10-28

<details>
<summary>Abstract</summary>

This paper proposes a novel approach to pre-train encoder-decoder sequence-to-sequence (seq2seq) model with unpaired speech and transcripts respectively. Our pre-training method is divided into two stages, named acoustic pre-trianing and linguistic pre-training. In the acoustic pre-training stage, we use a large amount of speech to pre-train the encoder by predicting masked speech feature chunks with its context. In the linguistic pre-training stage, we generate synthesized speech from a large number of transcripts using a single-speaker text to speech (TTS) system, and use the synthesized paired data to pre-train decoder. This two-stage pre-training method integrates rich acoustic and linguistic knowledge into seq2seq model, which will benefit downstream automatic speech recognition (ASR) tasks. The unsupervised pre-training is finished on AISHELL-2 dataset and we apply the pre-trained model to multiple paired data ratios of AISHELL-1 and HKUST. We obtain relative character error rate reduction (CERR) from 38.24% to 7.88% on AISHELL-1 and from 12.00% to 1.20% on HKUST. Besides, we apply our pretrained model to a cross-lingual case with CALLHOME dataset. For all six languages in CALLHOME dataset, our pre-training method makes model outperform baseline consistently.

</details>

### [Training ASR models by Generation of Contextual Information](1910.12367.md)
**Kritika Singh, Dmytro Okhonko, Jun Liu, Yongqiang Wang et al.** · 2019-10-27

<details>
<summary>Abstract</summary>

Supervised ASR models have reached unprecedented levels of accuracy, thanks in part to ever-increasing amounts of labelled training data. However, in many applications and locales, only moderate amounts of data are available, which has led to a surge in semi- and weakly-supervised learning research. In this paper, we conduct a large-scale study evaluating the effectiveness of weakly-supervised learning for speech recognition by using loosely related contextual information as a surrogate for ground-truth labels. For weakly supervised training, we use 50k hours of public English social media videos along with their respective titles and post text to train an encoder-decoder transformer model. Our best encoder-decoder models achieve an average of 20.8% WER reduction over a 1000 hours supervised baseline, and an average of 13.4% WER reduction when using only the weakly supervised encoder for CTC fine-tuning. Our results show that our setup for weak supervision improved both the encoder acoustic representations as well as the decoder language generation abilities.

</details>

### [Meta Learning for End-to-End Low-Resource Speech Recognition](1910.12094.md)
**Jui-Yang Hsu, Yuan-Jui Chen, Hung-yi Lee** · 2019-10-26

<details>
<summary>Abstract</summary>

In this paper, we proposed to apply meta learning approach for low-resource automatic speech recognition (ASR). We formulated ASR for different languages as different tasks, and meta-learned the initialization parameters from many pretraining languages to achieve fast adaptation on unseen target language, via recently proposed model-agnostic meta learning algorithm (MAML). We evaluated the proposed approach using six languages as pretraining tasks and four languages as target tasks. Preliminary results showed that the proposed method, MetaASR, significantly outperforms the state-of-the-art multitask pretraining approach on all target languages with different combinations of pretraining languages. In addition, since MAML's model-agnostic property, this paper also opens new research direction of applying meta learning to more speech-related applications.

</details>

### [Confidence Estimation for Black Box Automatic Speech Recognition Systems Using Lattice Recurrent Neural Networks](1910.11933.md)
**Alexandros Kastanos, Anton Ragni, Mark Gales** · 2019-10-25

<details>
<summary>Abstract</summary>

Recently, there has been growth in providers of speech transcription services enabling others to leverage technology they would not normally be able to use. As a result, speech-enabled solutions have become commonplace. Their success critically relies on the quality, accuracy, and reliability of the underlying speech transcription systems. Those black box systems, however, offer limited means for quality control as only word sequences are typically available. This paper examines this limited resource scenario for confidence estimation, a measure commonly used to assess transcription reliability. In particular, it explores what other sources of word and sub-word level information available in the transcription process could be used to improve confidence scores. To encode all such information this paper extends lattice recurrent neural networks to handle sub-words. Experimental results using the IARPA OpenKWS 2016 evaluation system show that the use of additional information yields significant gains in confidence estimation accuracy. The implementation for this model can be found online.

</details>

### [Exploring Lexicon-Free Modeling Units for End-to-End Korean and Korean-English Code-Switching Speech Recognition](1910.11590.md)
**Jisung Wang, Jihwan Kim, Sangki Kim, Yeha Lee** · 2019-10-25

<details>
<summary>Abstract</summary>

As the character-based end-to-end automatic speech recognition (ASR) models evolve, the choice of acoustic modeling units becomes important. Since Korean is a fairly phonetic language and has a unique writing system with its own Korean alphabet, it's worth investigating modeling units for an end-to-end Korean ASR task. In this work, we introduce lexicon-free modeling units in Korean, and explore them using a hybrid CTC/Attention-based encoder-decoder model. Five lexicon-free units are investigated: Syllable-based Korean character (with English character for a code-switching task), Korean Jamo character (with English character), sub-word on syllable-based character (with sub-word in English), sub-word on Jamo character (with sub-words in English), and finally byte unit, which is a universal one across language. Experiments on Zeroth-Korean (51.6 hrs) and Medical Record (2530 hrs) are done for Korean and Korean-English code-switching ASR tasks, respectively. Sequence-to-sequence learning with sub-words based on Korean syllables (and sub-words in English) performs the best for both tasks without lexicon and an extra language model integration.

</details>

### [Towards Online End-to-end Transformer Automatic Speech Recognition](1910.11871.md)
**Emiru Tsunoo, Yosuke Kashiwagi, Toshiyuki Kumakura, Shinji Watanabe** · 2019-10-25

<details>
<summary>Abstract</summary>

The Transformer self-attention network has recently shown promising performance as an alternative to recurrent neural networks in end-to-end (E2E) automatic speech recognition (ASR) systems. However, Transformer has a drawback in that the entire input sequence is required to compute self-attention. We have proposed a block processing method for the Transformer encoder by introducing a context-aware inheritance mechanism. An additional context embedding vector handed over from the previously processed block helps to encode not only local acoustic information but also global linguistic, channel, and speaker attributes. In this paper, we extend it towards an entire online E2E ASR system by introducing an online decoding process inspired by monotonic chunkwise attention (MoChA) into the Transformer decoder. Our novel MoChA training and inference algorithms exploit the unique properties of Transformer, whose attentions are not always monotonic or peaky, and have multiple heads and residual connections of the decoder layers. Evaluations of the Wall Street Journal (WSJ) and AISHELL-1 show that our proposed online Transformer decoder outperforms conventional chunkwise approaches.

</details>

### [L2RS: A Learning-to-Rescore Mechanism for Automatic Speech Recognition](1910.11496.md)
**Yuanfeng Song, Di Jiang, Xuefang Zhao, Qian Xu et al.** · 2019-10-25

<details>
<summary>Abstract</summary>

Modern Automatic Speech Recognition (ASR) systems primarily rely on scores from an Acoustic Model (AM) and a Language Model (LM) to rescore the N-best lists. With the abundance of recent natural language processing advances, the information utilized by current ASR for evaluating the linguistic and semantic legitimacy of the N-best hypotheses is rather limited. In this paper, we propose a novel Learning-to-Rescore (L2RS) mechanism, which is specialized for utilizing a wide range of textual information from the state-of-the-art NLP models and automatically deciding their weights to rescore the N-best lists for ASR systems. Specifically, we incorporate features including BERT sentence embedding, topic vector, and perplexity scores produced by n-gram LM, topic modeling LM, BERT LM and RNNLM to train a rescoring model. We conduct extensive experiments based on a public dataset, and experimental results show that L2RS outperforms not only traditional rescoring methods but also its deep neural network counterparts by a substantial improvement of 20.67% in terms of NDCG@10. L2RS paves the way for developing more effective rescoring models for ASR.

</details>

### [Recognizing long-form speech using streaming end-to-end models](1910.11455.md)
**Arun Narayanan, Rohit Prabhavalkar, Chung-Cheng Chiu, David Rybach et al.** · 2019-10-24

<details>
<summary>Abstract</summary>

All-neural end-to-end (E2E) automatic speech recognition (ASR) systems that use a single neural network to transduce audio to word sequences have been shown to achieve state-of-the-art results on several tasks. In this work, we examine the ability of E2E models to generalize to unseen domains, where we find that models trained on short utterances fail to generalize to long-form speech. We propose two complementary solutions to address this: training on diverse acoustic data, and LSTM state manipulation to simulate long-form audio when training using short utterances. On a synthesized long-form test set, adding data diversity improves word error rate (WER) by 90% relative, while simulating long-form training improves it by 67% relative, though the combination doesn't improve over data diversity alone. On a real long-form call-center test set, adding data diversity improves WER by 40% relative. Simulating long-form training on top of data diversity improves performance by an additional 27% relative.

</details>

### [An Empirical Study of Efficient ASR Rescoring with Transformers](1910.11450.md)
**Hongzhao Huang, Fuchun Peng** · 2019-10-24

<details>
<summary>Abstract</summary>

Neural language models (LMs) have been proved to significantly outperform classical n-gram LMs for language modeling due to their superior abilities to model long-range dependencies in text and handle data sparsity problems. And recently, well configured deep Transformers have exhibited superior performance over shallow stack of recurrent neural network layers for language modeling. However, these state-of-the-art deep Transformer models were mostly engineered to be deep with high model capacity, which makes it computationally inefficient and challenging to be deployed into large-scale real-world applications. Therefore, it is important to develop Transformer LMs that have relatively small model sizes, while still retaining good performance of those much larger models. In this paper, we aim to conduct empirical study on training Transformers with small parameter sizes in the context of ASR rescoring. By combining techniques including subword units, adaptive softmax, large-scale model pre-training, and knowledge distillation, we show that we are able to successfully train small Transformer LMs with significant relative word error rate reductions (WERR) through n-best rescoring. In particular, our experiments on a video speech recognition dataset show that we are able to achieve WERRs ranging from 6.46% to 7.17% while only with 5.5% to 11.9% parameter sizes of the well-known large GPT model [1], whose WERR with rescoring on the same dataset is 7.58%.

</details>

### [Pre-training in Deep Reinforcement Learning for Automatic Speech Recognition](1910.11256.md)
**Thejan Rajapakshe, Rajib Rana, Siddique Latif, Sara Khalifa et al.** · 2019-10-24

<details>
<summary>Abstract</summary>

Deep reinforcement learning (deep RL) is a combination of deep learning with reinforcement learning principles to create efficient methods that can learn by interacting with its environment. This led to breakthroughs in many complex tasks that were previously difficult to solve. However, deep RL requires a large amount of training time that makes it difficult to use in various real-life applications like human-computer interaction (HCI). Therefore, in this paper, we study pre-training in deep RL to reduce the training time and improve the performance in speech recognition, a popular application of HCI. We achieve significantly improved performance in less time on a publicly available speech command recognition dataset.

</details>

### [A Bayesian Approach to Recurrence in Neural Networks](1910.11247.md)
**Philip N. Garner, Sibo Tong** · 2019-10-24

<details>
<summary>Abstract</summary>

We begin by reiterating that common neural network activation functions have simple Bayesian origins. In this spirit, we go on to show that Bayes's theorem also implies a simple recurrence relation; this leads to a Bayesian recurrent unit with a prescribed feedback formulation. We show that introduction of a context indicator leads to a variable feedback that is similar to the forget mechanism in conventional recurrent units. A similar approach leads to a probabilistic input gate. The Bayesian formulation leads naturally to the two pass algorithm of the Kalman smoother or forward-backward algorithm, meaning that inference naturally depends upon future inputs as well as past ones. Experiments on speech recognition confirm that the resulting architecture can perform as well as a bidirectional recurrent network with the same number of parameters as a unidirectional one. Further, when configured explicitly bidirectionally, the architecture can exceed the performance of a conventional bidirectional recurrence.

</details>

### [Analyzing the impact of speaker localization errors on speech separation for automatic speech recognition](1910.11114.md)
**Sunit Sivasankaran, Emmaneul Vincent, Dominique Fohr** · 2019-10-24

<details>
<summary>Abstract</summary>

We investigate the effect of speaker localization on the performance of speech recognition systems in a multispeaker, multichannel environment. Given the speaker location information, speech separation is performed in three stages. In the first stage, a simple delay-and-sum (DS) beamformer is used to enhance the signal impinging from the speaker location which is then used to estimate a time-frequency mask corresponding to the localized speaker using a neural network. This mask is used to compute the second order statistics and to derive an adaptive beamformer in the third stage. We generated a multichannel, multispeaker, reverberated, noisy dataset inspired from the well studied WSJ0-2mix and study the performance of the proposed pipeline in terms of the word error rate (WER). An average WER of $29.4$% was achieved using the ground truth localization information and $42.4$% using the localization information estimated via GCC-PHAT. The signal-to-interference ratio (SIR) between the speakers has a higher impact on the ASR performance, to the extent of reducing the WER by $59$% relative for a SIR increase of $15$ dB. By contrast, increasing the spatial distance to $50^\circ$ or more improves the WER by $23$% relative only

</details>

### [ESPnet-TTS: Unified, Reproducible, and Integratable Open Source End-to-End Text-to-Speech Toolkit](1910.10909.md)
**Tomoki Hayashi, Ryuichi Yamamoto, Katsuki Inoue, Takenori Yoshimura et al.** · 2019-10-24

<details>
<summary>Abstract</summary>

This paper introduces a new end-to-end text-to-speech (E2E-TTS) toolkit named ESPnet-TTS, which is an extension of the open-source speech processing toolkit ESPnet. The toolkit supports state-of-the-art E2E-TTS models, including Tacotron~2, Transformer TTS, and FastSpeech, and also provides recipes inspired by the Kaldi automatic speech recognition (ASR) toolkit. The recipes are based on the design unified with the ESPnet ASR recipe, providing high reproducibility. The toolkit also provides pre-trained models and samples of all of the recipes so that users can use it as a baseline. Furthermore, the unified design enables the integration of ASR functions with TTS, e.g., ASR-based objective evaluation and semi-supervised learning with both ASR and TTS models. This paper describes the design of the toolkit and experimental evaluation in comparison with other toolkits. The experimental results show that our models can achieve state-of-the-art performance comparable to the other latest toolkits, resulting in a mean opinion score (MOS) of 4.25 on the LJSpeech dataset. The toolkit is publicly available at https://github.com/espnet/espnet.

</details>

### [Analyzing ASR pretraining for low-resource speech-to-text translation](1910.10762.md)
**Mihaela C. Stoian, Sameer Bansal, Sharon Goldwater** · 2019-10-23

<details>
<summary>Abstract</summary>

Previous work has shown that for low-resource source languages, automatic speech-to-text translation (AST) can be improved by pretraining an end-to-end model on automatic speech recognition (ASR) data from a high-resource language. However, it is not clear what factors --e.g., language relatedness or size of the pretraining data-- yield the biggest improvements, or whether pretraining can be effectively combined with other methods such as data augmentation. Here, we experiment with pretraining on datasets of varying sizes, including languages related and unrelated to the AST source language. We find that the best predictor of final AST performance is the word error rate of the pretrained ASR model, and that differences in ASR/AST performance correlate with how phonetic information is encoded in the later RNN layers of our model. We also show that pretraining and data augmentation yield complementary benefits for AST.

</details>

### [Correction of Automatic Speech Recognition with Transformer Sequence-to-sequence Model](1910.10697.md)
**Oleksii Hrinchuk, Mariya Popova, Boris Ginsburg** · 2019-10-23

<details>
<summary>Abstract</summary>

In this work, we introduce a simple yet efficient post-processing model for automatic speech recognition (ASR). Our model has Transformer-based encoder-decoder architecture which "translates" ASR model output into grammatically and semantically correct text. We investigate different strategies for regularizing and optimizing the model and show that extensive data augmentation and the initialization with pre-trained weights are required to achieve good performance. On the LibriSpeech benchmark, our method demonstrates significant improvement in word error rate over the baseline acoustic model with greedy decoding, especially on much noisier dev-other and test-other portions of the evaluation dataset. Our model also outperforms baseline with 6-gram language model re-scoring and approaches the performance of re-scoring with Transformer-XL neural language model.

</details>

### [A practical two-stage training strategy for multi-stream end-to-end speech recognition](1910.10671.md)
**Ruizhi Li, Gregory Sell, Xiaofei Wang, Shinji Watanabe et al.** · 2019-10-23

<details>
<summary>Abstract</summary>

The multi-stream paradigm of audio processing, in which several sources are simultaneously considered, has been an active research area for information fusion. Our previous study offered a promising direction within end-to-end automatic speech recognition, where parallel encoders aim to capture diverse information followed by a stream-level fusion based on attention mechanisms to combine the different views. However, with an increasing number of streams resulting in an increasing number of encoders, the previous approach could require substantial memory and massive amounts of parallel data for joint training. In this work, we propose a practical two-stage training scheme. Stage-1 is to train a Universal Feature Extractor (UFE), where encoder outputs are produced from a single-stream model trained with all data. Stage-2 formulates a multi-stream scheme intending to solely train the attention fusion module using the UFE features and pretrained components from Stage-1. Experiments have been conducted on two datasets, DIRHA and AMI, as a multi-stream scenario. Compared with our previous method, this strategy achieves relative word error rate reductions of 8.2--32.4%, while consistently outperforming several conventional combination methods.

</details>

### [Efficient Dynamic WFST Decoding for Personalized Language Models](1910.10670.md)
**Jun Liu, Jiedan Zhu, Vishal Kathuria, Fuchun Peng** · 2019-10-23

<details>
<summary>Abstract</summary>

We propose a two-layer cache mechanism to speed up dynamic WFST decoding with personalized language models. The first layer is a public cache that stores most of the static part of the graph. This is shared globally among all users. A second layer is a private cache that caches the graph that represents the personalized language model, which is only shared by the utterances from a particular user. We also propose two simple yet effective pre-initialization methods, one based on breadth-first search, and another based on a data-driven exploration of decoder states using previous utterances. Experiments with a calling speech recognition task using a personalized contact list demonstrate that the proposed public cache reduces decoding time by factor of three compared to decoding without pre-initialization. Using the private cache provides additional efficiency gains, reducing the decoding time by a factor of five.

</details>

### [End-to-end architectures for ASR-free spoken language understanding](1910.10599.md)
**Elisavet Palogiannidi, Ioannis Gkinis, George Mastrapas, Petr Mizera et al.** · 2019-10-23

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is the problem of extracting the meaning from speech utterances. It is typically addressed as a two-step problem, where an Automatic Speech Recognition (ASR) model is employed to convert speech into text, followed by a Natural Language Understanding (NLU) model to extract meaning from the decoded text. Recently, end-to-end approaches were emerged, aiming at unifying the ASR and NLU into a single SLU deep neural architecture, trained using combinations of ASR and NLU-level recognition units. In this paper, we explore a set of recurrent architectures for intent classification, tailored to the recently introduced Fluent Speech Commands (FSC) dataset, where intents are formed as combinations of three slots (action, object, and location). We show that by combining deep recurrent architectures with standard data augmentation, state-of-the-art results can be attained, without using ASR-level targets or pretrained ASR models. We also investigate its generalizability to new wordings, and we show that the model can perform reasonably well on wordings unseen during training.

</details>

### [A Transformer with Interleaved Self-attention and Convolution for Hybrid Acoustic Models](1910.10352.md)
**Liang Lu** · 2019-10-23

<details>
<summary>Abstract</summary>

Transformer with self-attention has achieved great success in the area of nature language processing. Recently, there have been a few studies on transformer for end-to-end speech recognition, while its application for hybrid acoustic model is still very limited. In this paper, we revisit the transformer-based hybrid acoustic model, and propose a model structure with interleaved self-attention and 1D convolution, which is proven to have faster convergence and higher recognition accuracy. We also study several aspects of the transformer model, including the impact of the positional encoding feature, dropout regularization, as well as training with and without time restriction. We show competitive recognition results on the public Librispeech dataset when compared to the Kaldi baseline at both cross entropy training and sequence training stages. For reproducible research, we release our source code and recipe within the PyKaldi2 toolbox.

</details>

### [RNN based Incremental Online Spoken Language Understanding](1910.10287.md)
**Prashanth Gurunath Shivakumar, Naveen Kumar, Panayiotis Georgiou, Shrikanth Narayanan** · 2019-10-23

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) typically comprises of an automatic speech recognition (ASR) followed by a natural language understanding (NLU) module. The two modules process signals in a blocking sequential fashion, i.e., the NLU often has to wait for the ASR to finish processing on an utterance basis, potentially leading to high latencies that render the spoken interaction less natural. In this paper, we propose recurrent neural network (RNN) based incremental processing towards the SLU task of intent detection. The proposed methodology offers lower latencies than a typical SLU system, without any significant reduction in system accuracy. We introduce and analyze different recurrent neural network architectures for incremental and online processing of the ASR transcripts and compare it to the existing offline systems. A lexical End-of-Sentence (EOS) detector is proposed for segmenting the stream of transcript into sentences for intent classification. Intent detection experiments are conducted on benchmark ATIS, Snips and Facebook's multilingual task oriented dialog datasets modified to emulate a continuous incremental stream of words with no utterance demarcation. We also analyze the prospects of early intent detection, before EOS, with our proposed system.

</details>

### [Instance-Based Model Adaptation For Direct Speech Translation](1910.10663.md)
**Mattia Antonino Di Gangi, Viet-Nhat Nguyen, Matteo Negri, Marco Turchi** · 2019-10-23

<details>
<summary>Abstract</summary>

Despite recent technology advancements, the effectiveness of neural approaches to end-to-end speech-to-text translation is still limited by the paucity of publicly available training corpora. We tackle this limitation with a method to improve data exploitation and boost the system's performance at inference time. Our approach allows us to customize "on the fly" an existing model to each incoming translation request. At its core, it exploits an instance selection procedure to retrieve, from a given pool of data, a small set of samples similar to the input query in terms of latent properties of its audio signal. The retrieved samples are then used for an instance-specific fine-tuning of the model. We evaluate our approach in three different scenarios. In all data conditions (different languages, in/out-of-domain adaptation), our instance-based adaptation yields coherent performance gains over static models.

</details>

### [QuartzNet: Deep Automatic Speech Recognition with 1D Time-Channel Separable Convolutions](1910.10261.md)
**Samuel Kriman, Stanislav Beliaev, Boris Ginsburg, Jocelyn Huang et al.** · 2019-10-22

<details>
<summary>Abstract</summary>

We propose a new end-to-end neural acoustic model for automatic speech recognition. The model is composed of multiple blocks with residual connections between them. Each block consists of one or more modules with 1D time-channel separable convolutional layers, batch normalization, and ReLU layers. It is trained with CTC loss. The proposed network achieves near state-of-the-art accuracy on LibriSpeech and Wall Street Journal, while having fewer parameters than all competing models. We also demonstrate that this model can be effectively fine-tuned on new datasets.

</details>

### [G2G: TTS-Driven Pronunciation Learning for Graphemic Hybrid ASR](1910.12612.md)
**Duc Le, Thilo Koehler, Christian Fuegen, Michael L. Seltzer** · 2019-10-22

<details>
<summary>Abstract</summary>

Grapheme-based acoustic modeling has recently been shown to outperform phoneme-based approaches in both hybrid and end-to-end automatic speech recognition (ASR), even on non-phonemic languages like English. However, graphemic ASR still has problems with rare long-tail words that do not follow the standard spelling conventions seen in training, such as entity names. In this work, we present a novel method to train a statistical grapheme-to-grapheme (G2G) model on text-to-speech data that can rewrite an arbitrary character sequence into more phonetically consistent forms. We show that using G2G to provide alternative pronunciations during decoding reduces Word Error Rate by 3% to 11% relative over a strong graphemic baseline and bridges the gap on rare name recognition with an equivalent phonetic setup. Unlike many previously proposed methods, our method does not require any change to the acoustic model training procedure. This work reaffirms the efficacy of grapheme-based modeling and shows that specialized linguistic knowledge, when available, can be leveraged to improve graphemic ASR.

</details>

### [Robust Neural Machine Translation for Clean and Noisy Speech Transcripts](1910.10238.md)
**Mattia Antonino Di Gangi, Robert Enyedi, Alessandra Brusadin, Marcello Federico** · 2019-10-22

<details>
<summary>Abstract</summary>

Neural machine translation models have shown to achieve high quality when trained and fed with well structured and punctuated input texts. Unfortunately, the latter condition is not met in spoken language translation, where the input is generated by an automatic speech recognition (ASR) system. In this paper, we study how to adapt a strong NMT system to make it robust to typical ASR errors. As in our application scenarios transcripts might be post-edited by human experts, we propose adaptation strategies to train a single system that can translate either clean or noisy input with no supervision on the input type. Our experimental results on a public speech translation data set show that adapting a model on a significant amount of parallel data including ASR transcripts is beneficial with test data of the same type, but produces a small degradation when translating clean text. Adapting on both clean and noisy variants of the same data leads to the best results on both input types.

</details>

### [GPU-Accelerated Viterbi Exact Lattice Decoder for Batched Online and Offline Speech Recognition](1910.10032.md)
**Hugo Braun, Justin Luitjens, Ryan Leary, Tim Kaldewey et al.** · 2019-10-22

<details>
<summary>Abstract</summary>

We present an optimized weighted finite-state transducer (WFST) decoder capable of online streaming and offline batch processing of audio using Graphics Processing Units (GPUs). The decoder is efficient in memory utilization, input/output (I/O) bandwidth, and uses a novel Viterbi implementation designed to maximize parallelism. The reduced memory footprint allows the decoder to process significantly larger graphs than previously possible, while optimizing I/O increases the number of simultaneous streams supported. GPU preprocessing of lattice segments enables intermediate lattice results to be returned to the requestor during streaming inference. Collectively, the proposed algorithm yields up to a 240x speedup over single core CPU decoding, and up to 40x faster decoding than the current state-of-the-art GPU decoder, while returning equivalent results. This decoder design enables deployment of production-grade ASR models on a large spectrum of systems, ranging from large data center servers to low-power edge devices.

</details>

### [Adversarial Example Detection by Classification for Deep Speech Recognition](1910.10013.md)
**Saeid Samizade, Zheng-Hua Tan, Chao Shen, Xiaohong Guan** · 2019-10-22

<details>
<summary>Abstract</summary>

Machine Learning systems are vulnerable to adversarial attacks and will highly likely produce incorrect outputs under these attacks. There are white-box and black-box attacks regarding to adversary's access level to the victim learning algorithm. To defend the learning systems from these attacks, existing methods in the speech domain focus on modifying input signals and testing the behaviours of speech recognizers. We, however, formulate the defense as a classification problem and present a strategy for systematically generating adversarial example datasets: one for white-box attacks and one for black-box attacks, containing both adversarial and normal examples. The white-box attack is a gradient-based method on Baidu DeepSpeech with the Mozilla Common Voice database while the black-box attack is a gradient-free method on a deep model-based keyword spotting system with the Google Speech Command dataset. The generated datasets are used to train a proposed Convolutional Neural Network (CNN), together with cepstral features, to detect adversarial examples. Experimental results show that, it is possible to accurately distinct between adversarial and normal examples for known attacks, in both single-condition and multi-condition training settings, while the performance degrades dramatically for unknown attacks. The adversarial datasets and the source code are made publicly available.

</details>

### [Improving Transformer-based Speech Recognition Using Unsupervised Pre-training](1910.09932.md)
**Dongwei Jiang, Xiaoning Lei, Wubo Li, Ne Luo et al.** · 2019-10-22

<details>
<summary>Abstract</summary>

Speech recognition technologies are gaining enormous popularity in various industrial applications. However, building a good speech recognition system usually requires large amounts of transcribed data, which is expensive to collect. To tackle this problem, an unsupervised pre-training method called Masked Predictive Coding is proposed, which can be applied for unsupervised pre-training with Transformer based model. Experiments on HKUST show that using the same training data, we can achieve CER 23.3%, exceeding the best end-to-end model by over 0.2% absolute CER. With more pre-training data, we can further reduce the CER to 21.0%, or a 11.8% relative CER reduction over baseline.

</details>

### [Transformer-based Acoustic Modeling for Hybrid Speech Recognition](1910.09799.md)
**Yongqiang Wang, Abdelrahman Mohamed, Duc Le, Chunxi Liu et al.** · 2019-10-22

<details>
<summary>Abstract</summary>

We propose and evaluate transformer-based acoustic models (AMs) for hybrid speech recognition. Several modeling choices are discussed in this work, including various positional embedding methods and an iterated loss to enable training deep transformers. We also present a preliminary study of using limited right context in transformer models, which makes it possible for streaming applications. We demonstrate that on the widely used Librispeech benchmark, our transformer-based AM outperforms the best published hybrid result by 19% to 26% relative when the standard n-gram language model (LM) is used. Combined with neural network LM for rescoring, our proposed approach achieves state-of-the-art results on Librispeech. Our findings are also confirmed on a much larger internal dataset.

</details>

### [Signal Combination for Language Identification](1910.09687.md)
**Shengye Wang, Li Wan, Yang Yu, Ignacio Lopez Moreno** · 2019-10-21

<details>
<summary>Abstract</summary>

Google's multilingual speech recognition system combines low-level acoustic signals with language-specific recognizer signals to better predict the language of an utterance. This paper presents our experience with different signal combination methods to improve overall language identification accuracy. We compare the performance of a lattice-based ensemble model and a deep neural network model to combine signals from recognizers with that of a baseline that only uses low-level acoustic signals. Experimental results show that the deep neural network model outperforms the lattice-based ensemble model, and it reduced the error rate from 5.5% in the baseline to 4.3%, which is a 21.8% relative reduction.

</details>

### [AeGAN: Time-Frequency Speech Denoising via Generative Adversarial Networks](1910.12620.md)
**Sherif Abdulatif, Karim Armanious, Karim Guirguis, Jayasankar T. Sajeev et al.** · 2019-10-21

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems are of vital importance nowadays in commonplace tasks such as speech-to-text processing and language translation. This created the need for an ASR system that can operate in realistic crowded environments. Thus, speech enhancement is a valuable building block in ASR systems and other applications such as hearing aids, smartphones and teleconferencing systems. In this paper, a generative adversarial network (GAN) based framework is investigated for the task of speech enhancement, more specifically speech denoising of audio tracks. A new architecture based on CasNet generator and an additional feature-based loss are incorporated to get realistically denoised speech phonetics. Finally, the proposed framework is shown to outperform other learning and traditional model-based speech enhancement approaches.

</details>

### [Predicting ice flow using machine learning](1910.08922.md)
**Yimeng Min, S. Karthik Mukkavilli, Yoshua Bengio** · 2019-10-20

<details>
<summary>Abstract</summary>

Though machine learning has achieved notable success in modeling sequential and spatial data for speech recognition and in computer vision, applications to remote sensing and climate science problems are seldom considered. In this paper, we demonstrate techniques from unsupervised learning of future video frame prediction, to increase the accuracy of ice flow tracking in multi-spectral satellite images. As the volume of cryosphere data increases in coming years, this is an interesting and important opportunity for machine learning to address a global challenge for climate change, risk management from floods, and conserving freshwater resources. Future frame prediction of ice melt and tracking the optical flow of ice dynamics presents modeling difficulties, due to uncertainties in global temperature increase, changing precipitation patterns, occlusion from cloud cover, rapid melting and glacier retreat due to black carbon aerosol deposition, from wildfires or human fossil emissions. We show the adversarial learning method helps improve the accuracy of tracking the optical flow of ice dynamics compared to existing methods in climate science. We present a dataset, IceNet, to encourage machine learning research and to help facilitate further applications in the areas of cryospheric science and climate change.

</details>

### [Neuro-SERKET: Development of Integrative Cognitive System through the Composition of Deep Probabilistic Generative Models](1910.08918.md)
**Tadahiro Taniguchi, Tomoaki Nakamura, Masahiro Suzuki, Ryo Kuniyasu et al.** · 2019-10-20

<details>
<summary>Abstract</summary>

This paper describes a framework for the development of an integrative cognitive system based on probabilistic generative models (PGMs) called Neuro-SERKET. Neuro-SERKET is an extension of SERKET, which can compose elemental PGMs developed in a distributed manner and provide a scheme that allows the composed PGMs to learn throughout the system in an unsupervised way. In addition to the head-to-tail connection supported by SERKET, Neuro-SERKET supports tail-to-tail and head-to-head connections, as well as neural network-based modules, i.e., deep generative models. As an example of a Neuro-SERKET application, an integrative model was developed by composing a variational autoencoder (VAE), a Gaussian mixture model (GMM), latent Dirichlet allocation (LDA), and automatic speech recognition (ASR). The model is called VAE+GMM+LDA+ASR. The performance of VAE+GMM+LDA+ASR and the validity of Neuro-SERKET were demonstrated through a multimodal categorization task using image data and a speech signal of numerical digits.

</details>

### [End-to-End Speech Recognition: A review for the French Language](1910.08502.md)
**Florian Boyer, Jean-Luc Rouas** · 2019-10-18

<details>
<summary>Abstract</summary>

Recently, end-to-end ASR based either on sequence-to-sequence networks or on the CTC objective function gained a lot of interest from the community, achieving competitive results over traditional systems using robust but complex pipelines. One of the main features of end-to-end systems, in addition to the ability to free themselves from extra linguistic resources such as dictionaries or language models, is the capacity to model acoustic units such as characters, subwords or directly words; opening up the capacity to directly translate speech with different representations or levels of knowledge depending on the target language. In this paper we propose a review of the existing end-to-end ASR approaches for the French language. We compare results to conventional state-of-the-art ASR systems and discuss which units are more suited to model the French language.

</details>

### [Indian EmoSpeech Command Dataset: A dataset for emotion based speech recognition in the wild](1910.13801.md)
**Subham Banga, Ujjwal Upadhyay, Piyush Agarwal, Aniket Sharma et al.** · 2019-10-18

<details>
<summary>Abstract</summary>

Speech emotion analysis is an important task which further enables several application use cases. The non-verbal sounds within speech utterances also play a pivotal role in emotion analysis in speech. Due to the widespread use of smartphones, it becomes viable to analyze speech commands captured using microphones for emotion understanding by utilizing on-device machine learning models. The non-verbal information includes the environment background sounds describing the type of surroundings, current situation and activities being performed. In this work, we consider both verbal (speech commands) and non-verbal sounds (background noises) within an utterance for emotion analysis in real-life scenarios. We create an indigenous dataset for this task namely "Indian EmoSpeech Command Dataset". It contains keywords with diverse emotions and background sounds, presented to explore new challenges in audio analysis. We exhaustively compare with various baseline models for emotion analysis on speech commands on several performance metrics. We demonstrate that we achieve a significant average gain of 3.3% in top-one score over a subset of speech command dataset for keyword spotting.

</details>

### [LibriVoxDeEn: A Corpus for German-to-English Speech Translation and German Speech Recognition](1910.07924.md)
**Benjamin Beilharz, Xin Sun, Sariya Karimova, Stefan Riezler** · 2019-10-17

<details>
<summary>Abstract</summary>

We present a corpus of sentence-aligned triples of German audio, German text, and English translation, based on German audiobooks. The speech translation data consist of 110 hours of audio material aligned to over 50k parallel sentences. An even larger dataset comprising 547 hours of German speech aligned to German text is available for speech recognition. The audio data is read speech and thus low in disfluencies. The quality of audio and sentence alignments has been checked by a manual evaluation, showing that speech alignment quality is in general very high. The sentence alignment quality is comparable to well-used parallel translation data and can be adjusted by cutoffs on the automatic alignment score. To our knowledge, this corpus is to date the largest resource for German speech recognition and for end-to-end German-to-English speech translation.

</details>

### [Lead2Gold: Towards exploiting the full potential of noisy transcriptions for speech recognition](1910.07323.md)
**Adrien Dufraux, Emmanuel Vincent, Awni Hannun, Armelle Brun et al.** · 2019-10-16

<details>
<summary>Abstract</summary>

The transcriptions used to train an Automatic Speech Recognition (ASR) system may contain errors. Usually, either a quality control stage discards transcriptions with too many errors, or the noisy transcriptions are used as is. We introduce Lead2Gold, a method to train an ASR system that exploits the full potential of noisy transcriptions. Based on a noise model of transcription errors, Lead2Gold searches for better transcriptions of the training data with a beam search that takes this noise model into account. The beam search is differentiable and does not require a forced alignment step, thus the whole system is trained end-to-end. Lead2Gold can be viewed as a new loss function that can be used on top of any sequence-to-sequence deep neural network. We conduct proof-of-concept experiments on noisy transcriptions generated from letter corruptions with different noise levels. We show that Lead2Gold obtains a better ASR accuracy than a competitive baseline which does not account for the (artificially-introduced) transcription noise.

</details>

### [Transformer ASR with Contextual Block Processing](1910.07204.md)
**Emiru Tsunoo, Yosuke Kashiwagi, Toshiyuki Kumakura, Shinji Watanabe** · 2019-10-16

<details>
<summary>Abstract</summary>

The Transformer self-attention network has recently shown promising performance as an alternative to recurrent neural networks (RNNs) in end-to-end (E2E) automatic speech recognition (ASR) systems. However, the Transformer has a drawback in that the entire input sequence is required to compute self-attention. In this paper, we propose a new block processing method for the Transformer encoder by introducing a context-aware inheritance mechanism. An additional context embedding vector handed over from the previously processed block helps to encode not only local acoustic information but also global linguistic, channel, and speaker attributes. We introduce a novel mask technique to implement the context inheritance to train the model efficiently. Evaluations of the Wall Street Journal (WSJ), Librispeech, VoxForge Italian, and AISHELL-1 Mandarin speech recognition datasets show that our proposed contextual block processing method outperforms naive block processing consistently. Furthermore, the attention weight tendency of each layer is analyzed to clarify how the added contextual inheritance mechanism models the global information.

</details>

### [Analyzing Large Receptive Field Convolutional Networks for Distant Speech Recognition](1910.07047.md)
**Salar Jafarlou, Soheil Khorram, Vinay Kothapally, John H. L. Hansen** · 2019-10-15

<details>
<summary>Abstract</summary>

Despite significant efforts over the last few years to build a robust automatic speech recognition (ASR) system for different acoustic settings, the performance of the current state-of-the-art technologies significantly degrades in noisy reverberant environments. Convolutional Neural Networks (CNNs) have been successfully used to achieve substantial improvements in many speech processing applications including distant speech recognition (DSR). However, standard CNN architectures were not efficient in capturing long-term speech dynamics, which are essential in the design of a robust DSR system. In the present study, we address this issue by investigating variants of large receptive field CNNs (LRF-CNNs) which include deeply recursive networks, dilated convolutional neural networks, and stacked hourglass networks. To compare the efficacy of the aforementioned architectures with the standard CNN for Wall Street Journal (WSJ) corpus, we use a hybrid DNN-HMM based speech recognition system. We extend the study to evaluate the system performances for distant speech simulated using realistic room impulse responses (RIRs). Our experiments show that with fixed number of parameters across all architectures, the large receptive field networks show consistent improvements over the standard CNNs for distant speech. Amongst the explored LRF-CNNs, stacked hourglass network has shown improvements with a 8.9% relative reduction in word error rate (WER) and 10.7% relative improvement in frame accuracy compared to the standard CNNs for distant simulated speech signals.

</details>

### [Transfer Learning for Algorithm Recommendation](1910.07012.md)
**Gean Trindade Pereira, Moisés dos Santos, Edesio Alcobaça, Rafael Mantovani et al.** · 2019-10-15

<details>
<summary>Abstract</summary>

Meta-Learning is a subarea of Machine Learning that aims to take advantage of prior knowledge to learn faster and with fewer data [1]. There are different scenarios where meta-learning can be applied, and one of the most common is algorithm recommendation, where previous experience on applying machine learning algorithms for several datasets can be used to learn which algorithm, from a set of options, would be more suitable for a new dataset [2]. Perhaps the most popular form of meta-learning is transfer learning, which consists of transferring knowledge acquired by a machine learning algorithm in a previous learning task to increase its performance faster in another and similar task [3]. Transfer Learning has been widely applied in a variety of complex tasks such as image classification, machine translation and, speech recognition, achieving remarkable results [4,5,6,7,8]. Although transfer learning is very used in traditional or base-learning, it is still unknown if it is useful in a meta-learning setup. For that purpose, in this paper, we investigate the effects of transferring knowledge in the meta-level instead of base-level. Thus, we train a neural network on meta-datasets related to algorithm recommendation, and then using transfer learning, we reuse the knowledge learned by the neural network in other similar datasets from the same domain, to verify how transferable is the acquired meta-knowledge.

</details>

### [MIMO-SPEECH: End-to-End Multi-Channel Multi-Speaker Speech Recognition](1910.06522.md)
**Xuankai Chang, Wangyou Zhang, Yanmin Qian, Jonathan Le Roux et al.** · 2019-10-15

<details>
<summary>Abstract</summary>

Recently, the end-to-end approach has proven its efficacy in monaural multi-speaker speech recognition. However, high word error rates (WERs) still prevent these systems from being used in practical applications. On the other hand, the spatial information in multi-channel signals has proven helpful in far-field speech recognition tasks. In this work, we propose a novel neural sequence-to-sequence (seq2seq) architecture, MIMO-Speech, which extends the original seq2seq to deal with multi-channel input and multi-channel output so that it can fully model multi-channel multi-speaker speech separation and recognition. MIMO-Speech is a fully neural end-to-end framework, which is optimized only via an ASR criterion. It is comprised of: 1) a monaural masking network, 2) a multi-source neural beamformer, and 3) a multi-output speech recognition model. With this processing, the input overlapped speech is directly mapped to text sequences. We further adopted a curriculum learning strategy, making the best use of the training set to improve the performance. The experiments on the spatialized wsj1-2mix corpus show that our model can achieve more than 60% WER reduction compared to the single-channel system with high quality enhanced signals (SI-SDR = 23.1 dB) obtained by the above separation function.

</details>

### [VAIS ASR: Building a conversational speech recognition system using language model combination](1910.05603.md)
**Quang Minh Nguyen, Thai Binh Nguyen, Ngoc Phuong Pham, The Loc Nguyen** · 2019-10-12

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have been evolving quickly and reaching human parity in certain cases. The systems usually perform pretty well on reading style and clean speech, however, most of the available systems suffer from situation where the speaking style is conversation and in noisy environments. It is not straight-forward to tackle such problems due to difficulties in data collection for both speech and text. In this paper, we attempt to mitigate the problems using language models combination techniques that allows us to utilize both large amount of writing style text and small number of conversation text data. Evaluation on the VLSP 2019 ASR challenges showed that our system achieved 4.85% WER on the VLSP 2018 and 15.09% WER on the VLSP 2019 data sets.

</details>

### [vq-wav2vec: Self-Supervised Learning of Discrete Speech Representations](1910.05453.md)
**Alexei Baevski, Steffen Schneider, Michael Auli** · 2019-10-12

<details>
<summary>Abstract</summary>

We propose vq-wav2vec to learn discrete representations of audio segments through a wav2vec-style self-supervised context prediction task. The algorithm uses either a gumbel softmax or online k-means clustering to quantize the dense representations. Discretization enables the direct application of algorithms from the NLP community which require discrete inputs. Experiments show that BERT pre-training achieves a new state of the art on TIMIT phoneme classification and WSJ speech recognition.

</details>

### [One-To-Many Multilingual End-to-end Speech Translation](1910.03320.md)
**Mattia Antonino Di Gangi, Matteo Negri, Marco Turchi** · 2019-10-08

<details>
<summary>Abstract</summary>

Nowadays, training end-to-end neural models for spoken language translation (SLT) still has to confront with extreme data scarcity conditions. The existing SLT parallel corpora are indeed orders of magnitude smaller than those available for the closely related tasks of automatic speech recognition (ASR) and machine translation (MT), which usually comprise tens of millions of instances. To cope with data paucity, in this paper we explore the effectiveness of transfer learning in end-to-end SLT by presenting a multilingual approach to the task. Multilingual solutions are widely studied in MT and usually rely on ``\textit{target forcing}'', in which multilingual parallel data are combined to train a single model by prepending to the input sequences a language token that specifies the target language. However, when tested in speech translation, our experiments show that MT-like \textit{target forcing}, used as is, is not effective in discriminating among the target languages. Thus, we propose a variant that uses target-language embeddings to shift the input representations in different portions of the space according to the language, so to better support the production of output in the desired target language. Our experiments on end-to-end SLT from English into six languages show important improvements when translating into similar languages, especially when these are supported by scarce data. Further improvements are obtained when using English ASR data as an additional language (up to $+2.5$ BLEU points).

</details>

### [SNDCNN: Self-normalizing deep CNNs with scaled exponential linear units for speech recognition](1910.01992.md)
**Zhen Huang, Tim Ng, Leo Liu, Henry Mason et al.** · 2019-10-04

<details>
<summary>Abstract</summary>

Very deep CNNs achieve state-of-the-art results in both computer vision and speech recognition, but are difficult to train. The most popular way to train very deep CNNs is to use shortcut connections (SC) together with batch normalization (BN). Inspired by Self- Normalizing Neural Networks, we propose the self-normalizing deep CNN (SNDCNN) based acoustic model topology, by removing the SC/BN and replacing the typical RELU activations with scaled exponential linear unit (SELU) in ResNet-50. SELU activations make the network self-normalizing and remove the need for both shortcut connections and batch normalization. Compared to ResNet- 50, we can achieve the same or lower (up to 4.5% relative) word error rate (WER) while boosting both training and inference speed by 60%-80%. We also explore other model inference optimization schemes to further reduce latency for production use.

</details>

### [Modeling Confidence in Sequence-to-Sequence Models](1910.01859.md)
**Jan Niehues, Ngoc-Quan Pham** · 2019-10-04

<details>
<summary>Abstract</summary>

Recently, significant improvements have been achieved in various natural language processing tasks using neural sequence-to-sequence models. While aiming for the best generation quality is important, ultimately it is also necessary to develop models that can assess the quality of their output. In this work, we propose to use the similarity between training and test conditions as a measure for models' confidence. We investigate methods solely using the similarity as well as methods combining it with the posterior probability. While traditionally only target tokens are annotated with confidence measures, we also investigate methods to annotate source tokens with confidence. By learning an internal alignment model, we can significantly improve confidence projection over using state-of-the-art external alignment tools. We evaluate the proposed methods on downstream confidence estimation for machine translation (MT). We show improvements on segment-level confidence estimation as well as on confidence estimation for source tokens. In addition, we show that the same methods can also be applied to other tasks using sequence-to-sequence models. On the automatic speech recognition (ASR) task, we are able to find 60% of the errors by looking at 20% of the data.

</details>

### [Convolutional Neural Networks for Speech Controlled Prosthetic Hands](1910.01918.md)
**Mohsen Jafarzadeh, Yonas Tadesse** · 2019-10-03

<details>
<summary>Abstract</summary>

Speech recognition is one of the key topics in artificial intelligence, as it is one of the most common forms of communication in humans. Researchers have developed many speech-controlled prosthetic hands in the past decades, utilizing conventional speech recognition systems that use a combination of neural network and hidden Markov model. Recent advancements in general-purpose graphics processing units (GPGPUs) enable intelligent devices to run deep neural networks in real-time. Thus, state-of-the-art speech recognition systems have rapidly shifted from the paradigm of composite subsystems optimization to the paradigm of end-to-end optimization. However, a low-power embedded GPGPU cannot run these speech recognition systems in real-time. In this paper, we show the development of deep convolutional neural networks (CNN) for speech control of prosthetic hands that run in real-time on a NVIDIA Jetson TX2 developer kit. First, the device captures and converts speech into 2D features (like spectrogram). The CNN receives the 2D features and classifies the hand gestures. Finally, the hand gesture classes are sent to the prosthetic hand motion control system. The whole system is written in Python with Keras, a deep learning library that has a TensorFlow backend. Our experiments on the CNN demonstrate the 91% accuracy and 2ms running time of hand gestures (text output) from speech commands, which can be used to control the prosthetic hands in real-time.

</details>

### [Neural Zero-Inflated Quality Estimation Model For Automatic Speech Recognition System](1910.01289.md)
**Kai Fan, Jiayi Wang, Bo Li, Shiliang Zhang et al.** · 2019-10-03

<details>
<summary>Abstract</summary>

The performances of automatic speech recognition (ASR) systems are usually evaluated by the metric word error rate (WER) when the manually transcribed data are provided, which are, however, expensively available in the real scenario. In addition, the empirical distribution of WER for most ASR systems usually tends to put a significant mass near zero, making it difficult to simulate with a single continuous distribution. In order to address the two issues of ASR quality estimation (QE), we propose a novel neural zero-inflated model to predict the WER of the ASR result without transcripts. We design a neural zero-inflated beta regression on top of a bidirectional transformer language model conditional on speech features (speech-BERT). We adopt the pre-training strategy of token level mask language modeling for speech-BERT as well, and further fine-tune with our zero-inflated layer for the mixture of discrete and continuous outputs. The experimental results show that our approach achieves better performance on WER prediction in the metrics of Pearson and MAE, compared with most existed quality estimation algorithms for ASR or machine translation.

</details>

### [From Senones to Chenones: Tied Context-Dependent Graphemes for Hybrid Speech Recognition](1910.01493.md)
**Duc Le, Xiaohui Zhang, Weiyi Zheng, Christian Fügen et al.** · 2019-10-02

<details>
<summary>Abstract</summary>

There is an implicit assumption that traditional hybrid approaches for automatic speech recognition (ASR) cannot directly model graphemes and need to rely on phonetic lexicons to get competitive performance, especially on English which has poor grapheme-phoneme correspondence. In this work, we show for the first time that, on English, hybrid ASR systems can in fact model graphemes effectively by leveraging tied context-dependent graphemes, i.e., chenones. Our chenone-based systems significantly outperform equivalent senone baselines by 4.5% to 11.1% relative on three different English datasets. Our results on Librispeech are state-of-the-art compared to other hybrid approaches and competitive with previously published end-to-end numbers. Further analysis shows that chenones can better utilize powerful acoustic models and large training data, and require context- and position-dependent modeling to work well. Chenone-based systems also outperform senone baselines on proper noun and rare word recognition, an area where the latter is traditionally thought to have an advantage. Our work provides an alternative for end-to-end ASR and establishes that hybrid systems can be improved by dropping the reliance on phonetic knowledge.

</details>

### [State-of-the-Art Speech Recognition Using Multi-Stream Self-Attention With Dilated 1D Convolutions](1910.00716.md)
**Kyu J. Han, Ramon Prieto, Kaixing Wu, Tao Ma** · 2019-10-01

<details>
<summary>Abstract</summary>

Self-attention has been a huge success for many downstream tasks in NLP, which led to exploration of applying self-attention to speech problems as well. The efficacy of self-attention in speech applications, however, seems not fully blown yet since it is challenging to handle highly correlated speech frames in the context of self-attention. In this paper we propose a new neural network model architecture, namely multi-stream self-attention, to address the issue thus make the self-attention mechanism more effective for speech recognition. The proposed model architecture consists of parallel streams of self-attention encoders, and each stream has layers of 1D convolutions with dilated kernels whose dilation rates are unique given stream, followed by a self-attention layer. The self-attention mechanism in each stream pays attention to only one resolution of input speech frames and the attentive computation can be more efficient. In a later stage, outputs from all the streams are concatenated then linearly projected to the final embedding. By stacking the proposed multi-stream self-attention encoder blocks and rescoring the resultant lattices with neural network language models, we achieve the word error rate of 2.2% on the test-clean dataset of the LibriSpeech corpus, the best number reported thus far on the dataset.

</details>

### [Domain Expansion in DNN-based Acoustic Models for Robust Speech Recognition](1910.00565.md)
**Shahram Ghorbani, Soheil Khorram, John H. L. Hansen** · 2019-10-01

<details>
<summary>Abstract</summary>

Training acoustic models with sequentially incoming data -- while both leveraging new data and avoiding the forgetting effect-- is an essential obstacle to achieving human intelligence level in speech recognition. An obvious approach to leverage data from a new domain (e.g., new accented speech) is to first generate a comprehensive dataset of all domains, by combining all available data, and then use this dataset to retrain the acoustic models. However, as the amount of training data grows, storing and retraining on such a large-scale dataset becomes practically impossible. To deal with this problem, in this study, we study several domain expansion techniques which exploit only the data of the new domain to build a stronger model for all domains. These techniques are aimed at learning the new domain with a minimal forgetting effect (i.e., they maintain original model performance). These techniques modify the adaptation procedure by imposing new constraints including (1) weight constraint adaptation (WCA): keeping the model parameters close to the original model parameters; (2) elastic weight consolidation (EWC): slowing down training for parameters that are important for previously established domains; (3) soft KL-divergence (SKLD): restricting the KL-divergence between the original and the adapted model output distributions; and (4) hybrid SKLD-EWC: incorporating both SKLD and EWC constraints. We evaluate these techniques in an accent adaptation task in which we adapt a deep neural network (DNN) acoustic model trained with native English to three different English accents: Australian, Hispanic, and Indian. The experimental results show that SKLD significantly outperforms EWC, and EWC works better than WCA. The hybrid SKLD-EWC technique results in the best overall performance.

</details>

### [Additional Shared Decoder on Siamese Multi-view Encoders for Learning Acoustic Word Embeddings](1910.00341.md)
**Myunghun Jung, Hyungjun Lim, Jahyun Goo, Youngmoon Jung et al.** · 2019-10-01

<details>
<summary>Abstract</summary>

Acoustic word embeddings --- fixed-dimensional vector representations of arbitrary-length words --- have attracted increasing interest in query-by-example spoken term detection. Recently, on the fact that the orthography of text labels partly reflects the phonetic similarity between the words' pronunciation, a multi-view approach has been introduced that jointly learns acoustic and text embeddings. It showed that it is possible to learn discriminative embeddings by designing the objective which takes text labels as well as word segments. In this paper, we propose a network architecture that expands the multi-view approach by combining the Siamese multi-view encoders with a shared decoder network to maximize the effect of the relationship between acoustic and text embeddings in embedding space. Discriminatively trained with multi-view triplet loss and decoding loss, our proposed approach achieves better performance on acoustic word discrimination task with the WSJ dataset, resulting in 11.1% relative improvement in average precision. We also present experimental results on cross-view word discrimination and word level speech recognition tasks.

</details>

### [Multilingual End-to-End Speech Translation](1910.00254.md)
**Hirofumi Inaguma, Kevin Duh, Tatsuya Kawahara, Shinji Watanabe** · 2019-10-01

<details>
<summary>Abstract</summary>

In this paper, we propose a simple yet effective framework for multilingual end-to-end speech translation (ST), in which speech utterances in source languages are directly translated to the desired target languages with a universal sequence-to-sequence architecture. While multilingual models have shown to be useful for automatic speech recognition (ASR) and machine translation (MT), this is the first time they are applied to the end-to-end ST problem. We show the effectiveness of multilingual end-to-end ST in two scenarios: one-to-many and many-to-many translations with publicly available data. We experimentally confirm that multilingual end-to-end ST models significantly outperform bilingual ones in both scenarios. The generalization of multilingual training is also evaluated in a transfer learning scenario to a very low-resource language pair. All of our codes and the database are publicly available to encourage further research in this emergent multilingual ST topic.

</details>

### [FaSNet: Low-latency Adaptive Beamforming for Multi-microphone Audio Processing](1909.13387.md)
**Yi Luo, Enea Ceolini, Cong Han, Shih-Chii Liu et al.** · 2019-09-29

<details>
<summary>Abstract</summary>

Beamforming has been extensively investigated for multi-channel audio processing tasks. Recently, learning-based beamforming methods, sometimes called \textit{neural beamformers}, have achieved significant improvements in both signal quality (e.g. signal-to-noise ratio (SNR)) and speech recognition (e.g. word error rate (WER)). Such systems are generally non-causal and require a large context for robust estimation of inter-channel features, which is impractical in applications requiring low-latency responses. In this paper, we propose filter-and-sum network (FaSNet), a time-domain, filter-based beamforming approach suitable for low-latency scenarios. FaSNet has a two-stage system design that first learns frame-level time-domain adaptive beamforming filters for a selected reference channel, and then calculate the filters for all remaining channels. The filtered outputs at all channels are summed to generate the final output. Experiments show that despite its small model size, FaSNet is able to outperform several traditional oracle beamformers with respect to scale-invariant signal-to-noise ratio (SI-SNR) in reverberant speech enhancement and separation tasks. Moreover, when trained with a frequency-domain objective function on the CHiME-3 dataset, FaSNet achieves 14.3\% relative word error rate reduction (RWERR) compared with the baseline model. These results show the efficacy of FaSNet particularly in reverberant and noisy signal conditions.

</details>

### [Language-Agnostic Syllabification with Neural Sequence Labeling](1909.13362.md)
**Jacob Krantz, Maxwell Dulin, Paul De Palma** · 2019-09-29

<details>
<summary>Abstract</summary>

The identification of syllables within phonetic sequences is known as syllabification. This task is thought to play an important role in natural language understanding, speech production, and the development of speech recognition systems. The concept of the syllable is cross-linguistic, though formal definitions are rarely agreed upon, even within a language. In response, data-driven syllabification methods have been developed to learn from syllabified examples. These methods often employ classical machine learning sequence labeling models. In recent years, recurrence-based neural networks have been shown to perform increasingly well for sequence labeling tasks such as named entity recognition (NER), part of speech (POS) tagging, and chunking. We present a novel approach to the syllabification problem which leverages modern neural network techniques. Our network is constructed with long short-term memory (LSTM) cells, a convolutional component, and a conditional random field (CRF) output layer. Existing syllabification approaches are rarely evaluated across multiple language families. To demonstrate cross-linguistic generalizability, we show that the network is competitive with state of the art systems in syllabifying English, Dutch, Italian, French, Manipuri, and Basque datasets.

</details>

### [Neural Hybrid Recommender: Recommendation needs collaboration](1909.13330.md)
**Ezgi Yıldırım, Payam Azad, Şule Gündüz Öğüdücü** · 2019-09-29

<details>
<summary>Abstract</summary>

In recent years, deep learning has gained an indisputable success in computer vision, speech recognition, and natural language processing. After its rising success on these challenging areas, it has been studied on recommender systems as well, but mostly to include content features into traditional methods. In this paper, we introduce a generalized neural network-based recommender framework that is easily extendable by additional networks. This framework named NHR, short for Neural Hybrid Recommender allows us to include more elaborate information from the same and different data sources. We have worked on item prediction problems, but the framework can be used for rating prediction problems as well with a single change on the loss function. To evaluate the effect of such a framework, we have tested our approach on benchmark and not yet experimented datasets. The results in these real-world datasets show the superior performance of our approach in comparison with the state-of-the-art methods.

</details>

### [AdaptivFloat: A Floating-point based Data Type for Resilient Deep Learning Inference](1909.13271.md)
**Thierry Tambe, En-Yu Yang, Zishen Wan, Yuntian Deng et al.** · 2019-09-29

<details>
<summary>Abstract</summary>

Conventional hardware-friendly quantization methods, such as fixed-point or integer, tend to perform poorly at very low word sizes as their shrinking dynamic ranges cannot adequately capture the wide data distributions commonly seen in sequence transduction models. We present AdaptivFloat, a floating-point inspired number representation format for deep learning that dynamically maximizes and optimally clips its available dynamic range, at a layer granularity, in order to create faithful encoding of neural network parameters. AdaptivFloat consistently produces higher inference accuracies compared to block floating-point, uniform, IEEE-like float or posit encodings at very low precision ($\leq$ 8-bit) across a diverse set of state-of-the-art neural network topologies. And notably, AdaptivFloat is seen surpassing baseline FP32 performance by up to +0.3 in BLEU score and -0.75 in word error rate at weight bit widths that are $\leq$ 8-bit. Experimental results on a deep neural network (DNN) hardware accelerator, exploiting AdaptivFloat logic in its computational datapath, demonstrate per-operation energy and area that is 0.9$\times$ and 1.14$\times$, respectively, that of equivalent bit width integer-based accelerator variants.

</details>

### [Self-Attention Transducers for End-to-End Speech Recognition](1909.13037.md)
**Zhengkun Tian, Jiangyan Yi, Jianhua Tao, Ye Bai et al.** · 2019-09-28

<details>
<summary>Abstract</summary>

Recurrent neural network transducers (RNN-T) have been successfully applied in end-to-end speech recognition. However, the recurrent structure makes it difficult for parallelization . In this paper, we propose a self-attention transducer (SA-T) for speech recognition. RNNs are replaced with self-attention blocks, which are powerful to model long-term dependencies inside sequences and able to be efficiently parallelized. Furthermore, a path-aware regularization is proposed to assist SA-T to learn alignments and improve the performance. Additionally, a chunk-flow mechanism is utilized to achieve online decoding. All experiments are conducted on a Mandarin Chinese dataset AISHELL-1. The results demonstrate that our proposed approach achieves a 21.3% relative reduction in character error rate compared with the baseline RNN-T. In addition, the SA-T with chunk-flow mechanism can perform online decoding with only a little degradation of the performance.

</details>

### [End-to-End Code-Switching ASR for Low-Resourced Language Pairs](1909.12681.md)
**Xianghu Yue, Grandee Lee, Emre Yılmaz, Fang Deng et al.** · 2019-09-27

<details>
<summary>Abstract</summary>

Despite the significant progress in end-to-end (E2E) automatic speech recognition (ASR), E2E ASR for low resourced code-switching (CS) speech has not been well studied. In this work, we describe an E2E ASR pipeline for the recognition of CS speech in which a low-resourced language is mixed with a high resourced language. Low-resourcedness in acoustic data hinders the performance of E2E ASR systems more severely than the conventional ASR systems.~To mitigate this problem in the transcription of archives with code-switching Frisian-Dutch speech, we integrate a designated decoding scheme and perform rescoring with neural network-based language models to enable better utilization of the available textual resources. We first incorporate a multi-graph decoding approach which creates parallel search spaces for each monolingual and mixed recognition tasks to maximize the utilization of the textual resources from each language. Further, language model rescoring is performed using a recurrent neural network pre-trained with cross-lingual embedding and further adapted with the limited amount of in-domain CS text. The ASR experiments demonstrate the effectiveness of the described techniques in improving the recognition performance of an E2E CS ASR system in a low-resourced scenario.

</details>

### [Improving RNN Transducer Modeling for End-to-End Speech Recognition](1909.12415.md)
**Jinyu Li, Rui Zhao, Hu Hu, Yifan Gong** · 2019-09-26

<details>
<summary>Abstract</summary>

In the last few years, an emerging trend in automatic speech recognition research is the study of end-to-end (E2E) systems. Connectionist Temporal Classification (CTC), Attention Encoder-Decoder (AED), and RNN Transducer (RNN-T) are the most popular three methods. Among these three methods, RNN-T has the advantages to do online streaming which is challenging to AED and it doesn't have CTC's frame-independence assumption. In this paper, we improve the RNN-T training in two aspects. First, we optimize the training algorithm of RNN-T to reduce the memory consumption so that we can have larger training minibatch for faster training speed. Second, we propose better model structures so that we obtain RNN-T models with the very good accuracy but small footprint. Trained with 30 thousand hours anonymized and transcribed Microsoft production data, the best RNN-T model with even smaller model size (216 Megabytes) achieves up-to 11.8% relative word error rate (WER) reduction from the baseline RNN-T model. This best RNN-T model is significantly better than the device hybrid model with similar size by achieving up-to 15.0% relative WER reduction, and obtains similar WERs as the server hybrid model of 5120 Megabytes in size.

</details>

### [Optimizing Speech Recognition For The Edge](1909.12408.md)
**Yuan Shangguan, Jian Li, Qiao Liang, Raziel Alvarez et al.** · 2019-09-26

<details>
<summary>Abstract</summary>

While most deployed speech recognition systems today still run on servers, we are in the midst of a transition towards deployments on edge devices. This leap to the edge is powered by the progression from traditional speech recognition pipelines to end-to-end (E2E) neural architectures, and the parallel development of more efficient neural network topologies and optimization techniques. Thus, we are now able to create highly accurate speech recognizers that are both small and fast enough to execute on typical mobile devices. In this paper, we begin with a baseline RNN-Transducer architecture comprised of Long Short-Term Memory (LSTM) layers. We then experiment with a variety of more computationally efficient layer types, as well as apply optimization techniques like neural connection pruning and parameter quantization to construct a small, high quality, on-device speech recognizer that is an order of magnitude smaller than the baseline system without any optimizations.

</details>

### [DARTS: Dialectal Arabic Transcription System](1909.12163.md)
**Sameer Khurana, Ahmed Ali, James Glass** · 2019-09-26

<details>
<summary>Abstract</summary>

We present the speech to text transcription system, called DARTS, for low resource Egyptian Arabic dialect. We analyze the following; transfer learning from high resource broadcast domain to low-resource dialectal domain and semi-supervised learning where we use in-domain unlabeled audio data collected from YouTube. Key features of our system are: A deep neural network acoustic model that consists of a front end Convolutional Neural Network (CNN) followed by several layers of Time Delayed Neural Network (TDNN) and Long-Short Term Memory Recurrent Neural Network (LSTM); sequence discriminative training of the acoustic model; n-gram and recurrent neural network language model for decoding and N-best list rescoring. We show that a simple transfer learning method can achieve good results. The results are further improved by using unlabeled data from YouTube in a semi-supervised setup. Various systems are combined to give the final system that achieves the lowest word error on on the community standard Egyptian-Arabic speech dataset (MGB-3).

</details>

### [An Investigation into the Effectiveness of Enhancement in ASR Training and Test for CHiME-5 Dinner Party Transcription](1909.12208.md)
**Catalin Zorila, Christoph Boeddeker, Rama Doddipatla, Reinhold Haeb-Umbach** · 2019-09-26

<details>
<summary>Abstract</summary>

Despite the strong modeling power of neural network acoustic models, speech enhancement has been shown to deliver additional word error rate improvements if multi-channel data is available. However, there has been a longstanding debate whether enhancement should also be carried out on the ASR training data. In an extensive experimental evaluation on the acoustically very challenging CHiME-5 dinner party data we show that: (i) cleaning up the training data can lead to substantial error rate reductions, and (ii) enhancement in training is advisable as long as enhancement in test is at least as strong as in training. This approach stands in contrast and delivers larger gains than the common strategy reported in the literature to augment the training database with additional artificially degraded speech. Together with an acoustic model topology consisting of initial CNN layers followed by factorized TDNN layers we achieve with 41.6% and 43.2% WER on the DEV and EVAL test sets, respectively, a new single-system state-of-the-art result on the CHiME-5 data. This is a 8% relative improvement compared to the best word error rate published so far for a speech recognizer without system combination.

</details>

### [Breaking the Data Barrier: Towards Robust Speech Translation via Adversarial Stability Training](1909.11430.md)
**Qiao Cheng, Meiyuan Fang, Yaqian Han, Jin Huang et al.** · 2019-09-25

<details>
<summary>Abstract</summary>

In a pipeline speech translation system, automatic speech recognition (ASR) system will transmit errors in recognition to the downstream machine translation (MT) system. A standard machine translation system is usually trained on parallel corpus composed of clean text and will perform poorly on text with recognition noise, a gap well known in speech translation community. In this paper, we propose a training architecture which aims at making a neural machine translation model more robust against speech recognition errors. Our approach addresses the encoder and the decoder simultaneously using adversarial learning and data augmentation, respectively. Experimental results on IWSLT2018 speech translation task show that our approach can bridge the gap between the ASR output and the MT input, outperforms the baseline by up to 2.83 BLEU on noisy ASR output, while maintaining close performance on clean text.

</details>

### [Understanding Semantics from Speech Through Pre-training](1909.10924.md)
**Pengwei Wang, Liangchen Wei, Yong Cao, Jinghui Xie et al.** · 2019-09-24

<details>
<summary>Abstract</summary>

End-to-end Spoken Language Understanding (SLU) is proposed to infer the semantic meaning directly from audio features without intermediate text representation. Although the acoustic model component of an end-to-end SLU system can be pre-trained with Automatic Speech Recognition (ASR) targets, the SLU component can only learn semantic features from limited task-specific training data. In this paper, for the first time we propose to do large-scale unsupervised pre-training for the SLU component of an end-to-end SLU system, so that the SLU component may preserve semantic features from massive unlabeled audio data. As the output of the acoustic model component, i.e. phoneme posterior sequences, has much different characteristic from text sequences, we propose a novel pre-training model called BERT-PLM, which stands for Bidirectional Encoder Representations from Transformers through Permutation Language Modeling. BERT-PLM trains the SLU component on unlabeled data through a regression objective equivalent to the partial permutation language modeling objective, while leverages full bi-directional context information with BERT networks. The experiment results show that our approach out-perform the state-of-the-art end-to-end systems with over 12.5% error reduction.

</details>

### [Automatic Lyrics Alignment and Transcription in Polyphonic Music: Does Background Music Help?](1909.10200.md)
**Chitralekha Gupta, Emre Yılmaz, Haizhou Li** · 2019-09-23

<details>
<summary>Abstract</summary>

Background music affects lyrics intelligibility of singing vocals in a music piece. Automatic lyrics alignment and transcription in polyphonic music are challenging tasks because the singing vocals are corrupted by the background music. In this work, we propose to learn music genre-specific characteristics to train polyphonic acoustic models. We first compare several automatic speech recognition pipelines for the application of lyrics transcription. We then present the lyrics alignment and transcription performance of music-informed acoustic models for the best-performing pipeline, and systematically study the impact of music genre and language model on the performance. With such genre-based approach, we explicitly model the music without removing it during acoustic modeling. The proposed approach outperforms all competing systems in the lyrics alignment and transcription tasks on several well-known polyphonic test datasets.

</details>

### [Improving OOV Detection and Resolution with External Language Models in Acoustic-to-Word ASR](1909.09993.md)
**Hirofumi Inaguma, Masato Mimura, Shinsuke Sakai, Tatsuya Kawahara** · 2019-09-22

<details>
<summary>Abstract</summary>

Acoustic-to-word (A2W) end-to-end automatic speech recognition (ASR) systems have attracted attention because of an extremely simplified architecture and fast decoding. To alleviate data sparseness issues due to infrequent words, the combination with an acoustic-to-character (A2C) model is investigated. Moreover, the A2C model can be used to recover out-of-vocabulary (OOV) words that are not covered by the A2W model, but this requires accurate detection of OOV words. A2W models learn contexts with both acoustic and transcripts; therefore they tend to falsely recognize OOV words as words in the vocabulary. In this paper, we tackle this problem by using external language models (LM), which are trained only with transcriptions and have better linguistic information to detect OOV words. The A2C model is used to resolve these OOV words. Experimental evaluations show that external LMs have the effects of not only reducing errors but also increasing the number of detected OOV words, and the proposed method significantly improves performances in English conversational and Japanese lecture corpora, especially for out-of-domain scenario. We also investigate the impact of the vocabulary size of A2W models and the data size for training LMs. Moreover, our approach can reduce the vocabulary size several times with marginal performance degradation.

</details>

### [Persian Signature Verification using Fully Convolutional Networks](1909.09720.md)
**Mohammad Rezaei, Nader Naderi** · 2019-09-20

<details>
<summary>Abstract</summary>

Fully convolutional networks (FCNs) have been recently used for feature extraction and classification in image and speech recognition, where their inputs have been raw signal or other complicated features. Persian signature verification is done using conventional convolutional neural networks (CNNs). In this paper, we propose to use FCN for learning a robust feature extraction from the raw signature images. FCN can be considered as a variant of CNN where its fully connected layers are replaced with a global pooling layer. In the proposed manner, FCN inputs are raw signature images and convolution filter size is fixed. Recognition accuracy on UTSig database, shows that FCN with a global average pooling outperforms CNN.

</details>

### [Self-Training for End-to-End Speech Recognition](1909.09116.md)
**Jacob Kahn, Ann Lee, Awni Hannun** · 2019-09-19

<details>
<summary>Abstract</summary>

We revisit self-training in the context of end-to-end speech recognition. We demonstrate that training with pseudo-labels can substantially improve the accuracy of a baseline model. Key to our approach are a strong baseline acoustic and language model used to generate the pseudo-labels, filtering mechanisms tailored to common errors from sequence-to-sequence models, and a novel ensemble approach to increase pseudo-label diversity. Experiments on the LibriSpeech corpus show that with an ensemble of four models and label filtering, self-training yields a 33.9% relative improvement in WER compared with a baseline trained on 100 hours of labelled data in the noisy speech setting. In the clean speech setting, self-training recovers 59.3% of the gap between the baseline and an oracle model, which is at least 93.8% relatively higher than what previous approaches can achieve.

</details>

### [A Random Gossip BMUF Process for Neural Language Modeling](1909.09010.md)
**Yiheng Huang, Jinchuan Tian, Lei Han, Guangsen Wang et al.** · 2019-09-19

<details>
<summary>Abstract</summary>

Neural network language model (NNLM) is an essential component of industrial ASR systems. One important challenge of training an NNLM is to leverage between scaling the learning process and handling big data. Conventional approaches such as block momentum provides a blockwise model update filtering (BMUF) process and achieves almost linear speedups with no performance degradation for speech recognition. However, it needs to calculate the model average from all computing nodes (e.g., GPUs) and when the number of computing nodes is large, the learning suffers from the severe communication latency. As a consequence, BMUF is not suitable under restricted network conditions. In this paper, we present a decentralized BMUF process, in which the model is split into different components, each of which is updated by communicating to some randomly chosen neighbor nodes with the same component, followed by a BMUF-like process. We apply this method to several LSTM language modeling tasks. Experimental results show that our approach achieves consistently better performance than conventional BMUF. In particular, we obtain a lower perplexity than the single-GPU baseline on the wiki-text-103 benchmark using 4 GPUs. In addition, no performance degradation is observed when scaling to 8 and 16 GPUs.

</details>

### [A Comparison of Hybrid and End-to-End Models for Syllable Recognition](1909.12232.md)
**Sebastian P. Bayerl, Korbinian Riedhammer** · 2019-09-19

<details>
<summary>Abstract</summary>

This paper presents a comparison of a traditional hybrid speech recognition system (kaldi using WFST and TDNN with lattice-free MMI) and a lexicon-free end-to-end (TensorFlow implementation of multi-layer LSTM with CTC training) models for German syllable recognition on the Verbmobil corpus. The results show that explicitly modeling prior knowledge is still valuable in building recognition systems. With a strong language model (LM) based on syllables, the structured approach significantly outperforms the end-to-end model. The best word error rate (WER) regarding syllables was achieved using kaldi with a 4-gram LM, modeling all syllables observed in the training set. It achieved 10.0% WER w.r.t. the syllables, compared to the end-to-end approach where the best WER was 27.53%. The work presented here has implications for building future recognition systems that operate independent of a large vocabulary, as typically used in a tasks such as recognition of syllabic or agglutinative languages, out-of-vocabulary techniques, keyword search indexing and medical speech processing.

</details>

### [Espresso: A Fast End-to-end Neural Speech Recognition Toolkit](1909.08723.md)
**Yiming Wang, Tongfei Chen, Hainan Xu, Shuoyang Ding et al.** · 2019-09-18

<details>
<summary>Abstract</summary>

We present Espresso, an open-source, modular, extensible end-to-end neural automatic speech recognition (ASR) toolkit based on the deep learning library PyTorch and the popular neural machine translation toolkit fairseq. Espresso supports distributed training across GPUs and computing nodes, and features various decoding approaches commonly employed in ASR, including look-ahead word-based language model fusion, for which a fast, parallelized decoder is implemented. Espresso achieves state-of-the-art ASR performance on the WSJ, LibriSpeech, and Switchboard data sets among other end-to-end systems without data augmentation, and is 4--11x faster for decoding than similar systems (e.g. ESPnet).

</details>

### [Code-Switched Language Models Using Neural Based Synthetic Data from Parallel Sentences](1909.08582.md)
**Genta Indra Winata, Andrea Madotto, Chien-Sheng Wu, Pascale Fung** · 2019-09-18

<details>
<summary>Abstract</summary>

Training code-switched language models is difficult due to lack of data and complexity in the grammatical structure. Linguistic constraint theories have been used for decades to generate artificial code-switching sentences to cope with this issue. However, this require external word alignments or constituency parsers that create erroneous results on distant languages. We propose a sequence-to-sequence model using a copy mechanism to generate code-switching data by leveraging parallel monolingual translations from a limited source of code-switching data. The model learns how to combine words from parallel sentences and identifies when to switch one language to the other. Moreover, it captures code-switching constraints by attending and aligning the words in inputs, without requiring any external knowledge. Based on experimental results, the language model trained with the generated sentences achieves state-of-the-art performance and improves end-to-end automatic speech recognition.

</details>

### [An Investigation Into On-device Personalization of End-to-end Automatic Speech Recognition Models](1909.06678.md)
**Khe Chai Sim, Petr Zadrazil, Françoise Beaufays** · 2019-09-14

<details>
<summary>Abstract</summary>

Speaker-independent speech recognition systems trained with data from many users are generally robust against speaker variability and work well for a large population of speakers. However, these systems do not always generalize well for users with very different speech characteristics. This issue can be addressed by building personalized systems that are designed to work well for each specific user. In this paper, we investigate the idea of securely training personalized end-to-end speech recognition models on mobile devices so that user data and models never leave the device and are never stored on a server. We study how the mobile training environment impacts performance by simulating on-device data consumption. We conduct experiments using data collected from speech impaired users for personalization. Our results show that personalization achieved 63.7\% relative word error rate reduction when trained in a server environment and 58.1% in a mobile environment. Moving to on-device personalization resulted in 18.7% performance degradation, in exchange for improved scalability and data privacy. To train the model on device, we split the gradient computation into two and achieved 45% memory reduction at the expense of 42% increase in training time.

</details>

### [Integrating Source-channel and Attention-based Sequence-to-sequence Models for Speech Recognition](1909.06614.md)
**Qiujia Li, Chao Zhang, Philip C. Woodland** · 2019-09-14

<details>
<summary>Abstract</summary>

This paper proposes a novel automatic speech recognition (ASR) framework called Integrated Source-Channel and Attention (ISCA) that combines the advantages of traditional systems based on the noisy source-channel model (SC) and end-to-end style systems using attention-based sequence-to-sequence models. The traditional SC system framework includes hidden Markov models and connectionist temporal classification (CTC) based acoustic models, language models (LMs), and a decoding procedure based on a lexicon, whereas the end-to-end style attention-based system jointly models the whole process with a single model. By rescoring the hypotheses produced by traditional systems using end-to-end style systems based on an extended noisy source-channel model, ISCA allows structured knowledge to be easily incorporated via the SC-based model while exploiting the complementarity of the attention-based model. Experiments on the AMI meeting corpus show that ISCA is able to give a relative word error rate reduction up to 21% over an individual system, and by 13% over an alternative method which also involves combining CTC and attention-based models.

</details>

### [FfDL : A Flexible Multi-tenant Deep Learning Platform](1909.06526.md)
**K. R. Jayaram, Vinod Muthusamy, Parijat Dube, Vatche Ishakian et al.** · 2019-09-14

<details>
<summary>Abstract</summary>

Deep learning (DL) is becoming increasingly popular in several application domains and has made several new application features involving computer vision, speech recognition and synthesis, self-driving automobiles, drug design, etc. feasible and accurate. As a result, large scale on-premise and cloud-hosted deep learning platforms have become essential infrastructure in many organizations. These systems accept, schedule, manage and execute DL training jobs at scale. This paper describes the design, implementation and our experiences with FfDL, a DL platform used at IBM. We describe how our design balances dependability with scalability, elasticity, flexibility and efficiency. We examine FfDL qualitatively through a retrospective look at the lessons learned from building, operating, and supporting FfDL; and quantitatively through a detailed empirical evaluation of FfDL, including the overheads introduced by the platform for various deep learning models, the load and performance observed in a real case study using FfDL within our organization, the frequency of various faults observed including unanticipated faults, and experiments demonstrating the benefits of various scheduling policies. FfDL has been open-sourced.

</details>

### [NeMo: a toolkit for building AI applications using Neural Modules](1909.09577.md)
**Oleksii Kuchaiev, Jason Li, Huyen Nguyen, Oleksii Hrinchuk et al.** · 2019-09-14

<details>
<summary>Abstract</summary>

NeMo (Neural Modules) is a Python framework-agnostic toolkit for creating AI applications through re-usability, abstraction, and composition. NeMo is built around neural modules, conceptual blocks of neural networks that take typed inputs and produce typed outputs. Such modules typically represent data layers, encoders, decoders, language models, loss functions, or methods of combining activations. NeMo makes it easy to combine and re-use these building blocks while providing a level of semantic correctness checking via its neural type system. The toolkit comes with extendable collections of pre-built modules for automatic speech recognition and natural language processing. Furthermore, NeMo provides built-in support for distributed training and mixed precision on latest NVIDIA GPUs. NeMo is open-source https://github.com/NVIDIA/NeMo

</details>

### [Harnessing Indirect Training Data for End-to-End Automatic Speech Translation: Tricks of the Trade](1909.06515.md)
**Juan Pino, Liezl Puzon, Jiatao Gu, Xutai Ma et al.** · 2019-09-14

<details>
<summary>Abstract</summary>

For automatic speech translation (AST), end-to-end approaches are outperformed by cascaded models that transcribe with automatic speech recognition (ASR), then translate with machine translation (MT). A major cause of the performance gap is that, while existing AST corpora are small, massive datasets exist for both the ASR and MT subsystems. In this work, we evaluate several data augmentation and pretraining approaches for AST, by comparing all on the same datasets. Simple data augmentation by translating ASR transcripts proves most effective on the English--French augmented LibriSpeech dataset, closing the performance gap from 8.2 to 1.4 BLEU, compared to a very strong cascade that could directly utilize copious ASR and MT data. The same end-to-end approach plus fine-tuning closes the gap on the English--Romanian MuST-C dataset from 6.7 to 3.7 BLEU. In addition to these results, we present practical recommendations for augmentation and pretraining approaches. Finally, we decrease the performance gap to 0.01 BLEU using a Transformer-based architecture.

</details>

### [A Comparative Study on Transformer vs RNN in Speech Applications](1909.06317.md)
**Shigeki Karita, Nanxin Chen, Tomoki Hayashi, Takaaki Hori et al.** · 2019-09-13

<details>
<summary>Abstract</summary>

Sequence-to-sequence models have been widely used in end-to-end speech processing, for example, automatic speech recognition (ASR), speech translation (ST), and text-to-speech (TTS). This paper focuses on an emergent sequence-to-sequence model called Transformer, which achieves state-of-the-art performance in neural machine translation and other natural language processing applications. We undertook intensive studies in which we experimentally compared and analyzed Transformer and conventional recurrent neural networks (RNN) in a total of 15 ASR, one multilingual ASR, one ST, and two TTS benchmarks. Our experiments revealed various training tips and significant performance benefits obtained with Transformer for each task including the surprising superiority of Transformer in 13/15 ASR benchmarks in comparison with RNN. We are preparing to release Kaldi-style reproducible recipes using open source and publicly available datasets for all the ASR, ST, and TTS tasks for the community to succeed our exciting outcomes.

</details>

### [Recognition of Handwritten Digit using Convolutional Neural Network in Python with Tensorflow and Comparison of Performance for Various Hidden Layers](1909.08490.md)
**Fathma Siddique, Shadman Sakib, Md. Abu Bakr Siddique** · 2019-09-12

<details>
<summary>Abstract</summary>

In recent times, with the increase of Artificial Neural Network (ANN), deep learning has brought a dramatic twist in the field of machine learning by making it more artificially intelligent. Deep learning is remarkably used in vast ranges of fields because of its diverse range of applications such as surveillance, health, medicine, sports, robotics, drones, etc. In deep learning, Convolutional Neural Network (CNN) is at the center of spectacular advances that mixes Artificial Neural Network (ANN) and up to date deep learning strategies. It has been used broadly in pattern recognition, sentence classification, speech recognition, face recognition, text categorization, document analysis, scene, and handwritten digit recognition. The goal of this paper is to observe the variation of accuracies of CNN to classify handwritten digits using various numbers of hidden layers and epochs and to make the comparison between the accuracies. For this performance evaluation of CNN, we performed our experiment using Modified National Institute of Standards and Technology (MNIST) dataset. Further, the network is trained using stochastic gradient descent and the backpropagation algorithm.

</details>

### [Large-Scale Multilingual Speech Recognition with a Streaming End-to-End Model](1909.05330.md)
**Anjuli Kannan, Arindrima Datta, Tara N. Sainath, Eugene Weinstein et al.** · 2019-09-11

<details>
<summary>Abstract</summary>

Multilingual end-to-end (E2E) models have shown great promise in expansion of automatic speech recognition (ASR) coverage of the world's languages. They have shown improvement over monolingual systems, and have simplified training and serving by eliminating language-specific acoustic, pronunciation, and language models. This work presents an E2E multilingual system which is equipped to operate in low-latency interactive applications, as well as handle a key challenge of real world data: the imbalance in training data across languages. Using nine Indic languages, we compare a variety of techniques, and find that a combination of conditioning on a language vector and training language-specific adapter layers produces the best model. The resulting E2E multilingual model achieves a lower word error rate (WER) than both monolingual E2E models (eight of nine languages) and monolingual conventional systems (all nine languages).

</details>

### [QuTiBench: Benchmarking Neural Networks on Heterogeneous Hardware](1909.05009.md)
**Michaela Blott, Lisa Halder, Miriam Leeser, Linda Doyle** · 2019-09-11

<details>
<summary>Abstract</summary>

Neural Networks have become one of the most successful universal machine learning algorithms. They play a key role in enabling machine vision and speech recognition for example. Their computational complexity is enormous and comes along with equally challenging memory requirements, which limits deployment in particular within energy constrained, embedded environments. In order to address these implementation challenges, a broad spectrum of new customized and heterogeneous hardware architectures have emerged, often accompanied with co-designed algorithms to extract maximum benefit out of the hardware. Furthermore, numerous optimization techniques are being explored for neural networks to reduce compute and memory requirements while maintaining accuracy. This results in an abundance of algorithmic and architectural choices, some of which fit specific use cases better than others. For system level designers, there is currently no good way to compare the variety of hardware, algorithm and optimization options. While there are many benchmarking efforts in this field, they cover only subsections of the embedded design space. None of the existing benchmarks support essential algorithmic optimizations such as quantization, an important technique to stay on chip, or specialized heterogeneous hardware architectures. We propose a novel benchmark suite, QuTiBench, that addresses this need. QuTiBench is a novel multi-tiered benchmarking methodology that supports algorithmic optimizations such as quantization and helps system developers understand the benefits and limitations of these novel compute architectures in regard to specific neural networks and will help drive future innovation. We invite the community to contribute to QuTiBench in order to support the full spectrum of choices in implementing machine learning systems.

</details>

### [Preech: A System for Privacy-Preserving Speech Transcription](1909.04198.md)
**Shimaa Ahmed, Amrita Roy Chowdhury, Kassem Fawaz, Parmesh Ramanathan** · 2019-09-09

<details>
<summary>Abstract</summary>

New Advances in machine learning have made Automated Speech Recognition (ASR) systems practical and more scalable. These systems, however, pose serious privacy threats as speech is a rich source of sensitive acoustic and textual information. Although offline and open-source ASR eliminates the privacy risks, its transcription performance is inferior to that of cloud-based ASR systems, especially for real-world use cases. In this paper, we propose Pr$εε$ch, an end-to-end speech transcription system which lies at an intermediate point in the privacy-utility spectrum. It protects the acoustic features of the speakers' voices and protects the privacy of the textual content at an improved performance relative to offline ASR. Additionally, Pr$εε$ch provides several control knobs to allow customizable utility-usability-privacy trade-off. It relies on cloud-based services to transcribe a speech file after applying a series of privacy-preserving operations on the user's side. We perform a comprehensive evaluation of Pr$εε$ch, using diverse real-world datasets, that demonstrates its effectiveness. Pr$εε$ch provides transcriptions at a 2% to 32.25% (mean 17.34%) relative improvement in word error rate over Deep Speech, while fully obfuscating the speakers' voice biometrics and allowing only a differentially private view of the textual content.

</details>

### [Self-Teaching Networks](1909.04157.md)
**Liang Lu, Eric Sun, Yifan Gong** · 2019-09-09

<details>
<summary>Abstract</summary>

We propose self-teaching networks to improve the generalization capacity of deep neural networks. The idea is to generate soft supervision labels using the output layer for training the lower layers of the network. During the network training, we seek an auxiliary loss that drives the lower layer to mimic the behavior of the output layer. The connection between the two network layers through the auxiliary loss can help the gradient flow, which works similar to the residual networks. Furthermore, the auxiliary loss also works as a regularizer, which improves the generalization capacity of the network. We evaluated the self-teaching network with deep recurrent neural networks on speech recognition tasks, where we trained the acoustic model using 30 thousand hours of data. We tested the acoustic model using data collected from 4 scenarios. We show that the self-teaching network can achieve consistent improvements and outperform existing methods such as label smoothing and confidence penalization.

</details>

### [Question Generation by Transformers](1909.05017.md)
**Kettip Kriangchaivech, Artit Wangperawong** · 2019-09-09

<details>
<summary>Abstract</summary>

A machine learning model was developed to automatically generate questions from Wikipedia passages using transformers, an attention-based model eschewing the paradigm of existing recurrent neural networks (RNNs). The model was trained on the inverted Stanford Question Answering Dataset (SQuAD), which is a reading comprehension dataset consisting of 100,000+ questions posed by crowdworkers on a set of Wikipedia articles. After training, the question generation model is able to generate simple questions relevant to unseen passages and answers containing an average of 8 words per question. The word error rate (WER) was used as a metric to compare the similarity between SQuAD questions and the model-generated questions. Although the high average WER suggests that the questions generated differ from the original SQuAD questions, the questions generated are mostly grammatically correct and plausible in their own right.

</details>

### [Neural Network-Based Modeling of Phonetic Durations](1909.03030.md)
**Xizi Wei, Melvyn Hunt, Adrian Skilling** · 2019-09-06

<details>
<summary>Abstract</summary>

A deep neural network (DNN)-based model has been developed to predict non-parametric distributions of durations of phonemes in specified phonetic contexts and used to explore which factors influence durations most. Major factors in US English are pre-pausal lengthening, lexical stress, and speaking rate. The model can be used to check that text-to-speech (TTS) training speech follows the script and words are pronounced as expected. Duration prediction is poorer with training speech for automatic speech recognition (ASR) because the training corpus typically consists of single utterances from many speakers and is often noisy or casually spoken. Low probability durations in ASR training material nevertheless mostly correspond to non-standard speech, with some having disfluencies. Children's speech is disproportionately present in these utterances, since children show much more variation in timing.

</details>

### [Bandwidth Embeddings for Mixed-bandwidth Speech Recognition](1909.02667.md)
**Gautam Mantena, Ozlem Kalinli, Ossama Abdel-Hamid, Don McAllaster** · 2019-09-05

<details>
<summary>Abstract</summary>

In this paper, we tackle the problem of handling narrowband and wideband speech by building a single acoustic model (AM), also called mixed bandwidth AM. In the proposed approach, an auxiliary input feature is used to provide the bandwidth information to the model, and bandwidth embeddings are jointly learned as part of acoustic model training. Experimental evaluations show that using bandwidth embeddings helps the model to handle the variability of the narrow and wideband speech, and makes it possible to train a mixed-bandwidth AM. Furthermore, we propose to use parallel convolutional layers to handle the mismatch between the narrow and wideband speech better, where separate convolution layers are used for each type of input speech signal. Our best system achieves 13% relative improvement on narrowband speech, while not degrading on wideband speech.

</details>

### [An efficient and perceptually motivated auditory neural encoding and decoding algorithm for spiking neural networks](1909.01302.md)
**Zihan Pan, Yansong Chua, Jibin Wu, Malu Zhang et al.** · 2019-09-03

<details>
<summary>Abstract</summary>

Auditory front-end is an integral part of a spiking neural network (SNN) when performing auditory cognitive tasks. It encodes the temporal dynamic stimulus, such as speech and audio, into an efficient, effective and reconstructable spike pattern to facilitate the subsequent processing. However, most of the auditory front-ends in current studies have not made use of recent findings in psychoacoustics and physiology concerning human listening. In this paper, we propose a neural encoding and decoding scheme that is optimized for speech processing. The neural encoding scheme, that we call Biologically plausible Auditory Encoding (BAE), emulates the functions of the perceptual components of the human auditory system, that include the cochlear filter bank, the inner hair cells, auditory masking effects from psychoacoustic models, and the spike neural encoding by the auditory nerve. We evaluate the perceptual quality of the BAE scheme using PESQ; the performance of the BAE based on speech recognition experiments. Finally, we also built and published two spike-version of speech datasets: the Spike-TIDIGITS and the Spike-TIMIT, for researchers to use and benchmarking of future SNN research.

</details>

### [Automatic Speech Recognition Services: Deaf and Hard-of-Hearing Usability](1909.02853.md)
**Abraham Glasser** · 2019-09-03

<details>
<summary>Abstract</summary>

Nowadays, speech is becoming a more common, if not standard, interface to technology. This can be seen in the trend of technology changes over the years. Increasingly, voice is used to control programs, appliances and personal devices within homes, cars, workplaces, and public spaces through smartphones and home assistant devices using Amazon's Alexa, Google's Assistant and Apple's Siri, and other proliferating technologies. However, most speech interfaces are not accessible for Deaf and Hard-of-Hearing (DHH) people. In this paper, performances of current Automatic Speech Recognition (ASR) with voices of DHH speakers are evaluated. ASR has improved over the years, and is able to reach Word Error Rates (WER) as low as 5-6% [1][2][3], with the help of cloud-computing and machine learning algorithms that take in custom vocabulary models. In this paper, a custom vocabulary model is used, and the significance of the improvement is evaluated when using DHH speech.

</details>

### [Avaya Conversational Intelligence: A Real-Time System for Spoken Language Understanding in Human-Human Call Center Conversations](1909.02851.md)
**Jan Mizgajski, Adrian Szymczak, Robert Głowski, Piotr Szymański et al.** · 2019-09-02

<details>
<summary>Abstract</summary>

Avaya Conversational Intelligence(ACI) is an end-to-end, cloud-based solution for real-time Spoken Language Understanding for call centers. It combines large vocabulary, real-time speech recognition, transcript refinement, and entity and intent recognition in order to convert live audio into a rich, actionable stream of structured events. These events can be further leveraged with a business rules engine, thus serving as a foundation for real-time supervision and assistance applications. After the ingestion, calls are enriched with unsupervised keyword extraction, abstractive summarization, and business-defined attributes, enabling offline use cases, such as business intelligence, topic mining, full-text search, quality assurance, and agent training. ACI comes with a pretrained, configurable library of hundreds of intents and a robust intent training environment that allows for efficient, cost-effective creation and customization of customer-specific intents.

</details>

### [EBPC: Extended Bit-Plane Compression for Deep Neural Network Inference and Training Accelerators](1908.11645.md)
**Lukas Cavigelli, Georg Rutishauser, Luca Benini** · 2019-08-30

<details>
<summary>Abstract</summary>

In the wake of the success of convolutional neural networks in image classification, object recognition, speech recognition, etc., the demand for deploying these compute-intensive ML models on embedded and mobile systems with tight power and energy constraints at low cost, as well as for boosting throughput in data centers, is growing rapidly. This has sparked a surge of research into specialized hardware accelerators. Their performance is typically limited by I/O bandwidth, power consumption is dominated by I/O transfers to off-chip memory, and on-chip memories occupy a large part of the silicon area. We introduce and evaluate a novel, hardware-friendly, and lossless compression scheme for the feature maps present within convolutional neural networks. We present hardware architectures and synthesis results for the compressor and decompressor in 65nm. With a throughput of one 8-bit word/cycle at 600MHz, they fit into 2.8kGE and 3.0kGE of silicon area, respectively - together the size of less than seven 8-bit multiply-add units at the same throughput. We show that an average compression ratio of 5.1x for AlexNet, 4x for VGG-16, 2.4x for ResNet-34 and 2.2x for MobileNetV2 can be achieved - a gain of 45-70% over existing methods. Our approach also works effectively for various number formats, has a low frame-to-frame variance on the compression ratio, and achieves compression factors for gradient map compression during training that are even better than for inference.

</details>

### [Fraudulent White Noise: Flat power spectra belie arbitrarily complex processes](1908.11405.md)
**P. M. Riechers, J. P. Crutchfield** · 2019-08-29

<details>
<summary>Abstract</summary>

Power spectral densities are a common, convenient, and powerful way to analyze signals. So much so that they are now broadly deployed across the sciences and engineering---from quantum physics to cosmology, and from crystallography to neuroscience to speech recognition. The features they reveal not only identify prominent signal-frequencies but also hint at mechanisms that generate correlation and lead to resonance. Despite their near-centuries-long run of successes in signal analysis, here we show that flat power spectra can be generated by highly complex processes, effectively hiding all inherent structure in complex signals. Historically, this circumstance has been widely misinterpreted, being taken as the renowned signature of "structureless" white noise---the benchmark of randomness. We argue, in contrast, to the extent that most real-world complex systems exhibit correlations beyond pairwise statistics their structures evade power spectra and other pairwise statistical measures. As concrete physical examples, we demonstrate that fraudulent white noise hides the predictable structure of both entangled quantum systems and chaotic crystals. To make these words of warning operational, we present constructive results that explore how this situation comes about and the high toll it takes in understanding complex mechanisms. First, we give the closed-form solution for the power spectrum of a very broad class of structurally-complex signal generators. Second, we demonstrate the close relationship between eigen-spectra of evolution operators and power spectra. Third, we characterize the minimal generative structure implied by any power spectrum. Fourth, we show how to construct arbitrarily complex processes with flat power spectra. Finally, leveraging this diagnosis of the problem, we point the way to developing more incisive tools for discovering structure in complex signals.

</details>

### [Estimation of a function of low local dimensionality by deep neural networks](1908.11140.md)
**Michael Kohler, Adam Krzyzak, Sophie Langer** · 2019-08-29

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) achieve impressive results for complicated tasks like object detection on images and speech recognition. Motivated by this practical success, there is now a strong interest in showing good theoretical properties of DNNs. To describe for which tasks DNNs perform well and when they fail, it is a key challenge to understand their performance. The aim of this paper is to contribute to the current statistical theory of DNNs. We apply DNNs on high dimensional data and we show that the least squares regression estimates using DNNs are able to achieve dimensionality reduction in case that the regression function has locally low dimensionality. Consequently, the rate of convergence of the estimate does not depend on its input dimension $d$, but on its local dimension $d^*$ and the DNNs are able to circumvent the curse of dimensionality in case that $d^*$ is much smaller than $d$. In our simulation study we provide numerical experiments to support our theoretical result and we compare our estimate with other conventional nonparametric regression estimates. The performance of our estimates is also validated in experiments with real data.

</details>

### [Two-Pass End-to-End Speech Recognition](1908.10992.md)
**Tara N. Sainath, Ruoming Pang, David Rybach, Yanzhang He et al.** · 2019-08-29

<details>
<summary>Abstract</summary>

The requirements for many applications of state-of-the-art speech recognition systems include not only low word error rate (WER) but also low latency. Specifically, for many use-cases, the system must be able to decode utterances in a streaming fashion and faster than real-time. Recently, a streaming recurrent neural network transducer (RNN-T) end-to-end (E2E) model has shown to be a good candidate for on-device speech recognition, with improved WER and latency metrics compared to conventional on-device models [1]. However, this model still lags behind a large state-of-the-art conventional model in quality [2]. On the other hand, a non-streaming E2E Listen, Attend and Spell (LAS) model has shown comparable quality to large conventional models [3]. This work aims to bring the quality of an E2E streaming model closer to that of a conventional system by incorporating a LAS network as a second-pass component, while still abiding by latency constraints. Our proposed two-pass model achieves a 17%-22% relative reduction in WER compared to RNN-T alone and increases latency by a small fraction over RNN-T.

</details>

### [MASR: A Modular Accelerator for Sparse RNNs](1908.08976.md)
**Udit Gupta, Brandon Reagen, Lillian Pentecost, Marco Donato et al.** · 2019-08-23

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) are becoming the de facto solution for speech recognition. RNNs exploit long-term temporal relationships in data by applying repeated, learned transformations. Unlike fully-connected (FC) layers with single vector matrix operations, RNN layers consist of hundreds of such operations chained over time. This poses challenges unique to RNNs that are not found in convolutional neural networks (CNNs) or FC models, namely large dynamic activation. In this paper we present MASR, a principled and modular architecture that accelerates bidirectional RNNs for on-chip ASR. MASR is designed to exploit sparsity in both dynamic activations and static weights. The architecture is enhanced by a series of dynamic activation optimizations that enable compact storage, ensure no energy is wasted computing null operations, and maintain high MAC utilization for highly parallel accelerator designs. In comparison to current state-of-the-art sparse neural network accelerators (e.g., EIE), MASR provides 2x area 3x energy, and 1.6x performance benefits. The modular nature of MASR enables designs that efficiently scale from resource-constrained low-power IoT applications to large-scale, highly parallel datacenter deployments.

</details>

### [Deploying Technology to Save Endangered Languages](1908.08971.md)
**Hilaria Cruz, Joseph Waring** · 2019-08-23

<details>
<summary>Abstract</summary>

Computer scientists working on natural language processing, native speakers of endangered languages, and field linguists to discuss ways to harness Automatic Speech Recognition, especially neural networks, to automate annotation, speech tagging, and text parsing on endangered languages.

</details>

### [Self-reinforcing Unsupervised Matching](1909.04138.md)
**Jiang Lu, Lei Li, Changshui Zhang** · 2019-08-23

<details>
<summary>Abstract</summary>

Remarkable gains in deep learning usually rely on tremendous supervised data. Ensuring the modality diversity for one object in training set is critical for the generalization of cutting-edge deep models, but it burdens human with heavy manual labor on data collection and annotation. In addition, some rare or unexpected modalities are new for the current model, causing reduced performance under such emerging modalities. Inspired by the achievements in speech recognition, psychology and behavioristics, we present a practical solution, self-reinforcing unsupervised matching (SUM), to annotate the images with 2D structure-preserving property in an emerging modality by cross-modality matching. This approach requires no any supervision in emerging modality and only one template in seen modality, providing a possible route towards continual learning.

</details>

### [Adabot: Fault-Tolerant Java Decompiler](1908.06748.md)
**Zhiming Li, Qing Wu, Kun Qian** · 2019-08-14

<details>
<summary>Abstract</summary>

Reverse Engineering(RE) has been a fundamental task in software engineering. However, most of the traditional Java reverse engineering tools are strictly rule defined, thus are not fault-tolerant, which pose serious problem when noise and interference were introduced into the system. In this paper, we view reverse engineering as a statistical machine translation task instead of rule-based task, and propose a fault-tolerant Java decompiler based on machine translation models. Our model is based on attention-based Neural Machine Translation (NMT) and Transformer architectures. First, we measure the translation quality on both the redundant and purified datasets. Next, we evaluate the fault-tolerance(anti-noise ability) of our framework on test sets with different unit error probability (UEP). In addition, we compare the suitability of different word segmentation algorithms for decompilation task. Experimental results demonstrate that our model is more robust and fault-tolerant compared to traditional Abstract Syntax Tree (AST) based decompilers. Specifically, in terms of BLEU-4 and Word Error Rate (WER), our performance has reached 94.50% and 2.65% on the redundant test set; 92.30% and 3.48% on the purified test set.

</details>

### [End-to-End Multi-Speaker Speech Recognition using Speaker Embeddings and Transfer Learning](1908.04737.md)
**Pavel Denisov, Ngoc Thang Vu** · 2019-08-13

<details>
<summary>Abstract</summary>

This paper presents our latest investigation on end-to-end automatic speech recognition (ASR) for overlapped speech. We propose to train an end-to-end system conditioned on speaker embeddings and further improved by transfer learning from clean speech. This proposed framework does not require any parallel non-overlapped speech materials and is independent of the number of speakers. Our experimental results on overlapped speech datasets show that joint conditioning on speaker embeddings and transfer learning significantly improves the ASR performance.

</details>

### [Space-time error estimates for deep neural network approximations for differential equations](1908.03833.md)
**Philipp Grohs, Fabian Hornung, Arnulf Jentzen, Philipp Zimmermann** · 2019-08-11

<details>
<summary>Abstract</summary>

Over the last few years deep artificial neural networks (DNNs) have very successfully been used in numerical simulations for a wide variety of computational problems including computer vision, image classification, speech recognition, natural language processing, as well as computational advertisement. In addition, it has recently been proposed to approximate solutions of partial differential equations (PDEs) by means of stochastic learning problems involving DNNs. There are now also a few rigorous mathematical results in the scientific literature which provide error estimates for such deep learning based approximation methods for PDEs. All of these articles provide spatial error estimates for neural network approximations for PDEs but do not provide error estimates for the entire space-time error for the considered neural network approximations. It is the subject of the main result of this article to provide space-time error estimates for DNN approximations of Euler approximations of certain perturbed differential equations. Our proof of this result is based (i) on a certain artificial neural network (ANN) calculus and (ii) on ANN approximation results for products of the form $[0,T]\times \mathbb{R}^d\ni (t,x)\mapsto tx\in \mathbb{R}^d$ where $T\in (0,\infty)$, $d\in \mathbb{N}$, which we both develop within this article.

</details>

### [Unsupervised Stemming based Language Model for Telugu Broadcast News Transcription](1908.03734.md)
**Mythili Sharan Pala, Parayitam Laxminarayana, A. V. Ramana** · 2019-08-10

<details>
<summary>Abstract</summary>

In Indian Languages , native speakers are able to understand new words formed by either combining or modifying root words with tense and / or gender. Due to data insufficiency, Automatic Speech Recognition system (ASR) may not accommodate all the words in the language model irrespective of the size of the text corpus. It also becomes computationally challenging if the volume of the data increases exponentially due to morphological changes to the root word. In this paper a new unsupervised method is proposed for a Indian language: Telugu, based on the unsupervised method for Hindi, to generate the Out of Vocabulary (OOV) words in the language model. By using techniques like smoothing and interpolation of pre-processed data with supervised and unsupervised stemming, different issues in language model for Indian language: Telugu has been addressed. We observe that the smoothing techniques Witten-Bell and Kneser-Ney perform well when compared to other techniques on pre-processed data from supervised learning. The ASRs accuracy is improved by 0.76% and 0.94% with supervised and unsupervised stemming respectively.

</details>

### [Exploiting Cross-Lingual Speaker and Phonetic Diversity for Unsupervised Subword Modeling](1908.03538.md)
**Siyuan Feng, Tan Lee** · 2019-08-09

<details>
<summary>Abstract</summary>

This research addresses the problem of acoustic modeling of low-resource languages for which transcribed training data is absent. The goal is to learn robust frame-level feature representations that can be used to identify and distinguish subword-level speech units. The proposed feature representations comprise various types of multilingual bottleneck features (BNFs) that are obtained via multi-task learning of deep neural networks (MTL-DNN). One of the key problems is how to acquire high-quality frame labels for untranscribed training data to facilitate supervised DNN training. It is shown that learning of robust BNF representations can be achieved by effectively leveraging transcribed speech data and well-trained automatic speech recognition (ASR) systems from one or more out-of-domain (resource-rich) languages. Out-of-domain ASR systems can be applied to perform speaker adaptation with untranscribed training data of the target language, and to decode the training speech into frame-level labels for DNN training. It is also found that better frame labels can be generated by considering temporal dependency in speech when performing frame clustering. The proposed methods of feature learning are evaluated on the standard task of unsupervised subword modeling in Track 1 of the ZeroSpeech 2017 Challenge. The best performance achieved by our system is $9.7\%$ in terms of across-speaker triphone minimal-pair ABX error rate, which is comparable to the best systems reported recently. Lastly, our investigation reveals that the closeness between target languages and out-of-domain languages and the amount of available training data for individual target languages could have significant impact on the goodness of learned features.

</details>

### [Challenging the Boundaries of Speech Recognition: The MALACH Corpus](1908.03455.md)
**Michael Picheny, Zóltan Tüske, Brian Kingsbury, Kartik Audhkhasi et al.** · 2019-08-09

<details>
<summary>Abstract</summary>

There has been huge progress in speech recognition over the last several years. Tasks once thought extremely difficult, such as SWITCHBOARD, now approach levels of human performance. The MALACH corpus (LDC catalog LDC2012S05), a 375-Hour subset of a large archive of Holocaust testimonies collected by the Survivors of the Shoah Visual History Foundation, presents significant challenges to the speech community. The collection consists of unconstrained, natural speech filled with disfluencies, heavy accents, age-related coarticulations, un-cued speaker and language switching, and emotional speech - all still open problems for speech recognition systems. Transcription is challenging even for skilled human annotators. This paper proposes that the community place focus on the MALACH corpus to develop speech recognition systems that are more robust with respect to accents, disfluencies and emotional speech. To reduce the barrier for entry, a lexicon and training and testing setups have been created and baseline results using current deep learning technologies are presented. The metadata has just been released by LDC (LDC2019S11). It is hoped that this resource will enable the community to build on top of these baselines so that the extremely important information in these and related oral histories becomes accessible to a wider audience.

</details>

### [Exploiting semi-supervised training through a dropout regularization in end-to-end speech recognition](1908.05227.md)
**Subhadeep Dey, Petr Motlicek, Trung Bui, Franck Dernoncourt** · 2019-08-08

<details>
<summary>Abstract</summary>

In this paper, we explore various approaches for semi supervised learning in an end to end automatic speech recognition (ASR) framework. The first step in our approach involves training a seed model on the limited amount of labelled data. Additional unlabelled speech data is employed through a data selection mechanism to obtain the best hypothesized output, further used to retrain the seed model. However, uncertainties of the model may not be well captured with a single hypothesis. As opposed to this technique, we apply a dropout mechanism to capture the uncertainty by obtaining multiple hypothesized text transcripts of an speech recording. We assume that the diversity of automatically generated transcripts for an utterance will implicitly increase the reliability of the model. Finally, the data selection process is also applied on these hypothesized transcripts to reduce the uncertainty. Experiments on freely available TEDLIUM corpus and proprietary Adobe's internal dataset show that the proposed approach significantly reduces ASR errors, compared to the baseline model.

</details>

### [Mitigating Noisy Inputs for Question Answering](1908.02914.md)
**Denis Peskov, Joe Barrow, Pedro Rodriguez, Graham Neubig et al.** · 2019-08-08

<details>
<summary>Abstract</summary>

Natural language processing systems are often downstream of unreliable inputs: machine translation, optical character recognition, or speech recognition. For instance, virtual assistants can only answer your questions after understanding your speech. We investigate and mitigate the effects of noise from Automatic Speech Recognition systems on two factoid Question Answering (QA) tasks. Integrating confidences into the model and forced decoding of unknown words are empirically shown to improve the accuracy of downstream neural QA systems. We create and train models on a synthetic corpus of over 500,000 noisy sentences and evaluate on two human corpora from Quizbowl and Jeopardy! competitions.

</details>

### [Fast and Accurate Capitalization and Punctuation for Automatic Speech Recognition Using Transformer and Chunk Merging](1908.02404.md)
**Binh Nguyen, Vu Bao Hung Nguyen, Hien Nguyen, Pham Ngoc Phuong et al.** · 2019-08-07

<details>
<summary>Abstract</summary>

In recent years, studies on automatic speech recognition (ASR) have shown outstanding results that reach human parity on short speech segments. However, there are still difficulties in standardizing the output of ASR such as capitalization and punctuation restoration for long-speech transcription. The problems obstruct readers to understand the ASR output semantically and also cause difficulties for natural language processing models such as NER, POS and semantic parsing. In this paper, we propose a method to restore the punctuation and capitalization for long-speech ASR transcription. The method is based on Transformer models and chunk merging that allows us to (1), build a single model that performs punctuation and capitalization in one go, and (2), perform decoding in parallel while improving the prediction accuracy. Experiments on British National Corpus showed that the proposed approach outperforms existing methods in both accuracy and decoding speed.

</details>

### [Random Directional Attack for Fooling Deep Neural Networks](1908.02658.md)
**Wenjian Luo, Chenwang Wu, Nan Zhou, Li Ni** · 2019-08-06

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been widely used in many fields such as images processing, speech recognition; however, they are vulnerable to adversarial examples, and this is a security issue worthy of attention. Because the training process of DNNs converge the loss by updating the weights along the gradient descent direction, many gradient-based methods attempt to destroy the DNN model by adding perturbations in the gradient direction. Unfortunately, as the model is nonlinear in most cases, the addition of perturbations in the gradient direction does not necessarily increase loss. Thus, we propose a random directed attack (RDA) for generating adversarial examples in this paper. Rather than limiting the gradient direction to generate an attack, RDA searches the attack direction based on hill climbing and uses multiple strategies to avoid local optima that cause attack failure. Compared with state-of-the-art gradient-based methods, the attack performance of RDA is very competitive. Moreover, RDA can attack without any internal knowledge of the model, and its performance under black-box attack is similar to that of the white-box attack in most cases, which is difficult to achieve using existing gradient-based attack methods.

</details>

### [SANTLR: Speech Annotation Toolkit for Low Resource Languages](1908.01067.md)
**Xinjian Li, Zhong Zhou, Siddharth Dalmia, Alan W. Black et al.** · 2019-08-02

<details>
<summary>Abstract</summary>

While low resource speech recognition has attracted a lot of attention from the speech community, there are a few tools available to facilitate low resource speech collection. In this work, we present SANTLR: Speech Annotation Toolkit for Low Resource Languages. It is a web-based toolkit which allows researchers to easily collect and annotate a corpus of speech in a low resource language. Annotators may use this toolkit for two purposes: transcription or recording. In transcription, annotators would transcribe audio files provided by the researchers; in recording, annotators would record their voice by reading provided texts. We highlight two properties of this toolkit. First, SANTLR has a very user-friendly User Interface (UI). Both researchers and annotators may use this simple web interface to interact. There is no requirement for the annotators to have any expertise in audio or text processing. The toolkit would handle all preprocessing and postprocessing steps. Second, we employ a multi-step ranking mechanism facilitate the annotation process. In particular, the toolkit would give higher priority to utterances which are easier to annotate and are more beneficial to achieving the goal of the annotation, e.g. quickly training an acoustic model.

</details>

### [Learning Joint Acoustic-Phonetic Word Embeddings](1908.00493.md)
**Mohamed El-Geish** · 2019-08-01

<details>
<summary>Abstract</summary>

Most speech recognition tasks pertain to mapping words across two modalities: acoustic and orthographic. In this work, we suggest learning encoders that map variable-length, acoustic or phonetic, sequences that represent words into fixed-dimensional vectors in a shared latent space; such that the distance between two word vectors represents how closely the two words sound. Instead of directly learning the distances between word vectors, we employ weak supervision and model a binary classification task to predict whether two inputs, one of each modality, represent the same word given a distance threshold. We explore various deep-learning models, bimodal contrastive losses, and techniques for mining hard negative examples such as the semi-supervised technique of self-labeling. Our best model achieves an $F_1$ score of 0.95 for the binary classification task.

</details>

### [DuTongChuan: Context-aware Translation Model for Simultaneous Interpreting](1907.12984.md)
**Hao Xiong, Ruiqing Zhang, Chuanqiang Zhang, Zhongjun He et al.** · 2019-07-30

<details>
<summary>Abstract</summary>

In this paper, we present DuTongChuan, a novel context-aware translation model for simultaneous interpreting. This model allows to constantly read streaming text from the Automatic Speech Recognition (ASR) model and simultaneously determine the boundaries of Information Units (IUs) one after another. The detected IU is then translated into a fluent translation with two simple yet effective decoding strategies: partial decoding and context-aware decoding. In practice, by controlling the granularity of IUs and the size of the context, we can get a good trade-off between latency and translation quality easily. Elaborate evaluation from human translators reveals that our system achieves promising translation quality (85.71% for Chinese-English, and 86.36% for English-Chinese), specially in the sense of surprisingly good discourse coherence. According to an End-to-End (speech-to-speech simultaneous interpreting) evaluation, this model presents impressive performance in reducing latency (to less than 3 seconds at most times). Furthermore, we successfully deploy this model in a variety of Baidu's products which have hundreds of millions of users, and we release it as a service in our AI platform.

</details>

### [Multi-Frame Cross-Entropy Training for Convolutional Neural Networks in Speech Recognition](1907.13121.md)
**Tom Sercu, Neil Mallinar** · 2019-07-29

<details>
<summary>Abstract</summary>

We introduce Multi-Frame Cross-Entropy training (MFCE) for convolutional neural network acoustic models. Recognizing that similar to RNNs, CNNs are in nature sequence models that take variable length inputs, we propose to take as input to the CNN a part of an utterance long enough that multiple labels are predicted at once, therefore getting cross-entropy loss signal from multiple adjacent frames. This increases the amount of label information drastically for small marginal computational cost. We show large WER improvements on hub5 and rt02 after training on the 2000-hour Switchboard benchmark.

</details>

### [Correlation Distance Skip Connection Denoising Autoencoder (CDSK-DAE) for Speech Feature Enhancement](1907.11361.md)
**Alzahra Badi, Sangwook Park, David K. Han, Hanseok Ko** · 2019-07-26

<details>
<summary>Abstract</summary>

Performance of learning based Automatic Speech Recognition (ASR) is susceptible to noise, especially when it is introduced in the testing data while not presented in the training data. This work focuses on a feature enhancement for noise robust end-to-end ASR system by introducing a novel variant of denoising autoencoder (DAE). The proposed method uses skip connections in both encoder and decoder sides by passing speech information of the target frame from input to the model. It also uses a new objective function in training model that uses a correlation distance measure in penalty terms by measuring dependency of the latent target features and the model (latent features and enhanced features obtained from the DAE). Performance of the proposed method was compared against a conventional model and a state of the art model under both seen and unseen noisy environments of 7 different types of background noise with different SNR levels (0, 5, 10 and 20 dB). The proposed method also is tested using linear and non-linear penalty terms as well, where, they both show an improvement on the overall average WER under noisy conditions both seen and unseen in comparison to the state-of-the-art model.

</details>

### [A comparison of Deep Learning performances with other machine learning algorithms on credit scoring unbalanced data](1907.12363.md)
**Louis Marceau, Lingling Qiu, Nick Vandewiele, Eric Charton** · 2019-07-25

<details>
<summary>Abstract</summary>

Training models on highly unbalanced data is admitted to be a challenging task for machine learning algorithms. Current studies on deep learning mainly focus on data sets with balanced class labels or unbalanced data, but with massive amount of samples available, like in speech recognition. However, the capacities of deep learning on imbalanced data with little samples is not deeply investigated in literature, while it is a very common application context in numerous industries. To contribute to fill this gap, this paper compares the performances of several popular machine learning algorithms previously applied with success to unbalanced data set with deep learning algorithms. We conduct those experiments on a highly unbalanced data set, used for credit scoring. We evaluate various configuration including neural network optimization techniques and try to determine their capacities when they operate with imbalanced corpora.

</details>

### [Cross-Attention End-to-End ASR for Two-Party Conversations](1907.10726.md)
**Suyoun Kim, Siddharth Dalmia, Florian Metze** · 2019-07-24

<details>
<summary>Abstract</summary>

We present an end-to-end speech recognition model that learns interaction between two speakers based on the turn-changing information. Unlike conventional speech recognition models, our model exploits two speakers' history of conversational-context information that spans across multiple turns within an end-to-end framework. Specifically, we propose a speaker-specific cross-attention mechanism that can look at the output of the other speaker side as well as the one of the current speaker for better at recognizing long conversations. We evaluated the models on the Switchboard conversational speech corpus and show that our model outperforms standard end-to-end speech recognition models.

</details>

### [2D-CTC for Scene Text Recognition](1907.09705.md)
**Zhaoyi Wan, Fengming Xie, Yibo Liu, Xiang Bai et al.** · 2019-07-23

<details>
<summary>Abstract</summary>

Scene text recognition has been an important, active research topic in computer vision for years. Previous approaches mainly consider text as 1D signals and cast scene text recognition as a sequence prediction problem, by feat of CTC or attention based encoder-decoder framework, which is originally designed for speech recognition. However, different from speech voices, which are 1D signals, text instances are essentially distributed in 2D image spaces. To adhere to and make use of the 2D nature of text for higher recognition accuracy, we extend the vanilla CTC model to a second dimension, thus creating 2D-CTC. 2D-CTC can adaptively concentrate on most relevant features while excluding the impact from clutters and noises in the background; It can also naturally handle text instances with various forms (horizontal, oriented and curved) while giving more interpretable intermediate predictions. The experiments on standard benchmarks for scene text recognition, such as IIIT-5K, ICDAR 2015, SVP-Perspective, and CUTE80, demonstrate that the proposed 2D-CTC model outperforms state-of-the-art methods on the text of both regular and irregular shapes. Moreover, 2D-CTC exhibits its superiority over prior art on training and testing speed. Our implementation and models of 2D-CTC will be made publicly available soon later.

</details>

### [On Modeling ASR Word Confidence](1907.09636.md)
**Woojay Jeon, Maxwell Jordan, Mahesh Krishnamoorthy** · 2019-07-22

<details>
<summary>Abstract</summary>

We present a new method for computing ASR word confidences that effectively mitigates the effect of ASR errors for diverse downstream applications, improves the word error rate of the 1-best result, and allows better comparison of scores across different models. We propose 1) a new method for modeling word confidence using a Heterogeneous Word Confusion Network (HWCN) that addresses some key flaws in conventional Word Confusion Networks, and 2) a new score calibration method for facilitating direct comparison of scores from different models. Using a bidirectional lattice recurrent neural network to compute the confidence scores of each word in the HWCN, we show that the word sequence with the best overall confidence is more accurate than the default 1-best result of the recognizer, and that the calibration method can substantially improve the reliability of recognizer combination.

</details>

### [Deep Learning to Address Candidate Generation and Cold Start Challenges in Recommender Systems: A Research Survey](1907.08674.md)
**Kiran Rama, Pradeep Kumar, Bharat Bhasker** · 2019-07-17

<details>
<summary>Abstract</summary>

Among the machine learning applications to business, recommender systems would take one of the top places when it comes to success and adoption. They help the user in accelerating the process of search while helping businesses maximize sales. Post phenomenal success in computer vision and speech recognition, deep learning methods are beginning to get applied to recommender systems. Current survey papers on deep learning in recommender systems provide a historical overview and taxonomy of recommender systems based on type. Our paper addresses the gaps of providing a taxonomy of deep learning approaches to address recommender systems problems in the areas of cold start and candidate generation in recommender systems. We outline different challenges in recommender systems into those related to the recommendations themselves (include relevance, speed, accuracy and scalability), those related to the nature of the data (cold start problem, imbalance and sparsity) and candidate generation. We then provide a taxonomy of deep learning techniques to address these challenges. Deep learning techniques are mapped to the different challenges in recommender systems providing an overview of how deep learning techniques can be used to address them. We contribute a taxonomy of deep learning techniques to address the cold start and candidate generation problems in recommender systems. Cold Start is addressed through additional features (for audio, images, text) and by learning hidden user and item representations. Candidate generation has been addressed by separate networks, RNNs, autoencoders and hybrid methods. We also summarize the advantages and limitations of these techniques while outlining areas for future research.

</details>

### [Comparison of Neural Network Architectures for Spectrum Sensing](1907.07321.md)
**Ziyu Ye, Andrew Gilman, Qihang Peng, Kelly Levick et al.** · 2019-07-15

<details>
<summary>Abstract</summary>

Different neural network (NN) architectures have different advantages. Convolutional neural networks (CNNs) achieved enormous success in computer vision, while recurrent neural networks (RNNs) gained popularity in speech recognition. It is not known which type of NN architecture is the best fit for classification of communication signals. In this work, we compare the behavior of fully-connected NN (FC), CNN, RNN, and bi-directional RNN (BiRNN) in a spectrum sensing task. The four NN architectures are compared on their detection performance, requirement of training data, computational complexity, and memory requirement. Given abundant training data and computational and memory resources, CNN, RNN, and BiRNN are shown to achieve similar performance. The performance of FC is worse than that of the other three types, except in the case where computational complexity is stringently limited.

</details>

### [Investigation on N-gram Approximated RNNLMs for Recognition of Morphologically Rich Speech](1907.06407.md)
**Balázs Tarján, György Szaszák, Tibor Fegyó, Péter Mihajlik** · 2019-07-15

<details>
<summary>Abstract</summary>

Recognition of Hungarian conversational telephone speech is challenging due to the informal style and morphological richness of the language. Recurrent Neural Network Language Model (RNNLM) can provide remedy for the high perplexity of the task; however, two-pass decoding introduces a considerable processing delay. In order to eliminate this delay we investigate approaches aiming at the complexity reduction of RNNLM, while preserving its accuracy. We compare the performance of conventional back-off n-gram language models (BNLM), BNLM approximation of RNNLMs (RNN-BNLM) and RNN n-grams in terms of perplexity and word error rate (WER). Morphological richness is often addressed by using statistically derived subwords - morphs - in the language models, hence our investigations are extended to morph-based models, as well. We found that using RNN-BNLMs 40% of the RNNLM perplexity reduction can be recovered, which is roughly equal to the performance of a RNN 4-gram model. Combining morph-based modeling and approximation of RNNLM, we were able to achieve 8% relative WER reduction and preserve real-time operation of our conversational telephone speech recognition system.

</details>

### [Investigating Target Set Reduction for End-to-End Speech Recognition of Hindi-English Code-Switching Data](1907.08293.md)
**Kunal Dhawan, Ganji Sreeram, Kumar Priyadarshi, Rohit Sinha** · 2019-07-15

<details>
<summary>Abstract</summary>

End-to-end (E2E) systems are fast replacing the conventional systems in the domain of automatic speech recognition. As the target labels are learned directly from speech data, the E2E systems need a bigger corpus for effective training. In the context of code-switching task, the E2E systems face two challenges: (i) the expansion of the target set due to multiple languages involved, and (ii) the lack of availability of sufficiently large domain-specific corpus. Towards addressing those challenges, we propose an approach for reducing the number of target labels for reliable training of the E2E systems on limited data. The efficacy of the proposed approach has been demonstrated on two prominent architectures, namely CTC-based and attention-based E2E networks. The experimental validations are performed on a recently created Hindi-English code-switching corpus. For contrast purpose, the results for the full target set based E2E system and a hybrid DNN-HMM system are also reported.

</details>

### [Learn Spelling from Teachers: Transferring Knowledge from Language Models to Sequence-to-Sequence Speech Recognition](1907.06017.md)
**Ye Bai, Jiangyan Yi, Jianhua Tao, Zhengkun Tian et al.** · 2019-07-13

<details>
<summary>Abstract</summary>

Integrating an external language model into a sequence-to-sequence speech recognition system is non-trivial. Previous works utilize linear interpolation or a fusion network to integrate external language models. However, these approaches introduce external components, and increase decoding computation. In this paper, we instead propose a knowledge distillation based training approach to integrating external language models into a sequence-to-sequence model. A recurrent neural network language model, which is trained on large scale external text, generates soft labels to guide the sequence-to-sequence model training. Thus, the language model plays the role of the teacher. This approach does not add any external component to the sequence-to-sequence model during testing. And this approach is flexible to be combined with shallow fusion technique together for decoding. The experiments are conducted on public Chinese datasets AISHELL-1 and CLMAD. Our approach achieves a character error rate of 9.3%, which is relatively reduced by 18.42% compared with the vanilla sequence-to-sequence model.

</details>

### [Large-Scale Mixed-Bandwidth Deep Neural Network Acoustic Modeling for Automatic Speech Recognition](1907.04887.md)
**Khoi-Nguyen C. Mac, Xiaodong Cui, Wei Zhang, Michael Picheny** · 2019-07-10

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR), wideband (WB) and narrowband (NB) speech signals with different sampling rates typically use separate acoustic models. Therefore mixed-bandwidth (MB) acoustic modeling has important practical values for ASR system deployment. In this paper, we extensively investigate large-scale MB deep neural network acoustic modeling for ASR using 1,150 hours of WB data and 2,300 hours of NB data. We study various MB strategies including downsampling, upsampling and bandwidth extension for MB acoustic modeling and evaluate their performance on 8 diverse WB and NB test sets from various application domains. To deal with the large amounts of training data, distributed training is carried out on multiple GPUs using synchronous data parallelism.

</details>

### [Acoustic Model Optimization Based On Evolutionary Stochastic Gradient Descent with Anchors for Automatic Speech Recognition](1907.04882.md)
**Xiaodong Cui, Michael Picheny** · 2019-07-10

<details>
<summary>Abstract</summary>

Evolutionary stochastic gradient descent (ESGD) was proposed as a population-based approach that combines the merits of gradient-aware and gradient-free optimization algorithms for superior overall optimization performance. In this paper we investigate a variant of ESGD for optimization of acoustic models for automatic speech recognition (ASR). In this variant, we assume the existence of a well-trained acoustic model and use it as an anchor in the parent population whose good "gene" will propagate in the evolution to the offsprings. We propose an ESGD algorithm leveraging the anchor models such that it guarantees the best fitness of the population will never degrade from the anchor model. Experiments on 50-hour Broadcast News (BN50) and 300-hour Switchboard (SWB300) show that the ESGD with anchors can further improve the loss and ASR performance over the existing well-trained acoustic models.

</details>

### [A Highly Efficient Distributed Deep Learning System For Automatic Speech Recognition](1907.05701.md)
**Wei Zhang, Xiaodong Cui, Ulrich Finkler, George Saon et al.** · 2019-07-10

<details>
<summary>Abstract</summary>

Modern Automatic Speech Recognition (ASR) systems rely on distributed deep learning to for quick training completion. To enable efficient distributed training, it is imperative that the training algorithms can converge with a large mini-batch size. In this work, we discovered that Asynchronous Decentralized Parallel Stochastic Gradient Descent (ADPSGD) can work with much larger batch size than commonly used Synchronous SGD (SSGD) algorithm. On commonly used public SWB-300 and SWB-2000 ASR datasets, ADPSGD can converge with a batch size 3X as large as the one used in SSGD, thus enable training at a much larger scale. Further, we proposed a Hierarchical-ADPSGD (H-ADPSGD) system in which learners on the same computing node construct a super learner via a fast allreduce implementation, and super learners deploy ADPSGD algorithm among themselves. On a 64 Nvidia V100 GPU cluster connected via a 100Gb/s Ethernet network, our system is able to train SWB-2000 to reach a 7.6% WER on the Hub5-2000 Switchboard (SWB) test-set and a 13.2% WER on the Call-home (CH) test-set in 5.2 hours. To the best of our knowledge, this is the fastest ASR training system that attains this level of model accuracy for SWB-2000 task to be ever reported in the literature.

</details>

### [Multi-layer Attention Mechanism for Speech Keyword Recognition](1907.04536.md)
**Ruisen Luo, Tianran Sun, Chen Wang, Miao Du et al.** · 2019-07-10

<details>
<summary>Abstract</summary>

As an important part of speech recognition technology, automatic speech keyword recognition has been intensively studied in recent years. Such technology becomes especially pivotal under situations with limited infrastructures and computational resources, such as voice command recognition in vehicles and robot interaction. At present, the mainstream methods in automatic speech keyword recognition are based on long short-term memory (LSTM) networks with attention mechanism. However, due to inevitable information losses for the LSTM layer caused during feature extraction, the calculated attention weights are biased. In this paper, a novel approach, namely Multi-layer Attention Mechanism, is proposed to handle the inaccurate attention weights problem. The key idea is that, in addition to the conventional attention mechanism, information of layers prior to feature extraction and LSTM are introduced into attention weights calculations. Therefore, the attention weights are more accurate because the overall model can have more precise and focused areas. We conduct a comprehensive comparison and analysis on the keyword spotting performances on convolution neural network, bi-directional LSTM cyclic neural network, and cyclic neural network with the proposed attention mechanism on Google Speech Command datasets V2 datasets. Experimental results indicate favorable results for the proposed method and demonstrate the validity of the proposed method. The proposed multi-layer attention methods can be useful for other researches related to object spotting.

</details>

### [M3D-GAN: Multi-Modal Multi-Domain Translation with Universal Attention](1907.04378.md)
**Shuang Ma, Daniel McDuff, Yale Song** · 2019-07-09

<details>
<summary>Abstract</summary>

Generative adversarial networks have led to significant advances in cross-modal/domain translation. However, typically these networks are designed for a specific task (e.g., dialogue generation or image synthesis, but not both). We present a unified model, M3D-GAN, that can translate across a wide range of modalities (e.g., text, image, and speech) and domains (e.g., attributes in images or emotions in speech). Our model consists of modality subnets that convert data from different modalities into unified representations, and a unified computing body where data from different modalities share the same network architecture. We introduce a universal attention module that is jointly trained with the whole network and learns to encode a large range of domain information into a highly structured latent space. We use this to control synthesis in novel ways, such as producing diverse realistic pictures from a sketch or varying the emotion of synthesized speech. We evaluate our approach on extensive benchmark tasks, including image-to-image, text-to-image, image captioning, text-to-speech, speech recognition, and machine translation. Our results show state-of-the-art performance on some of the tasks.

</details>

### [Analyzing Phonetic and Graphemic Representations in End-to-End Automatic Speech Recognition](1907.04224.md)
**Yonatan Belinkov, Ahmed Ali, James Glass** · 2019-07-09

<details>
<summary>Abstract</summary>

End-to-end neural network systems for automatic speech recognition (ASR) are trained from acoustic features to text transcriptions. In contrast to modular ASR systems, which contain separately-trained components for acoustic modeling, pronunciation lexicon, and language modeling, the end-to-end paradigm is both conceptually simpler and has the potential benefit of training the entire system on the end task. However, such neural network models are more opaque: it is not clear how to interpret the role of different parts of the network and what information it learns during training. In this paper, we analyze the learned internal representations in an end-to-end ASR model. We evaluate the representation quality in terms of several classification tasks, comparing phonemes and graphemes, as well as different articulatory features. We study two languages (English and Arabic) and three datasets, finding remarkable consistency in how different properties are represented in different layers of the deep neural network.

</details>

### [Teach an all-rounder with experts in different domains](1907.05698.md)
**Zhao You, Dan Su, Dong Yu** · 2019-07-09

<details>
<summary>Abstract</summary>

In many automatic speech recognition (ASR) tasks, an ideal model has to be applicable over multiple domains. In this paper, we propose to teach an all-rounder with experts in different domains. Concretely, we build a multi-domain acoustic model by applying the teacher-student training framework. First, for each domain, a teacher model (domain-dependent model) is trained by fine-tuning a multi-condition model with domain-specific subset. Then all these teacher models are used to teach one single student model simultaneously. We perform experiments on two predefined domain setups. One is domains with different speaking styles, the other is nearfield, far-field and far-field with noise. Moreover, two types of models are examined: deep feedforward sequential memory network (DFSMN) and long short term memory (LSTM). Experimental results show that the model trained with this framework outperforms not only multi-condition model but also domain-dependent model. Specially, our training method provides up to 10.4% relative character error rate improvement over baseline model (multi-condition model).

</details>

### [Improving Reverberant Speech Training Using Diffuse Acoustic Simulation](1907.03988.md)
**Zhenyu Tang, Lianwu Chen, Bo Wu, Dong Yu et al.** · 2019-07-09

<details>
<summary>Abstract</summary>

We present an efficient and realistic geometric acoustic simulation approach for generating and augmenting training data in speech-related machine learning tasks. Our physically-based acoustic simulation method is capable of modeling occlusion, specular and diffuse reflections of sound in complicated acoustic environments, whereas the classical image method can only model specular reflections in simple room settings. We show that by using our synthetic training data, the same neural networks gain significant performance improvement on real test sets in far-field speech recognition by 1.58% and keyword spotting by 21%, without fine-tuning using real impulse responses.

</details>

### [Joint Speech Recognition and Speaker Diarization via Sequence Transduction](1907.05337.md)
**Laurent El Shafey, Hagen Soltau, Izhak Shafran** · 2019-07-09

<details>
<summary>Abstract</summary>

Speech applications dealing with conversations require not only recognizing the spoken words, but also determining who spoke when. The task of assigning words to speakers is typically addressed by merging the outputs of two separate systems, namely, an automatic speech recognition (ASR) system and a speaker diarization (SD) system. The two systems are trained independently with different objective functions. Often the SD systems operate directly on the acoustics and are not constrained to respect word boundaries and this deficiency is overcome in an ad hoc manner. Motivated by recent advances in sequence to sequence learning, we propose a novel approach to tackle the two tasks by a joint ASR and SD system using a recurrent neural network transducer. Our approach utilizes both linguistic and acoustic cues to infer speaker roles, as opposed to typical SD systems, which only use acoustic cues. We evaluated the performance of our approach on a large corpus of medical conversations between physicians and patients. Compared to a competitive conventional baseline, our approach improves word-level diarization error rate from 15.8% to 2.2%.

</details>

### [ShrinkML: End-to-End ASR Model Compression Using Reinforcement Learning](1907.03540.md)
**Łukasz Dudziak, Mohamed S. Abdelfattah, Ravichander Vipperla, Stefanos Laskaridis et al.** · 2019-07-08

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) models are increasingly large and complex to achieve the best possible accuracy. In this paper, we build an AutoML system that uses reinforcement learning (RL) to optimize the per-layer compression ratios when applied to a state-of-the-art attention based end-to-end ASR model composed of several LSTM layers. We use singular value decomposition (SVD) low-rank matrix factorization as the compression method. For our RL-based AutoML system, we focus on practical considerations such as the choice of the reward/punishment functions, the formation of an effective search space, and the creation of a representative but small data set for quick evaluation between search steps. Finally, we present accuracy results on LibriSpeech of the model compressed by our AutoML system, and we compare it to manually-compressed models. Our results show that in the absence of retraining our RL-based search is an effective and practical method to compress a production-grade ASR system. When retraining is possible, we show that our AutoML system can select better highly-compressed seed models compared to manually hand-crafted rank selection, thus allowing for more compression than previously possible.

</details>

### [Listen, Attend, Spell and Adapt: Speaker Adapted Sequence-to-Sequence ASR](1907.04916.md)
**Felix Weninger, Jesús Andrés-Ferrer, Xinwei Li, Puming Zhan** · 2019-07-08

<details>
<summary>Abstract</summary>

Sequence-to-sequence (seq2seq) based ASR systems have shown state-of-the-art performances while having clear advantages in terms of simplicity. However, comparisons are mostly done on speaker independent (SI) ASR systems, though speaker adapted conventional systems are commonly used in practice for improving robustness to speaker and environment variations. In this paper, we apply speaker adaptation to seq2seq models with the goal of matching the performance of conventional ASR adaptation. Specifically, we investigate Kullback-Leibler divergence (KLD) as well as Linear Hidden Network (LHN) based adaptation for seq2seq ASR, using different amounts (up to 20 hours) of adaptation data per speaker. Our SI models are trained on large amounts of dictation data and achieve state-of-the-art results. We obtained 25% relative word error rate (WER) improvement with KLD adaptation of the seq2seq model vs. 18.7% gain from acoustic model adaptation in the conventional system. We also show that the WER of the seq2seq model decreases log-linearly with the amount of adaptation data. Finally, we analyze adaptation based on the minimum WER criterion and adapting the language model (LM) for score fusion with the speaker adapted seq2seq model, which result in further improvements of the seq2seq system performance.

</details>

### [NIESR: Nuisance Invariant End-to-end Speech Recognition](1907.03233.md)
**I-Hung Hsu, Ayush Jaiswal, Premkumar Natarajan** · 2019-07-07

<details>
<summary>Abstract</summary>

Deep neural network models for speech recognition have achieved great success recently, but they can learn incorrect associations between the target and nuisance factors of speech (e.g., speaker identities, background noise, etc.), which can lead to overfitting. While several methods have been proposed to tackle this problem, existing methods incorporate additional information about nuisance factors during training to develop invariant models. However, enumeration of all possible nuisance factors in speech data and the collection of their annotations is difficult and expensive. We present a robust training scheme for end-to-end speech recognition that adopts an unsupervised adversarial invariance induction framework to separate out essential factors for speech-recognition from nuisances without using any supplementary labels besides the transcriptions. Experiments show that the speech recognition model trained with the proposed training scheme achieves relative improvements of 5.48% on WSJ0, 6.16% on CHiME3, and 6.61% on TIMIT dataset over the base model. Additionally, the proposed method achieves a relative improvement of 14.44% on the combined WSJ0+CHiME3 dataset.

</details>

### [Improved low-resource Somali speech recognition by semi-supervised acoustic and language model training](1907.03064.md)
**Astik Biswas, Raghav Menon, Ewald van der Westhuizen, Thomas Niesler** · 2019-07-06

<details>
<summary>Abstract</summary>

We present improvements in automatic speech recognition (ASR) for Somali, a currently extremely under-resourced language. This forms part of a continuing United Nations (UN) effort to employ ASR-based keyword spotting systems to support humanitarian relief programmes in rural Africa. Using just 1.57 hours of annotated speech data as a seed corpus, we increase the pool of training data by applying semi-supervised training to 17.55 hours of untranscribed speech. We make use of factorised time-delay neural networks (TDNN-F) for acoustic modelling, since these have recently been shown to be effective in resource-scarce situations. Three semi-supervised training passes were performed, where the decoded output from each pass was used for acoustic model training in the subsequent pass. The automatic transcriptions from the best performing pass were used for language model augmentation. To ensure the quality of automatic transcriptions, decoder confidence is used as a threshold. The acoustic and language models obtained from the semi-supervised approach show significant improvement in terms of WER and perplexity compared to the baseline. Incorporating the automatically generated transcriptions yields a 6.55\% improvement in language model perplexity. The use of 17.55 hour of Somali acoustic data in semi-supervised training shows an improvement of 7.74\% relative over the baseline.

</details>

### [Toward Fairness in AI for People with Disabilities: A Research Roadmap](1907.02227.md)
**Anhong Guo, Ece Kamar, Jennifer Wortman Vaughan, Hanna Wallach et al.** · 2019-07-04

<details>
<summary>Abstract</summary>

AI technologies have the potential to dramatically impact the lives of people with disabilities (PWD). Indeed, improving the lives of PWD is a motivator for many state-of-the-art AI systems, such as automated speech recognition tools that can caption videos for people who are deaf and hard of hearing, or language prediction algorithms that can augment communication for people with speech or cognitive disabilities. However, widely deployed AI systems may not work properly for PWD, or worse, may actively discriminate against them. These considerations regarding fairness in AI for PWD have thus far received little attention. In this position paper, we identify potential areas of concern regarding how several AI technology categories may impact particular disability constituencies if care is not taken in their design, development, and testing. We intend for this risk assessment of how various classes of AI might interact with various classes of disability to provide a roadmap for future research that is needed to gather data, test these hypotheses, and build more inclusive algorithms.

</details>

### [End-to-End Speech Recognition with High-Frame-Rate Features Extraction](1907.01957.md)
**Cong-Thanh Do** · 2019-07-03

<details>
<summary>Abstract</summary>

State-of-the-art end-to-end automatic speech recognition (ASR) extracts acoustic features from input speech signal every 10 ms which corresponds to a frame rate of 100 frames/second. In this report, we investigate the use of high-frame-rate features extraction in end-to-end ASR. High frame rates of 200 and 400 frames/second are used in the features extraction and provide additional information for end-to-end ASR. The effectiveness of high-frame-rate features extraction is evaluated independently and in combination with speed perturbation based data augmentation. Experiments performed on two speech corpora, Wall Street Journal (WSJ) and CHiME-5, show that using high-frame-rate features extraction yields improved performance for end-to-end ASR, both independently and in combination with speed perturbation. On WSJ corpus, the relative reduction of word error rate (WER) yielded by high-frame-rate features extraction independently and in combination with speed perturbation are up to 21.3% and 24.1%, respectively. On CHiME-5 corpus, the corresponding relative WER reductions are up to 2.8% and 7.9%, respectively, on the test data recorded by microphone arrays and up to 11.8% and 21.2%, respectively, on the test data recorded by binaural microphones.

</details>

### [Scalable Multi Corpora Neural Language Models for ASR](1907.01677.md)
**Anirudh Raju, Denis Filimonov, Gautam Tiwari, Guitang Lan et al.** · 2019-07-02

<details>
<summary>Abstract</summary>

Neural language models (NLM) have been shown to outperform conventional n-gram language models by a substantial margin in Automatic Speech Recognition (ASR) and other tasks. There are, however, a number of challenges that need to be addressed for an NLM to be used in a practical large-scale ASR system. In this paper, we present solutions to some of the challenges, including training NLM from heterogenous corpora, limiting latency impact and handling personalized bias in the second-pass rescorer. Overall, we show that we can achieve a 6.2% relative WER reduction using neural LM in a second-pass n-best rescoring framework with a minimal increase in latency.

</details>

### [Latent Dirichlet Allocation Based Acoustic Data Selection for Automatic Speech Recognition](1907.01302.md)
**Mortaza, Doulaty, Thomas Hain** · 2019-07-02

<details>
<summary>Abstract</summary>

Selecting in-domain data from a large pool of diverse and out-of-domain data is a non-trivial problem. In most cases simply using all of the available data will lead to sub-optimal and in some cases even worse performance compared to carefully selecting a matching set. This is true even for data-inefficient neural models. Acoustic Latent Dirichlet Allocation (aLDA) is shown to be useful in a variety of speech technology related tasks, including domain adaptation of acoustic models for automatic speech recognition and entity labeling for information retrieval. In this paper we propose to use aLDA as a data similarity criterion in a data selection framework. Given a large pool of out-of-domain and potentially mismatched data, the task is to select the best-matching training data to a set of representative utterances sampled from a target domain. Our target data consists of around 32 hours of meeting data (both far-field and close-talk) and the pool contains 2k hours of meeting, talks, voice search, dictation, command-and-control, audio books, lectures, generic media and telephony speech data. The proposed technique for training data selection, significantly outperforms random selection, posterior-based selection as well as using all of the available data.

</details>

### [Attention model for articulatory features detection](1907.01914.md)
**Ievgen Karaulov, Dmytro Tkanov** · 2019-07-02

<details>
<summary>Abstract</summary>

Articulatory distinctive features, as well as phonetic transcription, play important role in speech-related tasks: computer-assisted pronunciation training, text-to-speech conversion (TTS), studying speech production mechanisms, speech recognition for low-resourced languages. End-to-end approaches to speech-related tasks got a lot of traction in recent years. We apply Listen, Attend and Spell~(LAS)~\cite{Chan-LAS2016} architecture to phones recognition on a small small training set, like TIMIT~\cite{TIMIT-1992}. Also, we introduce a novel decoding technique that allows to train manners and places of articulation detectors end-to-end using attention models. We also explore joint phones recognition and articulatory features detection in multitask learning setting.

</details>

### [Kite: Automatic speech recognition for unmanned aerial vehicles](1907.01195.md)
**Dan Oneata, Horia Cucu** · 2019-07-02

<details>
<summary>Abstract</summary>

This paper addresses the problem of building a speech recognition system attuned to the control of unmanned aerial vehicles (UAVs). Even though UAVs are becoming widespread, the task of creating voice interfaces for them is largely unaddressed. To this end, we introduce a multi-modal evaluation dataset for UAV control, consisting of spoken commands and associated images, which represent the visual context of what the UAV "sees" when the pilot utters the command. We provide baseline results and address two research directions: (i) how robust the language models are, given an incomplete list of commands at train time; (ii) how to incorporate visual information in the language model. We find that recurrent neural networks (RNNs) are a solution to both tasks: they can be successfully adapted using a small number of commands and they can be extended to use visual cues. Our results show that the image-based RNN outperforms its text-only counterpart even if the command-image training associations are automatically generated and inherently imperfect. The dataset and our code are available at http://kite.speed.pub.ro.

</details>

### [Learning Representations from Imperfect Time Series Data via Tensor Rank Regularization](1907.01011.md)
**Paul Pu Liang, Zhun Liu, Yao-Hung Hubert Tsai, Qibin Zhao et al.** · 2019-07-01

<details>
<summary>Abstract</summary>

There has been an increased interest in multimodal language processing including multimodal dialog, question answering, sentiment analysis, and speech recognition. However, naturally occurring multimodal data is often imperfect as a result of imperfect modalities, missing entries or noise corruption. To address these concerns, we present a regularization method based on tensor rank minimization. Our method is based on the observation that high-dimensional multimodal time series data often exhibit correlations across time and modalities which leads to low-rank tensor representations. However, the presence of noise or incomplete values breaks these correlations and results in tensor representations of higher rank. We design a model to learn such tensor representations and effectively regularize their rank. Experiments on multimodal language data show that our model achieves good results across various levels of imperfection.

</details>

### [Comparison of Lattice-Free and Lattice-Based Sequence Discriminative Training Criteria for LVCSR](1907.01409.md)
**Wilfried Michel, Ralf Schlüter, Hermann Ney** · 2019-07-01

<details>
<summary>Abstract</summary>

Sequence discriminative training criteria have long been a standard tool in automatic speech recognition for improving the performance of acoustic models over their maximum likelihood / cross entropy trained counterparts. While previously a lattice approximation of the search space has been necessary to reduce computational complexity, recently proposed methods use other approximations to dispense of the need for the computationally expensive step of separate lattice creation. In this work we present a memory efficient implementation of the forward-backward computation that allows us to use uni-gram word-level language models in the denominator calculation while still doing a full summation on GPU. This allows for a direct comparison of lattice-based and lattice-free sequence discriminative training criteria such as MMI and sMBR, both using the same language model during training. We compared performance, speed of convergence, and stability on large vocabulary continuous speech recognition tasks like Switchboard and Quaero. We found that silence modeling seriously impacts the performance in the lattice-free case and needs special treatment. In our experiments lattice-free MMI comes on par with its lattice-based counterpart. Lattice-based sMBR still outperforms all lattice-free training criteria.

</details>

### [Improving Performance of End-to-End ASR on Numeric Sequences](1907.01372.md)
**Cal Peyser, Hao Zhang, Tara N. Sainath, Zelin Wu** · 2019-07-01

<details>
<summary>Abstract</summary>

Recognizing written domain numeric utterances (e.g. I need $1.25.) can be challenging for ASR systems, particularly when numeric sequences are not seen during training. This out-of-vocabulary (OOV) issue is addressed in conventional ASR systems by training part of the model on spoken domain utterances (e.g. I need one dollar and twenty five cents.), for which numeric sequences are composed of in-vocabulary numbers, and then using an FST verbalizer to denormalize the result. Unfortunately, conventional ASR models are not suitable for the low memory setting of on-device speech recognition. E2E models such as RNN-T are attractive for on-device ASR, as they fold the AM, PM and LM of a conventional model into one neural network. However, in the on-device setting the large memory footprint of an FST denormer makes spoken domain training more difficult. In this paper, we investigate techniques to improve E2E model performance on numeric data. We find that using a text-to-speech system to generate additional numeric training data, as well as using a small-footprint neural network to perform spoken-to-written domain denorming, yields improvement in several numeric classes. In the case of the longest numeric sequences, we see reduction of WER by up to a factor of 8.

</details>

### [Analyzing Utility of Visual Context in Multimodal Speech Recognition Under Noisy Conditions](1907.00477.md)
**Tejas Srinivasan, Ramon Sanabria, Florian Metze** · 2019-06-30

<details>
<summary>Abstract</summary>

Multimodal learning allows us to leverage information from multiple sources (visual, acoustic and text), similar to our experience of the real world. However, it is currently unclear to what extent auxiliary modalities improve performance over unimodal models, and under what circumstances the auxiliary modalities are useful. We examine the utility of the auxiliary visual context in Multimodal Automatic Speech Recognition in adversarial settings, where we deprive the models from partial audio signal during inference time. Our experiments show that while MMASR models show significant gains over traditional speech-to-text architectures (upto 4.2% WER improvements), they do not incorporate visual information when the audio signal has been corrupted. This shows that current methods of integrating the visual modality do not improve model robustness to noise, and we need better visually grounded adaptation techniques.

</details>

### [Gated Embeddings in End-to-End Speech Recognition for Conversational-Context Fusion](1906.11604.md)
**Suyoun Kim, Siddharth Dalmia, Florian Metze** · 2019-06-27

<details>
<summary>Abstract</summary>

We present a novel conversational-context aware end-to-end speech recognizer based on a gated neural network that incorporates conversational-context/word/speech embeddings. Unlike conventional speech recognition models, our model learns longer conversational-context information that spans across sentences and is consequently better at recognizing long conversations. Specifically, we propose to use the text-based external word and/or sentence embeddings (i.e., fastText, BERT) within an end-to-end framework, yielding a significant improvement in word error rate with better conversational-context representation. We evaluated the models on the Switchboard conversational speech corpus and show that our model outperforms standard end-to-end speech recognition models.

</details>

### [One Size Does Not Fit All: Quantifying and Exposing the Accuracy-Latency Trade-off in Machine Learning Cloud Service APIs via Tolerance Tiers](1906.11307.md)
**Matthew Halpern, Behzad Boroujerdian, Todd Mummert, Evelyn Duesterwald et al.** · 2019-06-26

<details>
<summary>Abstract</summary>

Today's cloud service architectures follow a "one size fits all" deployment strategy where the same service version instantiation is provided to the end users. However, consumers are broad and different applications have different accuracy and responsiveness requirements, which as we demonstrate renders the "one size fits all" approach inefficient in practice. We use a production-grade speech recognition engine, which serves several thousands of users, and an open source computer vision based system, to explain our point. To overcome the limitations of the "one size fits all" approach, we recommend Tolerance Tiers where each MLaaS tier exposes an accuracy/responsiveness characteristic, and consumers can programmatically select a tier. We evaluate our proposal on the CPU-based automatic speech recognition (ASR) engine and cutting-edge neural networks for image classification deployed on both CPUs and GPUs. The results show that our proposed approach provides an MLaaS cloud service architecture that can be tuned by the end API user or consumer to outperform the conventional "one size fits all" approach.

</details>

### [A Winograd-based Integrated Photonics Accelerator for Convolutional Neural Networks](1906.10487.md)
**Armin Mehrabian, Mario Miscuglio, Yousra Alkabani, Volker J. Sorger et al.** · 2019-06-25

<details>
<summary>Abstract</summary>

Neural Networks (NNs) have become the mainstream technology in the artificial intelligence (AI) renaissance over the past decade. Among different types of neural networks, convolutional neural networks (CNNs) have been widely adopted as they have achieved leading results in many fields such as computer vision and speech recognition. This success in part is due to the widespread availability of capable underlying hardware platforms. Applications have always been a driving factor for design of such hardware architectures. Hardware specialization can expose us to novel architectural solutions, which can outperform general purpose computers for tasks at hand. Although different applications demand for different performance measures, they all share speed and energy efficiency as high priorities. Meanwhile, photonics processing has seen a resurgence due to its inherited high speed and low power nature. Here, we investigate the potential of using photonics in CNNs by proposing a CNN accelerator design based on Winograd filtering algorithm. Our evaluation results show that while a photonic accelerator can compete with current-state-of-the-art electronic platforms in terms of both speed and power, it has the potential to improve the energy efficiency by up to three orders of magnitude.

</details>

### [Machine Learning Construction: implications to cybersecurity](1906.10019.md)
**Waleed A. Yousef** · 2019-06-24

<details>
<summary>Abstract</summary>

Statistical learning is the process of estimating an unknown probabilistic input-output relationship of a system using a limited number of observations. A statistical learning machine (SLM) is the algorithm, function, model, or rule, that learns such a process; and machine learning (ML) is the conventional name of this field. ML and its applications are ubiquitous in the modern world. Systems such as Automatic target recognition (ATR) in military applications, computer aided diagnosis (CAD) in medical imaging, DNA microarrays in genomics, optical character recognition (OCR), speech recognition (SR), spam email filtering, stock market prediction, etc., are few examples and applications for ML; diverse fields but one theory. In particular, ML has gained a lot of attention in the field of cyberphysical security, especially in the last decade. It is of great importance to this field to design detection algorithms that have the capability of learning from security data to be able to hunt threats, achieve better monitoring, master the complexity of the threat intelligence feeds, and achieve timely remediation of security incidents. The field of ML can be decomposed into two basic subfields: \textit{construction} and \textit{assessment}. We mean by \textit{construction} designing or inventing an appropriate algorithm that learns from the input data and achieves a good performance according to some optimality criterion. We mean by \textit{assessment} attributing some performance measures to the constructed ML algorithm, along with their estimators, to objectively assess this algorithm. \textit{Construction} and \textit{assessment} of a ML algorithm require familiarity with different other fields: probability, statistics, matrix theory, optimization, algorithms, and programming, among others.f

</details>

### [Learning Waveform-Based Acoustic Models using Deep Variational Convolutional Neural Networks](1906.09526.md)
**Dino Oglic, Zoran Cvetkovic, Peter Sollich** · 2019-06-23

<details>
<summary>Abstract</summary>

We investigate the potential of stochastic neural networks for learning effective waveform-based acoustic models. The waveform-based setting, inherent to fully end-to-end speech recognition systems, is motivated by several comparative studies of automatic and human speech recognition that associate standard non-adaptive feature extraction techniques with information loss which can adversely affect robustness. Stochastic neural networks, on the other hand, are a class of models capable of incorporating rich regularization mechanisms into the learning process. We consider a deep convolutional neural network that first decomposes speech into frequency sub-bands via an adaptive parametric convolutional block where filters are specified by cosine modulations of compactly supported windows. The network then employs standard non-parametric 1D convolutions to extract relevant spectro-temporal patterns while gradually compressing the structured high dimensional representation generated by the parametric block. We rely on a probabilistic parametrization of the proposed neural architecture and learn the model using stochastic variational inference. This requires evaluation of an analytically intractable integral defining the Kullback-Leibler divergence term responsible for regularization, for which we propose an effective approximation based on the Gauss-Hermite quadrature. Our empirical results demonstrate a superior performance of the proposed approach over comparable waveform-based baselines and indicate that it could lead to robustness. Moreover, the approach outperforms a recently proposed deep convolutional neural network for learning of robust acoustic models with standard FBANK features.

</details>

### [End-to-End ASR for Code-switched Hindi-English Speech](1906.09426.md)
**Brij Mohan Lal Srivastava, Basil Abraham, Sunayana Sitaram, Rupesh Mehta et al.** · 2019-06-22

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have been explored for large speech corpora and have been found to match or outperform traditional pipeline-based systems in some languages. However, most prior work on end-to-end models use speech corpora exceeding hundreds or thousands of hours. In this study, we explore end-to-end models for code-switched Hindi-English language with less than 50 hours of data. We utilize two specific measures to improve network performance in the low-resource setting, namely multi-task learning (MTL) and balancing the corpus to deal with the inherent class imbalance problem i.e. the skewed frequency distribution over graphemes. We compare the results of the proposed approaches with traditional, cascaded ASR systems. While the lack of data adversely affects the performance of end-to-end models, we see promising improvements with MTL and balancing the corpus.

</details>

### [Phoneme-Based Contextualization for Cross-Lingual Speech Recognition in End-to-End Models](1906.09292.md)
**Ke Hu, Antoine Bruguier, Tara N. Sainath, Rohit Prabhavalkar et al.** · 2019-06-21

<details>
<summary>Abstract</summary>

Contextual automatic speech recognition, i.e., biasing recognition towards a given context (e.g. user's playlists, or contacts), is challenging in end-to-end (E2E) models. Such models maintain a limited number of candidates during beam-search decoding, and have been found to recognize rare named entities poorly. The problem is exacerbated when biasing towards proper nouns in foreign languages, e.g., geographic location names, which are virtually unseen in training and are thus out-of-vocabulary (OOV). While grapheme or wordpiece E2E models might have a difficult time spelling OOV words, phonemes are more acoustically salient and past work has shown that E2E phoneme models can better predict such words. In this work, we propose an E2E model containing both English wordpieces and phonemes in the modeling space, and perform contextual biasing of foreign words at the phoneme level by mapping pronunciations of foreign words into similar English phonemes. In experimental evaluations, we find that the proposed approach performs 16% better than a grapheme-only biasing model, and 8% better than a wordpiece-only biasing model on a foreign place name recognition task, with only slight degradation on regular English tasks.

</details>

### [Database Meets Deep Learning: Challenges and Opportunities](1906.08986.md)
**Wei Wang, Meihui Zhang, Gang Chen, H. V. Jagadish et al.** · 2019-06-21

<details>
<summary>Abstract</summary>

Deep learning has recently become very popular on account of its incredible success in many complex data-driven applications, such as image classification and speech recognition. The database community has worked on data-driven applications for many years, and therefore should be playing a lead role in supporting this new wave. However, databases and deep learning are different in terms of both techniques and applications. In this paper, we discuss research problems at the intersection of the two fields. In particular, we discuss possible improvements for deep learning systems from a database perspective, and analyze database applications that may benefit from deep learning techniques.

</details>

### [Integration of TensorFlow based Acoustic Model with Kaldi WFST Decoder](1906.11018.md)
**Minkyu Lim, Ji-Hwan Kim** · 2019-06-21

<details>
<summary>Abstract</summary>

While the Kaldi framework provides state-of-the-art components for speech recognition like feature extraction, deep neural network (DNN)-based acoustic models, and a weighted finite state transducer (WFST)-based decoder, it is difficult to implement a new flexible DNN model. By contrast, a general-purpose deep learning framework, such as TensorFlow, can easily build various types of neural network architectures using a tensor-based computation method, but it is difficult to apply them to WFST-based speech recognition. In this study, a TensorFlow-based acoustic model is integrated with a WFST-based Kaldi decoder to combine the two frameworks. The features and alignments used in Kaldi are converted so they can be trained by the TensorFlow model, and the DNN-based acoustic model is then trained. In the integrated Kaldi decoder, the posterior probabilities are calculated by querying the trained TensorFlow model, and a beam search is performed to generate the lattice. The advantages of the proposed one-pass decoder include the application of various types of neural networks to WFST-based speech recognition and WFST-based online decoding using a TensorFlow-based acoustic model. The TensorFlow based acoustic models trained using the RM, WSJ, and LibriSpeech datasets show the same level of performance as the model trained using the Kaldi framework.

</details>

### [Multi-Span Acoustic Modelling using Raw Waveform Signals](1906.11047.md)
**Patrick von Platen, Chao Zhang, Philip Woodland** · 2019-06-21

<details>
<summary>Abstract</summary>

Traditional automatic speech recognition (ASR) systems often use an acoustic model (AM) built on handcrafted acoustic features, such as log Mel-filter bank (FBANK) values. Recent studies found that AMs with convolutional neural networks (CNNs) can directly use the raw waveform signal as input. Given sufficient training data, these AMs can yield a competitive word error rate (WER) to those built on FBANK features. This paper proposes a novel multi-span structure for acoustic modelling based on the raw waveform with multiple streams of CNN input layers, each processing a different span of the raw waveform signal. Evaluation on both the single channel CHiME4 and AMI data sets show that multi-span AMs give a lower WER than FBANK AMs by an average of about 5% (relative). Analysis of the trained multi-span model reveals that the CNNs can learn filters that are rather different to the log Mel filters. Furthermore, the paper shows that a widely used single span raw waveform AM can be improved by using a smaller CNN kernel size and increased stride to yield improved WERs.

</details>

### [A simple and effective postprocessing method for image classification](1906.07934.md)
**Yan Liu, Yun Li, Yunhao Yuan, jipeng qiang** · 2019-06-19

<details>
<summary>Abstract</summary>

Whether it is computer vision, natural language processing or speech recognition, the essence of these applications is to obtain powerful feature representations that make downstream applications completion more efficient. Taking image recognition as an example, whether it is hand-crafted low-level feature representation or feature representation extracted by a convolutional neural networks(CNNs), the goal is to extract features that better represent image features, thereby improving classification accuracy. However, we observed that image feature representations share a large common vector and a few top dominating directions. To address this problems, we propose a simple but effective postprocessing method to render off-the-shelf feature representations even stronger by eliminating the common mean vector from off-the-shelf feature representations. The postprocessing is empirically validated on a variety of datasets and feature extraction methods.such as VGG, LBP, and HOG. Some experiments show that the features that have been post-processed by postprocessing algorithm can get better results than original ones.

</details>

### [Multi-Graph Decoding for Code-Switching ASR](1906.07523.md)
**Emre Yılmaz, Samuel Cohen, Xianghu Yue, David van Leeuwen et al.** · 2019-06-18

<details>
<summary>Abstract</summary>

In the FAME! Project, a code-switching (CS) automatic speech recognition (ASR) system for Frisian-Dutch speech is developed that can accurately transcribe the local broadcaster's bilingual archives with CS speech. This archive contains recordings with monolingual Frisian and Dutch speech segments as well as Frisian-Dutch CS speech, hence the recognition performance on monolingual segments is also vital for accurate transcriptions. In this work, we propose a multi-graph decoding and rescoring strategy using bilingual and monolingual graphs together with a unified acoustic model for CS ASR. The proposed decoding scheme gives the freedom to design and employ alternative search spaces for each (monolingual or bilingual) recognition task and enables the effective use of monolingual resources of the high-resourced mixed language in low-resourced CS scenarios. In our scenario, Dutch is the high-resourced and Frisian is the low-resourced language. We therefore use additional monolingual Dutch text resources to improve the Dutch language model (LM) and compare the performance of single- and multi-graph CS ASR systems on Dutch segments using larger Dutch LMs. The ASR results show that the proposed approach outperforms baseline single-graph CS ASR systems, providing better performance on the monolingual Dutch segments without any accuracy loss on monolingual Frisian and code-mixed segments.

</details>

### [Deep Xi as a Front-End for Robust Automatic Speech Recognition](1906.07319.md)
**Aaron Nicolson, Kuldip K. Paliwal** · 2019-06-18

<details>
<summary>Abstract</summary>

Current front-ends for robust automatic speech recognition(ASR) include masking- and mapping-based deep learning approaches to speech enhancement. A recently proposed deep learning approach toa prioriSNR estimation, called DeepXi, was able to produce enhanced speech at a higher quality and intelligibility than current masking- and mapping-based approaches. Motivated by this, we investigate Deep Xi as a front-end for robust ASR. Deep Xi is evaluated using real-world non-stationary and coloured noise sources at multiple SNR levels. Our experimental investigation shows that DeepXi as a front-end is able to produce a lower word error rate than recent masking- and mapping-based deep learning front-ends. The results presented in this work show that Deep Xi is a viable front-end, and is able to significantly increase the robustness of an ASR system. Availability: Deep Xi is available at:https://github.com/anicolson/DeepXi

</details>

### [Multi-Stream End-to-End Speech Recognition](1906.08041.md)
**Ruizhi Li, Xiaofei Wang, Sri Harish Mallidi, Shinji Watanabe et al.** · 2019-06-17

<details>
<summary>Abstract</summary>

Attention-based methods and Connectionist Temporal Classification (CTC) network have been promising research directions for end-to-end (E2E) Automatic Speech Recognition (ASR). The joint CTC/Attention model has achieved great success by utilizing both architectures during multi-task training and joint decoding. In this work, we present a multi-stream framework based on joint CTC/Attention E2E ASR with parallel streams represented by separate encoders aiming to capture diverse information. On top of the regular attention networks, the Hierarchical Attention Network (HAN) is introduced to steer the decoder toward the most informative encoders. A separate CTC network is assigned to each stream to force monotonic alignments. Two representative framework have been proposed and discussed, which are Multi-Encoder Multi-Resolution (MEM-Res) framework and Multi-Encoder Multi-Array (MEM-Array) framework, respectively. In MEM-Res framework, two heterogeneous encoders with different architectures, temporal resolutions and separate CTC networks work in parallel to extract complimentary information from same acoustics. Experiments are conducted on Wall Street Journal (WSJ) and CHiME-4, resulting in relative Word Error Rate (WER) reduction of 18.0-32.1% and the best WER of 3.6% in the WSJ eval92 test set. The MEM-Array framework aims at improving the far-field ASR robustness using multiple microphone arrays which are activated by separate encoders. Compared with the best single-array results, the proposed framework has achieved relative WER reduction of 3.7% and 9.7% in AMI and DIRHA multi-array corpora, respectively, which also outperforms conventional fusion strategies.

</details>

### [Real to H-space Encoder for Speech Recognition](1906.08043.md)
**Titouan Parcollet, Mohamed Morchid, Georges Linarès, Renato De Mori** · 2019-06-17

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) and more precisely recurrent neural networks (RNNs) are at the core of modern automatic speech recognition systems, due to their efficiency to process input sequences. Recently, it has been shown that different input representations, based on multidimensional algebras, such as complex and quaternion numbers, are able to bring to neural networks a more natural, compressive and powerful representation of the input signal by outperforming common real-valued NNs. Indeed, quaternion-valued neural networks (QNNs) better learn both internal dependencies, such as the relation between the Mel-filter-bank value of a specific time frame and its time derivatives, and global dependencies, describing the relations that exist between time frames. Nonetheless, QNNs are limited to quaternion-valued input signals, and it is difficult to benefit from this powerful representation with real-valued input data. This paper proposes to tackle this weakness by introducing a real-to-quaternion encoder that allows QNNs to process any one dimensional input features, such as traditional Mel-filter-banks for automatic speech recognition.

</details>

### [Adversarial Training for Multilingual Acoustic Modeling](1906.07093.md)
**Ke Hu, Hasim Sak, Hank Liao** · 2019-06-17

<details>
<summary>Abstract</summary>

Multilingual training has been shown to improve acoustic modeling performance by sharing and transferring knowledge in modeling different languages. Knowledge sharing is usually achieved by using common lower-level layers for different languages in a deep neural network. Recently, the domain adversarial network was proposed to reduce domain mismatch of training data and learn domain-invariant features. It is thus worth exploring whether adversarial training can further promote knowledge sharing in multilingual models. In this work, we apply the domain adversarial network to encourage the shared layers of a multilingual model to learn language-invariant features. Bidirectional Long Short-Term Memory (LSTM) recurrent neural networks (RNN) are used as building blocks. We show that shared layers learned this way contain less language identification information and lead to better performance. In an automatic speech recognition task for seven languages, the resultant acoustic model improves the word error rate (WER) of the multilingual model by 4% relative on average, and the monolingual models by 10%.

</details>

### [A Unified Framework of Constrained Robust Submodular Optimization with Applications](1906.06393.md)
**Rishabh Iyer** · 2019-06-14

<details>
<summary>Abstract</summary>

Robust optimization is becoming increasingly important in machine learning applications. In this paper, we study a unified framework of robust submodular optimization. We study this problem both from a minimization and maximization perspective (previous work has only focused on variants of robust submodular maximization). We do this under a broad range of combinatorial constraints including cardinality, knapsack, matroid as well as graph-based constraints such as cuts, paths, matchings and trees. Furthermore, we also study robust submodular minimization and maximization under multiple submodular upper and lower bound constraints. We show that all these problems are motivated by important machine learning applications including robust data subset selection, robust co-operative cuts and robust co-operative matchings. In each case, we provide scalable approximation algorithms and also study hardness bounds. Finally, we empirically demonstrate the utility of our algorithms on synthetic data, and real-world applications of robust cooperative matchings for image correspondence, robust data subset selection for speech recognition, and image collection summarization with multiple queries.

</details>

### [Cumulative Adaptation for BLSTM Acoustic Models](1906.06207.md)
**Markus Kitza, Pavel Golik, Ralf Schlüter, Hermann Ney** · 2019-06-14

<details>
<summary>Abstract</summary>

This paper addresses the robust speech recognition problem as an adaptation task. Specifically, we investigate the cumulative application of adaptation methods. A bidirectional Long Short-Term Memory (BLSTM) based neural network, capable of learning temporal relationships and translation invariant representations, is used for robust acoustic modelling. Further, i-vectors were used as an input to the neural network to perform instantaneous speaker and environment adaptation, providing 8\% relative improvement in word error rate on the NIST Hub5 2000 evaluation test set. By enhancing the first-pass i-vector based adaptation with a second-pass adaptation using speaker and environment dependent transformations within the network, a further relative improvement of 5\% in word error rate was achieved. We have reevaluated the features used to estimate i-vectors and their normalization to achieve the best performance in a modern large scale automatic speech recognition system.

</details>

### [Learning Video Representations using Contrastive Bidirectional Transformer](1906.05743.md)
**Chen Sun, Fabien Baradel, Kevin Murphy, Cordelia Schmid** · 2019-06-13

<details>
<summary>Abstract</summary>

This paper proposes a self-supervised learning approach for video features that results in significantly improved performance on downstream tasks (such as video classification, captioning and segmentation) compared to existing methods. Our method extends the BERT model for text sequences to the case of sequences of real-valued feature vectors, by replacing the softmax loss with noise contrastive estimation (NCE). We also show how to learn representations from sequences of visual features and sequences of words derived from ASR (automatic speech recognition), and show that such cross-modal training (when possible) helps even more.

</details>

### [Lattice Transformer for Speech Translation](1906.05551.md)
**Pei Zhang, Boxing Chen, Niyu Ge, Kai Fan** · 2019-06-13

<details>
<summary>Abstract</summary>

Recent advances in sequence modeling have highlighted the strengths of the transformer architecture, especially in achieving state-of-the-art machine translation results. However, depending on the up-stream systems, e.g., speech recognition, or word segmentation, the input to translation system can vary greatly. The goal of this work is to extend the attention mechanism of the transformer to naturally consume the lattice in addition to the traditional sequential input. We first propose a general lattice transformer for speech translation where the input is the output of the automatic speech recognition (ASR) which contains multiple paths and posterior scores. To leverage the extra information from the lattice structure, we develop a novel controllable lattice attention mechanism to obtain latent representations. On the LDC Spanish-English speech translation corpus, our experiments show that lattice transformer generalizes significantly better and outperforms both a transformer baseline and a lattice LSTM. Additionally, we validate our approach on the WMT 2017 Chinese-English translation task with lattice inputs from different BPE segmentations. In this task, we also observe the improvements over strong baselines.

</details>

### [Telephonetic: Making Neural Language Models Robust to ASR and Semantic Noise](1906.05678.md)
**Chris Larson, Tarek Lahlou, Diana Mingels, Zachary Kulis et al.** · 2019-06-13

<details>
<summary>Abstract</summary>

Speech processing systems rely on robust feature extraction to handle phonetic and semantic variations found in natural language. While techniques exist for desensitizing features to common noise patterns produced by Speech-to-Text (STT) and Text-to-Speech (TTS) systems, the question remains how to best leverage state-of-the-art language models (which capture rich semantic features, but are trained on only written text) on inputs with ASR errors. In this paper, we present Telephonetic, a data augmentation framework that helps robustify language model features to ASR corrupted inputs. To capture phonetic alterations, we employ a character-level language model trained using probabilistic masking. Phonetic augmentations are generated in two stages: a TTS encoder (Tacotron 2, WaveGlow) and a STT decoder (DeepSpeech). Similarly, semantic perturbations are produced by sampling from nearby words in an embedding space, which is computed using the BERT language model. Words are selected for augmentation according to a hierarchical grammar sampling strategy. Telephonetic is evaluated on the Penn Treebank (PTB) corpus, and demonstrates its effectiveness as a bootstrapping technique for transferring neural language models to the speech domain. Notably, our language model achieves a test perplexity of 37.49 on PTB, which to our knowledge is state-of-the-art among models trained only on PTB.

</details>

### [Word-level Speech Recognition with a Letter to Word Encoder](1906.04323.md)
**Ronan Collobert, Awni Hannun, Gabriel Synnaeve** · 2019-06-10

<details>
<summary>Abstract</summary>

We propose a direct-to-word sequence model which uses a word network to learn word embeddings from letters. The word network can be integrated seamlessly with arbitrary sequence models including Connectionist Temporal Classification and encoder-decoder models with attention. We show our direct-to-word model can achieve word error rate gains over sub-word level models for speech recognition. We also show that our direct-to-word approach retains the ability to predict words not seen at training time without any retraining. Finally, we demonstrate that a word-level model can use a larger stride than a sub-word level model while maintaining accuracy. This makes the model more efficient both for training and inference.

</details>

### [From Caesar Cipher to Unsupervised Learning: A New Method for Classifier Parameter Estimation](1906.02826.md)
**Yu Liu, Li Deng, Jianshu Chen, Chang Wen Chen** · 2019-06-06

<details>
<summary>Abstract</summary>

Many important classification problems, such as object classification, speech recognition, and machine translation, have been tackled by the supervised learning paradigm in the past, where training corpora of parallel input-output pairs are required with high cost. To remove the need for the parallel training corpora has practical significance for real-world applications, and it is one of the main goals of unsupervised learning. Recently, encouraging progress in unsupervised learning for solving such classification problems has been made and the nature of the challenges has been clarified. In this article, we review this progress and disseminate a class of promising new methods to facilitate understanding the methods for machine learning researchers. In particular, we emphasize the key information that enables the success of unsupervised learning - the sequential statistics as the distributional prior in the labels. Exploitation of such sequential statistics makes it possible to estimate parameters of classifiers without the need of paired input-output data. In this paper, we first introduce the concept of Caesar Cipher and its decryption, which motivated the construction of the novel loss function for unsupervised learning we use throughout the paper. Then we use a simple but representative binary classification task as an example to derive and describe the unsupervised learning algorithm in a step-by-step, easy-to-understand fashion. We include two cases, one with Bigram language model as the sequential statistics for use in unsupervised parameter estimation, and another with a simpler Unigram language model. For both cases, detailed derivation steps for the learning algorithm are included. Further, a summary table compares computational steps of the two cases in executing the unsupervised learning algorithm for learning binary classifiers.

</details>

### [When Does Label Smoothing Help?](1906.02629.md)
**Rafael Müller, Simon Kornblith, Geoffrey Hinton** · 2019-06-06

<details>
<summary>Abstract</summary>

The generalization and learning speed of a multi-class neural network can often be significantly improved by using soft targets that are a weighted average of the hard targets and the uniform distribution over labels. Smoothing the labels in this way prevents the network from becoming over-confident and label smoothing has been used in many state-of-the-art models, including image classification, language translation and speech recognition. Despite its widespread use, label smoothing is still poorly understood. Here we show empirically that in addition to improving generalization, label smoothing improves model calibration which can significantly improve beam-search. However, we also observe that if a teacher network is trained with label smoothing, knowledge distillation into a student network is much less effective. To explain these observations, we visualize how label smoothing changes the representations learned by the penultimate layer of the network. We show that label smoothing encourages the representations of training examples from the same class to group in tight clusters. This results in loss of information in the logits about resemblances between instances of different classes, which is necessary for distillation, but does not hurt generalization or calibration of the model's predictions.

</details>

### [Complex Evolution Recurrent Neural Networks (ceRNNs)](1906.02246.md)
**Izhak Shafran, Tom Bagby, R. J. Skerry-Ryan** · 2019-06-05

<details>
<summary>Abstract</summary>

Unitary Evolution Recurrent Neural Networks (uRNNs) have three attractive properties: (a) the unitary property, (b) the complex-valued nature, and (c) their efficient linear operators. The literature so far does not address -- how critical is the unitary property of the model? Furthermore, uRNNs have not been evaluated on large tasks. To study these shortcomings, we propose the complex evolution Recurrent Neural Networks (ceRNNs), which is similar to uRNNs but drops the unitary property selectively. On a simple multivariate linear regression task, we illustrate that dropping the constraints improves the learning trajectory. In copy memory task, ceRNNs and uRNNs perform identically, demonstrating that their superior performance over LSTMs is due to complex-valued nature and their linear operators. In a large scale real-world speech recognition, we find that pre-pending a uRNN degrades the performance of our baseline LSTM acoustic models, while pre-pending a ceRNN improves the performance over the baseline by 0.8% absolute WER.

</details>

### [Investigating the Lombard Effect Influence on End-to-End Audio-Visual Speech Recognition](1906.02112.md)
**Pingchuan Ma, Stavros Petridis, Maja Pantic** · 2019-06-05

<details>
<summary>Abstract</summary>

Several audio-visual speech recognition models have been recently proposed which aim to improve the robustness over audio-only models in the presence of noise. However, almost all of them ignore the impact of the Lombard effect, i.e., the change in speaking style in noisy environments which aims to make speech more intelligible and affects both the acoustic characteristics of speech and the lip movements. In this paper, we investigate the impact of the Lombard effect in audio-visual speech recognition. To the best of our knowledge, this is the first work which does so using end-to-end deep architectures and presents results on unseen speakers. Our results show that properly modelling Lombard speech is always beneficial. Even if a relatively small amount of Lombard speech is added to the training set then the performance in a real scenario, where noisy Lombard speech is present, can be significantly improved. We also show that the standard approach followed in the literature, where a model is trained and tested on noisy plain speech, provides a correct estimate of the video-only performance and slightly underestimates the audio-visual performance. In case of audio-only approaches, performance is overestimated for SNRs higher than -3dB and underestimated for lower SNRs.

</details>

### [Self-Attentional Models for Lattice Inputs](1906.01617.md)
**Matthias Sperber, Graham Neubig, Ngoc-Quan Pham, Alex Waibel** · 2019-06-04

<details>
<summary>Abstract</summary>

Lattices are an efficient and effective method to encode ambiguity of upstream systems in natural language processing tasks, for example to compactly capture multiple speech recognition hypotheses, or to represent multiple linguistic analyses. Previous work has extended recurrent neural networks to model lattice inputs and achieved improvements in various tasks, but these models suffer from very slow computation speeds. This paper extends the recently proposed paradigm of self-attention to handle lattice inputs. Self-attention is a sequence modeling technique that relates inputs to one another by computing pairwise similarities and has gained popularity for both its strong results and its computational efficiency. To extend such models to handle lattices, we introduce probabilistic reachability masks that incorporate lattice structure into the model and support lattice scores if available. We also propose a method for adapting positional embeddings to lattice structures. We apply the proposed model to a speech translation task and find that it outperforms all examined baselines while being much faster to compute than previous neural lattice models during both training and inference.

</details>

### [Listening while Speaking and Visualizing: Improving ASR through Multimodal Chain](1906.00579.md)
**Johanes Effendi, Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2019-06-03

<details>
<summary>Abstract</summary>

Previously, a machine speech chain, which is based on sequence-to-sequence deep learning, was proposed to mimic speech perception and production behavior. Such chains separately processed listening and speaking by automatic speech recognition (ASR) and text-to-speech synthesis (TTS) and simultaneously enabled them to teach each other in semi-supervised learning when they received unpaired data. Unfortunately, this speech chain study is limited to speech and textual modalities. In fact, natural communication is actually multimodal and involves both auditory and visual sensory systems. Although the said speech chain reduces the requirement of having a full amount of paired data, in this case we still need a large amount of unpaired data. In this research, we take a further step and construct a multimodal chain and design a closely knit chain architecture that combines ASR, TTS, image captioning, and image production models into a single framework. The framework allows the training of each component without requiring a large number of parallel multimodal data. Our experimental results also show that an ASR can be further trained without speech and text data and cross-modal data augmentation remains possible through our proposed chain, which improves the ASR performance.

</details>

### [Fluent Translations from Disfluent Speech in End-to-End Speech Translation](1906.00556.md)
**Elizabeth Salesky, Matthias Sperber, Alex Waibel** · 2019-06-03

<details>
<summary>Abstract</summary>

Spoken language translation applications for speech suffer due to conversational speech phenomena, particularly the presence of disfluencies. With the rise of end-to-end speech translation models, processing steps such as disfluency removal that were previously an intermediate step between speech recognition and machine translation need to be incorporated into model architectures. We use a sequence-to-sequence model to translate from noisy, disfluent speech to fluent text with disfluencies removed using the recently collected `copy-edited' references for the Fisher Spanish-English dataset. We are able to directly generate fluent translations and introduce considerations about how to evaluate success on this task. This work provides a baseline for a new task, the translation of conversational speech with joint removal of disfluencies.

</details>

### [Lattice-based lightly-supervised acoustic model training](1905.13150.md)
**Joachim Fainberg, Ondřej Klejch, Steve Renals, Peter Bell** · 2019-05-30

<details>
<summary>Abstract</summary>

In the broadcast domain there is an abundance of related text data and partial transcriptions, such as closed captions and subtitles. This text data can be used for lightly supervised training, in which text matching the audio is selected using an existing speech recognition model. Current approaches to light supervision typically filter the data based on matching error rates between the transcriptions and biased decoding hypotheses. In contrast, semi-supervised training does not require matching text data, instead generating a hypothesis using a background language model. State-of-the-art semi-supervised training uses lattice-based supervision with the lattice-free MMI (LF-MMI) objective function. We propose a technique to combine inaccurate transcriptions with the lattices generated for semi-supervised training, thus preserving uncertainty in the lattice where appropriate. We demonstrate that this combined approach reduces the expected error rates over the lattices, and reduces the word error rate (WER) on a broadcast task.

</details>

### [Regularization Advantages of Multilingual Neural Language Models for Low Resource Domains](1906.01496.md)
**Navid Rekabsaz, Nikolaos Pappas, James Henderson, Banriskhem K. Khonglah et al.** · 2019-05-29

<details>
<summary>Abstract</summary>

Neural language modeling (LM) has led to significant improvements in several applications, including Automatic Speech Recognition. However, they typically require large amounts of training data, which is not available for many domains and languages. In this study, we propose a multilingual neural language model architecture, trained jointly on the domain-specific data of several low-resource languages. The proposed multilingual LM consists of language specific word embeddings in the encoder and decoder, and one language specific LSTM layer, plus two LSTM layers with shared parameters across the languages. This multilingual LM model facilitates transfer learning across the languages, acting as an extra regularizer in very low-resource scenarios. We integrate our proposed multilingual approach with a state-of-the-art highly-regularized neural LM, and evaluate on the conversational data domain for four languages over a range of training data sizes. Compared to monolingual LMs, the results show significant improvements of our proposed multilingual LM when the amount of available training data is limited, indicating the advantages of cross-lingual parameter sharing in very low-resource language modeling.

</details>

### [Rethinking Full Connectivity in Recurrent Neural Networks](1905.12340.md)
**Matthijs Van Keirsbilck, Alexander Keller, Xiaodong Yang** · 2019-05-29

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) are omnipresent in sequence modeling tasks. Practical models usually consist of several layers of hundreds or thousands of neurons which are fully connected. This places a heavy computational and memory burden on hardware, restricting adoption in practical low-cost and low-power devices. Compared to fully convolutional models, the costly sequential operation of RNNs severely hinders performance on parallel hardware. This paper challenges the convention of full connectivity in RNNs. We study structurally sparse RNNs, showing that they are well suited for acceleration on parallel hardware, with a greatly reduced cost of the recurrent operations as well as orders of magnitude less recurrent weights. Extensive experiments on challenging tasks ranging from language modeling and speech recognition to video action recognition reveal that structurally sparse RNNs achieve competitive performance as compared to fully-connected networks. This allows for using large sparse RNNs for a wide range of real-world tasks that previously were too costly with fully connected networks.

</details>

### [A Study of BFLOAT16 for Deep Learning Training](1905.12322.md)
**Dhiraj Kalamkar, Dheevatsa Mudigere, Naveen Mellempudi, Dipankar Das et al.** · 2019-05-29

<details>
<summary>Abstract</summary>

This paper presents the first comprehensive empirical study demonstrating the efficacy of the Brain Floating Point (BFLOAT16) half-precision format for Deep Learning training across image classification, speech recognition, language modeling, generative networks and industrial recommendation systems. BFLOAT16 is attractive for Deep Learning training for two reasons: the range of values it can represent is the same as that of IEEE 754 floating-point format (FP32) and conversion to/from FP32 is simple. Maintaining the same range as FP32 is important to ensure that no hyper-parameter tuning is required for convergence; e.g., IEEE 754 compliant half-precision floating point (FP16) requires hyper-parameter tuning. In this paper, we discuss the flow of tensors and various key operations in mixed precision training, and delve into details of operations, such as the rounding modes for converting FP32 tensors to BFLOAT16. We have implemented a method to emulate BFLOAT16 operations in Tensorflow, Caffe2, IntelCaffe, and Neon for our experiments. Our results show that deep learning training using BFLOAT16 tensors achieves the same state-of-the-art (SOTA) results across domains as FP32 tensors in the same number of iterations and with no changes to hyper-parameters.

</details>

### [Inference with Hybrid Bio-hardware Neural Networks](1905.11594.md)
**Yuan Zeng, Zubayer Ibne Ferdous, Weixiang Zhang, Mufan Xu et al.** · 2019-05-28

<details>
<summary>Abstract</summary>

To understand the learning process in brains, biologically plausible algorithms have been explored by modeling the detailed neuron properties and dynamics. On the other hand, simplified multi-layer models of neural networks have shown great success on computational tasks such as image classification and speech recognition. However, the computational models that can achieve good accuracy for these learning applications are very different from the bio-plausible models. This paper studies whether a bio-plausible model of a in vitro living neural network can be used to perform machine learning tasks and achieve good inference accuracy. A novel two-layer bio-hardware hybrid neural network is proposed. The biological layer faithfully models variations of synapses, neurons, and network sparsity in in vitro living neural networks. The hardware layer is a computational fully-connected layer that tunes parameters to optimize for accuracy. Several techniques are proposed to improve the inference accuracy of the proposed hybrid neural network. For instance, an adaptive pre-processing technique helps the proposed neural network to achieve good learning accuracy for different living neural network sparsity. The proposed hybrid neural network with realistic neuron parameters and variations achieves a 98.3% testing accuracy for the handwritten digit recognition task on the full MNIST dataset.

</details>

### [A Cost Efficient Approach to Correct OCR Errors in Large Document Collections](1905.11739.md)
**Deepayan Das, Jerin Philip, Minesh Mathew, C. V. Jawahar** · 2019-05-28

<details>
<summary>Abstract</summary>

Word error rate of an ocr is often higher than its character error rate. This is especially true when ocrs are designed by recognizing characters. High word accuracies are critical to tasks like the creation of content in digital libraries and text-to-speech applications. In order to detect and correct the misrecognised words, it is common for an ocr module to employ a post-processor to further improve the word accuracy. However, conventional approaches to post-processing like looking up a dictionary or using a statistical language model (slm), are still limited. In many such scenarios, it is often required to remove the outstanding errors manually. We observe that the traditional post-processing schemes look at error words sequentially since ocrs process documents one at a time. We propose a cost-efficient model to address the error words in batches rather than correcting them individually. We exploit the fact that a collection of documents, unlike a single document, has a structure leading to repetition of words. Such words, if efficiently grouped together and corrected as a whole can lead to a significant reduction in the cost. Correction can be fully automatic or with a human in the loop. Towards this, we employ a novel clustering scheme to obtain fairly homogeneous clusters. We compare the performance of our model with various baseline approaches including the case where all the errors are removed by a human. We demonstrate the efficacy of our solution empirically by reporting more than 70% reduction in the human effort with near perfect error correction. We validate our method on Books from multiple languages.

</details>

### [Stochastic Gradient Methods with Layer-wise Adaptive Moments for Training of Deep Networks](1905.11286.md)
**Boris Ginsburg, Patrice Castonguay, Oleksii Hrinchuk, Oleksii Kuchaiev et al.** · 2019-05-27

<details>
<summary>Abstract</summary>

We propose NovoGrad, an adaptive stochastic gradient descent method with layer-wise gradient normalization and decoupled weight decay. In our experiments on neural networks for image classification, speech recognition, machine translation, and language modeling, it performs on par or better than well tuned SGD with momentum and Adam or AdamW. Additionally, NovoGrad (1) is robust to the choice of learning rate and weight initialization, (2) works well in a large batch setting, and (3) has two times smaller memory footprint than Adam.

</details>

### [CIF: Continuous Integrate-and-Fire for End-to-End Speech Recognition](1905.11235.md)
**Linhao Dong, Bo Xu** · 2019-05-27

<details>
<summary>Abstract</summary>

In this paper, we propose a novel soft and monotonic alignment mechanism used for sequence transduction. It is inspired by the integrate-and-fire model in spiking neural networks and employed in the encoder-decoder framework consists of continuous functions, thus being named as: Continuous Integrate-and-Fire (CIF). Applied to the ASR task, CIF not only shows a concise calculation, but also supports online recognition and acoustic boundary positioning, thus suitable for various ASR scenarios. Several support strategies are also proposed to alleviate the unique problems of CIF-based model. With the joint action of these methods, the CIF-based model shows competitive performance. Notably, it achieves a word error rate (WER) of 2.86% on the test-clean of Librispeech and creates new state-of-the-art result on Mandarin telephone ASR benchmark.

</details>

### [A collaborative filtering model with heterogeneous neural networks for recommender systems](1905.11133.md)
**Ge Fan, Wei Zeng, Shan Sun, Biao Geng et al.** · 2019-05-27

<details>
<summary>Abstract</summary>

In recent years, deep neural network is introduced in recommender systems to solve the collaborative filtering problem, which has achieved immense success on computer vision, speech recognition and natural language processing. On one hand, deep neural network can be used to model the auxiliary information in recommender systems. On the other hand, it is also capable of modeling nonlinear relationships between users and items. One advantage of deep neural network is that the performance of the algorithm can be easily enhanced by augmenting the depth of the neural network. However, two potential problems may emerge when the deep neural work is exploited to model relationships between users and items. The fundamental problem is that the complexity of the algorithm grows significantly with the increment in the depth of the neural network. The second one is that a deeper neural network may undermine the accuracy of the algorithm. In order to alleviate these problems, we propose a hybrid neural network that combines heterogeneous neural networks with different structures. The experimental results on real datasets reveal that our method is superior to the state-of-the-art methods in terms of the item ranking.

</details>

### [NTP : A Neural Network Topology Profiler](1905.09063.md)
**Raghavendra Bhat, Pravin Chandran, Juby Jose, Viswanath Dibbur et al.** · 2019-05-22

<details>
<summary>Abstract</summary>

Performance of end-to-end neural networks on a given hardware platform is a function of its compute and memory signature, which in-turn, is governed by a wide range of parameters such as topology size, primitives used, framework used, batching strategy, latency requirements, precision etc. Current benchmarking tools suffer from limitations such as a) being either too granular like DeepBench [1] (or) b) mandate a working implementation that is either framework specific or hardware-architecture specific or both (or) c) provide only high level benchmark metrics. In this paper, we present NTP (Neural Net Topology Profiler), a sophisticated benchmarking framework, to effectively identify memory and compute signature of an end-to-end topology on multiple hardware architectures, without the need for an actual implementation. NTP is tightly integrated with hardware specific benchmarking tools to enable exhaustive data collection and analysis. Using NTP, a deep learning researcher can quickly establish baselines needed to understand performance of an end-to-end neural network topology and make high level architectural decisions. Further, integration of NTP with frameworks like Tensorflow, Pytorch, Intel OpenVINO etc. allows for performance comparison along several vectors like a) Comparison of different frameworks on a given hardware b) Comparison of different hardware using a given framework c) Comparison across different heterogeneous hardware configurations for given framework etc. These capabilities empower a researcher to effortlessly make architectural decisions needed for achieving optimized performance on any hardware platform. The paper documents the architectural approach of NTP and demonstrates the capabilities of the tool by benchmarking Mozilla DeepSpeech, a popular Speech Recognition topology.

</details>

### [Acoustic-to-Word Models with Conversational Context Information](1905.08796.md)
**Suyoun Kim, Florian Metze** · 2019-05-21

<details>
<summary>Abstract</summary>

Conversational context information, higher-level knowledge that spans across sentences, can help to recognize a long conversation. However, existing speech recognition models are typically built at a sentence level, and thus it may not capture important conversational context information. The recent progress in end-to-end speech recognition enables integrating context with other available information (e.g., acoustic, linguistic resources) and directly recognizing words from speech. In this work, we present a direct acoustic-to-word, end-to-end speech recognition model capable of utilizing the conversational context to better process long conversations. We evaluate our proposed approach on the Switchboard conversational speech corpus and show that our system outperforms a standard end-to-end speech recognition system.

</details>

### [End-to-end Adaptation with Backpropagation through WFST for On-device Speech Recognition System](1905.07149.md)
**Emiru Tsunoo, Yosuke Kashiwagi, Satoshi Asakawa, Toshiyuki Kumakura** · 2019-05-17

<details>
<summary>Abstract</summary>

An on-device DNN-HMM speech recognition system efficiently works with a limited vocabulary in the presence of a variety of predictable noise. In such a case, vocabulary and environment adaptation is highly effective. In this paper, we propose a novel method of end-to-end (E2E) adaptation, which adjusts not only an acoustic model (AM) but also a weighted finite-state transducer (WFST). We convert a pretrained WFST to a trainable neural network and adapt the system to target environments/vocabulary by E2E joint training with an AM. We replicate Viterbi decoding with forward--backward neural network computation, which is similar to recurrent neural networks (RNNs). By pooling output score sequences, a vocabulary posterior for each utterance is obtained and used for discriminative loss computation. Experiments using 2--10 hours of English/Japanese adaptation datasets indicate that the fine-tuning of only WFSTs and that of only AMs are both comparable to a state-of-the-art adaptation method, and E2E joint training of the two components achieves the best recognition performance. We also adapt each language system to the other language using the adaptation data, and the results show that the proposed method also works well for language adaptations.

</details>

### [The Audio Auditor: User-Level Membership Inference in Internet of Things Voice Services](1905.07082.md)
**Yuantian Miao, Minhui Xue, Chao Chen, Lei Pan et al.** · 2019-05-17

<details>
<summary>Abstract</summary>

With the rapid development of deep learning techniques, the popularity of voice services implemented on various Internet of Things (IoT) devices is ever increasing. In this paper, we examine user-level membership inference in the problem space of voice services, by designing an audio auditor to verify whether a specific user had unwillingly contributed audio used to train an automatic speech recognition (ASR) model under strict black-box access. With user representation of the input audio data and their corresponding translated text, our trained auditor is effective in user-level audit. We also observe that the auditor trained on specific data can be generalized well regardless of the ASR model architecture. We validate the auditor on ASR models trained with LSTM, RNNs, and GRU algorithms on two state-of-the-art pipelines, the hybrid ASR system and the end-to-end ASR system. Finally, we conduct a real-world trial of our auditor on iPhone Siri, achieving an overall accuracy exceeding 80\%. We hope the methodology developed in this paper and findings can inform privacy advocates to overhaul IoT privacy.

</details>

### [Effective Sentence Scoring Method using Bidirectional Language Model for Speech Recognition](1905.06655.md)
**Joongbo Shin, Yoonhyung Lee, Kyomin Jung** · 2019-05-16

<details>
<summary>Abstract</summary>

In automatic speech recognition, many studies have shown performance improvements using language models (LMs). Recent studies have tried to use bidirectional LMs (biLMs) instead of conventional unidirectional LMs (uniLMs) for rescoring the $N$-best list decoded from the acoustic model. In spite of their theoretical benefits, the biLMs have not given notable improvements compared to the uniLMs in their experiments. This is because their biLMs do not consider the interaction between the two directions. In this paper, we propose a novel sentence scoring method considering the interaction between the past and the future words on the biLM. Our experimental results on the LibriSpeech corpus show that the biLM with the proposed sentence scoring outperforms the uniLM for the $N$-best list rescoring, consistently and significantly in all experimental conditions. The analysis of WERs by word position demonstrates that the biLM is more robust than the uniLM especially when a recognized sentence is short or a misrecognized word is at the beginning of the sentence.

</details>

### [Learning discriminative features in sequence training without requiring framewise labelled data](1905.06907.md)
**Jun Wang, Dan Su, Jie Chen, Shulin Feng et al.** · 2019-05-16

<details>
<summary>Abstract</summary>

In this work, we try to answer two questions: Can deeply learned features with discriminative power benefit an ASR system's robustness to acoustic variability? And how to learn them without requiring framewise labelled sequence training data? As existing methods usually require knowing where the labels occur in the input sequence, they have so far been limited to many real-world sequence learning tasks. We propose a novel method which simultaneously models both the sequence discriminative training and the feature discriminative learning within a single network architecture, so that it can learn discriminative deep features in sequence training that obviates the need for presegmented training data. Our experiment in a realistic industrial ASR task shows that, without requiring any specific fine-tuning or additional complexity, our proposed models have consistently outperformed state-of-the-art models and significantly reduced Word Error Rate (WER) under all test conditions, and especially with highest improvements under unseen noise conditions, by relative 12.94%, 8.66% and 5.80%, showing our proposed models can generalize better to acoustic variability.

</details>

### [Speaker-Independent Speech-Driven Visual Speech Synthesis using Domain-Adapted Acoustic Models](1905.06860.md)
**Ahmed Hussen Abdelaziz, Barry-John Theobald, Justin Binder, Gabriele Fanelli et al.** · 2019-05-15

<details>
<summary>Abstract</summary>

Speech-driven visual speech synthesis involves mapping features extracted from acoustic speech to the corresponding lip animation controls for a face model. This mapping can take many forms, but a powerful approach is to use deep neural networks (DNNs). However, a limitation is the lack of synchronized audio, video, and depth data required to reliably train the DNNs, especially for speaker-independent models. In this paper, we investigate adapting an automatic speech recognition (ASR) acoustic model (AM) for the visual speech synthesis problem. We train the AM on ten thousand hours of audio-only data. The AM is then adapted to the visual speech synthesis domain using ninety hours of synchronized audio-visual speech. Using a subjective assessment test, we compared the performance of the AM-initialized DNN to one with a random initialization. The results show that viewers significantly prefer animations generated from the AM-initialized DNN than the ones generated using the randomly initialized model. We conclude that visual speech synthesis can significantly benefit from the powerful representation of speech in the ASR acoustic models.

</details>

### [End to End Recognition System for Recognizing Offline Unconstrained Vietnamese Handwriting](1905.05381.md)
**Anh Duc Le, Hung Tuan Nguyen, Masaki Nakagawa** · 2019-05-14

<details>
<summary>Abstract</summary>

Inspired by recent successes in neural machine translation and image caption generation, we present an attention based encoder decoder model (AED) to recognize Vietnamese Handwritten Text. The model composes of two parts: a DenseNet for extracting invariant features, and a Long Short-Term Memory network (LSTM) with an attention model incorporated for generating output text (LSTM decoder), which are connected from the CNN part to the attention model. The input of the CNN part is a handwritten text image and the target of the LSTM decoder is the corresponding text of the input image. Our model is trained end-to-end to predict the text from a given input image since all the parts are differential components. In the experiment section, we evaluate our proposed AED model on the VNOnDB-Word and VNOnDB-Line datasets to verify its efficiency. The experiential results show that our model achieves 12.30% of word error rate without using any language model. This result is competitive with the handwriting recognition system provided by Google in the Vietnamese Online Handwritten Text Recognition competition.

</details>

### [Almost Unsupervised Text to Speech and Automatic Speech Recognition](1905.06791.md)
**Yi Ren, Xu Tan, Tao Qin, Sheng Zhao et al.** · 2019-05-13

<details>
<summary>Abstract</summary>

Text to speech (TTS) and automatic speech recognition (ASR) are two dual tasks in speech processing and both achieve impressive performance thanks to the recent advance in deep learning and large amount of aligned speech and text data. However, the lack of aligned data poses a major practical problem for TTS and ASR on low-resource languages. In this paper, by leveraging the dual nature of the two tasks, we propose an almost unsupervised learning method that only leverages few hundreds of paired data and extra unpaired data for TTS and ASR. Our method consists of the following components: (1) a denoising auto-encoder, which reconstructs speech and text sequences respectively to develop the capability of language modeling both in speech and text domain; (2) dual transformation, where the TTS model transforms the text $y$ into speech $\hat{x}$, and the ASR model leverages the transformed pair $(\hat{x},y)$ for training, and vice versa, to boost the accuracy of the two tasks; (3) bidirectional sequence modeling, which addresses error propagation especially in the long speech and text sequence when training with few paired data; (4) a unified model structure, which combines all the above components for TTS and ASR based on Transformer model. Our method achieves 99.84% in terms of word level intelligible rate and 2.68 MOS for TTS, and 11.7% PER for ASR on LJSpeech dataset, by leveraging only 200 paired speech and text data (about 20 minutes audio), together with extra unpaired speech and text data.

</details>

### [Encrypted Speech Recognition using Deep Polynomial Networks](1905.05605.md)
**Shi-Xiong Zhang, Yifan Gong, Dong Yu** · 2019-05-11

<details>
<summary>Abstract</summary>

The cloud-based speech recognition/API provides developers or enterprises an easy way to create speech-enabled features in their applications. However, sending audios about personal or company internal information to the cloud, raises concerns about the privacy and security issues. The recognition results generated in cloud may also reveal some sensitive information. This paper proposes a deep polynomial network (DPN) that can be applied to the encrypted speech as an acoustic model. It allows clients to send their data in an encrypted form to the cloud to ensure that their data remains confidential, at mean while the DPN can still make frame-level predictions over the encrypted speech and return them in encrypted form. One good property of the DPN is that it can be trained on unencrypted speech features in the traditional way. To keep the cloud away from the raw audio and recognition results, a cloud-local joint decoding framework is also proposed. We demonstrate the effectiveness of model and framework on the Switchboard and Cortana voice assistant tasks with small performance degradation and latency increased comparing with the traditional cloud-based DNNs.

</details>

### [Language Modeling with Deep Transformers](1905.04226.md)
**Kazuki Irie, Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2019-05-10

<details>
<summary>Abstract</summary>

We explore deep autoregressive Transformer models in language modeling for speech recognition. We focus on two aspects. First, we revisit Transformer model configurations specifically for language modeling. We show that well configured Transformer models outperform our baseline models based on the shallow stack of LSTM recurrent neural network layers. We carry out experiments on the open-source LibriSpeech 960hr task, for both 200K vocabulary word-level and 10K byte-pair encoding subword-level language modeling. We apply our word-level models to conventional hybrid speech recognition by lattice rescoring, and the subword-level models to attention based encoder-decoder models by shallow fusion. Second, we show that deep Transformer language models do not require positional encoding. The positional encoding is an essential augmentation for the self-attention mechanism which is invariant to sequence ordering. However, in autoregressive setup, as is the case for language modeling, the amount of information increases along the position dimension, which is a positional signal by its own. The analysis of attention weights shows that deep autoregressive self-attention models can automatically make use of such positional information. We find that removing the positional encoding even slightly improves the performance of these models.

</details>

### [Role of non-linear data processing on speech recognition task in the framework of reservoir computing](1906.02812.md)
**Flavio Abreu Araujo, Mathieu Riou, Jacob Torrejon, Sumito Tsunegi et al.** · 2019-05-10

<details>
<summary>Abstract</summary>

The reservoir computing neural network architecture is widely used to test hardware systems for neuromorphic computing. One of the preferred tasks for bench-marking such devices is automatic speech recognition. However, this task requires acoustic transformations from sound waveforms with varying amplitudes to frequency domain maps that can be seen as feature extraction techniques. Depending on the conversion method, these may obscure the contribution of the neuromorphic hardware to the overall speech recognition performance. Here, we quantify and separate the contributions of the acoustic transformations and the neuromorphic hardware to the speech recognition success rate. We show that the non-linearity in the acoustic transformation plays a critical role in feature extraction. We compute the gain in word success rate provided by a reservoir computing device compared to the acoustic transformation only, and show that it is an appropriate benchmark for comparing different hardware. Finally, we experimentally and numerically quantify the impact of the different acoustic transformations for neuromorphic hardware based on magnetic nano-oscillators.

</details>

### [MobiVSR: A Visual Speech Recognition Solution for Mobile Devices](1905.03968.md)
**Nilay Shrivastava, Astitwa Saxena, Yaman Kumar, Rajiv Ratn Shah et al.** · 2019-05-10

<details>
<summary>Abstract</summary>

Visual speech recognition (VSR) is the task of recognizing spoken language from video input only, without any audio. VSR has many applications as an assistive technology, especially if it could be deployed in mobile devices and embedded systems. The need of intensive computational resources and large memory footprint are two of the major obstacles in developing neural network models for VSR in a resource constrained environment. We propose a novel end-to-end deep neural network architecture for word level VSR called MobiVSR with a design parameter that aids in balancing the model's accuracy and parameter count. We use depthwise-separable 3D convolution for the first time in the domain of VSR and show how it makes our model efficient. MobiVSR achieves an accuracy of 73\% on a challenging Lip Reading in the Wild dataset with 6 times fewer parameters and 20 times lesser memory footprint than the current state of the art. MobiVSR can also be compressed to 6 MB by applying post training quantization.

</details>

### [Analysis of Deep Clustering as Preprocessing for Automatic Speech Recognition of Sparsely Overlapping Speech](1905.03500.md)
**Tobias Menne, Ilya Sklyar, Ralf Schlüter, Hermann Ney** · 2019-05-09

<details>
<summary>Abstract</summary>

Significant performance degradation of automatic speech recognition (ASR) systems is observed when the audio signal contains cross-talk. One of the recently proposed approaches to solve the problem of multi-speaker ASR is the deep clustering (DPCL) approach. Combining DPCL with a state-of-the-art hybrid acoustic model, we obtain a word error rate (WER) of 16.5 % on the commonly used wsj0-2mix dataset, which is the best performance reported thus far to the best of our knowledge. The wsj0-2mix dataset contains simulated cross-talk where the speech of multiple speakers overlaps for almost the entire utterance. In a more realistic ASR scenario the audio signal contains significant portions of single-speaker speech and only part of the signal contains speech of multiple competing speakers. This paper investigates obstacles of applying DPCL as a preprocessing method for ASR in such a scenario of sparsely overlapping speech. To this end we present a data simulation approach, closely related to the wsj0-2mix dataset, generating sparsely overlapping speech datasets of arbitrary overlap ratio. The analysis of applying DPCL to sparsely overlapping speech is an important interim step between the fully overlapping datasets like wsj0-2mix and more realistic ASR datasets, such as CHiME-5 or AMI.

</details>

### [A Hardware-Oriented and Memory-Efficient Method for CTC Decoding](1905.03175.md)
**Siyuan Lu, Jinming Lu, Jun Lin, Zhongfeng Wang** · 2019-05-08

<details>
<summary>Abstract</summary>

The Connectionist Temporal Classification (CTC) has achieved great success in sequence to sequence analysis tasks such as automatic speech recognition (ASR) and scene text recognition (STR). These applications can use the CTC objective function to train the recurrent neural networks (RNNs), and decode the outputs of RNNs during inference. While hardware architectures for RNNs have been studied, hardware-based CTCdecoders are desired for high-speed CTC-based inference systems. This paper, for the first time, provides a low-complexity and memory-efficient approach to build a CTC-decoder based on the beam search decoding. Firstly, we improve the beam search decoding algorithm to save the storage space. Secondly, we compress a dictionary (reduced from 26.02MB to 1.12MB) and use it as the language model. Meanwhile searching this dictionary is trivial. Finally, a fixed-point CTC-decoder for an English ASR and an STR task using the proposed method is implemented with C++ language. It is shown that the proposed method has little precision loss compared with its floating-point counterpart. Our experiments demonstrate the compression ratio of the storage required by the proposed beam search decoding algorithm are 29.49 (ASR) and 17.95 (STR).

</details>

### [RWTH ASR Systems for LibriSpeech: Hybrid vs Attention -- w/o Data Augmentation](1905.03072.md)
**Christoph Lüscher, Eugen Beck, Kazuki Irie, Markus Kitza et al.** · 2019-05-08

<details>
<summary>Abstract</summary>

We present state-of-the-art automatic speech recognition (ASR) systems employing a standard hybrid DNN/HMM architecture compared to an attention-based encoder-decoder design for the LibriSpeech task. Detailed descriptions of the system development, including model design, pretraining schemes, training schedules, and optimization approaches are provided for both system architectures. Both hybrid DNN/HMM and attention-based systems employ bi-directional LSTMs for acoustic modeling/encoding. For language modeling, we employ both LSTM and Transformer based architectures. All our systems are built using RWTHs open-source toolkits RASR and RETURNN. To the best knowledge of the authors, the results obtained when training on the full LibriSpeech training set, are the best published currently, both for the hybrid DNN/HMM and the attention-based systems. Our single hybrid system even outperforms previous results obtained from combining eight single systems. Our comparison shows that on the LibriSpeech 960h task, the hybrid DNN/HMM system outperforms the attention-based system by 15% relative on the clean and 40% relative on the other test sets in terms of word error rate. Moreover, experiments on a reduced 100h-subset of the LibriSpeech training corpus even show a more pronounced margin between the hybrid DNN/HMM and attention-based architectures.

</details>

### [Learning Optimal Data Augmentation Policies via Bayesian Optimization for Image Classification Tasks](1905.02610.md)
**Chunxu Zhang, Jiaxu Cui, Bo Yang** · 2019-05-06

<details>
<summary>Abstract</summary>

In recent years, deep learning has achieved remarkable achievements in many fields, including computer vision, natural language processing, speech recognition and others. Adequate training data is the key to ensure the effectiveness of the deep models. However, obtaining valid data requires a lot of time and labor resources. Data augmentation (DA) is an effective alternative approach, which can generate new labeled data based on existing data using label-preserving transformations. Although we can benefit a lot from DA, designing appropriate DA policies requires a lot of expert experience and time consumption, and the evaluation of searching the optimal policies is costly. So we raise a new question in this paper: how to achieve automated data augmentation at as low cost as possible? We propose a method named BO-Aug for automating the process by finding the optimal DA policies using the Bayesian optimization approach. Our method can find the optimal policies at a relatively low search cost, and the searched policies based on a specific dataset are transferable across different neural network architectures or even different datasets. We validate the BO-Aug on three widely used image classification datasets, including CIFAR-10, CIFAR-100 and SVHN. Experimental results show that the proposed method can achieve state-of-the-art or near advanced classification accuracy. Code to reproduce our experiments is available at https://github.com/zhangxiaozao/BO-Aug.

</details>

### [Parity Models: A General Framework for Coding-Based Resilience in ML Inference](1905.00863.md)
**Jack Kosaian, K. V. Rashmi, Shivaram Venkataraman** · 2019-05-02

<details>
<summary>Abstract</summary>

Machine learning models are becoming the primary workhorses for many applications. Production services deploy models through prediction serving systems that take in queries and return predictions by performing inference on machine learning models. In order to scale to high query rates, prediction serving systems are run on many machines in cluster settings, and thus are prone to slowdowns and failures that inflate tail latency and cause violations of strict latency targets. Current approaches to reducing tail latency are inadequate for the latency targets of prediction serving, incur high resource overhead, or are inapplicable to the computations performed during inference. We present ParM, a novel, general framework for making use of ideas from erasure coding and machine learning to achieve low-latency, resource-efficient resilience to slowdowns and failures in prediction serving systems. ParM encodes multiple queries together into a single parity query and performs inference on the parity query using a parity model. A decoder uses the output of a parity model to reconstruct approximations of unavailable predictions. ParM uses neural networks to learn parity models that enable simple, fast encoders and decoders to reconstruct unavailable predictions for a variety of inference tasks such as image classification, speech recognition, and object localization. We build ParM atop an open-source prediction serving system and through extensive evaluation show that ParM improves overall accuracy in the face of unavailability with low latency while using 2-4$\times$ less additional resources than replication-based approaches. ParM reduces the gap between 99.9th percentile and median latency by up to $3.5\times$ compared to approaches that use an equal amount of resources, while maintaining the same median.

</details>

### [An Investigation of Multilingual ASR Using End-to-end LF-MMI](s2:051117cc4342a3b6613e1354b48273edf9aaf679.md)
**Sibo Tong, Philip N. Garner, H. Bourlard** · 2019-05-01

<details>
<summary>Abstract</summary>

The end-to-end lattice-free maximum mutual information (LF-MMI) approach has recently been shown to be beneficial for automatic speech recognition (ASR) in general. More specifically, its end-to-end nature and use of context independent phone labels make it attractive for multilingual ASR. We show that end-to-end LF-MMI is indeed competitive on a low-resourced multilingual task, comfortably outperforming a connectionist temporal classification (CTC) baseline. We further investigate the feasibility of biphone contexts, being a candidate compromise between the context independent approach and the triphone contexts that usually perform well. We show that biphones do not initially perform well, but can do so after language adaptive training, concluding that biphones carry language variability but are promising for multilingual ASR.

</details>

### [Deep Learning for Audio Signal Processing](1905.00078.md)
**Hendrik Purwins, Bo Li, Tuomas Virtanen, Jan Schlüter et al.** · 2019-04-30

<details>
<summary>Abstract</summary>

Given the recent surge in developments of deep learning, this article provides a review of the state-of-the-art deep learning techniques for audio signal processing. Speech, music, and environmental sound processing are considered side-by-side, in order to point out similarities and differences between the domains, highlighting general methods, problems, key references, and potential for cross-fertilization between areas. The dominant feature representations (in particular, log-mel spectra and raw waveform) and deep learning models are reviewed, including convolutional neural networks, variants of the long short-term memory architecture, as well as more audio-specific neural network models. Subsequently, prominent deep learning application areas are covered, i.e. audio recognition (automatic speech recognition, music information retrieval, environmental sound detection, localization and tracking) and synthesis and transformation (source separation, audio enhancement, generative models for speech, sound, and music synthesis). Finally, key issues and future questions regarding deep learning applied to audio signal processing are identified.

</details>

### [Very Deep Self-Attention Networks for End-to-End Speech Recognition](1904.13377.md)
**Ngoc-Quan Pham, Thai-Son Nguyen, Jan Niehues, Markus Müller et al.** · 2019-04-30

<details>
<summary>Abstract</summary>

Recently, end-to-end sequence-to-sequence models for speech recognition have gained significant interest in the research community. While previous architecture choices revolve around time-delay neural networks (TDNN) and long short-term memory (LSTM) recurrent neural networks, we propose to use self-attention via the Transformer architecture as an alternative. Our analysis shows that deep Transformer networks with high learning capacity are able to exceed performance from previous end-to-end approaches and even match the conventional hybrid systems. Moreover, we trained very deep models with up to 48 Transformer layers for both encoder and decoders combined with stochastic residual connections, which greatly improve generalizability and training efficiency. The resulting models outperform all previous end-to-end ASR approaches on the Switchboard benchmark. An ensemble of these models achieve 9.9% and 17.7% WER on Switchboard and CallHome test sets respectively. This finding brings our end-to-end models to competitive levels with previous hybrid systems. Further, with model ensembling the Transformers can outperform certain hybrid systems, which are more complicated in terms of both structure and training procedure.

</details>

### [Semi-supervised Sequence-to-sequence ASR using Unpaired Speech and Text](1905.01152.md)
**Murali Karthick Baskar, Shinji Watanabe, Ramon Astudillo, Takaaki Hori et al.** · 2019-04-30

<details>
<summary>Abstract</summary>

Sequence-to-sequence automatic speech recognition (ASR) models require large quantities of data to attain high performance. For this reason, there has been a recent surge in interest for unsupervised and semi-supervised training in such models. This work builds upon recent results showing notable improvements in semi-supervised training using cycle-consistency and related techniques. Such techniques derive training procedures and losses able to leverage unpaired speech and/or text data by combining ASR with Text-to-Speech (TTS) models. In particular, this work proposes a new semi-supervised loss combining an end-to-end differentiable ASR$\rightarrow$TTS loss with TTS$\rightarrow$ASR loss. The method is able to leverage both unpaired speech and text data to outperform recently proposed related techniques in terms of \%WER. We provide extensive results analyzing the impact of data quantity and speech and text modalities and show consistent gains across WSJ and Librispeech corpora. Our code is provided in ESPnet to reproduce the experiments.

</details>

### [English Broadcast News Speech Recognition by Humans and Machines](1904.13258.md)
**Samuel Thomas, Masayuki Suzuki, Yinghui Huang, Gakuto Kurata et al.** · 2019-04-30

<details>
<summary>Abstract</summary>

With recent advances in deep learning, considerable attention has been given to achieving automatic speech recognition performance close to human performance on tasks like conversational telephone speech (CTS) recognition. In this paper we evaluate the usefulness of these proposed techniques on broadcast news (BN), a similar challenging task. We also perform a set of recognition measurements to understand how close the achieved automatic speech recognition results are to human performance on this task. On two publicly available BN test sets, DEV04F and RT04, our speech recognition system using LSTM and residual network based acoustic models with a combination of n-gram and neural network language models performs at 6.5% and 5.9% word error rate. By achieving new performance milestones on these test sets, our experiments show that techniques developed on other related tasks, like CTS, can be transferred to achieve similar performance. In contrast, the best measured human recognition performance on these test sets is much lower, at 3.6% and 2.8% respectively, indicating that there is still room for new techniques and improvements in this space, to reach human performance levels.

</details>

### [Curvature: A signature for Action Recognition in Video Sequences](1904.13003.md)
**He Chen, Gregory S. Chirikjian** · 2019-04-30

<details>
<summary>Abstract</summary>

In this paper, a novel signature of human action recognition, namely the curvature of a video sequence, is introduced. In this way, the distribution of sequential data is modeled, which enables few-shot learning. Instead of depending on recognizing features within images, our algorithm views actions as sequences on the universal time scale across a whole sequence of images. The video sequence, viewed as a curve in pixel space, is aligned by reparameterization using the arclength of the curve in pixel space. Once such curvatures are obtained, statistical indexes are extracted and fed into a learning-based classifier. Overall, our method is simple but powerful. Preliminary experimental results show that our method is effective and achieves state-of-the-art performance in video-based human action recognition. Moreover, we see latent capacity in transferring this idea into other sequence-based recognition applications such as speech recognition, machine translation, and text generation.

</details>

### [Adversarial Speaker Adaptation](1904.12407.md)
**Zhong Meng, Jinyu Li, Yifan Gong** · 2019-04-29

<details>
<summary>Abstract</summary>

We propose a novel adversarial speaker adaptation (ASA) scheme, in which adversarial learning is applied to regularize the distribution of deep hidden features in a speaker-dependent (SD) deep neural network (DNN) acoustic model to be close to that of a fixed speaker-independent (SI) DNN acoustic model during adaptation. An additional discriminator network is introduced to distinguish the deep features generated by the SD model from those produced by the SI model. In ASA, with a fixed SI model as the reference, an SD model is jointly optimized with the discriminator network to minimize the senone classification loss, and simultaneously to mini-maximize the SI/SD discrimination loss on the adaptation data. With ASA, a senone-discriminative deep feature is learned in the SD model with a similar distribution to that of the SI model. With such a regularized and adapted deep feature, the SD model can perform improved automatic speech recognition on the target speaker's speech. Evaluated on the Microsoft short message dictation dataset, ASA achieves 14.4% and 7.9% relative word error rate improvements for supervised and unsupervised adaptation, respectively, over an SI model trained from 2600 hours data, with 200 adaptation utterances per speaker.

</details>

### [Attentive Adversarial Learning for Domain-Invariant Training](1904.12400.md)
**Zhong Meng, Jinyu Li, Yifan Gong** · 2019-04-28

<details>
<summary>Abstract</summary>

Adversarial domain-invariant training (ADIT) proves to be effective in suppressing the effects of domain variability in acoustic modeling and has led to improved performance in automatic speech recognition (ASR). In ADIT, an auxiliary domain classifier takes in equally-weighted deep features from a deep neural network (DNN) acoustic model and is trained to improve their domain-invariance by optimizing an adversarial loss function. In this work, we propose an attentive ADIT (AADIT) in which we advance the domain classifier with an attention mechanism to automatically weight the input deep features according to their importance in domain classification. With this attentive re-weighting, AADIT can focus on the domain normalization of phonetic components that are more susceptible to domain variability and generates deep features with improved domain-invariance and senone-discriminativity over ADIT. Most importantly, the attention block serves only as an external component to the DNN acoustic model and is not involved in ASR, so AADIT can be used to improve the acoustic modeling with any DNN architectures. More generally, the same methodology can improve any adversarial learning system with an auxiliary discriminator. Evaluated on CHiME-3 dataset, the AADIT achieves 13.6% and 9.3% relative WER improvements, respectively, over a multi-conditional model and a strong ADIT baseline.

</details>

### [Transformers with convolutional context for ASR](1904.11660.md)
**Abdelrahman Mohamed, Dmytro Okhonko, Luke Zettlemoyer** · 2019-04-26

<details>
<summary>Abstract</summary>

The recent success of transformer networks for neural machine translation and other NLP tasks has led to a surge in research work trying to apply it for speech recognition. Recent efforts studied key research questions around ways of combining positional embedding with speech features, and stability of optimization for large scale learning of transformer networks. In this paper, we propose replacing the sinusoidal positional embedding for transformers with convolutionally learned input representations. These contextual representations provide subsequent transformer blocks with relative positional information needed for discovering long-range relationships between local concepts. The proposed system has favorable optimization characteristics where our reported results are produced with fixed learning rate of 1.0 and no warmup steps. The proposed model achieves a competitive 4.7% and 12.9% WER on the Librispeech ``test clean'' and ``test other'' subsets when no extra LM text is provided.

</details>

### [Assessing the Tolerance of Neural Machine Translation Systems Against Speech Recognition Errors](1904.10997.md)
**Nicholas Ruiz, Mattia Antonino Di Gangi, Nicola Bertoldi, Marcello Federico** · 2019-04-24

<details>
<summary>Abstract</summary>

Machine translation systems are conventionally trained on textual resources that do not model phenomena that occur in spoken language. While the evaluation of neural machine translation systems on textual inputs is actively researched in the literature , little has been discovered about the complexities of translating spoken language data with neural models. We introduce and motivate interesting problems one faces when considering the translation of automatic speech recognition (ASR) outputs on neural machine translation (NMT) systems. We test the robustness of sentence encoding approaches for NMT encoder-decoder modeling, focusing on word-based over byte-pair encoding. We compare the translation of utterances containing ASR errors in state-of-the-art NMT encoder-decoder systems against a strong phrase-based machine translation baseline in order to better understand which phenomena present in ASR outputs are better represented under the NMT framework than approaches that represent translation as a linear model.

</details>

### [Realizing Petabyte Scale Acoustic Modeling](1904.10584.md)
**Sree Hari Krishnan Parthasarathi, Nitin Sivakrishnan, Pranav Ladkat, Nikko Strom** · 2019-04-24

<details>
<summary>Abstract</summary>

Large scale machine learning (ML) systems such as the Alexa automatic speech recognition (ASR) system continue to improve with increasing amounts of manually transcribed training data. Instead of scaling manual transcription to impractical levels, we utilize semi-supervised learning (SSL) to learn acoustic models (AM) from the vast firehose of untranscribed audio data. Learning an AM from 1 Million hours of audio presents unique ML and system design challenges. We present the design and evaluation of a highly scalable and resource efficient SSL system for AM. Employing the student/teacher learning paradigm, we focus on the student learning subsystem: a scalable and robust data pipeline that generates features and targets from raw audio, and an efficient model pipeline, including the distributed trainer, that builds a student model. Our evaluations show that, even without extensive hyper-parameter tuning, we obtain relative accuracy improvements in the 10 to 20$\%$ range, with higher gains in noisier conditions. The end-to-end processing time of this SSL system was 12 days, and several components in this system can trivially scale linearly with more compute resources.

</details>

### [Natural Language Interactions in Autonomous Vehicles: Intent Detection and Slot Filling from Passenger Utterances](1904.10500.md)
**Eda Okur, Shachi H Kumar, Saurav Sahay, Asli Arslan Esme et al.** · 2019-04-23

<details>
<summary>Abstract</summary>

Understanding passenger intents and extracting relevant slots are important building blocks towards developing contextual dialogue systems for natural interactions in autonomous vehicles (AV). In this work, we explored AMIE (Automated-vehicle Multi-modal In-cabin Experience), the in-cabin agent responsible for handling certain passenger-vehicle interactions. When the passengers give instructions to AMIE, the agent should parse such commands properly and trigger the appropriate functionality of the AV system. In our current explorations, we focused on AMIE scenarios describing usages around setting or changing the destination and route, updating driving behavior or speed, finishing the trip and other use-cases to support various natural commands. We collected a multi-modal in-cabin dataset with multi-turn dialogues between the passengers and AMIE using a Wizard-of-Oz scheme via a realistic scavenger hunt game activity. After exploring various recent Recurrent Neural Networks (RNN) based techniques, we introduced our own hierarchical joint models to recognize passenger intents along with relevant slots associated with the action to be performed in AV scenarios. Our experimental results outperformed certain competitive baselines and achieved overall F1 scores of 0.91 for utterance-level intent detection and 0.96 for slot filling tasks. In addition, we conducted initial speech-to-text explorations by comparing intent/slot models trained and tested on human transcriptions versus noisy Automatic Speech Recognition (ASR) outputs. Finally, we compared the results with single passenger rides versus the rides with multiple passengers.

</details>

### [An Investigation of End-to-End Multichannel Speech Recognition for Reverberant and Mismatch Conditions](1904.09049.md)
**Aswin Shanmugam Subramanian, Xiaofei Wang, Shinji Watanabe, Toru Taniguchi et al.** · 2019-04-19

<details>
<summary>Abstract</summary>

Sequence-to-sequence (S2S) modeling is becoming a popular paradigm for automatic speech recognition (ASR) because of its ability to jointly optimize all the conventional ASR components in an end-to-end (E2E) fashion. This report investigates the ability of E2E ASR from standard close-talk to far-field applications by encompassing entire multichannel speech enhancement and ASR components within the S2S model. There have been previous studies on jointly optimizing neural beamforming alongside E2E ASR for denoising. It is clear from both recent challenge outcomes and successful products that far-field systems would be incomplete without solving both denoising and dereverberation simultaneously. This report uses a recently developed architecture for far-field ASR by composing neural extensions of dereverberation and beamforming modules with the S2S ASR module as a single differentiable neural network and also clearly defining the role of each subnetwork. The original implementation of this architecture was successfully applied to the noisy speech recognition task (CHiME-4), while we applied this implementation to noisy reverberant tasks (DIRHA and REVERB). Our investigation shows that the method achieves better performance than conventional pipeline methods on the DIRHA English dataset and comparable performance on the REVERB dataset. It also has additional advantages of being neither iterative nor requiring parallel noisy and clean speech data.

</details>

### [SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](1904.08779.md)
**Daniel S. Park, William Chan, Yu Zhang, Chung-Cheng Chiu et al.** · 2019-04-18

<details>
<summary>Abstract</summary>

We present SpecAugment, a simple data augmentation method for speech recognition. SpecAugment is applied directly to the feature inputs of a neural network (i.e., filter bank coefficients). The augmentation policy consists of warping the features, masking blocks of frequency channels, and masking blocks of time steps. We apply SpecAugment on Listen, Attend and Spell networks for end-to-end speech recognition tasks. We achieve state-of-the-art performance on the LibriSpeech 960h and Swichboard 300h tasks, outperforming all prior work. On LibriSpeech, we achieve 6.8% WER on test-other without the use of a language model, and 5.8% WER with shallow fusion with a language model. This compares to the previous state-of-the-art hybrid system of 7.5% WER. For Switchboard, we achieve 7.2%/14.6% on the Switchboard/CallHome portion of the Hub5'00 test set without the use of a language model, and 6.8%/14.1% with shallow fusion, which compares to the previous state-of-the-art hybrid system at 8.3%/17.3% WER.

</details>

### [Leveraging native language information for improved accented speech recognition](1904.09038.md)
**Shahram Ghorbani, John H. L. Hansen** · 2019-04-18

<details>
<summary>Abstract</summary>

Recognition of accented speech is a long-standing challenge for automatic speech recognition (ASR) systems, given the increasing worldwide population of bi-lingual speakers with English as their second language. If we consider foreign-accented speech as an interpolation of the native language (L1) and English (L2), using a model that can simultaneously address both languages would perform better at the acoustic level for accented speech. In this study, we explore how an end-to-end recurrent neural network (RNN) trained system with English and native languages (Spanish and Indian languages) could leverage data of native languages to improve performance for accented English speech. To this end, we examine pre-training with native languages, as well as multi-task learning (MTL) in which the main task is trained with native English and the secondary task is trained with Spanish or Indian Languages. We show that the proposed MTL model performs better than the pre-training approach and outperforms a baseline model trained simply with English data. We suggest a new setting for MTL in which the secondary task is trained with both English and the native language, using the same output set. This proposed scenario yields better performance with +11.95% and +17.55% character error rate gains over baseline for Hispanic and Indian accents, respectively.

</details>

### [TTS Skins: Speaker Conversion via ASR](1904.08983.md)
**Adam Polyak, Lior Wolf, Yaniv Taigman** · 2019-04-18

<details>
<summary>Abstract</summary>

We present a fully convolutional wav-to-wav network for converting between speakers' voices, without relying on text. Our network is based on an encoder-decoder architecture, where the encoder is pre-trained for the task of Automatic Speech Recognition, and a multi-speaker waveform decoder is trained to reconstruct the original signal in an autoregressive manner. We train the network on narrated audiobooks, and demonstrate multi-voice TTS in those voices, by converting the voice of a TTS robot.

</details>

### [Guiding CTC Posterior Spike Timings for Improved Posterior Fusion and Knowledge Distillation](1904.08311.md)
**Gakuto Kurata, Kartik Audhkhasi** · 2019-04-17

<details>
<summary>Abstract</summary>

Conventional automatic speech recognition (ASR) systems trained from frame-level alignments can easily leverage posterior fusion to improve ASR accuracy and build a better single model with knowledge distillation. End-to-end ASR systems trained using the Connectionist Temporal Classification (CTC) loss do not require frame-level alignment and hence simplify model training. However, sparse and arbitrary posterior spike timings from CTC models pose a new set of challenges in posterior fusion from multiple models and knowledge distillation between CTC models. We propose a method to train a CTC model so that its spike timings are guided to align with those of a pre-trained guiding CTC model. As a result, all models that share the same guiding model have aligned spike timings. We show the advantage of our method in various scenarios including posterior fusion of CTC models and knowledge distillation between CTC models with different architectures. With the 300-hour Switchboard training data, the single word CTC model distilled from multiple models improved the word error rates to 13.7%/23.1% from 14.9%/24.1% on the Hub5 2000 Switchboard/CallHome test sets without using any data augmentation, language model, or complex decoder.

</details>

### [End-to-End Speech Translation with Knowledge Distillation](1904.08075.md)
**Yuchen Liu, Hao Xiong, Zhongjun He, Jiajun Zhang et al.** · 2019-04-17

<details>
<summary>Abstract</summary>

End-to-end speech translation (ST), which directly translates from source language speech into target language text, has attracted intensive attentions in recent years. Compared to conventional pipeline systems, end-to-end ST models have advantages of lower latency, smaller model size and less error propagation. However, the combination of speech recognition and text translation in one model is more difficult than each of these two tasks. In this paper, we propose a knowledge distillation approach to improve ST model by transferring the knowledge from text translation model. Specifically, we first train a text translation model, regarded as a teacher model, and then ST model is trained to learn output probabilities from teacher model through knowledge distillation. Experiments on English- French Augmented LibriSpeech and English-Chinese TED corpus show that end-to-end ST is possible to implement on both similar and dissimilar language pairs. In addition, with the instruction of teacher model, end-to-end ST model can gain significant improvements by over 3.5 BLEU points.

</details>

### [A Multi-Task Learning Framework for Overcoming the Catastrophic Forgetting in Automatic Speech Recognition](1904.08039.md)
**Jiabin Xue, Jiqing Han, Tieran Zheng, Xiang Gao et al.** · 2019-04-17

<details>
<summary>Abstract</summary>

Recently, data-driven based Automatic Speech Recognition (ASR) systems have achieved state-of-the-art results. And transfer learning is often used when those existing systems are adapted to the target domain, e.g., fine-tuning, retraining. However, in the processes, the system parameters may well deviate too much from the previously learned parameters. Thus, it is difficult for the system training process to learn knowledge from target domains meanwhile not forgetting knowledge from the previous learning process, which is called as catastrophic forgetting (CF). In this paper, we attempt to solve the CF problem with the lifelong learning and propose a novel multi-task learning (MTL) training framework for ASR. It considers reserving original knowledge and learning new knowledge as two independent tasks, respectively. On the one hand, we constrain the new parameters not to deviate too far from the original parameters and punish the new system when forgetting original knowledge. On the other hand, we force the new system to solve new knowledge quickly. Then, a MTL mechanism is employed to get the balance between the two tasks. We applied our method to an End2End ASR task and obtained the best performance in both target and original datasets.

</details>

### [Hard Sample Mining for the Improved Retraining of Automatic Speech Recognition](1904.08031.md)
**Jiabin Xue, Jiqing Han, Tieran Zheng, Jiaxing Guo et al.** · 2019-04-17

<details>
<summary>Abstract</summary>

It is an effective way that improves the performance of the existing Automatic Speech Recognition (ASR) systems by retraining with more and more new training data in the target domain. Recently, Deep Neural Network (DNN) has become a successful model in the ASR field. In the training process of the DNN based methods, a back propagation of error between the transcription and the corresponding annotated text is used to update and optimize the parameters. Thus, the parameters are more influenced by the training samples with a big propagation error than the samples with a small one. In this paper, we define the samples with significant error as the hard samples and try to improve the performance of the ASR system by adding many of them. Unfortunately, the hard samples are sparse in the training data of the target domain, and manually label them is expensive. Therefore, we propose a hard samples mining method based on an enhanced deep multiple instance learning, which can find the hard samples from unlabeled training data by using a small subset of the dataset with manual labeling in the target domain. We applied our method to an End2End ASR task and obtained the best performance.

</details>

### [HARK Side of Deep Learning -- From Grad Student Descent to Automated Machine Learning](1904.07633.md)
**Oguzhan Gencoglu, Mark van Gils, Esin Guldogan, Chamin Morikawa et al.** · 2019-04-16

<details>
<summary>Abstract</summary>

Recent advancements in machine learning research, i.e., deep learning, introduced methods that excel conventional algorithms as well as humans in several complex tasks, ranging from detection of objects in images and speech recognition to playing difficult strategic games. However, the current methodology of machine learning research and consequently, implementations of the real-world applications of such algorithms, seems to have a recurring HARKing (Hypothesizing After the Results are Known) issue. In this work, we elaborate on the algorithmic, economic and social reasons and consequences of this phenomenon. We present examples from current common practices of conducting machine learning research (e.g. avoidance of reporting negative results) and failure of generalization ability of the proposed algorithms and datasets in actual real-life usage. Furthermore, a potential future trajectory of machine learning research and development from the perspective of accountable, unbiased, ethical and privacy-aware algorithmic decision making is discussed. We would like to emphasize that with this discussion we neither claim to provide an exhaustive argumentation nor blame any specific institution or individual on the raised issues. This is simply a discussion put forth by us, insiders of the machine learning field, reflecting on us.

</details>

### [Attention-Passing Models for Robust and Data-Efficient End-to-End Speech Translation](1904.07209.md)
**Matthias Sperber, Graham Neubig, Jan Niehues, Alex Waibel** · 2019-04-15

<details>
<summary>Abstract</summary>

Speech translation has traditionally been approached through cascaded models consisting of a speech recognizer trained on a corpus of transcribed speech, and a machine translation system trained on parallel texts. Several recent works have shown the feasibility of collapsing the cascade into a single, direct model that can be trained in an end-to-end fashion on a corpus of translated speech. However, experiments are inconclusive on whether the cascade or the direct model is stronger, and have only been conducted under the unrealistic assumption that both are trained on equal amounts of data, ignoring other available speech recognition and machine translation corpora. In this paper, we demonstrate that direct speech translation models require more data to perform well than cascaded models, and while they allow including auxiliary data through multi-task training, they are poor at exploiting such data, putting them at a severe disadvantage. As a remedy, we propose the use of end-to-end trainable models with two attention mechanisms, the first establishing source speech to source text alignments, the second modeling source to target text alignment. We show that such models naturally decompose into multi-task-trainable recognition and translation tasks and propose an attention-passing technique that alleviates error propagation issues in a previous formulation of a model with two attention stages. Our proposed model outperforms all examined baselines and is able to exploit auxiliary training data much more effectively than direct attentional models.

</details>

### [SpeechYOLO: Detection and Localization of Speech Objects](1904.07704.md)
**Yael Segal, Tzeviya Sylvia Fuchs, Joseph Keshet** · 2019-04-14

<details>
<summary>Abstract</summary>

In this paper, we propose to apply object detection methods from the vision domain on the speech recognition domain, by treating audio fragments as objects. More specifically, we present SpeechYOLO, which is inspired by the YOLO algorithm for object detection in images. The goal of SpeechYOLO is to localize boundaries of utterances within the input signal, and to correctly classify them. Our system is composed of a convolutional neural network, with a simple least-mean-squares loss function. We evaluated the system on several keyword spotting tasks, that include corpora of read speech and spontaneous speech. Our system compares favorably with other algorithms trained for both localization and classification.

</details>

### [Low-Latency Speaker-Independent Continuous Speech Separation](1904.06478.md)
**Takuya Yoshioka, Zhuo Chen, Changliang Liu, Xiong Xiao et al.** · 2019-04-13

<details>
<summary>Abstract</summary>

Speaker independent continuous speech separation (SI-CSS) is a task of converting a continuous audio stream, which may contain overlapping voices of unknown speakers, into a fixed number of continuous signals each of which contains no overlapping speech segment. A separated, or cleaned, version of each utterance is generated from one of SI-CSS's output channels nondeterministically without being split up and distributed to multiple channels. A typical application scenario is transcribing multi-party conversations, such as meetings, recorded with microphone arrays. The output signals can be simply sent to a speech recognition engine because they do not include speech overlaps. The previous SI-CSS method uses a neural network trained with permutation invariant training and a data-driven beamformer and thus requires much processing latency. This paper proposes a low-latency SI-CSS method whose performance is comparable to that of the previous method in a microphone array-based meeting transcription task.This is achieved (1) by using a new speech separation network architecture combined with a double buffering scheme and (2) by performing enhancement with a set of fixed beamformers followed by a neural post-filter.

</details>

### [STC Speaker Recognition Systems for the VOiCES From a Distance Challenge](1904.06093.md)
**Sergey Novoselov, Aleksei Gusev, Artem Ivanov, Timur Pekhovsky et al.** · 2019-04-12

<details>
<summary>Abstract</summary>

This paper presents the Speech Technology Center (STC) speaker recognition (SR) systems submitted to the VOiCES From a Distance challenge 2019. The challenge's SR task is focused on the problem of speaker recognition in single channel distant/far-field audio under noisy conditions. In this work we investigate different deep neural networks architectures for speaker embedding extraction to solve the task. We show that deep networks with residual frame level connections outperform more shallow architectures. Simple energy based speech activity detector (SAD) and automatic speech recognition (ASR) based SAD are investigated in this work. We also address the problem of data preparation for robust embedding extractors training. The reverberation for the data augmentation was performed using automatic room impulse response generator. In our systems we used discriminatively trained cosine similarity metric learning model as embedding backend. Scores normalization procedure was applied for each individual subsystem we used. Our final submitted systems were based on the fusion of different subsystems. The results obtained on the VOiCES development and evaluation sets demonstrate effectiveness and robustness of the proposed systems when dealing with distant/far-field audio under noisy conditions.

</details>

### [Unsupervised Speech Domain Adaptation Based on Disentangled Representation Learning for Robust Speech Recognition](1904.06086.md)
**Jong-Hyeon Park, Myungwoo Oh, Hyung-Min Park** · 2019-04-12

<details>
<summary>Abstract</summary>

In general, the performance of automatic speech recognition (ASR) systems is significantly degraded due to the mismatch between training and test environments. Recently, a deep-learning-based image-to-image translation technique to translate an image from a source domain to a desired domain was presented, and cycle-consistent adversarial network (CycleGAN) was applied to learn a mapping for speech-to-speech conversion from a speaker to a target speaker. However, this method might not be adequate to remove corrupting noise components for robust ASR because it was designed to convert speech itself. In this paper, we propose a domain adaptation method based on generative adversarial nets (GANs) with disentangled representation learning to achieve robustness in ASR systems. In particular, two separated encoders, context and domain encoders, are introduced to learn distinct latent variables. The latent variables allow us to convert the domain of speech according to its context and domain representation. We improved word accuracies by 6.55~15.70\% for the CHiME4 challenge corpus by applying a noisy-to-clean environment adaptation for robust ASR. In addition, similar to the method based on the CycleGAN, this method can be used for gender adaptation in gender-mismatched recognition.

</details>

### [Direct speech-to-speech translation with a sequence-to-sequence model](1904.06037.md)
**Ye Jia, Ron J. Weiss, Fadi Biadsy, Wolfgang Macherey et al.** · 2019-04-12

<details>
<summary>Abstract</summary>

We present an attention-based sequence-to-sequence neural network which can directly translate speech from one language into speech in another language, without relying on an intermediate text representation. The network is trained end-to-end, learning to map speech spectrograms into target spectrograms in another language, corresponding to the translated content (in a different canonical voice). We further demonstrate the ability to synthesize translated speech using the voice of the source speaker. We conduct experiments on two Spanish-to-English speech translation datasets, and find that the proposed model slightly underperforms a baseline cascade of a direct speech-to-text translation model and a text-to-speech synthesis model, demonstrating the feasibility of the approach on this very challenging task.

</details>

### [wav2vec: Unsupervised Pre-training for Speech Recognition](1904.05862.md)
**Steffen Schneider, Alexei Baevski, Ronan Collobert, Michael Auli** · 2019-04-11

<details>
<summary>Abstract</summary>

We explore unsupervised pre-training for speech recognition by learning representations of raw audio. wav2vec is trained on large amounts of unlabeled audio data and the resulting representations are then used to improve acoustic model training. We pre-train a simple multi-layer convolutional neural network optimized via a noise contrastive binary classification task. Our experiments on WSJ reduce WER of a strong character-based log-mel filterbank baseline by up to 36% when only a few hours of transcribed data is available. Our approach achieves 2.43% WER on the nov92 test set. This outperforms Deep Speech 2, the best reported character-based system in the literature while using two orders of magnitude less labeled training data.

</details>

### [From Semi-supervised to Almost-unsupervised Speech Recognition with Very-low Resource by Jointly Learning Phonetic Structures from Audio and Text Embeddings](1904.05078.md)
**Yi-Chen Chen, Sung-Feng Huang, Hung-yi Lee, Lin-shan Lee** · 2019-04-10

<details>
<summary>Abstract</summary>

Producing a large amount of annotated speech data for training ASR systems remains difficult for more than 95% of languages all over the world which are low-resourced. However, we note human babies start to learn the language by the sounds (or phonetic structures) of a small number of exemplar words, and "generalize" such knowledge to other words without hearing a large amount of data. We initiate some preliminary work in this direction. Audio Word2Vec is used to learn the phonetic structures from spoken words (signal segments), while another autoencoder is used to learn the phonetic structures from text words. The relationships among the above two can be learned jointly, or separately after the above two are well trained. This relationship can be used in speech recognition with very low resource. In the initial experiments on the TIMIT dataset, only 2.1 hours of speech data (in which 2500 spoken words were annotated and the rest unlabeled) gave a word error rate of 44.6%, and this number can be reduced to 34.2% if 4.1 hr of speech data (in which 20000 spoken words were annotated) were given. These results are not satisfactory, but a good starting point.

</details>

### [Distributed Deep Learning Strategies For Automatic Speech Recognition](1904.04956.md)
**Wei Zhang, Xiaodong Cui, Ulrich Finkler, Brian Kingsbury et al.** · 2019-04-10

<details>
<summary>Abstract</summary>

In this paper, we propose and investigate a variety of distributed deep learning strategies for automatic speech recognition (ASR) and evaluate them with a state-of-the-art Long short-term memory (LSTM) acoustic model on the 2000-hour Switchboard (SWB2000), which is one of the most widely used datasets for ASR performance benchmark. We first investigate what are the proper hyper-parameters (e.g., learning rate) to enable the training with sufficiently large batch size without impairing the model accuracy. We then implement various distributed strategies, including Synchronous (SYNC), Asynchronous Decentralized Parallel SGD (ADPSGD) and the hybrid of the two HYBRID, to study their runtime/accuracy trade-off. We show that we can train the LSTM model using ADPSGD in 14 hours with 16 NVIDIA P100 GPUs to reach a 7.6% WER on the Hub5- 2000 Switchboard (SWB) test set and a 13.1% WER on the CallHome (CH) test set. Furthermore, we can train the model using HYBRID in 11.5 hours with 32 NVIDIA V100 GPUs without loss in accuracy.

</details>

### [Performance Monitoring for End-to-End Speech Recognition](1904.04896.md)
**Ruizhi Li, Gregory Sell, Hynek Hermansky** · 2019-04-09

<details>
<summary>Abstract</summary>

Measuring performance of an automatic speech recognition (ASR) system without ground-truth could be beneficial in many scenarios, especially with data from unseen domains, where performance can be highly inconsistent. In conventional ASR systems, several performance monitoring (PM) techniques have been well-developed to monitor performance by looking at tri-phone posteriors or pre-softmax activations from neural network acoustic modeling. However, strategies for monitoring more recently developed end-to-end ASR systems have not yet been explored, and so that is the focus of this paper. We adapt previous PM measures (Entropy, M-measure and Auto-encoder) and apply our proposed RNN predictor in the end-to-end setting. These measures utilize the decoder output layer and attention probability vectors, and their predictive power is measured with simple linear models. Our findings suggest that decoder-level features are more feasible and informative than attention-level probabilities for PM measures, and that M-measure on the decoder posteriors achieves the best overall predictive performance with an average prediction error 8.8%. Entropy measures and RNN-based prediction also show competitive predictability, especially for unseen conditions.

</details>

### [Deep Cytometry: Deep learning with Real-time Inference in Cell Sorting and Flow Cytometry](1904.09233.md)
**Yueqin Li, Ata Mahjoubfar, Claire Lifan Chen, Kayvan Reza Niazi et al.** · 2019-04-09

<details>
<summary>Abstract</summary>

Deep learning has achieved spectacular performance in image and speech recognition and synthesis. It outperforms other machine learning algorithms in problems where large amounts of data are available. In the area of measurement technology, instruments based on the photonic time stretch have established record real-time measurement throughput in spectroscopy, optical coherence tomography, and imaging flow cytometry. These extreme-throughput instruments generate approximately 1 Tbit/s of continuous measurement data and have led to the discovery of rare phenomena in nonlinear and complex systems as well as new types of biomedical instruments. Owing to the abundance of data they generate, time-stretch instruments are a natural fit to deep learning classification. Previously we had shown that high-throughput label-free cell classification with high accuracy can be achieved through a combination of time-stretch microscopy, image processing and feature extraction, followed by deep learning for finding cancer cells in the blood. Such a technology holds promise for early detection of primary cancer or metastasis. Here we describe a new deep learning pipeline, which entirely avoids the slow and computationally costly signal processing and feature extraction steps by a convolutional neural network that directly operates on the measured signals. The improvement in computational efficiency enables low-latency inference and makes this pipeline suitable for cell sorting via deep learning. Our neural network takes less than a few milliseconds to classify the cells, fast enough to provide a decision to a cell sorter for real-time separation of individual target cells. We demonstrate the applicability of our new method in the classification of OT-II white blood cells and SW-480 epithelial cancer cells with more than 95% accuracy in a label-free fashion.

</details>

### [A Target-Agnostic Attack on Deep Models: Exploiting Security Vulnerabilities of Transfer Learning](1904.04334.md)
**Shahbaz Rezaei, Xin Liu** · 2019-04-08

<details>
<summary>Abstract</summary>

Due to insufficient training data and the high computational cost to train a deep neural network from scratch, transfer learning has been extensively used in many deep-neural-network-based applications. A commonly used transfer learning approach involves taking a part of a pre-trained model, adding a few layers at the end, and re-training the new layers with a small dataset. This approach, while efficient and widely used, imposes a security vulnerability because the pre-trained model used in transfer learning is usually publicly available, including to potential attackers. In this paper, we show that without any additional knowledge other than the pre-trained model, an attacker can launch an effective and efficient brute force attack that can craft instances of input to trigger each target class with high confidence. We assume that the attacker has no access to any target-specific information, including samples from target classes, re-trained model, and probabilities assigned by Softmax to each class, and thus making the attack target-agnostic. These assumptions render all previous attack models inapplicable, to the best of our knowledge. To evaluate the proposed attack, we perform a set of experiments on face recognition and speech recognition tasks and show the effectiveness of the attack. Our work reveals a fundamental security weakness of the Softmax layer when used in transfer learning settings.

</details>

### [Exploring Methods for the Automatic Detection of Errors in Manual Transcription](1904.04294.md)
**Xiaofei Wang, Jinyi Yang, Ruizhi Li, Samik Sadhu et al.** · 2019-04-08

<details>
<summary>Abstract</summary>

Quality of data plays an important role in most deep learning tasks. In the speech community, transcription of speech recording is indispensable. Since the transcription is usually generated artificially, automatically finding errors in manual transcriptions not only saves time and labors but benefits the performance of tasks that need the training process. Inspired by the success of hybrid automatic speech recognition using both language model and acoustic model, two approaches of automatic error detection in the transcriptions have been explored in this work. Previous study using a biased language model approach, relying on a strong transcription-dependent language model, has been reviewed. In this work, we propose a novel acoustic model based approach, focusing on the phonetic sequence of speech. Both methods have been evaluated on a completely real dataset, which was originally transcribed with errors and strictly corrected manually afterwards.

</details>

### [Knowledge Distillation For Recurrent Neural Network Language Modeling With Trust Regularization](1904.04163.md)
**Yangyang Shi, Mei-Yuh Hwang, Xin Lei, Haoyu Sheng** · 2019-04-08

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) have dominated language modeling because of their superior performance over traditional N-gram based models. In many applications, a large Recurrent Neural Network language model (RNNLM) or an ensemble of several RNNLMs is used. These models have large memory footprints and require heavy computation. In this paper, we examine the effect of applying knowledge distillation in reducing the model size for RNNLMs. In addition, we propose a trust regularization method to improve the knowledge distillation training for RNNLMs. Using knowledge distillation with trust regularization, we reduce the parameter size to a third of that of the previously published best model while maintaining the state-of-the-art perplexity result on Penn Treebank data. In a speech recognition N-bestrescoring task, we reduce the RNNLM model size to 18.5% of the baseline system, with no degradation in word error rate(WER) performance on Wall Street Journal data set.

</details>

### [Completely Unsupervised Speech Recognition By A Generative Adversarial Network Harmonized With Iteratively Refined Hidden Markov Models](1904.04100.md)
**Kuan-Yu Chen, Che-Ping Tsai, Da-Rong Liu, Hung-Yi Lee et al.** · 2019-04-08

<details>
<summary>Abstract</summary>

Producing a large annotated speech corpus for training ASR systems remains difficult for more than 95% of languages all over the world which are low-resourced, but collecting a relatively big unlabeled data set for such languages is more achievable. This is why some initial effort have been reported on completely unsupervised speech recognition learned from unlabeled data only, although with relatively high error rates. In this paper, we develop a Generative Adversarial Network (GAN) to achieve this purpose, in which a Generator and a Discriminator learn from each other iteratively to improve the performance. We further use a set of Hidden Markov Models (HMMs) iteratively refined from the machine generated labels to work in harmony with the GAN. The initial experiments on TIMIT data set achieve an phone error rate of 33.1%, which is 8.5% lower than the previous state-of-the-art.

</details>

### [Constrained Output Embeddings for End-to-End Code-Switching Speech Recognition with Only Monolingual Data](1904.03802.md)
**Yerbolat Khassanov, Haihua Xu, Van Tung Pham, Zhiping Zeng et al.** · 2019-04-08

<details>
<summary>Abstract</summary>

The lack of code-switch training data is one of the major concerns in the development of end-to-end code-switching automatic speech recognition (ASR) models. In this work, we propose a method to train an improved end-to-end code-switching ASR using only monolingual data. Our method encourages the distributions of output token embeddings of monolingual languages to be similar, and hence, promotes the ASR model to easily code-switch between languages. Specifically, we propose to use Jensen-Shannon divergence and cosine distance based constraints. The former will enforce output embeddings of monolingual languages to possess similar distributions, while the later simply brings the centroids of two distributions to be close to each other. Experimental results demonstrate high effectiveness of the proposed method, yielding up to 4.5% absolute mixed error rate improvement on Mandarin-English code-switching ASR task.

</details>

### [Enriching Rare Word Representations in Neural Language Models by Embedding Matrix Augmentation](1904.03799.md)
**Yerbolat Khassanov, Zhiping Zeng, Van Tung Pham, Haihua Xu et al.** · 2019-04-08

<details>
<summary>Abstract</summary>

The neural language models (NLM) achieve strong generalization capability by learning the dense representation of words and using them to estimate probability distribution function. However, learning the representation of rare words is a challenging problem causing the NLM to produce unreliable probability estimates. To address this problem, we propose a method to enrich representations of rare words in pre-trained NLM and consequently improve its probability estimation performance. The proposed method augments the word embedding matrices of pre-trained NLM while keeping other parameters unchanged. Specifically, our method updates the embedding vectors of rare words using embedding vectors of other semantically and syntactically similar words. To evaluate the proposed method, we enrich the rare street names in the pre-trained NLM and use it to rescore 100-best hypotheses output from the Singapore English speech recognition system. The enriched NLM reduces the word error rate by 6% relative and improves the recognition accuracy of the rare words by 16% absolute as compared to the baseline NLM.

</details>

### [Improved Speaker-Dependent Separation for CHiME-5 Challenge](1904.03792.md)
**Jian Wu, Yong Xu, Shi-Xiong Zhang, Lian-Wu Chen et al.** · 2019-04-08

<details>
<summary>Abstract</summary>

This paper summarizes several follow-up contributions for improving our submitted NWPU speaker-dependent system for CHiME-5 challenge, which aims to solve the problem of multi-channel, highly-overlapped conversational speech recognition in a dinner party scenario with reverberations and non-stationary noises. We adopt a speaker-aware training method by using i-vector as the target speaker information for multi-talker speech separation. With only one unified separation model for all speakers, we achieve a 10\% absolute improvement in terms of word error rate (WER) over the previous baseline of 80.28\% on the development set by leveraging our newly proposed data processing techniques and beamforming approach. With our improved back-end acoustic model, we further reduce WER to 60.15\% which surpasses the result of our submitted CHiME-5 challenge system without applying any fusion techniques.

</details>

### [Time Domain Audio Visual Speech Separation](1904.03760.md)
**Jian Wu, Yong Xu, Shi-Xiong Zhang, Lian-Wu Chen et al.** · 2019-04-07

<details>
<summary>Abstract</summary>

Audio-visual multi-modal modeling has been demonstrated to be effective in many speech related tasks, such as speech recognition and speech enhancement. This paper introduces a new time-domain audio-visual architecture for target speaker extraction from monaural mixtures. The architecture generalizes the previous TasNet (time-domain speech separation network) to enable multi-modal learning and at meanwhile it extends the classical audio-visual speech separation from frequency-domain to time-domain. The main components of proposed architecture include an audio encoder, a video encoder that extracts lip embedding from video streams, a multi-modal separation network and an audio decoder. Experiments on simulated mixtures based on recently released LRS2 dataset show that our method can bring 3dB+ and 4dB+ Si-SNR improvements on two- and three-speaker cases respectively, compared to audio-only TasNet and frequency-domain audio-visual networks

</details>

### [Speech Model Pre-training for End-to-End Spoken Language Understanding](1904.03670.md)
**Loren Lugosch, Mirco Ravanelli, Patrick Ignoto, Vikrant Singh Tomar et al.** · 2019-04-07

<details>
<summary>Abstract</summary>

Whereas conventional spoken language understanding (SLU) systems map speech to text, and then text to intent, end-to-end SLU systems map speech directly to intent through a single trainable model. Achieving high accuracy with these end-to-end models without a large amount of training data is difficult. We propose a method to reduce the data requirements of end-to-end SLU in which the model is first pre-trained to predict words and phonemes, thus learning good features for SLU. We introduce a new SLU dataset, Fluent Speech Commands, and show that our method improves performance both when the full dataset is used for training and when only a small subset is used. We also describe preliminary experiments to gauge the model's ability to generalize to new phrases not heard during training.

</details>

### [Token-Level Ensemble Distillation for Grapheme-to-Phoneme Conversion](1904.03446.md)
**Hao Sun, Xu Tan, Jun-Wei Gan, Hongzhi Liu et al.** · 2019-04-06

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is an important task in automatic speech recognition and text-to-speech systems. Recently, G2P conversion is viewed as a sequence to sequence task and modeled by RNN or CNN based encoder-decoder framework. However, previous works do not consider the practical issues when deploying G2P model in the production system, such as how to leverage additional unlabeled data to boost the accuracy, as well as reduce model size for online deployment. In this work, we propose token-level ensemble distillation for G2P conversion, which can (1) boost the accuracy by distilling the knowledge from additional unlabeled data, and (2) reduce the model size but maintain the high accuracy, both of which are very practical and helpful in the online production system. We use token-level knowledge distillation, which results in better accuracy than the sequence-level counterpart. What is more, we adopt the Transformer instead of RNN or CNN based models to further boost the accuracy of G2P conversion. Experiments on the publicly available CMUDict dataset and an internal English dataset demonstrate the effectiveness of our proposed method. Particularly, our method achieves 19.88% WER on CMUDict dataset, outperforming the previous works by more than 4.22% WER, and setting the new state-of-the-art results.

</details>

### [Measuring scheduling efficiency of RNNs for NLP applications](1904.03302.md)
**Urmish Thakker, Ganesh Dasika, Jesse Beu, Matthew Mattina** · 2019-04-05

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) have shown state of the art results for speech recognition, natural language processing, image captioning and video summarizing applications. Many of these applications run on low-power platforms, so their energy efficiency is extremely important. We observed that cache-oblivious RNN scheduling during inference typically results in 30-50x more data transferred on and off the CPU than the application's working set size. This can potentially impact its energy efficiency. This paper presents a new metric called Data Reuse Efficiency to gauge the RNN scheduling efficiency of a platform and shows the factors that influence the DRE value. Additionally, this paper discusses an optimization to improve reuse in RNNs and highlights the positive impact of this optimization on the total amount of memory read from or written to the memory controller (and, hence, the DRE value) during the execution of an RNN application for a mobile SoC.

</details>

### [Jasper: An End-to-End Convolutional Neural Acoustic Model](1904.03288.md)
**Jason Li, Vitaly Lavrukhin, Boris Ginsburg, Ryan Leary et al.** · 2019-04-05

<details>
<summary>Abstract</summary>

In this paper, we report state-of-the-art results on LibriSpeech among end-to-end speech recognition models without any external training data. Our model, Jasper, uses only 1D convolutions, batch normalization, ReLU, dropout, and residual connections. To improve training, we further introduce a new layer-wise optimizer called NovoGrad. Through experiments, we demonstrate that the proposed deep architecture performs as well or better than more complex choices. Our deepest Jasper variant uses 54 convolutional layers. With this architecture, we achieve 2.95% WER using a beam-search decoder with an external neural language model and 3.86% WER with a greedy decoder on LibriSpeech test-clean. We also report competitive results on the Wall Street Journal and the Hub5'00 conversational evaluation datasets.

</details>

### [LibriTTS: A Corpus Derived from LibriSpeech for Text-to-Speech](1904.02882.md)
**Heiga Zen, Viet Dang, Rob Clark, Yu Zhang et al.** · 2019-04-05

<details>
<summary>Abstract</summary>

This paper introduces a new speech corpus called "LibriTTS" designed for text-to-speech use. It is derived from the original audio and text materials of the LibriSpeech corpus, which has been used for training and evaluating automatic speech recognition systems. The new corpus inherits desired properties of the LibriSpeech corpus while addressing a number of issues which make LibriSpeech less than ideal for text-to-speech work. The released corpus consists of 585 hours of speech data at 24kHz sampling rate from 2,456 speakers and the corresponding texts. Experimental results show that neural end-to-end TTS models trained from the LibriTTS corpus achieved above 4.0 in mean opinion scores in naturalness in five out of six evaluation speakers. The corpus is freely available for download from http://www.openslr.org/60/.

</details>

### [An End-to-End Conversational Style Matching Agent](1904.02760.md)
**Rens Hoegen, Deepali Aneja, Daniel McDuff, Mary Czerwinski** · 2019-04-04

<details>
<summary>Abstract</summary>

We present an end-to-end voice-based conversational agent that is able to engage in naturalistic multi-turn dialogue and align with the interlocutor's conversational style. The system uses a series of deep neural network components for speech recognition, dialogue generation, prosodic analysis and speech synthesis to generate language and prosodic expression with qualities that match those of the user. We conducted a user study (N=30) in which participants talked with the agent for 15 to 20 minutes, resulting in over 8 hours of natural interaction data. Users with high consideration conversational styles reported the agent to be more trustworthy when it matched their conversational style. Whereas, users with high involvement conversational styles were indifferent. Finally, we provide design guidelines for multi-turn dialogue interactions using conversational style adaptation.

</details>

### [Sequence-to-Sequence Speech Recognition with Time-Depth Separable Convolutions](1904.02619.md)
**Awni Hannun, Ann Lee, Qiantong Xu, Ronan Collobert** · 2019-04-04

<details>
<summary>Abstract</summary>

We propose a fully convolutional sequence-to-sequence encoder architecture with a simple and efficient decoder. Our model improves WER on LibriSpeech while being an order of magnitude more efficient than a strong RNN baseline. Key to our approach is a time-depth separable convolution block which dramatically reduces the number of parameters in the model while keeping the receptive field large. We also give a stable and efficient beam search inference procedure which allows us to effectively integrate a language model. Coupled with a convolutional language model, our time-depth separable convolution architecture improves by more than 22% relative WER over the best previously reported sequence-to-sequence results on the noisy LibriSpeech test set.

</details>

### [Massively Multilingual Adversarial Speech Recognition](1904.02210.md)
**Oliver Adams, Matthew Wiesner, Shinji Watanabe, David Yarowsky** · 2019-04-03

<details>
<summary>Abstract</summary>

We report on adaptation of multilingual end-to-end speech recognition models trained on as many as 100 languages. Our findings shed light on the relative importance of similarity between the target and pretraining languages along the dimensions of phonetics, phonology, language family, geographical location, and orthography. In this context, experiments demonstrate the effectiveness of two additional pretraining objectives in encouraging language-independent encoder representations: a context-independent phoneme objective paired with a language-adversarial classification objective.

</details>

### [VideoBERT: A Joint Model for Video and Language Representation Learning](1904.01766.md)
**Chen Sun, Austin Myers, Carl Vondrick, Kevin Murphy et al.** · 2019-04-03

<details>
<summary>Abstract</summary>

Self-supervised learning has become increasingly important to leverage the abundance of unlabeled data available on platforms like YouTube. Whereas most existing approaches learn low-level representations, we propose a joint visual-linguistic model to learn high-level features without any explicit supervision. In particular, inspired by its recent success in language modeling, we build upon the BERT model to learn bidirectional joint distributions over sequences of visual and linguistic tokens, derived from vector quantization of video data and off-the-shelf speech recognition outputs, respectively. We use VideoBERT in numerous tasks, including action classification and video captioning. We show that it can be applied directly to open-vocabulary classification, and confirm that large amounts of training data and cross-modal information are critical to performance. Furthermore, we outperform the state-of-the-art on video captioning, and quantitative results verify that the model learns high-level semantic features.

</details>

### [End-to-End Visual Speech Recognition for Small-Scale Datasets](1904.01954.md)
**Stavros Petridis, Yujiang Wang, Pingchuan Ma, Zuwei Li et al.** · 2019-04-02

<details>
<summary>Abstract</summary>

Visual speech recognition models traditionally consist of two stages, feature extraction and classification. Several deep learning approaches have been recently presented aiming to replace the feature extraction stage by automatically extracting features from mouth images. However, research on joint learning of features and classification remains limited. In addition, most of the existing methods require large amounts of data in order to achieve state-of-the-art performance, otherwise they under-perform. In this work, we present an end-to-end visual speech recognition system based on fully-connected layers and Long-Short Memory (LSTM) networks which is suitable for small-scale datasets. The model consists of two streams which extract features directly from the mouth and difference images, respectively. The temporal dynamics in each stream are modelled by a Bidirectional LSTM (BLSTM) and the fusion of the two streams takes place via another BLSTM. An absolute improvement of 0.6%, 3.4%, 3.9%, 11.4% over the state-of-the-art is reported on the OuluVS2, CUAVE, AVLetters and AVLetters2 databases, respectively.

</details>

### [Unsupervised training of neural mask-based beamforming](1904.01578.md)
**Lukas Drude, Jahn Heymann, Reinhold Haeb-Umbach** · 2019-04-02

<details>
<summary>Abstract</summary>

We present an unsupervised training approach for a neural network-based mask estimator in an acoustic beamforming application. The network is trained to maximize a likelihood criterion derived from a spatial mixture model of the observations. It is trained from scratch without requiring any parallel data consisting of degraded input and clean training targets. Thus, training can be carried out on real recordings of noisy speech rather than simulated ones. In contrast to previous work on unsupervised training of neural mask estimators, our approach avoids the need for a possibly pre-trained teacher model entirely. We demonstrate the effectiveness of our approach by speech recognition experiments on two different datasets: one mainly deteriorated by noise (CHiME 4) and one by reverberation (REVERB). The results show that the performance of the proposed system is on par with a supervised system using oracle target masks for training and with a system trained using a model-based teacher.

</details>

### [Unsupervised training of a deep clustering model for multichannel blind source separation](1904.01340.md)
**Lukas Drude, Daniel Hasenklever, Reinhold Haeb-Umbach** · 2019-04-02

<details>
<summary>Abstract</summary>

We propose a training scheme to train neural network-based source separation algorithms from scratch when parallel clean data is unavailable. In particular, we demonstrate that an unsupervised spatial clustering algorithm is sufficient to guide the training of a deep clustering system. We argue that previous work on deep clustering requires strong supervision and elaborate on why this is a limitation. We demonstrate that (a) the single-channel deep clustering system trained according to the proposed scheme alone is able to achieve a similar performance as the multi-channel teacher in terms of word error rates and (b) initializing the spatial clustering approach with the deep clustering result yields a relative word error rate reduction of 26 % over the unsupervised teacher.

</details>

### [Learning Shared Encoding Representation for End-to-End Speech Recognition Models](1904.02147.md)
**Thai-Son Nguyen, Sebastian Stueker, Alex Waibel** · 2019-03-31

<details>
<summary>Abstract</summary>

In this work, we learn a shared encoding representation for a multi-task neural network model optimized with connectionist temporal classification (CTC) and conventional framewise cross-entropy training criteria. Our experiments show that the multi-task training not only tackles the complexity of optimizing CTC models such as acoustic-to-word but also results in significant improvement compared to the plain-task training with an optimal setup. Furthermore, we propose to use the encoding representation learned by the multi-task network to initialize the encoder of attention-based models. Thereby, we train a deep attention-based end-to-end model with 10 long short-term memory (LSTM) layers of encoder which produces 12.2\% and 22.6\% word-error-rate on Switchboard and CallHome subsets of the Hub5 2000 evaluation.

</details>

### [Acoustically Grounded Word Embeddings for Improved Acoustics-to-Word Speech Recognition](1903.12306.md)
**Shane Settle, Kartik Audhkhasi, Karen Livescu, Michael Picheny** · 2019-03-29

<details>
<summary>Abstract</summary>

Direct acoustics-to-word (A2W) systems for end-to-end automatic speech recognition are simpler to train, and more efficient to decode with, than sub-word systems. However, A2W systems can have difficulties at training time when data is limited, and at decoding time when recognizing words outside the training vocabulary. To address these shortcomings, we investigate the use of recently proposed acoustic and acoustically grounded word embedding techniques in A2W systems. The idea is based on treating the final pre-softmax weight matrix of an AWE recognizer as a matrix of word embedding vectors, and using an externally trained set of word embeddings to improve the quality of this matrix. In particular we introduce two ideas: (1) Enforcing similarity at training time between the external embeddings and the recognizer weights, and (2) using the word embeddings at test time for predicting out-of-vocabulary words. Our word embedding model is acoustically grounded, that is it is learned jointly with acoustic embeddings so as to encode the words' acoustic-phonetic content; and it is parametric, so that it can embed any arbitrary (potentially out-of-vocabulary) sequence of characters. We find that both techniques improve the performance of an A2W recognizer on conversational telephone speech.

</details>

### [Modeling Acoustic-Prosodic Cues for Word Importance Prediction in Spoken Dialogues](1903.12238.md)
**Sushant Kafle, Cecilia O. Alm, Matt Huenerfauth** · 2019-03-28

<details>
<summary>Abstract</summary>

Prosodic cues in conversational speech aid listeners in discerning a message. We investigate whether acoustic cues in spoken dialogue can be used to identify the importance of individual words to the meaning of a conversation turn. Individuals who are Deaf and Hard of Hearing often rely on real-time captions in live meetings. Word error rate, a traditional metric for evaluating automatic speech recognition, fails to capture that some words are more important for a system to transcribe correctly than others. We present and evaluate neural architectures that use acoustic features for 3-class word importance prediction. Our model performs competitively against state-of-the-art text-based word-importance prediction models, and it demonstrates particular benefits when operating on imperfect ASR output.

</details>

### [Automatic Spelling Correction with Transformer for CTC-based End-to-End Speech Recognition](1904.10045.md)
**Shiliang Zhang, Ming Lei, Zhijie Yan** · 2019-03-27

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) based end-to-end speech recognition system usually need to incorporate an external language model by using WFST-based decoding in order to achieve promising results. This is more essential to Mandarin speech recognition since it owns a special phenomenon, namely homophone, which causes a lot of substitution errors. The linguistic information introduced by language model will help to distinguish these substitution errors. In this work, we propose a transformer based spelling correction model to automatically correct errors especially the substitution errors made by CTC-based Mandarin speech recognition system. Specifically, we investigate using the recognition results generated by CTC-based systems as input and the ground-truth transcriptions as output to train a transformer with encoder-decoder architecture, which is much similar to machine translation. Results in a 20,000 hours Mandarin speech recognition task show that the proposed spelling correction model can achieve a CER of 3.41%, which results in 22.9% and 53.2% relative improvement compared to the baseline CTC-based systems decoded with and without language model respectively.

</details>

### [Imperceptible, Robust, and Targeted Adversarial Examples for Automatic Speech Recognition](1903.10346.md)
**Yao Qin, Nicholas Carlini, Ian Goodfellow, Garrison Cottrell et al.** · 2019-03-22

<details>
<summary>Abstract</summary>

Adversarial examples are inputs to machine learning models designed by an adversary to cause an incorrect output. So far, adversarial examples have been studied most extensively in the image domain. In this domain, adversarial examples can be constructed by imperceptibly modifying images to cause misclassification, and are practical in the physical world. In contrast, current targeted adversarial examples applied to speech recognition systems have neither of these properties: humans can easily identify the adversarial perturbations, and they are not effective when played over-the-air. This paper makes advances on both of these fronts. First, we develop effectively imperceptible audio adversarial examples (verified through a human study) by leveraging the psychoacoustic principle of auditory masking, while retaining 100% targeted success rate on arbitrary full-sentence targets. Next, we make progress towards physical-world over-the-air audio adversarial examples by constructing perturbations which remain effective even after applying realistic simulated environmental distortions.

</details>

### [Unsupervised Speech Enhancement Based on Multichannel NMF-Informed Beamforming for Noise-Robust Automatic Speech Recognition](1903.09341.md)
**Kazuki Shimada, Yoshiaki Bando, Masato Mimura, Katsutoshi Itoyama et al.** · 2019-03-22

<details>
<summary>Abstract</summary>

This paper describes multichannel speech enhancement for improving automatic speech recognition (ASR) in noisy environments. Recently, the minimum variance distortionless response (MVDR) beamforming has widely been used because it works well if the steering vector of speech and the spatial covariance matrix (SCM) of noise are given. To estimating such spatial information, conventional studies take a supervised approach that classifies each time-frequency (TF) bin into noise or speech by training a deep neural network (DNN). The performance of ASR, however, is degraded in an unknown noisy environment. To solve this problem, we take an unsupervised approach that decomposes each TF bin into the sum of speech and noise by using multichannel nonnegative matrix factorization (MNMF). This enables us to accurately estimate the SCMs of speech and noise not from observed noisy mixtures but from separated speech and noise components. In this paper we propose online MVDR beamforming by effectively initializing and incrementally updating the parameters of MNMF. Another main contribution is to comprehensively investigate the performances of ASR obtained by various types of spatial filters, i.e., time-invariant and variant versions of MVDR beamformers and those of rank-1 and full-rank multichannel Wiener filters, in combination with MNMF. The experimental results showed that the proposed method outperformed the state-of-the-art DNN-based beamforming method in unknown environments that did not match training data.

</details>

### [Evaluating Sequence-to-Sequence Models for Handwritten Text Recognition](1903.07377.md)
**Johannes Michael, Roger Labahn, Tobias Grüning, Jochen Zöllner** · 2019-03-18

<details>
<summary>Abstract</summary>

Encoder-decoder models have become an effective approach for sequence learning tasks like machine translation, image captioning and speech recognition, but have yet to show competitive results for handwritten text recognition. To this end, we propose an attention-based sequence-to-sequence model. It combines a convolutional neural network as a generic feature extractor with a recurrent neural network to encode both the visual information, as well as the temporal context between characters in the input image, and uses a separate recurrent neural network to decode the actual character sequence. We make experimental comparisons between various attention mechanisms and positional encodings, in order to find an appropriate alignment between the input and output sequence. The model can be trained end-to-end and the optional integration of a hybrid loss allows the encoder to retain an interpretable and usable output, if desired. We achieve competitive results on the IAM and ICFHR2016 READ data sets compared to the state-of-the-art without the use of a language model, and we significantly improve over any recent sequence-to-sequence approaches.

</details>

### [Automatic assessment of spoken language proficiency of non-native children](1903.06409.md)
**Roberto Gretter, Katharina Allgaier, Svetlana Tchistiakova, Daniele Falavigna** · 2019-03-15

<details>
<summary>Abstract</summary>

This paper describes technology developed to automatically grade Italian students (ages 9-16) on their English and German spoken language proficiency. The students' spoken answers are first transcribed by an automatic speech recognition (ASR) system and then scored using a feedforward neural network (NN) that processes features extracted from the automatic transcriptions. In-domain acoustic models, employing deep neural networks (DNNs), are derived by adapting the parameters of an original out of domain DNN.

</details>

### [Audiovisual Speaker Tracking using Nonlinear Dynamical Systems with Dynamic Stream Weights](1903.06031.md)
**Christopher Schymura, Dorothea Kolossa** · 2019-03-14

<details>
<summary>Abstract</summary>

Data fusion plays an important role in many technical applications that require efficient processing of multimodal sensory observations. A prominent example is audiovisual signal processing, which has gained increasing attention in automatic speech recognition, speaker localization and related tasks. If appropriately combined with acoustic information, additional visual cues can help to improve the performance in these applications, especially under adverse acoustic conditions. A dynamic weighting of acoustic and visual streams based on instantaneous sensor reliability measures is an efficient approach to data fusion in this context. This paper presents a framework that extends the well-established theory of nonlinear dynamical systems with the notion of dynamic stream weights for an arbitrary number of sensory observations. It comprises a recursive state estimator based on the Gaussian filtering paradigm, which incorporates dynamic stream weights into a framework closely related to the extended Kalman filter. Additionally, a convex optimization approach to estimate oracle dynamic stream weights in fully observed dynamical systems utilizing a Dirichlet prior is presented. This serves as a basis for a generic parameter learning framework of dynamic stream weight estimators. The proposed system is application-independent and can be easily adapted to specific tasks and requirements. A study using audiovisual speaker tracking tasks is considered as an exemplary application in this work. An improved tracking performance of the dynamic stream weight-based estimation framework over state-of-the-art methods is demonstrated in the experiments.

</details>

### [Multi-Geometry Spatial Acoustic Modeling for Distant Speech Recognition](1903.06539.md)
**Kenichi Kumatani, Minhua Wu, Shiva Sundaram, Nikko Strom et al.** · 2019-03-13

<details>
<summary>Abstract</summary>

The use of spatial information with multiple microphones can improve far-field automatic speech recognition (ASR) accuracy. However, conventional microphone array techniques degrade speech enhancement performance when there is an array geometry mismatch between design and test conditions. Moreover, such speech enhancement techniques do not always yield ASR accuracy improvement due to the difference between speech enhancement and ASR optimization objectives. In this work, we propose to unify an acoustic model framework by optimizing spatial filtering and long short-term memory (LSTM) layers from multi-channel (MC) input. Our acoustic model subsumes beamformers with multiple types of array geometry. In contrast to deep clustering methods that treat a neural network as a black box tool, the network encoding the spatial filters can process streaming audio data in real time without the accumulation of target signal statistics. We demonstrate the effectiveness of such MC neural networks through ASR experiments on the real-world far-field data. We show that our two-channel acoustic model can on average reduce word error rates (WERs) by~13.4 and~12.7% compared to a single channel ASR system with the log-mel filter bank energy (LFBE) feature under the matched and mismatched microphone placement conditions, respectively. Our result also shows that our two-channel network achieves a relative WER reduction of over~7.0% compared to conventional beamforming with seven microphones overall.

</details>

### [Frequency Domain Multi-channel Acoustic Modeling for Distant Speech Recognition](1903.05299.md)
**Minhua Wu, Kenichi Kumatani, Shiva Sundaram, Nikko Strom et al.** · 2019-03-13

<details>
<summary>Abstract</summary>

Conventional far-field automatic speech recognition (ASR) systems typically employ microphone array techniques for speech enhancement in order to improve robustness against noise or reverberation. However, such speech enhancement techniques do not always yield ASR accuracy improvement because the optimization criterion for speech enhancement is not directly relevant to the ASR objective. In this work, we develop new acoustic modeling techniques that optimize spatial filtering and long short-term memory (LSTM) layers from multi-channel (MC) input based on an ASR criterion directly. In contrast to conventional methods, we incorporate array processing knowledge into the acoustic model. Moreover, we initialize the network with beamformers' coefficients. We investigate effects of such MC neural networks through ASR experiments on the real-world far-field data where users are interacting with an ASR system in uncontrolled acoustic environments. We show that our MC acoustic model can reduce a word error rate (WER) by~16.5\% compared to a single channel ASR system with the traditional log-mel filter bank energy (LFBE) feature on average. Our result also shows that our network with the spatial filtering layer on two-channel input achieves a relative WER reduction of~9.5\% compared to conventional beamforming with seven microphones.

</details>

### [End-To-End Speech Recognition Using A High Rank LSTM-CTC Based Model](1903.05261.md)
**Yangyang Shi, Mei-Yuh Hwang, Xin Lei** · 2019-03-12

<details>
<summary>Abstract</summary>

Long Short Term Memory Connectionist Temporal Classification (LSTM-CTC) based end-to-end models are widely used in speech recognition due to its simplicity in training and efficiency in decoding. In conventional LSTM-CTC based models, a bottleneck projection matrix maps the hidden feature vectors obtained from LSTM to softmax output layer. In this paper, we propose to use a high rank projection layer to replace the projection matrix. The output from the high rank projection layer is a weighted combination of vectors that are projected from the hidden feature vectors via different projection matrices and non-linear activation function. The high rank projection layer is able to improve the expressiveness of LSTM-CTC models. The experimental results show that on Wall Street Journal (WSJ) corpus and LibriSpeech data set, the proposed method achieves 4%-6% relative word error rate (WER) reduction over the baseline CTC system. They outperform other published CTC based end-to-end (E2E) models under the condition that no external data or data augmentation is applied. Code has been made available at https://github.com/mobvoi/lstm_ctc.

</details>

### [Bridging the Gap Between Monaural Speech Enhancement and Recognition with Distortion-Independent Acoustic Modeling](1903.04567.md)
**Peidong Wang, Ke Tan, DeLiang Wang** · 2019-03-11

<details>
<summary>Abstract</summary>

Monaural speech enhancement has made dramatic advances since the introduction of deep learning a few years ago. Although enhanced speech has been demonstrated to have better intelligibility and quality for human listeners, feeding it directly to automatic speech recognition (ASR) systems trained with noisy speech has not produced expected improvements in ASR performance. The lack of an enhancement benefit on recognition, or the gap between monaural speech enhancement and recognition, is often attributed to speech distortions introduced in the enhancement process. In this study, we analyze the distortion problem, compare different acoustic models, and investigate a distortion-independent training scheme for monaural speech recognition. Experimental results suggest that distortion-independent acoustic modeling is able to overcome the distortion problem. Such an acoustic model can also work with speech enhancement models different from the one used during training. Moreover, the models investigated in this paper outperform the previous best system on the CHiME-2 corpus.

</details>

### [Accelerating Minibatch Stochastic Gradient Descent using Typicality Sampling](1903.04192.md)
**Xinyu Peng, Li Li, Fei-Yue Wang** · 2019-03-11

<details>
<summary>Abstract</summary>

Machine learning, especially deep neural networks, has been rapidly developed in fields including computer vision, speech recognition and reinforcement learning. Although Mini-batch SGD is one of the most popular stochastic optimization methods in training deep networks, it shows a slow convergence rate due to the large noise in gradient approximation. In this paper, we attempt to remedy this problem by building more efficient batch selection method based on typicality sampling, which reduces the error of gradient estimation in conventional Minibatch SGD. We analyze the convergence rate of the resulting typical batch SGD algorithm and compare convergence properties between Minibatch SGD and the algorithm. Experimental results demonstrate that our batch selection scheme works well and more complex Minibatch SGD variants can benefit from the proposed batch selection strategy.

</details>

### [Neural Network Model Extraction Attacks in Edge Devices by Hearing Architectural Hints](1903.03916.md)
**Xing Hu, Ling Liang, Lei Deng, Shuangchen Li et al.** · 2019-03-10

<details>
<summary>Abstract</summary>

As neural networks continue their reach into nearly every aspect of software operations, the details of those networks become an increasingly sensitive subject. Even those that deploy neural networks embedded in physical devices may wish to keep the inner working of their designs hidden -- either to protect their intellectual property or as a form of protection from adversarial inputs. The specific problem we address is how, through heavy system stack, given noisy and imperfect memory traces, one might reconstruct the neural network architecture including the set of layers employed, their connectivity, and their respective dimension sizes. Considering both the intra-layer architecture features and the inter-layer temporal association information introduced by the DNN design empirical experience, we draw upon ideas from speech recognition to solve this problem. We show that off-chip memory address traces and PCIe events provide ample information to reconstruct such neural network architectures accurately. We are the first to propose such accurate model extraction techniques and demonstrate an end-to-end attack experimentally in the context of an off-the-shelf Nvidia GPU platform with full system stack. Results show that the proposed techniques achieve a high reverse engineering accuracy and improve the one's ability to conduct targeted adversarial attack with success rate from 14.6\%$\sim$25.5\% (without network architecture knowledge) to 75.9\% (with extracted network architecture).

</details>

### [The Virtual Doctor: An Interactive Artificial Intelligence based on Deep Learning for Non-Invasive Prediction of Diabetes](1903.12069.md)
**Sebastian Spänig, Agnes Emberger-Klein, Jan-Peter Sowa, Ali Canbay et al.** · 2019-03-09

<details>
<summary>Abstract</summary>

Artificial intelligence (AI) will pave the way to a new era in medicine. However, currently available AI systems do not interact with a patient, e.g., for anamnesis, and thus are only used by the physicians for predictions in diagnosis or prognosis. However, these systems are widely used, e.g., in diabetes or cancer prediction. In the current study, we developed an AI that is able to interact with a patient (virtual doctor) by using a speech recognition and speech synthesis system and thus can autonomously interact with the patient, which is particularly important for, e.g., rural areas, where the availability of primary medical care is strongly limited by low population densities. As a proof-of-concept, the system is able to predict type 2 diabetes mellitus (T2DM) based on non-invasive sensors and deep neural networks. Moreover, the system provides an easy-to-interpret probability estimation for T2DM for a given patient. Besides the development of the AI, we further analyzed the acceptance of young people for AI in healthcare to estimate the impact of such system in the future.

</details>

### [Active and Semi-Supervised Learning in ASR: Benefits on the Acoustic and Language Models](1903.02852.md)
**Thomas Drugman, Janne Pylkkonen, Reinhard Kneser** · 2019-03-07

<details>
<summary>Abstract</summary>

The goal of this paper is to simulate the benefits of jointly applying active learning (AL) and semi-supervised training (SST) in a new speech recognition application. Our data selection approach relies on confidence filtering, and its impact on both the acoustic and language models (AM and LM) is studied. While AL is known to be beneficial to AM training, we show that it also carries out substantial improvements to the LM when combined with SST. Sophisticated confidence models, on the other hand, did not prove to yield any data selection gain. Our results indicate that, while SST is crucial at the beginning of the labeling process, its gains degrade rapidly as AL is set in place. The final simulation reports that AL allows a transcription cost reduction of about 70% over random selection. Alternatively, for a fixed transcription budget, the proposed approach improves the word error rate by about 12.5% relative.

</details>

### [Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction](1903.00888.md)
**Bo Li, Kele Xu, Dawei Feng, Haibo Mi et al.** · 2019-03-03

<details>
<summary>Abstract</summary>

B-mode ultrasound tongue imaging is widely used in the speech production field. However, efficient interpretation is in a great need for the tongue image sequences. Inspired by the recent success of unsupervised deep learning approach, we explore unsupervised convolutional network architecture for the feature extraction in the ultrasound tongue image, which can be helpful for the clinical linguist and phonetics. By quantitative comparison between different unsupervised feature extraction approaches, the denoising convolutional autoencoder (DCAE)-based method outperforms the other feature extraction methods on the reconstruction task and the 2010 silent speech interface challenge. A Word Error Rate of 6.17% is obtained with DCAE, compared to the state-of-the-art value of 6.45% using Discrete cosine transform as the feature extractor. Our codes are available at https://github.com/DeePBluE666/Source-code1.

</details>

### [KT-Speech-Crawler: Automatic Dataset Construction for Speech Recognition from YouTube Videos](1903.00216.md)
**Egor Lakomkin, Sven Magg, Cornelius Weber, Stefan Wermter** · 2019-03-01

<details>
<summary>Abstract</summary>

In this paper, we describe KT-Speech-Crawler: an approach for automatic dataset construction for speech recognition by crawling YouTube videos. We outline several filtering and post-processing steps, which extract samples that can be used for training end-to-end neural speech recognition systems. In our experiments, we demonstrate that a single-core version of the crawler can obtain around 150 hours of transcribed speech within a day, containing an estimated 3.5% word error rate in the transcriptions. Automatically collected samples contain reading and spontaneous speech recorded in various conditions including background noise and music, distant microphone recordings, and a variety of accents and reverberation. When training a deep neural network on speech recognition, we observed around 40\% word error rate reduction on the Wall Street Journal dataset by integrating 200 hours of the collected samples into the training set. The demo (http://emnlp-demo.lakomkin.me/) and the crawler code (https://github.com/EgorLakomkin/KTSpeechCrawler) are publicly available.

</details>

### [Incorporating End-to-End Speech Recognition Models for Sentiment Analysis](1902.11245.md)
**Egor Lakomkin, Mohammad Ali Zamani, Cornelius Weber, Sven Magg et al.** · 2019-02-28

<details>
<summary>Abstract</summary>

Previous work on emotion recognition demonstrated a synergistic effect of combining several modalities such as auditory, visual, and transcribed text to estimate the affective state of a speaker. Among these, the linguistic modality is crucial for the evaluation of an expressed emotion. However, manually transcribed spoken text cannot be given as input to a system practically. We argue that using ground-truth transcriptions during training and evaluation phases leads to a significant discrepancy in performance compared to real-world conditions, as the spoken text has to be recognized on the fly and can contain speech recognition mistakes. In this paper, we propose a method of integrating an automatic speech recognition (ASR) output with a character-level recurrent neural network for sentiment recognition. In addition, we conduct several experiments investigating sentiment recognition for human-robot interaction in a noise-realistic scenario which is challenging for the ASR systems. We quantify the improvement compared to using only the acoustic modality in sentiment recognition. We demonstrate the effectiveness of this approach on the Multimodal Corpus of Sentiment Intensity (MOSI) by achieving 73,6% accuracy in a binary sentiment classification task, exceeding previously reported results that use only acoustic input. In addition, we set a new state-of-the-art performance on the MOSI dataset (80.4% accuracy, 2% absolute improvement).

</details>

### [Context-aware Neural-based Dialog Act Classification on Automatically Generated Transcriptions](1902.11060.md)
**Daniel Ortega, Chia-Yu Li, Gisela Vallejo, Pavel Denisov et al.** · 2019-02-28

<details>
<summary>Abstract</summary>

This paper presents our latest investigations on dialog act (DA) classification on automatically generated transcriptions. We propose a novel approach that combines convolutional neural networks (CNNs) and conditional random fields (CRFs) for context modeling in DA classification. We explore the impact of transcriptions generated from different automatic speech recognition systems such as hybrid TDNN/HMM and End-to-End systems on the final performance. Experimental results on two benchmark datasets (MRDA and SwDA) show that the combination CNN and CRF improves consistently the accuracy. Furthermore, they show that although the word error rates are comparable, End-to-End ASR system seems to be more suitable for DA classification.

</details>

### [Vehicle Classification Based on Seismic Signatures with Weighted Intrinsic Mode Functions](1902.09981.md)
**Guozheng Jin** · 2019-02-24

<details>
<summary>Abstract</summary>

Seismic signal is used for vehicle classification widely. However, this task becomes difficult as a result of various noises. To solve the problem, this paper proposes a novel de-noising algorithm which evolves from a nonparametric adaptive tool named empirical mode decomposition (EMD). EMD can decompose signals into a set of zero-mean modes called intrinsic mode functions (IMFs) that can be used to denoise a signal. Unlike other EMD-based de-noising techniques, selecting the noise-free modes to denoise signals, this paper assigns appropriate weights to the modes. In addition, considering the similarities between speech recognition and seismic vehicle classification, an algorithm scheme, consisting of improved Mel frequency cepstral coefficient (MFCC) and artificial neural network, is applied to recognize seismic signals for vehicle targets. The data from DARPA's SensIt project, which contains various seismic signatures from two different vehicle types, is used to evaluate the method. Through experiments, results demonstrate the efficacy of proposed algorithm as compared to traditional MFCC.

</details>

### [The NIGENS General Sound Events Database](1902.08314.md)
**Ivo Trowitzsch, Jalil Taghia, Youssef Kashef, Klaus Obermayer** · 2019-02-21

<details>
<summary>Abstract</summary>

Computational auditory scene analysis is gaining interest in the last years. Trailing behind the more mature field of speech recognition, it is particularly general sound event detection that is attracting increasing attention. Crucial for training and testing reasonable models is having available enough suitable data -- until recently, general sound event databases were hardly found. We release and present a database with 714 wav files containing isolated high quality sound events of 14 different types, plus 303 `general' wav files of anything else but these 14 types. All sound events are strongly labeled with perceptual on- and offset times, paying attention to omitting in-between silences. The amount of isolated sound events, the quality of annotations, and the particular general sound class distinguish NIGENS from other databases.

</details>

### [All-neural online source separation, counting, and diarization for meeting analysis](1902.07881.md)
**Thilo von Neumann, Keisuke Kinoshita, Marc Delcroix, Shoko Araki et al.** · 2019-02-21

<details>
<summary>Abstract</summary>

Automatic meeting analysis comprises the tasks of speaker counting, speaker diarization, and the separation of overlapped speech, followed by automatic speech recognition. This all has to be carried out on arbitrarily long sessions and, ideally, in an online or block-online manner. While significant progress has been made on individual tasks, this paper presents for the first time an all-neural approach to simultaneous speaker counting, diarization and source separation. The NN-based estimator operates in a block-online fashion and tracks speakers even if they remain silent for a number of time blocks, thus learning a stable output order for the separated sources. The neural network is recurrent over time as well as over the number of sources. The simulation experiments show that state of the art separation performance is achieved, while at the same time delivering good diarization and source counting results. It even generalizes well to an unseen large number of blocks.

</details>

### [STFNets: Learning Sensing Signals from the Time-Frequency Perspective with Short-Time Fourier Neural Networks](1902.07849.md)
**Shuochao Yao, Ailing Piao, Wenjun Jiang, Yiran Zhao et al.** · 2019-02-21

<details>
<summary>Abstract</summary>

Recent advances in deep learning motivate the use of deep neural networks in Internet-of-Things (IoT) applications. These networks are modelled after signal processing in the human brain, thereby leading to significant advantages at perceptual tasks such as vision and speech recognition. IoT applications, however, often measure physical phenomena, where the underlying physics (such as inertia, wireless signal propagation, or the natural frequency of oscillation) are fundamentally a function of signal frequencies, offering better features in the frequency domain. This observation leads to a fundamental question: For IoT applications, can one develop a new brand of neural network structures that synthesize features inspired not only by the biology of human perception but also by the fundamental nature of physics? Hence, in this paper, instead of using conventional building blocks (e.g., convolutional and recurrent layers), we propose a new foundational neural network building block, the Short-Time Fourier Neural Network (STFNet). It integrates a widely-used time-frequency analysis method, the Short-Time Fourier Transform, into data processing to learn features directly in the frequency domain, where the physics of underlying phenomena leave better foot-prints. STFNets bring additional flexibility to time-frequency analysis by offering novel nonlinear learnable operations that are spectral-compatible. Moreover, STFNets show that transforming signals to a domain that is more connected to the underlying physics greatly simplifies the learning process. We demonstrate the effectiveness of STFNets with extensive experiments. STFNets significantly outperform the state-of-the-art deep learning models in all experiments. A STFNet, therefore, demonstrates superior capability as the fundamental building block of deep neural networks for IoT applications for various sensor inputs.

</details>

### [Audio-Linguistic Embeddings for Spoken Sentences](1902.07817.md)
**Albert Haque, Michelle Guo, Prateek Verma, Li Fei-Fei** · 2019-02-20

<details>
<summary>Abstract</summary>

We propose spoken sentence embeddings which capture both acoustic and linguistic content. While existing works operate at the character, phoneme, or word level, our method learns long-term dependencies by modeling speech at the sentence level. Formulated as an audio-linguistic multitask learning problem, our encoder-decoder model simultaneously reconstructs acoustic and natural language features from audio. Our results show that spoken sentence embeddings outperform phoneme and word-level baselines on speech recognition and emotion recognition tasks. Ablation studies show that our embeddings can better model high-level acoustic concepts while retaining linguistic content. Overall, our work illustrates the viability of generic, multi-modal sentence embeddings for spoken language understanding.

</details>

### [Learning with Inadequate and Incorrect Supervision](1902.07429.md)
**Chen Gong, Hengmin Zhang, Jian Yang, Dacheng Tao** · 2019-02-20

<details>
<summary>Abstract</summary>

Practically, we are often in the dilemma that the labeled data at hand are inadequate to train a reliable classifier, and more seriously, some of these labeled data may be mistakenly labeled due to the various human factors. Therefore, this paper proposes a novel semi-supervised learning paradigm that can handle both label insufficiency and label inaccuracy. To address label insufficiency, we use a graph to bridge the data points so that the label information can be propagated from the scarce labeled examples to unlabeled examples along the graph edges. To address label inaccuracy, Graph Trend Filtering (GTF) and Smooth Eigenbase Pursuit (SEP) are adopted to filter out the initial noisy labels. GTF penalizes the l_0 norm of label difference between connected examples in the graph and exhibits better local adaptivity than the traditional l_2 norm-based Laplacian smoother. SEP reconstructs the correct labels by emphasizing the leading eigenvectors of Laplacian matrix associated with small eigenvalues, as these eigenvectors reflect real label smoothness and carry rich class separation cues. We term our algorithm as `Semi-supervised learning under Inadequate and Incorrect Supervision' (SIIS). Thorough experimental results on image classification, text categorization, and speech recognition demonstrate that our SIIS is effective in label error correction, leading to superior performance to the state-of-the-art methods in the presence of label noise and label scarcity.

</details>

### [Phoneme Level Language Models for Sequence Based Low Resource ASR](1902.07613.md)
**Siddharth Dalmia, Xinjian Li, Alan W Black, Florian Metze** · 2019-02-20

<details>
<summary>Abstract</summary>

Building multilingual and crosslingual models help bring different languages together in a language universal space. It allows models to share parameters and transfer knowledge across languages, enabling faster and better adaptation to a new language. These approaches are particularly useful for low resource languages. In this paper, we propose a phoneme-level language model that can be used multilingually and for crosslingual adaptation to a target language. We show that our model performs almost as well as the monolingual models by using six times fewer parameters, and is capable of better adaptation to languages not seen during training in a low resource scenario. We show that these phoneme-level language models can be used to decode sequence based Connectionist Temporal Classification (CTC) acoustic model outputs to obtain comparable word error rates with Weighted Finite State Transducer (WFST) based decoding in Babel languages. We also show that these phoneme-level language models outperform WFST decoding in various low-resource conditions like adapting to a new language and domain mismatch between training and testing data.

</details>

### [A spelling correction model for end-to-end speech recognition](1902.07178.md)
**Jinxi Guo, Tara N. Sainath, Ron J. Weiss** · 2019-02-19

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence models for speech recognition jointly train an acoustic model, language model (LM), and alignment mechanism using a single neural network and require only parallel audio-text pairs. Thus, the language model component of the end-to-end model is only trained on transcribed audio-text pairs, which leads to performance degradation especially on rare words. While there have been a variety of work that look at incorporating an external LM trained on text-only data into the end-to-end framework, none of them have taken into account the characteristic error distribution made by the model. In this paper, we propose a novel approach to utilizing text-only data, by training a spelling correction (SC) model to explicitly correct those errors. On the LibriSpeech dataset, we demonstrate that the proposed model results in an 18.6% relative improvement in WER over the baseline model when directly correcting top ASR hypothesis, and a 29.0% relative improvement when further rescoring an expanded n-best list using an external LM.

</details>

### [Learned In Speech Recognition: Contextual Acoustic Word Embeddings](1902.06833.md)
**Shruti Palaskar, Vikas Raunak, Florian Metze** · 2019-02-18

<details>
<summary>Abstract</summary>

End-to-end acoustic-to-word speech recognition models have recently gained popularity because they are easy to train, scale well to large amounts of training data, and do not require a lexicon. In addition, word models may also be easier to integrate with downstream tasks such as spoken language understanding, because inference (search) is much simplified compared to phoneme, character or any other sort of sub-word units. In this paper, we describe methods to construct contextual acoustic word embeddings directly from a supervised sequence-to-sequence acoustic-to-word speech recognition model using the learned attention distribution. On a suite of 16 standard sentence evaluation tasks, our embeddings show competitive performance against a word2vec model trained on the speech transcriptions. In addition, we evaluate these embeddings on a spoken language understanding task, and observe that our embeddings match the performance of text-based embeddings in a pipeline of first performing speech recognition and then constructing word embeddings from transcriptions.

</details>

### [Self-Attention Aligner: A Latency-Control End-to-End Model for ASR Using Self-Attention Network and Chunk-Hopping](1902.06450.md)
**Linhao Dong, Feng Wang, Bo Xu** · 2019-02-18

<details>
<summary>Abstract</summary>

Self-attention network, an attention-based feedforward neural network, has recently shown the potential to replace recurrent neural networks (RNNs) in a variety of NLP tasks. However, it is not clear if the self-attention network could be a good alternative of RNNs in automatic speech recognition (ASR), which processes the longer speech sequences and may have online recognition requirements. In this paper, we present a RNN-free end-to-end model: self-attention aligner (SAA), which applies the self-attention networks to a simplified recurrent neural aligner (RNA) framework. We also propose a chunk-hopping mechanism, which enables the SAA model to encode on segmented frame chunks one after another to support online recognition. Experiments on two Mandarin ASR datasets show the replacement of RNNs by the self-attention networks yields a 8.4%-10.2% relative character error rate (CER) reduction. In addition, the chunk-hopping mechanism allows the SAA to have only a 2.5% relative CER degradation with a 320ms latency. After jointly training with a self-attention network language model, our SAA model obtains further error rate reduction on multiple datasets. Especially, it achieves 24.12% CER on the Mandarin ASR benchmark (HKUST), exceeding the best end-to-end model by over 2% absolute CER.

</details>

### [A Fully Differentiable Beam Search Decoder](1902.06022.md)
**Ronan Collobert, Awni Hannun, Gabriel Synnaeve** · 2019-02-16

<details>
<summary>Abstract</summary>

We introduce a new beam search decoder that is fully differentiable, making it possible to optimize at training time through the inference procedure. Our decoder allows us to combine models which operate at different granularities (e.g. acoustic and language models). It can be used when target sequences are not aligned to input sequences by considering all possible alignments between the two. We demonstrate our approach scales by applying it to speech recognition, jointly training acoustic and word-level language models. The system is end-to-end, with gradients flowing through the whole architecture from the word-level transcriptions. Recent research efforts have shown that deep neural networks with attention-based mechanisms are powerful enough to successfully train an acoustic model from the final transcription, while implicitly learning a language model. Instead, we show that it is possible to discriminatively train an acoustic model jointly with an explicit and possibly pre-trained language model.

</details>

### [Enhanced Robot Speech Recognition Using Biomimetic Binaural Sound Source Localization](1902.05446.md)
**Jorge, Davila-Chacon, Jindong, Liu et al.** · 2019-02-13

<details>
<summary>Abstract</summary>

Inspired by the behavior of humans talking in noisy environments, we propose an embodied embedded cognition approach to improve automatic speech recognition (ASR) systems for robots in challenging environments, such as with ego noise, using binaural sound source localization (SSL). The approach is verified by measuring the impact of SSL with a humanoid robot head on the performance of an ASR system. More specifically, a robot orients itself toward the angle where the signal-to-noise ratio (SNR) of speech is maximized for one microphone before doing an ASR task. First, a spiking neural network inspired by the midbrain auditory system based on our previous work is applied to calculate the sound signal angle. Then, a feedforward neural network is used to handle high levels of ego noise and reverberation in the signal. Finally, the sound signal is fed into an ASR system. For ASR, we use a system developed by our group and compare its performance with and without the support from SSL. We test our SSL and ASR systems on two humanoid platforms with different structural and material properties. With our approach we halve the sentence error rate with respect to the common downmixing of both channels. Surprisingly, the ASR performance is more than two times better when the angle between the humanoid head and the sound source allows sound waves to be reflected most intensely from the pinna to the ear microphone, rather than when sound waves arrive perpendicularly to the membrane.

</details>

### [Towards a Robust Deep Neural Network in Texts: A Survey](1902.07285.md)
**Wenqi Wang, Run Wang, Lina Wang, Zhibo Wang et al.** · 2019-02-12

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have achieved remarkable success in various tasks (e.g., image classification, speech recognition, and natural language processing (NLP)). However, researchers have demonstrated that DNN-based models are vulnerable to adversarial examples, which cause erroneous predictions by adding imperceptible perturbations into legitimate inputs. Recently, studies have revealed adversarial examples in the text domain, which could effectively evade various DNN-based text analyzers and further bring the threats of the proliferation of disinformation. In this paper, we give a comprehensive survey on the existing studies of adversarial techniques for generating adversarial texts written by both English and Chinese characters and the corresponding defense methods. More importantly, we hope that our work could inspire future studies to develop more robust DNN-based text analyzers against known and unknown adversarial techniques. We classify the existing adversarial techniques for crafting adversarial texts based on the perturbation units, helping to better understand the generation of adversarial texts and build robust models for defense. In presenting the taxonomy of adversarial attacks and defenses in the text domain, we introduce the adversarial techniques from the perspective of different NLP tasks. Finally, we discuss the existing challenges of adversarial attacks and defenses in texts and present the future research directions in this emerging and challenging field.

</details>

### [Deep learning and face recognition: the state of the art](1902.03524.md)
**Stephen Balaban** · 2019-02-10

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) have established themselves as a dominant technique in machine learning. DNNs have been top performers on a wide variety of tasks including image classification, speech recognition, and face recognition. Convolutional neural networks (CNNs) have been used in nearly all of the top performing methods on the Labeled Faces in the Wild (LFW) dataset. In this talk and accompanying paper, I attempt to provide a review and summary of the deep learning techniques used in the state-of-the-art. In addition, I highlight the need for both larger and more challenging public datasets to benchmark these systems. The high accuracy (99.63% for FaceNet at the time of publishing) and utilization of outside data (hundreds of millions of images in the case of Google's FaceNet) suggest that current face verification benchmarks such as LFW may not be challenging enough, nor provide enough data, for current techniques. There exist a variety of organizations with mobile photo sharing applications that would be capable of releasing a very large scale and highly diverse dataset of facial images captured on mobile devices. Such an "ImageNet for Face Recognition" would likely receive a warm welcome from researchers and practitioners alike.

</details>

### [End-to-end Anchored Speech Recognition](1902.02383.md)
**Yiming Wang, Xing Fan, I-Fan Chen, Yuzong Liu et al.** · 2019-02-06

<details>
<summary>Abstract</summary>

Voice-controlled house-hold devices, like Amazon Echo or Google Home, face the problem of performing speech recognition of device-directed speech in the presence of interfering background speech, i.e., background noise and interfering speech from another person or media device in proximity need to be ignored. We propose two end-to-end models to tackle this problem with information extracted from the "anchored segment". The anchored segment refers to the wake-up word part of an audio stream, which contains valuable speaker information that can be used to suppress interfering speech and background noise. The first method is called "Multi-source Attention" where the attention mechanism takes both the speaker information and decoder state into consideration. The second method directly learns a frame-level mask on top of the encoder output. We also explore a multi-task learning setup where we use the ground truth of the mask to guide the learner. Given that audio data with interfering speech is rare in our training data set, we also propose a way to synthesize "noisy" speech from "clean" speech to mitigate the mismatch between training and test data. Our proposed methods show up to 15% relative reduction in WER for Amazon Alexa live data with interfering background speech without significantly degrading on clean speech.

</details>

### [On the Choice of Modeling Unit for Sequence-to-Sequence Speech Recognition](1902.01955.md)
**Kazuki Irie, Rohit Prabhavalkar, Anjuli Kannan, Antoine Bruguier et al.** · 2019-02-05

<details>
<summary>Abstract</summary>

In conventional speech recognition, phoneme-based models outperform grapheme-based models for non-phonetic languages such as English. The performance gap between the two typically reduces as the amount of training data is increased. In this work, we examine the impact of the choice of modeling unit for attention-based encoder-decoder models. We conduct experiments on the LibriSpeech 100hr, 460hr, and 960hr tasks, using various target units (phoneme, grapheme, and word-piece); across all tasks, we find that grapheme or word-piece models consistently outperform phoneme-based models, even though they are evaluated without a lexicon or an external language model. We also investigate model complementarity: we find that we can improve WERs by up to 9% relative by rescoring N-best lists generated from a strong word-piece based baseline with either the phoneme or the grapheme model. Rescoring an N-best list generated by the phonemic system, however, provides limited improvements. Further analysis shows that the word-piece-based models produce more diverse N-best hypotheses, and thus lower oracle WERs, than phonemic models.

</details>

### [Using multi-task learning to improve the performance of acoustic-to-word and conventional hybrid models](1902.01951.md)
**Thai-Son Nguyen, Sebastian Stueker, Alex Waibel** · 2019-02-02

<details>
<summary>Abstract</summary>

Acoustic-to-word (A2W) models that allow direct mapping from acoustic signals to word sequences are an appealing approach to end-to-end automatic speech recognition due to their simplicity. However, prior works have shown that modelling A2W typically encounters issues of data sparsity that prevent training such a model directly. So far, pre-training initialization is the only approach proposed to deal with this issue. In this work, we propose to build a shared neural network and optimize A2W and conventional hybrid models in a multi-task manner. Our results show that training an A2W model is much more stable with our multi-task model without pre-training initialization, and results in a significant improvement compared to a baseline model. Experiments also reveal that the performance of a hybrid acoustic model can be further improved when jointly training with a sequence-level optimization criterion such as acoustic-to-word.

</details>

### [Speech Recognition Using Deep Neural Networks: A Systematic Review](s2:29650544fded20dd5b2fc49f60f9a3ad30d0e275.md)
**Ali Bou Nassif, I. Shahin, Imtinan B. Attili, Mohammad Azzeh et al.** · 2019-02-01

<details>
<summary>Abstract</summary>

Over the past decades, a tremendous amount of research has been done on the use of machine learning for speech processing applications, especially speech recognition. However, in the past few years, research has focused on utilizing deep learning for speech-related applications. This new area of machine learning has yielded far better results when compared to others in a variety of applications including speech, and thus became a very attractive area of research. This paper provides a thorough examination of the different studies that have been conducted since 2006, when deep learning first arose as a new area of machine learning, for speech applications. A thorough statistical analysis is provided in this review which was conducted by extracting specific information from 174 papers published between the years 2006 and 2018. The results provided in this paper shed light on the trends of research in this area as well as bring focus to new research topics.

</details>

### [Hardware-Guided Symbiotic Training for Compact, Accurate, yet Execution-Efficient LSTM](1901.10997.md)
**Hongxu Yin, Guoyang Chen, Yingmin Li, Shuai Che et al.** · 2019-01-30

<details>
<summary>Abstract</summary>

Many long short-term memory (LSTM) applications need fast yet compact models. Neural network compression approaches, such as the grow-and-prune paradigm, have proved to be promising for cutting down network complexity by skipping insignificant weights. However, current compression strategies are mostly hardware-agnostic and network complexity reduction does not always translate into execution efficiency. In this work, we propose a hardware-guided symbiotic training methodology for compact, accurate, yet execution-efficient inference models. It is based on our observation that hardware may introduce substantial non-monotonic behavior, which we call the latency hysteresis effect, when evaluating network size vs. inference latency. This observation raises question about the mainstream smaller-dimension-is-better compression strategy, which often leads to a sub-optimal model architecture. By leveraging the hardware-impacted hysteresis effect and sparsity, we are able to achieve the symbiosis of model compactness and accuracy with execution efficiency, thus reducing LSTM latency while increasing its accuracy. We have evaluated our algorithms on language modeling and speech recognition applications. Relative to the traditional stacked LSTM architecture obtained for the Penn Treebank dataset, we reduce the number of parameters by 18.0x (30.5x) and measured run-time latency by up to 2.4x (5.2x) on Nvidia GPUs (Intel Xeon CPUs) without any accuracy degradation. For the DeepSpeech2 architecture obtained for the AN4 dataset, we reduce the number of parameters by 7.0x (19.4x), word error rate from 12.9% to 9.9% (10.4%), and measured run-time latency by up to 1.7x (2.4x) on Nvidia GPUs (Intel Xeon CPUs). Thus, our method yields compact, accurate, yet execution-efficient inference models.

</details>

### [Harnessing GANs for Zero-shot Learning of New Classes in Visual Speech Recognition](1901.10139.md)
**Yaman Kumar, Dhruva Sahrawat, Shubham Maheshwari, Debanjan Mahata et al.** · 2019-01-29

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) is the process of recognizing or interpreting speech by watching the lip movements of the speaker. Recent machine learning based approaches model VSR as a classification problem; however, the scarcity of training data leads to error-prone systems with very low accuracies in predicting unseen classes. To solve this problem, we present a novel approach to zero-shot learning by generating new classes using Generative Adversarial Networks (GANs), and show how the addition of unseen class samples increases the accuracy of a VSR system by a significant margin of 27% and allows it to handle speaker-independent out-of-vocabulary phrases. We also show that our models are language agnostic and therefore capable of seamlessly generating, using English training data, videos for a new language (Hindi). To the best of our knowledge, this is the first work to show empirical evidence of the use of GANs for generating training samples of unseen classes in the domain of VSR, hence facilitating zero-shot learning. We make the added videos for new classes publicly available along with our code.

</details>

### [A Convolutional Neural Network model based on Neutrosophy for Noisy Speech Recognition](1901.10629.md)
**Elyas Rashno, Ahmad Akbari, Babak Nasersharif** · 2019-01-27

<details>
<summary>Abstract</summary>

Convolutional neural networks are sensitive to unknown noisy condition in the test phase and so their performance degrades for the noisy data classification task including noisy speech recognition. In this research, a new convolutional neural network (CNN) model with data uncertainty handling; referred as NCNN (Neutrosophic Convolutional Neural Network); is proposed for classification task. Here, speech signals are used as input data and their noise is modeled as uncertainty. In this task, using speech spectrogram, a definition of uncertainty is proposed in neutrosophic (NS) domain. Uncertainty is computed for each Time-frequency point of speech spectrogram as like a pixel. Therefore, uncertainty matrix with the same size of spectrogram is created in NS domain. In the next step, a two parallel paths CNN classification model is proposed. Speech spectrogram is used as input of the first path and uncertainty matrix for the second path. The outputs of two paths are combined to compute the final output of the classifier. To show the effectiveness of the proposed method, it has been compared with conventional CNN on the isolated words of Aurora2 dataset. The proposed method achieves the average accuracy of 85.96 in noisy train data. It is more robust against Car, Airport and Subway noises with accuracies 90, 88 and 81 in test sets A, B and C, respectively. Results show that the proposed method outperforms conventional CNN with the improvement of 6, 5 and 2 percentage in test set A, test set B and test sets C, respectively. It means that the proposed method is more robust against noisy data and handle these data effectively.

</details>

### [Progressive Label Distillation: Learning Input-Efficient Deep Neural Networks](1901.09135.md)
**Zhong Qiu Lin, Alexander Wong** · 2019-01-26

<details>
<summary>Abstract</summary>

Much of the focus in the area of knowledge distillation has been on distilling knowledge from a larger teacher network to a smaller student network. However, there has been little research on how the concept of distillation can be leveraged to distill the knowledge encapsulated in the training data itself into a reduced form. In this study, we explore the concept of progressive label distillation, where we leverage a series of teacher-student network pairs to progressively generate distilled training data for learning deep neural networks with greatly reduced input dimensions. To investigate the efficacy of the proposed progressive label distillation approach, we experimented with learning a deep limited vocabulary speech recognition network based on generated 500ms input utterances distilled progressively from 1000ms source training data, and demonstrated a significant increase in test accuracy of almost 78% compared to direct learning.

</details>

### [SirenAttack: Generating Adversarial Audio for End-to-End Acoustic Systems](1901.07846.md)
**Tianyu Du, Shouling Ji, Jinfeng Li, Qinchen Gu et al.** · 2019-01-23

<details>
<summary>Abstract</summary>

Despite their immense popularity, deep learning-based acoustic systems are inherently vulnerable to adversarial attacks, wherein maliciously crafted audios trigger target systems to misbehave. In this paper, we present SirenAttack, a new class of attacks to generate adversarial audios. Compared with existing attacks, SirenAttack highlights with a set of significant features: (i) versatile -- it is able to deceive a range of end-to-end acoustic systems under both white-box and black-box settings; (ii) effective -- it is able to generate adversarial audios that can be recognized as specific phrases by target acoustic systems; and (iii) stealthy -- it is able to generate adversarial audios indistinguishable from their benign counterparts to human perception. We empirically evaluate SirenAttack on a set of state-of-the-art deep learning-based acoustic systems (including speech command recognition, speaker recognition and sound event classification), with results showing the versatility, effectiveness, and stealthiness of SirenAttack. For instance, it achieves 99.45% attack success rate on the IEMOCAP dataset against the ResNet18 model, while the generated adversarial audios are also misinterpreted by multiple popular ASR platforms, including Google Cloud Speech, Microsoft Bing Voice, and IBM Speech-to-Text. We further evaluate three potential defense methods to mitigate such attacks, including adversarial training, audio downsampling, and moving average filtering, which leads to promising directions for further research.

</details>

### [Self-Attention Networks for Connectionist Temporal Classification in Speech Recognition](1901.10055.md)
**Julian Salazar, Katrin Kirchhoff, Zhiheng Huang** · 2019-01-22

<details>
<summary>Abstract</summary>

The success of self-attention in NLP has led to recent applications in end-to-end encoder-decoder architectures for speech recognition. Separately, connectionist temporal classification (CTC) has matured as an alignment-free, non-autoregressive approach to sequence transduction, either by itself or in various multitask and decoding frameworks. We propose SAN-CTC, a deep, fully self-attentional network for CTC, and show it is tractable and competitive for end-to-end speech recognition. SAN-CTC trains quickly and outperforms existing CTC models and most encoder-decoder models, with character error rates (CERs) of 4.7% in 1 day on WSJ eval92 and 2.8% in 1 week on LibriSpeech test-clean, with a fixed architecture and one GPU. Similar improvements hold for WERs after LM decoding. We motivate the architecture for speech, evaluate position and downsampling approaches, and explore how label alphabets (character, phoneme, subword) affect attention heads and performance.

</details>

### [Overfitting Mechanism and Avoidance in Deep Neural Networks](1901.06566.md)
**Shaeke Salman, Xiuwen Liu** · 2019-01-19

<details>
<summary>Abstract</summary>

Assisted by the availability of data and high performance computing, deep learning techniques have achieved breakthroughs and surpassed human performance empirically in difficult tasks, including object recognition, speech recognition, and natural language processing. As they are being used in critical applications, understanding underlying mechanisms for their successes and limitations is imperative. In this paper, we show that overfitting, one of the fundamental issues in deep neural networks, is due to continuous gradient updating and scale sensitiveness of cross entropy loss. By separating samples into correctly and incorrectly classified ones, we show that they behave very differently, where the loss decreases in the correct ones and increases in the incorrect ones. Furthermore, by analyzing dynamics during training, we propose a consensus-based classification algorithm that enables us to avoid overfitting and significantly improve the classification accuracy especially when the number of training samples is limited. As each trained neural network depends on extrinsic factors such as initial values as well as training data, requiring consensus among multiple models reduces extrinsic factors substantially; for statistically independent models, the reduction is exponential. Compared to ensemble algorithms, the proposed algorithm avoids overgeneralization by not classifying ambiguous inputs. Systematic experimental results demonstrate the effectiveness of the proposed algorithm. For example, using only 1000 training samples from MNIST dataset, the proposed algorithm achieves 95% accuracy, significantly higher than any of the individual models, with 90% of the test samples classified.

</details>

### [Predicting Performance using Approximate State Space Model for Liquid State Machines](1901.06240.md)
**Ajinkya Gorad, Vivek Saraswat, Udayan Ganguly** · 2019-01-18

<details>
<summary>Abstract</summary>

Liquid State Machine (LSM) is a brain-inspired architecture used for solving problems like speech recognition and time series prediction. LSM comprises of a randomly connected recurrent network of spiking neurons. This network propagates the non-linear neuronal and synaptic dynamics. Maass et al. have argued that the non-linear dynamics of LSMs is essential for its performance as a universal computer. Lyapunov exponent (mu), used to characterize the "non-linearity" of the network, correlates well with LSM performance. We propose a complementary approach of approximating the LSM dynamics with a linear state space representation. The spike rates from this model are well correlated to the spike rates from LSM. Such equivalence allows the extraction of a "memory" metric (tau_M) from the state transition matrix. tau_M displays high correlation with performance. Further, high tau_M system require lesser epochs to achieve a given accuracy. Being computationally cheap (1800x time efficient compared to LSM), the tau_M metric enables exploration of the vast parameter design space. We observe that the performance correlation of the tau_M surpasses the Lyapunov exponent (mu), (2-4x improvement) in the high-performance regime over multiple datasets. In fact, while mu increases monotonically with network activity, the performance reaches a maxima at a specific activity described in literature as the "edge of chaos". On the other hand, tau_M remains correlated with LSM performance even as mu increases monotonically. Hence, tau_M captures the useful memory of network activity that enables LSM performance. It also enables rapid design space exploration and fine-tuning of LSM parameters for high performance.

</details>

### [A Survey of the Recent Architectures of Deep Convolutional Neural Networks](1901.06032.md)
**Asifullah Khan, Anabia Sohail, Umme Zahoora, Aqsa Saeed Qureshi** · 2019-01-17

<details>
<summary>Abstract</summary>

Deep Convolutional Neural Network (CNN) is a special type of Neural Networks, which has shown exemplary performance on several competitions related to Computer Vision and Image Processing. Some of the exciting application areas of CNN include Image Classification and Segmentation, Object Detection, Video Processing, Natural Language Processing, and Speech Recognition. The powerful learning ability of deep CNN is primarily due to the use of multiple feature extraction stages that can automatically learn representations from the data. The availability of a large amount of data and improvement in the hardware technology has accelerated the research in CNNs, and recently interesting deep CNN architectures have been reported. Several inspiring ideas to bring advancements in CNNs have been explored, such as the use of different activation and loss functions, parameter optimization, regularization, and architectural innovations. However, the significant improvement in the representational capacity of the deep CNN is achieved through architectural innovations. Notably, the ideas of exploiting spatial and channel information, depth and width of architecture, and multi-path information processing have gained substantial attention. Similarly, the idea of using a block of layers as a structural unit is also gaining popularity. This survey thus focuses on the intrinsic taxonomy present in the recently reported deep CNN architectures and, consequently, classifies the recent innovations in CNN architectures into seven different categories. These seven categories are based on spatial exploitation, depth, multi-path, width, feature-map exploitation, channel boosting, and attention. Additionally, the elementary understanding of CNN components, current challenges, and applications of CNN are also provided.

</details>

### [Phoneme-Based Persian Speech Recognition](1901.04699.md)
**Saber Malekzadeh** · 2019-01-15

<details>
<summary>Abstract</summary>

Undoubtedly, one of the most important issues in computer science is intelligent speech recognition. In these systems, computers try to detect and respond to the speeches they are listening to, like humans. In this research, presenting of a suitable method for the diagnosis of Persian phonemes by AI using the signal processing and classification algorithms have tried. For this purpose, the STFT algorithm has been used to process the audio signals, as well as to detect and classify the signals processed by the deep artificial neural network. At first, educational samples were provided as two phonological phrases in Persian language and then signal processing operations were performed on them. Then the results for the data training have been given to the artificial deep neural network. At the final stage, the experiment was conducted on new sounds.

</details>

### [Speaker Adaptation for End-to-End CTC Models](1901.01239.md)
**Ke Li, Jinyu Li, Yong Zhao, Kshitiz Kumar et al.** · 2019-01-04

<details>
<summary>Abstract</summary>

We propose two approaches for speaker adaptation in end-to-end (E2E) automatic speech recognition systems. One is Kullback-Leibler divergence (KLD) regularization and the other is multi-task learning (MTL). Both approaches aim to address the data sparsity especially output target sparsity issue of speaker adaptation in E2E systems. The KLD regularization adapts a model by forcing the output distribution from the adapted model to be close to the unadapted one. The MTL utilizes a jointly trained auxiliary task to improve the performance of the main task. We investigated our approaches on E2E connectionist temporal classification (CTC) models with three different types of output units. Experiments on the Microsoft short message dictation task demonstrated that MTL outperforms KLD regularization. In particular, the MTL adaptation obtained 8.8\% and 4.0\% relative word error rate reductions (WERRs) for supervised and unsupervised adaptations for the word CTC model, and 9.6% and 3.8% relative WERRs for the mix-unit CTC model, respectively.

</details>

### [Deep Speech Enhancement for Reverberated and Noisy Signals using Wide Residual Networks](1901.00660.md)
**Dayana Ribas, Jorge Llombart, Antonio Miguel, Luis Vicente** · 2019-01-03

<details>
<summary>Abstract</summary>

This paper proposes a deep speech enhancement method which exploits the high potential of residual connections in a wide neural network architecture, a topology known as Wide Residual Network. This is supported on single dimensional convolutions computed alongside the time domain, which is a powerful approach to process contextually correlated representations through the temporal domain, such as speech feature sequences. We find the residual mechanism extremely useful for the enhancement task since the signal always has a linear shortcut and the non-linear path enhances it in several steps by adding or subtracting corrections. The enhancement capacity of the proposal is assessed by objective quality metrics and the performance of a speech recognition system. This was evaluated in the framework of the REVERB Challenge dataset, including simulated and real samples of reverberated and noisy speech signals. Results showed that enhanced speech from the proposed method succeeded for both, the enhancement task with intelligibility purposes and the speech recognition system. The DNN model, trained with artificial synthesized reverberation data, was able to deal with far-field reverberated speech from real scenarios. Furthermore, the method was able to take advantage of the residual connection achieving to enhance signals with low noise level, which is usually a strong handicap of traditional enhancement methods.

</details>

### [A Comprehensive Survey on Graph Neural Networks](1901.00596.md)
**Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long et al.** · 2019-01-03

<details>
<summary>Abstract</summary>

Deep learning has revolutionized many machine learning tasks in recent years, ranging from image classification and video processing to speech recognition and natural language understanding. The data in these tasks are typically represented in the Euclidean space. However, there is an increasing number of applications where data are generated from non-Euclidean domains and are represented as graphs with complex relationships and interdependency between objects. The complexity of graph data has imposed significant challenges on existing machine learning algorithms. Recently, many studies on extending deep learning approaches for graph data have emerged. In this survey, we provide a comprehensive overview of graph neural networks (GNNs) in data mining and machine learning fields. We propose a new taxonomy to divide the state-of-the-art graph neural networks into four categories, namely recurrent graph neural networks, convolutional graph neural networks, graph autoencoders, and spatial-temporal graph neural networks. We further discuss the applications of graph neural networks across various domains and summarize the open source codes, benchmark data sets, and model evaluation of graph neural networks. Finally, we propose potential research directions in this rapidly growing field.

</details>

### [A Deep Learning Approach for Similar Languages, Varieties and Dialects](1901.00297.md)
**Vidya Prasad K, Akarsh S, Vinayakumar R, Soman KP** · 2019-01-02

<details>
<summary>Abstract</summary>

Deep learning mechanisms are prevailing approaches in recent days for the various tasks in natural language processing, speech recognition, image processing and many others. To leverage this we use deep learning based mechanism specifically Bidirectional- Long Short-Term Memory (B-LSTM) for the task of dialectic identification in Arabic and German broadcast speech and Long Short-Term Memory (LSTM) for discriminating between similar Languages. Two unique B-LSTM models are created using the Large-vocabulary Continuous Speech Recognition (LVCSR) based lexical features and a fixed length of 400 per utterance bottleneck features generated by i-vector framework. These models were evaluated on the VarDial 2017 datasets for the tasks Arabic, German dialect identification with dialects of Egyptian, Gulf, Levantine, North African, and MSA for Arabic and Basel, Bern, Lucerne, and Zurich for German. Also for the task of Discriminating between Similar Languages like Bosnian, Croatian and Serbian. The B-LSTM model showed accuracy of 0.246 on lexical features and accuracy of 0.577 bottleneck features of i-Vector framework.

</details>

### [Exploring spectro-temporal features in end-to-end convolutional neural networks](1901.00072.md)
**Sean Robertson, Gerald Penn, Yingxue Wang** · 2019-01-01

<details>
<summary>Abstract</summary>

Triangular, overlapping Mel-scaled filters ("f-banks") are the current standard input for acoustic models that exploit their input's time-frequency geometry, because they provide a psycho-acoustically motivated time-frequency geometry for a speech signal. F-bank coefficients are provably robust to small deformations in the scale. In this paper, we explore two ways in which filter banks can be adjusted for the purposes of speech recognition. First, triangular filters can be replaced with Gabor filters, a compactly supported filter that better localizes events in time, or Gammatone filters, a psychoacoustically-motivated filter. Second, by rearranging the order of operations in computing filter bank features, features can be integrated over smaller time scales while simultaneously providing better frequency resolution. We make all feature implementations available online through open-source repositories. Initial experimentation with a modern end-to-end CNN phone recognizer yielded no significant improvements to phone error rate due to either modification. The result, and its ramifications with respect to learned filter banks, is discussed.

</details>

### [Speech Recognition](s2:4954c898d898197663d46e91ae7d83c3df7ac11f.md)
**Steffen Schneider, Alexei Baevski, R. Collobert, Michael Auli** · 2019-01-01

<details>
<summary>Abstract</summary>

We explore unsupervised pre-training for speech recognition by learning representations of raw audio. wav2vec is trained on large amounts of unlabeled audio data and the resulting representations are then used to improve acoustic model training. We pre-train a simple multi-layer convolutional neural network optimized via a noise contrastive binary classification task. Our experiments on WSJ reduce WER of a strong character-based log-mel filterbank baseline by up to 36 % when only a few hours of transcribed data is available. Our approach achieves 2.43 % WER on the nov92 test set. This outperforms Deep Speech 2, the best reported character-based system in the literature while using two orders of magnitude less labeled training data.1

</details>

