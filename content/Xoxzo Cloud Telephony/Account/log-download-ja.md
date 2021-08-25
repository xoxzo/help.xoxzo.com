Title: ログのウェブダウンロード
Date: 2019-8-20
Slug: web-log-download
Lang: ja
Category: Xoxzo Cloud Telephony/Account


APIご利用後のログの確認には、[**SMSのステータス確認API**](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api) をご利用いただけますが、.csv形式ファイルでウェブから、簡単にダウンロードすることもできます。 

まずは、[アカウントへログイン](https://www.xoxzo.com/ja/accounts/login/)して、下記手順 1 - 3 に沿って、ダウンロードを行ってください。

1. 左側メニューより _ご利用ログダウンロード_ を選ぶ
1. ご希望のログの期間とご利用のAPI種を選ぶ
1. _生成する_ をクリック

以上で、csvファイルが生成され、ダウンロード準備が出来ます。
下部に表示されるログファイルのリストからファイル名をクリックしてダウンロードしてください。

**ファイル名の読み方**

SMS配信ログ： outgoing_sms-logs_YYYY-MM-DD（期間始め）_to_YYYY-MM-DD（期間終わり）_ファイルID.csv <br>
音声通話ログ： outgoing_call-logs_YYYY-MM-DD（期間始め）_to_YYYY-MM-DD（期間終わり）_ファイルID.csv <br>
ダイヤル・イン・ナンバーログ： din-logs_YYYY-MM-DD（期間始め）_to_YYYY-MM-DD（期間終わり）_ファイルID.csv <br>

## 　ログファイルで確認できる項目は？

### SMS配信
- sender （送信者）
- url (URL)
- msgid (メッセージID）
- tags　（タグ）
- sent_time （送信日時）
- recipient （受信者）
- status (送信ステータス)
- cost （使用クレジット数）
- apiuser (APIユーザー名)
- link (リンク)
- shortlink (短縮リンク)
- accessed (リンクのクリック)
- accessed_on (リンククリック日時)

### 音声通話
- call_type (通話の種類)
- caller (発信者番号)
- callid (通話ID）
- cost (使用クレジット数)
- direction (通話方向）
- start_time(UTC) （開始日時・協定世界時表記）
- end_time(UTC) （終了日時・協定世界時表記）
- duration(secs) (通話時間)
- recipient (着信番号)
- status　（通話状態）
- tags (タグ)
- url (通話状態URL)
- apiuser (APIユーザー名)

### ダイヤル・イン・ナンバー
- caller (発信者番号)
- cost (使用クレジット数)
- direction (通話時間)
- recipient (着信者番号)
- start_time(UTC) （開始日時・協定世界時表記）
- end_time(UTC)　（終了日時・協定世界時表記）
- duration(secs)　(通話時間)
- status (通話状態)
- apiuser (APIユーザー名)
- uuid (着信通話ID)
- actionurl (アクションURL)

**ご注意**

1. ダウンロードできるのは、過去42日分のログデータとなります。
2. 生成されたファイルの保管期限は、90日間です。
3. 生成ファイルは最大5つまで保管できます。

ご質問は、help@xoxzo.com までお寄せください。

_このウェブダウンロード機能は、弊社運営のウェブベースSMS配信サービスであり、Xoxzo APIプラットフォームの前進である [EZSMS](https://www.ezsms.biz/ja/)にて、長年ご愛用いただいておりました。この度、多くのユーザー様からの熱いご要望を受け、それにお応えする形で Xoxzoでもご利用いただけるよう復刻できましたことを、大変嬉しく思っています。_
