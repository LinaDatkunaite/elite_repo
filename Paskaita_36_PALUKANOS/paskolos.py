import pandas as pd
from operator import add


class Loan:
    def __init__(self, sum, term, interest):
        self.sum = sum
        self.term = term
        self.interest = interest
        self.loan_sums_list = []
        self.remaining = []
        self.interests = []
        self.amount_payable = []

    def compute(self):
        for i in range(self.term):
            self.loan_sums_list.append((self.sum / self.term))
            remain = self.sum - i * (self.sum / self.term)
            self.remaining.append(float(remain))
            interest_rate = round((float(remain) / 12 * self.interest), 2)
            self.interests.append(interest_rate)
        self.remaining = self.remaining[1:]
        self.remaining.append(int(0))

        self.amount_payable = list(map(add, self.loan_sums_list, self.interests))

    def interest_graph2(self):
        df = pd.DataFrame(
            dict(Month_nr=range(1, self.term + 1), Restore_part=self.loan_sums_list, Remain=self.remaining,
                 Interest=self.interests,
                 Amount_payable=self.amount_payable))
        df.set_index(['Month_nr'], inplace=True)
        return df

    def loan_info(self):
        sum_interests = 0
        for i in self.interests:
            sum_interests += i

        sum_amount = 0
        for i in self.amount_payable:
            sum_amount += i
        return f'Sum: {self.sum} euro, \nTerm: {self.term} months, \nInterest rate: {self.interest * 100}%, \nTotal interests to pay: {sum_interests} euro, \nTotal amount to pay: {sum_amount} euro.'
