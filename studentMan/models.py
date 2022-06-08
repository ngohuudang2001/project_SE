from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
# Create your models here.
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        user = CustomUser(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = (('1', "Admin"), ('2', "Teacher"), ('3', "Student"))
    SEX_CATELOGY = [("1", "Nam"), ("0", "Nữ")]

    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(default='1', choices=USER_TYPE, max_length=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(default='', max_length=200)
    dateOfBirth = models.DateTimeField(default=now)
    sex = models.CharField(default='1', choices=SEX_CATELOGY, max_length=1)
    phone = models.CharField(default='', max_length=20)
    email = models.EmailField(default='')
    address = models.TextField(default='')
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Age(models.Model):
    year = models.CharField(max_length=200, null=False, unique=True)
    max_age = models.IntegerField(null=False)
    min_age = models.IntegerField(null=False)

    def __str__(self):
        return self.year


class ClassOfSchool(models.Model):
    classId = models.CharField(max_length=200, null=False, unique=False)
    max_number = models.IntegerField(null=False)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId


class Subject(models.Model):
    SubjectID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    approved_mark = models.FloatField(null=False)

    def __str__(self):
        return self.SubjectID


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classOfSchool = models.ManyToManyField(ClassOfSchool, blank=True)

    def __str__(self):
        return self.user.name


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classOfSchool = models.ManyToManyField(ClassOfSchool, blank=True)

    def __str__(self):
        return self.user.name


class Mark(models.Model):
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2')
    )
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    semester_mark = models.CharField(max_length=200, null=False, choices=SEMESTER_CATEGORY)
    markFifteen = models.FloatField(null=True, blank=True)
    markOne = models.FloatField(null=True, blank=True)
    markFinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.student.StudentID + '_' + self.semester_mark
