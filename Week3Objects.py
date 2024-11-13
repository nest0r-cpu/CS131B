#Population Data
Los_Angeles = 9606925
San_Francisco = 788478
#Supervisors Data
LA_Supervisors = 5
SF_Supervisors = 11
# Average age people represented using integer division 
AVG_LA_People_Represented_by_Supervisors_LA = Los_Angeles // LA_Supervisors
AVG_SF_People_Represented_by_Supervisors_SF = San_Francisco // SF_Supervisors
# Combined AVG and rounded 
AVG_LA_AND_SF_People_Per_Supervisor = round(AVG_LA_People_Represented_by_Supervisors_LA + AVG_SF_People_Represented_by_Supervisors_SF) /2
# Output 
print(f"Average number of people represented by a supervisor in Los Angeles: {AVG_LA_People_Represented_by_Supervisors_LA:.0f}")
print(f"Average number of people represented by a supervisor in San Francisco: {AVG_SF_People_Represented_by_Supervisors_SF:.0f}")
print(f"Overall average number of people represented by a supervisor in both counties: {AVG_LA_AND_SF_People_Per_Supervisor:.0f}")

#Source's 
# https://worldpopulationreview.com/us-counties/california/los-angeles-county 
# https://worldpopulationreview.com/us-cities/california/san-francisco
# https://bos.lacounty.gov/executive-office/about-us/board-of-supervisors/
# https://sfbos.org/
