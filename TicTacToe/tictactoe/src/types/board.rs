use super::{Board,Cell,Player,Move};
use crate::moves::MoveError;

const EMPTY_BOARD: [[Cell; 3]; 3] = [
    [ Cell::None, Cell::None, Cell::None,],
    [ Cell::None, Cell::None, Cell::None,],
    [ Cell::None, Cell::None, Cell::None,],
];

impl Board<'_> {
    pub fn new() -> Self {
        Board {
            next_to_move: &Player::O,
            cells: EMPTY_BOARD,
        }
    }
    pub fn clone(&self) -> Self {
        let mut cells: [[Cell; 3]; 3] = EMPTY_BOARD.clone();
        for i::usize in 0..2 {
            for j::usize in 0..2 {
                cells[i][j] = self.cells[i][j];
            }
        }
        Board { next_to_move: self.next_to_move, cells }
    }
    pub fn make_move<'a>(&'a mut self, new_move: &'a Move, player: &Player) -> (Option<MoveError>) {
        //let mut new_board = Board::clone(self);
        //if move_player == self.next_to_move {
            let new_row: u8 = new_move.coords.0;
            let new_col: u8 = new_move.coords.1;
            if new_row < 3 && new_col < 3 {
                if self.cells[new_row as usize][new_col as usize] != None {
                    Some(MoveError::WrongPlayer)
                } else if player != self.next_to_move {
                    Some(MoveError::WrongPlayer)
                } else {
                    self.cells[new_row as usize][new_col as usize] = Some(self.next_to_move);
                    self.next_to_move = self.next_to_move.other();
                    Option::None
                }
            } else {
                Some(MoveError::OutOfBounds)
            }
        //} else {
        //    (Some(MoveError::WrongPlayer))
        //}
    }
} impl Board<'static>