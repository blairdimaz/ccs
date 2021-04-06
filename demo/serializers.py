from rest_framework import serializers
# from .models import Book, BookNumber, Character,Author
from .models import ccsFormData
# from .models import Child

# class childSerializer(serializers.ModelSerializer):
#     # number = BookNumberSerializer(many=False)
#     # characters = CharacterSerializer(many=True)
#     # authors = AuthorSerializer(many=True)
#
#
#     class Meta:
#         model = Child
#         fields = ['childName']

class ccsSerializer(serializers.ModelSerializer):
    # number = BookNumberSerializer(many=False)
    # characters = CharacterSerializer(many=True)
    # authors = AuthorSerializer(many=True)


    class Meta:
        model = ccsFormData
        fields = ['id',
                  'clientNumber',
                  'firstName','lastName',
                  'firstNameNOTsame', 'lastNameNOTsame',
                  'nameOtherKnown' ,
                  'dob',
                  'gender',
                  'irdNumber',
                  'flatHouseNum',
                  'streetName',
                  'suburb',
                  'townCity',
                  'mailingAddr',
                  'homePhone',
                  'mobPhone',
                  'otherPhone',
                  'getEmails',
                  'ethnicity',
                  'usuallyNZ',
                  'residenceStatus',
                  'dateGranted',
                  'dateArrived',
                  'countryOfBirth',
                  'ccAssistanceReason',
                  'isWorking',
                  'employerName',
                  'employerAddr',
                  'employerPhone',
                  'employerFaxEmail',
                  'hoursPerWeek',
                  'hoursTravel',
                  'isWorkRelatedCourse',
                  'trainingOrgName',
                  'trainingOrgAddr',
                  'trainingOrgPhone',
                  'trainingOrgFaxEmail',
                  'employerFaxEmail',
                  'nameOfCourse',
                  'isNZQA',
                  'courseStartDate',
                  'courseEndDate',
                  'courseHoursPerWeek',
                  'otherStudyHoursPerWeek',
                  'hoursTravelCCtoCourse',
                  'isArrangedActivities',
                  'activityType',
                  'hoursActivity',
                  'hoursTravelCCtoActivity',
                  'applyForMedicalReasons',
                  'medicalDurationExpected',
                  'hoursPerWeekNeedCC',
                  'incomeWagesSalary',
                  'incomePPL',
                  'terminationPay',
                  'redundancyPay',
                  'acc',
                  'incomeInsurance',
                  'incomeBusiness',
                  'incomeSelfEmpContract',
                  'incomeInterest',
                  'incomeDividends',
                  'incomeRental',
                  'incomeFlatmates',
                  'incomeChildSup',
                  'incomeOtherForChild',
                  'incomeMaintenance',
                  'incomeFormerPartner',
                  'incomeStudentAllowance',
                  'incomeOverseasPension',
                  'incomeSuper',
                  'incomeEstate',
                  'incomeTrusts',
                  'incomeOther'
                  ]
