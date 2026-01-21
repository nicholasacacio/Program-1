import random
from typing import List, Tuple

class CountryGuessingGame:
    """
    A fun country guessing game where players try to guess a randomly selected country
    from a list of 195 countries in the world.
    """
    
    # List of 195 countries in the world (official English names)
    COUNTRIES = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
        "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde",
        "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
        "Congo", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
        "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador",
        "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini",
        "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany",
        "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
        "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
        "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
        "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos",
        "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
        "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
        "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
        "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
        "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
        "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
        "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
        "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan",
        "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
        "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago",
        "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
        "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    
    def __init__(self, max_attempts: int = 7):
        """Initialize the game with a random country and max attempts."""
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.secret_country = random.choice(self.COUNTRIES)
        self.guessed_countries = set()
        self.game_over = False
        self.won = False
        self.hints_used = 0
        self.max_hints = 3
        
    def display_welcome(self):
        """Display welcome message and game rules."""
        print("\n" + "="*70)
        print(" "*15 + "🌍 WELCOME TO COUNTRY GUESSING GAME 🌍")
        print("="*70)
        print("\n📋 RULES:")
        print("  • A random country will be selected from 195 countries worldwide")
        print("  • You have {} attempts to guess the correct country".format(self.max_attempts))
        print("  • Type your guess and press Enter")
        print("  • You can use up to {} hints during the game".format(self.max_hints))
        print("  • Type 'hint' for a clue, 'quit' to exit, or 'list' to see all countries")
        print("  • The game is NOT case-sensitive")
        print("\n" + "="*70)
        print()
    
    def get_hint(self) -> str:
        """Generate a helpful hint for the secret country."""
        if self.hints_used >= self.max_hints:
            return "❌ You've used all your hints!"
        
        hints = {
            "Afghanistan": "🏔️ Landlocked country in Central Asia, known for Hindu Kush mountains",
            "Albania": "🏞️ Small Balkan country on the Adriatic coast",
            "Algeria": "🏜️ Largest country in Africa by area, located in North Africa",
            "Andorra": "🏔️ Tiny European country in the Pyrenees mountains",
            "Angola": "🌍 African country on the Atlantic coast, formerly Portuguese colony",
            "Argentina": "🌎 South American country, home to tango and Buenos Aires",
            "Australia": "🦘 Island continent known for kangaroos and Great Barrier Reef",
            "Austria": "🎼 European country, famous for classical music and Alpine scenery",
            "Belgium": "🍺 Small European country famous for chocolate and beer",
            "Brazil": "🏝️ Largest country in South America, known for Amazon rainforest",
            "Canada": "🍁 North American country known for Niagara Falls and polar bears",
            "Chile": "📏 Long, narrow South American country along the Pacific coast",
            "China": "🏯 Most populous country in the world, known for Great Wall",
            "Egypt": "🐪 African country, home to the Pyramids and Nile River",
            "France": "🗼 European country known for Eiffel Tower and wine",
            "Germany": "🍺 European country known for beer, engineering, and Oktoberfest",
            "Greece": "🏛️ Mediterranean country known for ancient philosophy and islands",
            "India": "🌶️ South Asian country, second most populous in the world",
            "Indonesia": "🏝️ Southeast Asian archipelago with over 17,000 islands",
            "Italy": "🍝 European country shaped like a boot, known for art and fashion",
            "Japan": "🗾 East Asian island country known for cherry blossoms and technology",
            "Mexico": "🌮 North American country known for ancient Aztec ruins",
            "Netherlands": "🌷 European country, famous for tulips and windmills",
            "Russia": "🐻 Largest country by area, spanning Europe and Asia",
            "Spain": "🎭 European country known for flamenco and tapas",
            "United Kingdom": "🎩 Island nation in Europe, includes England, Scotland, Wales, and Northern Ireland",
            "United States": "🦅 North American country, world's largest economy",
        }
        
        self.hints_used += 1
        hint = hints.get(self.secret_country, 
                        f"📍 This country has {len(self.secret_country)} letters in its name")
        return f"💡 HINT #{self.hints_used}: {hint}"
    
    def get_country_info(self, country: str) -> str:
        """Get information about a country (first letter and length)."""
        if country not in self.COUNTRIES:
            return ""
        
        first_letter = country[0]
        length = len(country)
        revealed = first_letter + "." * (length - 2) + country[-1]
        
        if length <= 2:
            revealed = country
        
        return revealed
    
    def process_guess(self, guess: str) -> Tuple[bool, str]:
        """
        Process user's guess and return (is_correct, message).
        """
        guess = guess.strip().title()
        
        if not guess:
            return False, "❌ Please enter a country name!"
        
        if guess not in self.COUNTRIES:
            return False, f"❌ '{guess}' is not in our country list!"
        
        if guess in self.guessed_countries:
            return False, f"🔄 You already guessed '{guess}'! Try another country."
        
        self.guessed_countries.add(guess)
        
        if guess == self.secret_country:
            self.won = True
            self.game_over = True
            return True, "✅ CORRECT!"
        else:
            self.attempts_left -= 1
            similarity = self._check_similarity(guess)
            
            message = f"❌ Wrong! '{guess}' is not the answer.\n"
            message += f"   Attempts left: {self.attempts_left}/{self.max_attempts}\n"
            
            if similarity == "same_continent":
                message += f"   💡 Close! You're on the right continent!"
            elif similarity == "same_region":
                message += f"   💡 You're in the right region!"
            elif similarity == "close_letters":
                message += f"   💡 The country has similar letters!"
            
            if self.attempts_left == 0:
                self.game_over = True
                self.won = False
            
            return False, message
    
    def _check_similarity(self, guess: str) -> str:
        """Check if guess is similar to secret country in some way."""
        secret = self.secret_country.lower()
        guess_lower = guess.lower()
        
        # Check if they share many letters
        secret_letters = set(secret)
        guess_letters = set(guess_lower)
        common_letters = secret_letters & guess_letters
        
        if len(common_letters) / len(secret_letters) > 0.6:
            return "close_letters"
        
        return ""
    
    def display_status(self):
        """Display current game status."""
        print(f"\n📊 GAME STATUS:")
        print(f"   Country: {self.get_country_info(self.secret_country)}")
        print(f"   Attempts Left: {self.attempts_left}/{self.max_attempts}")
        print(f"   Hints Used: {self.hints_used}/{self.max_hints}")
        print(f"   Guessed Countries: {len(self.guessed_countries)}")
        if self.guessed_countries:
            print(f"   Your guesses: {', '.join(sorted(list(self.guessed_countries)[:5]))}")
            if len(self.guessed_countries) > 5:
                print(f"                ... and {len(self.guessed_countries) - 5} more")
        print()
    
    def display_game_over(self):
        """Display game over message."""
        print("\n" + "="*70)
        if self.won:
            print(" "*20 + "🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"   The country was: {self.secret_country}")
            print(f"   Guesses needed: {self.max_attempts - self.attempts_left}")
            print(f"   Hints used: {self.hints_used}")
        else:
            print(" "*25 + "😔 GAME OVER! 😔")
            print(f"   The correct country was: {self.secret_country}")
            print(f"   Better luck next time!")
        print("="*70 + "\n")
    
    def play(self):
        """Main game loop."""
        self.display_welcome()
        
        while not self.game_over:
            self.display_status()
            user_input = input("🌐 Your guess (or 'hint', 'list', 'quit'): ").strip()
            
            if user_input.lower() == 'quit':
                print(f"\n👋 Game ended. The country was: {self.secret_country}")
                self.game_over = True
                break
            elif user_input.lower() == 'hint':
                print(self.get_hint())
            elif user_input.lower() == 'list':
                print(f"\n📜 Total countries available ({len(self.COUNTRIES)}):")
                for i, country in enumerate(self.COUNTRIES, 1):
                    print(f"{i:3}. {country}", end="  ")
                    if i % 3 == 0:
                        print()
                print("\n")
            else:
                is_correct, message = self.process_guess(user_input)
                print(message)
        
        self.display_game_over()


def main():
    """Main entry point."""
    while True:
        game = CountryGuessingGame(max_attempts=7)
        game.play()
        
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
