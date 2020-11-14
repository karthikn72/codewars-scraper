def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health>0 and fighter2.health>0:
      if fighter1.name==first_attacker:
        fighter2.health-=fighter1.damage_per_attack
        first_attacker = fighter2.name
      else:
        fighter1.health-=fighter2.damage_per_attack
        first_attacker = fighter1.name

    return [fighter1.name,fighter2.name][int(first_attacker==fighter1.name)]
        