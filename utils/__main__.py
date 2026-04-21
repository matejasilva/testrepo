"""Allow running utils as python -m utils.

Re-exports :func:`utils.cli.main` for the ``python -m utils`` entrypoint.
"""

from .cli import main

if __name__ == "__main__":
    main()
