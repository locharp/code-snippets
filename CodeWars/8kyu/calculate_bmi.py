def bmi( weight, height ):
    bmi = weight / ( height * height )
    
    if bmi > 30:
        return "Obese"
    elif bmi > 25:
        return "Overweight"
    elif bmi > 18.5:
        return "Normal"
    else:
        return "Underweight"