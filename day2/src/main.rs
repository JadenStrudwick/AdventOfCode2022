use::std::fs::File;
use::std::io::Read;

fn load_input() -> String {
    let mut contents = String::new();
    File::open("input.txt")
        .expect("Failed to open input.txt")
        .read_to_string(&mut contents)
        .expect("Failed to read input.txt");
    contents
}

#[derive(Clone, Copy)]
enum RPS {
    Rock,
    Paper,
    Scissors,
}

fn parse_char1(c: char) -> RPS {
    match c {
        'A' => RPS::Rock,
        'B' => RPS::Paper,
        'C' => RPS::Scissors,
        'X' => RPS::Rock,
        'Y' => RPS::Paper,
        'Z' => RPS::Scissors,
        _ => panic!("Invalid character"),
    }
}

fn parse_char2(c: char) -> Outcomes {
    match c {
        'X' => Outcomes::Loss,
        'Y' => Outcomes::Draw,
        'Z' => Outcomes::Win,
        _ => panic!("Invalid character"),
    }
}


fn rps_outcome(opponent: RPS, player: RPS) -> i32 {
    match (opponent, player) {
        (RPS::Rock, RPS::Rock) => 3,
        (RPS::Rock, RPS::Paper) => 6,
        (RPS::Rock, RPS::Scissors) => 0,
        (RPS::Paper, RPS::Rock) => 0,
        (RPS::Paper, RPS::Paper) => 3,
        (RPS::Paper, RPS::Scissors) => 6,
        (RPS::Scissors, RPS::Rock) => 6,
        (RPS::Scissors, RPS::Paper) => 0,
        (RPS::Scissors, RPS::Scissors) => 3,
    }
}

fn play_bonus(player: RPS) -> i32 {
    match player {
        RPS::Rock => 1,
        RPS::Paper => 2,
        RPS::Scissors => 3,
    }
}

enum Outcomes {
    Win,
    Draw,
    Loss
}

fn get_play(opponent: RPS, required_outcome: Outcomes) -> RPS {
    match required_outcome {
        Outcomes::Win => {
            match opponent {
                RPS::Rock => RPS::Paper,
                RPS::Paper => RPS::Scissors,
                RPS::Scissors => RPS::Rock,
            }
        },
        Outcomes::Draw => {
            match opponent {
                RPS::Rock => RPS::Rock,
                RPS::Paper => RPS::Paper,
                RPS::Scissors => RPS::Scissors,
            }
        },
        Outcomes::Loss => {
            match opponent {
                RPS::Rock => RPS::Scissors,
                RPS::Paper => RPS::Rock,
                RPS::Scissors => RPS::Paper,
            }
        },
    }
}

fn calculate_round(player: RPS, opponent: RPS) -> i32 {
    rps_outcome(opponent, player) + play_bonus(player)
}

fn main() {
    let input = load_input();

    let mut player_score1 = 0;
    for line in input.lines() {
        let opponent = parse_char1(line.chars().nth(0).unwrap());
        let player = parse_char1(line.chars().nth(2).unwrap());
        player_score1 += calculate_round(player, opponent);
    }

    let mut player_score2 = 0;
    for line in input.lines() {
        let opponent = parse_char1(line.chars().nth(0).unwrap());
        let required_outcome = parse_char2(line.chars().nth(2).unwrap());
        let player = get_play(opponent, required_outcome);
        player_score2 += calculate_round(player, opponent);
    }

    println!("Player score 1: {}", player_score1);
    println!("Player score 2: {}", player_score2);
}
