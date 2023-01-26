from paskolos import Loan

loan = Loan(0, 0, 0)
while True:
    print('-' * 100)
    try:
        choice = int(input(
            "Choose\n1.Input data \n2.Loan info \n3.Loan graph \n4.Quit "))

        if choice == 1:
            print('-' * 100)
            sum = int(input("input loan sum in euro: "))
            term = int(input("input loan term in months: "))
            interests = float(input("input interest rate (e.g. input 0.1 for 10%): "))
            loan = Loan(sum, term, interests)
            loan.compute()
        if choice == 2:
            print('-' * 100)
            print(loan.loan_info())
        if choice == 3:
            print('-' * 100)
            print(loan.interest_graph2())
        if choice == 4:
            print("Bye")
            break
    except:
        print()
        print("Bad input")
        print()
