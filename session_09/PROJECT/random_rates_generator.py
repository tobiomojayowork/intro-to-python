
import datetime, random, os

# FILE AND DIRECTORY PATHS
#----------------------------------------------------------------
DATAFOLDER = "DATA"
OUTPUTFOLDER = os.path.join(DATAFOLDER, "OUTPUT")

#RATETYPEFILEPATH = "rate_types.txt"
RATEGROUPFILEPATH = os.path.join(DATAFOLDER, "rate_groups.txt")
CURRENCYFILEPATH = os.path.join(DATAFOLDER, "my_currencies.txt")

OUTPUTCLIENRATESTFILEPATH = os.path.join(OUTPUTFOLDER, "random_client_rates.csv")
OUTPUTCONSTANTRATESFILEPATH = os.path.join(OUTPUTFOLDER, "random_const_rates.csv")


# OUTPUT GENERATOR
# Output List 
#----------------------------------------------------------------
outputRates = {
    "constant": [],
    "client": []
}


# Rate types
#----------------------------------------------------------------
rate_types = ("Constant", "Day", "BalanceSheet", "ProfitAndLoss")


# Rate groups [USER CHECK/PROMPT #1]
#----------------------------------------------------------------
def LoadRateGroups():
    global rate_groups
    
    rate_groups = []

    f = open(RATEGROUPFILEPATH)

    for group in f:
        rate_groups.append(group.rstrip("\n"))

    f.close()

    rate_groups = tuple(rate_groups)

    #print(rate_groups)


# CURRENCIES  [USER CHECK/PROMPT #2]
# ensure currencies specified here matches what is in the database
#----------------------------------------------------------------

def LoadCurrencies():
    global currencies

    currencies = []

    f = open(CURRENCYFILEPATH)

    for curr in f:
        currencies.append(curr.rstrip("\n"))

    f.close()

    #print(currencies)


# Random Date generation
#----------------------------------------------------------------
def SetRandomDateConfig():
    global cfg   

    year = datetime.datetime.now().year
    startMonth = datetime.datetime.now().month
    startDay = datetime.datetime.now().day    

    randomOption = random.randint(0, 400)

    if randomOption > 300: year = random.randint(2017, datetime.datetime.now().year)
    if randomOption > 200: startMonth = random.randint(1, 12)
    if randomOption > 100: startDay = GetRandomDay(startMonth, year)
    maxDayInterval = randomOption

    cfg = { 
        "globalStartDate" : datetime.date(year, startMonth, startDay), 
        "globalMaxDayInterval": maxDayInterval
    }

def GetRandomDay(month, year):
    if month in [9, 4, 6, 11]:
        return random.randint(1, 30)
    elif month == 2 and year % 4 == 0:
        return random.randint(1, 29)
    elif month == 2:
        return random.randint(1, 28)
    else:
        return random.randint(1, 31)
    

def CreateStartDate():
    #random date
    randomDayInterval = random.randint(0, cfg["globalMaxDayInterval"])
    return cfg["globalStartDate"] + datetime.timedelta(days=randomDayInterval)

def CreateDateRange():
    #random date range
    date_start = CreateStartDate()
    return [ 
        date_start,
        date_start + datetime.timedelta(days=random.randint(0, cfg["globalMaxDayInterval"]))
    ]





    
def GetRateGroup(avoidDefault=None):
    # ensure all rates data and settings specified here matches what is in the database
    rate_group = random.choice(rate_groups)

    # the KPMG Default rate group is restricted to the Constant rate
    # for simplicity and ease of exclusion, ensure this group is the first element
    if avoidDefault:
        while rate_group == rate_groups[0]:
            rate_group = random.choice(rate_groups) 
    return rate_group


# RANDOM Currency Rate creators
#----------------------------------------------------------------
def GetCurrencyPair():
    currFrom = random.choice(currencies)
    currTo = random.choice(currencies) 
    # could make the rates plausible based on the currency pair
    # for now, make it completely random rates
    rate = float("{:.4f}".format(random.random() * random.randint(1, 100)))

    while currFrom == currTo:
        currTo = random.choice(currencies) 
    
    return [currFrom, currTo, rate]



