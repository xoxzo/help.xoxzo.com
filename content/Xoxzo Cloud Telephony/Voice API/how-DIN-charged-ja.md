Title: 着信電話APIへの着信課金方法は？
Date: 2024-04-15
Slug: how-din-charged
Lang: ja
Category:　Xoxzo Cloud Telephony/Voice API

### Xoxzoのダイアルイン番号API
着信した電話をコントロールする、[Xoxzoのダイアルイン番号API](https://www.xoxzo.com/ja/about/voice-api/#din)では、専用の着信番号を取得することによって、その番号で着信した通話に決まった音声ファイルで応答したり、別の番号へ転送したりすることが可能です。

### 着信番号への着信課金
着信用の電話番号は、契約時に初回30日分の料金が課金されます。<br>
着信用の電話番号を契約後は、着信時に指定のURLへwebhook呼び出しが行われます。<br>
（オプションのアクションは、[こちら](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/voice-api/articles/what-does-din-do/)をご参照ください）<br>
Webhookの呼び出した時点で、最低でも1分間分の従量課金が行われます。<br>
料金の詳細は、[こちら](https://www.xoxzo.com/ja/about/pricing/voice/#din)をご参照ください。<br>

### ご注意
番号の契約には、ご本人確認が必要となります。<br>
個別契約のないアカウントでのご契約は、ご連絡を差し上げ、ご本人確認および社内審査が必要となりますが、その結果により解約させていただくことがありますのでご留意ください。<br>
<br>
個別契約のないアカウントでのご利用時には、残高不足の場合、30日自動更新の着信用番号や、着信時のウェブフックの呼び出しができませんので、アカウントの残高にご注意ください。[設定したクレジット残高以下になると通知を行う機能](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/account/articles/top-up-reminder/)もございますので、ご活用ください。<br>



