import json

def convert(filename: str) -> None:
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            name, mul = line.split(",")
            dic[name.upper()] = float(mul)

    with open("file_json.json", "w") as f:
        json.dump(dic, f, ensure_ascii=False)


if __name__ == "__main__":
    convert("../hw7/result.txt")
