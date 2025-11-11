from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    vsData('life_expectancy_years.csv')
    




def vsData(path : str) :
    try :
        
        dataset = load(path)
        
        country_data = dataset[dataset['country'] == 'France']
        
        if country_data.empty:
            print("Error : No data found for choosen country")
            return
        
        country_data = country_data.drop(columns='country').T
        country_data.columns = ['Life Expectancy']
        country_data.index.name = 'Year'
        country_data.reset_index(inplace=True)
        #conver datatype
        
        country_data['Year'] = country_data['Year'].astype(int)
        life_expentacy_years = country_data['Life Expectancy'].astype(float)
        
        year = country_data['Year'].to_numpy().reshape(-1)
        life_expectancy = life_expentacy_years.to_numpy().reshape(-1)
        
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=year, y=life_expectancy)
        plt.title("Life Expectancy in Morocco Over Time")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(rotation=45)

        start_year = country_data['Year'].min()
        end_year = country_data['Year'].max()
        plt.xticks(range(start_year, end_year + 1, 40), rotation=45)

        plt.show()
        
    except KeyError as e:
        print(f"Error: Missing expected column - {e}")


if __name__ == "__main__":
    main()