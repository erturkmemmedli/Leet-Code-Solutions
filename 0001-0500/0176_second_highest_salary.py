import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = sorted(employee['salary'].unique(), key = lambda x: -x)
    return pd.DataFrame({'SecondHighestSalary': [salaries[1]] if len(salaries) > 1 else [None]})
