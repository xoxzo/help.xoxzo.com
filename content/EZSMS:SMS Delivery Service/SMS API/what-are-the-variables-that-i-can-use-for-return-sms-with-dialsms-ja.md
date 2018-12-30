Title: 返送SMSに利用可能な変数は？
Date: 2016-10-14 14:06
Slug: what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms
Lang: ja
Category: EZSMS:SMS delivery service/SMS API

返送ショートメッセージに変数を設定することが可能です。

変数を返送メッセージに入れると、実際の配信時に展開され、データが代入されます。受信側の動きをURLでトラッキングなどしたりできるため、ぜひご利用ください。

以下に、設定可能の変数を説明します。

<table align="center" border="1" cellpadding="1" cellspacing="1">
  <tbody>
    <tr>
      <td>変数</td>
      <td>説明</td>
      <td>実際の長さ</td>
      <td>設定したメッセージ</td>
      <td>実際のメッセージ</td>
    </tr>
    <tr>
      <td><strong>{{ mn }}</strong> </td>
      <td>発信元番号</td>
      <td>12</td>
      <td>クーポンはこちらです http://bit.ly/abc?num=<strong>{{ mn }}</strong> </td>
      <td>クーポンはこちらです http://bit.ly/abc?num=819012345678</td>
    </tr>
  </tbody>
</table>
