Title: How to use SMS sending Wizard
Date: 2022-07-14
Slug: how-to-use-wizard
Lang: en
Category: EZSMS:SMS delivery service/SMS API

Sending SMS from Wizard is a step-by-step wizarding function to input the information that you need for a sending.

You can select _From WEB_ or _CSV Upload_ instead of this Wizard to send your messages on EZSMS.

## 6 Steps of the Wizard (some can be skipped）
| | Setting item | Description | Skip | 
| :---------: | ------------------------- | ------------------------------------- | :---------: | 
| Step 1 | SenderID | The recipient will see this as _Sender_ of the message|No| 
| Step 2 | CSV Upload | Upload a file of recipient number & customize data|Yes|
| Step 3 | Recipient Number| Direct input the numbers if you skipped Step 2|No|
| Step 4 | Message | Message & Variables if you use|No|
| Step 5 | Editor|Recipient & Variables are listed for editing/adding/deleting|No| 
| Step 6 | Schedule Sending| Select whether sending the message asap or later |No| 

### Step 1 SenderID
Set the SenderID.
SenderID is shown as _Sender_ of the message in the recipient's device.<br>
To prevent spoofing, the SenderID is often restricted or controlled by the message carriers.<br>
Thus, please note that the carriers may replace the SenderID you set here at the time of sending.<br>
Please refer to [this article](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/what-senderid-can-i-use/)for more restriction details.<br>
Also, [this article](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/what-does-sender-id-do/)may help you to understand SenderIDs better.<br>

### Step 2 CSV Upload
If you want to insert customize data into the mssages, it will be convenient to upload your csv file to send.<br>
If you have a list of recipients' phone number, although no need of customizing the message, you can upload the list in .csv file to auto-feed the numbers, do not forget to set the header of the number as _to_ .<br>
Please visit [here](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/how-to-send-with-customised-csv/) for more about CSV Upload process.<br>

Please just click _Next_ button if you do not have any files to upload.<br>

### Step 3 受信者電話番号
送信先の電話番号を入力します。<br>
まず、送信先の国名を選択してください。複数国へ一度に送信する場合には、主な国名を選択してください。ここで選択した国名は、後ほど確認画面で送信先の電話番号が正しく入力されているかを判断するために使用します。入力フォーマットが間違っている場合、一括修正ボタンで一度に自動修正することができます。複数国へ一度に送信する場合には、一括修正がご利用いただけません。修正が必要な送信先が示されますので、送信先ごとに個別に修正できます。<br>
複数の送信先が載ったリストがある場合、コピー＆ペーストにて貼り付けていただいても結構です。<br>
一度の送信で1,000件までの送信先を登録できます。<br>
送信処理にかかる時間については、[こちら](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/what-is-the-max-number-of-request-and-how-quick-the-process/)から詳細をご確認ください。<br>

### Step 4 メッセージ本文
メッセージを入力します。<br>
GSMの仕様により１通のSMSには最大の文字数が決められています。最終的に受信側のキャリアや受信する機器によって若干の異なるところがありますが、一般的には<br>
1. ASCII の文字のみ含まれているメッセージでは最大 160 文字数までです。これ以上になると、分割されます。<br>
2. 日本語など(半角文字含む)ASCII 以外の文字が含まれる場合、最大 70 文字数までです。これ以上になると分割されます。<br>
3. 一度の送信にて、180文字までのメッセージが設定できますが、そのように送信されますと、分割されて3送信となる（３通分の料金がかかります）、ということをご了承ください。<br>
ASCII の文字のみ含まれているメッセージでは最大 160 文字数までです。これ以上になると、分割されます。<br>
詳しくは、[こちら](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/how-many-characters-would-fit-within-1-x-sms/)をご参照ください。<br>
#### メッセージ本文をカスタマイズする場合
**Step 2** でCSVファイルをアップロードし、送信先ごとにメッセージをカスタマイズした送信を行いたい場合、本文の中に、変更したい部分を _変数_ として入力する必要があります。変数は、CSVファイル内のヘッダーにつけた名前(半角アルファベット)を {{二重波括弧}} で囲うことで入力できます。<br>
変数について、詳しくは[こちら]()をご参照ください。<br>

### Step 5 送信内容を確認・編集
送信先と本文の内容をご確認ください。修正や編集が必要な場合は、ここで行うことができます。<br>
#### 自動修正を行う
![個別修正と一括修正](/images/wizard-01-ja.png)
送信先番号のうち、灰色のものは自動修正が可能です。<br>
上部の「一括自動修正ボタン」または個々の送信先にある「個別自動修正ボタン」をクリックすると自動修正が行われます。<br>
※この際、 **Step 3** で選択した送信先国を基準として自動修正が行われますのでご了承ください。<br>

#### 手動で修正を行う
![手動編集](images/wizard-04-ja.png)
送信先番号が赤色のものは、自動修正が不可となります。各送信先の右側にある「編集」もしくは「削除」ボタンにて手動で修正もしくは削除を行ってください。

#### カスタマイズ部分（変数）の修正を行う
![差し込み編集](images/wizard-03-ja.png)
メッセージ本文に {{name}} と {{time}} という変数を使用している例です。<br>
送信先電話番号やこの変数に差し込む内容を変更したい場合は、編集ボタンをクリックして、変更を加えてください。<br>

#### 送信先を追加する
![新規データ追加](images/wizard-02-ja.png)
- 新たに送信先を追加したい場合は、下部の _追加_ ボタンより送信先を追加してください。<br>

#### 送信先を削除する
送信先を削除する場合は、該当する送信先の右側にある _削除_ ボタンをクリックして削除してください。<br>


### Step 6 送信予約を行う
顧客の誕生日に、お祝いメッセージやクーポンを送信したり、キャンペーンの案内を送信したり、送信日時をある程度決めて送信したい場合、送信予約を行うことができます。<br>
1. 送信予約のスライドボタンをスライドさせる
2. 「送信時刻を設定する」欄をクリック
3. カレンダーや時刻設定画面を使用して送信日時を設定
してください。

送信ボタンをクリックすると、指定した内容がキューに追加されます。
送信が順次行われ、ポイントが消費されていきます。
