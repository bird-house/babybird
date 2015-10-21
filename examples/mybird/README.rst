======
MyBird
======

.. image:: https://travis-ci.org/bird-house/examples/mybird.svg?branch=master
   :target: https://travis-ci.org/bird-house/examples/mybird
   :alt: Travis Build


MyBird is an example for a minimal Web Processing Service using `PyWPS <https://github.com/geopython/PyWPS>`_. 
It uses Buildout to setup the complete installation with Nginx (Web Server), Gunicorn (Python WSGI) and Supervisor (service monitoring). The recipes to set up a WPS are coming from `Birdhouse <http://bird-house.github.io/>`_.

Installation
============

MyBird is installed like all Birdhouse components (http://birdhouse.readthedocs.org/en/latest/installation.html):

.. code-block:: sh

    $ https://github.com/bird-house/babybird.git
    $ cd babybird/examples/mybird
    $ make install
    $ make start
    
See if *mybird* is running:

.. code-block:: sh

    $ make status
    Supervisor status ...
    /home/pingu/.conda/envs/birdhouse/bin/supervisorctl status
    mybird                     RUNNING   pid 28185, uptime 0:00:03
    nginx                      RUNNING   pid 28192, uptime 0:00:03

By default MyBird is accessible at the URL::

    http://localhost:38101/wps


Configuration
=============

Edit ``custom.cfg`` to change default settings:

.. code-block:: sh

    $ vim custom.cfg
    $ cat custom.cfg
    [settings]
    hostname = localhost
    http-port = 38101

After these changes run:

.. code-block:: sh

    $ make update
    $ make restart


Example Usage with Birdy
========================

Install the Birdy WPS commandline client:

.. code-block:: sh

    $ conda install -c birdhouse birdhouse-birdy

Set the WPS service and run the birdy:

.. code-block:: sh

    $ export WPS_SERVICE=http://localhost:38101/wps
    $ birdy -h
    $ birdy wordcount -h
    $ birdy wordcount --text http://birdhouse.readthedocs.org/en/latest/installation.html




