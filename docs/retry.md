# Retry Utilities

Retry decorator for transient failures.

## Usage

```python
from utils import retry, RetryError

@retry(retries=3, delay=1, exceptions=(ConnectionError,))
def fetch():
    ...
```

## CLI

Retry is a decorator; no CLI command.
