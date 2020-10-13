Title: ダイヤルイン番号(DIN)って、どうやって使うの？
Date: 2020-10-14
Slug: what-does-din-do
Lang: ja
Category:　Xoxzo Cloud Telephony/Voice API

### ダイヤルイン番号 API
ダイヤルイン番号 (DIN) は、着信用の地域番号で、オンライン契約いただける番号です。 
契約した番号に、パラメーターを設定することで、
着信した電話に、.mp3ファイルに準備した音声で応答したり、
テキスト読み上げ機能（TTS）を使ってカスタマイズメッセージで応答したり、
実際に着信を受け取りたい番号へ転送したり、
ボイスメールに伝言を受け取って保存したりできます。


### ダイヤルイン番号 API の使い方
1. [取得可能な番号を探す](https://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)<br>
   検索すると、取得可能な番号が表示されます。気に入った番号が見つかったら、 `din_uid` を控えておいてください。<br>
   XoxzoのAPIにてご契約可能な、各国のプレフィックスは [料金ページ](https://www.xoxzo.com/en/about/pricing/voice/#din)よりご確認いただけます。<br>
2. [番号を契約する](https://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)<br>
   控えておいた `din_uid` を使って、ダイヤルイン番号を取得しましょう。 <br>
   「ちょっとお試しで使ってみたいけど、一ヶ月分の料金を払うのは・・・」という場合には、番号契約後24時間以内にその番号を解約してください。料金ページに表示の
   [24時間以内の費用](https://www.xoxzo.com/ja/about/pricing/voice/#din) が適用されます。<br>
   これで、ご自分の電話番号を取得できました。<br>
3. [ダイヤルイン番号にアクションを関連付ける](https://docs.xoxzo.com/ja/din.html#attach-an-action-to-the-dial-in-number-via-api)<br>
   契約した番号に、`action_url` を設定してください。 <br>
   番号へ着信があると、`action_url` にて指定したURLに、`GET` リクエストが送られて、どのように応答するかのコマンドを受け取ります。<br>
4. [アクション URLにアクションコマンドを設定する](https://docs.xoxzo.com/ja/din.html#sample)<br>
    `action_url` から、下記のアクションコマンドを返してください。<br>
<div class="table-responsive">
  <table border="1" cellpadding="10" cellspacing="1">
      <tr>
         <td>
         アクション
         </td>
         <td>
         動作
         </td>
      </tr>
      <tr>
         <td>
         playback
         </td>
         <td>
         mp3 を再生する
         </td>
      </tr>
      <tr>
         <td>
         transfer
         </td>
         <td>
         別の電話番号へ転送する
         </td>
      </tr>
      <tr>
         <td>
         say
         </td>
         <td>
         指定したテキストを読み上げる (Text-to-Speech)
         </td>
      </tr>      
      <tr>
         <td>
         voicemail
         </td>
         <td>
         アカウントにボイスメールを保存する
         </td>
      </tr>
   </table>
</div>
5. これで、契約したダイヤルイン番号で、着信を受ける準備ができました！



### ダイアルイン番号取得に、更なる付加価値「ローカル発信者番号」
しかも、取得した番号を、更に便利にご利用いただくことができます。これが、*音声通話APIの**「ローカル発信者番号」オプション** *です。

**Xoxzoのダイアルイン番号を取得することにより、音声APIにてAPIより日本国内向けの発信を行う際、通常は発信者番号として使用できない国内番号を、表示することが可能になります。**

### 「ローカル発信者番号」オプションご利用までの流れ
1. [ダイアルイン番号を探す](http://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)
2. [ダイアルイン番号を取得する](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api) <br>
参照：[音声電話着信料金](https://www.xoxzo.com/ja/about/pricing/voice/#din)
3. [音声API](http://docs.xoxzo.com/ja/voice.html#simple-playback-api)を[JP向けのオプション・パラメーターを使い](http://docs.xoxzo.com/ja/voice.html#jp-specific-optional-parameters)利用する <br>
参照：[音声電話発信料金（ローカル発信者番号）](https://www.xoxzo.com/ja/about/pricing/voice/#outbound-call)

*複数の国内番号を発信者番号として表示する場合、複数のダイアルイン番号を取得してください。
  
このオプションの料金につきましては、[Xoxzoの音声通話料金ページ](https://www.xoxzo.com/ja/about/pricing/voice)を、サービス内容に関しては、[ダイアルイン番号のご案内ページ](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)をご参照ください。
