# django-unmanaged-model
Demo for using Django unmanaged model in the tests.

## Installation
1. create a virtualenv
    ```shell
    virtualenv .venv
    ```

2. activate virtualenv
    ```shell
    . .venv/bin/activate
    ```

3. install packages
    ```shell
    make install
    ```

## Development
Update packages
```shell
make compile && make sync
```

Running tests
```shell
pytest
```
