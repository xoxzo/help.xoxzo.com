Title: How to use Voicemail?
Date: 2020-10-14
Slug: how-to-use-voicemail
Lang: en
Category:　Xoxzo Cloud Telephony/Voice API

### Voicemail and Dial In Number API
Voicemail works as an answering machine, by setting it to a Dial In Number(DIN) you subscribe.

Dial In Numbers (DIN) are local numbers (DID) which you can subscribe and receive calls with. By setting the parameter with any subscription of a DIN, you can either answer an incoming call with your specified .mp3 file, original message specified with our TTS,
transfer the call to the other number as you like or store messages in the Voicemail.


### Setting Voicemail
Please subscribe a Dial In Number to receive calls.
1. [Search for an available number](https://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api)<br>
   The DIN numbers that you can subscribe to will be shown by your search. Please note the `din_uid` of your favorite number for the later use.
   The types of the prefix for each country that are available to subscribe from Xoxzo API can be found in the [price page](https://www.xoxzo.com/en/about/pricing/voice/#din). <br>
2. [Subscribe to a DIN](https://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)<br>
   Use the `din_uid` you noted in No.1, subscribe to a DIN. 
   In case you are just trying this and do not wish to pay the full cost, please unsubscribe this number within the next 24 hours.
   [Discounted 24 hours](https://www.xoxzo.com/en/about/pricing/voice/#din) price will be applied to this subscription.<br>
   Now, you own a phone number.<br>
3. [Attach an action to the DIN](https://docs.xoxzo.com/en/din.html#attach-an-action-to-the-dial-in-number-via-api)<br>
   Please set `action_url` to the DIn you subscribed. <br>
   The url specified for `action_url` will be called via `GET` when there is incoming call to your subscribed DialIN number to get a command that will be used to handle the call.<br>
4. [Attach an action to the Dial In Number via API](https://docs.xoxzo.com/en/din.html#sample)<br>
    `action_url` must return the command _voicemail_.<br>

### When the number is called
With sufficient amount of credit in your account, which can be checked from [the pricing page](https://www.xoxzo.com/en/about/pricing/voice/#din),
the voicemail will be recorded and stored.
1. An email notification will be sent to you at every voicemail arrival.
2. Please select **Voicemail** from the left side menu in [Account page](https://www.xoxzo.com/en/you/profile/).
3. The list of voicemail stored is shown. Please click to play the new voicemail recording.
4. The unwanted record can be deleted after you play.
5. Without deleting the Voicemail records, the storage cost will be applied at every 30 days. 
Please check your inbox for the pre-notice of the next storage cycle reminder.
You may delete the record to avoid the next storage cycle start.

  
Please refer [Pricing page](https://www.xoxzo.com/ja/about/pricing/voice/#din) for the cost of this feature.
