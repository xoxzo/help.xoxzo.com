Title: Kプレミアム・サービスについて
Date: 2015-12-23 13:31
Modified: 2020-05-01
Slug: the-k-premium-service
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API

## Kプレミアムサービスとは？

Kプレミアムサービスとは、日本の国内キャリアのエンドユーザ様に、ショートメッセージを配信するために特化した、オプションのサービスです。キャリア側の制限や、昨今の激化するMNP事情などにより、配信したSMSが届きにくかったり、受信したメッセージに、設定通りのローマ字のSender IDが表示されなかったりすることがありますが、Kプレミアムサービスはキャリア直収のため、配信の確実性が上がり、指定および固定の送信元IDにて送信が可能となります。

**Kプレミアムサービスは、個別契約を頂いている法人向けのサービスです。** ご利用の際、事前登録と審査がございます。また、本サービスの迷惑メール防止と不正利用防止の観点から、登録情報を[KDDI株式会社](http://www.kddi.com/)に開示・共用させていただきます。[ソフトバンク株式会社](https://www.softbank.jp/) および [株式会社NTTドコモ](https://www.nttdocomo.co.jp/)、[楽天モバイル](https://network.mobile.rakuten.co.jp/) へも、健全な配信運用のため、顧客情報をキャリア側に開示することがありますので、ご了承ください。

## Kプレミアムサービスを使った送信

### 指定送信元IDの登録
Kプレミアムサービスのご利用には、ご登録が必要です。ご利用をご希望の送信元IDと企業登記謄本の写しなどが必要となりますので、登録・詳細については [help@xoxzo.com](mailto:help@xoxzo.com) までご連絡ください。


### 送信時の設定

[オプションパラメーター](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)を付けてください。全ての日本国内向け配信に対して、Kプレミアム配信が行われます。（[Kプレミアム送信のクレジット](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)が差し引かれます）

[**Kプレミアム Lite**](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-lite/)をご利用いただくことで、ご指定の送信元IDにて配信ができるAU(KDDI)およびNTTドコモ向けの配信**のみ**をKプレミアムサービスをご利用になり、配信を行うことができます。
システムが送信前に受信者の番号のキャリアを判定し、AU(KDDI)およびNTTドコモ向けの送信はKプレミアムサービスにて、ソフトバンクおよび楽天向けの送信にはKプレミアムサービスを使わずに送信をおこないます。

### AU（KDDI）、NTTドコモ、楽天向け送信

送信リクエスト時に、送信元IDとして *jp_kp_sender* のオプションパラメーターにKプレミアムサービス
ご登録時に指定した数字を設定し、そのまま受信者に表示することになります。
```jp_kp```も```jp_kpl```も、どちらのパラメーターも同様にKプレミアムサービスにて送信を行い、Kプレミアム送信の料金が課されることとなります。

### Softbank向け送信

```jp_kp```をご指定の場合（Kプレミアムの料金となります）</br>
送信元IDは、一律　__21053__　となります。

```jp_kpl```をご指定の場合（[**Kプレミアム Lite**](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-lite/)・通常送信の料金となります）</br>
送信は、```sender```にて設定の送信元IDを使って行われますが、そのまま受信者に届く保証はありません。


### Kプレミアムサービスの料金

Kプレミアムサービスを使った配信の価格は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/sms/#send-sms)をご参照ください。

詳しい使い方は、[ドキュメンテーション](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)をご参照ください。

* Kプレミアムサービスには、他にも [Kプレミアム Lite](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-lite) があります。[違うところを比べてみて](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-service-comparison)ください。
