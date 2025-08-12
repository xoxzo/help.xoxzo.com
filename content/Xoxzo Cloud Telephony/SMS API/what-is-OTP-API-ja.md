Title: SMS絶対認証（OTP API）とは？
Date: 2025-08-12
Slug: what-is-otp-api
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API


## 概要
**SMS絶対認証（OTP API）**は、ワンタイムパスワード（OTP）をSMSで送信し、本人認証を行うための専用APIです。  
アカウント登録やログイン時の二段階認証など、ユーザーの本人確認が必要な場面にご利用いただけます。

XoxzoはSMS業界のパイオニアとして、長年にわたり多くの企業・サービスを支えてきました。  
その実績と技術力を活かし、**たった3つのAPIで本人認証を実装できるシンプルな仕組み**を提供します。  
また、送信料金は**業界最安級（弊社調べ）**と非常に低コストです。最新の料金は[料金ページ](https://www.xoxzo.com/ja/about/pricing/)よりご確認ください。

## ご利用の流れ
1. **ウェブサイトURLの登録**  
   認証で利用するウェブサイトのURLを登録します。

2. **OTPリクエスト**  
   登録済みのウェブサイトと携帯電話番号を指定してリクエストします。  
   Xoxzoから指定された番号へSMSが送信されます。

3. **OTP認証**  
   ユーザーが受け取ったOTPを入力すると、認証結果が返されます。

---

## 関連情報
- [OTP API ドキュメンテーション（日本語）](https://docs.xoxzo.com/ja/otp)
- [SMS API ヘルプページ](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/sms-api/)

---

## 利用例
- 新規会員登録時の本人確認
- ログイン時の二段階認証
- パスワードリセット時の確認



## お問い合わせ
ご不明点がありましたら、**help@xoxzo.com** までお問い合わせください。
