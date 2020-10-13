Title: What is link-tracking?
Date: 2020-10-14
Slug: what-is-link-tracking
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

_track_link_ is an optional parameter for SMS API.

When this optional parameter is provided, the link tracking function is enabled. 
The first URL/domain name in the message will be replaced with our private short-url before being sent.
In the event of that the recipient clicks the link on their device, the date & time of the access to the url will be recorded.

Please use our [Check SMS status API](https://docs.xoxzo.com/en/sms.html#check-sms-status-api) to get this information.

### Send an SMS of _track_link_ enabled

Please provide the optional parameter _track_link_ within the request.

{
    "sender": "Sender",
    "message": "test link tracking https://www.xoxzo.com/en/",
    "recipient": "(recipient phone number)",
    "track_link": "true"
}


When the request is successfully received, a msgid will be returned.

    {
        "msgid": "VncyEuDbojkzRJ2GlKP3USB7C5F6atp1"
    }

### Check the SMS received and click on the url

Please check the recipient device. Click on the link (it should be shortened) in the message.

### Check the status

Via [Check SMS status API](), you will find:<br>
1. whether the link was clicked or not
2. if being clicked, when was it

    {
        "status": "DELIVERED",
        "sender": "(Sender)",
        "url": "https://api.xoxzo.com/sms/messages/(msgid)/",
        "sent_time": "YYYY-MM-DD HH:MM:SS",
        "cost": (cost),
        "msgid": "(an individual message id)",
        "tags": [],
        "recipient": "(recipient phone number)",
        "link_tracking": {
            "link": "https://www.xoxzo.com/en/",
            "shortlink": "https://(shortened private url)",
            "accessed": true,
            "accessed_on": "YYYY-MM-DD HH:MM:SS"
      }
 

