def BMIcal(feet, inches, weight, bmi, category):

    feet_in_inches = (feet * 12)
    height = (feet_in_inches + inches)

    m_height = (height * .025)
    print(m_height)

    m_weight = (weight * .45)
    print(m_weight)

    height_squared = float(m_height * m_height)
    bmi = (m_weight/height_squared)

    if bmi <= 18.5:
        category = ' weight category: Underweight'

    if 18.5 < bmi <= 24.9:
        category = ' weight category: Normal weight'

    if 25 <= bmi <= 29.9:
        category = ' weight category: Overweight'

    if bmi > 29.9:
        category = ' weight category: Obese'

    return bmi, category



def retirementCal(age, salary, percentageSaved, savingsGoal, savingsS):

    i=int(0)
    saving=int(0)
    boss_match=.35
    while i<=(100-age):

        saving=float((salary*(percentageSaved/100))+saving)
        bonus=((salary*(percentageSaved/100))*.35)
        saving=saving+bonus
        age+=1

        if saving>=savingsGoal:
            saving=str(saving)
            age=str(age)
            savingsGoal=str(savingsGoal)
            savingsS=("You will save: $"+saving+" by "+age+" which meets your saving's goal of $"+savingsGoal+"")
            return savingsS
        i=int(101)
