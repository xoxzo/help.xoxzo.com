Title: The K-Premium Lite service
Date: 2019−7−12
Slug: the-k-premium-lite
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

## What is the K-Premium Lite?

K-Premium Lite is an optional service tailored for JP's mobile operator au(KDDI) subscribers. Due to the restrictions on the operators, the subscribers cannot receive messages with the senderIDs as you set or some messages can get blocked. As the messages sent via K-Premium Lite will be directly passed to au(KDDI) operator, better delivery rates are expected with your pre-registered Sender IDs.

You will need to be registered in order to use K-Premium, and your registration details will be shared with [KDDI Corporation](https://www.kddi.com/english/) to prevent abuse of the service.

For more details and for registration, please contact [help@xoxzo.com](mailto:help@xoxzo.com).

## Sending with K-Premium Lite

__How to set K-Premium Lite__

Please add [Option Parameter](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)
when you make request to send to JP numbers. The system will autoatically look up the operators of your recipient number belongs to
and **only au(KDDI) numbers are applied K-Premium** when being sent. The recipient numbers that belongs to **Docomo and Softbank** will be 
sent as standard sendings.

Please read [**The K-Premium Service**](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)
and follow the instruction in case you would like to use direct connection to all Japanese carriers.

__Setting jp__

送信リクエスト時に、送信元IDとして *jp_kddi_sender* のオプションパラメーターにKプレミアムサービスのご登録時に指定した数字を設定してください。
そのままau(KDDI)の受信者に、SMSの配信元として表示することになります。
```jp_kpl```のパラメーターと合わせて設定頂くことにより、au(KDDI)の番号への送信にのみ Kプレミアムサービスにて送信を行い、Kプレミアム送信の料金が課されることとなります。

__Softbank および Docomo向け送信__

通常送信の料金となります。

送信は、```sender```にて設定の送信元IDを使って行われますが、そのまま受信者に届く保証はありません。

__Kプレミアム Lite の料金__

Kプレミアム Lite を使った配信の価格は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/#sms)をご参照ください。

[詳しくは、ドキュメンテーションをご参照ください](http://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)


