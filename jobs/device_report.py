"""Read-only example Job that inspects Device data."""

from django.db.models import Q
from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models import Device, Location

name = "Example Jobs"  # Groups these jobs together in the Nautobot UI


class DevicesWithPrimaryIP(Job):
    """Count devices that have a primary IPv4 or IPv6 address assigned."""

    location = ObjectVar(
        model=Location,
        required=False,
        description="Limit the count to one location (leave blank for all devices)",
    )

    class Meta:
        name = "Devices With Primary IP"
        description = "Counts devices with a primary IP assigned. Makes no changes."
        read_only = True
        has_sensitive_variables = False

    def run(self, *, location=None):  # pylint: disable=arguments-differ
        """Execute the job."""
        devices = Device.objects.all()
        if location:
            devices = devices.filter(location=location)

        total = devices.count()
        count = devices.filter(Q(primary_ip4__isnull=False) | Q(primary_ip6__isnull=False)).count()

        self.logger.info("%d of %d device(s) have a primary IP assigned.", count, total)
        return count


register_jobs(DevicesWithPrimaryIP)
