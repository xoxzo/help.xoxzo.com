Title: What does Carrier Lookup API do?
Date: 2016-11-07 14:47
Slug: what-does-carrier-lookup-api-do
Lang: en
Category: Xoxzo Cloud Telephony Platform/Utilities API

[Carrier Lookup API](https://www.xoxzo.com/en/about/utilities-api/)
This function will enable you to find out which country and carrier a certain mobile number belongs to. The API supports number portability as long as the end carrier supports it.
For more technical details on the utilities and related APIs, check our [API documentation](http://docs.xoxzo.com/en/utilsapi). For pricing information, please go to our [Utilities API pricing page](https://www.xoxzo.com/en/about/pricing/utils).

The response you would get regarding to the availabilities on SMS receipts and the status of the number you searched for is not assured.

There might be the case that some end carriers own multiple phone numbers in a bunch and this would result this search response as unsure of the number status of being really used.

The SMS you send to the number will not be reachable due to various reasons such as their contracts and/or filtering, no matter what status you would receive as the response from this API.

Please keep this in mind that it is more likely happening that the SMS will not reach to the number if the API response shows the unavailability of the number.