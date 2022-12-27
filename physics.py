# an application that calculates the force between force between charges
import math
print("This application calculates for missing paramters in Coulomb's law")

print("---------------------------")
print("Provide only numbers.")
print("Use e for exponents 10")
print("provide an empty space for the unknown parameter")
print("---------------------------")
print("Distances are in metres")
print()
print('---------------------------')
print('Forces are in Newton')
print("---------------------------")
print('charges are in coulomb')

param_obj={
  'force':" ",
  'charge_one':" ",
  'charge_two':" ",
  'distance':" "
}
coulomb_constant=9e9
computed_value=" "
count=0

for key in param_obj.keys():
  try:
    param_obj[key]=float(input("Enter value of {}:  ".format(key)))
  except ValueError as error:
    param_obj[key]=" "
    computed_value=key
  
  
def compute_parameter_value():
  if computed_value=='force':
    force=(coulomb_constant*param_obj['charge_one']*param_obj['charge_two'])/(param_obj['distance']**2)
    print("The value of the force in N is",force)
    return 0
  if computed_value=='distance':
    distance_square=(coulomb_constant*param_obj['charge_two']*param_obj['charge_one'])/(param_obj["force"])
    distance=math.sqrt(distance_square)
    print('The value of the distance in m is : ',distance)
    return 0
  if computed_value=="charge_one" or computed_value=="charge_two":
    distance_square=param_obj['distance']**2
    forcex_distance=(param_obj['distance']*param_obj["force"])
    charge=(forcex_distance*distance_square)/(coulomb_constant*distance_square)
    print("The value of charge in C is: ",charge)
    return 0
  else:
    print(count)
    return 0
    
    
compute_parameter_value()
    
    
  
    
    
    
  
  



		