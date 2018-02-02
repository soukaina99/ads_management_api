# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import UserAd, Ad, User


class AdSerializer(serializers.ModelSerializer):
    # serializer class to get user ads by type as json format
    class Meta:
        model = Ad
        fields = ('id','title', 'image', 'description')


class UserAdserializer(serializers.Serializer):
    list_ads = serializers.SerializerMethodField()

    def get_list_ads(self, obj):
        auto_ads = manual_ads = []
        ads = obj.userad_set.all()
        if ads:
            auto_ads = AdSerializer([item.ad for item in ads.filter(ad_type=UserAd.AUTO_SAVE)], many=True).data
            manual_ads = AdSerializer([item.ad for item in ads.filter(ad_type=UserAd.MANUAL_SAVE)], many=True).data
        return {'auto_ads': auto_ads, 'manual_ads': manual_ads}

    class Meta:
        fields = ('list_ads',)
