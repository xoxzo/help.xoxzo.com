Title: SMS送信ログは、どうやって見るのでしょう？
Date: 2016-10-12 16:14
Slug: how-to-read-your-log-file
Lang: ja
Category: EZSMS:SMS delivery service/Account

送信したSMSの結果のログをダウンロードすることができます。

ログは以下のようにCSVファイルとしてダウンロードできます。 

![Send log sample]({filename}/images/how-to-read-your-log-file/01.png)

各データの説明は以下のとおりです。(LOCAL TIMEについては下部追記をご参照ください。)

<div class="table-responsive">
  <table border="1" cellpadding="1" cellspacing="1">
    <tbody>
      <tr>
        <td style="text-align: center;">データ</td>
        <td style="text-align: center;">説明</td>
      </tr>
      <tr>
        <td>SEND TIME<br>
        (LOCALTIME)</td>
        <td>EZSMS側でメッセージの送信リクエストを受け付けた時刻。</td>
      </tr>
      <tr>
        <td>LATEST STATUS UPDATED TIME<br>
        (LOCAL TIME)</td>
        <td>SMS送信ステータスを更新した時刻。</td>
      </tr>
      <tr>
        <td>DELIVERY END TIME<br>
        (LOCALTIME)</td>
        <td>送信完了時刻。メッセージが不達の場合でも送信完了といいます。</td>
      </tr>
      <tr>
        <td>MESSAGE ID</td>
        <td>各メッセージに特定するためユニークなID。固有の送信について、問い合わせをいただく際に必要です。</td>
      </tr>
      <tr>
        <td>RECIPIENT</td>
        <td>送信の宛先</td>
      </tr>
      <tr>
        <td>SENDER ID</td>
        <td>送信元として設定されたID</td>
      </tr>
      <tr>
        <td>MESSAGE STATUS</td>
        <td>メッセージの送信状況です。以下のステータスのどれかになります。<br>
        <strong>MESSAGE_DELIVERY_COMPLETE</strong><br>
        正常に配信完了しました。<br>
        <strong>MESSAGE_PASSED_TO_CARRIER_FOR_DELIVERY</strong><br>
        メッセージがキャリアに渡してあります。配信完了までしばらくお待ちください。<br>
        <strong>MESSAGE_EXPIRED</strong><br>
        メッセージはキャリアまで渡っているが、キャリアが決めたリトライ回数に達しても宛先の携帯電話まで着信できなかったため配信できませんでした。<br>
        <strong>MESSAGE_DELIVERY_FAILED</strong><br>
        配信に失敗しました。考えられる理由としてこちらをご覧ください。</td>
      </tr>
      <tr>
        <td>USED_POINTS</td>
        <td>このメッセージの送信が消費したポイント数</td>
      </tr>
    </tbody>
  </table>
</div>

[APIドキュメンテーションはこちらからご参照ください。](https://drive.google.com/file/d/0B-EFLEP7IEAVeUdoN0RqR3gyZjA/view)

(2017.2.6 追記）
※ LOCAL TIME については、アカウントにご登録の「タイムゾーン」での表示となります。

![Screenshot]({filename}/images/how-to-read-your-log-file/02.png)