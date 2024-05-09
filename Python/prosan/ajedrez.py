from flask import Flask 
import chess
import chess.svg
app = Flask(__name__)

@app.route('/chess')
def play():

	#N for knight or horse
	#Nothing for pawn
	#R for rook
	#Q for queen
	#B for bishop
	#K for king

	board = chess.Board()
	board.push_san("Nf3")
	squares = board.attacks(chess.H8)
	board = chess.svg.board(board = board, 
               squares=squares, size = 400)
	
	return board

if __name__ == "__main__":
	app.run(debug=True)