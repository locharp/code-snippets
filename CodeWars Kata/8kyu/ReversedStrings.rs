fn solution(phrase: &str) -> String {
    phrase.chars().rev().collect::<String>()
}

fn main() {
  println!("{}", reverse_string("Hello, world"));
}
