Title: How many characters would fit within 1 x SMS?
Date: 2022-03-10 14:23
Slug: how-many-characters-would-fit-within-1-x-sms
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

The [GSM](https://en.wikipedia.org/wiki/Short_Message_Service) standard specifies a maximum character length for each SMS message. These are ultimately determined by the carrier and the receiving mobile, but generally as a guideline

* A message body containing only ASCII characters can have up to 160 characters

* For messages that contain even a single character other than the ASCII character set, such as Japanese kanji, the maximum length is 70 characters.

* Please note that a request with over-limit text will return **Message too long**.


## Manage your message wise
You have to be careful when you send **message text in English**.
Even if only one non-ASCII character is mixed into the text, the whole message will be regarded as **non-ASCII message** and the 160 ASCII-character limit will now be a NON-ASCII character limit of 70, and your request will get an error.

## How do you check if your message is genuine ASCII?
There are various ways to check, such as [this](https://pteo.paranoiaworks.mobi/diacriticsremover/) to check easily online.

**Do test-sending that will be the best**
Please do test-sending, before you start the bulk message sendings.
