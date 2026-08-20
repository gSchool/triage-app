from triage import TriageQueue


def display_queue(queue: TriageQueue) -> None:
    cases = queue.active_cases()

    if not cases:
        print("\nThe triage queue is empty.\n")
        return

    print(f"\n{'#':<5} {'ID':<10} {'Severity':<10} Description")
    print("-" * 55)
    for position, case in enumerate(cases, start=1):
        print(f"{position:<5} {case.id:<10} {case.severity.label():<10} {case.description}")
    print()


def submit_case(queue: TriageQueue) -> None:
    description = input("Description: ")
    severity = input("Severity (Critical / High / Medium / Low): ").strip()

    try:
        case = queue.submit(description, severity)
        print(f"\nCase submitted. ID: {case.id} | Severity: {case.severity.label()}\n")
    except ValueError as error:
        print(f"\nError: {error}\n")


def resolve_case(queue: TriageQueue) -> None:
    case_id = input("Enter case ID to resolve: ").strip()

    try:
        case = queue.resolve(case_id)
        print(f"\nResolved — [{case.severity.label()}] {case.description} (ID: {case.id})\n")
    except ValueError as error:
        print(f"\nError: {error}\n")


def main():
    queue = TriageQueue()
    print("=== Triage Application ===\n")

    while True:
        print("1. View queue")
        print("2. Submit case")
        print("3. Resolve case")
        print("4. Quit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            display_queue(queue)
        elif choice == "2":
            submit_case(queue)
        elif choice == "3":
            resolve_case(queue)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
