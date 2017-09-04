from rest_framework import serializers
from onlineapp.models import College,Student,MockTest1, LANGUAGE_CHOICES, STYLE_CHOICES


'''class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'acronym', 'location', 'contact')'''

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'college')

class MockTest1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('id', 'problem1', 'problem2', 'problem3', 'problem4','total','student')

class CollegeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    acronym = serializers.CharField(required=False, allow_blank=True, max_length=100)
    location = serializers.CharField(required=False, allow_blank=True, max_length=100)
    contact = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('title', instance.id)
        instance.name = validated_data.get('code', instance.name)
        instance.acronym = validated_data.get('linenos', instance.acronym)
        instance.location = validated_data.get('language', instance.location)
        instance.contact = validated_data.get('style', instance.contact)
        instance.save()
        return instance

