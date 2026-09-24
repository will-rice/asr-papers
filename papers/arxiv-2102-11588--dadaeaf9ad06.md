---
arxiv_id: "2102.11588"
title:
  "Data Fusion for Audiovisual Speaker Localization: Extending Dynamic Stream
  Weights to the Spatial Domain"
authors:
  - Julio Wissing
  - Benedikt Boenninghoff
  - Dorothea Kolossa
  - Tsubasa Ochiai
  - Marc Delcroix
  - Keisuke Kinoshita
  - Tomohiro Nakatani
  - Shoko Araki
  - Christopher Schymura
submitted: "2021-02-23"
categories:
  - cs.SD
  - cs.AI
  - cs.CL
  - cs.CV
  - cs.LG
  - eess.AS
  - eess.IV
arxiv_url: https://arxiv.org/abs/2102.11588
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:47:48+00:00"
references_parsed: 0
arxiv_version: ""
---

DATA FUSION FOR AUDIOVISUAL SPEAKER LOCALIZATION:\
EXTENDING DYNAMIC STREAM WEIGHTS TO THE SPATIAL DOMAIN
======================================================

###### Abstract

Estimating the positions of multiple speakers can be helpful for tasks like automatic speech recognition or speaker diarization. Both applications benefit from a known speaker position when, for instance, applying beamforming or assigning unique speaker identities. Recently, several approaches utilizing acoustic signals augmented with visual data have been proposed for this task. However, both the acoustic and the visual modality may be corrupted in specific spatial regions, for instance due to poor lighting conditions or to the presence of background noise. This paper proposes a novel audiovisual data fusion framework for speaker localization by assigning individual dynamic stream weights to specific regions in the localization space. This fusion is achieved via a neural network, which combines the predictions of individual audio and video trackers based on their time- and location-dependent reliability. A performance evaluation using audiovisual recordings yields promising results, with the proposed fusion approach outperforming all baseline models.

Index Terms—  audiovisual speaker localization, data fusion, dynamic stream weights

## 1 Introduction

Data fusion is a process aimed at combining several data sources to accomplish a task more reliably than it would be possible with just one individual sensor. This has several useful applications, ranging from medical diagnostics \[1\] to robotics \[2\] and smart buildings \[3\]. Tracking one or more speakers by means of acoustic and visual sensors also relies on an appropriate fusion of sensory inputs. This process is performed unconsciously in human listening, since humans naturally combine visual and acoustic stimuli in estimating the position of a person speaking or a sound source emitting noise \[4\].

Recent works in the domain of audiovisual speaker localization showed promising results utilizing different data fusion strategies. For example, \[5, 6\] introduce a variational Bayesian approximation to optimally merge acoustic and visual data for combined localization and tracking. A related approach introduced in \[7\] uses an expectation maximization (EM) algorithm for weighted clustering in the audiovisual observation space. Other probabilistic techniques for audiovisual speaker tracking based on particle filters were proposed in \[8, 9\]. Additionally, the work in \[10\] combined audiovisual speaker localization with speech separation on a robotic platform in a real-time processing system. A similarly designed audiovisual fusion system for smart rooms \[11\] allows for joint localization and identification of persons present in a room.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/figs/sample_output.png)

Fig. 1: Frame from the AVDIAR dataset \[12\], overlayed with speaker positions predicted by the proposed fusion model. Note that the model utilizes a discrete grid to represent the localization space, where each grid-cell is associated with a speaker presence probability, described in Sec. 2.3.

A classical approach to combine different sensors is the Kalman filter (KF) \[13\], where inference in a linear dynamical system (LDS) is carried out to estimate all latent variables of interest; such as positions, velocities or accelerations, based on noisy measurement data. Extending this concept to dynamic stream weights (DSWs) allows us to weight the contributions of each input based on their instantaneous reliability. This concept was originally proposed in the context of audiovisual automatic speech recognition (ASR) \[14\], and has proven valuable for speaker identification \[15\], but was also recently adopted for speaker localization and tracking \[16, 17\].

