Title: 許可IPアドレスを登録する
Date: 2016-01-26 15:29
Slug: white-listing-ip-addresses
Lang: ja
Category: Xoxzo Cloud Telephony Platform/Account

お客様のアカウントを不正利用から守るための１つの手段として本サービスのAPIに接続可能なIPアドレスを事前に登録しておくことです。許可アドレスを登録すると、どのAPIユーザでもそのIPからではない接続は拒否されます。

許可IPアドレスを登録する方法は、APIユーザの変更ページから以下のように、1行に1つのIPアドレスを入力し、更新ボタンを押してください。特定の1つのIPアドレスだけではなく、[CIDR形式](https://ja.wikipedia.org/wiki/Classless_Inter-Domain_Routing)でネットワークごとを許可することも可能です。

![IPアドレスを登録する方法]({filename}/images/white-listing-ip-addresses/ja.png)