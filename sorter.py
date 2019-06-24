import traceback

import dns.resolver
from time import time, sleep

start_time = time()

with open('emails.txt', 'r') as file:
    for line in file:
        domain = line.split('@')[1].strip('\n').split('.')

        if 'gmail' in domain:
            txt = 'google'
        elif 'yahoo' in domain or 'aol' in domain:
            txt = 'yahoo'
        elif 'outlook' in domain or 'hotmail' in domain:
            txt = 'outlook'
        elif 'comcast' in domain:
            txt = 'comcast'
        else:
            txt = 'none'

        with open('{}.txt'.format(txt), 'a') as f:
            f.write(line)

try:
    with open('none.txt', 'r') as file:
        for line in file:
            domain = line.split('@')[1].strip('\n')
            try:
                answers = dns.resolver.query(domain, 'MX')
                exchange = str(answers[0].exchange).split('.')
                print(exchange)
            except:
                exchange = ""
                traceback.print_exc()

            if 'google' in exchange:
                txt = 'google'
            elif 'yahoo' in exchange or 'aol' in exchange:
                txt = 'yahoo'
            elif 'outlook' in exchange or 'hotmail' in exchange:
                txt = 'outlook'
            elif 'comcast' in exchange:
                txt = 'comcast'
            else:
                txt = 'other'

            with open('{}.txt'.format(txt), 'a') as f:
                f.write(line)
except FileNotFoundError:
    pass


def writer(email, file, exchange):
    pass

# program end time
end_time = time()
tot_time = end_time - start_time

# printing run time
print("\n** Total Elapsed Runtime:",
      str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
      + str(int((tot_time % 3600) % 60)))
