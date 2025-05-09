import sys

class PokemonBinder:
    def __init__(self):
        """Initialize the binder with empty storage and load previous session if available"""
        self.card_placements = {}  # {pokedex_num: (page, row, col)}
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.rows_per_page = 8
        self.cols_per_page = 8
        
        # Try to load previous session
        try:
            self.load_session()
        except FileNotFoundError:
            pass  # First run, no previous session
    
    def add_card(self, pokedex_num):
        """Add a new Pokemon card to the binder"""
        # Validation checks
        if not self.is_valid_pokedex_num(pokedex_num):
            return "invalid"
        if pokedex_num in self.card_placements:
            return "duplicate"
        
        # Calculate placement
        total_cards = len(self.card_placements) + 1
        page = ((total_cards - 1) // self.cards_per_page) + 1
        position_on_page = (total_cards - 1) % self.cards_per_page
        
        row = (position_on_page // self.cols_per_page) + 1
        col = (position_on_page % self.cols_per_page) + 1
        
        # Store the placement
        self.card_placements[pokedex_num] = (page, row, col)
        self.save_session()
        
        return "added", page, (row, col)
    
    def is_valid_pokedex_num(self, num):
        """Check if the Pokedex number is valid"""
        return isinstance(num, int) and 1 <= num <= self.max_pokedex
    
    def reset_binder(self):
        """Clear all card placements"""
        self.card_placements = {}
        self.save_session()
        return True
    
    def get_collection_stats(self):
        """Return statistics about the current collection"""
        total = len(self.card_placements)
        percentage = (total / self.max_pokedex) * 100
        return total, percentage
    
    def save_session(self):
        """Save current session to a file"""
        with open("pokemon_session.txt", "w") as f:
            for num, (page, row, col) in self.card_placements.items():
                f.write(f"{num},{page},{row},{col}\n")
    
    def load_session(self):
        """Load previous session from file"""
        self.card_placements = {}
        with open("pokemon_session.txt", "r") as f:
            for line in f:
                num, page, row, col = map(int, line.strip().split(','))
                self.card_placements[num] = (page, row, col)
    
    def is_collection_complete(self):
        """Check if all Pokemon have been collected"""
        return len(self.card_placements) == self.max_pokedex

def display_main_menu():
    """Display the main menu options"""
    print("\n=== Pokemon Card Binder Organizer ===")
    print("1. Add a Pokemon card")
    print("2. Reset binder")
    print("3. View collection stats")
    print("4. Exit program")
    print("=" * 35)

def get_user_choice(prompt, valid_options):
    """Get and validate user input"""
    while True:
        try:
            choice = input(prompt).strip()
            if choice in valid_options:
                return choice
            print(f"Invalid option. Please choose from {valid_options}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None

def main():
    binder = PokemonBinder()
    
    while True:
        display_main_menu()
        choice = get_user_choice("Select an option (1-4): ", ["1", "2", "3", "4"])
        
        if choice == "1":
            # Mode 1: Add a Pokemon card
            try:
                pokedex_num = int(input("Enter Pokedex number (1-1025): "))
                result = binder.add_card(pokedex_num)
                
                if result == "invalid":
                    print("Error: Invalid Pokedex number. Must be between 1 and 1025.")
                elif result == "duplicate":
                    page, pos = binder.card_placements[pokedex_num]
                    print(f"This Pokemon (#{pokedex_num}) is already in your binder:")
                    print(f"  Page: {page}, Position: {pos}")
                else:
                    status, page, pos = result
                    print(f"Added Pokemon #{pokedex_num} to your binder:")
                    print(f"  Page: {page}, Position: {pos}")
                    
                    if binder.is_collection_complete():
                        print("\nCongratulations! You have caught them all!")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == "2":
            # Mode 2: Reset binder
            print("\nWARNING: This will permanently erase your current collection!")
            confirm = get_user_choice("Type 'CONFIRM' to reset or 'EXIT' to cancel: ", ["CONFIRM", "EXIT"])
            
            if confirm == "CONFIRM":
                binder.reset_binder()
                print("Binder has been reset. All Pokemon cards have been removed.")
        
        elif choice == "3":
            # Mode 3: View collection stats
            total, percentage = binder.get_collection_stats()
            print("\n=== Collection Statistics ===")
            print(f"Total cards in binder: {total}")
            print(f"Completion: {percentage:.2f}%")
            
            if total > 0:
                print("\nLast 5 added Pokemon:")
                last_five = sorted(binder.card_placements.items(), key=lambda x: x[1])[-5:]
                for num, (page, row, col) in last_five:
                    print(f"  #{num}: Page {page}, Position ({row},{col})")
        
        elif choice == "4":
            # Mode 4: Exit program
            total, _ = binder.get_collection_stats()
            print(f"\nSession ended. You collected {total} Pokemon cards.")
            print("Thank you for using the Pokemon Card Binder Organizer!")
            sys.exit()
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()