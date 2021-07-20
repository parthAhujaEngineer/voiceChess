function make_move() {
    // make HTTP POST request to make move API
    $.post('/make_move', { 'fen': game.fen() }, function (data) {
        // load fen into the current board state
        game.move(data.best_move, { sloppy: true })

        // update board position
        board.position(game.fen());

        // update game status
        updateStatus();
    });
}

// handle new game button click
$('#new_game').on('click', function () {
    // reset board state
    game.reset();

    // set initial board position
    board.position('start');
});

// handle make move button click
$('#make_move').on('click', function () {
    // make computer move
    make_move();
});

// handle take back button click
$('#take_back').on('click', function () {
    // take move back
    game.undo();
    game.undo();

    // update board position
    board.position(game.fen());

    // update game status
    updateStatus();
});

// handle flip board button click
$('#flip_board').on('click', function () {
    // flip board
    board.flip();

});

// GUI board & game state variables
var board = null;
var game = new Chess();
var $status = $('#status');
var $fen = $('#fen');
var $pgn = $('#pgn');
var $score = $('#score');
var $time = $('#time');
var $nodes = $('#nodes');
var $knps = $('#knps')

// on picking up a piece
function onDragStart(source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.game_over()) return false

    // only pick up pieces for the side to move
    if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
        return false
    }
}

// on dropping piece
function onDrop(source, target) {
    // see if the move is legal
    var move = game.move({
        from: source,
        to: target,
        promotion: 'q' // NOTE: always promote to a queen for example simplicity
    })

    // illegal move
    if (move === null) return 'snapback'

    // make computer move
    make_move();

    // update game status
    updateStatus();
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd() {
    board.position(game.fen())
}

// update game status
function updateStatus() {
    var status = ''

    var moveColor = 'White'
    if (game.turn() === 'b') {
        moveColor = 'Black'
    }

    // checkmate?
    if (game.in_checkmate()) {
        status = 'Game over, ' + moveColor + ' is in checkmate.'
    }

    // draw?
    else if (game.in_draw()) {
        status = 'Game over, drawn position'
    }

    // game still on
    else {
        status = moveColor + ' to move'

        // check?
        if (game.in_check()) {
            status += ', ' + moveColor + ' is in check'
        }
    }
}

// chess board configuration
var config = {
    draggable: true,
    position: 'start',
    onDragStart: onDragStart,
    onDrop: onDrop,
    onSnapEnd: onSnapEnd
}

// create chess board widget instance
board = Chessboard('chess_board', config)

// update game status
updateStatus();