# BaconCode overview
Decrypt simple messages using Francis Bacon rules

Francis Bacon was an English philosopher, statesman, scientist, jurist, orator, essayist and author. He served both as Attorney General and Lord Chancellor of England. After his death, he remained extremely influential through his works, especially as philosophical advocate and practitioner of the scientific method during the scientific revolution. His works established and popularised inductive methodologies for scientific inquiry, often called the Baconian method, or simply the scientific method. [Source: Wikipedia]

Baconian method assigns 0 and 1 to letters from the original messages (based on whether the letter is regular case or formatted), rewrite in base ten, and use the new numbers as indexes for the alphabets. For the sake of transmitting messages through different means, e.g. texting, status update, etc. that may drop the format, the messages follow the rule of 1 for upper case and 0 for lower case.

### How this works
1. Decrypting: The file decrypt.py accepts an input message, evaluates by Baconian method, and returns a the hidden message. 
  * Some requirements/notations:
    - Any non-alphabetical characters will be recognized as 0
    - Spaces are allowed
    - Input of correct upper/lowercase letters are extremely important
  * Examples:
    - Input message: The COw mOOs tHe chicKeN
    - Output message: TGIF
2. Encrypting: The file encrypt.py accepts an input message, evaluates by Baconian method, and returns a **suggestion** of upper/lowercase for letters 
