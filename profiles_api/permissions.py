from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiel"""
    def has_object_permission(self, request, view, obj):
        """check user is trying to edit thier own profile"""
        # print("he",obj.id, request.user.id)
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """check update ther own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update thier own status"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id

class UpdateProduct(permissions.BasePermission):
    """check update ther own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update thier own status"""
        # print("hehe", obj.user_profile.is_staff, request.user.is_staff)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff == True