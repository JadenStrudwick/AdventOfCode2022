use std::{collections::HashSet, thread, sync::{atomic::{AtomicUsize, Ordering}}};

fn main() {
    std::env::set_var("RUST_BACKTRACE", "1");
    std::env::set_var("RUSTFLAGS", "-C link-args=-Wl, -zstack-size=0x80000000");

    // load file
    let content = load_file();

    // extract sbs
    let mut sb = Vec::new();
    for line in content.lines() {
        sb.push(line_to_sb(line));
    }

    // get min and max x and y
    // let mut min_x = 0;
    // let mut max_x: i32 = 0;
    // let mut min_y = 0;
    // let mut max_y = 0;
    // for s in &sb {
    //     if s.min_x() < min_x {
    //         min_x = s.min_x();
    //     }
    //     if s.max_x() > max_x {
    //         max_x = s.max_x();
    //     }
    //     if s.min_y() < min_y {
    //         min_y = s.min_y();
    //     }
    //     if s.max_y() > max_y {
    //         max_y = s.max_y();
    //     }
    // }

    // // print min and max x and y
    // println!("min_x: {}", min_x);
    // println!("max_x: {}", max_x);
    // println!("min_y: {}", min_y);
    // println!("max_y: {}", max_y);

    // // create grid
    // println!("Creating grid...");
    // let mut grid = GRID::new(sb);
    // grid.print();

    // // fill grid
    // println!("Filling grid...");
    // grid.fill();
    // grid.print();

    // // draw incompatible sbs
    // println!("Drawing incompatible sbs...");
    // grid.draw_incompatible();
    // grid.print();

    // prompt for part1 or part2
    println!("Enter 1 for part1 or 2 for part2: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    if input.trim() == "1" {
        // part1
        println!("Which row do you want to count?");
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let row = input.trim().parse::<usize>().unwrap();
        // let count = grid.count_incompatible_in_row(row);

        let count = count_incompatible_in_row(&sb, row as i32);

        println!("count: {}", count);
    } else {
        // part2
        println!("At most?");
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();

        let row = input.trim().parse::<i32>().unwrap();
        let count = open_spaces_over_rows(&sb, row);
        println!("count: {}", count);
    }
}

