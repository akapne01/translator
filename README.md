### PDF Translator

This projects reads the text content from PDF files, translates it and saves
 translated text as a formatted PDF file. 

Two different translating options can be used:

1) Google translate python library googletrans (can be installed via pip
). To use this option, use script <code>python translator.py</code>
2) AWS Translate. This option requires you to have AWS account. You need to
 obtain the AWS access key and a secret access key and configure them either
  as environment variables or local files. To use AWS Translate: <code>python aws_translator.py</code>
 
Additional python packages that are required to install are: 
* <code>PyPDF2</code>
* <code>reportlab</code>
* <code>boto3</code> (AWS Python SDK)

#### AWS charges:
AWS offer free tier to try out the AWS Translator. Free tier included 2
 million characters for 12 months. Please note that after that the charges
  will occur and AWS will charge $15 per million characters. 
More info: <a href=https://aws.amazon.com/translate/pricing/ target=_blank> Click Here for more info</a>

#### If you get googletrans error, here is how to fix it:
Please note that there was a breaking change for googletrans. If you get error: <code>error in result (AttributeError: 'NoneType' object has no attribute 'group')</code>
Then to fix you need to do 2 things: 
1) Change URL to URL_COM = 'translate.googleapis.com'
2) Install the latest version of Google Translate: pip install googletrans==3.1.0a0
It fixed the issue. More information about the issue: 
https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group#52456197

#### How you can translate your own file? 
1) Change language to which you would like to translate to:
LANG = "lv" (ln: 19 in translator.py & ln: 13 in aws_translator.py)
2) Change the file name from <code>file_name = "example.pdf"</code>. Raplace example.pdf to match the pdf file name you have.
(ln: 61 in translator.py & ln: 59 in aws_translator.py)