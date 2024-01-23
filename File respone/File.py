rplc="[Name]"
with open ("Name.txt",mode="r") as file1:
    names=file1.readlines()
with open ("Sample_letters.txt",mode="r") as file2:
    content=file2.read()
    a=1
    for name in names:
        name=name.strip()
        new_letter=content.replace(rplc,name)
        with open (f"Letters/{a}.Letter_to_{name}.txt",mode="w") as temp_file:
            temp_file.write(new_letter)
        temp_file.close()
        a+=1