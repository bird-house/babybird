.. _configuration:

Configuration
=============

Command-line options
--------------------

You can overwrite the default `PyWPS`_ configuration by using command-line options.
See the Babybird help which options are available::

    $ babybird start --help
    --hostname HOSTNAME        hostname in PyWPS configuration.
    --port PORT                port in PyWPS configuration.

Start service with different hostname and port::

    $ babybird start --hostname localhost --port 5001

Use a custom configuration file
-------------------------------

You can overwrite the default `PyWPS`_ configuration by providing your own
PyWPS configuration file (just modifiy the options you want to change).
Use one of the existing ``sample-*.cfg`` files as example and copy them to ``etc/custom.cfg``.

For example change the hostname (*demo.org*) and logging level:

.. code-block:: console

   $ cd babybird
   $ vim etc/custom.cfg
   $ cat etc/custom.cfg
   [server]
   url = http://demo.org:5000/wps
   outputurl = http://demo.org:5000/outputs

   [logging]
   level = DEBUG

Start the service with your custom configuration:

.. code-block:: console

   # start the service with this configuration
   $ babybird start -c etc/custom.cfg


.. _PyWPS: http://pywps.org/
