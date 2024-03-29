Title: どのようなSenderIDを使用できますか？
Date: 2022-07-14
Slug: what-senderid-can-i-use
Lang: ja
Category: EZSMS: SMS delivery service/SMS

SMSを配信する際に受信者側に表示される、配信元番号（または配信元IDといいます）は、なりすまし防止の観点から原則としてキャリアにより規制対象になるケースが多くあります。EZSMSのご利用にあたって、**配信する際に配信元IDを指定できます** が、**受信者がメッセージを受け取る時には送信キャリアにより、別のものに置き換えられてある可能性がある** ということを、ご承知ください。<br>

そのため、受信者にメッセージの配信元を明確に知ってもらうために、メッセージ本文の中に配信元の情報を記載することを強くお勧めします。（送り主の社名、氏名をメッセージ内で名乗る）<br>
> こんにちは、◯◯クリニックです<br>
> xxクラブより緊急ミーティングのお知らせです
など
<br>
使用可能な配信元IDの情報は、各キャリアによって基準の違いもあり、内部機密情報のため開示されていませんが、以下の注意すべき点を挙げられます。<br>
なお、以下のリストが常時有効であるとも、保証できませんので、ご了承ください。

* 最大文字数は英数字の場合 10 です

* 4文字以下の短い配信元IDを設定すると規制される場合があります

* 送信時の設定がそのまま表示されるかどうかは、保証できません

* 国内送信の場合、日本で実在しそうな番号（i.e 08011223455または03897853334)を設定することはできません

***
複数、もしくは大量のメッセージを送る前に、使用する予定の配信元IDを、実際に指定して配信結果を確認した上でのご使用をお勧めします。<br>
また、キャリアの規定には、変更・アップデートがつきものです。定期的に送信を行う場合にも、時々試験送信を行い確認したり、送信の際、ご自分の携帯電話にも併せてメッセージを送信して、送信者の表示や、メッセージ内容の表示を確認することをお勧めいたします。
***
