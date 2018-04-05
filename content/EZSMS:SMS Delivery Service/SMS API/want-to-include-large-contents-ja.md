Title: 一通のSMSに含めたい情報が多すぎる時は？
Date: 2018-03-23 13:20
Slug: want-to-include-large-contents
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

##新製品の案内や、イベントのお知らせ等、一通のSMSに含めたい情報が多すぎる場合、本文に入り切りません。

日本語70文字で通知できる内容は、限られています。リマインダーなど、既知の事項確認であれば、70文字でも伝達が可能かもしれません。
しかしイベントのお知らせや、新製品のご案内等、多くの内容を通知したい場合、通知内容はウェブページに準備しておき、
SMSではそのURLを（[URL短縮機能](https://goo.gl/)等を使うと便利です）簡単な挨拶文と共に送信するだけで大丈夫です。
その際、KDDI（au）向けの送信には、[Kプレミアムサービス](https://www.ezsms.biz/ja/faq/kddi-premium/)をご利用下さい。

[Xoxzoの音声通話用API](https://www.xoxzo.com/ja/about/voice-api/)を使えば、ユーザーの入力した電話番号へ電話をかけて、
設定しておいた案内内容を音声ファイルを再生して伝えたり、[テキスト読み上げ機能](https://www.xoxzo.com/ja/about/utilities-api/)を使って、
カスタマイズしたメッセージを伝えることも、可能なのです。

さらに、[Xoxzoの音声電話着信API](https://www.xoxzo.com/ja/about/dial-in-api/)を使えば、ユーザー側から電話をかけてもらうことができます。
かかってきた電話は、案内内容を伝達するだけでなく、別の電話番号へと転送することもできます。

[Xoxzoのブログ](https://blog.xoxzo.com/ja/)には、サービスに関するお知らせから、弊社の普段の顔が垣間見える近況報告の他、
[Xoxzo](https://www.xoxzo.com/ja/)や[EZSMS](https://www.ezsms.biz/ja/)を上手に賢く使いこなすための、ヒントがたくさん詰まった
[チュートリアル](https://blog.xoxzo.com/ja/tutorials/)もご参照いただけます。
API初心者には、特に[ミコちゃんシリーズ](https://blog.xoxzo.com/ja/tag/mikochiyan/)が好評です。お気軽にお立ち寄り下さい。
