# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## Unreleased

### Fixed

-   Grid implementation for service factory methods.

- Test Errors like:

  ```json
  {
     "_type":"Error",
     "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
     "message":"You are not authorized to access this resource."
  }
  ```

## [v0.7.4](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.4) - 2021-03-26

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- User service test revert

### Fixed

- [Issue #24: TimeEntryServiceImpl find_between_days not working](https://github.com/Flying-Free/pyopenproject/issues/24)
- Codacy issues

## [v0.7.4-beta.3](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.4-beta.3) - 2021-03-26

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- Codacy issues

## [v0.7.4-beta.2](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.4-beta.2) - 2021-03-26

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- User service test revert

## [v0.7.4-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.4-beta.1) - 2021-03-26

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- [Issue #24: TimeEntryServiceImpl find_between_days not working](https://github.com/Flying-Free/pyopenproject/issues/24)

## [v0.7.3](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.3) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- Folder tree changed in order to make the imports like:

```python
from pyopenproject.openproject import OpenProject
from pyopenproject.model import WorkPackage
```

## [v0.7.2](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.2) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- Folder tree changed in order to make the imports like:

```python
from pyopenproject.openproject import OpenProject
from pyopenproject.model import WorkPackage
```

## [v0.7.2-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.2-beta.1) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Folder tree changed in order to make the imports like:

```python
from pyopenproject.openproject import OpenProject
from pyopenproject.model import WorkPackage
```

## [v0.7.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.1) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Folder tree changed in order to make the imports like:

```python
from pyopenproject.openproject import OpenProject
from pyopenproject.model import WorkPackage
```

## [v0.7.1-beta.2](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.1-beta.2) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Folder tree changed in order to make the imports like:

```python
from pyopenproject.openproject import OpenProject
from pyopenproject.model import WorkPackage
```


## [v0.7.1-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7.1-beta.1) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Folder tree changed in order to make the import like:

```python
from pyopenproject import OpenProject
```

## [v0.7](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Invite user. Now, the required parameter is the e-mail.


## [v0.7-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.7-beta.1) - 2021-03-22

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- Invite user. Now, the required parameter is the e-mail.

## [v0.6](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.6) - 2021-03-19

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added
Fix some update commands adding a rule to exclude read only fields:

- Time entry update
- Grid update
- Relation update
- Query update 

## [v0.5](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.5) - 2021-03-16

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Project's FindByContext class. Now, _pyopenproject_ can requests a project by its context.


### Fixed

- Find Role:

```json
{
     "_type":"Error",
     "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
     "message":"You are not authorized to access this resource."
}
```

## [v0.5-beta.2](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.5-beta.2) - 2021-03-16

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- Find Role:

```json
{
     "_type":"Error",
     "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
     "message":"You are not authorized to access this resource."
}
```

## [v0.5-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.5-beta.1) - 2021-03-15

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Project's FindByContext class. Now, _pyopenproject_ can requests a project by its context.

## [v0.4](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.4) - 2021-03-08

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Users's FindByContext class. Now, _pyopenproject_ can requests a user by its context.

## [v0.4-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.4-beta.1) - 2021-03-08

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Users's FindByContext class. Now, _pyopenproject_ can requests a user by its context.

## [v0.3](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.3) - 2021-03-03

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Management of pagination requests that return a list of objects.

## [v0.3-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.3-beta.1) - 2021-03-03

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

- Management of pagination requests that return a list of objects.

## [v0.2](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.2) - 2021-03-03

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- `setup.py` loads the dependences of the library from the `requirements.txt`

## [v0.2-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.2-beta.1) - 2021-03-03

Beta version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Changed

- `setup.py` loads the dependences of the library from the `requirements.txt`

## [v0.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.1) - 2021-02-26

First major version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Fixed

- GitHub Workflows has been fixed to make CI after PR and .

## [v0.1-beta.1](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.1-beta.1) - 2021-02-26

First alpha version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

## [v0.1-alpha](https://github.com/Flying-Free/pyopenproject/releases/tag/v0.1-alpha) - 2021-02-24

First alpha version of pyopenproject library. This library is a way to enable Python developers to communicate with
the [OpenProject API](https://docs.openproject.org/api/) with simplicity. Take in consideration that this development is
only available for Python 3.6 or more.

### Added

-   Service factory pattern to organize the multiple methods for the different classes of the model.

-   Model classes based on API endpoints

### Changed

-   [Update/create methods in model classes.](https://github.com/Flying-Free/pyopenproject/issues/2)
    Model classes don't have implemented methods from service factory

### Fixed

-   [Classes "Delete" in service command.](https://github.com/Flying-Free/pyopenproject/issues/3)
    Delete classes are not given Request errors

-   [Create/Update classes in service command.](https://github.com/Flying-Free/pyopenproject/issues/1)
    Create/Update classes are not given Request errors
