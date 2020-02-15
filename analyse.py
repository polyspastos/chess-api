import chess
import chess.engine


def get_analysis_score(fen):
    engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

    try:
        board = chess.Board(fen)
    except Exception as e:
        print('Invalid FEN. Please check input.\n', e)
        return False

    info = engine.analyse(board, chess.engine.Limit(depth=20))
    engine.quit()
    return info