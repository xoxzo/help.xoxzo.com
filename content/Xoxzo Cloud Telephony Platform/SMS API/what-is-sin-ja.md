Title: SMSイン番号(SIN) って？
Date: 2019-12-28
Slug: what-is-sin
Lang: ja
Category: Xoxzo Cloud Telephony Platform/SMS API

## SMS受信API (SIN）とは？
SMS受信API（SIN = SMS-IN-Number)では、APIを使って電話番号を契約することにより、
SMS受信のための携帯電話・スマホ・その他のデバイスがなくてもインターネット上でSMSの受信が可能になります。


## SMS受信API (SIN）を使うメリットは？
+ SMSの送信者の電話番号を自動でリストに追加したい
+ SMSの送信者に自動で決まった返信を送信できるようにしたい
+ 複数の電話番号に届くSMSを一括して管理したい
+ 届いたSMSの内容に応じて、受信したメッセージを自動で振り分けたい

など、SMS受信APIを使ってできることは、無限大です。

Xoxzoの[SMSウェブAPI](https://www.xoxzo.com/ja/about/sms-api/)には、SMS受信だけでなく送信用のAPIもご利用いただけます。
上手に組み合わせて、あなたのウェブシステムやアプリがより便利に、より安全なものとなるようご活用ください。


## SMS受信API (SIN）の使い方は？
[ドキュメンテーション](https://docs.xoxzo.com/ja/sms.html#receive-sms-messages-api)
および[ヘルプページ](https://help.xoxzo.com/xoxzo-cloud-telephony-platform/)をご参照ください。

概要としては、

1. 受信用の番号を契約する

2. 契約した番号へWebhookを関連付ける

これで、受信の準備は完了です。

SMSを受信すると、Webhookへメッセージの送信者、受信した契約中の番号、メッセージの内容と受信時刻が送られます。
