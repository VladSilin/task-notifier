"""Task Notifier.

Usage:
  task_notifier.py start
  service-monitor.py stop

"""

import os
import sys
import schedule
from docopt import docopt


def send_email(sender, recipient, subject, body):
    print 'Sending email.'

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

    schedule.every(10).minutes.do(send_email);