import pyinputplus as py
import random,time

print('hello Shiva baba my world')
noOfqsn= 10
correctAns =0
for i in range(noOfqsn):
    num1= random.randint(0,9)
    num2= random.randint(0,9)
    prompt = '%s:: %s x %s ='%(i,num1,num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        py.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)

    except py.TimeoutException:
        print('Out of time!')
    except py.RetryLimitException:
        print('Out of tries!')

    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAns += 1

    time.sleep(1)  # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAns, noOfqsn))
