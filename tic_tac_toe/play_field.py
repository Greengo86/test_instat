import dataclasses


@dataclasses.dataclass
class PlayField:
    """
    Field on board. Possible values - X, O, ''! '' - empty - value on default
    """
    field1: str = ''
    field2: str = ''
    field3: str = ''
    field4: str = ''
    field5: str = ''
    field6: str = ''
    field7: str = ''
    field8: str = ''
    field9: str = ''


class PlayTicTacToe:
    POSSIBLE_FIELD_VALUES = ('X', 'O', '')
    COMBINATION_WINS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (3, 6, 9),
        (2, 5, 8),
        (1, 5, 9),
        (3, 5, 7),
    )

    def __init__(self, board):
        self.board = board

    @staticmethod
    def checking_field_num(num: str) -> bool:
        return True if hasattr(PlayField, num) else False

    def checking_passed_value(self, value: str) -> bool:
        return True if value in self.POSSIBLE_FIELD_VALUES else False

    def set_state_field(self, field_num: str, field_value: str) -> None:
        if not PlayTicTacToe.checking_field_num(field_num):
            print(f'Your field num - {field_num} is wrong. Please, try again!')
            return

        if not self.checking_passed_value(field_value):
            print(f'Your field value - {field_value} is wrong. Please, try again!')
            return

        setattr(self.board, field_num, field_value)

    @staticmethod
    def field_str(combi: tuple, num: int) -> str:
        return f'field{combi[num]}'

    def get_game_status(self) -> str:
        all_empty = True
        for item in self.board.__dict__:
            if not getattr(self.board, item) == '':
                all_empty = False

        if all_empty:
            return 'empty'

        for value in self.POSSIBLE_FIELD_VALUES:
            if value:
                for combi in self.COMBINATION_WINS:
                    one, two, three = PlayTicTacToe.field_str(combi, 0), \
                                      PlayTicTacToe.field_str(combi, 1), \
                                      PlayTicTacToe.field_str(combi, 2)
                    if all([getattr(self.board, one) == value, getattr(self.board, two) == value,
                            getattr(self.board, three) == value]):
                        return f'winner player with sign - {value}'
        else:
            return 'Game In Progress'


def start_play():
    board = PlayField()
    play_obj = PlayTicTacToe(board=board)
    play_obj.set_state_field(field_num='field3', field_value='X')
    play_obj.set_state_field(field_num='field8', field_value='X')
    play_obj.set_state_field(field_num='field9', field_value='X')
    status = play_obj.get_game_status()
    print(status)


if __name__ == '__main__':
    start_play()
