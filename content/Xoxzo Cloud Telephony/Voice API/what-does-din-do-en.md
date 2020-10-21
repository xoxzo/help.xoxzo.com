Title: What does Dial-In-Number (DIN) do?
Date: 2020-10-14
Slug: what-does-din-do
Lang: en
Category:　Xoxzo Cloud Telephony/Voice API

### Dial-In-Numbers API
Dial In Numbers (DIN) are local numbers (DID) which you can subscribe and receive calls with. 
By setting the parameter with any subscription of a DIN, 
you can either answer an incoming call with your specified .mp3 file, 
original message specified with our TTS,  
transfer the call to the other number as you like or
store messages in the Voicemail.

### How to use the Dial-In-Numbers API
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
4. [Make the commands available via the action URL](https://docs.xoxzo.com/en/din.html#sample)<br>
   The command that `action_url` must return can be selected from below.<br>
<div class="table-responsive">
  <table border="1" cellpadding="10" cellspacing="1">
      <tr>
         <td>
         Action
         </td>
         <td>
         Description
         </td>
      </tr>
      <tr>
         <td>
         playback
         </td>
         <td>
         Plays back an mp3 file to the caller
         </td>
      </tr>
      <tr>
         <td>
         transfer
         </td>
         <td>
         Transfers the incoming call to another number
         </td>
      </tr>
      <tr>
         <td>
         say
         </td>
         <td>
         Takes text and reads it out loud (Text-to-Speech)
         </td>
      </tr>      
      <tr>
         <td>
         [voicemail](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/how-to-use-voicemail/)
         </td>
         <td>
         save voicemail recordings in the account
         </td>
      </tr>
   </table>
</div> <br>
5. Now you are ready to receive calls on the DIN and process them!!



### More merit with Dial-In-Numbers API
In addition, with any Japanese number you subscribe, you can use that number even more useful, this is what the [*optional **Local Caller ID**.*](https://www.xoxzo.com/en/about/voice-api/)

**By default, restrictions in Japan does not allow you to use a local number as the caller ID. Our optional local caller ID functionality through our Dial In Numbers allows you to use a local Japan number for your voice calls.**

### Here is how to:
1. [Find your favorite prefix number to subscribe](http://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api)
2. [Subscribe to the number](http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)</br>
Ref: [Dial-In-Numbers API](https://www.xoxzo.com/en/about/pricing/voice/#din)
3. Enjoy [calling](http://docs.xoxzo.com/en/voice.html#simple-playback-api) with notifying your call receivers who is calling by [using the jp optional parameter.](http://docs.xoxzo.com/en/voice.html#jp-specific-optional-parameters)</br>
Ref: [Pricing of Voice API](https://www.xoxzo.com/en/about/pricing/voice/#outbound-call)
