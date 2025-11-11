from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    compare_data_of_two_country("population_total.csv", "France", "Morocco")


def population_by_country(dataset, country):
    
    country_data = dataset[dataset['country'] == country]
    
    if country_data.empty:
        print("Error : No data found for choosen country")
        return

    country_data = country_data.drop(columns='country').T
    country_data.columns = ['Population']
    country_data.index.name = 'Year'
    country_data.reset_index(inplace=True)
    
    popul_data = country_data['Population']
    country_data['Population'] = popul_data.str.replace('M', '').astype(float)
    return country_data


def compare_data_of_two_country(path, country1, country2):
    
    dataset = load(path)
    
    if dataset is None:
        return

    data1 = population_by_country(dataset, country1)
    data2 = population_by_country(dataset, country2)
    
    if data1 is None and data2 is None:
        return 
    
    data1['Country']= country1
    data2['Country']= country2

    
    # Concatenate data for both countries
    all_data = pd.concat([data1, data2])

    all_data['Year'] = all_data['Year'].astype(int)
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=all_data, x='Year', y='Population', hue='Country')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population in Millions")
    
    
    start_year = all_data['Year'].min()
    end_year = min(all_data['Year'].max(), 2050) #limit the years
    plt.xticks(range(start_year, end_year + 1, 40), rotation=45)
    
    y_max = all_data['Population'].max()
    plt.yticks(
            range(0, int(y_max) + 1, 20),
            labels=[f"{y}M" for y in range(0, int(y_max) + 1, 20)])

    plt.legend(title='Country')
    plt.show()



if __name__ == "__main__":
    main()