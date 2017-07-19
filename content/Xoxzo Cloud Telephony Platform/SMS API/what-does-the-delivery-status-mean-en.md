Title: What does the delivery status mean?
Date: 2016-09-14 23:09
Slug: what-does-the-delivery-status-mean
Lang: en
Category: Xoxzo Cloud Telephony Platform/SMS API

There are **4 main types of SMS delivery reports** which you can find. This is an explanation of what they mean:

### FAILED

The message was sent but it did not reach it's recipient, and the carrier has given up trying.

Reasons for failures are many but not limited to 

1. Invalid phone numbers

2. Carrier restrictions or filtering

3. Handset or end user restrictions on filtering

4. Phone numbers which cannot receive SMS (i.e data only terminals)

### DELIVERING

The message was sent but was not delivered and the carrier is still in the process of trying send the message within it's resend policy timeframe. Reasons for this status are many but not limited to:

1. Phone numbers which are not turned on

2. Phone numbers which are out of the service area

3. Invalid phone numbers

4. Phone numbers which cannot receive SMS (i.e data only terminals)

### OK

The message has been delivered

### QUEUED

The message was received by Xoxzo and will be delivered to the carrier shortly.