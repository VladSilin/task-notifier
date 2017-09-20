"""Task Notifier.

Usage:
  task_notifier.py start
  task_notifier.py stop

"""

import os
import sys
import time

import schedule
from docopt import docopt

from gmail import send_email

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Task Notifier 1.0')

    if arguments.get('start'):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            print >> sys.stderr, 'Process fork failed %d - %s' % (e.errno, e.strerror)
            sys.exit(1)

        sender = ''
        recipient = ''
        subject = ''
        email_body = """
        Hello World!
        """

        schedule.every(1).minutes.do(
            lambda: send_email(sender, recipient, subject, email_body))

        while True:
            schedule.run_pending()
            time.sleep(1)
