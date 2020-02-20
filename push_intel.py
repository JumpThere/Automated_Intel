#!/venv/bin/python
import exchangelib
import os
from exchangelib import DELEGATE, Account, Credentials, Configuration, Folder
import time
## Let's calculate how much clock penalty would this script take - it's a script \
## and as such I don't have high hopes as compared to the compiled ones. ~JumpThere
start_timer = time.time()
creds = Credentials(
    username="domain\user",
    password="YourPassword"
)

config = Configuration(server='mail.yourmailserver.com', credentials=creds)

account = Account(
    primary_smtp_address="yourexchange@server.com",
    autodiscover=False,
    config=config,
    access_type=DELEGATE,
)
account.inbox.refresh()
#for item in accout.inbox.all():
 #   print item
#for item in account.inbox.all().order_by('-datetime_received')[:5]:
 #  print(item.subject, item.body, item.attachments)
 #  for test in item.attachments:
  #      print test

#for item in account.inbox.all().order_by('-datetime_received')[:5]:
# print item.attachments
#var.walk()
#### below this would walk the content within the given fol structure ##
#my_folder = account.inbox / 'PullThisFolder'
#for test in my_folder.all():
# print(test.attachments)
#### Marking this has done #######
my_folder = account.inbox / 'PullThis'
for test in my_folder.all()[:10]:
# print ("attachments			={}".format(test.attachments))
 for attachments in test.attachments:
   fpath = os.path.join('/home/dat/l_attach', attachments.name)
   with open(fpath, 'wb') as f:
      f.write(attachments.content)
end_timer = time.time()
penalty = end_timer - start_timer
print (penalty)   
