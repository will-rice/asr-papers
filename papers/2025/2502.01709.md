---
arxiv_id: "2502.01709"
title: Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models
authors:
  - Christopher Simic
  - Korbinian Riedhammer
  - Tobias Bocklet
submitted: "2025-02-03"
categories:
  - cs.SD
  - cs.LG
  - eess.AS
arxiv_url: https://arxiv.org/abs/2502.01709
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:46:59+00:00"
references_parsed: 0
arxiv_version: ""
---

# Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models

Christopher Simic Technische Hochschule Nuernberg\
Nuernberg, Germany\
christopher.simic@th-nuernberg.de    Korbinian Riedhammer Technische Hochschule Nuernberg\
Nuernberg, Germany\
korbinian.riedhammer@th-nuernberg.de    Tobias Bocklet Technische Hochschule Nuernberg\
Nuernberg, Germany\
tobias.bocklet@th-nuernberg.de

###### Abstract

We present an approach to Audio-Visual Speech Recognition that builds on a pre-trained Whisper model. To infuse visual information into this audio-only model, we extend it with an AV fusion module and LoRa adapters, one of the most up-to-date adapter approaches. One advantage of adapter-based approaches, is that only a relatively small number of parameters are trained, while the basic model remains unchanged. Common AVSR approaches train single models to handle several noise categories and noise levels simultaneously. Taking advantage of the lightweight nature of adapter approaches, we train noise-scenario-specific adapter-sets, each covering individual noise-categories or a specific noise-level range. The most suitable adapter-set is selected by previously classifying the noise-scenario. This enables our models to achieve an optimum coverage across different noise-categories and noise-levels, while training only a minimum number of parameters.

Compared to a full fine-tuning approach with SOTA performance our models achieve almost comparable results over the majority of the tested noise-categories and noise-levels, with up to 88.5% less trainable parameters. Our approach can be extended by further noise-specific adapter-sets to cover additional noise scenarios. It is also possible to utilize the underlying powerful ASR model when no visual information is available, as it remains unchanged.

###### Index Terms:

ASR, AVSR, adapter, self-supervised, multi-agent

## I Introduction

Automatic Speech Recognition (ASR) and Audio-Visual Speech Recognition (AVSR) share common targets, as both aim to transcribe input sequences. ASR approaches rely on audio-only speech data, which can be particularly challenging in noisy environments, resulting in increased Word Error Rates (WER). AVSR incorporates additional visual information, typically recordings of lip movements, which is one way to achieve a WER reduction, especially in noisy environments.

Common AVSR approaches train models from scratch on audio-visual data. In contrast, our approach builds on a pre-trained ASR model to benefit from the modeling capabilities of models that are trained on huge amounts of speech data. In this work, we utilize the SOTA ASR model Whisper, which is currently the most robust model for speech-to-text transcription. In general, our approach can be applied to any pre-trained ASR model.

To adapt the pre-trained audio-only ASR model to the additional visual modality, we use LoRa adapters instead of full fine-tuning the model. These adapters allow a baseline model to be adapted to a specific domain without changing the underlying baseline model’s basic behavior. These adapters can be switched on and off in case no visual information is available or changing environmental conditions.

Conventional AVSR approaches train single models to handle simultaneously all noise categories and a wide range of noise levels. Due to the very lightweight adapters, several domain-specific adapter-sets can be kept available at all times and switched dynamically. We take advantage of this by training multiple specific adapter-sets that enable customized adaptation to specific noise scenarios. Additionally, we include a simple classification layer that determines the noise scenario based on the input audio signal to select the most suitable adapter-set for processing.

Our key contributions are:

- •
  The first approach to integrate adapters into a pre-trained ASR model to enable processing of additional visual information, with a detailed analysis and comparison across multiple noise types and levels
- •
  The first multi-agent system for Audio-Visual Speech Recognition by developing multiple adapter-sets to optimize the performance across various noise categories and levels
- •
  Implementing noise category or level classification to dynamically select the most suitable adapter-set for each scenario

## II Related Work

### II-A ASR and AVSR

