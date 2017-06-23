


class Highscores:

    _FILE_NAME = 'highscores.csv'

    def __init__(self):
        self.highscores = self.load_scores_from_file()

    def load_scores_from_file(self):
        with open(self._FILE_NAME, 'r') as data_file:
            highscores = data_file.readlines()
        highscores = [line.replace('\n', '').split('|') for line in highscores]

        return highscores

    @property
    def csv_string(self):
        csv_scores = ''
        if len(self.highscores) > 0:
            for score in self.highscores:
                csv_scores += '{}|{}\n'.format(score[0], score[1])

        return csv_scores

    @property
    def highscore_string(self):
        output_scores = '{:<13} {}\n'.format('name:', 'score:')
        if len(self.highscores) > 0:
            for score in self.highscores:
                output_scores += '{:<13} {}\n'.format(score[0], score[1])

        return output_scores

    def save_to_file(self):
        with open(self._FILE_NAME, 'w') as data_file:
            data_file.write(self.csv_string)

    def sort_highscores(self):
        self.highscores = sorted(self.highscores)

    def add_highscore(self, highscore):
        highscore = [str(highscore[0]), str(highscore[1])]
        self.highscores.append(highscore)
        self.sort_highscores()
        if len(self.highscores) > 10:

            for i in range(9, len(self.highscores)-1):
                self.highscores.pop(i)