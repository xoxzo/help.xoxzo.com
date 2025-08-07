Title: How to set an "Dynamic Action URL"
Date: 2025-08-06
Slug: action-url
Lang: en
Category:　Xoxzo Cloud Telephony/Voice API

# About the Action URL Feature

The **Action URL** feature is an intuitive, browser-based interface that allows you to set and manage actions for your Dial-In Number (DIN). Compared to the current API-only setup, this new method offers greater flexibility and ease of use—no-programming-required.

---

## Overview

Log in to your account and access the Action menu
Configure actions for the following conditions:
  1. During active time
  2. Outside active time
  3. When the caller has a hidden (anonymous) number
Action options include:
  - TTS (Text-to-Speech) playback
  - MP3 file playback
  - Call forwarding
  - Voicemail

---

## How to Set Up

1. **Log in to your account**
   Visit [Sign in page](https://www.xoxzo.com/en/accounts/login/) and sign in.

2. **Access the Action menu**
   From the dashboard, select the menu **Action URL** and click **Add Action** button.

3. **Configure your actions**
   Define up to 3 sets of actions:
     - During active time
     - Outside active time
     - When caller is anonymous
   Up to 2 actions can be set to each set of actions.
      - i.e. Answer the call with "say" then "transfer"
      - Add each action in new line

4. **Set your active time schedule**
   By default, only "outside active time" exists. For holidays like Saturday or Sunday, users don't have to add active hours, as by default, they will be considered inactive hours. 
   Add your business hours or custom time ranges as active times.
     - Example: 9:00–12:00 and 13:00–17:00
     - You can define different active hours for each weekday.
     - You can also specify special dates (e.g., holidays), which will override recurring rules.

5. **Save and get your Action URL**
   Once your actions and schedule are configured, copy the URL.

6. **Attach the Action URL to your DIN**
   Use the API to associate the Action URL with your Dial-In Number.
   See [this documentation](https://docs.xoxzo.com/en/din#attach-an-action-to-the-dial-in-number-via-api) for details.

---

## How It Works

When a call comes in, the system refers to your active schedule and triggers the corresponding action you’ve set.  
You can also visit the Action URL directly from the dashboard to check the current behavior. By default the URL will provide an action for anonymous caller. To check active and inactive hours actions add **caller** query parameter ```<action_url>?caller=<valid_phonenumber>```

📌 *Example call flow image below:*  
![Call Flow Diagram](Insert-your-image-URL-here)

---

## Key Features

- ✅ **Visual interface for configuration directly in your browser**
- ✅ **Up to two actions can be configured** (API-based method allows only one)

---

## Important Notes

- This feature is available only to users who have an active **Dial-In Number (DIN)**.
- To subscribe to a DIN, **identity verification** is required for both corporate and individual accounts.

---

## Need Help?

If you have any questions, feel free to reach out to us:

📧 **help@xoxzo.com**

---

## Related Links

- [Overview of Dial-In Numbers and Actions](https://docs.xoxzo.com/en/din#what-are-actions)
- [How to Attach Actions to DIN via API](https://docs.xoxzo.com/en/din#attach-an-action-to-the-dial-in-number-via-api)
