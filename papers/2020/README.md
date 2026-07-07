# 2020

3 papers in this year.

### [A review of on-device fully neural end-to-end automatic speech recognition algorithms](2012.07974.md)
**Chanwoo Kim, Dhananjaya Gowda, Dongsoo Lee, Jiyeon Kim et al.** · 2020-12-14

<details>
<summary>Abstract</summary>

In this paper, we review various end-to-end automatic speech recognition algorithms and their optimization techniques for on-device applications. Conventional speech recognition systems comprise a large number of discrete components such as an acoustic model, a language model, a pronunciation model, a text-normalizer, an inverse-text normalizer, a decoder based on a Weighted Finite State Transducer (WFST), and so on. To obtain sufficiently high speech recognition accuracy with such conventional speech recognition systems, a very large language model (up to 100 GB) is usually needed. Hence, the corresponding WFST size becomes enormous, which prohibits their on-device implementation. Recently, fully neural network end-to-end speech recognition algorithms have been proposed. Examples include speech recognition systems based on Connectionist Temporal Classification (CTC), Recurrent Neural Network Transducer (RNN-T), Attention-based Encoder-Decoder models (AED), Monotonic Chunk-wise Attention (MoChA), transformer-based speech recognition systems, and so on. These fully neural network-based systems require much smaller memory footprints compared to conventional algorithms, therefore their on-device implementation has become feasible. In this paper, we review such end-to-end speech recognition models. We extensively discuss their structures, performance, and advantages compared to conventional algorithms.

</details>

### [A Better and Faster End-to-End Model for Streaming ASR](2011.10798.md)
**Bo Li, Anmol Gulati, Jiahui Yu, Tara N. Sainath et al.** · 2020-11-21

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have shown to outperform state-of-the-art conventional models for streaming speech recognition [1] across many dimensions, including quality (as measured by word error rate (WER)) and endpointer latency [2]. However, the model still tends to delay the predictions towards the end and thus has much higher partial latency compared to a conventional ASR model. To address this issue, we look at encouraging the E2E model to emit words early, through an algorithm called FastEmit [3]. Naturally, improving on latency results in a quality degradation. To address this, we explore replacing the LSTM layers in the encoder of our E2E model with Conformer layers [4], which has shown good improvements for ASR. Secondly, we also explore running a 2nd-pass beam search to improve quality. In order to ensure the 2nd-pass completes quickly, we explore non-causal Conformer layers that feed into the same 1st-pass RNN-T decoder, an algorithm called Cascaded Encoders [5]. Overall, we find that the Conformer RNN-T with Cascaded Encoders offers a better quality and latency tradeoff for streaming ASR.

</details>

### [Enhancing Monotonic Multihead Attention for Streaming ASR](2005.09394.md)
**Hirofumi Inaguma, Masato Mimura, Tatsuya Kawahara** · 2020-05-19

<details>
<summary>Abstract</summary>

We investigate a monotonic multihead attention (MMA) by extending hard monotonic attention to Transformer-based automatic speech recognition (ASR) for online streaming applications. For streaming inference, all monotonic attention (MA) heads should learn proper alignments because the next token is not generated until all heads detect the corresponding token boundaries. However, we found not all MA heads learn alignments with a naïve implementation. To encourage every head to learn alignments properly, we propose HeadDrop regularization by masking out a part of heads stochastically during training. Furthermore, we propose to prune redundant heads to improve consensus among heads for boundary detection and prevent delayed token generation caused by such heads. Chunkwise attention on each MA head is extended to the multihead counterpart. Finally, we propose head-synchronous beam search decoding to guarantee stable streaming inference.

</details>

