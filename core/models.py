from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    """
    Project relation.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    User relation. One user might have multiple project access and one project might have multiple users working on it
    """
    organisation = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    projects = models.ManyToManyField(Project, related_name="members")


class ResponsibleEntity(models.Model):
    """
    Responsibility relation.
    """
    person = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{},{}".format(self.person, self.position, self.organisation, self.site)


class Grievance(models.Model):
    """
    Grievance relation.
    """
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class Case(models.Model):
    """
    Case relation.
    """
    timestamp = models.DateTimeField(auto_created=True)
    project = models.ForeignKey(Project, related_name="cases", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="cases", on_delete=models.CASCADE)
    grievance = models.ForeignKey(Grievance, related_name="cases", on_delete=models.CASCADE)
    responsible_entity = models.ForeignKey(ResponsibleEntity, related_name="cases", on_delete=models.CASCADE)
    complainant_name = models.CharField(max_length=50, null=True, blank=True)
    complainant_address = models.TextField(null=True, blank=True)
    complainant_telephone = models.CharField(max_length=50, null=True, blank=True)
    incident_location_city = models.CharField(max_length=50, null=True, blank=True)
    incident_date = models.DateField()
    incident_location_type = models.CharField(max_length=50, choices=[
        ("home", "Home"),
        ("public_space", "Public Space"),
        ("work_site", "Work Site"),
        ("government_office", "Government office")
    ])
    incident_details = models.TextField(max_length=1024)
    accused_party = models.CharField(max_length=50)
    accused_name = models.CharField(max_length=50)
    incident_phase = models.IntegerField(default=1)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.project, self.complainant_name)
