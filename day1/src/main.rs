use std::fs::File;
use std::io::Read;
use std::vec::Vec;

fn load_input() -> String {
    let mut contents = String::new();
    File::open("input.txt")
        .expect("Failed to open input.txt")
        .read_to_string(&mut contents)
        .expect("Failed to read input.txt");
    contents
}

fn elf_calories(input: String) -> Vec<i32> {
    let mut elf_calories = Vec::new();
    let mut index = 0;

    for line in input.lines() {
        if line == "" {
            index = index + 1;
        } else {
            let current_calories = line.parse::<i32>().unwrap();
            if elf_calories.len() <= index {
                elf_calories.push(current_calories);
            } else {
                elf_calories[index] = elf_calories[index] + current_calories;
            }
        }
    }

    elf_calories
}

fn main() {
    let input = load_input();
    let mut elves = elf_calories(input);

    // sort the elves by calories descending
    elves.sort_by(|a, b| b.cmp(a));

    println!("Max elf calories: {}", elves[0]);
    println!("Top 3 elf calories: {:?}", &elves[0..3]);
    println!("Sum of top 3 elf calories: {}", &elves[0..3].iter().sum::<i32>());
}