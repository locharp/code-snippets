def get_drink_by_profession( param ):
  
    drinks = { "Jabroni": "Patron Tequila", 
              "School Counselor": "Anything with Alcohol", 
              "Programmer":	"Hipster Craft Beer", 
              "Bike Gang Member": "Moonshine", 
              "Politician":	"Your tax dollars", 
              "Rapper":	"Cristal" }
    
    param = param.title()
    
    if param in drinks:
        return drinks[param]
    else:
        return "Beer"
