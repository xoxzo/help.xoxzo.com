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

<img src="/images/longsms-en.png" alt="longsms" width="600px"><br>
<br>
Please refer to the table below for the details how your messages will be split while being sent and charged.
</br>
<table border="1" cellspacing="1" cellpadding="7" style="text-align:center" style="border-collapse:collapse">
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

* Please note that a request with over-limit text will return **Message too long**.

## SMS Message Counter
<p>If your message is ready, enter it below to pre-check how many SMS will be sent:</p>
<textarea id="smsInput" rows="4" cols="50" placeholder="Type your message here..." oninput="calculateSMS()" width="600"></textarea>

<p id="smsResult" style="font-weight:bold; margin-top:10px;"></p>

<script>
  function calculateSMS() {
    const input = document.getElementById('smsInput').value;
    const result = document.getElementById('smsResult');

    const isASCII = /^[\x00-\x7F]*$/.test(input); // Check if it's only ASCII
    const length = input.length;

    if (length === 0) {
      result.innerText = '';
      return;
    }

    if (isASCII) {
      if (length <= 140) result.innerText = `Detected ${length} ASCII characters. This will be sent as 1 SMS.`;
      else if (length <= 264) result.innerText = `Detected ${length} ASCII characters. This will be sent as 2 SMS.`;
      else if (length <= 396) result.innerText = `Detected ${length} ASCII characters. This will be sent as 3 SMS.`;
      else if (length <= 528) result.innerText = `Detected ${length} ASCII characters. This will be sent as 4 SMS.`;
      else if (length <= 660) result.innerText = `Detected ${length} ASCII characters. This will be sent as 5 SMS.`;
      else result.innerText = `The message exceeds the SMS character limit (maximum 660 ASCII characters).`;
    } else {
      if (length <= 70) result.innerText = `Detected ${length} Japanese (multi-byte) characters. This will be sent as 1 SMS.`;
      else if (length <= 132) result.innerText = `Detected ${length} Japanese characters. This will be sent as 2 SMS.`;
      else if (length <= 198) result.innerText = `Detected ${length} Japanese characters. This will be sent as 3 SMS.`;
      else if (length <= 264) result.innerText = `Detected ${length} Japanese characters. This will be sent as 4 SMS.`;
      else if (length <= 330) result.innerText = `Detected ${length} Japanese characters. This will be sent as 5 SMS.`;
      else if (length <= 396) result.innerText = `Detected ${length} Japanese characters. This will be sent as 6 SMS.`;
      else if (length <= 462) result.innerText = `Detected ${length} Japanese characters. This will be sent as 7 SMS.`;
      else if (length <= 528) result.innerText = `Detected ${length} Japanese characters. This will be sent as 8 SMS.`;
      else if (length <= 594) result.innerText = `Detected ${length} Japanese characters. This will be sent as 9 SMS.`;
      else if (length <= 660) result.innerText = `Detected ${length} Japanese characters. This will be sent as 10 SMS.`;
      else result.innerText = `The message exceeds the SMS character limit (maximum 660 Japanese characters).`;
    }
  }
</script>


## Manage your message wise
You have to be careful when you send **message text in English**.
Even if only one non-ASCII character is mixed into the text, the whole message will be regarded as **non-ASCII message** and the 160 ASCII-character limit will now be a NON-ASCII character limit of 70, and your request will get an error.

## How do you check if your message is genuine ASCII?
There are various ways to check, such as [this](https://pteo.paranoiaworks.mobi/diacriticsremover/) to check easily online.

**Do test-sending that will be the best**
Please do test-sending, before you start the bulk message sendings.
