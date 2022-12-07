use std::{fs::File, io::Read};

fn read_txt_file(path: &str) -> String {
    let mut file = File::open(path).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn is_contained(s: &str) -> bool {
    
    // split the string into two parts at ','
    let mut parts = s.split(',');
    let part1 = parts.next().unwrap();
    let part2 = parts.next().unwrap();

    // split the first part into two parts at '-'
    let mut parts = part1.split('-');
    let min1 = parts.next().unwrap().parse::<i32>().unwrap();
    let max1 = parts.next().unwrap().parse::<i32>().unwrap();

    // split the second part into two parts at '-'
    let mut parts = part2.split('-');
    let min2 = parts.next().unwrap().parse::<i32>().unwrap();
    let max2 = parts.next().unwrap().parse::<i32>().unwrap();

    // check if the first part is contained in the second part
    if min1 >= min2 && max1 <= max2 {
        return true;
    } else if min2 >= min1 && max2 <= max1 {
        return true;
    } else {
        return false;
    }
}

fn do_overlap(s: &str) -> bool {
    let mut parts = s.split(',');
    let part1 = parts.next().unwrap();
    let part2 = parts.next().unwrap();

    let mut parts = part1.split('-');
    let min1 = parts.next().unwrap().parse::<i32>().unwrap();
    let max1 = parts.next().unwrap().parse::<i32>().unwrap();

    let mut parts = part2.split('-');
    let min2 = parts.next().unwrap().parse::<i32>().unwrap();
    let max2 = parts.next().unwrap().parse::<i32>().unwrap();

    // return true if any of the parts overlap
    if min1 <= max2 && max1 >= min2 {
        return true;
    } else if min2 <= max1 && max2 >= min1 {
        return true;
    } else {
        return false;
    }
}

fn main() {
    let input = read_txt_file("input.txt");
    let mut count = 0;

    for line in input.lines() {
        if is_contained(line) {
            count += 1;
        }
    }

    let mut count2 = 0;
    
    for line in input.lines() {
        if do_overlap(line) {
            count2 += 1;
        }
    }

    println!("{}", count);
    println!("{}", count2);
}
