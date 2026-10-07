"""Nautobot Jobs loaded from this Git repository.

Nautobot imports this package when the repository syncs. Each job module calls
``register_jobs()`` itself, so importing a module here is enough to expose its jobs.
"""

from . import device_report, hello_world  # noqa: F401

