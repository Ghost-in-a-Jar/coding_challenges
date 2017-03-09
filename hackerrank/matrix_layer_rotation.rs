use std::io;
use std::fmt;

struct Matrix {
    original: Vec<Vec<String>>,
    rotated: Vec<Vec<String>>,
    rows: usize,
    cols: usize,

}

impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for line in &self.rotated {
            for num in line {
                try!(write!(f,"{} ", num));
            }
            try!(write!(f,"\n"));
        }
        write!(f,"")
    }
}

impl Matrix {

    fn read_matrix(num_rows : &usize, num_cols: &usize) -> Matrix {
        let mut rows = Vec::new();
        for _ in 0 .. *num_rows {
            let mut row_string = String::new();
            io::stdin().read_line(&mut row_string).ok().expect("read error");

            let row_arr : Vec<String> = row_string.trim().split_whitespace().map(|s| s.to_string()).collect();
            rows.push(row_arr);
        }
        let rows_copy = rows.to_vec();
        return Matrix{original: rows, rotated: rows_copy, rows: *num_rows, cols: *num_cols};
    }

    fn rotate(&mut self, rot : &usize) {
        self.rows-=1;
        self.cols-=1;
        for r in 0 .. self.rows+1 {
            for c in 0 .. self.cols+1 {
                let x = if r < self.rows - r {r} else {self.rows - r};
                let y = if c < self.cols - c {c} else {self.cols - c};
                let min = if x < y {x} else {y};
                let max_row = self.rows - min;
                let max_col = self.cols - min;
                let parameter = (max_row + max_col) * 2 - min * 4;

                let abs_rot : usize = if parameter == 0 {*rot} else {*rot % parameter};
                let mut row = r;
                let mut col = c;
                for _ in 0 .. abs_rot {
                    if col == min && row < max_row {
                        row+=1;
                    } else if row == max_row && col < max_col {
                        col+=1;
                    } else if row > min && col == max_col {
                        row-=1;
                    } else if row == min && col > min {
                        col-=1;
                    }
                }
                self.rotated[row][col] = self.original[r][c].clone();
            }
        }
    }
}

fn main() {
    // variable declaration
    let mut mnr_string = String::new();

    io::stdin().read_line(&mut mnr_string).ok().expect("read error");

    let mnr_int_arr : Vec<usize> = mnr_string.split_whitespace().map(|num| num.parse().unwrap()).collect();

    let m = mnr_int_arr[0];
    let n = mnr_int_arr[1];
    let r = mnr_int_arr[2];

    let mut matrix = Matrix::read_matrix(&m,&n);

    matrix.rotate(&r);

    print!("{}",matrix);
}