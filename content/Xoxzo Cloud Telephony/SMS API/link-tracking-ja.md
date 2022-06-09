Title: リンクトラッキングって？
Date: 2020-10-14
Slug: what-is-link-tracking
Modified: 2020-12-02
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API

オプションパラメーターの、_track_link_ は、SMS APIで使用されます。

- このオプションパラメーターが使われると、リンクトラッキング機能が作動します。<br>
- SMSのメッセージ本文中、最初に出てくる URLやドメイン名を自動で、独自の短縮URLに変換してリクエストを出します。 ※URLの前後は、最低1つの ASCII空白文字(0x20)を入れてください。<br>
- 受信者が受信したメッセージ中のリンクをクリックすると、その日時が記録されます。<br>
- リンクトラッキングのコールバックURLを _lt_callbackurl_ パラメータで指定している場合、指定されたURLをPOSTメソッドで呼び出します。<br>
- [SMSの配信状態を確認するAPI](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api) を使って、クリックの記録情報を確認できます。<br>

### _track_link_ を使って、SMSを送信する

オプションパラメータ _track_link_ をリクエストに含めて、送信を行ってください。

```
{
    "sender": "(送信者)",
    "message": "test link tracking https://www.xoxzo.com/en/",
    "recipient": "(受信者の電話番号)",
    "track_link": "true"
}
```

リクエストが問題なく受け付けられると、メッセージID(msgid)が返されます。

    {
        "msgid": "（メッセージID）"
    }


### SMSの受信を確認し、メッセージ中のURLをクリック

受信したデバイスを確認してください。メッセージ中にある、置き換えられたURLをクリックしてください。 

### _lt_callbackurl_ で指定のURLを呼び出す
- リンクトラッキング用ショートリンクがクリックされたとき、XOXZOクラウドシステムが _lt_callbackurl_ で指定されたURLを呼び出します。<br>
- XOXZOクラウドシステムはこのURLをPOSTメソッドで呼び出します。<br>
- コールバックURLは http のステータス 200 で応答する必要があります。この応答をうけとるまで、最大１０回まで呼び出しを繰り返します。<br>
- このURLは、ショートリンクが最初にクリックされたとき１回のみ呼び出されます。<br>

### ステータスをAPIで確認

[SMSの配信状態を確認するAPI](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api)を使います。<br>
次の情報が返されます。<br>
1. リンクがクリックされたか否か
2. クリックされていれば、その日時<br>


    {
        "status": "DELIVERED",
        "sender": "(送信者)",
        "url": "https://api.xoxzo.com/sms/messages/(msgid)/",
        "sent_time": "YYYY-MM-DD HH:MM:SS",
        "cost": (料金),
        "msgid": "(個別のメッセージID)",
        "tags": [],
        "recipient": "(受信者の電話番号)",
        "link_tracking": {
            "link": "https://www.xoxzo.com/en/",
            "shortlink": "https://(独自の短縮URL)",
            "accessed": true,
            "accessed_on": "YYYY-MM-DD HH:MM:SS"
        }

**独自の短縮URLは、送信後90日にて無効となりますので、ご注意ください**

詳しくは、[ドキュメンテーション](https://docs.xoxzo.com/ja/sms.html#send-sms-messages-api)を参照してください。
