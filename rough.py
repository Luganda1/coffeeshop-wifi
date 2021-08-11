import csv
import pandas as pd

with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    first_line = True
    cafes = []
    for row in csv_data:
        if not first_line:
            cafes.append({
                "CafeName": row[0],
                "Location": row[1],
                "Open": row[2],
                "Close": row[3],
                "Coffee": row[4],
                "Wifi": row[5],
                "Power": row[6],
        })
        else:
            first_line = False

print(cafes)
#
# data_file =  pd.read_csv('cafe-data.csv').to_records()
#
# for item in data_file:
#     print(item)

  # with open('.data/places.csv') as csv_file:
  #   data = csv.reader(csv_file, delimiter=',')
  #   first_line = True
  #   places = []
  #   for row in data:
  #     if not first_line:
  #       places.append({
  #         "city": row[0],
  #         "attraction": row[1],
  #         "gif_url": row[2]
  #       })
  #     else:
  #       first_line = False
  # return render_template("index.html", places=places)