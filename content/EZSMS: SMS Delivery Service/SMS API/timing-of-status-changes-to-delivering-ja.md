Title: メッセージのステータスが DELIVERING になるのはいつですか?
Date: 2017-10-30 15:50
Slug: timing-of-status-changes-to-delivering
Lang: ja
Category: EZSMS: SMS delivery service/SMS API

## 受信機が、SMSを受信できる状態ではない時に、EZSMSでは送信したメッセージのステータスが *delivering* となっていました。ステータスはどの時点で *DELIVERING* になるのでしょうか？

メッセージが EZSMS のシステムからキャリアに渡った時点から、キャリアが *SUCCESSFUL* または *FAILED* の結果を通知するまで、メッセージのステータスは *DELIVERING* になります。
