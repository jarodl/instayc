#######
instayc
#######

1. Add keywords that interest you
2. Run `instayc`
3. Read the articles later on Instapaper

Warning: you might want to wait until articles are put in their own
folder to prevent a lot of unwanted links being added to your instapaper
account.

=====
Usage
=====

Here is how to use it::

	$ instayc
	Instapaper username: bob
	Instapaper password:
	Success!
	$ instayc -a 'python, django, javascript, math, computer science'
	$ instayc
	Updating...
	14 article(s) were added to Instapaper

============
Installation
============

Use pip::

	pip install instayc

or..::

	easy_install instayc

====
TODO
====

* articles that do not have a interest in the title are added sometimes
* prevent duplicate interests in the config file
* use the new Instapaper API and only store a token instead of user/pass
* put articles in their own folder on Instapaper
