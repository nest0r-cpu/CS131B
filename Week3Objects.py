# Population data of the permanent members of the UN Security Council
unitedstates_population = 345426571
china_population = 1419321278
russia_population = 144820423
unitedkingdom_population = 69138192
france_population = 66548530


# Current world population
global_population = 8179234807  

# Calculating the total population of the permanent members
permanent_members_population = ( unitedkingdom_population + unitedstates_population + russia_population + china_population +france_population)

# Calculating the portion of the global population represented by permanent members
portion_of_global_population = permanent_members_population / global_population

# Output
print(f"About {portion_of_global_population * 100}% of the global population is represented by the five permanent members of the UN Security Council.")

# Sources:
# https://main.un.org/securitycouncil/en/content/current-members (This is where I found out who were the 5 permanent members)
# https://www.worldometers.info/world-population/  (Got the Data of the current population)
