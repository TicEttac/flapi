from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Score
from .serializers import scoreSerializer

@api_view(['GET'])
def getLeaderboard(request):
    scores = Score.objects.order_by('-score')[:50]
    serializer = scoreSerializer(scores, many=True)
    return Response(serializer.data)


def check_score(score_dict):
    scores_list = Score.objects.all()
    pipe_list = score_dict['pipe_passed']
    if score_dict['score'] != len(score_dict['pipe_passed']) or score_dict['score'] <= 0 or len(score_dict['pipe_passed']) <= 0:
        return False
    #secret key algo
    key = score_dict['death'] + pipe_list[0] / 3
    if round(score_dict['key'],1) != round(key,1):
        print("Wrong key : ", str(score_dict["key"]), " expected : ", key)
        return False
    return True


@api_view(['POST'])
def submitScore(request):
    score_dict = request.data
    existing_score = Score.objects.filter(pseudo=score_dict['pseudo']).first()
    if existing_score and existing_score['score'] <= score_dict['score']:
        serialized_score = scoreSerializer(existing_score)
        return Response(serialized_score.data)
    if check_score(score_dict):
        validated_score = Score(pseudo=score_dict['pseudo'], score=score_dict['score'])
            
        validated_score.save()
        serialized_score = scoreSerializer(validated_score)
        return Response(serialized_score.data)
    return Response(status=400)
        
