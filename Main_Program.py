from flask import Flask
from flask import render_template
from flask import request
from module import Get_Move as gm
import chess
import chess.engine

# --- Recursive Function - Check Valid Move ---
def checkMove(board, moveInfo):
    moveR = moveInfo
    if chess.Move.from_uci(moveInfo) not in board.legal_moves:
        moveR = checkMove(board, gm.getMove(False))
    return moveR

# --- Creating Chess Engine Instance ---
engine = chess.engine.SimpleEngine.popen_uci('.//engine//stockfish//stockfish_13_win_x64.exe')

# --- Creating Web chessApp Instance ---
chessApp = Flask(__name__)

# --- Root(Index) route ---
@chessApp.route('/')
def root():
    return render_template('voiceChess.html')

# --- Make Engine Move API --- 
@chessApp.route('/make_move', methods=['POST'])
def make_move():
    # --- Extract FEN String - HTTP POST Request/Board Status 
    fen = request.form.get('fen')
    # --- Python Chess Board Instance/Engine ---
    board = chess.Board(fen)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    # --- Extracting & Returning Board ---
    fen = board.fen()
    return {'fen': fen}

# --- Make Engine Move API --- 
@chessApp.route('/take_move', methods=['POST'])
def take_move():
    # --- Extract FEN String - HTTP POST Request/Board Status 
    fen = request.form.get('fen')
    # --- Python Chess Board Instance/Engine ---
    board = chess.Board(fen)
    getM = checkMove(board, gm.getMove(True))
    board.push(chess.Move.from_uci(getM))
    # --- Extracting & Returning Board ---
    fen = board.fen()
    return {'fen': fen}


# --- Main Driver Application ---
if __name__ == '__main__':
    # --- Start HTTP Server
    chessApp.run(debug = True, threaded=True)
