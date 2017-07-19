Title: 返送SMSの配信元IDについて
Date: 2016-10-14 15:35
Slug: what-will-be-displayed-as-senderid-of-the-dialsms-message
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

着信に対して予め設定したメッセージをSMSで発信者に返送しますが、その返送SMSの配信元ID（SMS受信する者からみるとSMSの配信元）の表示基準は受信する側のキャリアによって異なります。

以下に、配信元IDについて説明します。

<table border="1" cellpadding="1" cellspacing="1">
  <tbody>
    <tr>
      <td>受信側キャリア</td>
      <td>配信元ID</td>
      <td>設定可否</td>
      <td>例</td>
    </tr>
    <tr>
      <td>日本Docomo</td>
      <td>英数字・数字のみは不可</td>
      <td>可</td>
      <td>EZSMS123</td>
    </tr>
    <tr>
      <td>日本ソフトバンク</td>
      <td>英数字・数字のみ不可</td>
      <td>可</td>
      <td>EZSMS</td>
    </tr>
    <tr>
      <td>日本EMobile</td>
      <td>英数字・数字のみ不可</td>
      <td>可</td>
      <td>1ABC123</td>
    </tr>
    <tr>
      <td>日本AU</td>
      <td>着信番号と同様、数字のみ</td>
      <td>不可</td>
      <td>050123456789</td>
    </tr>
  </tbody>
</table>

設定可能の配信元IDは着信番号の管理画面から設定できます。取得時にデフォルトの値に、自動的に設定されますが、番号取得後、変更してください。