fn load_file() -> String {
    // get user input
    println!("Enter 0 for example.txt or 1 for input.txt: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();

    // get file name
    if input.trim() == "0" {
        input = "example.txt".to_string();
    } else {
        input = "input.txt".to_string();
    }

    // read file
    let mut file = std::fs::File::open(input).expect("File not found");
    let mut contents = String::new();
    std::io::Read::read_to_string(&mut file, &mut contents)
        .expect("Something went wrong reading the file");
    contents
}

#[derive(Debug, Clone)]
struct SB {
    sx: i32,
    sy: i32,
    bx: i32,
    by: i32,
}

impl SB {
    // calculate distance
    fn distance(&self) -> i32 {
        (self.sx - self.bx).abs() + (self.sy - self.by).abs()
    }

    fn min_x(&self) -> i32 {
        if self.sx < self.bx {
            self.sx
        } else {
            self.bx
        }
    }

    fn max_x(&self) -> i32 {
        if self.sx > self.bx {
            self.sx
        } else {
            self.bx
        }
    }

    fn min_y(&self) -> i32 {
        if self.sy < self.by {
            self.sy
        } else {
            self.by
        }
    }

    fn max_y(&self) -> i32 {
        if self.sy > self.by {
            self.sy
        } else {
            self.by
        }
    }
}

fn line_to_sb(line: &str) -> SB {
    let collection: Vec<&str> = line.split_whitespace().collect();
    SB {
        sx: collection[2]
            .chars()
            .skip(2)
            .take(collection[2].len() - 3)
            .collect::<String>()
            .parse()
            .unwrap(),
        sy: collection[3]
            .chars()
            .skip(2)
            .take(collection[3].len() - 3)
            .collect::<String>()
            .parse()
            .unwrap(),
        bx: collection[8]
            .chars()
            .skip(2)
            .take(collection[8].len() - 3)
            .collect::<String>()
            .parse()
            .unwrap(),
        by: collection[9]
            .chars()
            .skip(2)
            .take(collection[9].len() - 2)
            .collect::<String>()
            .parse()
            .unwrap(),
    }
}

#[derive(PartialEq, Clone, Copy)]
enum CELL {
    EMPTY,
    FULL,
    SENSOR,
    BEACON,
}

impl CELL {
    fn to_char(&self) -> char {
        match self {
            CELL::EMPTY => '.',
            CELL::FULL => '#',
            CELL::SENSOR => 'S',
            CELL::BEACON => 'B',
        }
    }
}

struct GRID {
    matrix: Vec<Vec<CELL>>,
    min_x: i32,
    min_y: i32,
    sbs: Vec<SB>,
}

impl GRID {
    fn new(sbs: Vec<SB>) -> GRID {
        // get min and max x and y
        let mut min_x = 0;
        let mut max_x = 0;
        let mut min_y = 0;
        let mut max_y = 0;
        for s in &sbs {
            if s.min_x() < min_x {
                min_x = s.min_x();
            }
            if s.max_x() > max_x {
                max_x = s.max_x();
            }
            if s.min_y() < min_y {
                min_y = s.min_y();
            }
            if s.max_y() > max_y {
                max_y = s.max_y();
            }
        }

        // create matrix
        let matrix: Vec<Vec<CELL>> =
            vec![vec![CELL::EMPTY; (max_x - min_x + 1) as usize]; (max_y - min_y + 1) as usize];

        GRID {
            matrix,
            min_x,
            min_y,
            sbs,
        }
    }

    fn convert_to_grid_coordinates(&self, x: i32, y: i32) -> (i32, i32) {
        ((x - self.min_x), (y - self.min_y))
    }

    fn print(&self) {
        for (i, row) in self.matrix.iter().enumerate() {
            print!("{}: \t", i);
            for col in row.iter() {
                print!("{}", col.to_char());
            }
            println!();
        }
        println!();
    }

    fn fill(&mut self) {
        for s in &self.sbs {
            let (sx, sy) = self.convert_to_grid_coordinates(s.sx, s.sy);
            let (bx, by) = self.convert_to_grid_coordinates(s.bx, s.by);

            println!(
                "Before: sx:{} sy:{} bx:{} by:{}, After: sx:{} sy:{} bx:{} by:{}",
                s.sx, s.sy, s.bx, s.by, sx, sy, bx, by
            );
            println!("\n");

            self.matrix[sy as usize][sx as usize] = CELL::SENSOR;
            self.matrix[by as usize][bx as usize] = CELL::BEACON;
        }
    }

    fn draw_incompatible(&mut self) {
        for s in &self.sbs {
            let distance = s.distance();

            for y_off in -distance..distance + 1 {
                let x_range;
                if y_off < 0 {
                    x_range = (distance + y_off).abs();
                } else {
                    x_range = (distance - y_off).abs();
                }
                for x_off in -x_range..=x_range {
                    let (sx, sy) = self.convert_to_grid_coordinates(s.sx, s.sy);

                    let x = sx + x_off;
                    let y = sy + y_off;

                    if x >= 0
                        && x < self.matrix[0].len() as i32
                        && y >= 0
                        && y < self.matrix.len() as i32
                    {
                        if self.matrix[y as usize][x as usize] == CELL::EMPTY {
                            self.matrix[y as usize][x as usize] = CELL::FULL;
                        }
                    }
                }
            }
        }
    }

    fn count_incompatible_in_row(&self, row: usize) -> i32 {
        let mut count = 0;
        for col in 0..self.matrix[0].len() {
            if self.matrix[row][col] == CELL::FULL {
                count += 1;
            }
        }
        count
    }
}

fn count_incompatible_in_row(sbs: &Vec<SB>, row: i32) -> i32 {
    let mut xs = HashSet::new();

    for (i, s) in sbs.iter().enumerate() {
        println!("Checking sensor {} of {}", i, sbs.len() - 1);
        let distance = s.distance();

        // check if the sensor can reach the row
        if (s.sy <= row && s.sy + distance >= row) || (s.sy >= row && s.sy - distance <= row) {
            let remaining_distance = (row - s.sy).abs();
            let x_range = distance - remaining_distance;

            for x_off in -x_range..=x_range {
                let x = s.sx + x_off;

                if !xs.contains(&x) {
                    xs.insert(x);
                }
            }
        }
    }

    // return the length of the ys vector minus 1
    xs.len() as i32 - 1
}

fn open_spaces(sbs: &Vec<SB>, row: &i32, at_most: &i32) -> HashSet<i32> {
    //println!("Finding open spaces in row {}", row);

    let mut open_spaces = (0..=*at_most).collect::<HashSet<i32>>();

    for (i, sb) in sbs.iter().enumerate() {
        // check if open_spaces is empty
        if open_spaces.is_empty() {
            break;
        } else {
            let distance = sb.distance();

            // check if the sensor can reach the row
            if (sb.sy <= *row && sb.sy + distance >= *row)
                || (sb.sy >= *row && sb.sy - distance <= *row)
            {
                let remaining_distance = (row - sb.sy).abs();
                let x_range = distance - remaining_distance;

                let x_set = (sb.sx - x_range..=sb.sx + x_range).collect::<HashSet<i32>>();

                open_spaces = open_spaces.difference(&x_set).cloned().collect();
            } else {
                continue;
            }
        }
    }
    return open_spaces;
}




fn open_spaces_over_rows(sbs: &Vec<SB>, at_most: i32) -> i32 {
    // rows and number of threads
    let rows = (0..=at_most).collect::<Vec<i32>>();
    let num_threads = 16;

    // split rows into chunks
    let mut chunks = Vec::new();
    let chunk_size = rows.len() / num_threads;
    for i in 0..num_threads {
        let start = i * chunk_size;
        let end = start + chunk_size;
        chunks.push(rows[start..end].to_vec());
    }

    // create threads
    let mut handles = Vec::new();
    for chunk in chunks {
        let sbs = sbs.clone();
        let handle = thread::spawn(move || {
            for (i, row) in chunk.iter().enumerate() {
                // start timer
                let start = std::time::Instant::now();

                let result = open_spaces(&sbs, &row, &at_most);
                if result.len() == 1 {
                    let val = result.iter().next().unwrap();
                    return val * 4000000 + row;
                } 

                // stop timer
                let duration = start.elapsed();
                println!("Row {} of {} took {} seconds", i, chunk.len() - 1, duration.as_secs());
            }
            return 0;
        });
        handles.push(handle);
    }

    // wait for all threads to finish
    for handle in handles {
        let result = handle.join().unwrap();
        if result != 0 {
            return result;
        }
    }

    return 0

}
