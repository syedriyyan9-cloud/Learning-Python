# Date: 19 november 2025
# Name: Riyyan

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

from Admin_Privileges import Admin

admin = Admin("Syed", "hassan")
admin.privileges.show_privileges()