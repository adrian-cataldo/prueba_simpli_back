from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models.query import QuerySet

"""
Adds urls for soft-deleted elements, returns deleted_at
Example for centers:
    (get)   api/centers/trashed/       -> trashed elements, paginated
    (get)   api/centers/4/get-trashed/ -> get trashed element
    (patch) api/centers/4/restore/     -> restore trashed element
"""
class SoftDeleteViewSet(viewsets.ViewSet):

    def full_queryset(self, queryset):
        return queryset.all()

    def get_queryset(self):
        return self.full_queryset(self.queryset)

    @action(detail=True, methods=['PATCH'])
    def restore(self, request, *args, **kwargs):
        self.queryset = self.full_queryset(self.querysetTrashed)
        instance = self.get_object()
        instance.restore()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], url_path='get-trashed')
    def getTrashed(self, request, *args, **kwargs):
        self.queryset = self.full_queryset(self.querysetTrashed)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if serializer.Meta.fields!=('__all__'):
            serializer.Meta.fields += ('deleted_at', )
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def trashed(self, request, *args, **kwargs):
        queryset = self.full_queryset(self.querysetTrashed)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            if serializer.child.Meta.fields!=('__all__'):
                serializer.child.Meta.fields += ('deleted_at', )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        if serializer.child.Meta.fields!=('__all__'):
            serializer.child.Meta.fields += ('deleted_at', )
        return Response(serializer.data)
