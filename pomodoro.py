import time
import threading

counter = 0

def countdown_timer(duration):
    remaining_time = duration
    try:
        while remaining_time > 0:
            mins, secs = divmod(int(remaining_time), 60)
            print(f"Time remaining: {mins:02}:{secs:02}", end='\r')
            time.sleep(1)
            remaining_time -= 1
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")

def start_timing_work():
    start_time = time.time()
    countdown_thread = threading.Thread(target=countdown_timer, args=(1500,))
    countdown_thread.start()
    countdown_thread.join()
    end_time = time.time()
    return end_time - start_time

def start_timing_rest():
    start_time = time.time()
    countdown_thread = threading.Thread(target=countdown_timer, args=(300,))
    countdown_thread.start()
    countdown_thread.join()
    end_time = time.time()
    return end_time - start_time

def long_break():
    start_time = time.time()
    countdown_thread = threading.Thread(target=countdown_timer, args=(1800,))
    countdown_thread.start()
    countdown_thread.join()
    end_time = time.time()
    return end_time - start_time

def main():
    global counter
    try:
        while True:
            start_input = input("Start timing work? (Y/N): ")
            if start_input.strip().lower() == 'y':
                elapsed_time_work = start_timing_work()
                print(f"Elapsed time: {elapsed_time_work:.0f} seconds")

                break_input = input("Start timing rest? (Y/N): ")
                if (break_input.strip().lower() == 'y' and (counter + 1) % 4 == 0):
                    option = input("Do you wish to take a long break? (Y/N): ")
                    if option.lower() == 'y':
                        elapsed_time_long_break = long_break()
                        print(f"Elapsed time: {elapsed_time_long_break:.0f} seconds")

                if break_input.strip().lower() == 'y':
                    elapsed_time_rest = start_timing_rest()
                    print(f"Elapsed time: {elapsed_time_rest:.0f} seconds")
                    counter += 1
                    print(f"Counter: {counter}")
                else:
                    break
            else:
                break
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    main()