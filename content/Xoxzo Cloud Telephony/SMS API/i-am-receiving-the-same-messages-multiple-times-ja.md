Title: 何回も同じメッセージが配信されてしまうのですが。
Date: 2015-11-04 13:17
Slug: i-am-receiving-the-same-messages-multiple-times
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API

![image](/images/multiple-sms-ja.jpg)
まれに、送信側が一度しか送っていないメッセージが、受信側で複数回受信されることがあります。 この現象は、端末側で受信に成功したという通知が、キャリア側に正しく届かず、キャリア側が再送を行ったときに発生します。 再送は、通常５分から１０分程度の間隔で、数回行われます。 このような現象が起きた時は、端末からキャリア側へ送られる信号をリセットするため、端末の電源のオン、オフを間隔をあけながら数回繰り返してみてください。