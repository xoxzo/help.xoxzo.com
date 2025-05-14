Title: How many characters would fit within 1 x SMS?
Date: 2022-03-10 14:23
Slug: how-many-characters-would-fit-within-1-x-sms
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

The [GSM](https://en.wikipedia.org/wiki/Short_Message_Service) standard specifies a maximum character length for each SMS message. These are ultimately determined by the carrier and the receiving mobile, but generally as a guideline

* A message body containing only ASCII characters can have up to 160 characters

* For messages that contain even a single character other than the ASCII character set, such as Japanese kanji, the maximum length is 70 characters.


## Up to 660 characters on Xoxzo SMS APIs
Xoxzo's SMSAPI accepts 660 characters per request (since 2025/04)<br>

<table>
  <tr>
    <th>SMS Part Count</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8</th>
    <th>9</th>
    <th>10</th>
  </tr>
  <tr>
    <td>double byte</td>
    <td>70</td>
    <td>132</td>
    <td>198</td>
    <td>264</td>
    <td>330</td>
    <td>396</td>
    <td>462</td>
    <td>528</td>
    <td>594</td>
    <td>660</td>
  </tr>
  <tr>
    <td>single byte</td>
    <td>140</td>
    <td>264</td>
    <td>396</td>
    <td>528</td>
    <td>660</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>
<br>

* Please note that a request with over-limit text will return **Message too long**.

## Manage your message wise
You have to be careful when you send **message text in English**.
Even if only one non-ASCII character is mixed into the text, the whole message will be regarded as **non-ASCII message** and the 160 ASCII-character limit will now be a NON-ASCII character limit of 70, and your request will get an error.

## How do you check if your message is genuine ASCII?
There are various ways to check, such as [this](https://pteo.paranoiaworks.mobi/diacriticsremover/) to check easily online.

**Do test-sending that will be the best**
Please do test-sending, before you start the bulk message sendings.
