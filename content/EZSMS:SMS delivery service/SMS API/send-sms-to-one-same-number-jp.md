Title: Is multiple sendings to one same number possible?
Date: 2017-10-27 13:20
Slug: send-mutiple-sms-to-one-number
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

## when we test an API, it can be happening to send multiple SMS to a same phone number. Does this cause any problems?

Yes and No,
Although the detailed specifications varies from carrier to carrier and it is impossible for us to cover them all, carriers have functions to block the continuously flowing messages called 'anti-flooding' to avoid one phone to receive the same messages repeatedly.

Taking above in consideration, to keep testing, you may set different body text or interval of sendings at 1 minutes or longer.

We may follow up any failed sendings when you find.
Please contact us with 
* the number that you send the message to
* the date and time that the messages were sent 
* your email address registered to EZSMS
