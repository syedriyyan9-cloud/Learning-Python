# Date: 19 november 2025
# Name: Riyyan

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a sepa-
# rate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.

from User_Privileges_Admin import User, Admin, Privileges

admin = Admin("Riyyan","Hassan")
admin.privileges.show_privileges()