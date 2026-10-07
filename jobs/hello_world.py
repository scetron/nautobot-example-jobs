"""Minimal example Job."""

from nautobot.apps.jobs import BooleanVar, Job, StringVar, register_jobs

name = "Example Jobs"  # Groups these jobs together in the Nautobot UI


class HelloWorld(Job):
    """Log a greeting to the Job Result."""

    greeting_name = StringVar(description="Who to greet", default="World")
    shout = BooleanVar(description="Uppercase the greeting", default=False)

    class Meta:
        name = "Hello World"
        description = "Logs a greeting. A starting point for new jobs."
        has_sensitive_variables = False

    def run(self, *, greeting_name, shout):  # pylint: disable=arguments-differ
        """Execute the job."""
        message = f"Hello, {greeting_name}!"
        if shout:
            message = message.upper()
        self.logger.info(message)
        return message


register_jobs(HelloWorld)
