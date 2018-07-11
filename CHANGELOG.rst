.. :changelog:

Release History
===============


1.5.3 (2018-07-07)
~~~~~~~~~~~~~~~~~~

**Improvements**

- API calls return actual `Response` object instead of returning `None`.
- Added "--attempts=<max>" option to specify maximum number of attempts before giving up.
- Added "check_rest_version" command.
- Added "mock" and "real" tests.

**Bugfixes**

- Added check that job was actually created on JPred server.


1.5.2 (2018-06-19)
~~~~~~~~~~~~~~~~~~

**Improvements**

- Isolated CLI into its own module.
- Added entry point, i.e. can use `$ jpredapi` instead of `python3 -m jpredapi`.


1.5.1 (2017-11-29)
~~~~~~~~~~~~~~~~~~

**Bugfixes**

- Minor bug fixes and cleanup.


1.5.0 (2017-02-07)
~~~~~~~~~~~~~~~~~~

- Initial public release 
  (version "1.5.0" matches the JPred REST API version).
