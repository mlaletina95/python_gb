# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
import string

s = """
GeekBrains is a Russian company in the field of online education. Founded in 2010. An educational platform that helps to master a profession and get an IT education. Teachers-practitioners have been teaching information technology, programming, analytics, testing, marketing, management, and design for more than 10 years. Since 2016, it has been a part of VK. One of the top five Russian online education companies.[1]

History
In 2010, Alexander Nikitin and Hayk Hayrapetyan launched the School of Programming project, and in 2014, the GeekBrains educational Internet platform was created on its basis.[2] In 2016, the GeekBrains LLC legal entity was registered.[3] In the same year, the Mail.ru Group acquired the 51% controlling stake of the company. At that time, the monthly audience of GeekBrains was estimated at 500 thousand people.[4]

In 2019, GeekBrains showed a profit over 300 million rubles. In 2020, the Mail.ru Group bought out the remaining 49% of the shares, so the holding became the sole owner of GeekBrains.[5] In the first half of 2020, the demand for education on this online platform increased by about 5 times compared to the same period in 2019.[6] In the rating of the leading Russian companies in the field of online education for 2018, GeekBrains took the 9th place. In the rating for 2019, the company moved up to the 5th place.[7] In 2020, GeekBrains ranked 4th among the largest online education companies according to Smart Ranking.[8] In 2020, the overall revenue of the GeekBrains and Skillbox educational projects amounted 6.1 billion rubles, which is 3 times higher than in 2019.[9]

In the first quarter of 2021, GeekBrains’ revenue increased by 207% compared to the same period in 2019 – up to 768 million rubles. According to this indicator, the project ranks 4th among educational projects in Russia.[10]

On June 4, 2021, GeekBrains and the Republic of Tatarstan signed an agreement for the development of information and communication technologies in Tatarstan as part of the SPIEF. The Prime Minister of the Republic of Tatarstan Aleksey Pesoshin signed a cooperation agreement with the CEO of the GeekBrains educational platform Alexander Volchek.[11]

In August 2021, Mail.ru Group announced the creation of an educational holding (Skillbox Holding) based on its assets - Skillbox and GeekBrains[12]. The consolidated revenue of Skillbox and GeekBrains for the first half of 2021 amounted to 4.3 billion rubles against 1.9 billion rubles for the same period of 2020.[12]

GeekBrains participates in the Digital Professions program[13]. In 2022, 75,000 people will receive extended education under the Digital Professions project. Training will be available to all residents of Russia.[13]

Research, personal learning paths
GeekBrains observes a strong trend towards an increase in online education and new IT professions.[14]

As it follows from the data of a study by GeekBrains, the professions of developers, database administrators, testers and web engineers are in highest demand in IT.[15]

54.6% of the surveyed Russian citizens are ready to change their profession if a long lockdown is introduced in the country, as it appears from the survey conducted by experts from the GeekBrains educational platform.[16]

More than 400 thousand people took part in the survey of the GeekBrains platform: schoolchildren, students and workers in various fields. More than a quarter of them would like to learn a new profession.[17]

Training programs
GeekBrains has a government license for educational activities. GeekBrains online platform hosts training programs, courses and webinars in information technology, programming, analytics, marketing, management, and design. The company offers assistance with internships and employment to its graduates.[18] The average age of the online platform users is 20–35 years old.[19]

GeekBrains launched a new educational format to create personal learning paths.[20]

As of August 2021, the GeekBrains platform offers over 150 Training programs.
"""

# преобразуем в нижний регистр
s = s.lower()

# убираем пунктуацию
# взято отсюда https://datagy.io/python-remove-punctuation-from-string
for p in string.punctuation:
    s = s.replace(p, "")

# разбиваем на слова по пробелу
words = s.split(" ")

counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("Top 10 words: ")
top10 = sorted_counts[0:10]
for word, c in top10:
    print(word, c)
