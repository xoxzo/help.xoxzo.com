Title: How to send with customised .csv?
Date: 2016-10-12 16:13
Slug: how-to-send-with-customised-csv
Lang: en
Category: EZSMS:SMS delivery service/SMS API

"I want to send the same structured messages with various contents according to the recipient"
"I want to contact my customers thanks for purchase message with the product that the customer has purchased"
With EZSMS, you can upload csv file with the data to insert the various contents to your set message according to the recipient.

*the maximum sending per upload is limited to 1,000*

Let's see more details with how to create a csv file in case you would like to send customised SMS to the phone number lists in spreadsheet like MS excel, by inserting some various data to a set message text. 

1. Please create a message text. Name `variables` with **double curly brackets** `{{ text }}` and put it where you want to change by recipient.

![image csv-01](/images/csv-01e.jpg)
_in the case of inserting customers' name in {{name}}, purchased goods in {{product}}, to send this message to the customers' mobile numbers_

2. Now creating the data file that contains the recipients' mobile phone numbers, names and products. This example shows you to prepare the file in excel. Please type the name of the `variables` on the first row. These name of `variables` are set in instruction number 1. (above). The data in this file will be inserted where you put `variables` in double curly brackets `{{ text }}` to be sent to the phones.

* The name of `Variable` are mandatory.
* Please create all `variable` and `data` that you set in the message text.
* **The first column of the first row has to be `to` and the data of recipients phone numbers.**
* Please set the text encoding to `UTF-8` 
* In case you insert 2 or more data in one cell and want to separate them with comma (,), please wrap the whole data in the cell with double quotation `"text,text"`
* Please also wrap the whole data in the cell with double quotation `"text text"` when you have any space within the cell data.
* Please do not wrap the recipient number data with double quotation.

![image csv-02](/images/csv-02.png)

3. Please select the columnns that you put the items on the first row and format them as `Text` data. 
![image csv-03](/images/csv-03.png)

4. Insert your data, then save the file as .csv
![image csv-04](/images/csv-04.png)

5. Go to `[Send CSV SMS](https://www.ezsms.biz/en/member/sendsms-csv/)` page to upload the csv file and proceed to the sending.
![image csv-05](/images/csv-05.png)

__The sample csv file used in above can be downloaded <a href="/images/ezsms_csvsample.csv" download target="_blank">here</a>__
