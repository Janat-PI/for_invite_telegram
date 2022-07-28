from classes import ReaderExcel, Converter


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

    print(converter.generate_dict(data))
    

  
