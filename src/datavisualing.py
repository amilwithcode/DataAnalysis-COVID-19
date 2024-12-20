# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# data = pd.read_csv('data/worldometer_data.csv')  # Faylın doğru adını daxil edin

# # Sütun adlarını uyğunlaşdırmaq 
# data.rename(columns={
#     'Country/Region': 'Country',
#     'ObservationDate': 'Date',
#     'Confirmed': 'TotalCases',
#     'Deaths': 'TotalDeaths',
#     'Recovered': 'TotalRecovered'
# }, inplace=True)

# # Məlumatları düzgün nömrələnmiş cədvəl halına salmaq
# data = data[['Country', 'TotalCases', 'TotalDeaths', 'TotalRecovered']].dropna()

# # Ölkələr üzrə ümumi statistikalar
# country_data = data.groupby("Country").sum(numeric_only=True).reset_index()

# # Əlavə göstəricilər
# country_data['DeathRate'] = (country_data['TotalDeaths'] / country_data['TotalCases']) * 100
# country_data['RecoveryRate'] = (country_data['TotalRecovered'] / country_data['TotalCases']) * 100

# # Təsdiqlənmiş hallar əsasında sıralanmış ölkələr
# country_data = country_data.sort_values('TotalCases', ascending=False)

# # Ən çox təsirlənmiş 10 ölkə
# top_10_countries = country_data.head(10)

# # Nəticəni çap etmək
# print(top_10_countries)

# # Vizuallaşdırma
# plt.figure(figsize=(12, 6))
# sns.barplot(x='TotalCases', y='Country', data=top_10_countries, palette="viridis")
# plt.title("Ən Çox Təsirlənmiş 10 Ölkə (Təsdiqlənmiş Hallar)")
# plt.xlabel("Təsdiqlənmiş Hallar")
# plt.ylabel("Ölkə")
# plt.show()


# plt.figure(figsize=(12, 6))
# sns.barplot(x='TotalCases', y='Country', data=top_10_countries, palette="coolwarm")
# plt.title("Top 10 Ölkələr üzrə Ümumi COVID-19 Halları")
# plt.xlabel("Ümumi Hallar")
# plt.ylabel("Ölkə")
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.barplot(x='DeathRate', y='Country', data=top_10_countries, palette="Reds")
# plt.title("Top 10 Ölkələr üzrə Ölüm Nisbətləri (%)")
# plt.xlabel("Ölüm Nisbəti (%)")
# plt.ylabel("Ölkə")
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.barplot(x='RecoveryRate', y='Country', data=top_10_countries, palette="Greens")
# plt.title("Top 10 Ölkələr üzrə Sağalma Nisbətləri (%)")
# plt.xlabel("Sağalma Nisbəti (%)")
# plt.ylabel("Ölkə")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Dataseti yükləyin
# data = pd.read_csv('worldometer_data.csv')  # Faylın doğru adını daxil edin
# # Sütun adlarını uyğunlaşdırmaq (əgər zəruridir)
# data.rename(columns={
#     'Country/Region': 'Country',
#     'ObservationDate': 'Date',
#     'Confirmed': 'TotalCases',
#     'Deaths': 'TotalDeaths',
#     'Recovered': 'TotalRecovered'
# }, inplace=True)

# # Məlumatları düzgün nömrələnmiş cədvəl halına salmaq
# data = data[['Country', 'TotalCases', 'TotalDeaths', 'TotalRecovered']].dropna()

# # İki ölkənin adlarını seçin
# selected_countries = ['USA', 'India']  # Ölkə adlarını dəyişdirə bilərsiniz

# # Seçilmiş ölkələr üzrə məlumatları süzmək
# selected_data = data[data['Country'].isin(selected_countries)]
# # Ölkələr üzrə ümumi statistikalar
# country_data = selected_data.groupby("Country").sum(numeric_only=True).reset_index()
# # Əlavə göstəricilər
# country_data['DeathRate'] = (country_data['TotalDeaths'] / country_data['TotalCases']) * 100
# country_data['RecoveryRate'] = (country_data['TotalRecovered'] / country_data['TotalCases']) * 100
# # Nəticəni çap etmək
# print(country_data)

# # Vizuallaşdırma: Ümumi halların müqayisəsi
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Country', y='TotalCases', data=country_data, palette="coolwarm")
# plt.title("Seçilmiş İki Ölkədə Təsdiqlənmiş Halların Müqayisəsi")
# plt.xlabel("Ölkə")
# plt.ylabel("Təsdiqlənmiş Hallar")
# plt.show()

# # Vizuallaşdırma: Ölüm və sağalma nisbətlərinin müqayisəsi
# plt.figure(figsize=(12, 6))
# country_data.set_index('Country')[['DeathRate', 'RecoveryRate']].plot(kind='bar', figsize=(10, 6), color=['red', 'green'])
# plt.title("Ölüm və Sağalma Nisbətlərinin Müqayisəsi (Seçilmiş İki Ölkə)")
# plt.xlabel("Ölkə")
# plt.ylabel("Faiz (%)")
# plt.legend(["Ölüm Nisbəti", "Sağalma Nisbəti"])
# plt.show()
