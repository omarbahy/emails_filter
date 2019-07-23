import re
print("------------------------------\n[+] created by OMAR_BAHY\n------------------------------\n")
path=input("Enter the name/path of the list: ")
file=open(path,"r")

file_text=file.read()
domains=re.findall(r"@\w+",file_text)
lst=[]
for i in domains:
    name=i.replace("@","")
    lst.append(name)
domains_list=list(set(lst))
len_domains=len(domains_list)
print("\n--------------------------------\nfound {} domains in this list\n--------------------------------\n\n".format(len_domains)+str(domains_list))
file.close()
file_2=open(path,"r")
text_1=file_2.readlines()
for i in range(len(domains_list)):
    for ab in text_1: 
     regex=re.findall(r'\S+@{}\.\S+'.format(lst[i]),ab)
     if str(regex) != "[]":
      
    
      file1=open(str(lst[i]+".txt"),"a+")
      for a in regex:
          file1.write(a+"\n")
          file1.close()
     else:
      pass

    
file1.close()
print(("Done !"))
