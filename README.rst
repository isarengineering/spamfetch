##############################################################
spamfetch - a utility for fetching messages from spam archives
##############################################################


*****
About
*****
These tools will help you preseeding a Rspamd_ instance with qualified email spam messages.

Suitable sources for spam messages are:
- http://artinvoice.hu/spams/
- http://untroubled.org/spam/ (please use the untroubled-spam-fetcher)

.. _Rspamd: https://rspamd.com/
.. _untroubled-spam-fetcher: https://pypi.python.org/pypi/untroubled-spam-fetcher


****************
Acknowledgements
****************
Thanks to `Vsevolod Stakhov`_ for conceiving, building and maintaining Rspamd_ and
to Frantique and Bruce Guenter for collecting and publishing their spam collections.

.. _Vsevolod Stakhov: https://github.com/vstakhov


***************
Getting started
***************

Introduction
============
The processing is a two-step process. You will acquire the email archives from
upstream servers first and then prepare a directory structure with emails as
single "mbox" files suitable for learning by Rspamd_.

Install
=======
::

    git clone https://github.com/isarengineering/spamfetch
    cd spamfetch
    virtualenv --python=python3 .venv
    source .venv/bin/activate

Install prerequisites::

    pip install requests
    pip install delegator.py


Usage
=====

Fetch spam archives from http://artinvoice.hu/spams/ and store them into the target directory::

    python spamfetch_artinvoice.py /var/lib/spamarchive/artinvoice

Scan for email archive files (e.g. spam--2018-03-23.gz) in the source directory,
split email messages using ``formail`` and store as individual files into the target directory::

    python formailx.py /var/lib/spamarchive/artinvoice /var/lib/spamarchive/mboxes

Let Rspamd_ learn spam messages::

    rspamc learn_spam /var/lib/spamarchive/mboxes


*******************
Project information
*******************

About
=====
The "spamfetch" program is released under the GPL license.
The code lives on `GitHub <https://github.com/isarengineering/spamfetch>`_ and
the Python package is published to `PyPI <https://pypi.org/project/spamfetch/>`_.

The software has been tested on Python 3.6.

If you'd like to contribute you're most welcome!
Spend some time taking a look around, locate a bug, design issue or
spelling mistake and then send us a pull request or create an issue.

Thanks in advance for your efforts, we really appreciate any help or feedback.

Code license
============
Licensed under the GPL license. See LICENSE_ file for details.

.. _LICENSE: https://github.com/isarengineering/spamfetch/blob/master/LICENSE

Disclaimer
==========
The project and its authors are not affiliated with the upstream projects
or their authors in any way. It is a sole project from the community
for making data more accessible in the spirit of open data.
