Title: How to send SMS via Mail2SMS
Date: 2023-07-05
Slug: how-to-send-via-mail2sms
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

Mail2SMS is the system to send SMS when receiving email messages with a simple initial setting.<br>
<br>
<img src="/images/mailsms/mailsms_en_04.png" alt="system-image" width="400px"><br>
<br>

##Initial Setting
1. Log in to your account and select Mail2SMS Users from the left side menu.<br>
<img src="/images/mailsms/mailsms_en_01.png" alt="process01" width="400px"><br>
2. Click Add Mail2SMS User button at the top right<br> 
<img src="/images/mailsms/mailsms_en_02.png" alt="process02" width="400px"><br>
3. Set each item on the screen and click the Create button<br>
<img src="/images/mailsms/mailsms_en_03.png" alt="process03" width="400px"><br>

<table border="1" cellpadding="3">
<tr>
<td>1</td>
<td>Mail2SMS User Email</td>
<td>The email address that you will send the messages from<br>
</td>
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

**A Tip**
You can test your message before doing the actual sends. to know the judgment, please send your message via email to verdict@acrt-mail.jp using your Mail2SMS email address, the result will be returned to the email.<br>
</br>
This is the end of the initial settings. <br>

The initial setting limits one account to having one Mail2SMS user. Please <a href="mailto:help@xoxzo.com?subject=Request to add Mail2SMS user">contact helpdesk</a> in case you need to create more Mail2SMS users. <br>

Let's send an email to send an SMS now.
</br>

##How to send SMS

Prepare a new email message from the email account set in above

<table border="1" cellpadding="3">
<tr>
<td>Sender</td>
<td>Use the set email address</td>
</tr>
<tr>
<td>Recipient</td>
<td>819012345678@mail2sms.xoxzo.com (See (1) below)</td>
</tr>
<tr>
<td>Subject</td>
<td>Blank or write anything</td>
</tr>
<tr>
<td>Message Body</td>
<td>Message body of the SMS</br>
The character limit for the text is the same as when sending standard SMS. See <a href="https://help.xoxzo.com/en/xoxzo-cloud-telephony/sms-api/articles/how-many-characters-would-fit-within-1-x-sms/">here</a> for more detail. 
</tr>
</table>

(1)</br>
For the recipient's email address, please enter the SMS destination mobile phone number and @mail2sms.xoxzo.com without spaces. When entering the recipient's mobile phone number, please keep the following in mind:</br>

<ul style="list-style-type:circle;">
  <li>Please use half-width + for the first character of the destination phone number.</li>
  <li>For sending within Japan, please continue with the country code 81.</li>
  <li>Destination telephone numbers that can be used for domestic transmissions are those beginning with 070, 080, and 090. When entering the above, omit the first 0 (zero) and enter it after the country code.</li>
  <li>The destination phone number will be 13 digits. Please note that an error will occur if the length is longer or shorter.</li>
</ul>  
Example) If the destination phone number is 080-1234-5678: Enter +818012345678.
<br>
If you register the address-book with the mail sending software you use, you can manage it by the name of the recipient and use it conveniently.

**email mode** <br>
In the case of text mode / HTML mixed mode, the text is sent as SMS text.
In HTML mode, text extraction may result in a different result than intended by the sender. Please be sure to send a test in advance and check the extraction results in the delivered SMS.

**Bulk sending** <br>
If you send a large number of emails to MailSMS in a short period of time, the number of emails will be limited and SMS-sending errors may occur. Please consider TPS when sending emails.
<br>
<br>
Please contact (help@xoxzo.com) for any questions.
<br>
<br>
<br>
<br>
<br>
##Mail Security Standard
Please refer to the tables below to set the mail security standards.</br>
Also, you can test your message before doing the actual sends. to know the judgment, please send your message via email to verdict@acrt-mail.jp using your Mail2SMS email address, the result will be returned to the email.<br>

<br>

<div id="dkim">
<h3>DKIM</h3>
</div>
<br>
DKIM (DomainKeys Identified Mail) is a method that uses electronic signatures to check whether the sender of the email has been spoofed.
By attaching an electronic signature to the email sent by the sender and verifying it when the recipient receives the email, spoofing and falsification of the email can be detected.
<br>
**how to set DKIM security at MailSMS** <br>
Please set one of the following values as the minimum criteria for DKIM judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass DKIM authentication.<br>
GRAY: In addition to PASS, send SMS without DKIM signature.<br>
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.<br>
<br>

<div id="dmarc">
<h3>DMARC</h3>
</div>
DMARC (Domain-based Message Authentication, Reporting and Conformance) is used by the sender to declare the recommended action when the receiver fails to authenticate to DNS as a DMARC policy, and to determine whether the receiver is spoofing when the authentication fails.
<br>
**how to set DMARC security at MailSMS**<br>
Please set one of the following values as the minimum criteria for DMARC judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass DMARC authentication.<br>
GRAY: In addition to PASS, also send SMS messages where at least one SPF or DKIM passed authentication, but the sending domain has no DMARC policy or uses the p=none policy.<br>
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.<br>
<br>


<div id="spf">
<h3>SPF</h3>
</div>
SPF (Sender Policy Framework) is a method to check whether the sender of the mail received using the address is spoofed.
Pre-register her IP address of the server used when sending mail as her SPF record in the sender's DNS. When the recipient receives the email, it checks it against the sender's SPF record to determine if it's spoofed.
<br>

**how to set SPF security at MailSMS**<br>
Please set one of the following values as the minimum criteria for SPF judgment to allow SMS sending.
<br>
PASS: Send SMS only for emails that pass SPF authentication.<br>
GRAY: In addition to PASS, send SMS even if the SPF policy does not exist.<br>
FAIL: In addition to PASS and GRAY, SMS will also be sent for verification failure.<br>
<br>
<br>
<br>

<div id="sample">
<h3>Sample of judgment and settings</h3>
</div>

**Sample of PASS the judgment** <br>
<table border="1" cellpadding="3">
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

**Sample of FAIL the judgement**<br>
<table border="1" cellpadding="3">
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
**SMS will not be sent if even one of the three criteria for sending SMS fails.**
