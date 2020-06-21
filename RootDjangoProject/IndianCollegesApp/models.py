from django.db import models


class AllStates(models.Model):
    state_name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.state_name


class AllCities(models.Model):
    city_name = models.TextField()
    state_id = models.ForeignKey(AllStates, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class AllColleges(models.Model):
    state_name = models.ForeignKey(AllStates, on_delete=models.CASCADE)
    city_name = models.ForeignKey(AllCities, on_delete=models.CASCADE)
    college_name = models.TextField(null=True, unique=True)
    location = models.TextField(null=True)
    college_type = models.CharField(null=True, max_length=1500)
    college_rank = models.FloatField(default=0)
    course_type = models.CharField(null=True, max_length=1500)
    established_date = models.DateField(null=True)
    affilicated_by = models.CharField(null=True, max_length=1500)
    college_fees_per_semester = models.FloatField(default=0)
    college_website_link = models.TextField(null=True)
    exams_for_admission = models.CharField(null=True, max_length=1500)
    course_duration = models.CharField(null=True, max_length=400)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.college_name


class CollegeImages(models.Model):
    image_url = models.ImageField(upload_to='all_images')
    college_id = models.ForeignKey(AllColleges, on_delete=models.CASCADE)


