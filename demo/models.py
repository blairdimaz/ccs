from django.db import models

# Create your models here.
class ece(models.Model):
    ECE_Id = models.CharField(max_length=9, blank=True)
    Org_Name = models.CharField(max_length=9, blank=True)
    Email = models.CharField(max_length=9, blank=True)
    Org_Type = models.CharField(max_length=9, blank=True)
    Twenty_Hrs_ECE = models.CharField(max_length=9, blank=True)
    Charges_HoldingAbsenceFee = models.CharField(max_length=9, blank=True)
    Education_Region = models.CharField(max_length=9, blank=True)
    Contact1_Name = models.CharField(max_length=9, blank=True)


class parent(models.Model):
    username = models.CharField(max_length=9, blank=True)
    children = models.CharField(max_length=9, blank=True)
    applications = models.CharField(max_length=9, blank=True)
    getEmails = models.CharField(max_length=40, blank=True)
    partner = models.CharField(max_length=40, blank=True)

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
    ethnicity = models.CharField(max_length=40, blank=True)




class children(models.Model):
    child_FullName = models.CharField(max_length=40, blank=True)
    child_DOB = models.DateField(null=True)
    child_Parent = models.CharField(max_length=40, blank=True)
    Child_ECE_Provider= models.CharField(max_length=40, blank=True)
    Child_ECE_WeekTotal= models.CharField(max_length=40, blank=True)
    Child_ECE_StartDate= models.DateField(null=True)


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
    jointPartnerWhere1 = models.CharField(max_length=40, blank=True)
    jointPartnerWith1 = models.CharField(max_length=40, blank=True)
    jointPartnerYou1 = models.CharField(max_length=40, blank=True)
    jointPartnerFreq1 = models.CharField(max_length=40, blank=True)
    jointPartnerWhere2 = models.CharField(max_length=40, blank=True)
    jointPartnerWith2 = models.CharField(max_length=40, blank=True)
    jointPartnerYou2 = models.CharField(max_length=40, blank=True)
    jointPartnerFreq2  = models.CharField(max_length=40, blank=True)
    jointPartnerWhere3  = models.CharField(max_length=40, blank=True)
    jointPartnerWith3  = models.CharField(max_length=40, blank=True)
    jointPartnerYou3  = models.CharField(max_length=40, blank=True)
    jointPartnerFreq3  = models.CharField(max_length=40, blank=True)
    jointPartnerWhere4  = models.CharField(max_length=40, blank=True)
    jointPartnerWith4  = models.CharField(max_length=40, blank=True)
    jointPartnerYou4  = models.CharField(max_length=40, blank=True)
    jointPartnerFreq4  = models.CharField(max_length=40, blank=True)
    jointPartnerWhere5  = models.CharField(max_length=40, blank=True)
    jointPartnerWith5  = models.CharField(max_length=40, blank=True)
    jointPartnerYou5  = models.CharField(max_length=40, blank=True)
    jointPartnerFreq5  = models.CharField(max_length=40, blank=True)



    other52weeksType1  = models.CharField(max_length=40, blank=True)
    other52weeksWhere1  = models.CharField(max_length=40, blank=True)
    other52weeksValue1  = models.CharField(max_length=40, blank=True)
    other52weeksType2  = models.CharField(max_length=40, blank=True)
    other52weeksWhere2  = models.CharField(max_length=40, blank=True)
    other52weeksValue2  = models.CharField(max_length=40, blank=True)
    other52weeksType3  = models.CharField(max_length=40, blank=True)
    other52weeksWhere3  = models.CharField(max_length=40, blank=True)
    other52weeksValue3  = models.CharField(max_length=40, blank=True)
    other52weeksType4  = models.CharField(max_length=40, blank=True)
    other52weeksWhere4  = models.CharField(max_length=40, blank=True)
    other52weeksValue4  = models.CharField(max_length=40, blank=True)
    other52weeksType5  = models.CharField(max_length=40, blank=True)
    other52weeksWhere5  = models.CharField(max_length=40, blank=True)
    other52weeksValue5  = models.CharField(max_length=40, blank=True)

    childFullName_1= models.CharField(max_length=40, blank=True)
    childDOB_1= models.DateField(null=True)
    childRelationToYou_1= models.CharField(max_length=40, blank=True)
    childFullName_2= models.CharField(max_length=40, blank=True)
    childDOB_2= models.DateField(null=True)
    childRelationToYou_2= models.CharField(max_length=40, blank=True)
    childFullName_3= models.CharField(max_length=40, blank=True)
    childDOB_3= models.DateField(null=True)
    childRelationToYou_3= models.CharField(max_length=40, blank=True)
    childFullName_4= models.CharField(max_length=40, blank=True)
    childDOB_4= models.DateField(null=True)
    childRelationToYou_4= models.CharField(max_length=40, blank=True)
    childFullName_5= models.CharField(max_length=40, blank=True)
    childDOB_5= models.DateField(null=True)
    childRelationToYou_5= models.CharField(max_length=40, blank=True)

    Child_ECE_ChildName_1= models.CharField(max_length=40, blank=True)
    Child_ECE_Provider_1= models.CharField(max_length=40, blank=True)
    Child_ECE_WeekTotal_1= models.CharField(max_length=40, blank=True)
    Child_ECE_StartDate_1= models.DateField(null=True)

    Child_ECE_ChildName_2= models.CharField(max_length=40, blank=True)
    Child_ECE_Provider_2= models.CharField(max_length=40, blank=True)
    Child_ECE_WeekTotal_2= models.CharField(max_length=40, blank=True)
    Child_ECE_StartDate_2= models.DateField(null=True)

    Child_ECE_ChildName_3= models.CharField(max_length=40, blank=True)
    Child_ECE_Provider_3= models.CharField(max_length=40, blank=True)
    Child_ECE_WeekTotal_3= models.CharField(max_length=40, blank=True)
    Child_ECE_StartDate_3= models.DateField(null=True)

    Child_ECE_ChildName_4= models.CharField(max_length=40, blank=True)
    Child_ECE_Provider_4= models.CharField(max_length=40, blank=True)
    Child_ECE_WeekTotal_4= models.CharField(max_length=40, blank=True)
    Child_ECE_StartDate_4= models.DateField(null=True)

    whichChildCCS_1= models.CharField(max_length=40, blank=True)
    whichChildCCS_2= models.CharField(max_length=40, blank=True)
    whichChildCCS_3= models.CharField(max_length=40, blank=True)
    whichChildCCS_4= models.CharField(max_length=40, blank=True)

    whichChildOSCAR_1= models.CharField(max_length=40, blank=True)
    whichChildOSCAR_2= models.CharField(max_length=40, blank=True)
    whichChildOSCAR_3= models.CharField(max_length=40, blank=True)
    whichChildOSCAR_4= models.CharField(max_length=40, blank=True)

    understandRelationship= models.CharField(max_length=40, blank=True)
    hasPartner= models.CharField(max_length=40, blank=True)
    partnerFullName= models.CharField(max_length=40, blank=True)
    partnerDOB= models.DateField(null=True)
    relationshipStatus= models.CharField(max_length=40, blank=True)

    p_clientNumber = models.CharField(max_length=9, blank=True)
    p_title = models.CharField(max_length=40, blank=True)
    p_firstName = models.CharField(max_length=40, blank=True)
    p_lastName = models.CharField(max_length=40, blank=True)
    p_firstNameNOTsame = models.CharField(max_length=40, blank=True)
    p_lastNameNOTsame = models.CharField(max_length=40, blank=True)
    p_nameOtherKnown = models.CharField(max_length=40, blank=True)
    p_namePrefer = models.CharField(max_length=40, blank=True)
    p_dob = models.DateField(null=True)

    p_gender = models.CharField(max_length=40, blank=True)
    p_irdNumber = models.CharField(max_length=40, blank=True)
    p_flatHouseNum = models.CharField(max_length=40, blank=True)
    p_streetName = models.CharField(max_length=40, blank=True)
    p_suburb = models.CharField(max_length=40, blank=True)
    p_townCity = models.CharField(max_length=40, blank=True)
    p_mailingAddr = models.CharField(max_length=40, blank=True)
    p_homePhone = models.CharField(max_length=40, blank=True)
    p_mobPhone = models.CharField(max_length=40, blank=True)
    p_otherPhone = models.CharField(max_length=40, blank=True)
    p_getEmails = models.CharField(max_length=40, blank=True)

    p_ethnicity = models.CharField(max_length=40, blank=True)
    p_usuallyNZ = models.CharField(max_length=40, blank=True)
    p_residenceStatus = models.CharField(max_length=40, blank=True)
    p_dateGranted = models.DateField(null=True)
    p_dateArrived = models.DateField(null=True)
    p_countryOfBirth = models.CharField(max_length=40, blank=True)
    p_ccAssistanceReason = models.CharField(max_length=40, blank=True)
    p_isWorking = models.CharField(max_length=40, blank=True)
    p_employerName = models.CharField(max_length=40, blank=True)
    p_employerAddr = models.CharField(max_length=40, blank=True)
    p_employerPhone = models.CharField(max_length=40, blank=True)
    p_employerFaxEmail = models.CharField(max_length=40, blank=True)
    p_hoursPerWeek = models.CharField(max_length=40, blank=True)
    p_hoursTravel = models.CharField(max_length=40, blank=True)
    p_isWorkRelatedCourse = models.CharField(max_length=40, blank=True)
    p_trainingOrgName = models.CharField(max_length=40, blank=True)
    p_trainingOrgAddr = models.CharField(max_length=40, blank=True)
    p_trainingOrgPhone = models.CharField(max_length=40, blank=True)
    p_trainingOrgFaxEmail = models.CharField(max_length=40, blank=True)
    p_employerFaxEmail = models.CharField(max_length=40, blank=True)

    p_nameOfCourse = models.CharField(max_length=40, blank=True)
    p_isNZQA = models.CharField(max_length=40, blank=True)
    p_courseStartDate = models.DateField(null=True)
    p_courseEndDate = models.DateField(null=True)
    p_courseHoursPerWeek = models.CharField(max_length=40, blank=True)
    p_otherStudyHoursPerWeek = models.CharField(max_length=40, blank=True)
    p_hoursTravelCCtoCourse = models.CharField(max_length=40, blank=True)
    p_isArrangedActivities = models.CharField(max_length=40, blank=True)
    p_activityType = models.CharField(max_length=40, blank=True)
    p_hoursActivity = models.CharField(max_length=40, blank=True)
    p_hoursTravelCCtoActivity = models.CharField(max_length=40, blank=True)
    p_applyForMedicalReasons = models.CharField(max_length=40, blank=True)
    p_medicalDurationExpected = models.CharField(max_length=40, blank=True)
    p_hoursPerWeekNeedCC = models.CharField(max_length=40, blank=True)
    p_incomeWagesSalary = models.CharField(max_length=40, blank=True)
    p_incomePPL = models.CharField(max_length=40, blank=True)
    p_terminationPay = models.CharField(max_length=40, blank=True)
    p_redundancyPay = models.CharField(max_length=40, blank=True)
    p_acc = models.CharField(max_length=40, blank=True)
    p_incomeInsurance = models.CharField(max_length=40, blank=True)
    p_incomeBusiness = models.CharField(max_length=40, blank=True)
    p_incomeSelfEmpContract = models.CharField(max_length=40, blank=True)
    p_incomeInterest = models.CharField(max_length=40, blank=True)
    p_incomeDividends = models.CharField(max_length=40, blank=True)
    p_incomeRental = models.CharField(max_length=40, blank=True)
    p_incomeFlatmates = models.CharField(max_length=40, blank=True)
    p_incomeChildSup = models.CharField(max_length=40, blank=True)
    p_incomeOtherForChild = models.CharField(max_length=40, blank=True)
    p_incomeMaintenance = models.CharField(max_length=40, blank=True)
    p_incomeFormerPartner = models.CharField(max_length=40, blank=True)
    p_incomeStudentAllowance = models.CharField(max_length=40, blank=True)
    p_incomeOverseasPension = models.CharField(max_length=40, blank=True)
    p_incomeSuper = models.CharField(max_length=40, blank=True)
    p_incomeEstate = models.CharField(max_length=40, blank=True)
    p_incomeTrusts = models.CharField(max_length=40, blank=True)
    p_incomeOther = models.CharField(max_length=40, blank=True)
    p_jointPartnerWhere1  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWith1  = models.CharField(max_length=40, blank=True)
    p_jointPartnerYou1  = models.CharField(max_length=40, blank=True)
    p_jointPartnerFreq1  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWhere2  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWith2  = models.CharField(max_length=40, blank=True)
    p_jointPartnerYou2  = models.CharField(max_length=40, blank=True)
    p_jointPartnerFreq2  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWhere3  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWith3  = models.CharField(max_length=40, blank=True)
    p_jointPartnerYou3  = models.CharField(max_length=40, blank=True)
    p_jointPartnerFreq3  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWhere4  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWith4  = models.CharField(max_length=40, blank=True)
    p_jointPartnerYou4  = models.CharField(max_length=40, blank=True)
    p_jointPartnerFreq4  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWhere5  = models.CharField(max_length=40, blank=True)
    p_jointPartnerWith5  = models.CharField(max_length=40, blank=True)
    p_jointPartnerYou5  = models.CharField(max_length=40, blank=True)
    p_jointPartnerFreq5  = models.CharField(max_length=40, blank=True)



    p_other52weeksType1  = models.CharField(max_length=40, blank=True)
    p_other52weeksWhere1  = models.CharField(max_length=40, blank=True)
    p_other52weeksValue1  = models.CharField(max_length=40, blank=True)
    p_other52weeksType2  = models.CharField(max_length=40, blank=True)
    p_other52weeksWhere2  = models.CharField(max_length=40, blank=True)
    p_other52weeksValue2  = models.CharField(max_length=40, blank=True)
    p_other52weeksType3  = models.CharField(max_length=40, blank=True)
    p_other52weeksWhere3  = models.CharField(max_length=40, blank=True)
    p_other52weeksValue3  = models.CharField(max_length=40, blank=True)
    p_other52weeksType4  = models.CharField(max_length=40, blank=True)
    p_other52weeksWhere4  = models.CharField(max_length=40, blank=True)
    p_other52weeksValue4  = models.CharField(max_length=40, blank=True)
    p_other52weeksType5  = models.CharField(max_length=40, blank=True)
    p_other52weeksWhere5  = models.CharField(max_length=40, blank=True)
    p_other52weeksValue5  = models.CharField(max_length=40, blank=True)






























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

