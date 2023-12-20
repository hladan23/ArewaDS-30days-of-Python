# Exercises: Level 1
# Q1

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        middle = n // 2

        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def mode(self):
        from collections import Counter
        frequencies = Counter(self.data)
        mode_values = [k for k, v in frequencies.items() if v == max(frequencies.values())]
        return mode_values if mode_values else None

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / len(self.data)

    def standard_deviation(self):
        import math
        return math.sqrt(self.variance())

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile(self, percent):
        sorted_data = sorted(self.data)
        index = (percent / 100) * (len(sorted_data) - 1)
        lower_index = int(index)
        upper_index = lower_index + 1

        if lower_index == upper_index:
            return sorted_data[lower_index]
        else:
            lower_value = sorted_data[lower_index]
            upper_value = sorted_data[upper_index]
            interpolation = index - lower_index
            return lower_value + (upper_value - lower_value) * interpolation

    def frequency_distribution(self):
        from collections import Counter
        return dict(Counter(self.data))


# Example:
def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', self.var())
        print('Standard Deviation: ', self.std())
        print('Frequency Distribution: ', self.freq_dist())
# usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()

# Exercises: Level 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        if description not in self.incomes:
            self.incomes[description] = amount
        else:
            self.incomes[description] += amount

    def add_expense(self, description, amount):
        if description not in self.expenses:
            self.expenses[description] = amount
        else:
            self.expenses[description] += amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Account Information for {self.firstname} {self.lastname}:\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n\n"
        info += "Income Details:\n"
        for desc, amount in self.incomes.items():
            info += f"{desc}: {amount}\n"
        info += "\nExpense Details:\n"
        for desc, amount in self.expenses.items():
            info += f"{desc}: {amount}\n"
        return info


# Example usage:
person = PersonAccount("Hajara", "Ladan")

person.add_income("Salary", 50000)
person.add_income("Bonus", 10000)

person.add_expense("Rent", 150000)
person.add_expense("Groceries", 20000)
person.add_expense("Utilities", 30000)

print(person.account_info())


