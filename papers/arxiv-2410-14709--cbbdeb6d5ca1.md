---
arxiv_id: "2410.14709"
title:
  A two-stage transliteration approach to improve performance of a multilingual
  ASR
authors:
  - Rohit Kumar
submitted: "2024-10-09"
categories:
  - cs.CL
  - cs.SD
  - eess.AS
arxiv_url: https://arxiv.org/abs/2410.14709
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:51:00+00:00"
references_parsed: 0
arxiv_version: ""
---

# A two-stage transliteration approach to improve performance of a multilingual ASR

###### Abstract

End-to-end Automatic Speech Recognition (ASR) systems are rapidly claiming to become state-of-art over other modeling methods. Several techniques have been introduced to improve their ability to handle multiple languages. However, due to variation in writing scripts for different languages, while decoding acoustically similar units, they do not always map to an appropriate grapheme in the target language. This restricts the scalability and adaptability of the model while dealing with multiple languages in code-mixing scenarios. This paper presents an approach to build a language-agnostic end-to-end model trained on a grapheme set obtained by projecting the multilingual grapheme data to the script of a more generic target language. This approach saves the acoustic model from retraining to span over a larger space and can easily be extended to multiple languages. A two-stage transliteration process realizes this approach and proves to minimize speech-class confusion. We performed experiments with an end-to-end multilingual speech recognition system for two Indic Languages, namely Nepali and Telugu. The original grapheme space of these languages is projected to the Devanagari script. We achieved a relative reduction of 20% in the Word Error Rate (WER) and 24% in the Character Error Rate (CER) in the transliterated space, over other language-dependent modeling methods.

Index Terms: Speech recognition, Transliteration, Code-Mixing, Language-agnostic, multilingual model

## 1 Introduction

