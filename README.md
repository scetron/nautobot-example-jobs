# Nautobot Example Jobs

Example [Nautobot Jobs](https://docs.nautobot.com/projects/core/en/stable/development/jobs/), structured so Nautobot can load them directly as a Git repository.

## Layout

```
jobs/
├── __init__.py        # Imports each job module so Nautobot discovers it
├── hello_world.py     # Minimal job with input variables
└── device_report.py   # Read-only report against Device data
```

Nautobot only looks at the `jobs/` package in a Git repository. Every module in it must call `register_jobs(...)`, and must also be imported in `jobs/__init__.py`.

## Loading into Nautobot

1. Push this repository to a Git server Nautobot can reach.
2. In Nautobot, go to **Extensibility → Git Repositories → Add**.
3. Set the remote URL and branch, and select **jobs** under *Provided Contents*.
4. Save and sync the repository, then go to **Jobs → Jobs** and enable the new jobs. Jobs are disabled by default.

After pushing changes, click **Sync** on the Git repository to reload the jobs.

## Local development

Install the dev tooling with [uv](https://docs.astral.sh/uv/). This also installs `nautobot`, so your editor can resolve its imports:

```bash
uv sync
uv run ruff check .
uv run ruff format .
```

To run the jobs, you need a Nautobot instance, either a dev environment or one with this repository added as described above.

## Adding a job

1. Create `jobs/<your_module>.py` with a `Job` subclass and call `register_jobs(YourJob)` at the bottom.
2. Add the module to the import in `jobs/__init__.py`.
3. Commit, push, and sync the repository in Nautobot.
