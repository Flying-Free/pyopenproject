# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Fixed

- Grid implementation for service factory methods
- Test Errors like:
  ```json
  {
     "_type":"Error",
     "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
     "message":"You are not authorized to access this resource."
  }
  ```

## [v0.1-alpha] - 2021-02-24

First alpha version of openproject-sdk library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Service factory pattern to organize the multiple methods for the different classes of the model.
- Model classes based on API endpoints

### Changed

- [Update/create methods in model classes.](https://github.com/Flying-Free/python-openproject-api/issues/2)
  Model classes don't have implemented methods from service factory

### Fixed

- [Classes "Delete" in service command.](https://github.com/Flying-Free/python-openproject-api/issues/3)
  Delete classes are not given Request errors
- [Create/Update classes in service command.](https://github.com/Flying-Free/python-openproject-api/issues/1)
  Create/Update classes are not given Request errors
