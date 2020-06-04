def make_car(manufacturer, model_name, **additional_info):
	info = {}
	info['manufacturer'] = manufacturer
	info['model_name'] = model_name
	for key, value in additional_info.items():
		info[key] = value
	return info

car = make_car('subaru', 'outback', 
				color = 'blue', 
				tow_package = True)
print(car)
