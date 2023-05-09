Title: How many characters would fit within 1 x SMS?
Date: 2022-03-10 14:23
Slug: how-many-characters-would-fit-within-1-x-sms
Lang: en
Category: EZSMS: SMS delivery service/SMS API

The [GSM](https://en.wikipedia.org/wiki/Short_Message_Service) standard specifies a maximum character length for each SMS message. These are ultimately determined by the carrier and the receiving mobile, but generally as a guideline

* A message body containing only ASCII characters can have up to 160 characters

* For the messages that contains even a single character other than the ASCII character set, such as Japanese kanji, the maximum length is 70 characters.

* 1 send request can set the message with up to 180 characters, but please note that will **split the message into 3 messages**.


## Manage your message body wise to save on cost of SMS Sendings
It is not economical to send overlimit sized messages, while it is also important to consider the message contents to be attractive and easy to understand for the recipients.

MS word can [show the word count](https://support.office.com/en-us/article/show-the-word-count-and-more-3c9e6a11-a04d-43b4-977c-563a0e0d5da3) and you can check the text length before you send it.
Of course [EZSMS](https://www.ezsms.biz/ja/) has **send from the web** feature and it will count the character you input as well. ![send_from_web](images/send_from_web-en.png)

But you have to be careful when you send **message text in English**.
Even if only one non-ASCII character is mixed into the text, the whole message will be regarded as **non-ASCII message** and the 160 ASCII-character limit will now be NON-ASCII character limit of 70, and your one sending will be splitted into 3.

## How do you check if your message is genuine ASCII?
There are various ways to check, such as [this](https://pteo.paranoiaworks.mobi/diacriticsremover/) to check easily online.

**Do test-sending that will be the best**
Please do test-sending, before you start the bulk message sendings.