Automatic Speech Recognition (ASR) systems have experienced a paradigm shift in recent years, from statistical modeling towards end-to-end solutions. Traditional ASR systems relied on appropriate parametric representation to train acoustic models and aided with optimal pronunciation lexicon and language models, dealing with finding the best sequence of words (W)\[[1](https://arxiv.org/html/2410.14709v1#bib.bib1)\]. For such systems, acoustic models are realized over good quality audio recordings, aided with the corresponding transcriptions, by appropriately mapping the statistical characteristics of the audio segment to the label. The language model (LM) helps derive a valid sequence of words once the decoding has been done\[[2](https://arxiv.org/html/2410.14709v1#bib.bib2)\].

End-to-end ASR systems directly map the sequence of input acoustic features to a sequence of graphemes or words. The system encapsulates speech recognition components such as the acoustic, language, and lexicon model into a single pipeline, thus bypassing the required linguistic resources while transferring the useful bias from the source model to the target language\[[3](https://arxiv.org/html/2410.14709v1#bib.bib3), [4](https://arxiv.org/html/2410.14709v1#bib.bib4), [5](https://arxiv.org/html/2410.14709v1#bib.bib5), [6](https://arxiv.org/html/2410.14709v1#bib.bib6), [7](https://arxiv.org/html/2410.14709v1#bib.bib7)\]. Usually, the performance of end-to-end ASR systems over traditional systems has an absolute edge. For popular languages, these systems have already been able to handle gender, dialect, and age diversity. However, for scenarios dealing either with low resources or unseen languages, the performance of these systems suffers considerably. Such scenarios include code-switching, code-mixing, and low resource cases. Without an explicit language specification, the model usually confuses between multiple languages, especially for languages that have very little overlap in their scripts.

India is a diverse country comprising multicultural societies, hosting a hub of several bilingual speakers. Indic languages exhibit significant diversity, and this creates challenges in realizing a good performing ASR system. Different languages have their native script, and furthermore, there is considerable overlap of acoustic content across languages. Hence it is quite likely for acoustically similar segments to be mapped to different graphemes in any ASR system. In multicultural societies, overlapping of language information such as common words, lexical content, occurs quite often, due to language family relations and the geographical significance of the speakers. In India, there are 22 official languages, each with quite a variety of dialects. For several speakers, multiple language pairs frequently appear, mostly in combination with English (code-mixing)\[[8](https://arxiv.org/html/2410.14709v1#bib.bib8)\]. Code-mixing appears as a word or clausal level embedding of one language in the matrix of another and poses quite a challenge for ASR systems to handle. In India, code-mixing with English is an inherent characteristic for speakers of several regions, for example, Telugu-English in Southern, Nepali-English in North-Eastern, and Hindi-English in Northern parts of India.

Multilingual models for speech recognition have evolved from the early Hidden Markov Model-based to Deep Neural network-based architectures, and even for the recent state-of-art end-to-end systems\[[9](https://arxiv.org/html/2410.14709v1#bib.bib9), [10](https://arxiv.org/html/2410.14709v1#bib.bib10), [11](https://arxiv.org/html/2410.14709v1#bib.bib11)\]. Generally, speech recognition of multiple languages requires a lot of training data with the corresponding annotation, hence it’s difficult to train the acoustic model for low resource languages. Acoustic models trained in one language, when borrowed do not perform well in the context of other languages. The reason for this is the phonetic content mismatch between the source language and the target language. These factors limit the performance of speech recognition modules in the context of multilingual scenarios.

In this paper, we propose a two-stage transliteration approach that helps the model learn internal representation, thus enhancing acoustic-phonetic content from languages. Transliteration is a way of representing how the phonetic content of words of one language can be represented in the lexicon of another language. Transliteration is mostly employed for tasks such as machine translation, text retrieval, and ASR systems. For a source language, transliteration provides a unique set of characters in a target grapheme space, thus allowing the mapping of acoustically similar units to a single sequence of graphemes. Apart from such acoustically similar units, this mapping is usually bijective in nature, and hence the transliterated text can easily be mapped to the target language domain in an error-free manner. For units similar in nature, language models in the target language can help determine the appropriate grapheme in case of confusion. The proposed two-stage transliteration prioritizes the reduction of grapheme scope for reduced confusion during the phoneme-grapheme mapping, hence enhancing the performance of ASR in the transliterated space. Organization of the paper is as follows: Section 2 describes the related work done, Section 3 describes the proposed transliteration approach, Section 4 briefs the data, experimental setup, and result analysis, and is followed by the conclusion in Section 5.

## 2 Related work

For end-to-end ASR systems, MFCC features extracted from the time-domain signal serve as a popular choice for the neural network\[[12](https://arxiv.org/html/2410.14709v1#bib.bib12)\]. The neural network maps the input frame to grapheme space in the target language. A vocabulary accommodating different characters from multilingual data induces speech-class ambiguity for acoustically similar units. Most of the recent ASRs have been developed over large datasets, with over 10,000 hours of audio recordings, and even use data augmentation methods over high-resource language to realize sophisticated systems\[[13](https://arxiv.org/html/2410.14709v1#bib.bib13)\].

\[[14](https://arxiv.org/html/2410.14709v1#bib.bib14)\] proposed an approach where monolingual Hindi acoustic models were trained through phoneme adaptation. Often in recognition of code-mixed/switched speech, mixing/switching or borrowing of words is mostly confusing due to the lack of standardization of code-mixed transcripts leading to the presence of homophones. \[[15](https://arxiv.org/html/2410.14709v1#bib.bib15)\] proposed the use of a WX-based standard pronunciation scheme to automatically identify and disambiguate homophones.

Multilingual modeling refers to training over multiple languages for a single network pipeline and recognizing utterances corresponding to the diverse language set. In previous works, \[[16](https://arxiv.org/html/2410.14709v1#bib.bib16), [17](https://arxiv.org/html/2410.14709v1#bib.bib17)\] combined different multilingual acoustic models and language models (LM) together in a probabilistic framework. \[[18](https://arxiv.org/html/2410.14709v1#bib.bib18)\] combined different monolingual LMs into multilingual LM and introduced the concept of grammar into multilingual LM. The set of shared units, the structure of shared states, and the shared acoustic-phonetic properties help the language universal and language adaptive acoustic model to outperform the language-specific model\[[19](https://arxiv.org/html/2410.14709v1#bib.bib19)\]. Multilingual acoustic models have subsequently outperformed monolingual acoustic models\[[20](https://arxiv.org/html/2410.14709v1#bib.bib20)\]. Recently, a grapheme-based sequence-to-sequence model is trained by taking a union of language-specific grapheme sets on different Indian languages together\[[21](https://arxiv.org/html/2410.14709v1#bib.bib21)\]. While training high resource language with low resource language, the performance of high resource language degrades due to heterogeneous multilingual data\[[22](https://arxiv.org/html/2410.14709v1#bib.bib22)\].

Transliteration has been widely used with different applications to write words from one language into another language. Transliteration has also been used as a metric for evaluating the modeling errors in the acoustic and language model\[[23](https://arxiv.org/html/2410.14709v1#bib.bib23)\]. Transliteration helps the acoustic model to reduce the number of modeling units, which eventually leads to a more flexible method for a newer language.

## 3 Proposed Transliteration Approach

For code-mixing/code-switching scenarios, similar phonetic entities align themselves with different graphemes, according to their writing script, which leads to phonetic confusion while creating a super-set of like-sounded phones during training. This section introduces the proposed two-stage transliteration approach to handle multiple languages in an end-to-end schema.

The proposed two-stage Phoneme-to-Grapheme based transliteration approach is based on mapping the phoneme set of the target language to intermediate language grapheme sets. The target language ($`l_{tgt}`$) here is the language, or a mix of multiple languages that serve as input to the ASR. The intermediate language ($`l_{int}`$) is the language whose script is being transformed to. Indic languages have a complex combination of consonants, vowels, and diacritics, which makes it difficult to map to Roman script, and restricts the encoding of language information. The challenges to map Indic languages with other Latin scripts have been highlighted in literature\[[23](https://arxiv.org/html/2410.14709v1#bib.bib23)\]. The proposed approach hence chooses the Devanagari script as $`l_{int}`$ to convert the target languages $`l_{tgt}`$ Nepali, and Telugu. These languages share some common phonemes with the Devanagari script and hence the transformation is smooth. Following are the two stages of the proposed transliteration approach.

### 3.1 Stage-1 : Lexical Transformation

![[Uncaptioned image]](https://arxiv.org/html/extracted/5910027/figures/table11.jpg)

Table 1: Representation of characters in the two-stage transliteration method.

Stage-1 addresses the lexical representation of $`l_{tgt}`$ to script of $`l_{int}`$. A lexicon of the Nepali and Telugu graphemes is formed containing all the native and foreign words (which constitute the code-switching/mixing scenario). A mapping is used to convert all the graphemes to their corresponding phoneme sequence. The phonemic sequence of $`l_{tgt}`$ is then mapped to the corresponding phonemic sequences of the $`l_{int}`$ Devanagari script. Phonemic sequences in $`l_{int}`$ are then arranged according to vowel-consonant rules for word formation according to the Devanagari script. Finally, the phonemic sequence in $`l_{int}`$ Devanagari script are mapped to their corresponding grapheme sequence. For $`l_{tgt}`$ Nepali, combined words are split initially into individual words to avoid ambiguity and to enrich the lexicon.

### 3.2 Stage-2 of transliteration

After Stage-1, a major issue of mapping acoustically similar entities to a common sequence of graphemes remains. Stage-2 addresses this by focusing on converting the dependent form (matra) of a vowel to the independent form. This conversion allows the same phonetic sound of matras to get mapped to graphemes of their independent form of vowels. This mapping minimizes the speech-class confusion as well by limiting the size of the vocabulary. Table [1](https://arxiv.org/html/2410.14709v1#S3.T1 "Table 1 ‣ 3.1 Stage-1 : Lexical Transformation ‣ 3 Proposed Transliteration Approach ‣ A two-stage transliteration approach to improve performance of a multilingual ASR") shows this conversion of matra to its independent form of vowel. Table [2](https://arxiv.org/html/2410.14709v1#S4.T2 "Table 2 ‣ 4.1 Data ‣ 4 Data, Experiment and Result Analysis ‣ A two-stage transliteration approach to improve performance of a multilingual ASR") illustrates the 2-stage process with different examples for both target languages.

## 4 Data, Experiment and Result Analysis

### 4.1 Data

We conducted experiments on data from 2 target languages, namely Nepali and Telugu, which overall corresponds to the total amount of 160 hours of training, and 26 hours of test data. Nepali data is collected from read-out phrases by native speakers\[[24](https://arxiv.org/html/2410.14709v1#bib.bib24)\] and contributes to 113 hours of training data. Telugu data is collected from read-out phrases and conversational speech\[[25](https://arxiv.org/html/2410.14709v1#bib.bib25)\] and contributes to 47 hours of training data. The data are recorded at a sampling rate of 16 kHz with a 16-bit resolution. Both languages have been manually transcribed into their native grapheme set. Both training and testing data exhibit a considerable proportion of code-mixing with English.

![[Uncaptioned image]](https://arxiv.org/html/extracted/5910027/figures/table2.jpg)

Table 2: Illustration of examples using a two-stage transliteration method.

### 4.2 Experimental Setup

The method uses an end-to-end deep-learning architecture with connectionist temporal classification (CTC) loss function as proposed in Deepspeech2\[[26](https://arxiv.org/html/2410.14709v1#bib.bib26)\] for building ASR system. The network composes of 2 CNN layers followed by 5 RNN layers, and a softmax layer with CTC Loss criterion. The system is usually trained on inputs as audio segment or equivalent frequency-domain representation, with the expected output being the corresponding grapheme representing the phonetic content. Model parameters and feature specifications have slightly been modified for tuning the model to a multilingual scenario. In the current work, spectrogram of power normalized audio segments are used as input features. We considered 96 audio features derived over a window size of 20 ms, at a stride of 10 ms, transformed over 512 DFT bins, at an audio sampling rate of 16 KHz. Beam search decoder with language model scoring and beam width of 512 is used. Labels from the proposed transliteration scheme represent the output.

|              |        |      |        |      |         |      |
| ------------ | ------ | ---- | ------ | ---- | ------- | ---- |
| Experiment   | Nepali |      | Telugu |      | Average |      |
|              | WER    | CER  | WER    | CER  | WER     | CER  |
| E0(Baseline) | 32.1   | 10.4 | 47.6   | 22.3 | 39.8    | 16.3 |
| E1           | 30.7   | 9.0  | 45.3   | 20.2 | 38      | 14.6 |
| E2 (stage-1) | 25.4   | 8.3  | 41.8   | 18.1 | 33.9    | 13.9 |
| E3 (stage-2) | 23.8   | 7.8  | 39.5   | 15.7 | 31.6    | 11.7 |

Table 3: Performance (WER/CER) of ASR system after Stage-1 and Stage-2 of transliteration.

### 4.3 Result Analysis

In this section, we discuss the effect of our proposed two-stage phoneme-to-grapheme based transliteration approach over the multilingual acoustic model. In Table [3](https://arxiv.org/html/2410.14709v1#S4.T3 "Table 3 ‣ 4.2 Experimental Setup ‣ 4 Data, Experiment and Result Analysis ‣ A two-stage transliteration approach to improve performance of a multilingual ASR"), we present the performance of the ASR system after the different stages of transliteration. The baseline for the ASR system is represented as experiment E0. Experiment E1 represents training the acoustic model without transliteration. Experiment E2 represents training the acoustic model with stage-1 of the proposed transliteration approach, and experiment E3 represents training the acoustic model with stage-2 of the proposed method. A significant improvement in the performance of the ASR system after each stage of transliteration concerning that of the acoustic model trained without transliteration can be noted in the Tab. [3](https://arxiv.org/html/2410.14709v1#S4.T3 "Table 3 ‣ 4.2 Experimental Setup ‣ 4 Data, Experiment and Result Analysis ‣ A two-stage transliteration approach to improve performance of a multilingual ASR"). After stage-1, the language information among the different languages is encoded into a single writing script, resulting in reduction in number of classes during the phone classification. And in Stage-2, after the replacement of matra with its full vowel, the vocabulary size gets further reduced, having a minimal number of characters left. Thus, reducing the speech-class confusion and allowing mapping of similar-sounding acoustics to individual graphemes. We observe a reduction of 22.4

## 5 Conclusion

In this paper, we explored a transliteration-based approach to address the code-mixing scenario in a monolingual acoustic model. Our motivation is to improve upon the performance while avoiding retraining the acoustic model, which is usually done in case of overlapping of language information among multiple languages. We propose a two-stage phoneme-to-grapheme based transliteration approach, while choosing a popular and standard language as intermediate script for multiple languages in the target set. The proposed transliteration method operates in two stages. In the former stage, we perform transliteration with the dependent vowels, i.e., matra. In the latter stage, we map the dependent form of a vowel to its independent form. We achieve an average reduction of 20

## References

- \[1\] D. Povey, A. Ghoshal, G. Boulianne, L. Burget, O. Glembek, N. Goel, M. Hannemann, P. Motlicek, Y. Qian, P. Schwarz _et al._, “The kaldi speech recognition toolkit,” in _IEEE 2011 workshop on automatic speech recognition and understanding_, no. CONF.   IEEE Signal Processing Society, 2011.
- \[2\] J. Picone, “Continuous speech recognition using hidden markov models,” _IEEE Assp magazine_, vol. 7, no. 3, pp. 26–41, 1990.
- \[3\] A. Graves, “Sequence transduction with recurrent neural networks,” _arXiv preprint arXiv:1211.3711_, 2012.
- \[4\] A. Graves and N. Jaitly, “Towards end-to-end speech recognition with recurrent neural networks,” in _International conference on machine learning_.   PMLR, 2014, pp. 1764–1772.
- \[5\] W. Chan, N. Jaitly, Q. Le, and O. Vinyals, “Listen, attend and spell: A neural network for large vocabulary conversational speech recognition,” in _2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.   IEEE, 2016, pp. 4960–4964.
- \[6\] R. Prabhavalkar, K. Rao, T. N. Sainath, B. Li, L. Johnson, and N. Jaitly, “A comparison of sequence-to-sequence models for speech recognition.” in _Interspeech_, 2017, pp. 939–943.
- \[7\] C.-C. Chiu, T. N. Sainath, Y. Wu, R. Prabhavalkar, P. Nguyen, Z. Chen, A. Kannan, R. J. Weiss, K. Rao, E. Gonina _et al._, “State-of-the-art speech recognition with sequence-to-sequence models,” in _2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.   IEEE, 2018, pp. 4774–4778.
- \[8\] K. Bhuvanagiri and S. Kopparapu, “An approach to mixed language automatic speech recognition,” _Oriental COCOSDA, Kathmandu, Nepal_, 2010.
- \[9\] S. Thomas, S. Ganapathy, and H. Hermansky, “Multilingual mlp features for low-resource lvcsr systems,” in _2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.   IEEE, 2012, pp. 4269–4272.
- \[10\] Z. Tüske, J. Pinto, D. Willett, and R. Schlüter, “Investigation on cross-and multilingual mlp features under matched and mismatched acoustical conditions,” in _2013 IEEE International Conference on Acoustics, Speech and Signal Processing_.   IEEE, 2013, pp. 7349–7353.
- \[11\] T. Sercu, G. Saon, J. Cui, X. Cui, B. Ramabhadran, B. Kingsbury, and A. Sethy, “Network architectures for multilingual speech representation learning,” in _2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.   IEEE, 2017, pp. 5295–5299.
- \[12\] A. Hannun, C. Case, J. Casper, B. Catanzaro, G. Diamos, E. Elsen, R. Prenger, S. Satheesh, S. Sengupta, A. Coates _et al._, “Deep speech: Scaling up end-to-end speech recognition,” _arXiv preprint arXiv:1412.5567_, 2014.
- \[13\] D. Amodei, S. Ananthanarayanan, R. Anubhai, J. Bai, E. Battenberg, C. Case, J. Casper, B. Catanzaro, Q. Cheng, G. Chen _et al._, “Deep speech 2: End-to-end speech recognition in english and mandarin,” in _International conference on machine learning_, 2016, pp. 173–182.
- \[14\] A. Pandey, B. M. L. Srivastava, and S. V. Gangashetty, “Adapting monolingual resources for code-mixed hindi-english speech recognition,” in _Asian Language Processing (IALP), 2017 International Conference on_.   IEEE, 2017, pp. 218–221.
- \[15\] B. M. L. Srivastava and S. Sitaram, “Homophone identification and merging for code-switched speech recognition,” _Proc. Interspeech 2018_, pp. 1943–1947, 2018.
- \[16\] T. Ward, S. Roukos, C. Neti, J. Gros, M. Epstein, and S. Dharanipragada, “Towards speech understanding across multiple languages.” in _ICSLP_.   Citeseer, 1998.
- \[17\] Z. Wang, U. Topkara, T. Schultz, and A. Waibel, “Towards universal speech recognition,” in _Proceedings. Fourth IEEE International Conference on Multimodal Interfaces_.   IEEE, 2002, pp. 247–252.
- \[18\] C. Fugen, S. Stuker, H. Soltau, F. Metze, and T. Schultz, “Efficient handling of multilingual language models,” in _2003 IEEE Workshop on Automatic Speech Recognition and Understanding (IEEE Cat. No. 03EX721)_.   IEEE, 2003, pp. 441–446.
- \[19\] H. Lin, L. Deng, D. Yu, Y.-f. Gong, A. Acero, and C.-H. Lee, “A study on multilingual acoustic modeling for large vocabulary asr,” in _2009 IEEE International Conference on Acoustics, Speech and Signal Processing_.   IEEE, 2009, pp. 4333–4336.
- \[20\] G. Heigold, V. Vanhoucke, A. Senior, P. Nguyen, M. Ranzato, M. Devin, and J. Dean, “Multilingual acoustic models using distributed deep neural networks,” in _2013 IEEE international conference on acoustics, speech and signal processing_.   IEEE, 2013, pp. 8619–8623.
- \[21\] S. Toshniwal, T. N. Sainath, R. J. Weiss, B. Li, P. Moreno, E. Weinstein, and K. Rao, “Multilingual speech recognition with a single end-to-end model,” in _2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.   IEEE, 2018, pp. 4904–4908.
- \[22\] B. Li, R. Pang, T. N. Sainath, A. Gulati, Y. Zhang, J. Qin, P. Haghani, W. R. Huang, M. Ma, and J. Bai, “Scaling end-to-end models for large-scale multilingual asr,” _arXiv preprint arXiv:2104.14830_, 2021.
- \[23\] J. Emond, B. Ramabhadran, B. Roark, P. Moreno, and M. Ma, “Transliteration based approaches to improve code-switched speech recognition performance,” in _2018 IEEE Spoken Language Technology Workshop (SLT)_.   IEEE, 2018, pp. 448–455.
- \[24\] O. Kjartansson, S. Sarin, K. Pipatsrisawat, M. Jansche, and L. Ha, “Crowd-Sourced Speech Corpora for Javanese, Sundanese, Sinhala, Nepali, and Bangladeshi Bengali,” in _Proc. The 6th Intl. Workshop on Spoken Language Technologies for Under-Resourced Languages (SLTU)_, Gurugram, India, Aug. 2018, pp. 52–55. \[Online\]. Available: [http://dx.doi.org/10.21437/SLTU.2018-11](http://dx.doi.org/10.21437/SLTU.2018-11)
- \[25\] B. M. L. Srivastava, S. Sitaram, R. K. Mehta, K. D. Mohan, P. Matani, S. Satpal, K. Bali, R. Srikanth, and N. Nayak, “Interspeech 2018 low resource automatic speech recognition challenge for indian languages.” in _SLTU_, 2018, pp. 11–14.
- \[26\] A. et al, “Deep speech 2: End-to-end speech recognition in english and mandarin,” in _Proceedings of the 33rd International Conference on International Conference on Machine Learning - Volume 48_, ser. ICML’16.   JMLR.org, 2016, p. 173–182.
