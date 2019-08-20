Title: What does "Sender ID" do?
Date: 2018-11-09
Slug: what-does-sender-id-do
Lang: en
Category: ezsmssms-delivery-service/SMS API

Sender ID set during SMS sending using the *sender* parameter will be displayed at the recipients device as a message sender.

This can be a business name or corporate phone number/customer service hotline as some device has functionality to click and call to the message sender as well. 

To prevent impersonation or fraud, the Sender ID is generally restricted by many carriers. You can still set your desired Sender ID when sending through the API, but this is sent via best-effort delivery and *carriers may not deliver the Sender ID as being set or can change the Sender ID at any time*.

There are no guarantees to usable Sender IDs, but the list below may give you guidelines when deciding what Sender ID to set when doing your SMS sending:

* Short Sender IDs less than 4 usually are subject to strict restrictions.

* Your Sender ID might not be shown as it is

* Many carriers restrict local numbers for their local network, and local numbers (i.e for Japan it is something like 08011223455 or 03897853334) cannot be set.

We suggest you do some test sending with your desired Sender ID and check the results to make sure you can show your desired Sender ID to your recipients.

[K-Premium service](https://www.xoxzo.com/en/about/sms-api/#k-premium) will give you the guarantee that the Sender ID you pre-register will be shown to Japanese AU (KDDI) recipients. Please contact support (help@xoxzo.com) for detailed registration process for K-Premium service.
