from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    course_name=models.CharField(max_length=50,unique=True)
    course_duration=models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    batch_code=models.CharField(max_length=50,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_date=models.DateField(auto_now=True)
    course_fees=models.CharField(max_length=50)
    action=(
        ('1','Yet to begin'),
        ('2','Ongoing'),
        ('3','Completed')
    )
    batch_status=models.CharField(max_length=30,choices=action)

    def __str__(self):
        return self.batch_code

class Enquiry(models.Model):
    enquiryid=models.CharField(max_length=100,primary_key=True,editable=False)
    studentname=models.CharField(max_length=100)
    address=models.TextField()
    qualification=models.CharField(max_length=50)
    collegename=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    contact=models.IntegerField()
    email=models.EmailField(unique=True)
    enquirydate=models.DateField(auto_now=True)
    followup_date=models.DateField(auto_now=True)
    action=(
        ('1','Call_back'),
        ('2','Admitted'),
        ('3','Cancel')
    )
    status=models.CharField(max_length=20,choices=action)

    def __str__(self):
        return str(self.enquiryid)

class Admission(models.Model):
    admission_no=models.CharField(max_length=50,unique=True)
    enquiry_id=models.CharField(max_length=50)
    course_fees=models.IntegerField()
    batch_code=models.ForeignKey(Batch,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.admission_no

class Payment(models.Model):
    admission_no=models.CharField(max_length=50)
    amount=models.IntegerField()
    payment_date=models.DateField(auto_now=True)
    enquiryid=models.CharField(max_length=50)

    def __str__(self):
        return self.amount