All of these approaches specify DSWs as time-dependent weighting factors for the acoustic and visual modalities. In this study, we introduce a fundamental update: Since the reliability of the acoustic and visual streams may also vary over time and _location_, we extend the idea of DSWs to the spatial dimension, as depicted in Fig. 1. Therefore, we introduce a spatial weighting matrix to replace the scalar DSWs used in previous works. Compared to previously proposed approaches, spatial DSWs can effectively capture specific position-dependent sensor reliability properties, e.g., bright lighting conditions coming from a certain direction or directional acoustic noise sources. Whereas scalar DSWs can only provide a global estimate of sensor reliability, the model proposed here provides a more fine-grained location-dependent framework for data fusion.

## 2 System description

The proposed data fusion network consists of two building-blocks: the individual unimodal tracking networks and the DSW-based data fusion network, as depicted in Fig 2.

### 2.1 Audio tracker

We adopt the unimodal audio tracker from the DOAnet architecture \[18\]. Here, a multi-channel short-time Fourier transform (STFT) is performed on the individual microphone signals. Time-frequency analysis is conducted on the 6-channel acoustic inputs using a window length of 1920 samples with no overlap and a fast Fourier transform (FFT) size of 2048. This results in a frame length of $`40\hspace{0pt}\text{ms}`$, matching the length of one video frame in the utilized dataset. A context of one frame in both temporal directions around the $`t`$-th time step is used, which results in a 3-dimensional acoustic input tensor $`\mathbf{X}_{\text{A},t}`$ of dimensions $`3 \times 1024 \times 12`$, representing the time, frequency and channel dimensions. The third dimension is spanned by the stacked amplitude and phase of all 6 audio channels.

Similar to the DOAnet architecture, the acoustic input tensor is fed through 4 convolutional stages first. Herein, each stage is composed of a 2-dimensional convolution with $`64`$ filters and a kernel size of $`3 \times 3`$, batch normalization, rectified linear unit (ReLU) nonlinearity, max-pooling of size $`1 \times 8`$, and a dropout layer with a rate of $`0.5`$. Subsequently, the tensor is flattened, yielding a dimensionality of $`3 \times 128`$, and input to a bidirectional gated recurrent unit (GRU) with two layers. The output of these recurrent layers is then fed to a classification network, composed of three fully connected layers with $`2048`$, $`1024`$ and $`512`$ neurons and ReLUs, respectively. Lastly, the output layer is constructed using another fully connected layer with $`480`$ neurons and sigmoid activations. The outputs are reshaped to a grid with $`20 \times 24`$ cells, as depicted in Fig. 1. The grid size was chosen to roughly represent the size of a face in the utilized dataset. Using a binary indicator variable $`\zeta_{i,j}`$ corresponding to the $`i`$-th row and $`j`$-th column of the grid, the probability that a speaker is located at this particular grid point given only the current acoustic observation can be expressed as $`z_{\text{A},t}^{(i,j)} = {p\hspace{0pt}\left( \zeta_{i,j} \middle| \mathbf{X}_{\text{A},t} \right)}`$.

### 2.2 Video tracker

Video tracking is conducted using the _you only look once_ (YOLO) framework proposed in \[19\], which achieves a high detection rate in combination with real-time tracking capabilities. The implementation of YOLOFace is used, which is based on YOLOv3 \[20\]. Before an input video frame $`\mathbf{X}_{\text{V},t}`$ is processed by the video tracker, it is first resized to $`832 \times 832`$ pixels to meet the requirements of YOLOv3. We adapt the bounding box output to the $`20 \times 24`$ grid size. The grid size can be set to arbitrary values if one is willing to retrain the network. We evaluated the localization performance using several grid sizes. However, we did not find any significant differences in localization performance. We decided to set the size of the individual grid-cells to roughly match the size of a human face in the dataset. The video tracker’s output probability is denoted as $`z_{\text{V},t}^{(i,j)} = {p\hspace{0pt}\left( \zeta_{i,j} \middle| \mathbf{X}_{\text{V},t} \right)}`$.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/x1.png)

Fig. 2: High-level overview of the proposed data fusion framework. The acoustic and visual inputs $`\mathbf{X}_{\text{A},t}`$ and $`\mathbf{X}_{\text{V},t}`$ are first processed via unimodal trackers and then combined in a dedicated fusion network, producing a grid of speaker presence probabilities $`\mathbf{Y}_{t}`$ as output.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/x2.png)