Automatic Speech Recognition (ASR) and Audio-Visual Speech Recognition (AVSR) approaches target the automatic transcription of input signals (audio-only or audio-visual). Conformer and transformer architectures have established in these domains. Beside conformer approaches \[[9](https://arxiv.org/html/2502.01709v1#bib.bib9), [2](https://arxiv.org/html/2502.01709v1#bib.bib2)\] espacially transformer approaches like Whisper \[[18](https://arxiv.org/html/2502.01709v1#bib.bib18)\], HuBERT \[[11](https://arxiv.org/html/2502.01709v1#bib.bib11)\], and Wav2Vec2 \[[3](https://arxiv.org/html/2502.01709v1#bib.bib3)\] have gained popularity in ASR. Whisper can be emphasized here as it exhibits a comparatively high robustness in moderate noise conditions \[[8](https://arxiv.org/html/2502.01709v1#bib.bib8)\]. However, all ASR approaches suffer from increased Word Error Rates (WER) under noisy conditions.

One way, to tackle this problem is the development of transformer \[[21](https://arxiv.org/html/2502.01709v1#bib.bib21), [22](https://arxiv.org/html/2502.01709v1#bib.bib22), [10](https://arxiv.org/html/2502.01709v1#bib.bib10), [17](https://arxiv.org/html/2502.01709v1#bib.bib17)\] and conformer-based\[[15](https://arxiv.org/html/2502.01709v1#bib.bib15), [16](https://arxiv.org/html/2502.01709v1#bib.bib16), [20](https://arxiv.org/html/2502.01709v1#bib.bib20)\] AVSR approaches, which use visual information from lip movements to reduce the WER, espacially for noisy conditions. The best performance for AVSR is currently achieved by the approaches RAVEn \[[10](https://arxiv.org/html/2502.01709v1#bib.bib10)\], AV-HuBERT \[[22](https://arxiv.org/html/2502.01709v1#bib.bib22)\] and AUTO-AVSR \[[15](https://arxiv.org/html/2502.01709v1#bib.bib15)\], meaning that all of them can be considered as state-of-the-art (SOTA). While most common AVSR approaches train models from scratch, Whisper-Flamingo \[[19](https://arxiv.org/html/2502.01709v1#bib.bib19)\] and our previous work AV Fusion \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] use pre-trained Whisper models. AV-Fusion combines the audio-visual features in a fusion module located upstream of the encoder. Whisper-Flamingo works with separate audio and visual encoders and fuses the modalities in the decoder.

### II-B Adapter Approaches

Adapter approaches like LoRa \[[12](https://arxiv.org/html/2502.01709v1#bib.bib12)\] and AdaLoRa \[[26](https://arxiv.org/html/2502.01709v1#bib.bib26)\] allow transformer and conformer fine-tuning, without changing the baseline model’s parameters. For this purpose, both insert additional blocks, consisting of two serial linear layers alongside each linear layer within the baseline model’s attention blocks. The rank, which describes the dimension between both linear layer is chosen to be small in order to significantly reduce the number of trainable parameters compared to a full fine-tuning. Various approaches demonstrate that adapters are suitable for adapting pre-trained ASR models to changed domains \[[14](https://arxiv.org/html/2502.01709v1#bib.bib14), [13](https://arxiv.org/html/2502.01709v1#bib.bib13), [6](https://arxiv.org/html/2502.01709v1#bib.bib6), [7](https://arxiv.org/html/2502.01709v1#bib.bib7), [25](https://arxiv.org/html/2502.01709v1#bib.bib25), [20](https://arxiv.org/html/2502.01709v1#bib.bib20)\] or to extend Large Language Models (LLM) with additional modalities \[[4](https://arxiv.org/html/2502.01709v1#bib.bib4), [27](https://arxiv.org/html/2502.01709v1#bib.bib27)\]. The advantage of trainable adapters, apart from the reduced number of parameters to be trained, is their ability to be used as a lightweight add-on to the baseline model and falling back to the baseline model’s basic behaviour if adapters are switched off.

![Refer to caption](https://arxiv.org/html/extracted/6174880/data/overview_3.png)

Figure 1: Overall model architecture. AVSR model on the left, including the frozen, pre-trained ASR model (gray) and the selected set of LoRa adapters (orange) and the AV fusion module (green). Noise-scenario-classifier (blue) to select the most suitable adapter-set on the right.

## III Data

### III-A LRS3

We utilize the LRS3-TED dataset \[[1](https://arxiv.org/html/2502.01709v1#bib.bib1)\], the most comprehensive and challenging dataset for AVSR, to train and evaluate our models. LRS3 contains 150k sequences from TED Talks on YouTube, featuring over 9k speakers and a vocabulary of 51k words. The dataset comprises more than 430 hours of video, divided into Pretrain (407 hours), Trainval (30 hours), and Test (1 hour), which we adopt for our experiments.

### III-B VoxCeleb2

VoxCeleb2 \[[5](https://arxiv.org/html/2502.01709v1#bib.bib5)\] is an audio-visual dataset originally designed for speaker recognition, without provided transcriptions. As our approach is trained self-supervised, we can utilize this dataset. It contains over one million utterances from more than 6k speakers. While the dataset is multilingual, we focus solely on the English sequences with approximately 1700 hours.

### III-C Musan

To systematically contaminate speech data with synthetic noise, we employ the Musan dataset \[[24](https://arxiv.org/html/2502.01709v1#bib.bib24)\], which provides diverse audio samples across different categories. 60 hours of speech, 42.5 hours of music, and 6 hours of natural sounds. Following the AV-HuBERT \[[21](https://arxiv.org/html/2502.01709v1#bib.bib21)\] methodology, we generate babble noise by merging 30 speech samples. We split each noise category into 80% for training, 10% for validation, and 10% for testing to prevent any overlap.

## IV Method

### IV-A Overall Model

Figure [1](https://arxiv.org/html/2502.01709v1#S2.F1 "Figure 1 ‣ II-B Adapter Approaches ‣ II Related Work ‣ Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models") shows our model’s overall structure, with the AVSR model on the left and multiple adapter-sets and the noise-scenario-classifier on the right.

The AVSR model consist of three parts, a pre-trained, frozen ASR model (gray), a group of LoRa adapter (orange) and an AV fusion module (green). Each adapter-set on the right consists of a spicific set of LoRa adapters and an AV fusion module, which are kept to replace the adapter-set in the AVSR model if necessary. The classifier (blue) receives the noisy input mel-spectrum to determine the current noise scenario and select the optimum adapter-set.

Like \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23), [19](https://arxiv.org/html/2502.01709v1#bib.bib19)\], we choose Whisper as the core element of our AVSR model, which is currently one of the most powerful ASR models. As Whisper can only process audio information, the model must be extended by the upstream AV fusion module, which is adopted from \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\]. This fusion module consists two processing levels. The first level includes two separate CNN-based feature extraction modules for audio and visual inputs. The extracted audio and visual feature vectors are processed by a multi-layer multi-head cross-attention module, which produces the inputs for the Whisper-based model. Further details about the fusion module architecture can be taken from \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\].

In contrast to \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] and \[[19](https://arxiv.org/html/2502.01709v1#bib.bib19)\], which perform a full fine-tuning for the pre-trained ASR model, we add LoRa adapters to the ASR model. These adapters provide the advantage that the ASR model weights are kept frozen while only the adapter weights are trained, which means that the base model’s basic behavior remains unchanged. We insert adapters to all linear layers of the ASR transformer model’s Query, Value, Key and Output layers with a rank of 64. Initially, we also tested AdaLoRa adapters. These perform an SVD to determine the optimum rank for each layer, under the constraint that the average rank across all layers remains constant. Against our expectations, it turned out that LoRa adapters yield better results for the tested parameters.

Usually AVSR models aim to simultaneously cover all noise categories and the entire Signal-to-Noise Ratio (SNR) range. We benefit from the lightweight nature of adapter-based approaches and train several noise-scenario-specific adapter-sets that share the same base model. Each adapter-set covers only a small part of the entire noise spectrum. Due to their lightweight character, the adapter-sets can be easily exchanged when noise scenarios change. We distinguish between two basic concepts and analyze which concept provides better results:

- •
  Noise-category-specific – One specific adapter-set for each of the noise categories Babble, Music, Noise and Single Sidespeaker
- •
  Noise-level-specific – One adapter-set each for the SNR range above or below 0dB

Like  \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] we use the frozen Whisper ASR model to generate target values from clean audio inputs at the model levels mel-spectrum level, embedding level after the encoder and logit level after the decoder. The AVSR model receives synthetically contaminated audio inputs and corresponding video frames, that contain the speaker’s lip movements. During training, we calculate a loss for all three model levels, which are added to a weighted total loss.

```math
\text{L}_{\text{pre}} = {{{0.5 \cdot L}1\left( {Mel_{c}},{Mel_{n}} \right)} + {L1\left( {Emb_{c}},{Emb_{n}} \right)}}
```

```math
\text{L}_{\text{ft}} = {\text{L}_{\text{pre}} + {CE\left( {Dec_{c}},{Dec_{n}} \right)}}
```

$`\text{L}_{\text{pre}}`$ defines the loss used during pre-training. Therefore, we calculate the Mean Absolute Error (MAE) between the model receiving clean inputs and the trained AVSR model receiving noisy inputs at the mel-spectrum and embedding level after the encoder. The mel-spectrum loss is semi-weighted to reduce its influence on the training process. This loss aims to prevent the generated mel-spectrum from drifting too far from natural mel-spectrums. $`\text{L}_{\text{ft}}`$ defines the loss during the fine-tuning. This extends $`\text{L}_{\text{pre}}`$ by the loss term at the logit level after the decoder. We follow the example of the original Whisper training and use a Cross-Entropy loss at this level.

### IV-B Training Details

We use two model sizes for our approach, based on the Whisper variants base (74M) and small (244M). The applied fusion module contains 13.2M parameters. The LoRa adapters with rank 64 contain 4.8M parameters for base and 14.3M for small. For the noise-category-specific concept we use four adapter-sets and fusion modules that share one Whisper model. This results in a total of 146M model parameters, of which 72M are trainable for the base version and a total of 354M model parameters with 110M trainable parameters for the larger small version. For the noise-level-specific concept, only two adapter-sets and fusion modules share one Whisper model. This results in 110M total model parameters with 36M trainable parameters for the smaller version and 299M total model parameters with 55M trainable parameters for the larger version.

Our models are trained with a batch size of 16. For the first training step, we use the Voxceleb2 dataset for 112k iterations to pre-condition the models. This is followed by 112k iterations with the LRS3 dataset. For these two steps, we only train fusion module and encoder adapters with a learning rate of 1e-4. Afterwards, we train the the fusion module and all adapters using $`\text{L}_{\text{ft}}`$. For this, we also use the LRS3 dataset and start with a learning rate of 1e-5 for 21k iterations. This is followed by 21k iterations with the learning rate gradually reduced to 1e-7. Due to convergence problems, the learning rate for the larger small models was reduced by 0.5 after the first training step. We follows the suggestion of \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] and choose a SNR range from -15dB to 30dB during training.

### IV-C Adapter-Set Selector

As we train individual adapter-sets for different noise scenarios, the noise category or noise level must be determined before processing. For fully automatic adapter-set selection, we built a classifier which is illustrated as the blue block in Figure [1](https://arxiv.org/html/2502.01709v1#S2.F1 "Figure 1 ‣ II-B Adapter Approaches ‣ II Related Work ‣ Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models") on the right. For this purpose, we utilize a 10-layer CNN ResNet with 64 processing channels. To determine the noise category, the CNN ResNet is followed by two fully connected linear layer and one Softmax layer. This results in four classes representing the four noise categories. For training, we use a Cross-Entropy Loss. To determine the noise level, which is defined by the Signal-to-Noise Ratio (SNR) value, the CNN ResNet is also followed by two fully connected linear layers, with a single output neuron in the second layer. Since we predict continuous SNR values, we use a Mean Squared Error Loss (MSE) during training.

## V Results

|                                                                             |          |          |                   |      |     |     |                  |     |     |     |                    |     |     |     |                    |      |      |     |
| --------------------------------------------------------------------------- | -------- | -------- | ----------------- | ---- | --- | --- | ---------------- | --- | --- | --- | ------------------ | --- | --- | --- | ------------------ | ---- | ---- | --- |
|                                                                             |          |          | Babble SNR \[dB\] |      |     |     | Music SNR \[dB\] |     |     |     | Natural SNR \[dB\] |     |     |     | Sidesp. SNR \[dB\] |      |      |     |
| Models                                                                      | TrP      | ToP      | -10               | 0    | 10  | 20  | -10              | 0   | 10  | 20  | -10                | 0   | 10  | 20  | -10                | 0    | 10   | 20  |
| AV-Fusion base FFT \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\]  | 87M      | 87M      | 46.7              | 7.1  | 2.9 | 2.5 | 9.4              | 3.2 | 2.7 | 2.4 | 14.2               | 4.1 | 3.0 | 2.5 | 9.9                | 5.2  | 3.0  | 2.5 |
| (Ours) LoRa-AVSR base - Full noise spectrum                                 | 18M      | 92M      | 60.7              | 10.0 | 2.9 | 2.5 | 13.7             | 4.1 | 2.8 | 2.5 | 18.8               | 4.7 | 2.7 | 2.4 | 16.6               | 8.6  | 3.7  | 2.4 |
| (Ours) LoRa-AVSR base - Noise category spec. (Babble)                       | 18M      | 92M      | 51.5              | 8.3  | 2.8 | 2.6 | 48.5             | 7.9 | 3.3 | 2.8 | 36.1               | 8.3 | 3.3 | 2.7 | 122.7              | 79.1 | 6.6  | 2.8 |
| (Ours) LoRa-AVSR base - Noise category spec. (Music)                        | 18M      | 92M      | 77.1              | 13.4 | 3.0 | 2.6 | 11.4             | 3.8 | 3.0 | 2.7 | 19.2               | 5.1 | 2.8 | 2.6 | 87.4               | 44.3 | 5.6  | 2.8 |
| (Ours) LoRa-AVSR base - Noise category spec. (Noise)                        | 18M      | 92M      | 80.0              | 14.4 | 3.2 | 2.8 | 21.9             | 5.1 | 3.2 | 2.9 | 17.3               | 4.4 | 2.9 | 2.6 | 124.2              | 82.7 | 7.6  | 2.9 |
| (Ours) LoRa-AVSR base - Noise category spec. (Sidespeaker)                  | 18M      | 92M      | 90.8              | 15.3 | 3.4 | 2.6 | 22.1             | 5.2 | 3.0 | 2.6 | 26.6               | 6.0 | 3.0 | 2.6 | 8.7                | 5.1  | 2.9  | 2.5 |
| \hdashline                                                                  |          |          |                   |      |     |     |                  |     |     |     |                    |     |     |     |                    |      |      |     |
| (Ours) LoRa-AVSR base - Noise category spec. + Classifier                   | 72M\*\*  | 146M\*\* | 51.6              | 8.3  | 2.8 | 2.6 | 11.5             | 3.9 | 3.0 | 2.7 | 17.2               | 4.4 | 2.9 | 2.5 | 9.2                | 5.3  | 2.9  | 2.6 |
| (Ours) LoRa-AVSR base - Noise level spec. (HighNoise)                       | 18M      | 92M      | 48.7              | 7.8  | 3.2 | 2.7 | 9.6              | 3.5 | 3.1 | 2.9 | 14.5               | 4.3 | 2.7 | 2.8 | 7.7                | 6.2  | 10.7 | 6.8 |
| (Ours) LoRa-AVSR base - Noise level spec. (LowNoise)                        | 18M      | 92M      | 78.4              | 10.5 | 3.0 | 2.6 | 20.1             | 4.5 | 3.0 | 2.7 | 22.7               | 5.2 | 3.0 | 2.6 | 45.9               | 10.9 | 3.3  | 2.7 |
| \hdashline                                                                  |          |          |                   |      |     |     |                  |     |     |     |                    |     |     |     |                    |      |      |     |
| (Ours) LoRa-AVSR base - Noise level spec. + Classifier                      | 36M\*\*  | 110M\*\* | 48.8              | 7.8  | 3.0 | 2.6 | 9.6              | 3.6 | 3.0 | 2.7 | 14.6               | 4.4 | 3.0 | 2.6 | 10.9               | 6.7  | 5.4  | 2.7 |
| AV-HuBERT large\* \[[22](https://arxiv.org/html/2502.01709v1#bib.bib22)\]   | 477M     | 477M     | 34.9              | 5.8  | 2.0 | –   | 9.7              | 2.5 | 1.8 | –   | 9.7                | 2.5 | 1.8 | –   | 11.4               | 2.9  | 1.8  | –   |
| AV-Fusion small FFT \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] | 257M     | 257M     | 38.7              | 4.7  | 2.2 | 1.9 | 6.7              | 2.4 | 1.9 | 1.9 | 10.6               | 2.8 | 2.1 | 2.0 | 5.4                | 2.8  | 2.0  | 1.9 |
| (Ours) LoRa-AVSR small - Full noise spectrum                                | 28M      | 272M     | 52.0              | 6.1  | 2.1 | 1.9 | 9.1              | 2.6 | 2.0 | 1.9 | 12.7               | 3.2 | 2.1 | 1.9 | 8.9                | 4.1  | 2.2  | 1.9 |
| (Ours) LoRa-AVSR small - Noise category spec. (Babble)                      | 28M      | 272M     | 46.2              | 6.2  | 1.9 | 1.9 | 38.5             | 4.4 | 2.2 | 2.0 | 23.8               | 5.0 | 2.1 | 1.8 | 119.8              | 49.8 | 3.0  | 1.9 |
| (Ours) LoRa-AVSR small - Noise category spec. (Music)                       | 28M      | 272M     | 67.3              | 8.0  | 2.2 | 1.9 | 8.9              | 2.5 | 1.9 | 2.0 | 14.7               | 3.4 | 2.1 | 1.9 | 82.6               | 27.6 | 2.8  | 2.0 |
| (Ours) LoRa-AVSR small - Noise category spec. (Noise)                       | 28M      | 272M     | 71.8              | 9.0  | 2.1 | 1.8 | 15.4             | 3.1 | 2.0 | 1.9 | 13.0               | 3.1 | 2.0 | 1.9 | 117.3              | 52.1 | 3.0  | 1.9 |
| (Ours) LoRa-AVSR small - Noise category spec. (Sidespeaker)                 | 28M      | 272M     | 74.2              | 9.2  | 2.2 | 1.9 | 15.7             | 3.1 | 2.2 | 1.9 | 18.2               | 3.7 | 2.2 | 1.9 | 6.5                | 3.7  | 2.0  | 1.8 |
| \hdashline                                                                  |          |          |                   |      |     |     |                  |     |     |     |                    |     |     |     |                    |      |      |     |
| (Ours) LoRa-AVSR small - Noise category spec. + Classifier                  | 110M\*\* | 354M\*\* | 46.2              | 6.3  | 1.9 | 1.9 | 8.9              | 2.6 | 1.9 | 2.0 | 13.0               | 3.1 | 2.0 | 1.9 | 7.0                | 3.8  | 2.1  | 1.8 |
| (Ours) LoRa-AVSR small - Noise level spec. (LowNoise)                       | 28M      | 272M     | 44.6              | 6.4  | 2.3 | 2.0 | 7.0              | 2.5 | 2.1 | 2.1 | 11.0               | 3.2 | 2.1 | 1.9 | 5.6                | 3.9  | 5.3  | 3.4 |
| (Ours) LoRa-AVSR small - Noise level spec. (HighNoise)                      | 28M      | 272M     | 75.1              | 8.0  | 2.1 | 1.8 | 14.9             | 2.9 | 2.0 | 1.9 | 18.0               | 4.3 | 2.0 | 1.8 | 40.8               | 6.8  | 2.1  | 1.8 |
| \hdashline                                                                  |          |          |                   |      |     |     |                  |     |     |     |                    |     |     |     |                    |      |      |     |
| (Ours) LoRa-AVSR small - Noise level spec. + Classifier                     | 55M\*\*  | 299M\*\* | 44.6              | 6.4  | 2.1 | 1.8 | 7.1              | 2.5 | 2.0 | 1.9 | 11.1               | 3.2 | 2.0 | 1.8 | 8.4                | 4.3  | 3.3  | 1.8 |

TABLE I: WER \[%\] for AV-HuBERT large, AV-Fusion (with full fine-tuning) and several of ours adapter-based model combinations. The models are grouped by model size. TrP indicates the number of trainable parameters, ToP the number of total model parameters. WER values are provided for different noise categories and noise levels. \* Values for AV-HuBERT are taken from the official paper. \[[22](https://arxiv.org/html/2502.01709v1#bib.bib22)\] \*\* For all classifier-based models, all available adapter-set parameters are listed, while only one particular adapter-set is used for inference (same number of parameters as for the noise-specific models listed above)

TABLE [I](https://arxiv.org/html/2502.01709v1#S5.T1 "TABLE I ‣ V Results ‣ Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models") provides the results for our models and two benchmark models, AV-HuBERT \[[22](https://arxiv.org/html/2502.01709v1#bib.bib22)\] and AV-Fusion \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\]. All models are divided into two groups according to their model size, with the smaller models in the upper part and the larger models in the lower part. All models are tested on the noise categories Babble, Music, Natural and Sidespeaker across a wide SNR range from -10dB to 20dB, with -10dB representing scenarios with very high background noise levels. All results are given in Word Error Rate (WER) in \[%\].

### V-A AV-HuBERT vs. AV-Fusion

To ensure comparability, we trained the AV-Fusion \[[23](https://arxiv.org/html/2502.01709v1#bib.bib23)\] models, from the official repo for both model sizes on our data. This was necessary because AV-Fusion does not provide models that were pre-trained on VoxCeleb2 and fine-tuned on 430h LRS3. Since AV-HuBERT does not provide a seed definition, our splits are not identical and a test on our data would produce different results. Consequently, we use the values from the official paper \[[22](https://arxiv.org/html/2502.01709v1#bib.bib22)\]. We are limited to the large version, as no values are available for the smaller base version. In contrast to AV-HuBERT, we analyze Music and Natural noise separately, so we report the mean values given by AV-HuBERT for both noise categories.

Comparing the larger AV-Fusion small FFT model to AV-HuBERT large reveals that AV-HuBERT is superior for Babble noise, while AV-Fusion has clear advantages for Sidespeaker noise. We also see a mixed picture for Music and Natural noise. Across all SNR values, that AV-HuBERT provides results for (-10dB, -5dB, 0dB, 5dB, 10dB) and all noise categories AV-Fusion achieves an average reduction in WER of 2.1%, which demonstrates that both approaches have a very similar performance, with a slight advantage for AV-Fusion. Another AVSR with similar performance is Whisper-Flamingo \[[19](https://arxiv.org/html/2502.01709v1#bib.bib19)\]. The official paper only provides one value for SNR 0dB and the noise category Babble with a WER of 5.7, which is also slightly higher than the value of 4.7 achieved by AV-Fusion.

Since all of these approaches show quite similar performance, we will focus on the comparison to AV-Fusion FFT in the subsequent discussion, as results for both model sizes and SNR values from -10 dB to 20 dB are available for this approach.

### V-B LoRa Adapter

The LoRa-AVSR base/small - Full noise spectrum models share the same model architecture as all subsequent noise-scenario-specific models, but have been trained simultaneously on all four noise categories and the entire SNR range.

Compared to the AV-Fusion FFT models, which were trained on the same data, the results reveal an average increase of 41.5% for high noise levels (-10dB) across all noise categories. For the SNR range from 0dB to 20dB, the average increase in WER is reduced to 11.0%. For these models, the number of trainable parameters is 79.3% to 89.1% lower than for AV-Fusion and 94.1% lower than for AV-HuBERT large, which explains the lower performance.

### V-C Noise-Scenario-Specific Adapter-Sets

TABLE [I](https://arxiv.org/html/2502.01709v1#S5.T1 "TABLE I ‣ V Results ‣ Adapter-Based Multi-Agent AVSR Extension for Pre-Trained ASR Models") provides the results for noise-category and noise-level-specific adapter models for both model sizes and a comparison to AV-Fusion with full fine-tuning and AV-HuBERT large. The noise-category-spcific adapters were trained on individual noise categories spanning the entire SNR range from -15dB to 30dB. The noise-level-specific adapters were trained on the SNR range greater than or less than 0dB, but received examples from all noise categories. All adapter-sets share the same frozen Whisper models. The results for the noise scenarios each model was trained for, are highlighted in gray, and show that noise-scenario-specific training leads to significant improvements compared to the LoRa-AVSR - Full noise spectrum models. The noise-level-specific adapter-set models in particular show a clear improvement compared to training over the entire SNR range, demonstrating the benefits of using adapter-sets for specific noise scenarios. The WER values are still worse, but relatively close to those of AV-Fusion FFT, which is remarkable since AV-Fusion trains many times more parameters. For the smaller models and the noise category Sidespeaker, we actually achieve an improvement compared to AV-Fusion for an SNR value of -10db.

In general, it is noticeable that the noise-level-specific models perform slightly better than the noise-category-specific models. Especially for high noise levels at -10dB and 0dB, the noise-level-specific models achieve lower WER values across both model sizes and the majority of noise categories. We hypothesize that the noise-level-specific HighNoise models are forced to pay high attention to the visual information during training, as the audio inputs are very noisy. In contrast, the noise-category-specific models receive many examples from the SNR range between 5dB to 30dB and 5% clean audio inputs, which may have the effect that these models do not require the visual information to generate correct embedding and logits, for the majority of training samples.

The blue/green marked rows represent the results achieved when the noise-category (green) and noise-level (blue) are not known a-priori but estimated with our proposed classifier for adapter-set selection (sec. IV.C). The noise-category-classifier achieves a recognition rate of 98.1%. The noise-level-classifier actually performs a SNR regression. We specify a threshold value of 5dB, which is used for the HighNoise/LowNoise selection, leading to a correct classification rate of 94.7%.

All noise-scenario-specific models with classifier achieve results that are almost identical to the optimum results for each noise-scenario-specific model, which demonstrates the strength of this approach. The only exception is the noise category Sidespeaker, especially for the noise-level-specific models.

We identified two reasons for the weakness at this noise category: First, for Sidespeaker noise, the gap between the results for the HighNoise and LowNoise models is larger than for any other noise category, especially at -10dB, which leads to a stronger negative influence of misclassifications. We suspect that this gap could be reduced by presenting a few examples from the LowNoise range to the HighNoise models during training, to get them used to these noise scenarios, and reduce the gap. Second, the noise-level-classifier performs poorer for this noise category compared to other noise categories. (Noise-Level-Classifier - correct classification rate at SNR -10dB: Babble 100.0% / Music 98.4% / Natural 93.3% / Sidespeaker 91.3%). An explanation might be that this noise category overlaps two equivalent speech signals and the classifier struggles to identify the main signal, leading to incorrect SNR predictions.

All noise-scenario-specific models achieve a significant improvement for both model sizes compared to the LoRa-AVSR - Full noise spectrum models and the results tend to be close to those of the AV-Fusion FFT, but are still slightly poorer. Comparing the number of trainable parameters reveals that the noise-level-specific models in particular have 58.6% to 78.6% less trainable parameters than AV-Fusion and 88.5% less trainable parameters than AV-HUBERT large.

As part of several ablation studies, we tested the AV-Fusion FFT models’ ability to handle audio-only information, to simulate the case that no visual information is available, which led to an dramatic increase in WER values even at low noise levels. This demonstrates one of the main advantages of our adapter-based models. If no visual information is available, the underlying unmodified ASR model can be used, which is very capable on audio-only data as it has been trained on huge amounts of speech data. Using the AV-Fusion small FFT model with 257M parameters, an extra Whisper small model with 244M parameters needs to be provided for this case.

Another advantage is the easy expandability, as the underlying Whisper model remains unchanged. This allows the extension by further adapter-sets, for instance additional noise categories or even more specific adapter-sets such as a Babble noise adapter-set explicitly trained on high noise levels to improve the adaptation to this specific scenario. In case of changing noise categories, a fully fine-tuned AV-Fusion or AV-HuBERT model would require a re-training.

## VI Conclusion

We presented an adapter-based approach to Audio-Visual Speech Recognition that allows to train noise-scenario-specific adapter-sets to cover a large range of noise levels and different noise categories. We deploy two classifiers with very high recognition rates to select the optimum adapter-set for each specific noise scenario. We demonstrate that the AV-Fusion approach, which is related to our approach, achieves a performance comparable to one of the current SOTA AVSR approaches, AV-HuBERT. Compared to AV-Fusion, our models reveal a slightly higher word error rate on average, which is partly caused by certain weaknesses towards the noise category Sidespeaker. Across large ranges of tested SNR values and noise categories, our models show a performance close to that of AV-Fusion and AV-HuBERT, despite 88.5% less trainable parameters and smaller overall model size compared to AV-HuBERT.

The moderate weaknesses in terms of performance are compensated by the advantages such as the expandability with additional noise scenario-specific adapter-sets and the usability of the unchanged underlying powerful Whisper ASR model, in case no visual information is available.

## References

- \[1\] Triantafyllos Afouras, Joon Son Chung, and Andrew Zisserman. LRS3-TED: a large-scale dataset for visual speech recognition. In arXiv preprint, 09 2018.
- \[2\] Andrei Andrusenko, Rauf Nasretdinov, and Aleksei Romanenko. UCONV-Conformer: High Reduction of Input Sequence Length for End-to-End Speech Recognition. 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1–5, 2022.
- \[3\] Baevski, Alexei and Zhou, Henry and Mohamed, Abdelrahman and Auli, Michael. Wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations. In Proceedings of the 34th International Conference on Neural Information Processing Systems, NIPS’20, Red Hook, NY, USA, 2020. Curran Associates Inc.
- \[4\] Zeren Chen, Ziqin Wang, Zhen Wang, Huayang Liu, Zhenfei Yin, Si Liu, Lu Sheng, Wanli Ouyang, and Jing Shao. Octavius: Mitigating Task Interference in MLLMs via MoE. In 2024 International Conference on Learning Representations (ICLR), 2024.
- \[5\] Joon Son Chung, Arsha Nagrani, and Andrew Zisserman. Voxceleb2: Deep speaker recognition. In Interspeech, 2018.
- \[6\] Tiantian Feng and Shrikanth S. Narayanan. PEFT-SER: On the Use of Parameter Efficient Transfer Learning Approaches For Speech Emotion Recognition Using Pre-trained Speech Models. 2023 11th International Conference on Affective Computing and Intelligent Interaction (ACII), pages 1–8, 2023.
- \[7\] Thomas Palmeira Ferraz, Marcely Zanon Boito, Caroline Brun, and Vassilina Nikoulina. Multilingual DistilWhisper: Efficient Distillation of Multi-task Speech Models via Language-Specific Experts. In 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024.
- \[8\] Yuan Gong, Sameer Khurana, Leonid Karlinsky, and James Glass. Whisper-AT: Noise-Robust Automatic Speech Recognizers are Also Strong Audio Event Taggers. In Interspeech 2023, 2023.
- \[9\] Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar, Yu Zhang, Jiahui Yu, Wei Han, Shibo Wang, Zhengdong Zhang, Yonghui Wu, and Ruoming Pang. Conformer: Convolution-augmented Transformer for Speech Recognition. In Interspeech 2023, pages 5036–5040, 10 2020.
- \[10\] Alexandros Haliassos, Pingchuan Ma, Rodrigo Mira, Stavros Petridis, and Maja Pantic. Jointly Learning Visual and Auditory Speech Representations from Raw Data. In 2023 International Conference on Learning Representations (ICLR), 2023.
- \[11\] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Tsai, Kushal Lakhotia, Ruslan Salakhutdinov, and Abdelrahman Mohamed. HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units. IEEE/ACM Transactions on Audio, Speech, and Language Processing, PP:1–1, 10 2021.
- \[12\] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-Rank Adaptation of Large Language Models. In 2022 International Conference on Learning Representations (ICLR), 2022.
- \[13\] Yingting Li, Ambuj Mehrish, Rishabh Bhardwaj, Navonil Majumder, Bo Cheng, Shuai Zhao, Amir Zadeh, Rada Mihalcea, and Soujanya Poria. Evaluating Parameter-Efficient Transfer Learning Approaches on SURE Benchmark for Speech Understanding. In 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1–5, 2023.
- \[14\] Wei Liu, Ying Qin, Zhiyuan Peng, and Tan Lee. Sparsely Shared LoRA on Whisper for Child Speech Recognition. In 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023.
- \[15\] Pingchuan Ma, Alexandros Haliassos, Adriana Fernandez-Lopez, Honglie Chen, Stavros Petridis, and Maja Pantic. Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels. In 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1–5, 2023.
- \[16\] Pingchuan Ma, Stavros Petridis, and Maja Pantic. End-To-End Audio-Visual Speech Recognition with Conformers. In 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 7613–7617, 2021.
- \[17\] Avner May, Dmitriy Serdyuk, Ankit Parag Shah, Otavio Braga, and Olivier Siohan. Audio-visual fine-tuning of audio-only ASR models. CoRR, abs/2312.09369, 2023.
- \[18\] Alec Radford, Jong Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever. Robust Speech Recognition via Large-Scale Weak Supervision. In ICML, 12 2022.
- \[19\] Andrew Rouditchenko, Yuan Gong, Samuel Thomas, Leonid Karlinsky, Hilde Kuehne, Rogerio Feris, and James Glass. Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation. In Interspeech 2024, 2024.
- \[20\] Paul Seo, Arsha Nagrani, and Cordelia Schmid. AVFormer: Injecting Vision into Frozen Speech Models for Zero-Shot AV-ASR. In CVPR 2023, pages 22922–22931, 06 2023.
- \[21\] Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, and Abdelrahman Mohamed. Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction. 2022 International Conference on Learning Representations (ICLR), 2022.
- \[22\] Bowen Shi, Wei-Ning Hsu, and Abdelrahman Mohamed. Robust Self-Supervised Audio-Visual Speech Recognition. In Proc. Interspeech 2022, pages 2118–2122, 2022.
- \[23\] Christopher Simic and Tobias Bocklet. Self-Supervised Adaptive AV Fusion Module for Pre-Trained ASR Models. In 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023.
- \[24\] David Snyder, Guoguo Chen, and Daniel Povey. MUSAN: A Music, Speech, and Noise Corpus, 2015. arXiv:1510.08484v1.
- \[25\] Yiming Wang and Jinyu Li. ResidualTransformer: Residual Low-Rank Learning with Weight-Sharing for Transformer Layers. In 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024.
- \[26\] Qingru Zhang, Minshuo Chen, Alexander Bukharin, Pengcheng He, Yu Cheng, Weizhu Chen, and Tuo Zhao. Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning . In 2023 International Conference on Learning Representations (ICLR), 2023.
- \[27\] Bingchen Zhao, Haoqin Tu, Chen Wei, Jieru Mei, and Cihang Xie. Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning. In The Twelfth International Conference on Learning Representations, 2024.
