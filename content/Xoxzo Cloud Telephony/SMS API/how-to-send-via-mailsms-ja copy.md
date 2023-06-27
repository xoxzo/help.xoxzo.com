Title: How to send SMS via MailSMS
Date: 2023-07-05
Slug: how-to-send-via-mailsms
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

MailSMS is the system to send SMS when receiving email messages with simple initial settings.

##Initial Settings
1. Log in to your account and select MailSMS Users from the left side menu.
![send_via_mailsms](images/mailsms_en_01.png)
2. Click Add MailSMS User button at the top right 
![send_via_mailsms](images/mailsms_en_02.png)
3. Set each item on the screen and click the Create button
![send_via_mailsms](images/mailsms_en_03.png)

<table>
<tr>
<td>1</td>
<td>MailSMS User Email</td>
<td>The email address that you will send the messages from</td>
</tr>
<tr>
<td>2</td>
<td>Sender</td>
<td>Will be displayed as the sender of the SMS on the recipient’s phone</br><a href="https://help.xoxzo.com/ja/xoxzo-cloud-telephony/sms-api/articles/what-does-sender-id-do-xoxzo/">
What does SenderID do?</a></td>
</tr>
<tr>
<td>3</td>
<td><a href="#dkim">DKIM</a></td>
<td rowspan="3">
Email security is determined before sending against <a href="#dkim">DKIM</a>, <a href="#spf">SPF</a>, and <a href="#dmarc">DMARC</a> standards.
SMS will be sent only when the judgment result exceeds the criteria (PASS/FAIL/GRAY) set here. For details, please refer to the page of each standard.
</br><a href="#sample">Sample of judgment and setting</a></td>
</tr>
<tr>
<td>4</td>
<td><a href="#spf">SPF</a></td>
</tr>
<tr>
<td>5</td>
<td><a href="#dmarc">DMARC</a></td>
</tr>
</table>
</br>
This is the end of the initial settings. Let's send email to send SMS now.
</br>

##How to send SMS

Prepare a new email message from the email account set in above

<table>
<tr>
<td>Sender</td>
<td>Use the set email address</td>
</tr>
<tr>
<td>Recipient</td>
<td>819012345678@mailsms.xoxzo.com (See (1) below)</td>
</tr>
<tr>
<td>Subject</td>
<td>Blank or write anything</td>
</tr>
<tr>
<td>Message Body</td>
<td>Message body of the SMS</br>
The character limit for the text is the same as when sending standard SMS. See <a href="">here</a> for more detail. 
</tr>
</table>

(1)
For the recipient's email address, please enter the SMS destination mobile phone number and @mailsms.xoxzo.com without spaces. When entering the recipient's mobile phone number, please keep the following in mind:
<br>
-Please use half-width + for the first character of the destination phone number.
-For sending within Japan, please continue with the country code 81.
-Destination telephone numbers that can be used for domestic transmissions are those beginning with 070, 080, and 090. When entering the above, omit the first 0 (zero) and enter it after the country code.
-The destination phone number will be 13 digits. Please note that an error will occur if the length is longer or shorter.
<br>
Example) If the destination phone number is 080-1234-5678: Enter +818012345678.
<br>
If you register the phone book with the mail sending software you use, you can manage it by the name of the recipient and use it conveniently.

**email mode**
In the case of text mode / HTML mixed mode, the text is sent as SMS text.
In HTML mode, text extraction may result in a different result than intended by the sender. Please be sure to send a test in advance and check the extraction results in the delivered SMS.

**Bulk sending**
If you send a large number of emails to MailSMS in a short period of time, the number of emails will be limited and SMS-sending errors may occur. Please consider TPS when sending emails.


Please contact (help@xoxzo.com) for any questions.


##メールセキュリティの基準について

<div id="dkim">###DKIM</div>
<br>
DKIM (DomainKeys Identified Mail) is a method that uses electronic signatures to check whether the sender of the email has been spoofed.
By attaching an electronic signature to the email sent by the sender and verifying it when the recipient receives the email, spoofing and falsification of the email can be detected.
<br>
**how to set DKIM security at MailSMS** <br>
Please set one of the following values as the minimum criteria for DKIM judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass DKIM authentication.
GRAY: In addition to PASS, send SMS without DKIM signature.
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.
<br>

<div id="dmarc">###DMARC</div>
<br>
DMARC (Domain-based Message Authentication, Reporting and Conformance) is used by the sender to declare the recommended action when the receiver fails to authenticate to DNS as a DMARC policy, and to determine whether the receiver is spoofing when the authentication fails.
<br>
**how to set DMARC security at MailSMS**<br>
Please set one of the following values as the minimum criteria for DMARC judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass DMARC authentication.
GRAY: In addition to PASS, also send SMS messages where at least one SPF or DKIM passed authentication, but the sending domain has no DMARC policy or uses the p=none policy.
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.
<br>


<div id="spf">###SPF</div>
<br>

SPF (Sender Policy Framework) is a method to check whether the sender of the mail received using the address is spoofed.
Pre-register her IP address of the server used when sending mail as her SPF record in the sender's DNS. When the recipient receives the email, it checks it against the sender's SPF record to determine if it's spoofed.
<br>

**how to set SPF security at MailSMS**<br>
Please set one of the following values as the minimum criteria for SPF judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass SPF authentication.
GRAY: In addition to PASS, send SMS even if the SPF policy does not exist.
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.
<br>




<div id="sample">##Sample of judgment and settings</div>


（この図は、アクリーとのもの。Xoxzoバージョンを作成すること）

###Sample of PASS the judgment
<table>
<tr>
<th>Email Judgment</th>
<th>Result</th>
<th>User setting</th>
<th>SMS judgment</th>
</tr>
<tr>
<td><a href="#dkim">DKIM</a></td>
<td>PASS</td>
<td>PASS</td>
<td>PASS</td>
</tr>
<tr>
<td><a href="#spf">SPF</a></td>
<td>GRAY</td>
<td>PASS</td>
<td>PASS</td>
</tr>
<tr>
<td><a href="#dmarc">DMARC</a></td>
<td>GRAY</td>
<td>GRAY</td>
<td>PASS</td>
</tr>
</table>
</br>

###Sample of FAIL the judgement
<table>
<tr>
<th>Email Judgment</th>
<th>Result</th>
<th>User setting</th>
<th>SMS judgment</th>
</tr>
<tr>
<td><a href="#dkim">DKIM</a></td>
<td>GRAY</td>
<td>PASS</td>
<td>FAIL</td>
</tr>
<tr>
<td><a href="#spf">SPF</a></td>
<td>GRAY</td>
<td>PASS</td>
<td>PASS</td>
</tr>
<tr>
<td><a href="#dmarc">DMARC</a></td>
<td>GRAY</td>
<td>GRAY</td>
<td>PASS</td>
</tr>
</table>
</br>
SMS will not be sent if even one of the three criteria for sending SMS fails.
