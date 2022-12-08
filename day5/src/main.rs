use std::{fs::File, io::Read};

fn main() {
    // get input.txt contents
    let input = read_txt_file("input.txt");

    // split into lines
    let lines: Vec<&str> = input.split("\n").collect();

    // partition lines into (stacks, instructions) at ""
    let (inst, stack_lines) = lines
        .iter()
        .partition::<Vec<&str>, _>(|&x| x.starts_with("m"));

    // create stacks
    let num_row = stack_lines[stack_lines.len() - 3];
    let num_stacks: usize = num_row.split_whitespace().count();
    let mut stacks: Vec<Vec<char>> = vec![];
    for _ in 0..num_stacks {
        stacks.push(vec![]);
    }

    // fill stacks
    for line in stack_lines[0..stack_lines.len() - 3].iter() {
        for index in (1..line.len()).step_by(4) {
            let c = line.chars().nth(index).unwrap();
            let stack_index = num_row.chars().nth(index).unwrap().to_digit(10).unwrap() as usize;
            if c != ' ' {
                stacks[stack_index - 1].push(c);
            }            
        }
    }

    // reverse stacks
    for stack in stacks.iter_mut() {
        stack.reverse();
    }

    // // execute instructions (part 1)
    // for line in inst.iter() {
    //     let parts = line.split_whitespace().collect::<Vec<&str>>();

    //     let number = parts[1].parse::<i32>().unwrap();
    //     let from = parts[3].parse::<usize>().unwrap();
    //     let to = parts[5].parse::<usize>().unwrap();

    //     //println!("{}: number = {}, from = {}, to = {}", line, number, from, to);
    //     move_item(&mut stacks, number, from, to);
    // }

    // execute instructions (part 2)
    for line in inst.iter() {
        let parts = line.split_whitespace().collect::<Vec<&str>>();

        let number = parts[1].parse::<i32>().unwrap();
        let from = parts[3].parse::<usize>().unwrap();
        let to = parts[5].parse::<usize>().unwrap();

        //println!("{}: number = {}, from = {}, to = {}", line, number, from, to);
        group_move_item(&mut stacks, number, from, to);
    }


    // print stacks
    print_stacks(&stacks);

}

fn read_txt_file(path: &str) -> String {
    let mut file = File::open(path).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
    contents
}

fn print_stacks(stacks: &Vec<Vec<char>>) {
    for (i, stack) in stacks.iter().enumerate() {
        print!("{}: ", i + 1);
        for c in stack {
            print!("{}", c);
        }
        println!();
    }
}

fn move_item(stacks: &mut Vec<Vec<char>>, number: i32, from: usize, to: usize) {
    for _ in 0..number {
        let item = stacks[from - 1].pop().unwrap();
        stacks[to - 1].push(item);
    }
}

fn group_move_item(stacks: &mut Vec<Vec<char>>, number: i32, from: usize, to: usize) {
    let mut items = vec![];
    for _ in 0..number {
        let item = stacks[from - 1].pop().unwrap();
        items.push(item);
    }
    items.reverse();
    for item in items {
        stacks[to - 1].push(item);
    }
}