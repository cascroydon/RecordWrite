from struct import Struct

class Record:
    "this represents a single record"
    structure = Struct("i 20s")

    def __init__(self, user_id, password):
        "initialize a record from the given inputs"
        self.user_id = user_id
        self.password = password

    def pack(self):
        "return the record encoded as binary data"
        return Record.structure.pack(self.user_id, self.password.encode())

    @classmethod
    def unpack(cls, record_data):
        "returns a Record decoded from binary data"
        user_id, password_data = Record.structure.unpack(record_data)
        return cls(user_id, password_data.decode())

    @classmethod
    def size(cls):
        "returns the size of this record in bytes"
        return Record.structure.size

class DataFile:
    "this represents a file containing a number of fixed size records"
    def __init__(self, data_file_name, number_of_records):
        "create a blank data file"
        self.data_file_name = data_file_name
        self.record_size = Record.size()
        self.number_of_records = number_of_records
        with open(data_file_name, "wb") as data_file:
            for _ in range(0, number_of_records):
                data_file.write(bytes(self.record_size))

    def write_record(self, record_number, record):
        "writes the given record into the file at the given position"
        with open(self.data_file_name, "r+b") as data_file:
            data_file.seek(self.record_size * record_number)
            data_file.write(record.pack())
    
    def read_record(self, record_number):
        "reads the record at the given position from the file"
        with open(self.data_file_name, "rb") as data_file:
            data_file.seek(self.record_size * record_number)
            return Record.unpack(data_file.read(self.record_size))

def main():
    # create a blank data file
    data_file = DataFile("data_file.dat", 100)
    
    # add some records
    data_file.write_record(0, Record(123, "FpvyXnGW"))
    data_file.write_record(1, Record(456, "2EtDKbmf"))

    # overwrite a record
    data_file.write_record(1, Record(456, "h3X4yHru"))

    # extract a record to examine the data
    record = data_file.read_record(1)
    print("user id: {0} password: {1}".format(record.user_id, record.password))

if __name__ == '__main__':
    main()
