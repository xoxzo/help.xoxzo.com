Title: What are the variables that I can use for return SMS with DialSMS?
Date: 2016-10-14 14:06
Slug: what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms
Lang: en
Category: EZSMS:SMS delivery service/SMS API

Variable can be inserted in the message body.

By setting this variable in the message, it will be developed when being sent, the data will be assigned for the valiable. Please use this to track the recipient's action via URL.

Below is the details of this valiable.

<table align="center" border="1" cellpadding="1" cellspacing="1">
  <tbody>
    <tr>
      <td>Variable</td>
      <td>Content</td>
      <td>Actual length</td>
      <td>Sample message</td>
      <td>Developed message</td>
    </tr>
    <tr>
      <td><strong>{{ mn }}</strong> </td>
      <td>SenderID</td>
      <td>12</td>
      <td>Get your discount ticket here: http://bit.ly/abc?num=<strong>{{ mn }}</strong> </td>
      <td>Get your discount ticket here: http://bit.ly/abc?num=819012345678</td>
    </tr>
  </tbody>
</table>
