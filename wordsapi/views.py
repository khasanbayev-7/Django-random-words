from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import WordRequestSerializer
from random_word import RandomWords


@api_view(['POST'])
def random_words_view(request):
    serializer = WordRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    count = serializer.validated_data['count']
    letter = serializer.validated_data['letter']

    rw = RandomWords()
    words = []
    trials = 0
    is_upper = letter.isupper()

    while len(words) < count and trials < 200:
        trials += 1
        word = rw.get_random_word()

        if (
            isinstance(word, str)
            and len(word) > 0
            and word[0].lower() == letter.lower()
            and word not in words
        ):
            word = word.capitalize() if is_upper else word.lower()
            words.append(word)

    if len(words) < count:
        return Response(
            {"detail": f"Yetarli so'z topilmadi. Topilgan: {len(words)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    return Response(
        data={"result": " ".join(words)},
        status=status.HTTP_200_OK
    )
