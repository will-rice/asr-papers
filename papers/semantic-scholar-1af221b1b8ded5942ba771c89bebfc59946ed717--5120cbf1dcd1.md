---
arxiv_id: s2:1af221b1b8ded5942ba771c89bebfc59946ed717
title: ANALISIS PERFORMA OCR TESSERACT DAN CRNN PADA DOKUMEN SURAT JALAN SEMI-TERSTRUKTUR
authors:
  - Ali As’ad
  - Iska Yanuartanti
  - Danang Erwanto
submitted: "2026-07-10"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/1af221b1b8ded5942ba771c89bebfc59946ed717
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-15T06:57:26+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Surat jalan merupakan dokumen penting dalam proses logistik yang memerlukan pencatatan data secara akurat, namun metode manual yang masih digunakan seringkali tidak efisien dan rentan terhadap kesalahan, terutama pada lingkungan dengan volume tinggi. Penelitian ini bertujuan untuk mengevaluasi performa Optical Character Recognition (OCR) berbasis Tesseract dan Convolutional Recurrent Neural Network (CRNN) dalam mengenali teks pada dokumen semi-terstruktur. Penelitian ini menggunakan pendekatan eksperimental komparatif dengan dataset sebanyak 200 citra dokumen yang mencakup 180 teks cetak dan 20 tulisan tangan dengan berbagai variasi kondisi. Sebanyak 33 citra digunakan sebagai data uji, sedangkan sisanya digunakan sebagai data pelatihan dengan augmentasi. Sistem yang dikembangkan meliputi preprocessing citra, pengenalan teks, serta ekstraksi field menggunakan regular expression. Evaluasi dilakukan menggunakan metrik Character Error Rate (CER), Word Error Rate (WER), dan Match Error Rate (MER). Hasil menunjukkan bahwa OCR Tesseract lebih unggul pada tingkat karakter (CER) sebesar 42,84% , sedangkan OCR+CRNN menunjukkan performa yang relatif lebih baik pada tingkat kata dan pencocokan keseluruhan (WER dan MER) sebesar 68,24% dan 51,56% . Perlu dicatat bahwa kedua nilai tersebut masih sangat tinggi, CER 42,84% mengindikasikan hampir separuh karakter masih salah dikenali, sedangkan WER 68,24% menunjukkan lebih dari dua pertiga kata masih mengandung kesalahan, sehingga sistem belum siap untuk diterapkan secara praktis. Namun, peningkatan performa oleh CRNN belum signifikan, yang mengindikasikan keterbatasan jumlah dan variasi data pelatihan. Selain itu, performa sistem dipengaruhi oleh karakteristik dokumen, di mana teks cetak memberikan hasil yang lebih baik dibandingkan tulisan tangan yang masih terbatas dan belum representatif. Pada tahap ekstraksi informasi, field terstruktur menunjukkan akurasi lebih tinggi dibandingkan field kompleks, yang menegaskan bahwa kualitas hasil OCR menjadi faktor utama dalam keberhasilan ekstraksi. Penelitian ini menunjukkan bahwa pemilihan metode OCR perlu disesuaikan dengan karakteristik dokumen serta menegaskan pentingnya ketersediaan dataset yang lebih besar dan beragam untuk meningkatkan performa model berbasis deep learning.
