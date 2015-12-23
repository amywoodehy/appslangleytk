import csv
from datetime import datetime

ANVIZ_KEYS = ('id', 'user', 'time', 'office', 'action',)

WARNINGS = {

}

def parse_database_csv(file_handle, separator=',', **kwargs):
    data, warnings = [], []
    csv_reader = csv.reader(file_handle, delimiter=separator, **kwargs)

    def csv_warning(warning):
        return str(csv_reader.line_num) + ': ' + warning

    for csv_record in csv_reader:
        record = dict(zip(ANVIZ_KEYS, csv_record))
        if record['action'] not in ['I', 'O', 'LI', 'LO']:
            warnings.append(csv_warning(WARNINGS['action'] % record['action']))
            continue
        try:
            record['time'] = datetime.strptime(record['time'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            warnings.append(csv_warning(WARNINGS['time']))
            continue
        data.append(record)
    return data, warnings
