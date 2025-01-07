import math





while True:
    user_input = input('what is your initial expense or type stop to end -> ')
    if user_input.lower() == 'stop':
        print('program ended')
        break

    try:
        c0 = int(user_input)
    except ValueError:
        print("Invalid Input. Please enter a number.")
        continue


    ###Initialize balances and values###
    ########################
    f0 = 100000  ## Inital Bank balance

    n = 12  ## number of years to survive

    i = 1.011  ## the percent of expenses that coumponds every year.. so each year his expenses increases 10%

    p = 1.01  ## the percent of interest he earns each year so 1%
    #########################

    for year in range(n):
        
        inital_balance = f0
        year_expense = c0
        f0 = f0 - c0  ## withdrawing expenses 
        end_balance = f0

        f0 = math.ceil(f0 * p)  ## adding his interest he accumulated that year

        c0 = math.ceil(c0 * i) ## Coumpounding expenses by 10%

        print('year: ' + str(year + 1) + ' expense ' + str(year_expense) + ' ------------- intital year ' + str(year+1) + ' balance: ' + str(inital_balance) + ' end year '+ str(year+1) + ' balance: ' + str(end_balance))


