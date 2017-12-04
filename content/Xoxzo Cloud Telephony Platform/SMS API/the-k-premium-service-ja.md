Title: Kプレミアム・サービスについて
Date: 2015-12-23 13:31
Modified: 2017-12-04 17:00
Slug: the-k-premium-service
Lang: ja
Category: Xoxzo Cloud Telephony Platform/SMS API

## Kプレミアムサービスとは？

Kプレミアムサービスとは、日本の国内キャリアのエンドユーザ様に、ショートメッセージを配信するために特化した、オプションのサービスです。キャリア側の制限や、昨今の激化するMNP事情などにより、配信したSMSが届きにくかったり、受信したメッセージに、設定通りのローマ字のSender IDが表示されなかったりすることがありますが、Kプレミアムサービスはキャリア直収のため、配信の確実性が上がり、ある一定の規律に従った送信元IDにて送信が可能となります。

ご利用の際、事前登録と審査がございます。また、本サービスの迷惑メール防止と不正利用防止の観点から、登録情報を[KDDI株式会社](http://www.kddi.com/)に開示・共用させていただきます。[ソフトバンク株式会社](https://www.softbank.jp/) および [株式会社NTTドコモ](https://www.nttdocomo.co.jp/) へも、健全な配信運用のため、顧客情報をキャリア側に開示することがありますので、ご了承ください。

登録・詳細については [help@xoxzo.com](mailto:help@xoxzo.com) までご連絡ください。

## Kプレミアムサービスを使った送信

__送信時の設定__

[オプションパラメーター](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)を付けてください。全ての日本国内向け配信に対して、Kプレミアム配信が行われます。（[Kプレミアム送信のクレジット](https://www.xoxzo.com/en/about/pricing/#sms)が差し引かれます）

__AU（KDDI）向け送信__

送信リクエスト時に、送信元IDとして *jp_kddi_sender* のオプションパラメーターにKプレミアムサービス
ご登録時に指定した数字を設定し、そのままauの受信者に表示することになります。

__Softbank向け送信__

送信元IDは、一律　__22472__　となります。

__Docomo向け送信__

送信元IDは、一律　__0344057440__　となります。

__Kプレミアムサービスの料金__

Kプレミアムサービスを使った配信の価格は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/)をご参照ください。

[詳しくは、ドキュメンテーションをご参照ください](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)


