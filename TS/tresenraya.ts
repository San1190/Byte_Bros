import * as readlineSync from 'readline-sync';

class TresEnRaya {
    symbol:string;
    tablero: Array<Array<string>>
    indexes:Record<number, string>
    win:boolean;
    
    constructor() {
        this.symbol = 'x';
        this.tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]];
        this.win = false;
        this.indexes = {
            1: this.tablero[0][0],
            2: this.tablero[0][1],
            3: this.tablero[0][2],
            4: this.tablero[1][0],
            5: this.tablero[1][1],
            6: this.tablero[1][2],
            7: this.tablero[2][0],
            8: this.tablero[2][1],
            9: this.tablero[2][2]
        }
    }

    check_rows(symbol:string) {
        for (let i = 0; i < 3; i++) {
            if (this.tablero[i][0] == symbol && this.tablero[i][1] == symbol && this.tablero[i][2] == symbol) {
                return true;
            }
        }
        return false;
    }

    check_columns(symbol:string) {
        for (let i = 0; i < 3; i++) {
            if (this.tablero[0][i] == symbol && this.tablero[1][i] == symbol && this.tablero[2][i] == symbol) {
                return true;
            }
        }
        return false;
    }

    check_diagonals(symbol:string) {
        return (this.tablero[0][0] == symbol && this.tablero[1][1] == symbol && this.tablero[2][2] == symbol) ||
            (this.tablero[0][2] == symbol && this.tablero[1][1] == symbol && this.tablero[2][0] == symbol);
    }

    check_win(symbol:string) {
        return this.check_rows(symbol) || this.check_columns(symbol) || this.check_diagonals(symbol);
    }

    draw () {
        this.tablero.forEach(element => {
            console.log(element);
        });
    }

    ask_position() {
        let pos;
        do {
            pos = readlineSync.questionInt('Introduce la posición: ');
            if (pos < 1 || pos > 9 || this.is_occupied(pos)) {
                console.log("Posición inválida");
            }
        } while (pos < 1 || pos > 9 || this.is_occupied(pos));
    
        return pos;
    }
    
    
    

    is_occupied(pos:number) {

        return this.indexes[pos] != " ";
    }

    all_occupied() {
        for (let i = 1; i <= 9; i++) {
            if (this.indexes[i] == " ") {
                return false;
            }
        }
        return true;
    }


    main() {
        let pos;
        while (!this.win) {
            this.draw();
            pos = this.ask_position();
            
            // Calculate the row and column of the position
            let row = Math.floor((pos - 1) / 3);
            let col = (pos - 1) % 3;
    
            // Update the board
            this.tablero[row][col] = this.symbol;
    
            if (this.check_win(this.symbol)) {
                this.win = true;
                console.log(this.symbol + " ha ganado");
            } else if (this.all_occupied()) {
                this.win = true;
                console.log("Empate");
            } else {
                this.symbol = this.symbol == 'x' ? 'o' : 'x';
            }
            
        }
    }
    
    
}


let game = new TresEnRaya();
game.main();