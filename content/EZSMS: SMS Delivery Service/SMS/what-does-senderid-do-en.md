Title: What does "Sender ID" do?
Date: 2018-11-09
Slug: what-does-sender-id-do
Lang: en
Category: EZSMS:SMS delivery service/SMS API

## Sender ID set during SMS sending using the *sender* parameter will be displayed at the recipients device as a message sender.

This can be a business name or corporate phone number/customer service hotline as some device has functionality to click and call to the message sender as well. 

To prevent impersonation or fraud, the Sender ID is generally restricted by many carriers. 

You can still set your desired Sender ID, but this is sent via best-effort delivery and **carriers may not deliver the Sender ID as being set or can replace the Sender ID at any time**.

There are no guarantees to usable Sender IDs, but the list below may give you guidelines when deciding what Sender ID to set when doing your SMS sending:

* Short Sender IDs less than 4 usually are subject to strict restrictions.

* Your Sender ID might not be shown as it is

* Many carriers restrict local numbers for their local network, and local numbers (i.e for Japan it is something like 08011223455 or 03897853334) cannot be set.

**We suggest you do some test sending with your desired Sender ID and check the results to make sure you can show your desired Sender ID to your recipients.**


## キャリアに事前登録を行うことで、登録した送信元IDを置き換えられることなく送信することができます

EZSMSでは、ウェブから送信するSMSサービスのパイオニアとしての経験、知識、技術を駆使した、質の良い海外ルートを使った送信を行っています。

2021年9月に、EZSMSを運営する株式会社Xoxzoが傘下に入った[株式会社アクリート](https://www.accrete-inc.com/)では、国内ルートによる送信を取り扱っています。 
[SMSコネクト](https://www.accrete-inc.com/service/onewaysms/index.html)のウェブ管理画面による送信は、EZSMS同様、直感的に操作してSMSを送信できるため、使いやすい上、 国内キャリアに事前登録を行うことで、送信時に設定する送信元IDが置き換えられることなく、受信者へメッセージを届けることができます。

詳しくは EZSMSヘルプデスク support@ezsms.biz までお気軽にお問い合わせください。
