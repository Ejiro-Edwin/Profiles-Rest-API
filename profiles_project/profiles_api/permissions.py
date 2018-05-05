from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows users to edit own profile"""
    def has_object_permission(self, request, view, obj):
        """check if user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permissions(self,request,view,obj):
        """checks the user is trying to update their own status"""

        if request.methos in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
        """checks if the users status id matches the user that is logged in"""