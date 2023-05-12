Title: The K-Premium service
Date: 2015-12-23 13:31
Modified: 2020-05-01
Slug: the-k-premium-service
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

## What is the K-Premium Service?

K-Premium is an optional service tailored for JP's mobile operator subscribers.
Due to the restrictions on the operators and frequent MNPs, some JP subscribers cannot
receive messages from alphanumeric sender IDs or some messages can get blocked.
As the messages sent via K-Premium will be directly passed to the JP operators,
better delivery rates are expected. Sender IDs for messages through K-Premium
will be set as below.

You will need to be registered in order to use K-Premium, and your registration
details will be shared with [KDDI Corporation](http://www.kddi.com/english/).
To prevent abuse of the service your registration details might also be shared with
[Softbank Group Corp](https://www.softbank.jp/en/), [NTT Docomo, Inc.](https://www.nttdocomo.co.jp/english/)
and [Rakuten Mobile (Japanese only)](https://network.mobile.rakuten.co.jp/)
as the need arises.

Please contact [help@xoxzo.com](mailto:help@xoxzo.com) for more details and registration.

## Details of K-Premium Sending

### How to set K-Premium

Please add [K-Premium optional parameters](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)
when you make your request to send to a JP number. The messages will be sent using our K-Preimum direct route
and you will be charged the [K-Premium price](https://www.xoxzo.com/en/about/pricing/sms/#send-sms)
per message sent.

Please use **K-Premium lite** when you want to apply this K-premium function **ONLY on the KDDI(au) & NTT Docomo numbers**, the system will automatically look up the operators of your recipient number belongs to and **only KDDI(au) & NTT Docomo numbers are applied K-premium** when being sent, the recipient numbers that belongs to **Softbank & Rakuten will be sent as standard sendings**.

### AU（KDDI）, NTT Docomo & Rakuten recipients

Please set the sender ID that you specify at the registration with the option parameter *jp_kp_sender*
and it will be shown as you specify at the device of the recipients.

Both parameter 
```jp_kp``` and ```jp_kpl``` 
will have K-premium cost applied and will act the same.


### SoftBank recipients

with parameter ```jp_kp``` (K-premium cost will be applied) </br>
Sender ID that will be shown at the recipients will be fixed to __21053__.

with parameter ```jp_kpl``` (Standard SMS cost will be applied)</br>
Sender ID can be set as you wish with *sender* parameter but there is no guarantee that the set Sender ID will be delivered as it's set.


### Cost for K-Premium

The cost of K-premium service delivery can be referred in the [price page](https://www.xoxzo.com/en/about/pricing/sms/#send-sms).

[For more details, please see our documentation.](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)

* K-premium service has a sister service called [K-premium Lite](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-lite). [What's the difference](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service-comparison)?
