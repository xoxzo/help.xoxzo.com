Title: SMS送信ログは、どうやって見るのでしょう？
Date: 2016-10-12 16:14
Modified: 2021-02-03
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
        <td>MESSAGE</td>
        <td>設定されたメッセージ</td>
      </tr>
      <tr>
        <td>MESSAGE STATUS</td>
        <td>メッセージの送信状況です。以下のステータスのどれかになります。<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_COMPLETE</strong><br>
        &nbsp;&nbsp;正常に配信完了しました。<br>
        &nbsp;&nbsp;<strong>MESSAGE_PASSED_TO_CARRIER_FOR_DELIVERY</strong><br>
        &nbsp;&nbsp;メッセージはキャリアに渡っています。配信完了までしばらくお待ちください。<br>
        &nbsp;&nbsp;<strong>MESSAGE_EXPIRED</strong><br>
        &nbsp;&nbsp;メッセージはキャリアまで渡っていますが、キャリアが決めたリトライ回数に達しても宛先の携帯電話まで着信できなかったため配信できませんでした。<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_FAILED</strong><br>
        &nbsp;&nbsp;配信に失敗しました。考えられる理由として[こちら](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/what-would-cause-the-sending-failure/)をご覧ください。</td>
      </tr>
      <tr>
        <td>USED_POINTS</td>
        <td>このメッセージの送信が消費したポイント数 参照：[料金ページ](https://www.ezsms.biz/ja/faq/price/)</td>
      </tr>
      <tr>
        <td>SHORTLINK STATUS</td>
        <td>リンクトラッキングを使った送信時に、リンク（URL）がアクセスされたかどうかを示します。<br>
        <strong>0 の場合</strong> リンクはアクセスされていません<br>
        <strong>1 の場合</strong>　リンクはアクセスされています</td>
      </tr>
      <tr>
        <td>SHORTLINK URL</td>
        <td>リンクトラッキングに使われた、ショートURL</td>
      </tr>
    </tbody>
  </table>
</div>

※ LOCAL TIME については、アカウントにご登録の「タイムゾーン」での表示となります。

![Screenshot]({filename}/images/how-to-read-your-log-file/02.png)
