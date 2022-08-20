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

### Step 3 Recipients Phone numbers
Input the mobile phone numbers of the recipients.<br>
Please select the country name of the recipient first.<br>
In case you are sending the message to multiple countries, please select the main country. This selection will be used for the auto number correction functionality, which will correct all the wrong format numbers in a list by one click, to judge the recipient numbers are correct. Unfortunately, auto-correction will not be available for the list of recipients including multiple countries. The correction will be still suggested and you can check each of them.<br>
The list can not only be uploaded but also be copy & pasted.<br>
Up to 1,000 recipients can be set for one batch of sending.<br>
Please find the duration necessary to send SMS [here](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/what-is-the-max-number-of-request-and-how-quick-the-process/).<br>

### Step 4 Message body
Please write your message here.<br>
The maximum number of character to be fit in one SMS message is set by the GSM regulation. Although there may be a little difference by the recipient carriers or the devices, in general:<br>
1. The maximum number of character in one message being consisted with ASCII is 160. The longer messages will be split.<br>
2. The maximum number of character in one message with other than ASCII is 70. The longer messages will be split.<br>
3. Please note that EZSMS will accept the message length up to 180 characters. You will be charged for the split sending if you send the maximum length.<br>
<br>
Please see [this article](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/how-many-characters-would-fit-within-1-x-sms/) for more details about the message length restriction.<br>
#### Message customization
If you set variables to customize the message in your csv file uploaded at **Step 2**, your message needs to have the _valiable_ within. The header of the variable column in your csv file will be the name of the _valiable_, please insert the name with {{double wavy brackets}} in your message.<br>
Please see more details about _valiable_ [here]().<br>

### Step 5 Confirm your sending details
Please check and confirm the details of your sending. Any necessary editions can be done here.<br>
#### Use auto-correction tool
![個別修正と一括修正](/images/wizard-01-ja.png)
The gray numbers in the recipient numbers need auto-correction.<br>
The auto-correction will work when you click the individual correction button at each listed number or the auto-correction button at the top.<br>
※The auto-correction will be made based on the country of the recipients you selected at **Step 3**.<br>

#### Manual correction
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
