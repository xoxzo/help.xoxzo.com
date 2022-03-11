Title: How to use Number Formatter?
Date: 2022-3-11
Slug: how-to-use-number-formatter
Lang: en
Category: EZSMS:SMS delivery service/SMS API

番号自動修正ツールは、携帯電話番号をウェブ送信用のフォーマットに自動で修正するツールです。

The new phone number formatter, is a tool which automatically corrects mobile phone numbers to the right format for web sending.

The recipient number you enter at "Send from the Web" must be written in a format based on a standard called [E.164] (). However, in Japan, a different format is used usually. <br>
Example) <br>

| Number type | Domestic notation | E.164 notation |
| --------- | ------------ | ----------- |
Landline | (0111) 000-9999 | +8111110009999 |
| Mobile Phones | 080-0000-9999 | +818000009999 |
Toll-free number | 0120-000-999 | +81120000999 |

Therefore, EZSMS, which is an online SMS sending service, and sends to domestic telephone networks, has an _phone number formatter_ that can quickly correct numbers that weren't written in the standard way, so that they can be recognized by the system.

## How to use the phone number formatter

To use this tool, log in to your account and select _Send from Web_ from the menu on the left.

### 1. Enter the required information for sending

The following are required:
(1) Sender (2) Recipient (3) Message <br>

These are optional:
(4) Link tracking (5) Scheduled sending <br>

(6) Click "send SMS"


![ウェブから送信画面](/images/number_formatter_howto_01ja.png)

### 2. Start using the phone number formatter
#### Check the number list that you want to use for the formatter tool.
(2) If there are any errors in the recipient's input, the formatter tool will be displayed. <br>
(If all the received recipient numbers entered are correct, you won't see the tool and the messages will be send) <br>
The recipient numbers will be automatically modified to match the E.164 format, which will be displayed. <br>
If the number can't be modified, it will be excluded from this list and displayed.

![送信用フォーマット](/images/number_formatter_howto_02ja.png)

#### 「国内表示フォーマット」をオンにして国内表示を確認
「国内表示フォーマット」のスライドボタンをオンにすると、受信者番号のリストは、国内標準フォーマットで表示されます。<br>
※除外された番号を覗いた、正しい番号のリストをお手元に残したい場合、このリストをコピー＆ペーストしてご自分のファイルに貼り付けて保存することができます。

![国内表示フォーマット](/images/number_formatter_howto_03ja.png)

#### 自動修正の内容、除外番号と除外要因を確認
番号自動修正ツール画面左側の「修正内容」を選択すると、もともと入力された番号がどのように[E.164]()フォーマットへ変換されているか、や、リストから削除されている場合その理由が表示されます。<br>
この自動修正ツールの修正内容を、実際の送信画面の「受信者」に使いたい場合、右下の「番号を自動修正する」ボタンをクリックしてください。<br>
自動修正ツールの修正を反映させずに、ご自分で受信者番号のフォーマットを修正される場合は、「修正せずに閉じる」をクリックして、元の送信画面へ戻ってください。

![修正内容](/images/number_formatter_howto_04ja.png)

### 3. 修正内容を再度確認し、送信する

「ウェブから送信」画面に戻り、修正後の受信者番号が反映されていることを確認してください。<br>
よろしければ、画面右下の「SMSを送信」ボタンを再度クリックし、送信を行ってください。

![ダイヤルSMS利用目的](/images/number_formatter_howto_05ja.png)


### 補足:修正基準国を日本以外にする場合

番号自動修正ツールは、受信者番号がすべて日本国内であるということを前提に修正を行います。<br>
受信者番号が、日本国外の番号である場合、受信者入力エリア下にある国名を選択することで、変更できます。<br>
※受信者番号が、複数の国を含む場合は、自動番号修正ツールをお使いいただけません。手動で E.164フォーマットに修正いただくか、受信者番号を国ごとに分けて送信をお試しください。

![受信者国名選択](/images/number_formatter_howto_06ja.png)


