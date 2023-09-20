def declare_winner( fighter1, fighter2, first_attacker ):
    if first_attacker == fighter2.name:
        fighter1.health -= fighter2.damage_per_attack
        
    while True:
        if fighter1.health < 1:
            return fighter2.name
        
        fighter2.health -= fighter1.damage_per_attack
        
        if fighter2.health < 1:
            return fighter1.name
        
        fighter1.health -= fighter2.damage_per_attack