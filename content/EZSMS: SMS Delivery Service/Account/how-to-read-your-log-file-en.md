Title: How to read your log file?
Date: 2016-10-12 16:14
Modified: 2021-02-03
Slug: how-to-read-your-log-file
Lang: en
Category: EZSMS:SMS delivery service/Account

The log file is downloadable from the account page in a .csv format.

![Send log sample]({filename}/images/how-to-read-your-log-file/01.png)

Please refer to the table below for what each data shows. 
The relation of LOCAL TIME and set Time-zone is explained below the table.

<div class="table-responsive">
  <table border="1" cellpadding="1" cellspacing="1">
    <tbody>
      <tr>
        <td style="text-align: center;">Data</td>
        <td style="text-align: center;">Description</td>
      </tr>
      <tr>
        <td>SEND TIME<br>
        (LOCALTIME)</td>
        <td>The time stamp of when EZSMS system accepted the request</td>
      </tr>
      <tr>
        <td>LATEST STATUS UPDATED TIME<br>
        (LOCAL TIME)</td>
        <td>The time stamp of status is updated</td>
      </tr>
      <tr>
        <td>DELIVERY END TIME<br>
        (LOCALTIME)</td>
        <td>The time stamp of completion, even the delivery is failed.</td>
      </tr>
      <tr>
        <td>MESSAGE ID</td>
        <td>A unique ID for each message. This is to be referred when you inquire about the message status to us.</td>
      </tr>
      <tr>
        <td>RECIPIENT</td>
        <td>The mobile number that the message was forwarded to</td>
      </tr>
      <tr>
        <td>SENDER ID</td>
        <td>The ID that is set as to be a Sender of the message</td>
      </tr>
      <tr>
        <td>MESSAGE</td>
        <td>The bodytext</td>
      </tr>
      <tr>
        <td>MESSAGE STATUS</td>
        <td>The message sending status. One of below should be found.<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_COMPLETE</strong><br>
        &nbsp;&nbsp;The message has been sent successfully<br>
        &nbsp;&nbsp;<strong>MESSAGE_PASSED_TO_CARRIER_FOR_DELIVERY</strong><br>
        &nbsp;&nbsp;The message was passed to the carrier, please wait for the delivery completion<br>
        &nbsp;&nbsp;<strong>MESSAGE_EXPIRED</strong><br>
        &nbsp;&nbsp;The delivery was failed due to the number of retry was more than what the carrier set<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_FAILED</strong><br>
        &nbsp;&nbsp;The delivery was failed, please refer [here](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/what-would-cause-the-sending-failure/) for the conceivable causes</td>
      </tr>
      <tr>
        <td>USED_POINTS</td>
        <td>The number of the point that this message consumed:[Pricing Page](https://www.ezsms.biz/en/faq/price/)</td>
      </tr>
      <tr>
        <td>SHORTLINK STATUS</td>
        <td>This shows whether the link is accessed or not, when the message is sent with Link-tracking option<br>
        &nbsp;&nbsp;<strong>0 means</strong> The link hasn NOT been accessed<br>
        &nbsp;&nbsp;<strong>1 means</strong>　The link has been accessed</td>
      </tr>
      <tr>
        <td>SHORTLINK URL</td>
        <td>The shortened URL used for the link-tracking</td>
      </tr>
    </tbody>
  </table>
</div>

※ Please note that **LOCAL TIME** shows the date & time of the time zone that your account is set.

![Screenshot]({filename}/images/how-to-read-your-log-file/02e.png)
