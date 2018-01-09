# TIE-02100 Johdatus ohjelmointiin 
# Dancing Queen

def read_file(filename):
    
    # reads the played songs and their scores from the file

    try:
        fileobject = open(filename, "r")
        
        # TODO: initialize your data structure here
        score = []
        player_song = []
        song_results =[]
        block_songs = []
        # loop over fileobject row by row
        for row in fileobject:
            parts = row.strip().split(";")
            player = parts[0] # name of the player
            songs = parts[1:] # songs

            # TODO: make a data structure for this single
            #       player that includes his/her songs and scores
            player_song.append(player)

            # loop over this player's songs
            for song in songs:
                parts = song.split(":")
                results = parts[1].split(",")
                name = parts[0] # name of the song
                # list of presses, all integer
                results = [int(luku) for luku in results] 

                # TODO: connect these results to the song
                song_results.append(name)
                song_results.append(results)
                #block_songs.append(song_results)

            # TODO: add this player's data structure into the 
            #       main data structure
            player_song.append(song_results)
            score.append(player_song)

            song_results = []
            block_songs = []
            player_song = []
        return  score # TODO return the main data structure

    except IOError:
        print("Error! The file could not be read.")
        return None


def main():

    coefficients = [5, 4, 2, 0, -6, -12]
    MAX_EFFICIENT = 5
    filename = 'tanssipelit.txt'#input("Enter the name of the file: ")
    score = read_file(filename)

    # TODO : print ...
    for element in sorted(score):
        print(element)
    for sub_score in sorted(score):
        print(sub_score[0])
        for element in range(len(sorted(sub_score[1][0::2]))):
            temp = '- ' + str(sub_score[1][0::2][element])
            numerator = 0
            denominator = 0
            total = 0
            for index in range(len(sub_score[1][sub_score[1].index(sub_score[1][0::2][element]) + 1])):
               numerator += sub_score[1][sub_score[1].index(sub_score[1][0::2][element]) + 1][index] * coefficients[index]

            for index in range(len(sub_score[1][sub_score[1].index(sub_score[1][0::2][element]) + 1])):
                denominator += sub_score[1][sub_score[1].index(sub_score[1][0::2][element]) + 1][index] *  MAX_EFFICIENT

            total = float(numerator/denominator)*100

            print(temp + ': ' + format(total, '.2f')+ '%')

            numerator = 0
            denominator = 0
            total = 0
main()
