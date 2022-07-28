"""
it is module for running all code
"""
from excel_read.classes import ReaderExcel, Converter
from telegram.login import Login
    

if __name__ == "__main__":
    reader = ReaderExcel("file/data.xlsx")
    data1 = reader.read(columns=["name", "phone"])
    new_data = data1.to_dict(orient="split")

    index, columns, data = list(new_data.keys())

    converter = Converter(
        new_data=new_data, 
        index=index, 
        columns=columns,
        data=data
        )
    all_client = converter.generate_to_new_dict(data)

    client = Login()
    all_clients = client.get_clients(all_client)
    client.sign_in(user=all_clients)

    
    
    