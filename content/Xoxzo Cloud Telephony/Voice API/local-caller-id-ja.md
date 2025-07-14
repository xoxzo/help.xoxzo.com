Title: ダイアルイン番号のオプション　ローカル発信者番号について  
Date: 2017-08-21 11:00  
Slug: local-caller-id-for-dial-in-numbers  
Lang: ja  
Category: Xoxzo Cloud Telephony/Voice API  

### ローカル発信者番号オプションとは？

このページでは、Xoxzoのダイアルイン番号に付加できる「ローカル発信者番号」オプションについて説明します。

このオプションを利用すると、取得したダイアルイン番号を**日本国内向けの発信時に、発信者番号として表示**できるようになります。  
通常、日本国内では制限により任意の番号を発信者番号として表示できませんが、ローカル発信者番号を利用することで、実在する国内番号を発信元として通知できます。

---

### ご利用手順

1. [ダイアルイン番号を探す](http://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)  
2. [ダイアルイン番号を取得する](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)  
   参照：[音声電話着信料金](https://www.xoxzo.com/ja/about/pricing/voice/#din)  
3. [音声API](http://docs.xoxzo.com/ja/voice.html#simple-playback-api)を使用して発信する  
   [JP向けのオプション・パラメーターを使用する](http://docs.xoxzo.com/ja/voice.html#jp-specific-optional-parameters)  
   参照：[音声電話発信料金（ローカル発信者番号）](https://www.xoxzo.com/ja/about/pricing/voice/#outbound-call)  

※複数の国内番号を発信者番号として使用したい場合、それぞれに対応するダイアルイン番号を取得してください。

---

### 関連リンク

- [Xoxzoの音声通話料金ページ](https://www.xoxzo.com/ja/about/pricing/voice)  
- [ダイアルイン番号のご案内ページ（ブログ）](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)
