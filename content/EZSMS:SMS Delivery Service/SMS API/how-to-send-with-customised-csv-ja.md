Title: CSVファイルでSMSの本文をカスタマイズする方法
Date: 2022-05-25
Slug: how-to-send-with-customised-csv
Lang: ja
Category: EZSMS:SMS delivery service/SMS

EZSMSでは、SMSの本文をカスタマイズできます。
リストをアップロードして、受信者それぞれに「ある部分」だけ入れ替えた「同じ文章」のSMSを送信することができるのです。

![csv_screen](/images/csv_screen.png)

### ① メニューエリアから _CSVアップロード_ を選択
### ② _送信者_ を入力 
送信者について詳細は[こちら](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/what-does-sender-id-do/)から
### ③ メッセージを入力　
カスタマイズ部分（受信者によって入れ替えを行いたい部分）は、変数名をつけて{{二重波括弧}} で囲ってください。
<details><summary>書き方の例/セミナー参加へのお礼</summary>
  変数名 name に受信者の名前
  変数名　seminar にセミナータイトルを入れて送信したい場合
  ```
{{name}}様　  先日は{{seminar}}へご参加いただきありがとうございました。
  ```
</details>
