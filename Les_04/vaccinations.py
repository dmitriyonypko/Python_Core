"""
Task 3:
Vaccinations for children under 5
You have been put in charge of administrating vaccinations for children in your local area.
Write a function that will generate a list of vaccines for each child presented for vaccination,
based on the child's age and vaccination history, and the month of the year.

The function takes three parameters: age, status and month
The parameter 'age' will be given in weeks up to 16 weeks, and thereafter in months.
You can assume that children presented will be scheduled for vaccination (eg '16 weeks', '12 months' etc).
The parameter 'status' indicates if the child has missed a scheduled vaccination,
and the argument will be a string that says 'up-to-date',
or a scheduled stage (eg '8 weeks') that has been missed, in which case you need to add any missing shots to the list.
Only one missed vaccination stage will be passed in per function call.
If the month is 'september', 'october' or 'november' add 'offer fluVaccine' to the list.
Make sure there are no duplicates in the returned list, and sort it alphabetically.
Example input and output
input     ('12 weeks', 'up-to-date', 'december')
output    ['fiveInOne', 'rotavirus']

input     ('12 months', '16 weeks', 'june')
output     ['fiveInOne', 'hibMenC', 'measlesMumpsRubella', 'meningitisB', 'pneumococcal']

input     ('40 months', '12 months', 'october') 
output    ['hibMenC', 'measlesMumpsRubella', 'meningitisB', 'offer fluVaccine', 'preSchoolBooster']

To save you typing it up, here is the vaccinations list
fiveInOne : ['8 weeks', '12 weeks', '16 weeks'],
//Protects against: diphtheria, tetanus, whooping cough, polio and Hib (Haemophilus influenzae type b)
pneumococcal : ['8 weeks', '16 weeks'],
//Protects against: some types of pneumococcal infection
rotavirus : ['8 weeks', '12 weeks'],
//Protects against: rotavirus infection, a common cause of childhood diarrhoea and sickness
meningitisB : ['8 weeks', '16 weeks', '12 months'],
//Protects against: meningitis caused by meningococcal type B bacteria
hibMenC : ['12 months'],
//Protects against: Haemophilus influenzae type b (Hib), meningitis caused by meningococcal group C bacteria    
measlesMumpsRubella : ['12 months', '40 months'],
//Protects against: measles, mumps and rubella
fluVaccine : ['september','october','november'],
//Given at: annually in Sept/Oct
preSchoolBooster : ['40 months']
//Protects against: diphtheria, tetanus, whooping cough and polio
"""


age = input("Enter the age: ").lower()
status = input("Enter the missed vaccine: ").lower()
month = input("Enter the month: ").lower()


def vaccinations(age, status, month):
    """Generate a list of vaccines."""
    
    vaccinations_list = []
    parameters_list = [age, status, month]
    scheduled_list = ['8 weeks', '12 weeks', '16 weeks', '12 months', '40 months'] # нужно для параметра 'up-to-date'
    dict_vac = { 'fiveInOne': ['8 weeks', '12 weeks', '16 weeks'],
                 'pneumococcal': ['8 weeks', '16 weeks'],
                 'rotavirus': ['8 weeks', '12 weeks'],
                 'meningitisB': ['8 weeks', '16 weeks', '12 months'],
                 'hibMenC': ['12 months'],
                 'measlesMumpsRubella': ['12 months', '40 months'],
                 'offer fluVaccine': ['september','october','november'],
                 'preSchoolBooster': ['40 months']}
    # convert param 'up-to-date' to last scheduled period
    status = age if status == 'up-to-date' and age == '8 weeks' else scheduled_list[scheduled_list.index(age) - 1]
    # add vaccinations_list
    for param in parameters_list:
        for vaccination in dict_vac:
            if param in dict_vac[vaccination]:
                if vaccination not in vaccinations_list:
                    vaccinations_list.append(vaccination)
    vaccinations_list.sort()
    return vaccinations_list


print(vaccinations(age, status, month))
