import praw
import time
from datetime import datetime, timedelta

####### >>>> SPECIFICATION <<<<


## >> Oauth details <<  
APP_ID = ""
APP_SECRET = ""
APP_URI = ""
APP_REFRESH = ""
## >> Oauth details end here <<

subreddit_name = "" #Enter the name of the subreddit
subject_list = ["submitter",] #If the message subject contains one of this keyterms, the user will be made a submitter. You can add more keyterms after a comma. 
pause = 300  #this value will specify how many seconds will the bot wait between cycles. 

###### >>>> SPECIFICATION END HERE <<<<

print("logging in")


r = praw.Reddit("approved submitter adder by /u/rajjjjk")
r.set_oauth_app_info(APP_ID, APP_SECRET, APP_URI)
r.refresh_access_information(APP_REFRESH)



def message_scanner():
    print('searching inbox' )
    subreddit = r.get_subreddit(subreddit_name)
    mailbox = list(r.get_unread(limit = 100))
    for message in mailbox:
        try:
            message_author = message.author.name
            message_subject = message.subject.lower()
            
            karma = r.get_redditor(message_author).link_karma
            age_in_days = (datetime.now() - datetime.fromtimestamp(user.created_utc)).days
            if any(word.lower() in message_subject for word in subject_list) and karma > 100 and age_in_days < 365:
                subreddit.add_contributor(message_author)
                print(message_author + ' is now an approved submitter')
                message.mark_as_read()
            
        except AttributeError:
            print('failed to fetch new user')

while True:
    try:
        message_scanner()
    except Exception as error:
        print('An error has been generated : ' + str(error))

    print('paused for ', wait, ' seconds.')
    time.sleep(pause)
