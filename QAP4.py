# Description: Program for One Stop Insurance Company 
#         Used to enter and calculate new Insurance Policy
# Author:            Walid Jerjawi
# Dates:       July 16, 2024 - July 20, 2024


# Define required libraries.
import datetime
import time
import sys


# Define program constants.

PROV_LIST = ['ON', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'PE', 'NL', 'YT', 'NT', 'NU']
PAY_METHOD_LST = ["Full", "Monthly", "Down Pay"]
LIABILITY_MAX = 1000000.00
NUM_PAYMENT=8

f = open('Const.dat', 'r')
POLICY_NO = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DISC_RATE = float(f.readline())
LIAB_COVRG_COST = float(f.readline())
GLASS_COVRG_COST = float(f.readline())
LOANER_COVRG_COST = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PAY_FEE = float(f.readline())

f.close()



# Define program functions.

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()



def current_and_next_month_date():
    current_date = datetime.date.today()
    if current_date.month == 12:
        next_month_date = datetime.date(current_date.year + 1, 1, 1)
    else:
        next_month_date = datetime.date(current_date.year, current_date.month + 1, 1)
    return current_date.strftime('%d-%b-%Y'), next_month_date.strftime('%d-%b-%Y')



def calculate_extra_cost(Liability, GlassCoverage, LoanerCar, InsuredCars):
    ExtraCost = 0
    if Liability == "Y":
        ExtraCost += LIAB_COVRG_COST * InsuredCars

    if GlassCoverage == "Y":
        ExtraCost += GLASS_COVRG_COST * InsuredCars

    if LoanerCar == "Y":
        ExtraCost += LOANER_COVRG_COST * InsuredCars

    return ExtraCost

# Function to format a number to $#,###.##
def FNumber2(Value):
    ValueStr = "${:,.2f}".format(Value)
    return ValueStr



while True:
    
