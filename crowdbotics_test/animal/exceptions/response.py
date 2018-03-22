from rest_framework import status
from rest_framework.response import Response
from .invalid_serializer import InvalidSerializerDataException


class ExceptionResponse:

    @staticmethod
    def get(ex):
        _status, data, ex_type = status.HTTP_400_BAD_REQUEST, {'code': 400, 'message': 'HTTP 400 Bad Request'}, type(ex)

        if ex_type == InvalidSerializerDataException:
            data['developerMessage'] = ex.errors
        else:
            data['developerMessage'] = str(ex)

        return Response(status=_status, data=data)
