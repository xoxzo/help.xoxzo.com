Title: track_link 分析方法
Date: 2025−09−30
Slug: link-tracking-analysis
Lang: ja
Category: Xoxzo Cloud Telephony/SMS API

track_link 分析方法 – Googleスプレッドシートで簡単に！

track_link を使うと、SMS本文に含まれるURLのクリック状況を取得できます。
ここでは、GoogleスプレッドシートとApps Script を使って、送信結果とクリックデータを自動取得・可視化する方法を紹介します。

1. 準備するもの

Xoxzo API の SID と TOKEN

Google アカウント（Google スプレッドシート利用）

2. スプレッドシートを作成

新しいGoogleスプレッドシートを開く

メニューの [拡張機能] → [Apps Script] を選択

下記のコードをコピー＆ペースト

3. スクリプト（完成版）

以下のスクリプトを貼り付けて保存してください。
このスクリプトは 直近7日分の送信結果を取得し、重複なくシートに保存 します。


<details><summary>スクリプト</summary><div>
/*** Xoxzo → Google Sheets：毎回“直近7日分(UTC)”を重複なしで取り込み ***/

const SHEET_NAME = 'Messages';
const MIN_INTERVAL_MIN = 20;      // 429対策
const LOOKBACK_DAYS = 7;          // 直近7日分を取得

// 1) 初回：SID/TOKENを保存
function setupXoxzo() {
  const ui = SpreadsheetApp.getUi();
  const sid = ui.prompt('Xoxzo SID', 'ダッシュボードの SID を入力', ui.ButtonSet.OK_CANCEL);
  if (sid.getSelectedButton() !== ui.Button.OK) return;

  const token = ui.prompt('Xoxzo TOKEN', 'ダッシュボードの TOKEN を入力', ui.ButtonSet.OK_CANCEL);
  if (token.getSelectedButton() !== ui.Button.OK) return;

  PropertiesService.getScriptProperties().setProperties({
    XOXZO_SID: sid.getResponseText().trim(),
    XOXZO_TOKEN: token.getResponseText().trim()
  }, true);

  ui.alert('保存しました。「fetchSentMessagesNow」を実行してください。');
}

// 2) 単発実行：直近7日分を取得
function fetchSentMessagesNow() {
  const props = PropertiesService.getScriptProperties();
  const sid = props.getProperty('XOXZO_SID');
  const token = props.getProperty('XOXZO_TOKEN');
  if (!sid || !token) throw new Error('SID/TOKENが未設定です。まず setupXoxzo を実行してください。');

  const nowUtc = new Date();
  const sinceDateStr = Utilities.formatDate(
    new Date(nowUtc.getTime() - (LOOKBACK_DAYS - 1) * 24*60*60*1000),
    'UTC', 'yyyy-MM-dd'
  );

  const url = 'https://api.xoxzo.com/sms/messages/?sent_date%3E=' + sinceDateStr;

  const options = {
    method: 'get',
    headers: { Authorization: 'Basic ' + Utilities.base64Encode(sid + ':' + token) },
    muteHttpExceptions: true
  };

  const resp = UrlFetchApp.fetch(url, options);
  const code = resp.getResponseCode();
  if (code !== 200) throw new Error(`HTTP ${code}: ${resp.getContentText()}`);

  const items = JSON.parse(resp.getContentText());
  const sheet = getOrCreateSheet_(SHEET_NAME);
  ensureHeader_(sheet);

  const idx = buildIndexByMsgid_(sheet);
  const updates = [], appends = [];

  items.forEach(it => {
    const lt = it.link_tracking || {};
    const row = [
      it.msgid, it.recipient, it.sender, it.status, it.parts, it.cost,
      it.sent_time, lt.accessed === true, lt.accessed_on,
      lt.link, lt.shortlink, Array.isArray(it.tags) ? it.tags.join(',') : ''
    ];
    const rowNum = idx[it.msgid];
    if (rowNum) {
      updates.push({ rowNum, row });
    } else {
      appends.push(row);
    }
  });

  updates.forEach(u => sheet.getRange(u.rowNum, 1, 1, u.row.length).setValues([u.row]));
  if (appends.length) sheet.getRange(sheet.getLastRow()+1, 1, appends.length, appends[0].length).setValues(appends);

  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, 12);

  SpreadsheetApp.getActive().toast(`更新 ${updates.length} 件、追加 ${appends.length} 件（対象日: >= ${sinceDateStr}）`, 'Xoxzo', 5);
}

// 3) 自動実行（毎時）
function installHourlyTrigger() {
  ScriptApp.newTrigger('fetchSentMessagesNow').timeBased().everyHours(1).create();
}

/* ヘルパー */
function getOrCreateSheet_(name) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheetByName(name) || ss.insertSheet(name);
}

function ensureHeader_(sheet) {
  const header = ['msgid','recipient','sender','status','parts','cost','sent_time',
                  'lt_accessed','lt_accessed_on','lt_original_link','lt_shortlink','tags'];
  const rng = sheet.getRange(1, 1, 1, header.length);
  const vals = rng.getValues()[0];
  if (vals[0] !== 'msgid') {
    sheet.clear();
    rng.setValues([header]);
  }
}

function buildIndexByMsgid_(sheet) {
  const lastRow = sheet.getLastRow();
  const map = {};
  if (lastRow >= 2) {
    const ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
    ids.forEach((r, i) => {
      const id = (r[0] || '').toString();
      if (id) map[id] = i + 2;
    });
  }
  return map;
}
</div></details>

4. 実行手順

setupXoxzo を実行して SID/TOKEN を保存

fetchSentMessagesNow を実行して直近7日分を取得

シートに送信結果＋リンククリック情報が保存されます

グラフ機能を使えばクリック率などを可視化できます

5. 次のステップ

グラフの例（棒グラフ・折れ線グラフ）を紹介

必要に応じて毎時自動更新トリガーを追加