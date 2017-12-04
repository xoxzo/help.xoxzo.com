Title: The K-Premium service
Date: 2015-12-23 13:31
Modified: 2017-12-4 15:00
Slug: the-k-premium-service
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

## What is the K-Premium Service?

K-Premium is an optional service tailored for JP's mobile operation subscribers. Due to the restrictions on the operators and frequent MNPs, some JP subscribers cannot receive messages from alphanumeric sender ids or the message gets blocked. As the messages sent via K-Premium will be directly passed to the JP carriers, better delivery rates are expected. As the sender ids on the messages are to be surely set, this will increase the user experience for your recipients, as they will know from whom the messages originated.

You will need to be registered in order to use K-Premium, and to prevent abuse of the service your registration details will be shared with [KDDI Corporation](http://www.kddi.com/english/) as well as [Softbank Corporation](https://www.softbank.jp/en/).

Please contact [help@xoxzo.com](mailto:help@xoxzo.com) for more details and registration.


K-Premium allows you to specify specific numeric sender ids which will be shown as it is to the au subscriber upon sending to au (KDDI) subscribers. Sending towards the subscribers on the other JP operators, which is Softbank and Docomo, always a set numeric sender id will be shown. This will increase the user experience for your recipients, as they will know from whom the messages originated. For au(KDDI) subscribers, if the number you specified is callable (i.e your customer support number) they can also call that number by pressing the call back button on their mobile.


## Details of K-Premium Sending

__How to set K-Premium__
Please add K-Premium option parameter, then all the domestic message delivery will be treated as K-Premium. The messages will take the direct route to the recipients and the K-Premium Credit will be consumed.

__AU（KDDI）recipients__
Please set the sender id that you specify at the registration with the option parameter and it will be shown as you specify at the device of the recipients.

__Softbank/Docomo recipients__
Sender id that will be shon at the recipients will be XXXXX no matter what you set.

__Cost for K-Premium__
The cost of K-premium service delivery is 13 credits per message.

[For more details, please see our documentation.](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters)


