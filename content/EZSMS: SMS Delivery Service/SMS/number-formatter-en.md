Title: How to use Number Formatter?
Date: 2022-3-11
Slug: how-to-use-number-formatter
Lang: en
Category: EZSMS: SMS delivery service/SMS API

The new phone number formatter, is a tool which automatically corrects mobile phone numbers to the right format for web sending.

The recipient number you enter at "Send from the Web" must be written in a format based on a standard called [E.164](https://help.xoxzo.com/ezsms-sms-delivery-service/articles/E164-format/). However, in Japan, a different format is used usually. <br>
Example) <br>

| Number type | Domestic notation | E.164 notation |
| --------------- | ------------------ | ----------------- |
|Landline | (0111) 000-9999 | +8111110009999 |
| Mobile Phones | 080-0000-9999 | +818000009999 |
|Toll-free number | 0120-000-999 | +81120000999 |

Therefore, EZSMS, which is an online SMS sending service, and sends to domestic telephone networks, has a _phone number formatter_ that can quickly correct numbers that weren't written in the standard way, so that they can be recognized by the system.

## How to use the phone number formatter

To use this tool, log in to your account and select _Send from Web_ from the menu on the left.

### 1. Enter the required information for sending

The following are required:
(1) Sender (2) Recipient (3) Message <br>

These are optional:
(4) Link tracking (5) Scheduled sending <br>

(6) Click "send SMS"


![Send from web](/images/number_formatter_howto_01en.png)

### 2. Start using the phone number formatter
#### Check the number list that you want to use for the formatter tool.
(2) If there are any errors in the recipient's input, the formatter tool will be displayed. <br>
(If all the received recipient numbers entered are correct, you won't see the tool and the messages will be send) <br>
The recipient numbers will be automatically modified to match the E.164 format, which will be displayed. <br>
If the number can't be modified, it will be excluded from this list and displayed.

![Sending Format](/images/number_formatter_howto_02en.png)


#### Check the (Japanese) domestic format by turning on "Domestic display format"

If you click on the "Domestic Display Format" button, the list of recipient numbers will be displayed in the national standard format of Japan. <br>
* If you want to keep a list of correct numbers and/or look at the excluded numbers, you can copy and paste the list, paste it into your own file, and save it.

![Domestic Format](/images/number_formatter_howto_03en.png)

#### View the revised and deleted numbers

If you select "Correction" on the left side of the screen inside the tool, you can see how the originally entered number was converted to the [E.164] () format. Or if it was deleted from the list, you can find out the reason. <br>
If you want to use the corrected content of this tool for the "recipient" at the actual sending screen, click the "format number" button at the bottom right. <br>
If you want to manually modify the format of the recipient number, click "Close without modification" to return to the original sending screen.

![Corrections](/images/number_formatter_howto_04en.png)

### 3. Review the corrections and send

Return to the "Send from Web" screen and double-check that the modified recipient numbers are there. <br>
After reviewing, click the "Send SMS" button at the bottom right of the screen again to send.

![Review](/images/number_formatter_howto_05en.png)

### Exta: When you want to use the tool for a country other than Japan

The phone number formatter executes its corrections based on recipient numbers in Japan.
If the recipient number is not Japanese, you can change it by selecting the country name under the recipient input area. <br>
* If the recipient number includes multiple countries, the phone number formatter unfortunately can't be used. Please manually modify the numbers to the E.164 format or try sending by country.

![Country Selection](/images/number_formatter_howto_06en.png)


