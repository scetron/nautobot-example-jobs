"""Read-only example Job that inspects Device data."""

from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models import Device, Location

name = "Example Jobs"  # Groups these jobs together in the Nautobot UI


class DevicesMissingPrimaryIP(Job):
    """Report devices that have no primary IPv4 or IPv6 address."""

    location = ObjectVar(
        model=Location,
        required=False,
        description="Limit the report to one location (leave blank for all devices)",
    )

    class Meta:
        name = "Devices Missing Primary IP"
        description = "Lists devices with no primary IP assigned. Makes no changes."
        read_only = True
        has_sensitive_variables = False

    def run(self, *, location=None):  # pylint: disable=arguments-differ
        """Execute the job."""
        devices = Device.objects.filter(primary_ip4__isnull=True, primary_ip6__isnull=True)
        if location:
            devices = devices.filter(location=location)

        devices = devices.select_related("location").order_by("name")
        count = 0
        for device in devices:
            count += 1
            self.logger.warning("No primary IP on %s (%s)", device.name, device.location, extra={"object": device})

        if count:
            self.logger.info("Found %d device(s) without a primary IP.", count)
        else:
            self.logger.info("Every device in scope has a primary IP.")
        return count


register_jobs(DevicesMissingPrimaryIP)
