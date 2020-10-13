Title: ダイヤルインナンバー(DIN)って、どうやって使うの？
Date: 2020-10-14
Slug: what-does-din-do
Lang: ja
Category:　Xoxzo Cloud Telephony/Voice API

### ダイヤルインナンバー API
ダイヤルインナンバー (DIN) は、着信用の地域番号で、オンライン契約いただける番号です。 
契約した番号に、パラメーターを設定することで、
着信した電話に、.mp3ファイルに準備した音声で応答したり、
テキスト読み上げ機能（TTS）を使ってカスタマイズメッセージで応答したり、
実際に着信を受け取りたい番号へ転送したり、
ボイスメールに伝言を受け取って保存したりできます。


### ダイヤルインナンバー API の使い方
1. [取得可能な番号を探す](https://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)
   検索すると、取得可能な番号が表示されます。気に入った番号が見つかったら、 `din_uid` を控えておいてください。
   XoxzoのAPIにてご契約可能な、各国のプレフィックスは [料金ページ](https://www.xoxzo.com/en/about/pricing/voice/#din)よりご確認いただけます。
   
2. [番号を契約する](https://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)
   控えておいた `din_uid` を使って、ダイヤルインナンバーを取得しましょう。 
   「ちょっとお試しで使ってみたいけど、一ヶ月分の料金を払うのは・・・」という場合には、番号契約後24時間以内にその番号を解約してください。料金ページに表示の
   [24時間以内の費用](https://www.xoxzo.com/ja/about/pricing/voice/#din) が適用されます。
   
   これで、ご自分の電話番号を取得できました。
   
3. [ダイヤルインナンバーにアクションを関連付ける](https://docs.xoxzo.com/ja/din.html#attach-an-action-to-the-dial-in-number-via-api)
   契約した番号に、`action_url` を設定してください。 
   番号へ着信があると、`action_url` にて指定したURLに、`GET` リクエストが送られて、どのように応答するかのコマンドを受け取ります。
   
4. [アクション URLにアクションコマンドを設定する](https://docs.xoxzo.com/ja/din.html#sample)
    `action_url` から、下記のアクションコマンドを返してください。
   <table frame-"box">
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

5. これで、契約したダイヤルインナンバーで、着信を受ける準備ができました！


### More merit with Dial-In-Numbers API
In addition, with any Japanese number you subscribe, you can use that number even more useful, this is what the [*optional **Local Caller ID**.*](https://www.xoxzo.com/en/about/voice-api/)

**By default, restrictions in Japan does not allow you to use a local number as the caller ID. Our optional local caller ID functionality through our Dial In Numbers allows you to use a local Japan number for your voice calls.**

### Here is how to:
1. [Find your favorite prefix number to subscribe](http://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api)
2. [Subscribe to the number](http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)</br>
Ref: [Dial-In-Numbers API](https://www.xoxzo.com/en/about/pricing/voice/#din)
3. Enjoy [calling](http://docs.xoxzo.com/en/voice.html#simple-playback-api) with notifying your call receivers who is calling by [using the jp optional parameter.](http://docs.xoxzo.com/ja/voice.html#jp-specific-optional-parameters)</br>
Ref: [Pricing of Voice API](https://www.xoxzo.com/en/about/pricing/voice/#outbound-call)
