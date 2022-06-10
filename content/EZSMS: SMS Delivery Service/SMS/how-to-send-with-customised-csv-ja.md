Title: CSVファイルでSMSの本文をカスタマイズする方法
Date: 2022-05-25
Slug: how-to-send-with-customised-csv
Lang: ja
Category: EZSMS:SMS delivery service/SMS

EZSMSでは、SMSの本文をカスタマイズできます。
リストをアップロードして、受信者それぞれに「**ある部分**だけ入れ替えた**同じ文章**」のSMSを送信することができるのです。

![csv_screen](/images/csv_screen01.png)

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

<details><summary>書き方の例/地域ごとの避難指示の場合</summary>
  変数名 local に地域の名前
  変数名　shelter に避難所の名称を入れて送信したい場合
  ```
警戒レベル４発令
  {{local}}地区の方は{{shelter}}へ避難してください
  ```
</details>

### ④ csvファイルの準備・アップロード
#### 作成
**【テキストファイルとして作成する場合】**
テキスト編集用のソフトで、各項目をコンマで区切って入力してください。
  ![csv_screen](/images/csv_screen05.png)
 
**【MSエクセルなどの表計算ソフトで作成する場合】**
③で{{二重波括弧}} で囲った変数名を一行目に、二行目以降に該当データを入力してください。
<details>
  <summary>ファイル入力の例/セミナー参加へのお礼</summary>
  ![csv_screen](/images/csv_screen02.png)
 </details>
 
 <details>
  <summary>ファイル入力の例/地域ごとの避難指示の場合</summary>
  ![csv_screen](/images/csv_screen03.png)
 </details>
 
**ファイル保存時に、必ず _ファイル形式_ を _CSV UTF-8 (コンマ区切り)(.csv)_ として保存してください。**
  ![csv_screen](/images/csv_screen04.png)
 
#### アップロード
  ![csv_screen](/images/csv_screen06.png)
- CSVファイルをドラッグ＆ドロップ
- _Browse_ ボタンをクリックしてファイルの場所を指定 
枠内に、ファイル名が表示されていることを確認してください。

### ⑤ 送信のタイミング設定
送信は、_今すぐ送信_ と _送信予約_ を選択できます。<br>
_今すぐ送信_ する場合は、右下の **SMSを送信** ボタンをクリックしてください。<br>
_送信予約_ をする場合は、下記のように _予約する_　のオプションを選択し、送信日時を指定してから、右下の **SMSを送信** ボタンをクリックしてください。<br>
① _予約する_ を選択する <br>
② 送信日を指定する <br>
③ 送信時間を指定する <br>
![csv_screen](/images/csv_screen06.png)

:::note warn
SMS送信は、ベストエフォート・ベースで配信開始され、順次配信が行われます。 **予約されたメッセージが必ずしも、予約した時刻にすべて配信開始・完了する保障のないことを、ご承知ください。**
SMS配信の予約前に、**アカウントのポイント残高が、すでに予約済みメッセージを含めた全ての送信に十分であるかどうかも、ご確認ください。**
:::
