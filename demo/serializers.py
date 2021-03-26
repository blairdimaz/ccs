from rest_framework import serializers
# from .models import Book, BookNumber, Character,Author
from .models import ccsFormData



# class BookNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookNumber
#         fields = ['id','isbn_10', 'isbn_13']
#
# class CharacterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Character
#         fields = ['id','name']
#
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id','name', 'surname']

class ccsSerializer(serializers.ModelSerializer):
    # number = BookNumberSerializer(many=False)
    # characters = CharacterSerializer(many=True)
    # authors = AuthorSerializer(many=True)


    class Meta:
        model = ccsFormData
        fields = ['id','name', 'surname','email',
                  'phone']