Fig. 3: Architecture of the acoustic and visual DSW estimation networks, taking as input the observations $`\mathbf{Z}_{\text{A},t}`$ and $`\mathbf{Z}_{\text{V},t}`$ obtained from the acoustic and visual trackers and producing as output the corresponding DSWs $`\mathbf{\Lambda}_{\text{A},t}`$ and $`\mathbf{\Lambda}_{\text{V},t}`$ covering the spatial grid.

### 2.3 Data fusion

At each time $`t`$, a conventional data fusion strategy would handle all acoustic and visual tracker outputs equally. In the log-domain, this _flat fusion_ strategy can be expressed as

```math
{y_{t}^{(i,j)} = {{\log z_{\text{A},t}^{(i,j)}} + {\log z_{\text{V},t}^{(i,j)}}}},
```

where $`y_{t}^{(i,j)}`$ represents the log-likelihood of a speaker being present in grid-cell $`(i,j)`$ at time-step $`t`$, taking into account both acoustic and visual observations. Note that the derivation of Eq. (1) is based on assuming statistical independence between acoustic and visual observations, as well as imposing an uninformative prior on $`{\zeta_{i,j}\hspace{0pt}{\forall i}},j`$, cf. \[16\]. However, when working with audiovisual input data, modalities may not be equally informative in all spatial regions due to, e.g., challenging lighting conditions or a directional noise source. In these cases, it should be possible to weight each source individually to lessen or increase the impact of an input. This process must be dynamic, in the sense that the network should be able to adapt over space and time. A _weighted fusion_ approach

```math
y_{t}^{(i,j)} = {{\lambda_{\text{A},t}^{(i,j)}\hspace{0pt}{\log z_{\text{A},t}^{(i,j)}}} + {\lambda_{\text{V},t}^{(i,j)}\hspace{0pt}{\log z_{\text{V},t}^{(i,j)}}}}
```

is proposed here, where $`\lambda_{\text{A},t}^{(i,j)}`$, $`\lambda_{\text{V},t}^{(i,j)} \in \lbrack 0,\, 1\rbrack`$ denote the location- and time-dependent DSWs for the acoustic and visual modalities, respectively. In this manner, we are proposing an extension of the DSW idea, originally introduced to handle only time-variant sensor reliability, to the spatial domain, allowing us to learn how different locations are covered more or less reliably by the available modalities. All relevant variables can be expressed in matrix notation as

```math
{{\mathbf{Y}_{t} = \begin{bmatrix}
y_{t}^{(i,j)}
\end{bmatrix}_{i,j}},{{\mathbf{Z}_{m,t} = \begin{bmatrix}
z_{m,t}^{(i,j)}
\end{bmatrix}_{i,j}},{\mathbf{\Lambda}_{m,t} = \begin{bmatrix}
\lambda_{m,t}^{(i,j)}
\end{bmatrix}_{i,j}}}},
```

with $`m \in \left\{ \text{A},\text{V} \right\}`$, each covering the entire $`20 \times 24`$ grid. The actual data fusion is performed conjointly with estimating the DSWs in Eq. (2) and the subsequent estimation of the speaker positions.

### 2.4 Weight estimation

The individual acoustic and visual tracking networks discussed in Secs. 2.1 and 2.2, serve as inputs to the fusion neural network. The architecture of the corresponding DSW estimation networks is depicted in Fig. 3. Its output is subsequently combined with the outputs from both unimodal trackers according to Eq. (2). To further refine the resulting speaker presence probability grid, it is fed into a dedicated refinement network based on the image restoration architecture proposed in \[21\]. The parameterization of the model \[21\] is adapted to the specific requirements of this work. In particular, the input and output size is set to $`20 \times 24`$, matching the size of the probability grid. Each convolutional layer consists of 128 filters with a kernel size of $`3 \times 3`$ and padding. The refinement operation is valuable to remove outliers and noisy estimates from the output grid, which should only contain peaks in grid cells close to the true speaker positions.

## 3 Experimental setup

