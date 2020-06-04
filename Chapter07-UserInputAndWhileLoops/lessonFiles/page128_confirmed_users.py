# Start with users that need to be verified,
#  and an empty list ot hold confirmed_usrs.
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = [ ]

# Verify each users until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("verified users: " + current_user.title())
	confirmed_users.append(current_user)
# Dispay all confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
