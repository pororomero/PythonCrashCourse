alien_0 = {'color': 'green', 'points': '5'}

#Printing a key-value
print(alien_0['color'])
print(alien_0['points'])

#Accesing values in dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!" )

#Adding a new key-pair values
print(alien_0) 					#<-original
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 					#<-after adding

#Starting an empty dictionary
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = '10'
print(alien_0)

# Modifying Values in a Dictionary - color
alien_0 = {'color': 'green'}
print("The alien is " + str(alien_0['color']) + ".")
alien_0['color'] = 'yellow'
print("The alien is " + str(alien_0['color']) + ".")

# Modifying Values in a Dictionary - x_position
alien_0 = {'x_position': '0', 'y_position': '25', 'speed': 'medium'}
print("Original x-position: " + alien_0['x_position'])
# Move the alien to the right.
# Determine how far the move the alien based on its current speed.
#alien_0['speed'] = 'edit here' <- effectively implement change speed
if alien_0['speed'] == 'slow':
	x_increment = 1 
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3
# The new position is the old position + the increment
alien_0['x_position'] = int(alien_0['x_position']) + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Removing ke-value pairs
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)
del alien_0['points']
print(alien_0)
