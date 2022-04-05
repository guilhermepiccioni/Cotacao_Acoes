from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


class Actions:

    def __init__(self):
        self.table_tickers = pd.read_excel("Tickers.xlsx")
        self.start_action = "04-01-2022"  # Formatting: MM/DD/AAAA
        self.end_action = "04-03-2022"  # Formatting: MM/DD/AAAA
        self.local_web = "yahoo"

    def get_all_actions(self):

        for company in self.table_tickers["Company"]:
            if company[0] == "^":
                print(company)
                indices = web.DataReader(f'{company}',
                                         data_source=f'{self.local_web}',
                                         start=f'{self.start_action}',
                                         end=f'{self.end_action}')
                indices["Adj Close"].plot(figsize=(10, 5))
                plt.title(f'{company}')
                plt.show()
            else:
                print(company)
                action = web.DataReader(f'{company}.SA',
                                        data_source=f'{self.local_web}',
                                        start=f'{self.start_action}',
                                        end=f'{self.end_action}')
                action["Adj Close"].plot(figsize=(10, 5))
                plt.title(f'{company}')
                plt.show()


if __name__ == '__main__':
    cl = Actions()
    cl.get_all_actions()
