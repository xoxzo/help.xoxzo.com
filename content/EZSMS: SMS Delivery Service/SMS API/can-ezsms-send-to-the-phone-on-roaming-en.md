Title: Can I verify a number via the Lookup API?
Date: 2016-09-14 14:37
Slug: can-i-verify-a-number-via-the-lookup-api
Lang: en
Category: EZSMS: SMS delivery service/SMS API

The Lookup API identifies which carrier a certain number belongs too. It does not guarantee that the number can and will receive SMS messages.

As carriers sometimes return results based on blocks of numbers which it owns instead of individual numbers, it also does not guarantee that the number is valid or is currently being used.

Even if the API returns a positive result for a certain number, because of contractual or filtering issues you still might not be able to send messages to that number.

At the same time, if your lookup result is negative, there is a very high probability that trying to send to that number will result in failure.