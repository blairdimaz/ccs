from django.db import models

# Create your models here.

class ccsFormData(models.Model):
    clientNumber = models.CharField(max_length=9, blank=True)
    title = models.CharField(max_length=40, blank=True)
    firstName = models.CharField(max_length=40, blank=True)
    lastName = models.CharField(max_length=40, blank=True)
    firstNameNOTsame = models.CharField(max_length=40, blank=True)
    lastNameNOTsame = models.CharField(max_length=40, blank=True)
    nameOtherKnown = models.CharField(max_length=40, blank=True)
    namePrefer = models.CharField(max_length=40, blank=True)
    dob = models.DateField(null=True)

    gender = models.CharField(max_length=40, blank=True)
    irdNumber = models.CharField(max_length=40, blank=True)
    flatHouseNum = models.CharField(max_length=40, blank=True)
    streetName = models.CharField(max_length=40, blank=True)
    suburb = models.CharField(max_length=40, blank=True)
    townCity = models.CharField(max_length=40, blank=True)
    mailingAddr = models.CharField(max_length=40, blank=True)
    homePhone = models.CharField(max_length=40, blank=True)
    mobPhone = models.CharField(max_length=40, blank=True)
    otherPhone = models.CharField(max_length=40, blank=True)
    getEmails = models.CharField(max_length=40, blank=True)

    ethnicity = models.CharField(max_length=40, blank=True)
    usuallyNZ = models.CharField(max_length=40, blank=True)
    residenceStatus = models.CharField(max_length=40, blank=True)
    dateGranted = models.DateField(null=True)
    dateArrived = models.DateField(null=True)
    countryOfBirth = models.CharField(max_length=40, blank=True)
    ccAssistanceReason = models.CharField(max_length=40, blank=True)
    isWorking = models.CharField(max_length=40, blank=True)
    employerName = models.CharField(max_length=40, blank=True)
    employerAddr = models.CharField(max_length=40, blank=True)
    employerPhone = models.CharField(max_length=40, blank=True)
    employerFaxEmail = models.CharField(max_length=40, blank=True)
    hoursPerWeek = models.CharField(max_length=40, blank=True)
    hoursTravel = models.CharField(max_length=40, blank=True)
    isWorkRelatedCourse = models.CharField(max_length=40, blank=True)
    trainingOrgName = models.CharField(max_length=40, blank=True)
    trainingOrgAddr = models.CharField(max_length=40, blank=True)
    trainingOrgPhone = models.CharField(max_length=40, blank=True)
    trainingOrgFaxEmail = models.CharField(max_length=40, blank=True)
    employerFaxEmail = models.CharField(max_length=40, blank=True)

    nameOfCourse = models.CharField(max_length=40, blank=True)
    isNZQA = models.CharField(max_length=40, blank=True)
    courseStartDate = models.DateField(null=True)
    courseEndDate = models.DateField(null=True)
    courseHoursPerWeek = models.CharField(max_length=40, blank=True)
    otherStudyHoursPerWeek = models.CharField(max_length=40, blank=True)
    hoursTravelCCtoCourse = models.CharField(max_length=40, blank=True)
    isArrangedActivities = models.CharField(max_length=40, blank=True)
    activityType = models.CharField(max_length=40, blank=True)
    hoursActivity = models.CharField(max_length=40, blank=True)
    hoursTravelCCtoActivity = models.CharField(max_length=40, blank=True)
    applyForMedicalReasons = models.CharField(max_length=40, blank=True)
    medicalDurationExpected = models.CharField(max_length=40, blank=True)
    hoursPerWeekNeedCC = models.CharField(max_length=40, blank=True)
    incomeWagesSalary = models.CharField(max_length=40, blank=True)
    incomePPL = models.CharField(max_length=40, blank=True)
    terminationPay = models.CharField(max_length=40, blank=True)
    redundancyPay = models.CharField(max_length=40, blank=True)
    acc = models.CharField(max_length=40, blank=True)
    incomeInsurance = models.CharField(max_length=40, blank=True)
    incomeBusiness = models.CharField(max_length=40, blank=True)
    incomeSelfEmpContract = models.CharField(max_length=40, blank=True)
    incomeInterest = models.CharField(max_length=40, blank=True)
    incomeDividends = models.CharField(max_length=40, blank=True)
    incomeRental = models.CharField(max_length=40, blank=True)
    incomeFlatmates = models.CharField(max_length=40, blank=True)
    incomeChildSup = models.CharField(max_length=40, blank=True)
    incomeOtherForChild = models.CharField(max_length=40, blank=True)
    incomeMaintenance = models.CharField(max_length=40, blank=True)
    incomeFormerPartner = models.CharField(max_length=40, blank=True)
    incomeStudentAllowance = models.CharField(max_length=40, blank=True)
    incomeOverseasPension = models.CharField(max_length=40, blank=True)
    incomeSuper = models.CharField(max_length=40, blank=True)
    incomeEstate = models.CharField(max_length=40, blank=True)
    incomeTrusts = models.CharField(max_length=40, blank=True)
    incomeOther = models.CharField(max_length=40, blank=True)
















# class BookNumber(models.Model):
#     isbn_10 = models.CharField(max_length=10, blank=True)
#     isbn_13 = models.CharField(max_length=13, blank=True)
#
# class Book(models.Model):
#
#     title = models.CharField(max_length=36, blank=False, unique=True)
#     description = models.TextField(max_length=256, blank=True)
#
#     price = models.DecimalField(max_digits=6, default=0, decimal_places=2)
#     published = models.DateField(blank=True, null=True, default=None)
#     cover = models.FileField(upload_to='covers/', blank=True)
#     is_published = models.BooleanField(default=False)
#
#     number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
# class Character(models.Model):
#     name = models.CharField(max_length=30)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='characters')
#
# class Author(models.Model):
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)
#     books = models.ManyToManyField(Book, related_name='authors')
#

