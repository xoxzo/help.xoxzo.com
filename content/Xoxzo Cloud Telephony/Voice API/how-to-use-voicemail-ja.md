Title: ボイスメールって、どうやって使うの？
Date: 2020-10-14
Slug: how-to-use-voicemail
Lang: ja
Category:　Xoxzo Cloud Telephony/Voice API

### ボイスメールとダイヤルイン番号 API
ボイスメール機能は、契約したダイヤルイン番号(DIN)に設定することで、留守番電話のような働きをします。

ダイヤルイン番号 (DIN) は、着信用の地域番号で、オンライン契約いただける番号です。 
契約した番号に、パラメーターを設定することで、
着信した電話に、.mp3ファイルに準備した音声で応答したり、
テキスト読み上げ機能（TTS）を使ってカスタマイズメッセージで応答したり、
実際に着信を受け取りたい番号へ転送したり、
ボイスメールに伝言を受け取って保存したりできます。


### ボイスメールの設定
まずは、着信を受けるためのダイヤルイン番号（DIN）を契約します。

1. [取得可能な番号を探す](https://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)<br>
   検索すると、取得可能な番号が表示されます。気に入った番号が見つかったら、 `din_uid` を控えておいてください。<br>
   XoxzoのAPIにてご契約可能な、各国のプレフィックスは [料金ページ](https://www.xoxzo.com/ja/about/pricing/voice/#din)よりご確認いただけます。<br>
2. [番号を契約する](https://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)<br>
   控えておいた `din_uid` を使って、ダイヤルイン番号を取得しましょう。 <br>
   「ちょっとお試しで使ってみたいけど、一ヶ月分の料金を払うのは・・・」という場合には、番号契約後24時間以内にその番号を解約してください。料金ページに表示の
   [24時間以内の費用](https://www.xoxzo.com/ja/about/pricing/voice/#din) が適用されます。<br>
   これで、ご自分の電話番号を取得できました。<br>
3. [ダイヤルイン番号にアクションを関連付ける](https://docs.xoxzo.com/ja/din.html#attach-an-action-to-the-dial-in-number-via-api)<br>
   契約した番号に、`action_url` を設定してください。 <br>
   番号へ着信があると、`action_url` にて指定したURLに、`GET` リクエストが送られて、どのように応答するかのコマンドを受け取ります。<br>
4. [アクション URLにボイスメールのアクションコマンドを設定する](https://docs.xoxzo.com/ja/din.html#sample)<br>
    `action_url` から、アクションコマンド _voicemail_ を返してください。<br>
    
これで、契約したダイヤルイン番号で、ボイスメールを受ける準備ができました！

### ボイスメールが着信したら
ボイスメールを受け取るには、アカウントに十分なクレジット残高が必要です。必要な料金は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/voice/#din)よりご確認ください。

1. ボイスメールの着信ごとに、メール通知が届きます。

2. [アカウントページ]()にて、左側メニューより **ボイスメール** を選んでください。

3. 受け取ったボイスメールが、リスト表示されます。新着ボイスメールを再生して確認してください。

4. 再生後、ボイスメールの保管が不要な場合は、リストより削除できます。

5. 削除しない場合、保管は30日ごとの更新となります。保管期限の前に通知のメールが届きますので、次期保管更新が不要の場合は、該当のボイスメールを削除してください。

  
このオプションの料金につきましては、[Xoxzoの音声通話料金ページ](https://www.xoxzo.com/ja/about/pricing/voice)をご参照ください。
