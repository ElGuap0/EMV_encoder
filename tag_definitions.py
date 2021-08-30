emv_dict = {

# --------------------------------------------------

'TVR':['Offline data processing was not performed',
'SDA failed',
'ICC data missing',
'Card number appears on hotlist',
'DDA failed',
'CDA failed',
'RFU (Now SDA was selected)',
'RFU',

'Card and terminal have different application versions',
'Expired application',
'Application not yet effective',
'Requested service not allowed for card product',
'New card',
'RFU',
'RFU',
'RFU',

'Cardholder verification was not successful',
'Unrecognised CVM',
'PIN try limit exceeded',
'PIN entry required, but no PIN pad present or not working',
'PIN entry required, PIN pad present, but PIN was not entered',
'On-line PIN entered',
'RFU',
'RFU',

'Transaction exceeds floor limit',
'Lower consecutive offline limit exceeded',
'Upper consecutive offline limit exceeded',
'Transaction selected randomly of on-line processing',
'Merchant forced transaction on-line',
'RFU',
'RFU',
'RFU',

'Default TDOL Used',
'Issuer authentication failed',
'Script processing failed before final Generate AC',
'Script processing failed after final Generate AC',
'Relay resistance threshold exceeded (Contactless Kernel 2)',
'Relay resistance time limits exceeded (Contactless Kernel 2)',
{'00':'Relay resistance protocol not supported (Contactless Kernel 2)',
'01':'Relay resistance protocol not performed (Contactless Kernel 2)',
'10':'Relay resistance protocol performed (Contactless Kernel 2)',
'11':'RFU'}],

# --------------------------------------------------

'Issuer Action Code':
['Offline data authentication was not performed',
'SDA failed',
'ICC data missing',
'Card appears on terminal exception file',
'DDA failed',
'CDA failed',
'RFU',
'RFU',

'ICC and terminal have different applicatioin versions',
'Expired application',
'Application not yet effective',
'Requested service not allowed for card product',
'New Card',
'RFU',
'RFU',
'RFU',

'Cardholder verification was not successful',
'Unrecognised CVM',
'PIN Try Limit exceeded',
'PIN entry required and PIN pad not present or not working',
'PIN entry required, PIN pad present, but PIN was not entered',
'Online PIN entered',
'RFU',
'RFU',

'Transaction exceeds floor limit',
'Lower consecutive offline limit exceeded',
'Upper consecutive offline limit exceeded',
'Transaction selected randomly for online processing',
'Merchant forced transaction online',
'RFU',
'RFU',
'RFU',

'Default TDOL used',
'Issuer authentication failed',
'Script processing failed before final GENERATE AC',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU'],

# --------------------------------------------------

'AIP':['RFU',
'SDA supported',
'DDA supported',
'Cardholder verification is supported',
'Terminal risk management is to be performed',
'Issuer authentication is supported ',
'RFU',
'CDA supported',

'RFU',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU'],

# --------------------------------------------------

'AUC':['Valid for domestic cash transactions',
'Valid for international cash transactions',
'Valid for domestic goods',
'Valid for international goods',
'Valid for domestic services',
'Valid for international services',
'Valid at ATMs',
'Valid at terminals other than ATMs',

'Domestic cashback allowed',
'International cashback allowed',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU',
'RFU']

}