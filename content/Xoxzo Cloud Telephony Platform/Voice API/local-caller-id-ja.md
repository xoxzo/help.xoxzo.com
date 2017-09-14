Title: ダイアルイン番号のオプション　ローカル発信者番号について
Date: 2017-08-21 11:00
Slug: local-caller-id-for-dial-in-numbers
Lang: ja
Category:　Xoxzo Cloud Telephony Platform/Voice API


### Xoxzoのダイアルイン番号API
着信した電話をコントロールする、[Xoxzoのダイアルイン番号API](https://www.xoxzo.com/ja/about/dial-in-api/)では、専用の着信番号を取得することによって、その番号で着信した通話に決まった音声ファイルで応答したり、別の番号へ転送したりすることが可能です。

### ダイアルイン番号取得に、更なる付加価値「ローカル発信者番号」
しかも、取得した番号を、更に便利にご利用いただくことができます。これが、*音声通話APIの**「ローカル発信者番号」オプション** *です。

**Xoxzoのダイアルイン番号を取得することにより、音声APIにてAPIより日本国内向けの発信を行う際、通常は発信者番号として使用できない国内番号を、表示することが可能になります。**

### 「ローカル発信者番号」オプションご利用までの流れ
1. [ダイヤルイン番号を探す](http://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)
2. [ダイヤルイン番号を取得する](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)
参照：[音声電話着信料金](https://www.xoxzo.com/ja/about/pricing/#din)
3. [音声API](http://docs.xoxzo.com/ja/voice.html#simple-playback-api)を[JP向けのオプション・パラメーターを使い](http://docs.xoxzo.com/ja/voice.html#jp-specific-optional-parameters)利用する
参照：[音声電話発信料金（ローカル発信者番号）](https://www.xoxzo.com/ja/about/pricing/#voice)

*複数の国内番号を発信者番号として表示する場合、複数のダイヤルイン番号を取得してください。
  
このオプションの料金につきましては、[Xoxzoの音声通話料金ページ](https://www.xoxzo.com/ja/about/pricing/#voice)を、サービス内容に関しては、[ダイアルイン番号のご案内ページ](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)をご参照ください。
