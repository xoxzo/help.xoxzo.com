Title: ログのウェブダウンロード
Date: 2019-8-20
Slug: web-log-download
Lang: ja
Category: Xoxzo Cloud Telephony Platform/Account


ユーザーの方々は、SMS配信後に、もちろんログの確認を行うものですので、 
Xoxzoでも [**SMSのステータス確認API**](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api) などをご用意しております。

しかし、**SMSの配信状況ステータス確認が、csv形式ファイルでウェブから、とても簡単にダウンロードすることもできます。** 

1. [アカウントへログインする](https://www.xoxzo.com/ja/accounts/login/)
1. 画面右上の _アカウント_ プルダウンより _ご利用ログをダウンロードする_ を選ぶ
1. ご希望の期間を選んで _作成する_ をクリック

以上で、csvファイルのダウンロード準備が出来ます。ファイル内の項目は、

- sender
- url
- msgid
- tags
- sent_time
- recipient
- status
- cost
- apiuser
です。

**ダウンロードできるのは、過去42日分のログデータとなります。**

ご質問は、help@xoxzo.com までお寄せください。

_このウェブダウンロード機能は、弊社運営のウェブベースSMS配信サービスであり、Xoxzo APIプラットフォームの前進である [EZSMS](https://www.ezsms.biz/en/)にて、長年ご愛用いただいておりました。この度、多くのユーザー様からの熱いご要望を受け、それにお応えする形で Xoxzoでもご利用いただけるよう復刻できましたことを、大変嬉しく思っています。_
