import csv
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    headers = data[0]
headers.append('poster_link')
