Title: The K-Premium service
Date: 2015-12-23 13:31
Modified: 2017-12-04 17:00
Slug: the-k-premium-service
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

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
[Softbank Group Corp](https://www.softbank.jp/en/) and [NTT Docomo, Inc.](https://www.nttdocomo.co.jp/english/)
as the need arises.

Please contact [help@xoxzo.com](mailto:help@xoxzo.com) for more details and registration.

## Details of K-Premium Sending

__How to set K-Premium__

Please add [K-Premium optional parameters](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)
when you make your request to send to a JP number. The messages will be sent using our K-Preimum direct route
and you will be charged the [K-Premium price](https://www.xoxzo.com/en/about/pricing/#sms)
per message sent.

__AU（KDDI）recipients__

Please set the sender ID that you specify at the registration with the option parameter *jp_kddi_sender*
and it will be shown as you specify at the device of the recipients.

__SoftBank recipients__

Sender ID that will be shown at the recipients will be fixed to __22472__.

__DOCOMO recipients__

Sender ID that will be shown at the recipients will fixed to __0344057440__.

__Cost for K-Premium__

The cost of K-premium service delivery can be referred in the [price page](https://www.xoxzo.com/en/about/pricing/#sms).

[For more details, please see our documentation.](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)


