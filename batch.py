import string
import random
import keyword

# 변수 설정
length = 100
hiddenlistresult = []
hiddenloclistresult = []
hiddencharlistresult = []
hiddenlist = []
hiddencharlist = []
hiddenloclist =[]
randomvar = []
file = './flag.bat'

def generate_random(length): # 배치 파일 변수 이름 랜덤 지정을 위한 함수
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #문자들
    random_str = ''.join(random.choice(letters) for _ in range(length)) 

    while keyword.iskeyword(random_str):
        random_str = ''.join(random.choice(letters) for _ in range(length))

    return random_str

def generate_random_hidden(length, hidden): #배치 파일 변수 값에 문자를 집어넣기 위한 함수
    if hidden.isspace(): 
        letters = string.ascii_letters
        random_str = ''.join(random.choice(letters) for _ in range(length+1))

        while keyword.iskeyword(random_str):
            random_str = ''.join(random.choice(letters) for _ in range(length+1))
        return random_str
    elif (hidden == "%" or hidden == "@" or hidden == '"' or hidden == "(" or hidden == ")" or hidden == ":"):
        # or hidden == "=" or hidden == "==" 
        letters = string.ascii_letters
        random_str = ''.join(random.choice(letters) for _ in range(length+1))

        while keyword.iskeyword(random_str):
            random_str = ''.join(random.choice(letters) for _ in range(length+1))
        return random_str
    else:
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for _ in range(length))

        while keyword.iskeyword(random_str):
            random_str = ''.join(random.choice(letters) for _ in range(length))

        random_index = random.randint(0, len(random_str)-1)
        new_str = random_str[:random_index] + hidden + random_str[random_index:]
        return new_str


with open(file, 'r') as f:
    line = f.readline()
    while line:
        for i in range(len(line)):
            temp = line[i]
            hiddencharlist.append(temp)
            hidden = generate_random_hidden(length,temp)
            hiddenlist.append(hidden)
            hiddenloclist.append(hidden.find(temp))
        line = f.readline()

zipped = list(zip(hiddenlist, hiddenloclist, hiddencharlist))
random.shuffle(zipped)
shuffledhiddenlist, shuffledhiddenloclist, shuffledhiddencharlist = zip(*zipped)

# print(shuffledhiddenlist)
# print(shuffledhiddenloclist)
# print(shuffledhiddencharlist)

for v in shuffledhiddencharlist:
    if v not in hiddencharlistresult:
        temp = shuffledhiddencharlist.index(v)
        hiddenloclistresult.append(shuffledhiddenloclist[temp])
        hiddenlistresult.append(shuffledhiddenlist[temp])
        hiddencharlistresult.append(v)
        randomvar.append(generate_random(length))
        

charhidden = dict(zip(hiddencharlistresult, hiddenlistresult))
randomhidden = dict(zip(randomvar, hiddenlistresult))
hiddenrandom = dict(zip(hiddencharlistresult, randomvar))

# print(randomhidden)
# print(res.get('e'))

# temp = res.get('e').find('e')
# print(charhidden)
# print(temp)
# print(hiddenrandom)

with open(file, 'r') as f:
    line = f.readline()
    for keys in randomhidden:
        for key, value in randomhidden.items():
            if key == keys:
                temp = keys
        print(f'SET "{temp}={randomhidden.get(keys)}"')
    while line:
        for i in range(len(line)):
            if(line[i].isspace()):
                print(end = " ")
            elif(line[i]=='"'):
                print('"',end="")
            # elif(line[i]=="="):
            #     print("=",end="")
            # elif(line[i]=="=="):
            #     print("==",end="")
            elif(line[i]=="("):
                print("(",end="")
            elif(line[i]==")"):
                print(")",end="")
            # elif(line[i]==":"):
            #     print(":",end="")
            elif(line[i]=="@"):
                print("cls")
                print("@", end="")
            elif(line[i] == "%"):
                print("%", end="")
            elif(line[i] == ":"):
                print(":", end="")
            elif(line[i] == "&"):
                print("&", end="")
            else:
                print(f"%{hiddenrandom.get(line[i])}:~{charhidden.get(line[i]).find(line[i])},1%", end = "")
        print("")
        line = f.readline()