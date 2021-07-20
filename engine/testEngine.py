import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(".//stockfish//stockfish_13_win_x64.exe")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)

engine.quit()
