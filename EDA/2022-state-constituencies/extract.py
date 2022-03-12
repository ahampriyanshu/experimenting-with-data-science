import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate


header = ["Candidate", "Party", "Criminal Cases", "Education", "Age", "Total Assets", "Liabilities"]
data = []

def inr_to_int(text):
    try:
        text = text.split()
        text = text[1].replace(",", "")
    except:
        return 0
    return int(text)


def main():
    for i in range(420):
        print("Extracting data for", state, ":", input_states[state])
        try:
            url = "https://myneta.info/Uttarpradesh2022/index.php?action=show_candidates&constituency_id=1"
            html = urlopen(url)
            soup = BeautifulSoup(html,'html.parser')
            title = soup.title.text
            title = title.split()
            print("Fetching data for", title[4])
            table = soup.find("table", {"id": "table1"})
            rows = table.find_all('tr')
            total_rows = len(rows)
            for i in range(1, total_rows):
                col_data = []
                cols = rows[i].find_all('td')
                total_cols = len(cols)
                for i in range(total_cols):
                    if i > 4:
                        col_data.append(inr_to_int(cols[i].text))
                    else:
                        col_data.append(cols[i].text)
                data.append(col_data)
            print(tabulate(data, headers=header, tablefmt='fancy_grid'))
        except e:
            print(e)
    df = pd.DataFrame(data = data, columns = header)
    df.to_csv('up.csv', index=False)

main()