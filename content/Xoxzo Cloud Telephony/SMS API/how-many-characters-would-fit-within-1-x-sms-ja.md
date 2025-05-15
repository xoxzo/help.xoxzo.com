Title: SMS1通に含めることのできる最大文字数は？
Date: 2025-05-13
Slug: how-many-characters-would-fit-within-1-x-sms
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API


[GSMの仕様](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9)により１通のSMSには最大の文字数が決められています。最終的に受信側のキャリアや受信する機器によって若干の異なるところがありますが、一般的には

1. ASCII の文字のみ含まれているメッセージでは**最大 160 文字数まで**です。

2. 日本語など(半角文字含む)ASCII 以外の文字が含まれる場合、**最大 70 文字数まで**です。

## Xoxzoでは、一度のリクエストにて660文字まで対応
XoxzoのSMS送信APIでは、一度に660文字までのメッセージが送信できます（2025年4月より）。<br>

<img src="/images/longsms-ja.png" alt="longsms" width="600px"><br>
<br>
XoxzoのSMS送信APIによる長文SMSの分割送信、課金についての詳細は、下記をご参照ください。
</br>

<table border="1" cellspacing="1" cellpadding="7" style="text-align:center" style="border-collapse:collapse">
  <tr>
    <th>SMSの通数</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8</th>
    <th>9</th>
    <th>10</th>
  </tr>
  <tr>
    <td>日本語メッセージ</td>
    <td>70</td>
    <td>132</td>
    <td>198</td>
    <td>264</td>
    <td>330</td>
    <td>396</td>
    <td>462</td>
    <td>528</td>
    <td>594</td>
    <td>660</td>
  </tr>
  <tr>
    <td>ASCII文字<br>（シングルバイト）</td>
    <td>140</td>
    <td>264</td>
    <td>396</td>
    <td>528</td>
    <td>660</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>
これ以上の長さのテキストを送信されますと、 **Message too long**、というエラーが返されますことをご了承ください。

## <h2 id="sms-checker">SMS通数チェッカー</h2>

送信したいメッセージが準備できている場合、下にメッセージを入力してください。<br>
SMS何通分になるかを、簡易自動計算します。参考までに、お使いください。
<textarea id="smsInput" rows="4" cols="50" placeholder="ここにメッセージを入力..." oninput="calculateSMS()" style="width:600px;"></textarea>

<p id="smsResult" style="font-weight:bold; margin-top:10px;"></p>

<script>
  function calculateSMS() {
    const input = document.getElementById('smsInput').value;
    const result = document.getElementById('smsResult');

    const isASCII = /^[\x00-\x7F]*$/.test(input); // ASCIIだけかを判定
    const length = input.length;

    if (length === 0) {
      result.innerText = '';
      return;
    }

    if (isASCII) {
      if (length <= 140) result.innerText = `ASCIIの文字数 ${length} 文字を検出しました。SMSは 1 通で送信されます。`;
      else if (length <= 264) result.innerText = `ASCIIの文字数 ${length} 文字を検出しました。SMSは 2 通で送信されます。`;
      else if (length <= 396) result.innerText = `ASCIIの文字数 ${length} 文字を検出しました。SMSは 3 通で送信されます。`;
      else if (length <= 528) result.innerText = `ASCIIの文字数 ${length} 文字を検出しました。SMSは 4 通で送信されます。`;
      else if (length <= 660) result.innerText = `ASCIIの文字数 ${length} 文字を検出しました。SMSは 5 通で送信されます。`;
      else result.innerText = `SMSの文字数上限を超えています（ASCIIは最大660文字まで）`;
    } else {
      if (length <= 70) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 1 通で送信されます。）`;
      else if (length <= 132) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 2 通で送信されます。`;
      else if (length <= 198) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 3 通で送信されます。`;
      else if (length <= 264) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 4 通で送信されます。）`;
      else if (length <= 330) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 5 通で送信されます。`;
      else if (length <= 396) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 6 通で送信されます。`;
      else if (length <= 462) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 7 通で送信されます。`;
      else if (length <= 528) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 8 通で送信されます。`;
      else if (length <= 594) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 9 通で送信されます。`;
      else if (length <= 660) result.innerText = `日本語の文字数 ${length} 文字を検出しました。SMSは 10 通で送信されます。`;
      else result.innerText = `SMSの文字数上限を超えています（日本語は最大660文字まで）`;
    }
  }
</script>


送信内容を理解しやすく、しかも魅力的に作るのも大切なことですが、実際の送信には、文字数分の送信料金がかかってしまいます。本文の文字数を管理して、SMS送信料金を節約し、ベストパフォーマンスを得られるSMS送信を心がけましょう。
