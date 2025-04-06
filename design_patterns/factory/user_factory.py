"""
User Factory Example - Demonstrating the Factory Design Pattern with User Roles

This script defines a simple user permission system using the Factory Design Pattern.

Key Components:
1. `User` - Abstract base class that requires subclasses to implement `get_permissions()`.
2. `Admin`, `Editor`, and `Viewer` - Concrete subclasses representing different user roles.
   - Each implements `get_permissions()` to return role-specific permissions.
   - The output includes both the user's name and a list of allowed actions.
3. `UserFactory` - Contains a method `create_user()` to instantiate a user object based on role.
   - Supports dynamic creation of Admin, Editor, or Viewer objects.

Usage:
- Create users by specifying their role and name using the factory.
- Call `get_permissions()` to retrieve the permissions for a user.

This structure provides a clean separation of roles and logic, making it easy to manage permissions 
and user creation from a central place.

Example output:
{
  'userName': 'Admin', 
  'permissions': ['create', 'read', 'update', 'delete']
}
"""

class User:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        raise NotImplementedError

class UserFactory:
    def create_user(self, role, name):
        if(role == 'admin'):
            return Admin(name)
        if(role == 'editor'):
            return Editor(name)
        if(role == 'viewer'):
            return Viewer(name)

class Admin(User):
    def get_permissions(self):
        return {
            "userName": self.name,
            "permissions": ["create", "read", "update", "delete"]
        }
        return ["create", "read", "update", "delete"]

class Editor(User):
    def get_permissions(self):
        return {
            "userName": self.name,
            "permissions": ["read", "update"]
        }

class Viewer(User):
    def get_permissions(self):
        return {
            "userName": self.name,
            "permissions": ["read"]
        }
    
admin = UserFactory().create_user('admin','Admin')
editor = UserFactory().create_user('editor','Editor')
viewer = UserFactory().create_user('viewer','Viewer')

print(admin.get_permissions())
print(editor.get_permissions())
print(viewer.get_permissions())