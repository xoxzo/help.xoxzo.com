Title: How to Analyze track_link Results – Easily with Google Sheets
Date: 2025−09−30
Slug: link-tracking-analysis
Lang: en
Category: Xoxzo Cloud Telephony/SMS API

With track_link, you can automatically shorten URLs in your SMS and record click activity.
This guide explains how to use Google Sheets and Apps Script to automatically fetch your SMS results and click data, then visualize them in charts.

1. What You Need

Your Xoxzo API SID and TOKEN

A Google account (to use Google Sheets)

2. Create a Google Spreadsheet

Open a new Google Spreadsheet

Go to [Extensions] → [Apps Script]

Copy & paste the code below

3. The Script (Complete Version)

This script fetches the last 7 days of sent messages and updates or appends them in your sheet without duplication.

<details><summary>Script</summary><div>
/*** Xoxzo → Google Sheets: Import the last 7 days (UTC) without duplicates ***/

const SHEET_NAME = 'Messages';
const MIN_INTERVAL_MIN = 20;      // Prevent too-frequent execution (429 rate limit)
const LOOKBACK_DAYS = 7;          // Always fetch the last 7 days

// 1) Run once to store SID/TOKEN securely
function setupXoxzo() {
  const ui = SpreadsheetApp.getUi();
  const sid = ui.prompt('Xoxzo SID', 'Enter your SID from the dashboard', ui.ButtonSet.OK_CANCEL);
  if (sid.getSelectedButton() !== ui.Button.OK) return;

  const token = ui.prompt('Xoxzo TOKEN', 'Enter your TOKEN from the dashboard', ui.ButtonSet.OK_CANCEL);
  if (token.getSelectedButton() !== ui.Button.OK) return;

  PropertiesService.getScriptProperties().setProperties({
    XOXZO_SID: sid.getResponseText().trim(),
    XOXZO_TOKEN: token.getResponseText().trim()
  }, true);

  ui.alert('Saved. Next, run "fetchSentMessagesNow".');
}

// 2) Run manually: fetch the last 7 days and update/append by msgid
function fetchSentMessagesNow() {
  const props = PropertiesService.getScriptProperties();
  const sid = props.getProperty('XOXZO_SID');
  const token = props.getProperty('XOXZO_TOKEN');
  if (!sid || !token) throw new Error('SID/TOKEN not set. Please run setupXoxzo first.');

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

  SpreadsheetApp.getActive().toast(
    `Import complete: Updated ${updates.length}, Added ${appends.length} (since ${sinceDateStr})`,
    'Xoxzo',
    5
  );
}

// 3) Optional: schedule automatic hourly updates
function installHourlyTrigger() {
  ScriptApp.newTrigger('fetchSentMessagesNow').timeBased().everyHours(1).create();
}

/* Helpers */
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

4. How to Run

Run setupXoxzo once to save your SID/TOKEN securely.

Run fetchSentMessagesNow to fetch the last 7 days of SMS results.

Data including click tracking info will be stored in the Messages sheet.

Use Google Sheets’ chart feature to visualize click-through rates.

5. Next Steps

Create charts: bar chart (clicks by recipient), line chart (daily CTR), pie chart (click/no-click).

Optionally, enable hourly triggers for automatic updates.

👉 With this setup, you can quickly measure the effectiveness of your SMS campaigns with track_link and Google Sheets.