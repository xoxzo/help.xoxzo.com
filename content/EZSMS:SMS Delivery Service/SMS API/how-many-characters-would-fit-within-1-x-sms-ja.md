Title: SMS1通に含めることのできる最大文字数は？
Date: 2016-09-13 14:23
Slug: how-many-characters-would-fit-within-1-x-sms
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

[GSMの仕様](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9)により１通のSMSには最大の文字数が決められています。最終的に受信側のキャリアや受信する機器によって若干の異なるところがありますが、一般的には

1. ASCII の文字のみ含まれているメッセージでは**最大 160 文字数まで**です。これ以上になると、分割されます。

2. 日本語など(半角文字含む)ASCII 以外の文字が含まれる場合、**最大 70 文字数まで**です。これ以上になると分割されます。

3. 一度のAPIリクエストにて、180文字までのメッセージが設定できますが、そのように送信されますと、**分割されて3送信となる**、ということをご了承ください。