def CreateRate(rateFields):
    currFrom, currTo, dateStart, dateEnd, rateType, rate, rateGroup = rateFields

    return {
        "CurrFrom": currFrom,
        "CurrTo": currTo,
        "StartDate": dateStart,
        "EndDate": dateEnd,
        "RateType": rateType,
        "Rate": rate,
        "RateGroup": rateGroup
    }    

def CreateDayRate(currFrom, currTo, rate):
    # MUST have the same start and end date
    date_start = CreateStartDate()

    return CreateRate([
        currFrom,
        currTo,
        date_start,
        date_start,
        random.choice([rate_types[1], rate_types[2]]),
        rate,
        GetRateGroup(True)
    ])
    


def CreateProfitAndLossRate(currFrom, currTo, rate):
    date_start, date_end = CreateDateRange()

    # only add rate pair if it does not already exist - at least in our output
    # because of contiguous date error

    return CreateRate([
        currFrom,
        currTo,
        date_start,
        date_end,
        rate_types[3],
        rate,
        GetRateGroup(True)
    ])

def CreateConstantRate(currFrom, currTo, rate):
    # date NOT REQUIRED for constant rates
    # must output on separate sheet

    # only add rate pair if it does not already exist - at least in our output

    return CreateRate([
        currFrom,
        currTo,
        None,
        None,
        rate_types[0],
        rate,
        GetRateGroup()
    ])

# Validators
#----------------------------------------------------------------
def RatePairExists(sourceKey, rateToFind):
    for rate in outputRates[sourceKey]:
        if rateToFind["CurrFrom"]==rate["CurrFrom"] and rateToFind["CurrTo"]==rate["CurrTo"] and rateToFind["RateType"]==rate["RateType"]:
            return True
    
    return False

# PROGRAM START 
#----------------------------------------------------------------
#----------------------------------------------------------------


LoadCurrencies()
LoadRateGroups()





#Set Year Month Date parameters for random dates generation
SetRandomDateConfig()


# GENERATE Random Currency Rates 
rateCount = 200
randomiseDateInterval = 5

while rateCount != 0:
    currFrom, currTo, rate = GetCurrencyPair()

    actionIndex = random.randint(1,4)

    newrate = None

    if actionIndex == 2: 
        newrate = CreateProfitAndLossRate(currFrom, currTo, rate)

        if not RatePairExists("client", newrate):
            outputRates["client"].append(newrate)
        else: 
            print(f'rate {newrate["CurrFrom"]} - {newrate["CurrTo"]} ({newrate["RateType"]}) already exists, will not be added')
            actionIndex = 3

    if actionIndex == 3: 
        newrate = CreateConstantRate(currFrom, currTo, rate)

        if not RatePairExists("constant", newrate):
            outputRates["constant"].append(newrate)
        else: 
            print(f'rate {newrate["CurrFrom"]} - {newrate["CurrTo"]} ({newrate["RateType"]}) already exists, will not be added')
            actionIndex = 1

    if actionIndex == 1: 
        newrate = CreateDayRate(currFrom, currTo, rate)
        outputRates["client"].append(newrate)

    if actionIndex == 4: SetRandomDateConfig()

    if actionIndex != 4: rateCount-=1




# OUTPUT FILES:
fclient = open(OUTPUTCLIENRATESTFILEPATH, "w" )

fclient.write("CurrFrom,CurrTo,StartDate,EndDate,RateType,Rate,RateGroup")
for rate in outputRates["client"]:
    fclient.write(f'\n{rate["CurrFrom"]},{rate["CurrTo"]},{rate["StartDate"]},{rate["EndDate"]},{rate["RateType"]},{float(rate["Rate"])},{rate["RateGroup"]}')

fclient.close()

fconst = open(OUTPUTCONSTANTRATESFILEPATH, "w")
fconst.write("CurrFrom,CurrTo,RateType,Rate,RateGroup")
for rate in outputRates["constant"]:
    fconst.write(f'\n{rate["CurrFrom"]},{rate["CurrTo"]},{rate["RateType"]},{float(rate["Rate"])},{rate["RateGroup"]}')

fconst.close()



# PROGRAM END  
#----------------------------------------------------------------
#----------------------------------------------------------------


TEST OUTPUT IN CURRENCYAPP