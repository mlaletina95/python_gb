def split_and_mul(line):
    ni_s, nf_s = line.split("|")
    ni = int(ni_s)
    nf = float(nf_s)
    return ni * nf

def combine_numbers_and_names():
    with open("numbers.txt", "r") as f1:
        with open("names.txt", "r") as f2:
            with open("result.txt", "w+") as f:
                len1 = len(f1.readlines())
                len2 = len(f2.readlines())

                for i in range(max(len1, len2)):
                    line1 = f1.readline()
                    line2 = f2.readline()

                    if line1 == "":
                        f1.seek(0)
                        line1 = f1.readline()

                    if line2 == "":
                        f2.seek(0)
                        line2 = f2.readline()

                    mul = split_and_mul(line1)
                    name = line2.strip()
                    if mul < 0:
                        f.write(name.lower() + "," + str(abs(mul)))
                        f.write("\n")
                    else:
                        f.write(name.upper() + "," + str(round(mul)))
                        f.write("\n")


if __name__ == "__main__":
    combine_numbers_and_names()