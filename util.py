import settings as set

def ServerInfo(contend, data1, data2):
    st = {}
    for element in contend:
        try:
            if element in data1:
                print(f"data1 ---> {element} - {data1[element]}")
                st[element] = str(data1[element])
            elif element in data2:
                print(f"data2 ---> {element} - {data2[element]}")
                st[element] = str(data2[element])
            else:
                raise Exception(f"Element '{element}' not found in both data1 and data2")
        except Exception as err:
            print(f"Exception with: {element} - {err}")
            return False
    print(st)
    return st

    