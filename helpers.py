
import csv

def to_csv(data, scraper):
    filename = scraper.replace('.py', '.csv')
    with open(filename, 'w') as fp:
        writer = csv.writer(fp)
        for row in data:
            try:
                writer.writerow(row)
            except:
                raise Exception("Failed to write row %s" % row)
