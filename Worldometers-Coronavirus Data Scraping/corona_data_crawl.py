from lxml import html
from lxml import etree
import requests
import mysql.connector
from datetime import timedelta
from datetime import datetime



#Connection informations for MySQL Database
cnx_corona = mysql.connector.connect(
    user='root',
    password='Aa12345',
    host='localhost',
    database='test',
    port=3306,
    charset='utf8', auth_plugin='mysql_native_password')

cursor_corona = cnx_corona.cursor()


#Function for scraping data
def content_crawl(country_list, data_time):
    for country in country_list:

        #Turn <tr> (country block) to HTML and turn it to lxml.
        country_row = html.fromstring(etree.tostring(country))

        country_name = country_row.xpath('//td[1]//text()')
        country_name = country_name[0].strip()
        if country_name.find("Total:") != -1 or country_name.strip() == "":
            continue

        total_case = country_row.xpath('//td[2]//text()')
        total_case = total_case[0].replace(',','').strip()

        new_case = country_row.xpath('//td[3]//text()')
        if len(new_case) > 0:
            new_case = new_case[0].replace('+','').replace(',','').strip()
        else:
            new_case = None

        total_deaths = country_row.xpath('//td[4]//text()')
        if len(total_deaths) > 0 and total_deaths[0].strip() != "":
            total_deaths = total_deaths[0].replace(',','').strip()
        else:
            total_deaths = None

        new_deaths = country_row.xpath('//td[5]//text()')
        if len(new_deaths) > 0:
            new_deaths = new_deaths[0].replace('+','').replace(',','').strip()
        else:
            new_deaths = None

        total_recovered = country_row.xpath('//td[6]//text()')

        if len(total_recovered) > 0:
            total_recovered = total_recovered[0].replace(',','').strip()
            if total_recovered == "N/A":
                total_recovered = None
        else:
            total_recovered = None

        active_cases = country_row.xpath('//td[7]//text()')
        active_cases = active_cases[0].replace(',','').strip()

        serious  = country_row.xpath('//td[8]//text()')
        if len(serious) > 0:
            serious = serious[0].replace(',','').strip()
        else:
            serious = None

        total_cases_1M_pop = country_row.xpath('//td[9]//text()')
        if len(total_cases_1M_pop) > 0:
            total_cases_1M_pop = total_cases_1M_pop[0].replace(',', '').strip()
        else:
            total_cases_1M_pop = None

        deaths_1M_pop = country_row.xpath('//td[10]//text()')
        if len(deaths_1M_pop) > 0:
            deaths_1M_pop = deaths_1M_pop[0].replace(',', '').strip()
        else:
            deaths_1M_pop = None

        data = {
            "data_time" : data_time,
            "country_name" : country_name,
            "total_case" : total_case,
            "new_case" : new_case ,
            "total_deaths" : total_deaths,
            "new_deaths" : new_deaths,
            "total_recovered" : total_recovered,
            "active_cases" : active_cases,
            "serious" : serious,
            "total_cases_1M_pop" : total_cases_1M_pop,
            "deaths_1M_pop": deaths_1M_pop,

        }
        print(data)
        product_insert(data)


#Function for insert data to MySQL DB
def product_insert(data):
    try:
        columns = data.keys()
        joined_columns = ', '.join(data.keys())
        values = [data[column] for column in columns]
        tuple_values = tuple(values)

        sql = "INSERT INTO corona_country (%s) VALUES %s " % (joined_columns, tuple_values)

        sql = sql.replace('None', 'null')

        cursor_corona.execute(sql)
        cnx_corona.commit()
        return cursor_corona.rowcount

    except Exception as e:
        error = str(e)
        if error.startswith('1062 (23000): Duplicate entry'):
            print('This country-time data already have.')

        else:
            print(error)

#Get HTML of site
url = "https://www.worldometers.info/coronavirus/#countries"
source_code = requests.get(url)
source_code = source_code.text
lxml_text = html.fromstring(source_code)


#Scraping last data time from HTML
lu_pos1 = source_code.find("Last updated:")
lu_pos2 = source_code[lu_pos1:].find("</div>")
time = source_code[lu_pos1:lu_pos1+lu_pos2]
time = time.replace("Last updated:", "").strip()
#print(time)


#Convert times to suitable format (YYYY-MM-DD HH:MI:SS")
current_time = datetime.strptime(time, '%B %d, %Y, %H:%M GMT')
yesterday_time = datetime.strftime(current_time, '%Y-%m-%d')
yesterday_time = datetime.strptime(yesterday_time + " 23:59:59", '%Y-%m-%d %H:%M:%S') - timedelta(days=1)
yesterday_time = datetime.strftime(yesterday_time, '%Y-%m-%d %H:%M:%S')
last_data_time = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')


#Scraping yesterday data
country_xpath = '//table[@id="main_table_countries_yesterday"]/tbody/tr'
country_list = lxml_text.xpath(country_xpath)
content_crawl(country_list, yesterday_time)


#Scraping today last data
country_xpath = '//table[@id="main_table_countries_today"]/tbody/tr'
country_list = lxml_text.xpath(country_xpath)
content_crawl(country_list, last_data_time)
