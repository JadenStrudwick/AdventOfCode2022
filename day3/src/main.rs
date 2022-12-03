use std::{fs::File, io::Read};

fn load_input() -> String {
    let mut contents = String::new();
    File::open("input.txt")
        .expect("Failed to open input.txt")
        .read_to_string(&mut contents)
        .expect("Failed to read input.txt");
    contents
}

fn letter_in_both(a: String, b: String) -> char {
    for letter in a.chars() {
        if b.contains(letter) {
            return letter;
        }
    }
    ' '
}

fn letter_in_three(a: String, b: String, c: String) -> char {
    for letter in a.chars() {
        if b.contains(letter) && c.contains(letter) {
            return letter;
        }
    }
    ' '
}

fn split_string_half(s: String) -> (String, String) {
    let half = s.len() / 2;
    let (a, b) = s.split_at(half);
    (a.to_string(), b.to_string())
}

fn scoring(s: char) -> i32 {
    // a through z have 1 through 26 points
    // A through Z have 27 through 52 points
    let mut score = 0;
    if s.is_lowercase() {
        score = s as i32 - 96;
    } else if s.is_uppercase() {
        score = s as i32 - 64 + 26;
    }
    score
}

fn main() {
    let input = load_input();

    // part 1
    let mut total = 0;
    for line in input.lines() {
        let (a, b) = split_string_half(line.to_string());
        let letter = letter_in_both(a, b);
        total += scoring(letter);
    }
    println!("Total: {}", total);

    // part 2
    // get three lines at a time
    let mut total = 0;
    let mut lines = input.lines();

    loop {
        let a = match lines.next() {
            Some(line) => line.to_string(),
            None => break,
        };
        let b = match lines.next() {
            Some(line) => line.to_string(),
            None => break,
        };
        let c = match lines.next() {
            Some(line) => line.to_string(),
            None => break,
        };

        println!("{} {} {}", a, b, c);

        let letter = letter_in_three(a, b, c);
        total += scoring(letter);
    }
    println!("Total: {}", total);

}
