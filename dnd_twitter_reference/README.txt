This is a reference folder that shows how the DnD Character of the Day Twitter account posts are created and posted.

A specific api_keys.txt file has been omitted to protect privacy to the Twitter account.  This file is used in the
automator_execution.py script to post to the DnD Character of the Day Twitter account automatically.

The process of the scripts in order are:
1. twitter_bot_automator.py creates a DnD 5th edition character stat sheet according to the DnD 5th edition rules
   reference.
   a. twitter_bot_automator.py generates random six sided dice rolls through dice_roller.py as needed within the script
   b. twitter_bot_automator.py generates a random name with name generator that pulls from btn_givennames.txt and
      btn_surnames.txt files
   c. twitter_bot_automator.py generates a random catchphrase from catch_phrase_list.py
2. automator_execution.py pulls the generated DnD character created in twitter_bot_automator.py and posts the text file
   to the DnD Twitter account with API keys.