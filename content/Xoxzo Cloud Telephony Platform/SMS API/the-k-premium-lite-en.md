Title: The K-Premium Lite service
Date: 2019-07-12
Slug: the-k-premium-lite
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

## What is the K-Premium Lite?

K-Premium Lite is an optional service tailored for JP's mobile operator au(KDDI) subscribers. Due to the restrictions on the operators, the subscribers cannot receive messages with the senderIDs as you set or some messages can get blocked. As the messages sent via K-Premium Lite will be directly passed to au(KDDI) operator, better delivery rates are expected with your pre-registered Sender IDs.

You will need to be registered in order to use K-Premium, and your registration details will be shared with [KDDI Corporation](https://www.kddi.com/english/) to prevent abuse of the service.

For more details and for registration, please contact [help@xoxzo.com](mailto:help@xoxzo.com).

## Sending with K-Premium Lite

__How to set K-Premium Lite__

Please add [Option Parameter](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)
when you make request to send to JP numbers. The system will autoatically look up the operators of your recipient number belongs to
and **only au(KDDI) numbers are applied K-Premium** when being sent. The recipient numbers that belongs to **Docomo and Softbank** will be 
sent as standard sendings.

Please read [**The K-Premium Service**](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)
and follow the instruction in case you would like to use direct connection to all Japanese carriers.

__Setting jp_kpl__

Please set the sender ID that you specify at the registration with the option parameter *jp_kddi_sender* and it will be shown as you specify at the device of the recipients.
Setting ```jp_kpl``` parameter, the request to the au(KDDI) recipients will be sent as **K-premium** and will be charged as **K-premium** sending.


__Sending to Softbank and Docomo recipients__

Request to send to Softbank and Docomo recipients will be treated as **standard** sending.

```sender``` parameter can be set but it is not guarateed to reach the recipients as you set.


__Cost for K-premium Lite__

Please find the cost for K-premium Lite in the [Price Page](https://www.xoxzo.com/en/about/pricing/#sms).

[For more details, please see our documentation](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)

* [K-premium service]({filename}/the-k-premium-service-en.md) is what we originally have. [What's the difference](the-k-premium-comparison-en.md)?
