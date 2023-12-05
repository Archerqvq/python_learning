# In Python, the statement
#
# from email.message import EmailMessage imports
#
# only the EmailMessage class from the email.message module. This allows
# you to use the EmailMessage class directly in your code without needing
# to prefix the module name.

# Here is how you would use it:

from email.message import EmailMessage

message = EmailMessage()
message['Subject'] = 'Hello'
message['From'] = 'sender@example.com'
message['To'] = 'receiver@example.com'
message.set_content('This is a test mail.')

# On the other hand, the statement
#
# import EmailMessage
#
# attempts to import a module named EmailMessage directly, which
# will not work because there is no standard module by that name.
# If you were trying to import the EmailMessage class, this would
# result in an ImportError.

# The correct way to import the EmailMessage class, if you don't want
# to use the
#
# from module import class
#
# syntax, is to import the email.message module and use the EmailMessage
# class with the module prefix like so:

import email.message

message = email.message.EmailMessage()
message['Subject'] = 'Hello'
message['From'] = 'sender@example.com'
message['To'] = 'receiver@example.com'
message.set_content('This is a test mail.')

# However, the first method using
#
# from email.message import EmailMessage
#
# is more common and convenient when you only need the
# EmailMessage class from the email,message module.
