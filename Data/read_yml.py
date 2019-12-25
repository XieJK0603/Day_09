import yaml

with open("./value1.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)

    print("data:{}".format(data))

    #print("类型:{}".format(type(data.get("value23"))))
    # print("类型:{}".format(type(data.get("value24"))))