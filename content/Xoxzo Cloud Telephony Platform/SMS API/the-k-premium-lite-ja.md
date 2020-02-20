Title: Kプレミアム Lite について
Date: 2019-07-12
Modified: 2020-02-20
Slug: the-k-premium-lite
Lang: ja
Category: Xoxzo Cloud Telephony Platform/SMS API

## Kプレミアム Lite とは？

Kプレミアム Lite は、[Kプレミアムサービス](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)の一部です。
Kプレミアムサービスは、日本の国内キャリアのエンドユーザ様にショートメッセージを配信するために特化した、オプションのサービスです。キャリア側の制限により配信したSMSが届きにくかったり、受信したメッセージに設定通りのSender IDが表示されなかったりすることがありますが、Kプレミアムサービスは キャリア直収のため、配信の確実性が上がるのに加え、au(KDDI)と NTTドコモ向けの送信には、事前登録いただいたご指定の送信元IDを、ソフトバンク向けには一定の固定送信元IDを使った送信が可能となります。

**Kプレミアム Lite**は、Kプレミアムサービスでは固定の送信元IDとなるソフトバンク向けの送信を通常配信に、指定の送信元IDをご利用頂ける au(KDDI)とNTT
ドコモへの配信をKプレミアムを使った直収サービスにて行うことのできるサービスです。Kプレミアムサービスにご登録であれば、パラメーターの変更だけでご利用いただけます。登録の送信元IDは、一度の登録でKプレミアムサービスにも、Kプレミアム Liteにもご利用いただけます。

**Kプレミアムサービス および Kプレミアム Liteは、法人向けのサービスです。** ご利用の際、事前登録と審査がございます。また、本サービスの迷惑メール防止と不正利用防止の観点から、登録情報を[KDDI株式会社](http://www.kddi.com/)に開示・共用させていただきます。[ソフトバンク株式会社](https://www.softbank.jp/) および [株式会社NTTドコモ](https://www.nttdocomo.co.jp/) へも、健全な配信運用のため、顧客情報をキャリア側に開示することがありますので、ご了承ください。

登録・詳細については [help@xoxzo.com](mailto:help@xoxzo.com) までご連絡ください。

## Kプレミアム Lite を使った送信

### 送信時の設定

[オプションパラメーター](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)を付けてください。送信リクエストの中から、システムが自動で選定した、au(KDDI)およびNTTドコモの携帯電話番号への送信にのみ、Kプレミアム Lite 配信が行われます。[Kプレミアム送信のクレジット](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)が差し引かれます。ソフトバンク向けの送信には、通常のSMS配信用クレジットが差し引かれ、通常送信が行われます。

日本国内全てのキャリア（au(KDDI)、Softbank、Docomo）に直収接続サービスを利用したい場合は、[**Kプレミアムサービス**](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)をご利用ください。

### jp_kddi_sender の設定

送信リクエスト時に、送信元IDとして *jp_kddi_sender* のオプションパラメーターにKプレミアムサービスのご登録時に指定した数字を設定してください。
そのままau(KDDI)およびNTTドコモの受信者に、SMSの配信元として表示することになります。
```jp_kpl```のパラメーターと合わせて設定頂くことにより、au(KDDI)およびNTTドコモの番号への送信にのみ Kプレミアムサービスにて送信を行い、[Kプレミアム送信のクレジット](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)が課されることとなります。

### Softbank向け送信

[通常送信の料金](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)となります。

送信は、```sender```にて設定の送信元IDを使って行われますが、そのまま受信者に届く保証はありません。事前にテスト送信を行っていただきご確認いただくことをおすすめいたします。

### Kプレミアム Lite の料金

Kプレミアム Lite を使った配信の価格は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)をご参照ください。

[詳しくは、ドキュメンテーションをご参照ください](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)

* Kプレミアムサービスは、もともと [Kプレミアムサービス](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/the-k-premium-service) として生まれました。[違うところを比べてみて](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/the-k-premium-service-comparison)ください。
