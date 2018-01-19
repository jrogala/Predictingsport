import csv

def update(s,wm,bm,res,we,be):
    temp = ["" for i in range(6)]
    temp[0] = wm
    temp[1] = we
    temp[2] = bm
    temp[3] = be
    temp[4] = str(int(we) - int(be))
    if res=="1-0": 
        #white won
        temp[5] = "White"
        flag = True
    elif res=="0-1":
        #black won
        temp[5] = "Black"
        flag = True
    elif res=="1/2-1/2":
        #draw
        temp[5] = "Draw"
        flag = True
    else:
        print("Some error")
        flag = False
    if flag:
        s.writerow(temp)
    


def parser(s,filename):
    #get standardized pgn file
    with open(filename,'r') as f:
        print("Opening " + filename)
        line = f.readline()
        while line != "":
            if line[0:7] == "[White ":
                whiteman = line[8:-4]
            elif line[0:7] == "[Black ":
                blackman = line[8:-4]
            elif line[0:8] == "[Result ":
                result = line[9:-4]
            elif line[0:10] == "[WhiteElo ":
                whiteelo = line[11:-4]
            elif line[0:10] == "[BlackElo ":
                blackelo = line[11:-4]
            elif line[0:11] == "[EventDate ":
                update(s,whiteman,blackman,result,whiteelo,blackelo)
            line = f.readline()
        print("Closing " +filename)
    

def main():
    s = csv.writer(open("chessgame.csv", "wb"))
    #parser(s,"database/KingBase2017-A00-A39.pgn")
    #parser(s,"database/KingBase2017-A40-A79.pgn")
    #parser(s,"database/KingBase2017-A80-A99.pgn")
    #parser(s,"database/KingBase2017-B00-B19.pgn")
    #parser(s,"database/KingBase2017-B20-B49.pgn")
    #parser(s,"database/KingBase2017-B50-B99.pgn")
    parser(s,"database/KingBase2017-C00-C19.pgn")

if __name__ == '__main__':
    main()

