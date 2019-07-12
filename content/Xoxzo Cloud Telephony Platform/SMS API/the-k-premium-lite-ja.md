Title: Kプレミアム Lite について
Date: 2019−7−12
Slug: the-k-premium-lite
Lang: ja
Category: Xoxzo Cloud Telephony Platform/SMS API

## Kプレミアム Lite とは？

Kプレミアム Lite とは、日本の国内キャリア au (KDDI) のエンドユーザ様にショートメッセージを配信するために特化した、オプションのサービスです。キャリア側の制限により配信したSMSが届きにくかったり、受信したメッセージに設定通りのSender IDが表示されなかったりすることがありますが、Kプレミアム Lite は au(KDDI)直収のため、配信の確実性が上がるのに加え、事前登録いただいた送信元IDを使った送信が可能となります。

ご利用開始前に、事前登録と審査がございます。また、本サービスの迷惑メール防止と不正利用防止の観点から、登録情報を[KDDI株式会社](http://www.kddi.com/)に開示・共用させていただきます。

登録・詳細については [help@xoxzo.com](mailto:help@xoxzo.com) までご連絡ください。

## Kプレミアム Lite を使った送信

__送信時の設定__

[オプションパラメーター](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)を付けてください。送信リクエストの中から、システムが自動で選定した、au(KDDI)の携帯電話番号への送信にのみ、Kプレミアム Lite 配信が行われます。au(KDDI)向けの送信には、[Kプレミアム送信のクレジット](https://www.xoxzo.com/ja/about/pricing/#sms)が差し引かれ、その他のキャリア向けの送信には、オプションのない、通常のSMS配信用クレジットが差し引かれます

日本国内全てのキャリア（au(KDDI)、Softbank、Docomo）に直収接続サービスを利用したい場合は、[**Kプレミアムサービス**](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)をご利用ください。

__jp_kddi_sender の設定__

送信リクエスト時に、送信元IDとして *jp_kddi_sender* のオプションパラメーターにKプレミアムサービスのご登録時に指定した数字を設定してください。
そのままau(KDDI)の受信者に、SMSの配信元として表示することになります。
```jp_kpl```のパラメーターと合わせて設定頂くことにより、au(KDDI)の番号への送信にのみ Kプレミアムサービスにて送信を行い、Kプレミアム送信の料金が課されることとなります。

__Softbank および Docomo向け送信__

通常送信の料金となります。

送信は、```sender```にて設定の送信元IDを使って行われますが、そのまま受信者に届く保証はありません。

__Kプレミアム Lite の料金__

Kプレミアム Lite を使った配信の価格は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/#sms)をご参照ください。

[詳しくは、ドキュメンテーションをご参照ください](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)