In this section, we define the experimental settings and metrics¹¹1A Python implementation of all algorithms described in this paper is publicly available at https://github.com/rub-ksv/spatial-stream-weights.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/x3.png)

(a) Audio Baseline

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/x4.png)

(b) Spatially invariant DSWs

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2102.11588/assets/x5.png)

(c) Weighted Fusion

Fig. 4: Benchmark results plotted with respect to the threshold. The dashed lines represent the best unimodal baseline results.

### 3.1 Dataset

The AVDIAR \[12\] dataset is employed to evaluate the tracking capabilities of the proposed data fusion strategy. It contains 27 audiovisual sequences, which were recorded in three different rooms with a duration between 10 seconds and 3 minutes. The overall duration of the dataset is about 27 minutes. The recordings were conducted using 6 microphones attached to a dummy head and two cameras located right below the head. The microphone signals were acquired using a sampling rate of 48 kHz. The cameras cover a field of view of $`{{97\hspace{0pt}{^\circ}} \times 80}\hspace{0pt}{^\circ}`$ at 25 frames per second. The video signals have a resolution of $`720 \times 450`$ pixels. In this work, only one video signal from the left camera is used. The dataset was partitioned according to a training, validation and test split utilizing approximately $`75\%`$, $`10\%`$ and $`15\%`$ of the available data, respectively. The splitting procedure ensured that all subsets included audiovisual sequences with one, two, three and four simultaneously visible speakers.

### 3.2 Implementation details

All trainable weights were initialized using the Glorot initialization scheme \[22\]. In our experiments, the Adam optimizer \[23\] with a batch size of 64, a learning rate of 0.001 and early stopping yielded the best results. The fusion networks were trained for 20 epochs, with early stopping triggering in the first five epochs with a patience of 4. The audio tracking networks were trained for 100 epochs, with early stopping triggering after 30 epochs with a patience of 20.

### 3.3 Evaluation metrics

Localization error (LE) and frame recall (FR), as proposed in \[18, 24\], were utilized as evaluation metrics in this work. The LE metric was slightly modified to cope with the discrete grid structure used here. Therefore, the Euclidean distance between a ground-truth speaker position and the center point of a grid cell where a speaker was detected (both represented as pixel coordinates), was utilized. This distance was computed for all possible combinations of detected speakers and ground-truth speaker positions at each time-frame. If fewer speakers were predicted than are actually present, the prediction vector was filled with the next highest activation, to have at least one prediction per target. To calculate the localization error for an estimated speaker position given the corresponding ground-truth, a cost matrix was optimized using the Hungarian algorithm \[25\]. The resulting distances were summed up and divided by the total number of speakers present at the particular time-frame, yielding the average distance per speaker. This process is repeated and averaged for the complete test set to obtain the final LE metric.

The FR represents the ability of the network to predict the correct number of speakers in a specific frame. If the estimated number of speakers matches the ground-truth in that frame, the metric is set to one, otherwise it is zero. In the proposed framework, the number of speakers is set to the number of posterior grid probabilities surpassing the specified detection threshold, which has to be set empirically or via, e.g., a grid-search approach. Potentially, it might be included into an end-to-end optimization pipeline. Therefore, in Sec. 4.1, different threshold values are evaluated for this purpose.

The FR cannot differentiate between missed and excessive numbers of speakers. Therefore, we additionally count the average number of false positives (FPs) for each frame. This metric can be used to better understand and analyze causes of any detection issues. A low FR in combination with a high FP suggests that the network is not performing well due to the threshold being too low. On the other hand, in combination with a low FP it seems reasonable that either the threshold is too high, pruning too many activations, or that the detector is not working properly.

## 4 Results and discussion

In the following, we present and analyze the results of our baseline systems and the proposed fusion network architecture.

### 4.1 Baseline methods

The results of our two single-modality baselines, i.e. audio- and video-only tracking systems, are provided in the first two rows of Tab. 1. As expected, the video-only baseline is generally superior in good visual conditions. The audio-only system outperforms video localization when faces are occluded or outside the field-of-view.

