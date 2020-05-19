Title: The K-Premium Lite service
Date: 2019-07-12
modified: 2020-05-01
Slug: the-k-premium-lite
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

## What is the K-Premium Lite?

K-Premium Lite is an optional service tailored for JP's mobile operator subscribers. Due to the restrictions on the operators, the subscribers cannot receive messages with the senderIDs as you set or some messages can get blocked. As the messages sent via K-Premium Lite will be directly passed to au(KDDI) & NTT Docomo and better delivery rates are expected with your pre-registered Sender IDs.

You will need to be registered in order to use K-Premium(and K-Premium Lite), and your registration details will be shared with [KDDI Corporation](https://www.kddi.com/english/), [NTT Docomo](https://www.nttdocomo.co.jp/english/) to prevent abuse of the service.

For more details and for registration, please contact [help@xoxzo.com](mailto:help@xoxzo.com).

## Sending with K-Premium Lite

### How to set K-Premium Lite

Please add [Option Parameter](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)
when you make request to send to JP numbers. The system will autoatically look up the operators of your recipient number belongs to
and **only au(KDDI), NTT Docomo and Rakuten numbers are applied K-Premium** when being sent. The recipient numbers that belongs to **Softbank & Rakuten** will be 
sent as standard sendings.

Please read [**The K-Premium Service**](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/)
and follow the instruction in case you would like to use direct connection to all Japanese carriers.

### Setting jp_kpl

Please set the sender ID that you specify at the registration with the option parameter *jp_kp_sender* and it will be shown as you specify at the device of the recipients.
Setting ```jp_kpl``` parameter, the request to the au(KDDI) & NTT Docomo recipients will be sent as **K-premium** and will be charged as **K-premium** sending.


### Sending to Softbank recipients

Request to send to Softbank and Docomo recipients will be treated as **standard** sending.

```sender``` parameter can be set but it is not guarateed to reach the recipients as you set.


### Cost for K-premium Lite

Please find the cost for K-premium Lite in the [Price Page](https://www.xoxzo.com/en/about/pricing/sms/#send-sms).

[For more details, please see our documentation](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)

* [K-premium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service) is what we originally have. [What's the difference](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service-comparison)?
