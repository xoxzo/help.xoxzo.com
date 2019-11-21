Title: Kプレミアムのメッセージの、最大の長さ教えてください
Date: 2016-10-13 15:17
Slug: what-is-the-standard-length-of-the-message-for-k-premium
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

Kプレミアムの仕様により、１つのメッセージは他のAPIと違って最長shift_jisの140バイトの本文が、送信可能です。 それ以上の長さの本文が送信されると、自動的に複数のメッセージに分割され、各メッセージに対して課金されます。 

メッセージを送信される前に、一度shift_jisにエンコードしてバイト数を確認することをお勧めします。