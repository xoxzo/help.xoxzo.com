Title: Incoming-call notification URL
Date: 2019-02-18 15:00
Slug: incoming-call-notification-url
Lang: en
Category: EZSMS:SMS delivery service/SMS API

##How to use Incoming call URL on DialSMS?

First, please get your DialSMS number ready.

When an incoming call received to the number, the notification below will be sent to the URL you set in real time. 

**Note**

This notification WILL NOT be sent again even recipient side had any errors.

|action type|POST|

|parameter|results|

|expecting response code|200|


Data sample
`Content-Type: application/json 

{

  "caller": "818012345678",  
  
  "recipient": "815012345678",  
  
  "call_time": "1327111224",
  
 }`
 
 
 _caller: Phone number that made the call_
 
 _recipient: DialSMS number you subscribed_
 
 _call_time: Time of the call receipt, in unix standard time format_
   

