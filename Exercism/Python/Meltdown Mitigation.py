def is_criticality_balanced( temperature, neutrons_emitted ):
    
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000



def reactor_efficiency( voltage, current, theoretical_max_power ):
    
    power_efficiency = 100 * voltage * current / theoretical_max_power

    if power_efficiency < 30:
        return "black"
    
    if power_efficiency < 60:
        return "red"
    
    if power_efficiency < 80:
        return "orange"
    
    return "green"



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    if output < 0.9:
        return "LOW"
    
    if output <= 1.1:
        return "NORMAL"
    
    return "DANGER"
