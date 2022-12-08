use std::{fs::File, io::Read};

fn main() {
    let input = read_txt_file("input.txt");
    let marker = marker_location(&input);
    let message = message_location(&input);
    println!("marker: {}", marker);
    println!("message: {}", message);
}

fn read_txt_file(path: &str) -> String {
    let mut file = File::open(path).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
    contents
}

fn are_all_different(sub: &str) -> bool {
    for i in 0..sub.len() {
        for j in i + 1..sub.len() {
            if sub.chars().nth(i).unwrap() == sub.chars().nth(j).unwrap() {
                return false;
            }
        }
    }
    true
}

fn marker_location(line: &str) -> usize {
    // iterate over the line in chunks of 4
    for i in 0..line.len() - 3 {
        let sub = &line[i..i + 4];
        if are_all_different(sub) {
            return i + 4;
        }
    }
    return line.len();
}

fn message_location(line: &str) -> usize {
    // iterate over the line in chunks of 14
    for i in 0..line.len() - 13 {
        let sub = &line[i..i + 14];
        if are_all_different(sub) {
            return i + 14;
        }
    }
    return line.len();
}