# Gather user inputs.

    # Validate First name of the customer.
    while True:
        CustFirst=input("Enter Customer first name: ").title()

        if CustFirst=="":
            print("   Data Entry Error - customer first name cannot be blank.")
        elif CustFirst.isalpha()==False:
            print("  Data Entry Error - Customer first name must be alphapetic.")
        else:
            break


    # Validate the last name of the customer 
    while True:
        CustLast=input("Enter Customer last name : ").title()

        if CustLast=="":
            print("   Data Entry Error - customer family name cannot be blank.")
        elif CustLast.isalpha()==False:
            print("  Data Entry Error - Customer family name must be alphapetic.")
        else:
            break


    
    StreetAd = input("Enter street address: ").title()
    City = input("Enter city: ").title()

    
    # Validate the Province
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("  Data Entry Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("  Data Entry Error - Province is a 2 digit code.")
        elif Prov not in PROV_LIST:
            print("  Data Entry Error - Not a valid province.")
        else:
            break


    PostalCode = input("Enter postal code (XXXXXX): ").upper()

    #Validate the phone number
    while True:
        PhoneNum=input("Enter the phone number (9999999999):  ")

        if PhoneNum=="":
            print("   Data Entry Error - phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("   Data Entry Error - phone number must be 10 digits.")
        elif PhoneNum.isdigit()==False:
            print("  Data Entry Error - Phone Number contains invalid characters.")
        else:
            break


    InsuredCars=int(input("Enter the number of cars being Insured: "))
    
    
    Liability= input("Do you want to add liability ( Y/N )? ").upper()

    GlassCoverage= input("Do you want to add Glass coverage ( Y/N )? ").upper()

    LoanerCar=input("Do you want to add loaner car covarage( Y/N )? ").upper()


    #Validate Payment method
    while True:
        PayMethod= input("How would you like to pay (Full, Monthly or Down Pay)? ").title()
        if PayMethod == "":
            print("  Data Entry Error - ayMethod cannot be blank.")
        elif PayMethod not in PAY_METHOD_LST:
            print("  Data Entry Error - Not a valid PayMethod.")
        else:
            if PayMethod=="Down Pay":
                DownPayAmnt=float(input("Enter Down payment amount: "))
            else:
                DownPayAmnt = 0
            break


    # Initialize claim lists
    ClaimLst = []
    DateLst = []
    AmountLst = []

    while True:
        while True:
            try:
                ClaimNumListing = int(input("Enter the Listing claim Number (-1 to end): "))
                if ClaimNumListing == -1:
                    break # Exit claim entry loop early
            except:
                print("Error - invalid value for the listing price.")
            else:
                break

        if ClaimNumListing == -1:
            break


        while True:
            try:
                ClaimDateListing = input("Enter the Claim date listing (YYYY-MM-DD): ")
                ClaimDateListing = datetime.datetime.strptime(ClaimDateListing, "%Y-%m-%d")
            except:
                print("   Data Entry Error - Claim date is not in a valid format.")
            else:
                break


        while True:
            try:
                ClaimAmountListing = float(input("Enter claim amount: "))
            except:
                print("   Data Entry Error - invalid value for the listing amount.")
            else:
                break

        
        ClaimLst.append(ClaimNumListing)
        DateLst.append(ClaimDateListing)
        AmountLst.append(ClaimAmountListing)


    # Perform required calculations.
        if InsuredCars == 1:
            InsurancePrem = BASIC_PREM
        else :
            InsurancePrem = BASIC_PREM + (InsuredCars - 1) * BASIC_PREM * (1 - ADD_CAR_DISC_RATE)


    ExtraCost = calculate_extra_cost(Liability, GlassCoverage, LoanerCar, InsuredCars)

    TotInsuPrem = InsurancePrem + ExtraCost
    HST = HST_RATE * TotInsuPrem
    TotalCost = TotInsuPrem + HST


    if PayMethod != "Down Pay":

        MonthPay = (MONTHLY_PAY_FEE + TotalCost) / NUM_PAYMENT

    else:

        MonthPay = (MONTHLY_PAY_FEE + (TotalCost - DownPayAmnt)) / NUM_PAYMENT

    

    InvoiceDate, FirstPayDate = current_and_next_month_date()



# Display user output
    print("\n\n")
    print("      One Stop Insurance Company")
    print("     Customer Summary and Receipt")
    print()
    print("─" * 37)
    print()
    print(f"Policy No:  {POLICY_NO:<9d}")
    print()
    print(f"Client Name and Address:")
    print()
    print(f"{CustFirst} {CustLast}")
    print(f"{StreetAd:<24s}")
    print(f"{City:<15s}, {Prov:<2s}  {PostalCode:<6s}")
    print()
    print(f"Phone: ({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]} (C)")
    print()


    print(f"Number of Cars:            {InsuredCars:>9d}")

    if Liability == "Y":
        LB = "YES"
    else:
        LB = "NO"
    print(f"Liability Coverage:        {LB:>9s}")

    if GlassCoverage == "Y":
        GC = "YES"
    else:
        GC = "NO"
    print(f"Glass Coverage:            {GC:>9s}")

    if LoanerCar == "Y":
        LC = "YES"
    else:
        LC = "NO"
    print(f"Loaner Car Coverage:       {LC:>9s}")

    print(f"Payment Method:            {PayMethod:>9s}")
    print("                            --------")



    if PayMethod == "Down Pay":
        DownPayAmntDsp = FNumber2(DownPayAmnt)
        print(f"Down Payment Amount:       {DownPayAmntDsp:>9s}")
        

    InsurancePremDsp = FNumber2(InsurancePrem)
    print(f"Insurance Premium:         {InsurancePremDsp:>9s}")

    ExtraCostDsp = FNumber2(ExtraCost)
    print(f"Extra Cost:                {ExtraCostDsp:>9s}")

    print("                            --------")

    TotInsuPremDsp = FNumber2(TotInsuPrem)
    print(f"Total Premium:             {TotInsuPremDsp:>9s}")

    HSTDsp = FNumber2(HST)
    print(f"HST:                       {HSTDsp:>9s}")

    print("                            --------")



    TotalCostDsp = FNumber2(TotalCost)
    print(f"Total Cost:                {TotalCostDsp:>9s}")

    if PayMethod in ["Monthly", "Down Pay"]:
        MonthPayDsp = FNumber2(MonthPay)
        print(f"Monthly Payment:           {MonthPayDsp:>9s}")

    print("─" * 37)



    print()
    print(f"Invoice Date:             {InvoiceDate}")
    print(f"First Payment Date:       {FirstPayDate}")
    print("─" * 37)



    print()
    print("Claim History:")
    print()
    print(" Claim #     Claim Date      Amount")
    print("-" * 37)

    #Displaying Claim list
    for i in range(len(ClaimLst)):
        
        AmountLstDsp = [FNumber2(amount) for amount in AmountLst]
        print(f"  {ClaimLst[i]:<10d} {DateLst[i].strftime('%Y-%m-%d'):<15s}{AmountLstDsp[i]:>9s}")

    print("-" * 37)
    print()
    print(f"Thank You For Choosing One Stop Insurance!")



    f = open("Policy.dat", "a")
 
    # Any value written to a file must be recognized as a string.

    f.write(f"{str(POLICY_NO)}, ")
    f.write(f"{InvoiceDate}, ")
    f.write(f"{CustFirst}, ")
    f.write(f"{CustLast}, ")
    f.write(f"{StreetAd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostalCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{str(InsuredCars)}, ")
    f.write(f"{'Y' if Liability == 'Y' else 'N'}, ")
    f.write(f"{'Y' if GlassCoverage == 'Y' else 'N'}, ")
    f.write(f"{'Y' if LoanerCar == 'Y' else 'N'}, ")
    f.write(f"{PayMethod}, ")
    if PayMethod == "Down Pay":
        f.write(f"{str(DownPayAmnt)}, ")
    else:
        f.write("0, ")  # If no down payment, record 0
    f.write(f"{str(InsurancePrem)}, ")
    f.write(f"{str(ExtraCost)}, ")
    f.write(f"{str(TotInsuPrem)}\n")

    f.close()

    print()


    #Progress bar 
    TotalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Policy Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()
    print()
    print("Policy information has been successfully saved to Policy.dat ...")
    print()

    #Incrementing policy Number
    POLICY_NO += 1
    print()
    Continue = input("Do you want to enter another policy (Y/N)? ").upper()
    if Continue == "N":
        break
   

# Any housekeeping duties at the end of the program.
# Write the values to a file for future reference.
f= open('Const.dat', 'w')
f.write(f"{POLICY_NO}\n")
f.write(f"{BASIC_PREM}\n")
f.write(f"{ADD_CAR_DISC_RATE}\n")
f.write(f"{LIAB_COVRG_COST}\n")
f.write(f"{GLASS_COVRG_COST}\n")
f.write(f"{LOANER_COVRG_COST}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{MONTHLY_PAY_FEE}\n")
f.close() 
    





















