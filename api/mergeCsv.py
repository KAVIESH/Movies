import csv
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    headers = data[0]
headers.append('poster_link')

with open('final.csv') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open('movies1.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovieLinks = data[1:]

for i in allMovies:
    posterFound = any(i[8] in allMovieLinks for movieLinks in allMovieLinks)
    if posterFound:
        for q in allMovieLinks:
            if i[8] == q[0]:
                i.append(q[1])
                if len(i) == 28:
                    with open('final.csv', 'a+') as f:
                     csvwriter = csv.writer(f)
                     csvwriter.writerow(i)

            
    