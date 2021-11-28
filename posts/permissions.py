from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'ris uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # tahrirlash uchun ruxsatnoma faqatgina post muallifigagina beriladi
        return obj.author == request.user
