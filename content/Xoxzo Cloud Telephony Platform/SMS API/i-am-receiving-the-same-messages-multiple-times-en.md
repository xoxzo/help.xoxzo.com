Title: I'm receiving the same messages multiple times
Date: 2015-11-04 13:17
Slug: i-am-receiving-the-same-messages-multiple-times
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

In certain rare cases, a single message can be sent to the recipient multiple times.

The reason for this happening is that the "received signal" from the mobile did not reach the carrier in a proper manner, causing the carrier to resend the message. This is usually done in a pre-determined interval set by the carrier, like every 5 or 10 minutes.

We usually recommend that the recipient tries turning off and turning back on the affected mobile to reset the signals being sent to the carrier, a few times and with some interval in between.