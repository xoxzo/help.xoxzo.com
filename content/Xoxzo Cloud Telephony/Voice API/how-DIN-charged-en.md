Title: How we charge the Voice-Receiving API
Date: 2024-04-15
Slug: how-din-charged
Lang: en
Category:　Xoxzo Cloud Telephony/Voice API

### Dial-In-Numbers API
Dial In Numbers (DIN) are local (Japanese) numbers (DID) to which you can subscribe and receive calls with. <br>
By setting the parameter with any subscription of a DIN, 
you can either answer an incoming call with your specified .mp3 file, 
original message specified with our TTS,  
transfer the call to the other number as you like or
store messages in the Voicemail.

### Charges for Dial-In-Numbers API
The first 30-day number subscription costs will be deducted from your account balance at the time of your subscription. <br>
Every webhook call will charge the account for receiving call charges according to the length of the call. The first one-minute charge will be deducted from the account balance at the webhook call.<br>
(Optional actions can be found [here](https://help.xoxzo.com/en/xoxzo-cloud-telephony/voice-api/articles/what-does-din-do/))<br>
The pricing can be confirmed on the [pricing page](https://www.xoxzo.com/en/about/pricing/voice/#din).<br>

### Notes
Account authentication is required for a DIN subscription. <br>
We will contact you for the authentication in case you don't not have a contract with us, and the DIN subscription may be cancelled in case there is an authentication failure. <br>
<br>
Users without a user contract (prepay user), should make sure of a sufficient account balance to prevent the failure in DIN subscription renewal and webhook call at the call receipt.<br>
[top-up-reminder](https://help.xoxzo.com/xoxzo-cloud-telephony/account/articles/top-up-reminder/) may help you to be alert. 
