Title: How to send with customised .csv?
Date: 2016-10-12 16:13
Slug: how-to-send-with-customised-csv
Lang: en
Category: EZSMS:SMS delivery service/SMS API

"I want to send the same structured messages with various contents according to the recipient"
"I want to contact my customers thanks for purchase message with the product that the customer has purchased"
With EZSMS, you can upload csv file with the data to insert the various contents to your set message according to the recipient.

Let's see more details with how to use this. 
下記は、ある決まった文章でできたメッセージ中に、部分的に別のデータを差し入れて、カスタマイズされたメッセージを、エクセルなどのスプレッドシートに入った、多数の宛先電話番号向けに送信する場合の、csv ファイルの作り方です。

1. まずは、送信したい基本の文面を作成します。送信先ごとに別のデータになる部分を、変数名をつけ、二重波括弧で囲ってください。

![image csv-01](/images/csv-01.png)
_{{name}}には顧客名を、{{product}}には、その顧客が購入した製品名を差し入れて、顧客の携帯電話へメッセージを送信する場合_

2. 次に、宛先電話番号や差し入れるデータの入ったファイルを作成します。ここでは、エクセルを使っています。1行目に、送信メッセージ中に含まれる変数名（1.で作成したデータ挿入部分）を入力していきます。CSVファイルをアップロードして送信すると、本文中の変数の位置（{{}}ダブル波括弧で囲まれた、カラムのタイトル）にデータが差し込まれます。

* 変数名は必ず必要です。
* 基本の文面内で設定した変数は、すべて変数名および挿入データを作成してください。
* A列には、to と入れて、宛先の電話番号を入力してください。この項目は、必須です。
* テキストのエンコーディングは必ず「UTF-8」に指定してください。 
* 一つのデータ内に２つ以上のアイテムが入り、「,」（カンマ）で区切る場合には全体をダブルクォーテーションで囲ってください。
* 一つのデータ内にスペースが入るときにも、ダブルクォーテーションで囲んでください。
* 送信先の番号は、ダブルクォーテーションで囲まないでください。

![image csv-02](/images/csv-02.png)
![image csv-03](/images/csv-03.png)
3. 項目が入力できたら、入力した列を選んで、フォーマットし、「テキスト」とし .csv 形式で保存します。

4. 送信内容データを、入力したら、ファイルは完成です。
![image csv-04](/images/csv-04.png)

5. EZSMSのログインページより、「CSVでカスタマイズSMS送信」を選び、完成したファイルをアップロードし、送信を行ってください。
![image csv-05](/images/csv-05.png)

__上記で使用した、サンプルCSVファイルは、<a href="/images/ezsms_csvsample.csv" download target="_blank">こちらよりダウンロード</a>いただけます。__