With the single-modality audio tracker and a threshold of 0.75, an LE of 11.93 pixels was achieved, while the FR was quite low at 23%. On average, a frame contained 1.07 false positives. Fig. 4 (a) shows the performance of the audio tracker as a function of the threshold. The LE shows that the audio tracker predicts speakers with an error of roughly half a grid point. However, the low FR indicates that many false positives are included in the tracking result. Even with a threshold of 0.75, on average, one false positive is included in every frame.

|                       | LEpx  | FR   | FP    |
| --------------------- | ----- | ---- | ----- |
| Audio-only (Sec. 2.1) | 11.93 | 0.24 | 0.072 |
| Video-only (Sec. 2.2) | 19.95 | 0.83 | 0.006 |
| Flat fusion (Eq. 1)   | 7.65  | 0.82 | 0.003 |

Table 1: Results of the baseline trackers. For audio only the results for a threshold of 0.75 are given. For audio-visual tracking, we show the results of spatially flat fusion at a threshold of 0.75.

In comparison to the audio-only system, the video tracker in the second row in Tab. 1 unsurprisingly achieves a significant higher FR of 83.45%, due to its access to a highly informative modality, in line with its good benchmark results in other works \[20, 26\]. Note that no threshold is needed for the video tracker, as its output is binary. Additionally, the number of false positives per frame is lower, at 0.006. The LE is still below the size of one grid point with 19.95 pixels distance on average.

The face tracking capabilities lead to a good result with YOLO detecting the right number of faces in most cases. This is also reflected by the number of false positives, which are close to zero.

Finally, the third row shows results of our naive audio-visual baseline system with the flat fusion, implemented according to Eq. (1). As can be seen, the performance improves already, giving a lower localization error and false positive rate than the best uni-modal system at a virtually identical frame recall to the better-performing video setup.

### 4.2 Spatially invariant fusion

Fig. 4 (b) shows the results for the spatially invariant dynamic stream weighting approach. In this case, the DSWs in Eq. (2) are simplified by using a time-variant but spatially invariant scalar, i.e.: $`y_{t}^{(i,j)} = {{\lambda_{t}\hspace{0pt}{\log z_{\text{A},t}^{(i,j)}}} + {\left( {1 - \lambda_{t}} \right)\hspace{0pt}{\log z_{\text{V},t}^{(i,j)}}}}`$.

The dashed lines in Fig. 4 (b) represent the best reported single-modality baseline results for the LE and FR, respectively. The spatially invariant fusion is able to achieve a similar, but slightly worse FR of 0.82. Taking the threshold into consideration, the FR rises from 0.1 to above 0.7 for thresholds of 0.5 to 0.6. The reason is that the low activations around 0.5 of the audio-only tracker are carried over to the spatially invariant fusion and the flat fusion as well. Beyond a threshold of 0.6, the FR increases slowly but steadily.

Comparing the LEs in Fig. 4 (b) with the reported values in Tab. 1, we can observe that incorporating additional information to the data fusion layer leads to further improvements in the model’s ability to extrapolate the ground-truth location of the speakers: With temporal information, we see an improvement from 11.9 to 10.1 pixels. With the flat fusion strategy reported in Tab. 1, we would see a lower LE, reduced from 10.1 to 7.7 pixels.

Through multi-modal fusion, the number of false positives also improves w.r.t. the respective best-performing unimodal system, which is again similarly observable for the flat fusion strategy. Note that lower thresholds generally return worse results and choosing a higher threshold helps to mask out outliers. Increasing the threshold beyond 0.55 does not lead to any further changes in the LEs and FPs, indicating that outliers are sufficiently suppressed at this threshold.

### 4.3 Spatially weighted fusion

Fig. 4 (c) shows the performance of the weighted fusion system. At a threshold of 0.75, the network achieves a FR of 0.92, clearly outperforming all the other strategies. Again, the low performance at a threshold of 0.5 mentioned in Sec. 4.2 is still visible.

In terms of the LE, the best result was achieved with 4.10 pixels distance at a threshold of 0.75. For all thresholds above 0.5, nearly constant results were measured. The FPs per frame were relatively low, at an average of 0.028 over-predictions per frame.

Overall, the spatially weighted fusion strategy with a location-dependent matrix achieved the best performance. The target speakers were located with a high precision, showing the lowest LE measured across all experiments. Even though the number of false positives was increased slightly, the overall capabilities of the network are significantly better compared to the other systems.

