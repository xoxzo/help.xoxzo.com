Title: Incoming-call notification URL
Date: 2019-02-18 15:00
Slug: incoming-call-notification-url
Lang: en
Category: EZSMS:SMS delivery service/SMS API

##How to use Incoming call URL on DialSMS?

First, please get your DialSMS number ready.

When an incoming call received to the number, the notification below will be sent to the URL you set in real time. 

<div class="alert alert-danger">
  <b>** Note **</b>
  <br>
  This notification WILL NOT be sent again even recipient side had any errors.
</div>

<table border="1" cellpadding="10" cellspacing="1">
  <tbody>
    <tr>
      <td>Action type</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameter</td>
      <td>results</td>
    </tr>
    <tr>
      <td>Expecting response code</td>
      <td>200</td>
    </tr>
  </tbody>
</table>


### Data sample

```
Content-Type: application/json
{
  "caller": "818012345678",
  "recipient": "815012345678",
  "call_time": "1327111224",
}
```

* caller: Phone number that made the call
* recipient: DialSMS number you subscribed
* call_time: Time of the call receipt, in unix standard time format

