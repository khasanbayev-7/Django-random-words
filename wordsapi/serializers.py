from rest_framework import serializers

class WordRequestSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=1)
    letter = serializers.CharField(max_length=1)

    def validate_letter(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Harf faqat 1 alifbodagi belgidan bolishi kera.")
        return value
