# PyOpenProject

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea408dca24024a2580aea41a9cd890ad)](https://app.codacy.com/gh/Flying-Free/pyopenproject?utm_source=github.com&utm_medium=referral&utm_content=Flying-Free/pyopenproject&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/f8f668fa0b344ba7bea7b56ba743a091)](https://www.codacy.com/gh/Flying-Free/pyopenproject/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Flying-Free/pyopenproject&utm_campaign=Badge_Coverage)
[![Run Test Cases](https://github.com/Flying-Free/pyopenproject/actions/workflows/test_cases.yml/badge.svg?branch=main)](https://github.com/Flying-Free/pyopenproject/actions/workflows/test_cases.yml)

Python library to interact with OpenProject API.

```python
from pyopenproject.openproject import OpenProject

op = OpenProject(url="http://localhost:8080", apikey="6289058256894568479567886794")
user = op.get_user_services().create(
                    login="h.wurst",
                    email="h.wurst@openproject.com",
                    first_name="Hans",
                    last_name="Wurst",
                    admin=False,
                    language="de",
                    status="active",
                    # Password minimum is 10 characters)
                    password="h.wurst1234567890"
                )
```

This library could be understood as a compendium of OpenProject endpoints services to use in a client project with the
purpose of interact with OpenProject instance through its API.

## Installing pyopenproject

PyOpenProject is available on PyPI:

```shell
python -m pip install pyopenproject
```

## Documentation

-   [API Reference](https://docs.openproject.org/api/)
-   You can see some code examples developed in our [test cases](./tests/test_cases)

## Contributing

If you want to contribute, please:

1. Fork it (<https://github.com/Flying-Free/pyopenproject/fork>)
2. Create your feature branch (`git checkout -b feature/newEndpoint`)
3. Commit your changes (`git commit -am 'Add some new Endpoint'`)
4. Push to the branch (`git push origin feature/newEndpoint`)
5. Create a new Pull Request

## Authors

-   ### Alan Padierna Fernández
    [@AlanPadi95](https://github.com/AlanPadi95)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5.svg?logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/alan-padierna-fern%C3%A1ndez-199a48152/)

-   ### Marcelo Torrejón Manso
    [@marcelotm23](https://github.com/marcelotm23)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5.svg?logo=LinkedIn&logoColor=white)](https://es.linkedin.com/in/marcelo-torrej%C3%B3n-manso-b45952160)

## Contributors

-   ### Pablo Suarez García
    [@PabloSuaGar](https://github.com/PabloSuaGar)
