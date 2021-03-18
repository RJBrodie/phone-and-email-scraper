import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
(\d\d\d\d\d) ? 	 # area code optional
(\s|-) 			 # first separator
\d\d\d\d\d\d
)  	 # number
''',re.VERBOSE)

# Create a regex for mobile numbers
mobileRegex = re.compile(r'''
(
(\d\d\d\d\d\d\d\d\d) 	 # number
)  	 # number
''',re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ 			    # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedMobile = mobileRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

allMobileNumber = []
for mobile in extractedMobile:
	allMobileNumber.append(mobile[0])

# print(allPhoneNumbers)
# print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allMobileNumber) + '\n'.join(extractedEmail) + '\n'
pyperclip.copy(results)
