import random
import statistics as stats
import matplotlib.pyplot as plt
import csv

####################  PLEASE CHANGE THIS TO YOUR DESIRED FOLDER PATH FOR THE CODE TO WORK  ####################
folder_path = "C:\\Users\\George\\Documents\\scissors paper stone\\"

# main menu
def main_menu():
    while True:
        print("\n" + "="*50)
        print("ROCK-PAPER-SCISSORS GAME MENU")
        print("="*50)
        print("1. Task 1: Human vs Computer")
        print("2. Task 2: Computer vs Computer (one million times)")
        print("3. Exit")
        print("="*50)
        
        choice = input("Please select an option (1-3): ")
        
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


#save results to text file            
def save_results(filename, content):
    with open(folder_path + filename + '.txt', "w") as f:
        f.write(content)
    print(f"\nResults saved to {folder_path + filename}")

#Task 1
def task1():
    print("\n" + "="*50)
    print("TASK 1: HUMAN VS COMPUTER- 10 matches")
    print("="*50)
    
    choices = ['r', 'p', 's']
    
    # Initialize statistics that persist across sessions
    win = 0
    loss = 0
    tie = 0
    session_count = 0
    
    while True:
        session_count += 1
        print(f"\n--- Starting Session {session_count} ---")
        
        # Play 10 rounds
        with open(folder_path + "match_log.csv", 'w', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow(['Match Number', 'Player Choice', 'Computer Choice', 'Result'])
            for match in range(1, 11):
                print(f'--- Round {match} ---')

                while True:
                    user_choice = input('Rock, paper, or scissors? Please indicate r/p/s: ').lower()
                
                    if user_choice in choices:
                        print('Valid choice... lets battle!')
                        computer_choice = random.choice(choices)
                        print(f'You chose {user_choice}')
                        print(f'Computer chose {computer_choice}')
                    
                        if user_choice == computer_choice:
                            tie += 1
                            print("It's a tie!")
                            writer.writerow([match, user_choice, computer_choice, 'Tie'])
                        elif (
                            (user_choice == 'r' and computer_choice == 's') or
                            (user_choice == 'p' and computer_choice == 'r') or
                            (user_choice == 's' and computer_choice == 'p')):
                            win += 1
                            print('You win! Humans do beat machines sometimes...')
                            writer.writerow([match, user_choice, computer_choice, 'Player Win'])
                        elif (
                            (user_choice == 'r' and computer_choice == 'p') or
                            (user_choice == 'p' and computer_choice == 's') or
                            (user_choice == 's' and computer_choice == 'r')):
                            loss += 1
                            print('Computer wins! Machines are taking over...')
                            writer.writerow([match, user_choice, computer_choice, 'Computer Win'])
                        break
                    else:
                        print('Invalid choice, please choose r, p, or s next time.')
            
        # Display cumulative statistics
        print(f'\n--- Cumulative Statistics After {session_count} Session(s) ---')
        print(f'Wins: {win}, Losses: {loss}, Ties: {tie}')
        
        # Ask if user wants to play another session
        play_again = input('\nWe have finished this session. Play another session? (y/n): ').lower()
        if play_again == 'y':
            print("Great! Let's play another session!")
        elif play_again == 'n':
            print('Thanks for playing! Here are your final cumulative statistics:')
            break
        else:
            print('Invalid choice, defaulting to exit.')
            break
    
    # Final Statistics for Task 1
    total_games = win + loss + tie
    if total_games > 0:
        win_percentage = (win / total_games) * 100
        loss_percentage = (loss / total_games) * 100
        tie_percentage = (tie / total_games) * 100

        print(f'\nTotal games played: {total_games}')
        print(f"Total sessions played: {session_count}")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+")
        print(f"|{'Win %':^10}|{'Loss %':^10}|{'Tie %':^10}|")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+")
        print(f"|{win_percentage:^10.2f}|{loss_percentage:^10.2f}|{tie_percentage:^10.2f}|")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+")

        # Advanced statistics
        mean = stats.mean([win, loss, tie])
        stddev = stats.stdev([win, loss, tie])
        pvar = stats.pvariance([win, loss, tie])
        expected_value = total_games / 3
        chi_2_value = ((win - expected_value) ** 2 / expected_value) + \
                     ((loss - expected_value) ** 2 / expected_value) + \
                     ((tie - expected_value) ** 2 / expected_value)
        degree_of_freedom = 3 - 1
        significance = "not significant (p > 0.05)" if chi_2_value < 5.99 else "significant (p < 0.05)"

        print(f'\nStandard Deviation: {stddev:.3g}')
        print(f'P Variance: {pvar:.3g}')
        print(f'Expected value for each outcome is: {expected_value:.3g}')
        print(f"Chi_2_value: {chi_2_value:.3g}")
        print(f"Deviations are {significance}")

        # Save results from task 1 to text file
        save = input("\nWould you like to save these results to a file? (y/n): ").lower()
        if save == 'y':
            content = (
                "Task 1: Human vs Computer Statistics (Cumulative)\n"
                f"Total sessions: {session_count}\n"
                f"Wins: {win}, Losses: {loss}, Ties: {tie}\n"
                f"Total games played: {total_games}\n"
                f"Win %: {win_percentage:.2f}, Loss %: {loss_percentage:.2f}, Tie %: {tie_percentage:.2f}\n"
                f"Mean: {mean:.3g}\n"
                f"Standard Deviation: {stddev:.3g}\n"
                f"P Variance: {pvar:.3g}\n"
                f"Expected value: {expected_value:.3g}\n"
                f"Chi_2_value: {chi_2_value:.3g}\n")
            filename = input("Enter filename to save: ")
            save_results(filename, content)
        
        # Plotting
        plt.bar(['Wins', 'Losses', 'Ties'], [win, loss, tie], color=['green', 'red', 'blue'])
        plt.xlabel('Outcome')
        plt.ylabel('Number of rounds')
        plt.title(f'RPS Game outcomes (Human vs Computer)\nTotal Sessions: {session_count}')
        plt.show()
    else:
        print("No games played, so no statistics to show.")



#Task 2
def task2():
    print("\n" + "="*50)
    print("TASK 2: COMPUTER VS COMPUTER ONE MILLION TIMES")
    print("="*50)
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        computer1_wins = 0
        computer2_wins = 0
        ties = 0

        user_choice = input("Welcome to rock, paper, scissors between two computers one million times! To start, press y/n: ").lower()
        if user_choice == 'y':
            print("Playing against each other...", end="")
            print('.')
            print('.')
            print('.')  
            print(" Done! Here are the results:")
            
            with open(folder_path + "match_log2.csv", 'w', newline='') as log_file2:
                writer = csv.writer(log_file2)
                writer.writerow(['Match Number', 'Computer 1 Choice', 'Computer 2 Choice', 'Result'])
                for match in range(1, 1_000_001):
                    computer1 = random.choice(choices)
                    computer2 = random.choice(choices)
                    
                    if computer1 == computer2:
                        ties += 1
                        writer.writerow([match, computer1, computer2, 'Tie'])
                    elif (computer1 == 'rock' and computer2 == 'scissors') or \
                        (computer1 == 'paper' and computer2 == 'rock') or \
                        (computer1 == 'scissors' and computer2 == 'paper'):
                        computer1_wins += 1
                        writer.writerow([match, computer1, computer2, 'Computer 1 Win'])
                    else:
                        computer2_wins += 1
                        writer.writerow([match, computer1, computer2, 'Computer 2 Win'])
                        
                print("\nFinal statistics after 1,000,000 matches:")
                print("="*60)
                print(f"Total ties: {ties}")
                print(f"Computer 1 wins: {computer1_wins}")
                print(f"Computer 2 wins: {computer2_wins}")
                break
        elif user_choice == 'n':
            print("Goodbye!")
            return
        else:
            print("Invalid choice, please choose y or n next time.")

    # Basic Statistics for Task 2
    total_games = computer1_wins + computer2_wins + ties
    computer1_percentage = (computer1_wins / total_games) * 100
    computer2_percentage = (computer2_wins / total_games) * 100 
    tie_percentage = (ties / total_games) * 100

    if total_games > 0:
        print(f'\nTotal games played: {total_games}')
        print(f"+{'-'*20}+{'-'*20}+{'-'*20}+")
        print(f"|{'Computer1 win %':^20}|{'Computer2 win %':^20}|{'Tie %':^20}|")
        print(f"+{'-'*20}+{'-'*20}+{'-'*20}+")
        print(f"|{computer1_percentage:^20.2f}|{computer2_percentage:^20.2f}|{tie_percentage:^20.2f}|")
        print(f"+{'-'*20}+{'-'*20}+{'-'*20}+")
    

    # Advanced statistics
        mean = stats.mean([computer1_wins, computer2_wins, ties])
        stddev = stats.stdev([computer1_wins, computer2_wins, ties])
        pvar = stats.pvariance([computer1_wins, computer2_wins, ties])
        var = stats.variance([computer1_wins, computer2_wins, ties])
        expected_value = total_games / 3
        chi_2_value = ((computer1_wins - expected_value) ** 2 / expected_value) + \
                     ((computer2_wins - expected_value) ** 2 / expected_value) + \
                     ((ties - expected_value) ** 2 / expected_value)
        significance = "not significant (p > 0.05)" if chi_2_value < 5.99 else "significant (p < 0.05)"

        print(f'\nMean: {mean:.3g}')
        print(f'Standard Deviation: {stddev:.3g}')
        print(f'P Variance: {pvar:.3g}')
        print(f'Variance: {var:.3g}')
        print(f'Expected value for each outcome is: {expected_value:.3g}')
        print(f'Chi Square Value: {chi_2_value:.3g}')
        print(f"Deviations are {significance}")

    else:
        print("No games played, so no statistics to show.")

    # Save results from task 2 to text file
    save = input("\nWould you like to save these results to a file? (y/n): ").lower()
    if save == 'y':
        content = (
            "Task 2: Computer vs Computer Statistics\n"
            f"Computer 1 wins: {computer1_wins}, Computer 2 wins: {computer2_wins}, Ties: {ties}\n"
            f"Total games played: {total_games}\n"
            f"Computer 1 win %: {computer1_percentage:.2f}, Computer 2 win %: {computer2_percentage:.2f}, Tie %: {tie_percentage:.2f}\n"
            f"Mean: {mean:.3g}\n"
            f"Standard Deviation: {stddev:.3g}\n"
            f"P Variance: {pvar:.3g}\n"
            f"Variance: {var:.3g}\n"
            f"Expected value: {expected_value:.3g}\n"
            f"Chi Square Value: {chi_2_value:.3g}\n"
            f"Significance: {significance}\n")
        filename = input("Enter filename to save: ")
        save_results(filename, content)

    # Plotting
    plt.bar(['Computer 1 Wins', 'Computer 2 Wins', 'Ties'], 
            [computer1_wins, computer2_wins, ties], 
            color=['blue', 'orange', 'green'])
    plt.xlabel('Outcomes')
    plt.ylabel('Matches')
    plt.title('Rock-Paper-Scissors between two computers')
    plt.show()

# Back to main menu
main_menu()