Finally, comparing Fig. 4 (b) and (c), the questions arises, whether the improved performance may be caused by the ability to focus on different modalities in different parts of the room and whether this ability may be helpful in dealing with multiple speakers. To investigate these questions, we compared the performance metrics for audio frames containing only a single speaker with audio frames containing $`4`$ different speakers. As hypothesized, we achieved the same results (LE = 1.31, FR = 1 and FP = 0) for both fusion strategies, when only a single speaker is involved. In contrast, when 4 speakers are present, the performances differ significantly. While the performance of the spatially weighted fusion strategy remains stable (LE = 0,53, FR = 0,99, FP = 0), the LE of the spatially invariant fusion strategy suffers (LE = 10,4, FR = 0,81, FP = 0). While based on comparatively little data, this analysis appears to indicate that spatial weighting is better equipped for dealing with multi-speaker scenarios.

## 5 Conclusion

In this paper, we introduced a novel deep-learning-based data-fusion strategy by extending the idea of dynamic temporal stream weights to the spatial domain. Experiments show that the unimodal baseline video tracker based on the YOLO-framework achieved accurate results as a stand-alone system, while, unsurprisingly, using only the unimodal audio tracker led to a significantly higher false positive rate. However, by fusing acoustic and visual information, it was possible to achieve an improved tracking result, with a 10% increase of the frame recall and a far more accurate localization, showing an error of 3.83 pixels on average. The results show that the audiovisual tracking system benefits from the proposed data fusion strategy, and that adding spatial dependence of stream weights is highly beneficial compared to a purely temporal dependence, as in standard dynamic stream weighting.

## References

