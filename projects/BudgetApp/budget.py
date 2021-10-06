class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([a['amount'] for a in self.ledger])

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        top = self.name.center(30, '*') + '\n'
        ledger_items = ['{:<23}{:>7.2f}'.format(i['description'][:23], float(i['amount'])) for i in self.ledger]
        ledger_items = '\n'.join(ledger_items) + '\n'
        total = 'Total: ' + str(self.get_balance())
        return top + ledger_items + total


def create_spend_chart(categories):
    tops = 'Percentage spent by category'

    # Prepare data for plot
    total_spent = [[a['amount'] for a in cat.ledger if a['amount'] < 0] for cat in categories]
    total_spent = -sum([x for y in total_spent for x in y])

    dic = {}

    for cat in categories:
        cat_spent = -sum([a['amount'] for a in cat.ledger if a['amount'] < 0])
        cat_share_spent = (cat_spent / total_spent) * 100
        dic[cat.name] = cat_share_spent

    # Plot barchart
    bc = []
    for i in range(100, -1, -10):
        line = '{:>3}|'.format(i)
        for cat in categories:
            if dic[cat.name] >= i:
                line += ' o '
            else:
                line += ' ' * 3
        bc.append(line + ' ')
    barchart = '\n'.join(bc)

    # Plot legend below barchart
    bot_line = ' ' * 4 + '-' * 3 * len(categories) + '-'
    longest_cat_name = max(dic.keys(), key=len)

    legend = []
    for i in range(len(longest_cat_name)):
        line = ' ' * 4
        for cat in categories:
            try:
                line += cat.name[i].center(3, ' ')
            except IndexError:
                line += ' ' * 3
        legend.append(line + ' ')
    legend = '\n'.join(legend)

    return '\n'.join([tops, barchart, bot_line, legend])

