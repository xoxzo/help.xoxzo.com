Title: 短いsenderでSMSを送信したら不着でした。なぜでしょう？
Date: 2016-10-12 16:11
Slug: why-the-message-with-short-sender-id-has-been-failed
Lang: ja
Category: EZSMS: SMS delivery service/SMS API

受信側の携帯電話の種類によって、ある種のsenderは受信できない仕様となっている場合があります。 特にCDMA系の携帯電話では、短いSenderIDの不着は、よくみられる現象です。

senderIDをいくつかのパターンで試してみて送信してみてください。
例えば「TEST123」、「TESTMESSAGE」、「1234567890」のような、アルファベットが入ってるsenderや 6桁以上の数字などのsenderを試してみてください。