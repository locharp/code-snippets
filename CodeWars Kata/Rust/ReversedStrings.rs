fn reverse_string(phrase: &str) -> String {
  phrase.rsplit("").collect()
}

fn main() {
  println!("{}", reverse_string("Hello, world"));
}
