Title: 送信元ID (Sender ID) って何？
Date: 2018-11-09
Slug: what-does-sender-id-do
Lang: ja
Category: EZSMS: SMS delivery service/SMS API

## 送信元ID (Sender ID)は、受信者の端末で、メッセージの送り主として表示されるものとなります。

SMSを配信する際に受信者側で表示される送信元IDは、なりすまし防止の観点から原則としてキャリアにより規制対象になることが多くあります。

通常の送信時、送信元IDを指定はできますが、キャリアによって、別のものに置き換えられる可能性があるということをご承知ください。
置き換えとなった送信元IDは、アカウントページ右上のプルダウンメニューから「ご利用ログ」のダウンロードして確認できる場合もありますが、できない場合もあります。
いずれの場合も、置き換えにより規制を回避し、メッセージが届きやすくなりますので、ご了承ください。

そのため、受信者にメッセージを配信している相手を明確に知ってもらうために、本文の中に配信元の情報を記載することを強くお勧めします。

使用可能な送信元IDの情報は各キャリアによって基準の違いもあり、（内部情報ですので開示されていませんが）以下の注意点が挙げられますのでご確認ください。

なお、以下のリストが常に有効であるとは保証できませんので、ご了承ください。

* 4文字以下の短い配信元IDを設定すると規制される場合があります

* 送信時に設定した送信元IDがそのまま受信者に表示されるという保証はありません

* 多くのキャリアでは、なりすまし防止の観点から、その国内にあるような番号（i.e 日本の場合08011223455または03897853334)に設定することができません

**メッセージの送信前に、使用する予定の配信元IDを実際に指定してテスト送信を行い、配信結果を確認した上でのご使用をお勧めします。**


## キャリアに事前登録を行うことで、登録した送信元IDを置き換えられることなく送信することができます

EZSMSでは、ウェブから送信するSMSサービスのパイオニアとしての経験、知識、技術を駆使した、質の良い海外ルートを使った送信を行っています。

2021年9月に、EZSMSを運営する株式会社Xoxzoが傘下に入った [株式会社アクリート](https://www.accrete-inc.com/)では、国内ルートを取り扱っています。
[SMSコネクト](https://www.accrete-inc.com/service/onewaysms/index.html)のウェブ管理画面による送信は、EZSMS同様、直感的に操作してSMSを送信できるため、使いやすい上、
国内キャリアに事前登録を行うことで、送信時に設定する送信元IDが置き換えられることなく、受信者へメッセージを届けることができます。

詳しくは EZSMSヘルプデスク support@ezsms.biz までお気軽にお問い合わせください。 

