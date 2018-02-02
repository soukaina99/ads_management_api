# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Ad, UserAd
from .serializers import UserAdserializer


class AdsManagmentViewApi(viewsets.GenericViewSet,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin):
    serializer_class = UserAdserializer
    permission_classes = (IsAuthenticated,)

    parser_classes = (FormParser, MultiPartParser, JSONParser)

    # an endpoint to deal with user ads operation(retrieve,create,destroy)

    def retrieve(self, request, pk=None):
        pk = self.kwargs.get('pk', None)
        data = {}
        if pk == 'current':
            data = UserAdserializer(request.user).data
        return Response(data)

    def create(self, request, *args, **kwargs):
        data = request.data
        ad_type = data.get('ad_type')
        ad_id = data.get('ad_id') or None
        try:
            ad = Ad.objects.get(pk=ad_id)
        except ObjectDoesNotExist:
            return Response(
                {'message': 'No ad found with provided id!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        ad_type = UserAd.AUTO_SAVE if ad_type == 'auto' else UserAd.MANUAL_SAVE
        UserAd.objects.get_or_create(ad=ad, user=request.user, defaults={'ad_type': ad_type})
        return HttpResponse(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            ad_id = self.kwargs.get('pk', None)
            UserAd.objects.get(user=request.user, ad__pk=ad_id).delete()
        except ObjectDoesNotExist:
            return Response(
                {'message': 'No ad found with provided id!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return HttpResponse(status=status.HTTP_200_OK)
