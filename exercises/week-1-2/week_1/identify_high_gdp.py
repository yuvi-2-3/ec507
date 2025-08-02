gdp_values = [4.2,1.4,6.7,5.8,7.1,3.5,2.9]

# Basic loop to find countries with GDP greater than 3.0 
for gdp in gdp_values:
    if gdp > 3.0:
        print("Country with GDP greater than 3.0:")

# To get the list of countries with GDP greater than 3.0
high_gdp_countries = [gdp for gdp in gdp_values if gdp > 3.0]
print("Countries with GDP greater than 3.0:", high_gdp_countries)

#Avergage GDP calculation
total_gdp = sum(gdp_values)
count_countries = len(gdp_values)
average_gdp = total_gdp / count_countries
print("Average GDP of the countries:", average_gdp)


