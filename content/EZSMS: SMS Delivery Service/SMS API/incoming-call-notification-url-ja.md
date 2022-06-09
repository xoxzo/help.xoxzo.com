Title: 着信通知(CR) URLについて
Date: 2019-02-18 15:00
Slug: incoming-call-notification-url
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

##ダイヤルSMS着信通知（CR）の通知サービス

ダイヤル SMSの着信番号に着信があると、設定した通知 URL に以下の通知がリアルタイムに送られます。

<div class="alert alert-danger">
  <b>**ご注意** </b>
  <br>
  受け取る側にエラーが出てもこの通知は再送されませんので、ご了承ください。
</div>

<table border="1" cellpadding="10" cellspacing="1">
  <tbody>
    <tr>
      <td>アクションタイプ</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>パラメーター名</td>
      <td>results</td>
    </tr>
    <tr>
      <td>期待応答コード</td>
      <td>200</td>
    </tr>
  </tbody>
</table>

### 送信されるデータの例

```
Content-Type: application/x-www-form-urlencoded
{
  "caller": "818012345678",
  "recipient": "815012345678",
  "call_time": "1327111224",
}
```

* caller: 発信した電話番号
* recipient: 着信した電話番号（ダイヤルSMS番号）
* call_time: 着信した時刻、unix標準時間形式