- \[1\] J. J. A. Mendes, M. Vieira, M. B. Pires, and S. L. Stevan, “Sensor fusion and smart sensor in sports and biomedical applications,” Sensors (Basel, Switzerland), vol. 16, no. 10, September 2016.
- \[2\] M. Kam, X. Zhu, and P. Kalata, “Sensor fusion for mobile robot navigation,” Proceedings of the IEEE, vol. 85, no. 1, pp. 108–119, 1997.
- \[3\] W. Li, Z. Wang, G. Wei, L. Ma, J. Hu, and D. Ding, “A survey on multisensor fusion and consensus filtering for sensor networks,” Discrete Dynamics in Nature and Society, vol. 2015, pp. 683701, Oct 2015.
- \[4\] J. R. Hershey and J. R. Movellan, “Audio Vision: Using audio-visual synchrony to locate sounds,” in Advances in Neural Information Processing Systems 12, S. A. Solla, T. K. Leen, and K. Müller, Eds., pp. 813–819. MIT Press, 2000.
- \[5\] Y. Ban, X. Alameda-Pineda, Laurent Girin, and R. Horaud, “Variational Bayesian inference for audio-visual tracking of multiple speakers,” CoRR, vol. abs/1809.10961, 2018.
- \[6\] X. Alameda-Pineda, S. Arias, Y. Ban, G. Delorme, L. Girin, R. Horaud, X. Li, B. Morgue, and G. Sarrazin, “Audio-visual variational fusion for multi-person tracking with robots,” in Proceedings of the 27th ACM International Conference on Multimedia, New York, NY, USA, 2019, MM ’19, p. 1059–1061, Association for Computing Machinery.
- \[7\] I. D. Gebru, X. Alameda-Pineda, R. Horaud, and F. Forbes, “Audio-visual speaker localization via weighted clustering,” in 2014 IEEE International Workshop on Machine Learning for Signal Processing (MLSP), Sep. 2014, pp. 1–6.
- \[8\] D. Gatica-Perez, G. Lathoud, I. McCowan, J. . Odobez, and D. Moore, “Audio-visual speaker tracking with importance particle filters,” in Proceedings 2003 International Conference on Image Processing, 2003, vol. 3, pp. III–25.
- \[9\] D. Gatica-Perez, G. Lathoud, J. Odobez, and I. McCowan, “Audiovisual probabilistic tracking of multiple speakers in meetings,” IEEE Transactions on Audio, Speech, and Language Processing, vol. 15, no. 2, pp. 601–616, Feb 2007.
- \[10\] K. Nakadai, K. Hidai, H. G. Okuno, and H. Kitano, “Real-time speaker localization and speech separation by audio-visual integration,” in Proceedings 2002 IEEE International Conference on Robotics and Automation, 2002, vol. 1, pp. 1043–1049.
- \[11\] C. Busso, S. Hernanz, C.-W. Chu, S.-I. Kwon, S. Lee, P. G. Georgiou, I. Cohen, and S. Narayanan, “Smart room: participant and speaker localization and identification,” in Proceedings. (ICASSP ’05). IEEE International Conference on Acoustics, Speech, and Signal Processing, 2005., 2005, vol. 2, pp. ii/1117–ii/1120 Vol. 2.
- \[12\] I. D. Gebru, S. Ba, X. Li, and R. Horaud, “Audio-Visual Speaker Diarization Based on Spatiotemporal Bayesian Fusion,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 40, no. 5, 2018.
- \[13\] R. E. Kalman, “A new approach to linear filtering and prediction problems,” Journal of Basic Engineering, vol. 82, no. 1, pp. 35–45, 03 1960.
- \[14\] H. Meutzner, N. Ma, R. Nickel, C. Schymura, and D. Kolossa, “Improving audio-visual speech recognition using deep neural networks with dynamic stream reliability estimates,” in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), March 2017, pp. 5320–5324.
- \[15\] L. Schönherr, D. Orth, M. Heckmann, and D. Kolossa, “Environmentally robust audio-visual speaker identification,” in 2016 IEEE Spoken Language Technology Workshop (SLT), Dec 2016.
- \[16\] C. Schymura and D. Kolossa, “Audiovisual speaker tracking using nonlinear dynamical systems with dynamic stream weights,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 1065–1078, 2020.
- \[17\] C. Schymura, T. Ochiai, M. Delcroix, K. Kinoshita, T. Nakatani, S. Araki, and D. Kolossa, “A Dynamic Stream Weight backprop Kalman filter for audiovisual speaker tracking,” in ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 581–585.
- \[18\] S. Adavanne, A. Politis, and T. Virtanen, “Direction of arrival estimation for multiple sound sources using convolutional recurrent neural network,” in 2018 26th European Signal Processing Conference (EUSIPCO), Sep. 2018, pp. 1462–1466.
- \[19\] J. Redmon, S. K. Divvala, R. B. Girshick, and A. Farhadi, “You only look once: Unified, real-time object detection,” CoRR, vol. abs/1506.02640, 2015.
- \[20\] J. Redmon and A. Farhadi, “YOLOv3: An incremental improvement,” CoRR, vol. abs/1804.02767, 2018.
- \[21\] X. Mao, C. Shen, and Y. Yang, “Image restoration using very deep convolutional encoder-decoder networks with symmetric skip connections,” in Advances in Neural Information Processing Systems 29, D. D. Lee, M. Sugiyama, U. V. Luxburg, I. Guyon, and R. Garnett, Eds., pp. 2802–2810. Curran Associates, Inc., 2016.
- \[22\] X. Glorot and Y. Bengio, “Understanding the difficulty of training deep feedforward neural networks,” in Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, Yee Whye Teh and Mike Titterington, Eds., Chia Laguna Resort, Sardinia, Italy, 13–15 May 2010, vol. 9 of Proceedings of Machine Learning Research, pp. 249–256, PMLR.
- \[23\] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, Y. Bengio and Y. LeCun, Eds., 2015.
- \[24\] S. Adavanne, A. Politis, J. Nikunen, and T. Virtanen, “Sound event localization and detection of overlapping sources using convolutional recurrent neural networks,” IEEE Journal of Selected Topics in Signal Processing, vol. 13, no. 1, pp. 34–48, 2019.
- \[25\] H. W. Kuhn, “The Hungarian method for the assignment problem,” Naval Research Logistics Quarterly, vol. 2, no. 1‐2, pp. 83–97, 1955.
- \[26\] W. Chen, H. Huang, S. Peng, C. Changsheng, and C. Zhang, “YOLO-Face: a real-time face detector,” The Visual Computer, Mar 2020.
