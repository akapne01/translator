### PDF Translator

This projects reads the text content from PDF files, translates it and saves
 translated text as a formatted PDF file. 

Two different translating options can be used:

1) Google translate python library googletrans (can be installed via pip
). To use this option, use script <code> translate_pdfs/translator.py</code>
2) AWS Translate. This option requires you to have AWS account. You need to
 obtain the AWS access key and a secret access key and configure them either
  as environment variables or local files. To use AWS Translate: <code>translate_pds/aws_translator.py</code>
 
Additional python packages that are required to install are: 
* <code>PyPDF2</code>
* <code>reportlab</code>
* <code>boto3</code> (AWS Python SDK)

#### AWS charges:
AWS offer free tier to try out the AWS Translator. Free tier included 2
 million characters for 12 months. Please note that after that the charges
  will occur and AWS will charge $15 per million characters. 
More info: <a href=https://aws.amazon.com/translate/pricing/ target=_blank> Click Here for more info</a>

