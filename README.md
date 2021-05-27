# Slack-birthday-bot
  Slack bot in python that reads birthday from a csv file, and posts a congratulations message to the desired channel. 

# Requirements
  The .csv file should be in the following format:

  'Full Name", 'Date', 'Month', 'Slack_ID' (to tag).
  
Example:
  John Smith, 12, 04, <@U451228439>  # John Smith is born on the 12th of April and has user ID <@U451228439>
  
Python libraries:
  slack_sdk
  dotenv
  datetime
  attr
  csv
  os
  
Environment-variable:
  Used to store your slack-token and what channel to post to. Loaded through dotenv.
  
ENJOY!

  

  
